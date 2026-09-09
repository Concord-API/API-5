# DoR detalhado e Critérios de Aceitação
 
### US-01 — Busca por tema em linguagem natural · Must · 8 SP
 
> Como **advogado**, quero digitar o tema do meu caso em linguagem natural e receber temas jurídicos apurados — não uma lista de processos — para descobrir como aquilo vem sendo decidido sem garimpar acórdão por acórdão.
 
**Regras de negócio**
 
- A busca aceita texto livre em português e retorna **temas**, nunca processos individuais.
- A busca é full-text no Postgres, tolerante a ausência de acento e a erro de digitação.
- Busca sem resultado retorna estado vazio explicativo, não lista vazia.
- Consulta com menos de 3 caracteres não é submetida.
**Dados a armazenar**
 
- `termo de busca`: texto, obrigatório, mínimo 3 caracteres.
- `identificador do tema`: identificador, obrigatório.
- `título do tema`: texto, obrigatório.
- `vetor de busca`: índice full-text em português, gerado na carga.
- Grão do resultado: um registro por tema.
**Mensagens**
 
- Confirmação: "N temas encontrados para «termo»."
- Erro: "Digite ao menos 3 caracteres para buscar."
- Aviso: "Nenhum tema encontrado para «termo» no escopo TJSP, TJRJ e TJMG."
**Protótipo** — tela de busca com campo único e lista de resultados.
 
**Critérios de aceitação**
 
```
Cenário: Buscar um tema existente
Dado que existem temas apurados na base
Quando o advogado digitar "juros abusivos em contrato bancário"
Então o sistema exibirá uma lista de temas jurídicos, e não de processos
 
Cenário: Buscar com erro de digitação
Dado que existe o tema "Dano moral por negativação indevida"
Quando o advogado digitar "negativacao indevda"
Então o sistema retornará esse mesmo tema
 
Cenário: Buscar termo sem correspondência
Dado que não há tema correspondente na base
Quando o advogado buscar "contrato de arrendamento de satélite"
Então o sistema exibirá "Nenhum tema encontrado para «...» no escopo TJSP, TJRJ e TJMG"
```
 
---
 
### US-02 — Ordenação por firmeza do entendimento · Must · 2 SP
 
> Como **advogado**, quero que os resultados venham ordenados pela firmeza do entendimento, e não por relevância textual, para encontrar primeiro o que me serve para sustentar a tese.
 
**Regras de negócio**
 
- A ordenação padrão da lista é pela **nota de firmeza**, decrescente.
- Em caso de empate na nota, desempata pelo maior volume de decisões.
- A relevância textual é usada apenas para filtrar quais temas entram na lista, nunca para ordená-la.
**Dados a armazenar**
 
- `nota de firmeza`: inteiro de 0 a 100, opcional (vazio quando abaixo do limiar).
- `volume de decisões`: inteiro, obrigatório.
**Mensagens**
 
- Confirmação: "Ordenado por firmeza do entendimento."
- Erro: não se aplica.
- Aviso: "Alguns temas não possuem nota calculada e aparecem ao final da lista."
**Protótipo** — lista de resultados com indicador de ordenação visível.
 
**Critérios de aceitação**
 
```
Cenário: Ordenação padrão da lista
Dado que a busca retornou temas com notas 82, 47 e 91
Quando a lista for exibida
Então os temas aparecerão na ordem 91, 82, 47
 
Cenário: Empate na nota de firmeza
Dado que dois temas possuem nota 70, com 400 e 120 decisões
Quando a lista for exibida
Então o tema com 400 decisões aparecerá primeiro
```
 
---
 
### US-04 — Filtros por tribunal, período, grau e força mínima · Must · 5 SP
 
> Como **advogado**, quero filtrar os resultados por tribunal, período, grau e força mínima, vendo quantos processos cada tribunal tem, para reduzir a lista ao recorte do meu caso.
 
**Regras de negócio**
 
- Filtros disponíveis: tribunal (TJSP, TJRJ, TJMG), período por ano, grau e força mínima da nota.
- Cada opção de tribunal exibe a **contagem de processos** correspondente.
- Filtros são combináveis e refletidos na lista imediatamente.
- Combinação sem resultado mostra estado vazio explicativo e mantém os filtros aplicados visíveis.
**Dados a armazenar**
 
