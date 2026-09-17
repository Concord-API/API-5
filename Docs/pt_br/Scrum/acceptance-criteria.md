DoR detalhada e critérios de aceite para todas as 32 histórias do
[Product Backlog](../../README.md#-product-backlog), na ordem do backlog. Os cenários são
escritos em BDD, como a [Definition of Ready](definition-of-ready.md) exige.

Cada cabeçalho carrega prioridade, épico, estimativa, sprint, estado e dependências. Os
valores de domínio permanecem em português (`NFR-20`), de modo que termos como *Consolidada*
e *súmula* aparecem como aparecem na tela.

---

# Sprint 1

---

### US-01 — Busca de tema em linguagem natural
`Must` · E1 · 8 SP · Sprint 1 · pronta · depende de —

> Como **usuário**, quero digitar o tema do meu caso em linguagem natural e obter temas
> jurídicos curados — não uma lista de processos — para que eu descubra como aquilo está
> sendo decidido sem garimpar um acórdão de cada vez.

**Regras de negócio**

- A busca aceita texto livre em português e devolve **temas**, nunca processos individuais.
- Busca full-text no Postgres, tolerante à ausência de acentos e a erros de digitação.
- Uma consulta com menos de 3 caracteres não é submetida.
- Uma busca vazia não é erro: ela devolve os temas de maior volume.
- Um tema sem julgamento calculado não aparece — um tema sem resultado não responde nada.
**Dados**

- `termo de busca`: texto, obrigatório, mínimo de 3 caracteres.
- `id do tema`, `título do tema`: obrigatórios.
- `vetor de busca`: índice full-text em português, gerado no momento da carga.
**Mensagens**

- Confirmação: "N temas encontrados para «termo»."
- Erro: "Digite ao menos 3 caracteres para buscar."
- Vazio: "Nenhum tema encontrado para «termo» no escopo TJSP, TJRJ e TJMG."
**Critérios de aceite**

```gherkin
Cenário: Buscar um tema existente
Dado que existem temas calculados na base
Quando o usuário digita "inscrição indevida em cadastro de inadimplentes"
Então o sistema exibe uma lista de temas jurídicos, e nenhum item da lista é um processo individual

Cenário: Buscar sem acentos
Dado que o tema "Inscrição indevida" existe
Quando o usuário digita "inscricao indevida"
Então o sistema devolve esse mesmo tema

Cenário: Buscar com erro de digitação
Dado que o tema "Dano moral por negativação indevida" existe
Quando o usuário digita "negativacao indevda"
Então o sistema recupera o tema por similaridade em vez de devolver vazio

Cenário: Buscar sem correspondência
Dado que não há tema correspondente na base
Quando o usuário busca "contrato de arrendamento de satélite"
Então o sistema explica o escopo TJSP, TJRJ e TJMG e sugere reformular

Cenário: Busca vazia
Dado que o usuário submete a busca sem termo
Quando a busca é executada
Então o sistema devolve os temas de maior volume

Cenário: Compartilhar a busca
Dado que o usuário submeteu uma busca
Quando o termo aparece na URL
Então recarregar a página ou abrir o link reproduz a mesma busca
```

---

### US-02 — Resultados ordenados pela força do entendimento
`Must` · E1 · 2 SP · Sprint 1 · pronta · depende de US-01, US-06

> Como **usuário**, quero os resultados ordenados pelo quanto o entendimento está
> consolidado, e não pela relevância textual, para que eu encontre primeiro o que sustenta
> minha tese.

**Regras de negócio**

- A ordenação padrão é pelo score de força, decrescente, e a tela declara isso.
- Empates são resolvidos pelo maior volume de decisões; a relevância textual é usada apenas para decidir quais temas entram na lista, nunca para ordená-la.
- O volume por trás de cada score fica visível ao lado dele.
**Critérios de aceite**

```gherkin
Cenário: Ordenação padrão
Dado um conjunto de resultados
Quando a lista é exibida
Então ela está ordenada pelo score de força, decrescente, e a tela declara isso

Cenário: Empate no score
Dado dois temas com o mesmo score
Quando a lista é montada
Então o empate é resolvido pelo volume de decisões, e a relevância textual não é exibida

Cenário: Volume alto, disputa em aberto
Dado um tema com volume grande e decisões divididas meio a meio
Quando os resultados aparecem
Então ele não fica no topo apenas pelo volume

Cenário: Score alto, volume baixo
Dado um tema com score alto e pouquíssimos julgados
Quando ele aparece na lista
Então o volume por trás dele fica visível ao lado do score
```

---

### US-04 — Filtrar os resultados para o formato do meu caso
`Must` · E1 · 5 SP · Sprint 1 · aguardando decisão 2 · depende de US-03

> Como **usuário**, quero filtrar os resultados por tribunal, período, instância e força
> mínima, vendo quantos processos cada tribunal tem, para que eu possa estreitar a lista até
> o meu caso.

**Regras de negócio**

- Os filtros se combinam e são aplicados pela API; a lista nunca é filtrada no navegador.
- O filtro de tribunal exibe a contagem de processos de cada tribunal, vinda da API.
- O filtro de instância oferece apenas as instâncias que existem no escopo carregado.
- Os filtros ativos são refletidos na URL, de modo que uma visão estreitada possa ser compartilhada.
**Mensagens**

- Resultado vazio: a tela descreve os filtros aplicados e oferece o caminho para limpá-los.
**Critérios de aceite**

```gherkin
Cenário: Filtrar por tribunal com contagens
Dado os tribunais no escopo
Quando o filtro de tribunal é renderizado
Então cada tribunal exibe sua contagem de processos, vinda da API

Cenário: Filtro de instância apenas com tribunais estaduais
Dado que a decisão 2 mantém o escopo em tribunais estaduais
Quando o filtro de instância é renderizado
Então a opção "Superior" não é exibida

Cenário: Aplicar e compartilhar
Dado que o usuário escolheu filtros
Quando ele os aplica
Então a lista é reconstruída pela API e os filtros aparecem na URL

Cenário: Limpar filtros
Dado que há filtros aplicados
Quando o usuário os limpa
Então todo filtro volta ao seu padrão e a lista é reconstruída

Cenário: Estreitamento sem resultados
Dado uma combinação de filtros sem resultado
Quando ela é aplicada
Então a tela descreve o estreitamento aplicado e oferece um caminho para limpá-lo
```

---

### US-09 — Ler o entendimento em prosa
`Must` · E3 · 8 SP · Sprint 1 · pronta · depende de US-06

> Como **usuário**, quero ler o entendimento do tema em prosa, abrindo com o número que
> responde à pergunta e com a contagem de processos (`n`) ao lado de todo percentual, para
> que eu compreenda o padrão sem abrir uma tabela.

**Regras de negócio**

- O cabeçalho do tema carrega o score, o grau, a tag de área, o título da tese e a linha de metadados: processos, tribunais, período e última decisão.
- O texto abre com uma linha de destaque que já contém o número que responde à pergunta, com seu `n`.
- Todo número no corpo vem acompanhado do seu `n`, e nenhum deles é calculado na tela.
- Enquanto não existir geração automática da prosa, o resumo é o texto **curado** conforme a decisão 20, e o dado registra que ele é curado.
- Blocos cuja fonte não está confirmada — citação de acórdão, botão de inteiro teor, marcadores de citação, rodapé de decisões citadas — não aparecem, e seu lugar explica por quê.
**Critérios de aceite**

```gherkin
Cenário: A linha de abertura responde à pergunta
Dado um tema com dados calculados
Quando seu resumo é renderizado
Então a primeira linha de destaque contém o número que responde à pergunta, com seu n

Cenário: Todo percentual carrega seu n
Dado qualquer percentual no corpo do texto
Quando ele é exibido
Então a contagem de processos a partir da qual foi calculado é exibida junto

Cenário: Nada é calculado na tela
Dado que o texto e seus números vêm dos agregados
Quando a página é renderizada
Então nenhum número é calculado no frontend

Cenário: Bloco sem fonte
Dado que a citação de acórdão depende do inteiro teor, que não tem fonte confirmada
Quando a página é renderizada
Então o bloco de citação não aparece e seu lugar explica por quê, com link para a página de limitações

Cenário: O rodapé declara a procedência
Dado que a página foi alimentada por uma ou mais fontes
Quando o rodapé é renderizado
Então ele lista todas as fontes, a data de extração e a versão da metodologia
```

---

### US-10 — Ver a distribuição dos resultados em uma figura
`Must` · E3 · 5 SP · Sprint 1 · aguardando decisão 3 · depende de US-09

> Como **usuário**, quero ver a distribuição dos resultados do tema em uma figura com a fonte
> declarada, para que eu enxergue de relance quanto é procedente, parcialmente procedente e
> improcedente.

**Regras de negócio**

- A figura exibe contagens e percentuais por categoria de resultado.
- Ela é numerada, fica no fluxo do texto — nunca em uma grade de cards — e carrega a fonte logo abaixo.
- Sem fonte declarada a figura simplesmente não é renderizada.
- O tratamento dos pedidos parcialmente procedentes (decisão 3) é declarado onde o número é calculado.
- Regras visuais: barras retangulares, sem raio, sem eixo, sem grade, sem tooltip.
**Critérios de aceite**

```gherkin
Cenário: Distribuição com contagens e percentuais
Dado um tema com resultados calculados
Quando a figura é renderizada
Então cada categoria de resultado exibe sua contagem e seu percentual

Cenário: Figura sem fonte
Dado uma figura cuja fonte não está declarada
Quando a página é montada
Então a figura não é renderizada

Cenário: A figura de valores não tem fonte
Dado que a faixa de valores arbitrados depende do inteiro teor, que não tem fonte
Quando a página é renderizada
Então a figura de valores não aparece e seu lugar explica por quê
```

---

### US-18 — Ver os precedentes qualificados que me vinculam
`Could` · E4 · 8 SP · Sprint 1 · fonte a verificar · depende de —

> Como **usuário**, quero ver os precedentes qualificados vinculados ao tema — súmula, tema
> repetitivo, IRDR — distinguindo o que é juridicamente vinculante do que é meramente
> persuasivo, para que eu saiba o que me vincula.

**Pré-condição da DoR:** fonte de precedentes verificada — existe uma API pública utilizável,
ela cobre os três tribunais, e seus termos permitem armazenar em base própria — com a
resposta registrada na wiki. Até lá o bloco não aparece e seu lugar explica por quê.

**Regras de negócio**

- Cada precedente carrega sua espécie, seu efeito, quantas das decisões do tema o citam e se ele foi seguido.
- O efeito distingue o juridicamente vinculante do persuasivo, e a hierarquia visual espelha a hierarquia jurídica — preenchimento sólido apenas para o que é obrigatório.
- Cada precedente tem um caminho para sua fonte oficial.
**Critérios de aceite**

```gherkin
Cenário: Vinculante e persuasivo são distinguíveis
Dado um tema com precedentes vinculados
Quando o bloco é renderizado
Então o que é juridicamente vinculante é visualmente distinto do que é persuasivo

Cenário: Um tribunal que se afasta do precedente
Dado um tribunal que se afasta do precedente
Quando o bloco é renderizado
Então isso é sinalizado como divergência em aberto

Cenário: Procedência do bloco
Dado que o bloco de precedentes está exibido
Quando o usuário verifica sua procedência
Então ele declara de onde vieram os precedentes e quando
```

---

### US-21 — Saber o que citar além da jurisprudência
`Must` · E4 · 8 SP · Sprint 1 · fonte a verificar · depende de —

> Como **usuário**, quero ver a doutrina invocada, com autor, obra e sua posição no debate,
> com link para o artigo quando houver, para que eu saiba o que citar além da jurisprudência.

**Pré-condição da DoR:** uma fonte verificada para os artigos **e** uma resposta por escrito
sobre de onde vem a associação entre doutrina e tema — essa é a lacuna real, não a fonte do
texto. Curadoria manual é aceitável se declarada, com a ressalva de que não escala.

> Este é o único **Must** do backlog cuja fonte não está confirmada. Ou a verificação é
> respondida logo no início da Sprint 1, ou a prioridade está errada — ver o aviso no
> [Product Backlog](product-backlog.md).

**Regras de negócio**

- Cada entrada carrega autor, obra, edição ou capítulo, e sua posição no debate (majoritária, intermediária, minoritária).
- Um **artigo** carrega link para onde está publicado, preferencialmente com identificador estável.
- Um **livro** aparece como referência textual — autor, título, edição, capítulo. **Nunca como PDF**: obra protegida por direito autoral não é hospedada.
**Critérios de aceite**

```gherkin
Cenário: Artigo com link estável
Dado uma entrada de artigo
Quando ela é exibida
Então ela carrega um link para onde está publicada

Cenário: Livro como referência textual
Dado uma entrada de livro
Quando ela é exibida
Então ela aparece como autor, título, edição e capítulo, sem PDF hospedado

Cenário: Associação curada
Dado que a associação entre doutrina e tema foi curada manualmente
Quando a procedência é exibida
Então ela declara que houve curadoria, e quando
```

---

### US-23 — Ler o inteiro teor da decisão citada na aplicação
`Could` · E4 · 5 SP · Sprint 1 · fonte a verificar · depende de US-37

> Como **usuário**, quero ler o inteiro teor da decisão citada dentro da aplicação, para que
> eu possa conferir o contexto antes de usá-la.

**Pré-condição da DoR:** decisão 21 tomada — o inteiro teor pode ser armazenado e exibido
dentro da aplicação? — mais uma rota verificada para obter esse texto nos três tribunais,
registrada na wiki. Ler na aplicação significa **armazenar** o texto, não apenas apontar para
ele, e isso muda o modelo de dados (`NFR-01`) e a análise de LGPD (`NFR-21`).

**Regras de negócio**

- O texto da decisão é exibido dentro da aplicação, com sua fonte e data de extração ao lado, como qualquer outro dado (`NFR-02`).
- Abrir o texto não faz perder o contexto do tema: o usuário consegue voltar para onde estava.
- Onde o texto não foi obtido para uma decisão, não há botão morto — a ausência é explícita (`US-26`), e o número do processo continua visível para uma consulta manual no tribunal.
- Um processo em segredo de justiça nunca é exibido, qualquer que seja a rota — ele é sinalizado como sigiloso.
- O texto é armazenado como foi obtido. Ele não é resumido, reescrito nem completado por um modelo.
**Critérios de aceite**

```gherkin
Cenário: Ler uma decisão na aplicação
Dado uma decisão citada cujo inteiro teor foi obtido
Quando o usuário pede para lê-la
Então o texto é exibido na aplicação com sua fonte e data de extração

Cenário: Voltar ao tema
Dado que o usuário está lendo o texto de uma decisão
Quando ele volta
Então ele retorna ao ponto do tema de onde veio

Cenário: Texto não obtido
Dado uma decisão cujo inteiro teor não foi obtido
Quando a linha é renderizada
Então não há botão morto, a ausência é explícita, e o número do processo continua visível

Cenário: Processo em segredo de justiça
Dado um processo em segredo de justiça
Quando ele aparece em qualquer lugar
Então nenhum texto é exibido e o processo é sinalizado como sigiloso

Cenário: O texto não é reescrito
Dado um texto de decisão armazenado
Quando ele é exibido
Então ele corresponde ao que foi obtido da fonte, sem resumo gerado por modelo apresentado como a decisão
```

---

### US-24 — Conhecer o escopo de cobertura
`Must` · E5 · 2 SP · Sprint 1 · pronta · depende de —

> Como **usuário**, quero que toda tela deixe claro que os dados cobrem TJSP, TJRJ e TJMG,
> para que eu não tire uma conclusão nacional de um percentual que reflete três estados.

**Regras de negócio**

- O escopo fica visível **sem interação** — não escondido em um tooltip.
- O texto nomeia os tribunais e não usa vocabulário técnico interno.
- A lista de tribunais não é texto fixo espalhado pela interface: se a decisão 2 mudar o escopo, a declaração acompanha.
**Critérios de aceite**

```gherkin
Cenário: Escopo visível em toda tela com números
Dado a tela de resultados e as duas abas de detalhe
Quando cada uma delas é renderizada
Então o escopo territorial fica visível sem interação

Cenário: Mudança de escopo
Dado que a decisão 2 muda o escopo
Quando as telas são renderizadas
Então a declaração reflete a nova cobertura, a partir de uma fonte única
```

---

### US-25 — Conhecer a fonte e a data de todo número
`Must` · E5 · 3 SP · Sprint 1 · pronta · depende de —

> Como **usuário**, quero saber a fonte e a data de extração de todo número que estou vendo,
> para que eu saiba exatamente o que estou citando.

**Regras de negócio**

- Quando uma página é alimentada por mais de uma fonte, o rodapé lista **todas** elas; dois blocos de fontes diferentes declaram cada um a sua.
- A data de extração vem do dado carregado, nunca do relógio do servidor no momento da requisição.
- Um bloco sem procedência disponível **não é exibido** — procedência é requisito, não ornamento.
- A versão da metodologia usada para calcular as métricas é exibida junto da procedência.
**Critérios de aceite**

```gherkin
Cenário: Fonte e data em toda tela com números
Dado a tela de resultados e as duas abas de detalhe
Quando cada uma delas é renderizada
Então a fonte e a data de extração são declaradas

Cenário: Várias fontes em uma página
Dado que a página foi alimentada por mais de uma fonte
Quando o rodapé é renderizado
Então todas as fontes são listadas, não apenas a principal

Cenário: Bloco sem procedência
Dado um bloco cuja procedência não está disponível
Quando a página é renderizada
Então esse bloco não é exibido

Cenário: A data vem do dado
Dado uma página renderizada hoje a partir de uma carga executada na semana passada
Quando a data de extração é exibida
Então ela mostra a data da carga, não a de hoje
```

---

### US-26 — Ver "sem dado" explicado em vez de um campo vazio
`Must` · E5 · 3 SP · Sprint 1 · pronta · depende de —

> Como **usuário**, quero que a tela me diga o que não existe e por quê, em vez de exibir um
> campo vazio ou um valor plausível, para que eu não construa uma peça sobre dado que não
> existe.

**Regras de negócio**

- Três mensagens distintas, cada uma com seu próprio texto: **a fonte não fornece isso**, **o dado ainda não foi carregado** e **não se aplica a este tema**. A mensagem genérica nunca é usada.
- Uma lista vazia devolvida pela API é conteúdo, não erro, e nunca um placeholder inventado.
- Um campo sem fonte dentro de uma tabela: a coluna não aparece, ou aparece explicitamente sinalizada — nunca com valor.
**Critérios de aceite**

```gherkin
Cenário: Bloco sem fonte confirmada
Dado qualquer bloco sem fonte confirmada hoje
Quando o detalhe do tema é renderizado
Então ele declara o que não existe e por quê, com caminho para a explicação completa

Cenário: Lista vazia vinda da API
Dado que a API devolve uma lista vazia
Quando a tela é renderizada
Então o estado vazio é conteúdo, sem placeholder inventado

Cenário: A mensagem certa para cada situação
Dado cada uma das três situações
Quando a tela é renderizada
Então ela exibe a mensagem correspondente, nunca a genérica
```

---

# Sprint 2

---

### US-03 — Comparar teses na lista de resultados
`Must` · E1 · 8 SP · Sprint 2 · pronta · depende de US-01, US-06

> Como **usuário**, quero ver em cada resultado o score, a área do direito, o título da tese,
> um resumo curto, os tribunais, o volume, o período, a última decisão e o percentual
> favorável, para que eu possa comparar teses antes de abrir qualquer uma delas.

**Regras de negócio**

- Cada item carrega: score em um círculo com `/100`, tag de área, título da tese, um resumo de até duas linhas, siglas dos tribunais, número de processos, período, data da última decisão e o percentual favorável com sua barra de alinhamento.
- O percentual favorável carrega seu `n` na mesma linha.
- Quando um tema tem mais tribunais do que os chips exibidos, um indicador `+N` mostra exatamente a diferença; quando todos cabem, o indicador não é renderizado.
- Os números são formatados em português (12.418, não 12,418) e nunca são recalculados na tela.
**Critérios de aceite**

```gherkin
Cenário: Um item de resultado completo
Dado um tema na lista de resultados
Quando o item é renderizado
Então ele exibe score, área, título, resumo, tribunais, volume, período, última decisão e percentual favorável

Cenário: Percentual sem base
Dado que o percentual favorável está exibido
Quando o item é renderizado
Então seu n fica visível na mesma linha

Cenário: Mais tribunais do que chips
Dado um tema com mais tribunais do que os chips exibidos
Quando o item é renderizado
Então um indicador +N mostra exatamente a diferença

Cenário: Abrir o tema
Dado um item de resultado
Quando o usuário clica nele
Então o detalhe do tema é aberto
```

---

### US-38 — Sugestões de consulta na tela inicial
`Could` · E1 · 2 SP · Sprint 2 · pronta · depende de US-01

> Como **usuário**, quero consultas frequentes sugeridas na tela inicial, para que eu entenda
> que tipo de pergunta a ferramenta responde antes de digitar a minha.

**Regras de negócio**

- As sugestões vêm de dados reais do escopo carregado, nunca de uma lista fixa no código.
- Elas são temas em linguagem natural, reforçando o que a US-01 ensina sobre o que se busca aqui.
- Sem sugestões disponíveis, a área simplesmente não aparece — sem espaço vazio, sem texto de erro.
**Critérios de aceite**

```gherkin
Cenário: Clicar em uma sugestão
Dado que a tela inicial exibe sugestões
Quando o usuário clica em uma delas
Então a busca é executada com aquele termo

Cenário: Nenhuma sugestão disponível
Dado que não há sugestões a exibir
Quando a tela inicial é renderizada
Então a área de sugestões não é renderizada de forma alguma
```

---

### US-06 — O score de 0 a 100
`Must` · E2 · 8 SP · Sprint 2 · aguardando decisão 4 · depende de —

> Como **usuário**, quero um score de 0 a 100 que me diga o quanto o entendimento sobre o
> tema está consolidado, para que eu saiba se vale a pena sustentar a tese ou se é uma briga
> em aberto.

**Regras de negócio**

- O score combina quatro componentes — concordância, volume, cobertura e recência — com pesos que somam 1,0.
- O score é **determinístico**: mesma base, mesmo score, e nenhum componente é opinião de um modelo.
- Um tema sem julgamento calculado não recebe score e não aparece.
- As limitações conhecidas ficam registradas onde o usuário chega à composição do score — em particular a de que a recência usa apenas o ano da última decisão, não a densidade recente.
**Critérios de aceite**

```gherkin
Cenário: Tema dividido meio a meio
Dado um tema decidido metade de um jeito e metade do outro
Quando o score é calculado
Então a concordância é 0

Cenário: Tema unânime
Dado um tema decidido do mesmo jeito em todos os julgamentos
Quando o score é calculado
Então a concordância é 1

Cenário: Volume acima da saturação
Dado um tema com volume acima do ponto de saturação
Quando o score é calculado
Então mais decisões não aumentam o score

Cenário: Tese envelhecida
Dado um tema cuja última decisão é suficientemente antiga
Quando o score é calculado
Então a recência é 0

Cenário: Cobertura antes da recalibração
Dado que a decisão 4 não foi tomada
Quando um tema é exibido
Então nenhum score é exibido

Cenário: Exemplo de referência
Dado o exemplo de referência publicado na wiki
Quando o teste automatizado é executado
Então ele reproduz exatamente o score daquele exemplo
```

---

### US-07 — O grau em linguagem jurídica
`Must` · E2 · 2 SP · Sprint 2 · aguardando decisão 14 · depende de US-06

> Como **usuário**, quero que o score venha com um grau em linguagem que já existe no meio
> jurídico — Consolidada, Dominante, Em formação, Divergente — para que eu não tenha que
> interpretar uma escala inventada.

**Regras de negócio**

- Cada faixa de score corresponde a um dos quatro graus, e o grau aparece ao lado do score.
- Existe um **número mínimo de julgados** (decisão 14) abaixo do qual o score é exibido sem o grau textual — uma tese com 95% de concordância sobre oito julgados tomaria emprestada uma autoridade que oito processos não sustentam.
- Os quatro rótulos são termos que já existem no vocabulário jurídico; o produto não inventa nenhum.
**Critérios de aceite**

```gherkin
Cenário: Grau ao lado do score
Dado um tema com julgados suficientes
Quando o score é exibido
Então o grau correspondente é exibido ao lado dele

Cenário: Abaixo do mínimo
Dado um tema com concordância alta, mas com menos julgados que o mínimo
Quando o score é exibido
Então ele aparece sem o grau textual
```

---

### US-08 — Auditar a composição do score
`Must` · E2 · 3 SP · Sprint 2 · pronta · depende de US-06

> Como **usuário**, quero abrir a composição do score — os quatro componentes, seus pesos e a
> base de cálculo — para que eu possa citar a estatística sabendo exatamente de onde ela vem.

**Regras de negócio**

- A composição exibe os quatro componentes com seu valor e peso, mais a base: julgados, favoráveis, desfavoráveis, número de tribunais e o ano da última decisão.
- A composição é alcançável na interface — não escondida, não apenas via API.
- A metodologia e os pesos estão documentados e são alcançáveis a partir da tela.
**Critérios de aceite**

```gherkin
Cenário: Abrir a composição
Dado um score exibido
Quando o usuário abre sua composição
Então ele vê os quatro componentes com valor e peso, e a base de cálculo

Cenário: Nada é recalculado
Dado que o score chega pronto da API
Quando a tela é renderizada
Então nem os componentes nem o total são recalculados
```

---

### US-11 — Ver o alinhamento evoluir ao longo do tempo
`Must` · E3 · 5 SP · Sprint 2 · pronta · depende de US-09

> Como **usuário**, quero ver como o alinhamento do tema evoluiu ano a ano, com a frase de
> tendência, para que eu saiba se o entendimento está se consolidando ou mudando.

**Regras de negócio**

- A série vai do mais antigo ao mais recente, com o ano mais recente destacado.
- A frase de tendência diz "X% → Y% na direção predominante", ambos os valores vindos do agregado — não calculados na tela.
- Um ano sem resultado calculado não tem barra vazia.
- Com dados em um único ano, a frase de tendência não é exibida — não há dois pontos para comparar.
**Critérios de aceite**

```gherkin
Cenário: Série anual
Dado um tema com resultados ao longo de vários anos
Quando a série é renderizada
Então ela vai do mais antigo ao mais recente, com o ano mais recente destacado

Cenário: Ano sem resultado
Dado um ano sem resultado calculado
Quando a série é renderizada
Então não há barra vazia para aquele ano

Cenário: Ano único
Dado um tema com dados em um único ano
Quando a série é renderizada
Então a frase de tendência não é exibida
```

---

### US-12 — Ver o alinhamento por tribunal
`Must` · E3 · 3 SP · Sprint 2 · pronta · depende de US-09

> Como **usuário**, quero ver o alinhamento do tema por tribunal, para que eu saiba se a tese
> se sustenta igual em São Paulo, no Rio e em Minas.

**Regras de negócio**

- Cada tribunal no escopo exibe seu percentual na direção predominante, com seu `n` disponível ao lado.
- Um tribunal sem julgamento calculado não aparece com zero por cento — ele aparece como sem dado, ou não aparece.
**Critérios de aceite**

```gherkin
Cenário: Alinhamento por tribunal
Dado um tema com decisões em mais de um tribunal
Quando a lista é renderizada
Então cada tribunal exibe seu percentual na direção predominante, com seu n

Cenário: Tribunal sem julgados
Dado um tribunal sem julgamento calculado no tema
Quando a lista é renderizada
Então ele não aparece com zero por cento

Cenário: Os números fecham
Dado a soma dos tribunais
Quando ela é comparada com o total do tema
Então os números batem
```

---

### US-14 — Comparar o comportamento de cada tribunal
`Must` · E4 · 3 SP · Sprint 2 · pronta · depende de US-12

> Como **usuário**, quero uma tabela do comportamento de cada tribunal — decisões,
> alinhamento e data da mais recente — para que eu possa comparar meu tribunal com os outros.

**Regras de negócio**

- Por tribunal: número de decisões, alinhamento e data da última decisão.
- O valor mediano arbitrado depende do inteiro teor e não tem fonte: essa coluna não aparece, ou aparece sinalizada como sem fonte — nunca com valor.
- Regras visuais: texto em serifa, números em monoespaçada alinhados à direita, cabeçalho em versalete, sem zebrado, sem bordas verticais.
- Uma tabela mais larga que seu contêiner rola **dentro dele**; a página nunca rola horizontalmente.
**Critérios de aceite**

```gherkin
Cenário: Comportamento por tribunal
Dado um tema com decisões em mais de um tribunal
Quando a tabela é renderizada
Então cada linha exibe decisões, alinhamento e a data da última decisão

Cenário: Coluna sem fonte
Dado que o valor mediano não tem fonte confirmada
Quando a tabela é renderizada
Então essa coluna não aparece, ou aparece sinalizada como sem fonte

Cenário: Tabela larga
Dado uma tabela mais larga que seu contêiner
Quando ela é renderizada
Então ela rola dentro do contêiner e a página não rola horizontalmente
```

---

### US-15 — Conferir a amostra de processos por trás do tema
`Must` · E4 · 5 SP · Sprint 2 · pronta · depende de US-09

> Como **usuário**, quero uma amostra auditável dos processos por trás do tema, com câmara,
> data e resultado, para que eu possa conferir os processos antes de citá-los.

**Regras de negócio**

- Cada linha carrega número do processo, câmara, data e resultado calculado.
- Relator e valor não têm fonte confirmada: essas colunas vêm **vazias e sinalizadas**, nunca preenchidas.
- Um processo em segredo de justiça é sinalizado e nenhum dado sigiloso é exposto.
- A ordenação padrão é declarada e estável entre visitas, e a amostra informa quantas linhas exibe de quantas no total ("N de M decisões").
**Critérios de aceite**

```gherkin
Cenário: Amostra auditável
Dado um tema com processos calculados
Quando a amostra é renderizada
Então cada linha exibe número do processo, câmara, data e resultado

Cenário: Colunas sem fonte
Dado que relator e valor não têm fonte confirmada
Quando uma linha é renderizada
Então essas colunas ficam vazias e sinalizadas, nunca preenchidas

Cenário: Processo em segredo de justiça
Dado um processo em segredo de justiça
Quando ele aparece na amostra
Então ele é sinalizado e nenhum dado sigiloso é exposto

Cenário: Ordenação estável
Dado a mesma consulta executada duas vezes
Quando a amostra é renderizada
Então a ordem é a mesma
```

---

### US-17 — Saber se as câmaras do tribunal divergem
`Should` · E4 · 5 SP · Sprint 2 · pronta · depende de US-14

> Como **usuário**, quero saber se as câmaras do meu tribunal estão decidindo do mesmo jeito,
> para que eu identifique divergência interna antes de decidir.

**Regras de negócio**

- Por tribunal, o alinhamento de cada câmara, com o `n` de cada câmara visível ao lado do percentual.
- Uma câmara com um único julgado não aparece — um caso isolado é ruído, não divergência.
- Uma câmara que se afasta do padrão do próprio tribunal é sinalizada.
**Critérios de aceite**

```gherkin
Cenário: Alinhamento por câmara
Dado um tribunal com decisões em várias câmaras
Quando o bloco é renderizado
Então cada câmara exibe seu alinhamento e seu n

Cenário: Câmara com um único julgado
Dado uma câmara com apenas um julgado
Quando o bloco é renderizado
Então essa câmara não aparece

Cenário: Câmara divergente
Dado uma câmara que se afasta do padrão do próprio tribunal
Quando o bloco é renderizado
Então a divergência é sinalizada

Cenário: Os números fecham
Dado a soma das câmaras de um tribunal
Quando ela é comparada com o total daquele tribunal
Então os números batem
```

---

### US-19 — Escolher o argumento que mais vence
`Could` · E4 · 8 SP · Sprint 2 · fonte a verificar · depende de —

> Como **usuário**, quero ver os fundamentos invocados nas decisões do tema, com a frequência
> e a taxa de acolhimento de cada um, para que eu escolha o argumento que mais vence e evite
> o que sempre perde.

**Pré-condição da DoR:** uma rota verificada para o inteiro teor nos três tribunais, mais uma
resposta por escrito sobre a viabilidade de extrair fundamentos — custo, qualidade em
comparação com a conferência manual, e auditabilidade. Sem o texto das decisões não há
fundamento a extrair.

**Regras de negócio**

- Cada fundamento carrega sua natureza (lei, jurisprudência, súmula, tese de defesa), em quantas decisões foi citado e sua taxa de acolhimento.
- Onde a extração é automatizada, é possível rastrear em quais decisões um fundamento foi identificado.
- **Frequência e taxa de acolhimento vêm de contagem sobre os dados**, nunca do modelo.
**Critérios de aceite**

```gherkin
Cenário: Fundamentos com frequência e acolhimento
Dado um tema com fundamentos extraídos
Quando o bloco é renderizado
Então cada fundamento exibe sua natureza, sua contagem de citações e sua taxa de acolhimento

Cenário: Extração rastreável
Dado um fundamento extraído automaticamente
Quando o usuário o confere
Então ele consegue ver em quais decisões o fundamento foi identificado

Cenário: O modelo não conta
Dado que um modelo participou da extração
Quando os números são exibidos
Então nenhum deles veio do modelo
```

---

### US-22 — Montar a citação completa
`Could` · E4 · 5 SP · Sprint 2 · fonte a verificar · depende de —

> Como **usuário**, quero o nome do relator na amostra e na referência de citação, para que eu
> consiga montar a citação completa.

**Pré-condição da DoR:** uma rota verificada até o relator — campo estruturado, raspagem do
portal ou inteiro teor. Se o dado não for consistente nos três tribunais, o item não entra.

**Regras de negócio**

- O relator aparece na amostra auditável e na referência de citação.
- Onde o relator não foi obtido, o campo fica **vazio e sinalizado**, nunca preenchido por inferência.
**Critérios de aceite**

```gherkin
Cenário: Relator na amostra
Dado um processo cujo relator foi obtido
Quando a linha é renderizada
Então o nome aparece na amostra e na referência de citação

Cenário: Relator não obtido
Dado um processo cujo relator não foi obtido
Quando a linha é renderizada
Então o campo fica vazio e sinalizado, não inferido
```

---

### US-37 — Ver o acórdão por trás de cada afirmação
`Could` · E4 · 8 SP · Sprint 2 · fonte a verificar · depende de —

> Como **usuário**, quero ver no texto do entendimento o acórdão que sustenta cada afirmação,
> com a referência completa e a lista de decisões citadas ao pé, para que eu possa citar a
> mesma decisão.

**Pré-condição da DoR:** uma rota verificada para o inteiro teor. Sem ela não há ementa a
citar, e a referência completa também depende do relator (`US-22`).

**Regras de negócio**

- Uma afirmação sustentada por uma decisão específica carrega um marcador de citação clicável que leva à entrada correspondente na lista de decisões citadas.
- Cada entrada carrega número do processo, câmara, relator, data e uma síntese de uma linha.
- Toda decisão citada existe na base — nenhuma citação é gerada sem lastro.
- Onde o inteiro teor não está disponível para uma decisão, não há botão morto.
**Critérios de aceite**

```gherkin
Cenário: Marcador de citação
Dado uma afirmação sustentada por uma decisão específica
Quando o usuário lê o texto
Então há um marcador de citação clicável ao lado dela

Cenário: Chegar à decisão citada
Dado que o usuário clica no marcador
Quando o clique acontece
Então ele chega à entrada correspondente na lista de decisões citadas

Cenário: Nenhuma citação sem lastro
Dado qualquer decisão citada
Quando ela é exibida
Então ela existe na base
```

---

# Sprint 3

---

### US-27 — Exportar as decisões do tema
`Should` · E5 · 5 SP · Sprint 3 · pronta · depende de US-15

> Como **usuário**, quero exportar para CSV as decisões que sustentam o tema, para que eu
> possa trabalhar os dados fora da ferramenta.

**Regras de negócio**

- O arquivo é gerado pelo servidor a partir dos mesmos dados da tela — nunca montado no navegador.
- Ele contém as mesmas linhas que a tela exibiria para o mesmo filtro: sem divergência entre tela e arquivo.
- O arquivo declara fonte, data de extração e escopo territorial.
- Um campo sem fonte vem como coluna vazia, nunca preenchido.
- Existe um teto de linhas declarado, e a interface informa qual é ele em vez de falhar sem explicação.
**Critérios de aceite**

```gherkin
Cenário: A exportação corresponde à tela
Dado um tema com um filtro aplicado
Quando o usuário exporta para CSV
Então o arquivo contém as mesmas linhas que a tela exibiria para aquele filtro

Cenário: O arquivo declara sua procedência
Dado um arquivo exportado
Quando ele é aberto
Então ele declara fonte, data de extração e escopo territorial

Cenário: Planilha em português
Dado uma planilha configurada em português
Quando o arquivo é aberto
Então números, datas e caracteres acentuados são exibidos corretamente

Cenário: Volume acima do teto
Dado um tema com mais decisões que o teto de exportação
Quando o usuário exporta
Então a interface informa o teto em vez de falhar silenciosamente
```

---

### US-28 — Copiar a citação pronta para colar
`Should` · E5 · 3 SP · Sprint 3 · pronta · depende de US-25

> Como **usuário**, quero copiar a citação do tema já com a fonte, a data de extração, o
> escopo e o `n`, para que eu possa colá-la sem redigitar.

**Regras de negócio**

- O texto copiado é texto puro, de uma ou duas linhas, sem marcação de formatação e sem quebra de linha que obrigue a reeditar.
- Nada sem lastro entra na citação.
- Existe uma confirmação visível de que a cópia aconteceu.
**Critérios de aceite**

```gherkin
Cenário: Copiar e colar
Dado que o usuário copia a citação do tema
Quando ele a cola
Então ela contém o número, o n, a fonte, a data de extração e o escopo territorial

Cenário: Confirmação visível
Dado que a citação foi copiada
Quando o usuário olha para a tela
Então há uma confirmação visível da ação

Cenário: Bloco sem fonte
Dado um bloco sem fonte
Quando a citação é montada
Então nada sem lastro entra nela
```

---

### US-29 — Saber se o dado está atual
`Should` · E5 · 3 SP · Sprint 3 · aguardando decisão 16 · depende de US-25

> Como **usuário**, quero saber quando o dado foi atualizado pela última vez, e ser avisado
> quando ele estiver desatualizado, para que eu não me apoie em um retrato de meses atrás.

**Regras de negócio**

- Toda tela com número exibe a data da última extração.
- Passado o limite definido na decisão 16, há um aviso explícito de que o dado está desatualizado.
- Depois de uma carga falhando por dias, o produto não pode apresentar dado desatualizado com aparência de atual — esse é o pior caso para quem o cita.
**Critérios de aceite**

```gherkin
Cenário: Data de extração visível
Dado qualquer tela que exiba números
Quando ela é renderizada
Então a data da última extração fica visível

Cenário: Dado desatualizado
Dado que a última extração é mais antiga que o limite definido
Quando o usuário abre a tela
Então há um aviso explícito de que o dado está desatualizado

Cenário: Carga falhando há dias
Dado que a carga falhou por vários dias
Quando o usuário usa o produto
Então ele não apresenta dado desatualizado com aparência de dado atual
```

---

### US-30 — Saber quanto tempo leva até uma decisão
`Could` · E6 · 8 SP · Sprint 3 · aguardando decisão 1 · depende de —

> Como **usuário**, quero saber quanto tempo costuma levar da distribuição até a decisão neste
> tema, para que eu possa calibrar a expectativa do meu cliente.

**Pré-condição da DoR:** a decisão 1 precisa ter escolhido o grão de **movimentação**. Com
grão de julgamento essa métrica não pode ser calculada, e a história sai do backlog em vez de
ser entregue como aproximação.

**Regras de negócio**

- A métrica exibe a tendência central do tempo decorrido entre distribuição e decisão, com seu `n`.
- Processos sem decisão não entram, e isso é declarado — a média dos já decididos não é a média de todos.
- A abertura da métrica (por tribunal, por instância) é declarada, e a ressalva de que esse é tempo observado no escopo carregado, não uma previsão, fica visível.
**Critérios de aceite**

```gherkin
Cenário: Tempo decorrido com sua base
Dado um tema com processos decididos
Quando a métrica é exibida
Então ela exibe a tendência central com seu n

Cenário: Processos sem decisão
Dado processos ainda sem decisão
Quando a métrica é calculada
Então eles não entram, e a tela declara isso

Cenário: Não é uma previsão
Dado que a métrica está exibida
Quando o usuário a lê
Então a ressalva de que é tempo observado, não previsão, fica visível
```

---

### US-34 — Perguntar em linguagem natural
`Should` · E7 · 13 SP · Sprint 3 · aguardando decisão 18 · depende de US-01, US-09

> Como **usuário**, quero perguntar a um chatbot sobre um tema em linguagem natural e receber
> a resposta em prosa com os números, para as perguntas que nenhum filtro de tela responde.

**Pré-condição da DoR:** agregados estáveis, e as consultas das telas já expostas como funções
parametrizadas validadas, sem SQL livre. Antes disso, o chatbot responderia números que as
telas ainda não confirmam.

**Regras de negócio**

- **Todo número de uma resposta vem de uma consulta**; o modelo apenas interpreta a pergunta e escreve a prosa.
- O chatbot usa as mesmas consultas das telas, de modo que a mesma pergunta feita nos dois lugares devolve números idênticos.
- O chatbot descreve o que o dado mostra. Ele não dá consultoria jurídica: "o pedido foi julgado procedente em 82% dos casos" é dado; "ajuíze esta ação" não é o produto.
- O chatbot aparece onde a decisão 18 o posicionar.
**Critérios de aceite**

```gherkin
Cenário: Uma pergunta que nenhum filtro responde
Dado uma pergunta como "este tema é mais favorável em SP ou em MG?"
Quando o usuário a faz
Então ele recebe uma resposta em prosa com os números

Cenário: Os mesmos números da tela
Dado a mesma pergunta feita na tela e no chat
Quando ambos respondem
Então os números são idênticos

Cenário: Sem consultoria jurídica
Dado que o usuário pede um conselho
Quando o chatbot responde
Então ele descreve o que o dado mostra e não diz ao usuário o que fazer
```

---

### US-35 — Poder conferir o que o chatbot respondeu
`Should` · E7 · 5 SP · Sprint 3 · pronta · depende de US-34

> Como **usuário**, quero que toda resposta do chatbot traga o `n`, a fonte, a data de
> extração, o escopo e o link para os processos, para que eu possa conferi-la antes de usá-la.

**Regras de negócio**

- Todo percentual de uma resposta carrega seu `n`; todo número carrega sua fonte e data de extração.
- Uma afirmação sobre um tema carrega um caminho até os processos por trás dela.
- Uma pergunta sobre "os tribunais brasileiros" é respondida para os tribunais do escopo, **dizendo quantos são** — nunca sugerindo cobertura nacional.
- Existe uma suíte de avaliação com perguntas de resposta conhecida, conferidas contra a consulta direta, rodando em CI. Ela é **pré-condição para expor o chatbot**.
**Critérios de aceite**

```gherkin
Cenário: Percentual com sua base
Dado qualquer percentual em uma resposta
Quando ele é exibido
Então ele carrega seu n, sua fonte e sua data de extração

Cenário: Pergunta que sugere cobertura nacional
Dado uma pergunta sobre "os tribunais brasileiros"
Quando ela é respondida
Então a resposta cobre os tribunais do escopo e diz quantos são

Cenário: A suíte de avaliação pega a divergência
Dado uma pergunta de resposta conhecida cujo número diverge da consulta direta
Quando a suíte roda em CI
Então ela falha
```

---

### US-36 — Receber "não sei" em vez de um número inventado
`Should` · E7 · 3 SP · Sprint 3 · pronta · depende de US-34

> Como **usuário**, quero que o chatbot diga que não sabe quando o dado não está na base, para
> que eu não receba um número plausível e inventado.

**Regras de negócio**

- Quando o dado não está na base, a resposta diz isso explicitamente.
- O chatbot não inventa jurisprudência para um tema que não existe na base.
- Todo número de uma resposta corresponde a um valor devolvido por uma daquelas funções de consulta — conferido pela suíte de avaliação, que falha se um número não tiver essa origem.
**Critérios de aceite**

```gherkin
Cenário: Dado que não está na base
Dado uma pergunta cujo dado não está na base
Quando ela é respondida
Então a resposta diz explicitamente que aquele dado não está lá

Cenário: Tema que não existe
Dado um tema que não existe na base
Quando o usuário pergunta sobre ele
Então o chatbot não inventa jurisprudência

Cenário: Bloco sem fonte confirmada
Dado uma pergunta sobre um bloco sem fonte confirmada
Quando ela é respondida
Então a resposta diz que aquilo está fora do escopo dos dados, e por quê

Cenário: Todo número rastreado até uma consulta
Dado uma resposta contendo números
Quando a suíte de avaliação roda
Então todo número corresponde a um valor devolvido por uma função de consulta, e a suíte falha caso contrário
```