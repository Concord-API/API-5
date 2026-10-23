# Documentação ETL

Como o Ratio transforma decisões judiciais e doutrina no schema `dw` que a API lê. Este documento descreve o repositório `API5-Pipeline` como ele está em 23/10/2026; o código é a fonte de verdade, e os identificadores de decisão (D-xx) remetem à wiki de docs do projeto (`06-operacao/02-decisoes-e-riscos.md`).

## Sumário

1. [Objetivo](#1-objetivo)
2. [Fontes de dados (Extract)](#2-fontes-de-dados-extract)
3. [Transformações (Transform)](#3-transformações-transform)
4. [Carga dos dados (Load)](#4-carga-dos-dados-load)
5. [Ferramentas e tecnologias](#5-ferramentas-e-tecnologias)
6. [Diagrama do fluxo ETL](#6-diagrama-do-fluxo-etl)
7. [Agendamento e automatização](#7-agendamento-e-automatização)
8. [Problemas encontrados e decisões tomadas](#8-problemas-encontrados-e-decisões-tomadas)

## 1. Objetivo

O ETL coleta decisões cíveis do DataJud e artigos de doutrina de fontes abertas, normaliza tudo em um modelo dimensional e gera um arquivo SQL de carga que popula o schema `dw`. A API lê somente o `dw`, para entregar a busca por tema, o score de força e a rastreabilidade de cada número.

O pipeline roda do nosso lado, nunca no servidor do cliente. O schema `dw` é criado pela API por migration (DbUp); o pipeline cria apenas `raw`, `staging` e `etl` no banco de carga e entrega dados já validados e amarrados à versão do schema em que foram gerados.

Tribunais coletados hoje: TJSP, TJRJ, TJMG e STJ, só matéria cível. O STF está no escopo do projeto (decisão de out/2026), mas o pipeline ainda não tem coletor para ele; veja a [seção 8](#8-problemas-encontrados-e-decisões-tomadas).

## 2. Fontes de dados (Extract)

| Fonte | Acesso | Comando | O que é coletado |
| --- | --- | --- | --- |
| DataJud (CNJ) | Endpoint Elasticsearch `_search`, um índice por tribunal: `https://api-publica.datajud.cnj.jus.br/api_publica_{tribunal}/_search`, cabeçalho `Authorization: APIKey <chave>` | `python -m pipeline` | Processos cíveis de `tjsp`, `tjrj`, `tjmg` e `stj`, com todas as movimentações |
| DOAJ | REST, `https://doaj.org/api/search/articles`, sem autenticação | `python -m pipeline.harvest_doaj [--term T] [--year Y]` | Artigos dos 25 termos de busca em `pipeline/data/doaj_terms.json` |
| SciELO | API ArticleMeta, `https://articlemeta.scielo.org/api/v1/article/`, sem autenticação | `python -m pipeline.harvest_scielo [--issn I]` | Artigos dos 6 ISSNs em `pipeline/data/scielo_issns.json` |
| OAI-PMH | Endpoints Dublin Core (`oai_dc`), sem autenticação | `python -m pipeline.harvest_oai [--repository R]` | Artigos dos 48 endpoints de revistas em `pipeline/data/oai_sources.json` (47 habilitados; um está desabilitado porque o endpoint exige acesso) |
| STF | Painel de decisões do Corte Aberta (CSV), fora do DataJud | não implementado | Veja a seção 8 |

O DataJud é a única fonte de decisões; as outras três alimentam a dimensão de doutrina. Os coletores de doutrina são comandos separados e não são executados por `python -m pipeline`; o comando principal apenas transforma o que já estiver em `raw.doctrine_article`.

### Como o DataJud é consultado

A coleta é um recorte deliberado, nunca "tudo". A consulta enviada a cada tribunal filtra na origem:

| Filtro | Valor |
| --- | --- |
| Classe processual | `classe.codigo` nas classes cíveis da TPU (`pipeline/data/tpu.json`). Para o STJ, as classes recursais `1032`, `11881`, `1137` e `11956` |
| Assunto | `assuntos.codigo` nos códigos de uma área da TPU |
| Decisão | `movimentos.codigo` nos 6 códigos de decisão conferidos (veja a [seção 3.2](#32-resultado-das-movimentações)) |
| Exclusão | qualquer assunto penal (`assuntos_penal` na TPU) é removido com `must_not` |

Cada tribunal é consultado uma vez por área da TPU, com uma cota de documentos lidos por tribunal e área:

| Grupo | Códigos de área da TPU | Cota por tribunal e área |
| --- | --- | --- |
| Núcleo | `899`, `1156`, `8826`, `9985`, `14`, `195` | 700 |
| Apoio | `12480`, `7724`, `10110`, `864`, `9633`, `12734`, `12775` | 250 |

Isso limita uma execução a 5.950 documentos lidos por tribunal (6 × 700 + 7 × 250), ou 23.800 nos quatro tribunais. A cota conta documentos lidos, não só os novos.

Comportamento da coleta (`pipeline/datajud.py`):

- Páginas de 100 documentos, ordenadas por `@timestamp` decrescente e paginadas com `search_after`; timeout de 180 s por requisição.
- Em erro de rede, HTTP 429 ou 5xx, a requisição é repetida até 5 vezes, esperando `min(30, 3 × tentativa)` segundos. Se todas as tentativas falham, a coleta daquele tribunal e área para na execução e as linhas já inseridas são mantidas.
- A coleta também para quando a cota é atingida, quando uma página volta sem documentos ou após 5 páginas seguidas sem nenhum documento novo.
- Há um commit após cada tribunal e área, então uma execução interrompida preserva o que já coletou.
- Cada documento é gravado uma só vez em `raw.datajud_case` (`UNIQUE (source, payload_hash)`, em que o hash é o SHA-256 do `_id` do DataJud), então coletar de novo nunca duplica um processo.

### Reforço de temas com poucos julgados

`python -m pipeline --top-up` faz uma segunda coleta, depois da primeira carga, para os assuntos dos temas com menos de 5 processos julgados. Lê até 300 documentos por tribunal para esses assuntos, recarrega e imprime quantos temas têm 5 ou mais processos julgados antes e depois.

### Coletores de doutrina

Os três coletores gravam o payload do artigo como JSONB em `raw.doctrine_article`, de forma idempotente (`UNIQUE (source, payload_hash)`). Eles esperam entre as requisições (0,15 s no DOAJ, 0,3 s no OAI-PMH, 0,05 s no SciELO), repetem até 4 vezes em erro de rede, 429 ou 5xx, e fazem commit após cada termo, revista ou repositório.

### Frequência e autenticação

| Item | Valor |
| --- | --- |
| Frequência | Sob demanda. Alguém roda os comandos quando o time decide atualizar a base |
| Autenticação do DataJud | A chave pública do CNJ, informada na variável de ambiente `DATAJUD_API_KEY` |
| Demais fontes | Sem autenticação |
| Credenciais | Só por variável de ambiente; o `.env` é lido com `override=False` e nunca é versionado |

## 3. Transformações (Transform)

Tudo abaixo roda em `pipeline/run.py`, nesta ordem: achatar, carregar dimensões e fato, ligar doutrina, montar temas, semear configurações, gerar narrativas, checar integridade e gerar o arquivo de carga.

### 3.1 Achatamento dos processos do DataJud

`pipeline/transform.py` transforma cada processo cru em uma linha de `staging.case_event` por movimentação. A tabela `staging.case_event` é esvaziada e refeita a partir do `raw` a cada execução.

| Regra | Comportamento |
| --- | --- |
| Sem `numeroProcesso` | O processo é descartado |
| Assunto penal | O processo inteiro é descartado |
| Classe fora das permitidas para o tribunal | O processo é descartado |
| Movimentação sem data, código ou nome | A movimentação é ignorada (o nome usa uma tabela de código para nome quando o payload não traz) |
| Datas | ISO 8601 (com `Z`) e `yyyyMMddHHmmss` são lidas; uma data que não dá para ler vira vazio, nunca erro |
| Grau (`grau`) | `G1` → `First`, `G2` → `Second`, `JE` → `SpecialCourt`, `TR` → `AppealPanel`, `GRAU_UNICO` e `SUP` → `Superior`, `GR` → `Second`. Um valor fora do mapa passa como veio |
| Órgão julgador do STJ | O órgão que decidiu cada movimentação é resolvido para um colegiado: um órgão nomeado (`Corte Especial`, `Primeira Turma`, `Segunda Seção`...) é reconhecido pelo texto, depois de corrigir problema de codificação; senão, o nome do ministro é buscado na composição dos colegiados em `pipeline/data/stj_panels.json`, que tem datas de vigência por ministro |

### 3.2 Resultado das movimentações

O DataJud não publica o resultado de um julgamento como campo; ele só existe como movimentação. Por isso o pipeline conta na métrica somente os códigos de movimentação que foram conferidos contra a tabela oficial da TPU:

| Código | Nome | Resultado | Polaridade (de quem é a pretensão) |
| --- | --- | --- | --- |
| 219 | Procedência | Granted | autor (`pretensao_autor`) |
| 220 | Improcedência | Denied | autor |
| 221 | Procedência em Parte | PartiallyGranted | autor |
| 237 | Provimento | Granted | recorrente (`pretensao_recorrente`) |
| 238 | Provimento em Parte | PartiallyGranted | recorrente |
| 239 | Não-Provimento | Denied | recorrente |

Todo outro código entra em `dim_movement` como `Neutral` com `code_verified = false`. Movimentações neutras contam para volume e série temporal, nunca para percentual de resultado. Resultados do lado do autor e do lado do recorrente não podem ser somados, por isso cada código conferido carrega uma polaridade.

### 3.3 Dimensões e fato

`load_dimensions` carrega, nesta ordem:

1. Dados de referência: tribunais (`TJSP`, `TJRJ`, `TJMG`, `STJ`) e os resultados de decisão, semeados a partir de listas no código. O STF só será semeado quando tiver dado.
2. Movimentações conferidas, com resultado e polaridade; depois as classes processuais, os órgãos julgadores e as demais movimentações (neutras).
3. `dim_case`, uma linha por número de processo, com tribunal, classe, grau, nível de sigilo e data de ajuizamento.
4. `dim_subject` (nome e código TPU do assunto, com a área da TPU), uma trava que aborta se algum assunto penal passou, e `bridge_case_subject`.
5. `dim_date`, um calendário diário de 01/01/1940 até o fim do ano seguinte.
6. `fact_case_event`, uma linha por movimentação de processo, com chave `numero_do_processo|codigo_da_movimentacao|data_hora` e `ON CONFLICT DO NOTHING`, então recarregar nunca infla a contagem (D-13).
7. O número do processo formatado como `NNNNNNN-DD.AAAA.J.TR.OOOO` e o link para a página do próprio tribunal: link direto do e-SAJ para o TJSP (a consulta de primeiro grau para `First` e `SpecialCourt`, a de segundo grau para `Second` e `AppealPanel`) e o portal de consulta do tribunal para TJRJ, TJMG e STJ.
8. Os artigos de doutrina em `dim_doctrine`.

### 3.4 Doutrina

O payload de cada coletor tem um formato diferente, então `pipeline/doctrine_transform.py` extrai um registro comum: título, autores, revista, ano, DOI, URL do artigo e área do assunto.

| Regra | Comportamento |
| --- | --- |
| Limpeza de texto | Entidades HTML são decodificadas até três vezes (algumas fontes vêm com codificação dupla) e os espaços são colapsados |
| DOI | O prefixo `doi.org` ou `doi:` é removido e o valor vai para minúsculas; o que não começa com `10.` é descartado |
| Duplicados | Um artigo é mantido uma vez por DOI e uma vez por (fonte, URL), começando pelo coletado mais recentemente |
| Carga | Artigos com DOI entram por upsert pelo DOI; os demais por (fonte, URL). Um DOI descoberto depois é anexado à linha existente |

A doutrina é ligada aos assuntos por `pipeline/doctrine_link.py`, com uma regra híbrida: o título do artigo e o nome do assunto precisam estar próximos no espaço de embeddings (similaridade de cosseno de pelo menos 0,55, os 10 assuntos mais próximos por artigo) **e** compartilhar palavras distintivas (pelo menos duas quando o nome do assunto tem duas ou mais, comparando prefixos de 7 letras, ignorando stopwords e palavras com menos de 4 letras). Cada ligação grava `similarity`, `link_method` (`embedding_cosine+lexical`) e `embedding_model`, então pode ser auditada e apertada depois. A tabela é refeita a cada execução. Os embeddings vêm do modelo `paraphrase-multilingual-MiniLM-L12-v2`, executado localmente em CPU, sem chave de API.

### 3.5 Temas

Um tema é uma camada acima do assunto bruto da TPU, para que o produto possa voltar à granularidade de assunto se o agrupamento for descartado.

- Os assuntos listados em `pipeline/data/theme_merge_groups.json` são fundidos no tema curado com o nome ali definido.
- Todo outro assunto vira um tema próprio (1:1). Nomes de tema repetidos ganham um sufixo numérico.
- A área do direito vem de `pipeline/data/theme_area_rules.json`: primeiro o nome exato (109 entradas), depois regras por palavra-chave (14 áreas) sobre o nome sem acentos.
- A `theme_key` pública vem de `etl.theme_registry`, que atribui uma chave na primeira vez que vê um nome e nunca a reaproveita, então as chaves se mantêm estáveis entre cargas (D-31).
- A área oficial da TPU de um tema é a área TPU mais frequente entre seus assuntos. Uma trava aborta se um tema ficar sem assunto.

Novos candidatos a fusão são propostos, não decididos, por `python -m pipeline.propose`: ele agrupa nomes de assunto (aglomerativo, distância de cosseno, limiar 0,20) e imprime os grupos ainda não curados, ordenados por volume de processos. Uma pessoa lê os grupos e registra a decisão pelo nome do assunto em `theme_merge_groups.json`. Assunto sem decisão continua 1:1.

### 3.6 Configurações, sinônimos e narrativas

- `dw.strength_config` é semeada com a versão de metodologia `1.0`, cobertura de 5 tribunais, mínimo de 10 julgados para graduar, divergência de 20 pontos e mínimo de 5 julgados para divergência.
- `dw.search_synonym` é refeita a partir de `pipeline/data/search_synonyms.json` (14 entradas).
- `dw.theme_narrative` é gerada por template: as views materializadas são atualizadas e cada tema recebe uma frase de abertura e um corpo compostos com números do `dw`. Abaixo do mínimo de julgados, mostra a contagem em vez de percentual (D-32). Nenhum modelo de linguagem é chamado em ponto algum da carga (D-37).

### 3.7 Verificações de integridade

`pipeline/integrity.py` roda 9 verificações e aborta a execução com `IntegrityError` se qualquer consulta devolver uma linha. Nesse caso, nenhum arquivo de carga é escrito.

| Verificação | O que pega |
| --- | --- |
| fact without date | Um fato com `date_sk` vazio |
| penal subject | Um assunto penal da TPU dentro de `dim_subject` |
| theme without subject | Um tema sem linha em `bridge_theme_subject` |
| theme key outside the registry | Um tema cuja chave e nome não estão em `etl.theme_registry` |
| decision movement not verified | Uma movimentação que conta na métrica mas tem `code_verified = false` |
| theme summary diverging from the facts | `theme_summary.judged_case_count` diferente de uma recontagem feita direto do fato |
| provenance diverging from the facts | Contagens de `data_provenance` diferentes das linhas de fato e de doutrina |
| judged theme without text | Um tema com processos julgados e sem narrativa |
| doctrine link without score or method | Uma ligação sem `similarity`, `link_method` ou `embedding_model`, ou abaixo do limiar |

## 4. Carga dos dados (Load)

### Modelo de destino

O destino é o PostgreSQL 16 (locale ICU `pt-BR`, extensões `unaccent` e `pg_trgm`). A definição de referência do `dw` são os scripts de migration da API; o pipeline mantém uma cópia do schema em `tests/fixtures/dw_schema.sql` para os testes (atualizada por `scripts/refresh_test_schema.py`), que lista:

| Tipo | Objetos |
| --- | --- |
| Fato | `fact_case_event`, grão: uma movimentação de um processo |
| Dimensões | `dim_case`, `dim_case_class`, `dim_court`, `dim_date`, `dim_decision_outcome`, `dim_doctrine`, `dim_judging_body`, `dim_movement`, `dim_subject`, `dim_theme` |
| Pontes | `bridge_case_subject`, `bridge_subject_doctrine`, `bridge_theme_subject` |
| Tabelas de apoio | `search_synonym`, `strength_config`, `theme_narrative` |
| Views materializadas | `case_current_result`, `data_provenance`, `theme_outcome_distribution`, `theme_strength`, `theme_summary` |
| View | `theme_provenance` |

Schemas de trabalho no banco de carga: `raw` (payloads originais, mantidos para que recarregar nunca exija voltar às fontes), `staging` (registros achatados) e `etl` (o registro de temas). Só o `dw` vai para o destino.

### Dois passos: montar e exportar

1. **Montar, no banco de carga.** O pipeline grava por upsert (`ON CONFLICT`), então rodar duas vezes com os mesmos dados não muda nada. Ele se recusa a começar se o schema `dw` não existir: suba a API contra esse banco primeiro. Faz commit antes de exportar, porque o `pg_dump` abre a própria conexão.
2. **Exportar um arquivo de carga.** `pipeline/load_file.py` escreve um arquivo SQL, por padrão `ratio-load.sql` (caminho em `LOAD_FILE_PATH`), com esta estrutura:

| Parte | Finalidade |
| --- | --- |
| `BEGIN;` | A carga inteira é uma transação: se algo falhar, o destino mantém os dados anteriores |
| Trava de versão | Compara a última migration aplicada no destino (`migrations.schema_versions`) com a versão para a qual o arquivo foi gerado, e dá erro se forem diferentes ou se a API nunca migrou o banco |
| `TRUNCATE` de toda tabela do `dw` com `RESTART IDENTITY CASCADE` | Recarga completa, sem merge |
| `pg_dump` só de dados do schema `dw` | Os dados em si |
| `REFRESH MATERIALIZED VIEW` de cada view | Em ordem de dependência, calculada a partir do catálogo |
| `COMMIT;` | |

Ao lado dele, o pipeline escreve `ratio-load.manifest.json`, com a versão do schema, a data de extração (o maior `extracted_at` do fato), a contagem de linhas de cada tabela do `dw`, o número de processos decididos em mais de um tribunal e o número de decisões do STJ, contadas na métrica, cujo órgão julgador não pôde ser mapeado para turma, seção ou Corte Especial.

### Publicação de uma carga

`python -m pipeline.publish` empacota a carga para entrega. Exige o manifesto e uma árvore git limpa, e se recusa a publicar uma tag que já existe.

| Saída | Conteúdo |
| --- | --- |
| Tag | `load-AAAAMMDD-<versão do schema>`, a partir da data de extração e da versão do schema |
| Arquivos | `ratio-<tag>.zip` com o arquivo SQL, o `.sha256` dele e o manifesto |
| Notas da release | Versão do schema, data de extração, commit do pipeline e a contagem de linhas por tabela |
| Destino | Uma release do GitHub em `Concord-API/API5-Pipeline`, criada com a CLI `gh` |

### Aplicação de uma carga

Com o banco de destino já migrado pela API (suba a API contra ele uma vez):

```bash
psql -d <banco> -v ON_ERROR_STOP=1 -f ratio-load.sql
```

Uma carga de amostra pode ser gerada a partir de dados de fixture com `python -m pipeline.sample`, num banco vazio. É o que o CI usa para provar que a API serve o que o pipeline produz.

## 5. Ferramentas e tecnologias

| Área | Ferramenta |
| --- | --- |
| Linguagem | Python 3.12 |
| Acesso ao banco | `psycopg2-binary` 2.9.10 (inserção em lote com `execute_values`), `pg_dump` e `psql` |
| HTTP | `requests` 2.32.3, com retry e espera entre tentativas |
| Configuração | `python-dotenv` 1.2.3 (`.env`) |
| Embeddings | `sentence-transformers` 5.1.2 (em `requirements-nlp.txt`), modelo `paraphrase-multilingual-MiniLM-L12-v2`, local em CPU |
| Clusterização | `scikit-learn` 1.8.0 e `numpy` 2.3.5 |
| Destino | PostgreSQL 16, schema `dw` criado pela API .NET 10 (DbUp) |
| Testes e qualidade | `pytest` 8.3.4, `pytest-cov`, `testcontainers[postgres]` 4.9.0, `ruff` 0.8.4, SonarQube Cloud |
| Automação | GitHub Actions, CLI `gh` para as releases |

As dependências de embeddings só são necessárias quando há artigos de doutrina para ligar; sem eles, o encoder nunca é chamado, e é por isso que o CI instala só o `requirements.txt`.

## 6. Diagrama do fluxo ETL

```mermaid
flowchart TD
    DJ["API do DataJud<br/>TJSP, TJRJ, TJMG, STJ"] -->|"python -m pipeline"| RAWC[("raw.datajud_case")]
    DO["DOAJ, SciELO, OAI-PMH"] -->|"python -m pipeline.harvest_*"| RAWD[("raw.doctrine_article")]
    RAWC -->|"achatar"| STGC[("staging.case_event")]
    RAWD -->|"extrair"| STGD[("staging.doctrine_article")]
    STGC --> DW[("dw: dimensões, fato, pontes")]
    STGD --> DW
    DW --> TH["Ligações de doutrina, temas,<br/>configurações de força, narrativas"]
    TH --> IC{"9 verificações de integridade"}
    IC -->|"qualquer violação"| STOP["Aborta: sem arquivo de carga"]
    IC -->|"limpo"| LF["ratio-load.sql + manifesto"]
    LF --> REL["Release do GitHub<br/>zip + sha256"]
    REL --> DEST[("Banco de destino<br/>migrado pela API")]
```

## 7. Agendamento e automatização

A carga é manual por decisão (D-17): não há agendador, nem contêiner de ETL em produção, nem alarme para execução perdida. A data de extração é exibida aos usuários, e as verificações de integridade impedem que uma base inconsistente seja exportada.

### Configuração

| Variável | Finalidade | Padrão |
| --- | --- | --- |
| `DATABASE_URL` | Banco de carga, por exemplo `postgresql://usuario:senha@localhost:5432/ratio` | nenhum, obrigatória |
| `DATAJUD_API_KEY` | Chave pública do DataJud; obrigatória, exceto com `--skip-harvest` sem `--top-up` | nenhum |
| `LOAD_FILE_PATH` | Onde o arquivo de carga é escrito | `ratio-load.sql` |

### Comandos

| Comando | O que faz |
| --- | --- |
| `python -m pipeline.harvest_doaj`, `harvest_scielo`, `harvest_oai` | Coletam doutrina em `raw.doctrine_article`. Opcionais e seguros de repetir |
| `python -m pipeline` | Coleta do DataJud, transforma, carrega, checa a integridade e escreve o arquivo de carga e o manifesto |
| `python -m pipeline --skip-harvest` | Refaz tudo a partir do que já está no `raw`, sem chamar o DataJud |
| `python -m pipeline --top-up` | Como acima, mais uma segunda coleta para temas com menos de 5 julgados |
| `python -m pipeline.propose` | Lista novos grupos de assunto para revisão; não escreve nada no banco |
| `python -m pipeline.publish` | Empacota a carga e cria a release no GitHub |
| `python -m pipeline.sample` | Gera `ratio-sample.sql` a partir da fixture, num banco vazio |

Erros (variável ausente, schema `dw` ausente, verificação de integridade falha) vão para o stderr e terminam com status 1. Quando o coletor parecer travado no Windows, rode o Python sem buffer com `python -u`.

### Ordem de execução

1. Suba a API contra o banco de carga, para que ela crie o `dw` e o histórico de migrations.
2. Opcionalmente, rode os coletores de doutrina.
3. Rode `python -m pipeline`, com `--top-up` quando os temas com poucos julgados importarem.
4. Rode `python -m pipeline.propose` e registre os novos grupos em `theme_merge_groups.json`; depois rode `python -m pipeline --skip-harvest` de novo.
5. Rode `python -m pipeline.publish` e aplique o arquivo no destino.

### Automação que existe

O workflow `Pipeline CI` (`.github/workflows/ci.yml`) roda em pull requests para `main` e para branches `us*`, e em pushes na `main`:

| Job | O que verifica |
| --- | --- |
| `tests` | `ruff check` e `pytest` com cobertura. Os testes sobem um PostgreSQL descartável via Testcontainers; o HTTP é sempre simulado |
| `quality` | Quality gate do SonarQube Cloud, obrigatório no caminho para a `main` |
| `compatibility` | Compila a API, deixa que ela migre dois bancos vazios, monta a amostra com o pipeline, aplica no segundo banco e confere que `/health/ready` responde `Pronto` e que `/api/themes` devolve temas |

## 8. Problemas encontrados e decisões tomadas

| Problema | Decisão |
| --- | --- |
| O DataJud não tem campo de resultado do julgamento | O resultado é lido das movimentações, e só 6 códigos conferidos contra a tabela oficial da TPU contam na métrica; todo outro código é neutro. Na dúvida, o código fica de fora (D-10) |
| Os códigos de resultado têm polaridades diferentes: 219, 220 e 221 se referem à pretensão do autor, 237, 238 e 239 à do recorrente | Cada movimentação conferida carrega uma polaridade, e as duas nunca são somadas |
| Só a similaridade de embeddings ligou artigos de "moral" (filosofia) a "dano moral" (o instituto jurídico), pontuando acima dos corretos | A doutrina só é ligada quando a similaridade e a coincidência lexical valem juntas; a cobertura cai, que é a direção mais segura, porque artigo sem ligação é recuperável e artigo ligado errado não é (D-16) |
| A clusterização de nomes de assunto mistura assuntos sem relação | A clusterização só propõe; uma pessoa cura pelo nome do assunto, e assunto sem curadoria continua 1:1 |
| Identidade de tema mudando entre cargas quebraria ligações e favoritos | Um registro persistente (`etl.theme_registry`) dá a cada tema uma chave pública estável (D-31) |
| Um processo pode ser decidido num tribunal estadual e no STJ | O manifesto conta processos decididos em mais de um tribunal, e a regra é que esse processo conta uma vez, no tribunal da última decisão (D-41) |
| As decisões do STJ vêm com o ministro ou um órgão interno, não com o colegiado | O colegiado é derivado do nome do órgão ou das datas de composição do ministro em `stj_panels.json`; o manifesto informa os órgãos que não puderam ser mapeados |
| Um percentual numérico sobre poucas decisões engana | Abaixo do mínimo de julgados, os textos mostram a contagem em vez do percentual (D-32) |
| Um modelo de linguagem na carga deixaria os números inverificáveis | Nenhum modelo é chamado na carga automática; as narrativas são templates sobre números do `dw`, e todo número vem de um `SELECT` (D-37) |
| Matéria penal está fora do escopo do produto | Assuntos penais são excluídos na consulta, descartados ao achatar, travados na carga e conferidos no final |
| Carregar num banco que a API não migrou corromperia ou falharia no meio | O pipeline se recusa a começar sem o `dw`, e o arquivo de carga se recusa a rodar em outra versão de schema |
| Agendar a carga exigiria infraestrutura no servidor do cliente | A carga é manual, roda do nosso lado e segue como um arquivo validado (D-17) |
| O STF não está no DataJud (não é subordinado ao CNJ) | A única fonte aberta encontrada é o painel de decisões do Corte Aberta, um CSV sem número CNJ do processo e sem código de assunto da TPU. O STF seria uma instância à parte, e a regra da D-41 não o alcança. O escopo inclui o STF, mas ele precisa de um coletor novo, do mapeamento do texto de andamento para resultado e do assunto para tema, e da semeadura em `dim_court` quando houver dado. Detalhes em `03-dados/07-fonte-stf.md` da wiki de docs |