- `tribunal`: lista pré-definida (TJSP, TJRJ, TJMG), obrigatório.
- `ano da decisão`: inteiro de 4 dígitos, obrigatório.
- `grau`: lista pré-definida, obrigatório.
- `força mínima`: inteiro de 0 a 100, opcional.
- Origem: consulta OLAP pré-agregada por tema, ano e tribunal.
**Mensagens**
 
- Confirmação: "N temas com os filtros aplicados."
- Erro: "Período inválido: o ano inicial deve ser anterior ao final."
- Aviso: "Nenhum tema atende a essa combinação de filtros. Remova um filtro para ampliar o resultado."
**Protótipo** — painel lateral de filtros com contadores por tribunal.
 
**Critérios de aceitação**
 
```
Cenário: Filtrar por tribunal
Dado que a lista exibe temas dos três tribunais
Quando o advogado marcar apenas TJSP
Então a lista exibirá somente temas com decisões do TJSP
E cada tribunal exibirá a quantidade de processos ao lado do nome
 
Cenário: Combinação de filtros sem resultado
Dado que o advogado filtrou por TJMG, ano 2015 e força mínima 90
Quando nenhum tema atender à combinação
Então o sistema exibirá "Nenhum tema atende a essa combinação de filtros"
E manterá os filtros aplicados visíveis na tela
 
Cenário: Período invertido
Dado que o advogado informou o período de 2024 a 2019
Quando aplicar o filtro
Então o sistema exibirá "Período inválido: o ano inicial deve ser anterior ao final"
```
 
---
 
### US-05 — Separação de teses distintas sob o mesmo assunto CNJ · Should · 13 SP
 
> Como **advogado**, quero que a busca separe teses distintas que hoje caem no mesmo assunto do CNJ, para encontrar a tese do meu caso e não a categoria dela.
 
**Regras de negócio**
 
- Um assunto CNJ pode originar **mais de um tema** na base.
- Cada tema resultante exibe o assunto CNJ de origem, para o usuário entender a separação.
- A relação entre assunto CNJ e tema é N:N e vive em **tabela-ponte** no DW.
- O critério de separação usado é registrado e exibível junto ao tema.
**Dados a armazenar**
 
- `código do assunto CNJ`: texto, obrigatório.
- `descrição do assunto CNJ`: texto, obrigatório.
- `identificador do tema`: identificador, obrigatório.
- `critério de separação`: texto, obrigatório.
- Tabela-ponte entre tema e assunto CNJ, grão: um registro por par tema × assunto CNJ.
**Mensagens**
 
- Confirmação: "Este assunto do CNJ contém N teses distintas."
- Erro: "Não foi possível separar as teses deste assunto. Exibindo o assunto agrupado."
- Aviso: "Este tema compartilha o assunto CNJ «...» com outras teses."
**Protótipo** — resultado com etiqueta do assunto CNJ de origem em cada tema.
 
**Critérios de aceitação**
 
```
Cenário: Assunto CNJ com mais de uma tese
Dado que o assunto CNJ "Contratos bancários" agrupa 3 teses distintas
Quando o advogado buscar por esse assunto
Então o sistema exibirá 3 temas separados
E cada um exibirá o assunto CNJ de origem
 
Cenário: Assunto CNJ com tese única
Dado que o assunto CNJ possui apenas uma tese
Quando o advogado buscar por ele
Então o sistema exibirá um único tema, sem aviso de compartilhamento
```
 
---
 
### US-09 — Entendimento do tema em prosa · Must · 8 SP
 
> Como **juiz**, quero ler o entendimento do tema em prosa, abrindo com o número que responde à pergunta e com o processo apurado junto de todo percentual, para entender o padrão sem abrir tabela.
 
**Regras de negócio**
 
- O texto abre com o número que responde à pergunta central do tema.
- **Todo percentual citado no texto vem acompanhado do método de apuração** — quantidade de decisões, recorte e fórmula.
- O texto é gerado a partir dos agregados do DW, nunca de valores digitados à mão.
- Sem dados suficientes, o texto não é gerado: exibe-se o motivo.
**Dados a armazenar**
 
- `texto do entendimento`: texto, obrigatório.
- `percentual`: decimal de 0 a 100, 1 casa.
- `número de decisões`: inteiro, obrigatório para todo percentual exibido.
- `método de apuração`: texto, obrigatório.
**Mensagens**
 
- Confirmação: não se aplica (leitura).
- Erro: "Não foi possível gerar o entendimento deste tema."
- Aviso: "Entendimento apurado sobre N decisões — amostra reduzida, leia com cautela."
**Protótipo** — aba "Entendimento" com o texto corrido e a procedência ao pé.
 
**Critérios de aceitação**
 
```
Cenário: Ler o entendimento de um tema consolidado
Dado que o tema possui 412 decisões apuradas
Quando o juiz abrir a aba de entendimento
Então o texto abrirá com o número que responde à pergunta central
E cada percentual citado virá acompanhado do número de decisões e do método de apuração
 
Cenário: Tema com amostra reduzida
Dado que o tema possui apenas 7 decisões apuradas
Quando o juiz abrir a aba de entendimento
Então o sistema exibirá "Entendimento apurado sobre 7 decisões — amostra reduzida, leia com cautela"
```
 
---
 
### US-10 — Figura da distribuição dos desfechos · Must · 5 SP
 
> Como **advogado**, quero ver a distribuição dos desfechos do tema em uma figura com a fonte declarada, para enxergar de uma vez quanto é procedente, parcialmente procedente e improcedente.
 
**Regras de negócio**
 
- A figura exibe as três categorias: procedente, parcialmente procedente e improcedente.
- A soma dos percentuais é 100%; diferença de arredondamento é absorvida na maior fatia.
- A figura traz **fonte, data de extração e total de decisões** declarados junto dela.
- Categoria com zero ocorrências aparece com valor 0, não é omitida.
**Dados a armazenar**
 
- `desfecho`: lista pré-definida (procedente, parcialmente procedente, improcedente), obrigatório.
- `quantidade de decisões`: inteiro, obrigatório.
- `percentual`: decimal com 1 casa.
- Origem: consulta OLAP pré-agregada por tema e desfecho.
**Mensagens**
 
- Confirmação: não se aplica.
- Erro: "Não há decisões classificadas por desfecho para este tema."
- Aviso: "Distribuição apurada sobre N decisões."
**Protótipo** — gráfico de distribuição com legenda e bloco de procedência.
 
**Critérios de aceitação**
 
```
Cenário: Visualizar a distribuição de desfechos
Dado que o tema possui 300 decisões classificadas
Quando o advogado abrir o tema
Então a figura exibirá procedente, parcialmente procedente e improcedente
E exibirá a fonte, a data de extração e o total de 300 decisões
 
Cenário: Desfecho sem ocorrência
Dado que nenhuma decisão do tema é parcialmente procedente
Quando a figura for exibida
Então a categoria aparecerá com 0%, e não será omitida
```
 
---
 
### US-13 — Aba corrente na URL · Should · 2 SP
 
> Como **advogado**, quero que a aba que estou vendo fique na URL, para mandar a um colega o link exato da parte que quero mostrar.
 
**Regras de negócio**
 
- Trocar de aba atualiza a URL sem recarregar a página.
- Abrir a URL com a aba indicada carrega direto naquela aba.
- Aba inexistente na URL cai na aba padrão do tema.
**Dados a armazenar**
 
- `aba`: lista pré-definida, opcional na URL.
- `identificador do tema`: identificador, obrigatório na URL.
**Mensagens**
 
- Confirmação: "Link copiado."
- Erro: "Tema não encontrado."
- Aviso: "Aba não reconhecida. Exibindo a aba inicial do tema."
**Protótipo** — abas do tema com botão de copiar link.
 
**Critérios de aceitação**
 
```
Cenário: Compartilhar a aba corrente
Dado que o advogado está na aba de distribuição de um tema
Quando copiar a URL e abri-la em outra janela
Então a página abrirá diretamente na aba de distribuição do mesmo tema
 
Cenário: Aba inválida na URL
Dado que a URL indica uma aba que não existe
Quando a página for aberta
Então o sistema exibirá a aba inicial do tema e o aviso "Aba não reconhecida"
```
 
---
 
### US-18 — Precedentes qualificados ligados ao tema · Could · 8 SP
 
> Como **juiz**, quero ver os precedentes qualificados ligados ao tema — súmula, tema repetitivo, IRDR — distinguindo o que vincula de direito do que apenas persuade, para saber o que me obriga.
 
**Regras de negócio**
 
- Cada precedente é classificado como **vinculante** ou **persuasivo**, e a distinção é visível na tela.
- Tipos aceitos: súmula, tema repetitivo e IRDR.
- A relação entre tema e precedente é N:N, em tabela-ponte.
- Tema sem precedente qualificado exibe estado vazio explicativo.
**Dados a armazenar**
 
- `tipo de precedente`: lista pré-definida (súmula, tema repetitivo, IRDR), obrigatório.
- `identificação do precedente`: texto, obrigatório.
- `caráter`: lista pré-definida (vinculante, persuasivo), obrigatório.
- `órgão de origem`: texto, obrigatório.
- Tabela-ponte entre tema e precedente, grão: um registro por par tema × precedente.
**Mensagens**
 
- Confirmação: não se aplica.
- Erro: "Não foi possível carregar os precedentes deste tema."
- Aviso: "Nenhum precedente qualificado identificado para este tema."
**Protótipo** — aba de precedentes, separada em vinculantes e persuasivos.
 
**Critérios de aceitação**
 
```
Cenário: Tema com precedentes de naturezas diferentes
Dado que o tema está ligado a uma súmula vinculante e a um IRDR persuasivo
Quando o juiz abrir a aba de precedentes
Então os dois serão exibidos em grupos distintos, identificados como vinculante e persuasivo
 
Cenário: Tema sem precedente qualificado
Dado que o tema não possui precedente vinculado
Quando o juiz abrir a aba
Então o sistema exibirá "Nenhum precedente qualificado identificado para este tema"
```
 
---
 
### US-21 — Doutrina invocada · Could · 8 SP
 
> Como **advogado**, quero ver a doutrina invocada com autor, obra e a posição dela no debate, com link para o artigo quando houver, para saber o que citar além de jurisprudência.
 
**Regras de negócio**
 
- Cada referência traz autor, obra e a posição no debate (favorável, contrária ou neutra).
- O link para o artigo é exibido apenas quando existir.
- A relação entre tema e doutrina é N:N, em tabela-ponte.
**Dados a armazenar**
 
- `autor`: texto, obrigatório.
- `obra`: texto, obrigatório.
- `posição no debate`: lista pré-definida (favorável, contrária, neutra), obrigatório.
- `link do artigo`: texto, opcional, com validação de formato de URL.
- Tabela-ponte entre tema e doutrina, grão: um registro por par tema × referência.
**Mensagens**
 
- Confirmação: não se aplica.
- Erro: "Não foi possível carregar a doutrina deste tema."
- Aviso: "Nenhuma doutrina identificada para este tema."
**Protótipo** — aba de doutrina em lista, agrupada por posição.
 
**Critérios de aceitação**
 
```
Cenário: Doutrina com link disponível
Dado que a referência possui URL cadastrada
Quando o advogado abrir a aba de doutrina
Então autor, obra e posição serão exibidos com link para o artigo
 
Cenário: Doutrina sem link
Dado que a referência não possui URL cadastrada
Quando a aba for exibida
Então autor, obra e posição serão exibidos sem link, e sem campo vazio na tela
```
 
---
 
### US-23 — Inteiro teor da decisão citada · Could · 5 SP
 
> Como **advogado**, quero ler o inteiro teor da decisão citada, para conferir o contexto antes de usá-la.
 
**Regras de negócio**
 
- Toda decisão citada na ferramenta oferece acesso ao inteiro teor.
- Quando o inteiro teor não está disponível na base, a tela informa a indisponibilidade e a origem do documento.
- O documento exibido traz número do processo, tribunal e data.
**Dados a armazenar**
 
- `número do processo`: texto, obrigatório, com validação de formato CNJ.
- `inteiro teor`: texto, opcional.
- `link de origem`: texto, opcional, com validação de formato de URL.
- `data da decisão`: data válida, obrigatório.
**Mensagens**
 
- Confirmação: não se aplica.
- Erro: "Não foi possível carregar o inteiro teor desta decisão."
- Aviso: "Inteiro teor não disponível na base. Consulte a decisão na origem."
**Protótipo** — painel lateral com o texto da decisão e o cabeçalho de identificação.
 
**Critérios de aceitação**
 
```
Cenário: Abrir uma decisão com inteiro teor disponível
Dado que a decisão possui inteiro teor na base
Quando o advogado clicar sobre ela
Então o sistema exibirá o texto completo com número do processo, tribunal e data
 
Cenário: Decisão sem inteiro teor
Dado que a decisão não possui inteiro teor armazenado
Quando o advogado clicar sobre ela
Então o sistema exibirá "Inteiro teor não disponível na base. Consulte a decisão na origem"
```
 
---
 
### US-24 — Escopo dos dados visível em toda tela · Must · 2 SP
 
> Como **advogado**, quero que toda tela deixe claro que os dados cobrem TJSP, TJRJ e TJMG, para não tirar conclusão nacional de um percentual que reflete três estados.
 
**Regras de negócio**
 
- O escopo aparece em **todas as telas** que exibem dado apurado.
- O texto do escopo é único e centralizado, para não divergir entre telas.
- Quando um filtro reduz o escopo, o indicador reflete o recorte aplicado.
**Dados a armazenar**
 
- `descrição do escopo`: texto, obrigatório, valor padrão "TJSP, TJRJ e TJMG".
**Mensagens**
 
- Confirmação: não se aplica.
- Erro: não se aplica.
- Aviso: "Dados restritos a TJSP, TJRJ e TJMG. Não representam a média nacional."
**Protótipo** — faixa fixa de escopo no cabeçalho das telas de dado.
 
**Critérios de aceitação**
 
```
Cenário: Escopo visível na tela de resultados
Dado que o advogado está em qualquer tela que exibe dado apurado
Quando a tela for carregada
Então o indicador "TJSP, TJRJ e TJMG" estará visível sem necessidade de rolagem
 
Cenário: Escopo reduzido por filtro
Dado que o advogado filtrou apenas TJSP
Quando a tela for atualizada
Então o indicador exibirá somente TJSP
```
 
---
 
### US-25 — Fonte e data de extração de cada número · Must · 3 SP
 
> Como **juiz**, quero saber de que fonte e de que data de extração vem cada número que estou vendo, para saber exatamente o que estou citando.
 
**Regras de negócio**
 
- **Nenhum número é exibido sem fonte e data de extração.** Se a procedência falta, o número não vai para a tela.
- A data de extração é a da carga que originou o número, não a data da consulta.
- A regra vale para todos os temas e para todas as telas.
**Dados a armazenar**
 
- `fonte`: texto, obrigatório.
- `data de extração`: data válida, obrigatório.
- `método de apuração`: texto, obrigatório.
- Registrados na dimensão de carga, ligados ao grão da tabela fato.
**Mensagens**
 
- Confirmação: não se aplica.
- Erro: "Número indisponível: procedência não registrada."
- Aviso: "Fonte: «...» · Extração em dd/mm/aaaa."
**Protótipo** — bloco de procedência ao pé de cada figura e tabela.
 
**Critérios de aceitação**
 
```
Cenário: Número com procedência completa
Dado que o percentual possui fonte e data de extração registradas
Quando o juiz visualizar o número
Então a fonte e a data de extração serão exibidas junto dele
 
Cenário: Número sem procedência registrada
Dado que um valor não possui fonte ou data de extração
Quando a tela for montada
Então o valor não será exibido
E o sistema exibirá "Número indisponível: procedência não registrada"
```
 
---
 
### US-26 — Ausência de dado explicada · Must · 3 SP
 
> Como **advogado**, quero que a tela me diga o que não existe e por quê, em vez de mostrar campo vazio ou valor plausível, para não construir uma peça sobre dado que não existe.
 
**Regras de negócio**
 
- Nenhuma tela exibe campo vazio, traço solto ou zero ambíguo no lugar de dado ausente.
- Todo estado vazio informa **o que falta e por quê** — sem dado na base, fora do escopo ou fora do período filtrado.
- Ausência de dado nunca é substituída por estimativa ou valor padrão.
**Dados a armazenar**
 
- `motivo da ausência`: lista pré-definida (sem dado na base, fora do escopo, fora do período filtrado), obrigatório quando não há valor.
**Mensagens**
 
- Confirmação: não se aplica.
- Erro: "Não foi possível verificar a disponibilidade deste dado."
- Aviso: "Sem dado para este recorte: «motivo». Nenhum valor foi estimado."
**Protótipo** — componente único de estado vazio, reutilizado em todas as telas.
 
**Critérios de aceitação**
 
```
Cenário: Recorte sem dado na base
Dado que o tema não possui decisões no TJMG
Quando o advogado filtrar por TJMG
Então o sistema exibirá "Sem dado para este recorte: sem dado na base"
E não exibirá campo vazio nem valor estimado
 
Cenário: Recorte fora do período
Dado que o tema só possui decisões a partir de 2019
Quando o advogado filtrar o período de 2010 a 2015
Então o sistema exibirá "Sem dado para este recorte: fora do período filtrado"
```