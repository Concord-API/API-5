# Requisitos funcionais

O que o produto faz, derivado do Product Backlog. Cada requisito rastreia a user story de origem.

### Busca e descoberta

| # | Requisito | Origem |
| --- | --- | --- |
| RF-01 | Buscar temas a partir de texto livre em português, retornando temas jurídicos apurados e não processos. | US-01 |
| RF-02 | Realizar a busca full-text tolerando ausência de acento e erro de digitação. | US-01 |
| RF-03 | Ordenar os resultados pela nota de firmeza, em ordem decrescente, desempatando pelo volume de decisões. | US-02 |
| RF-04 | Filtrar os resultados por tribunal, período, grau e força mínima, de forma combinável. | US-04 |
| RF-05 | Exibir a quantidade de processos de cada tribunal nas opções de filtro. | US-04 |
| RF-06 | Separar teses distintas agrupadas sob o mesmo assunto do CNJ, exibindo o assunto de origem em cada tema. | US-05 |
| RF-07 | Exibir sugestões de consultas frequentes na tela inicial. | US-38 |

### Apresentação do tema

| # | Requisito | Origem |
| --- | --- | --- |
| RF-08 | Exibir, em cada resultado, a nota, a matéria, o título da tese, o resumo, os tribunais, o volume, o período, a última decisão e o percentual favorável. | US-03 |
| RF-09 | Refletir a aba corrente na URL e abrir a página diretamente na aba indicada. | US-13 |

### Nota de firmeza

| # | Requisito | Origem |
| --- | --- | --- |
| RF-10 | Calcular uma nota de firmeza de 0 a 100 para cada tema. | US-06 |
| RF-11 | Classificar a nota em grau: Consolidada, Dominante, Em formação ou Divergente. | US-07 |
| RF-12 | Permitir abrir a composição da nota — os quatro componentes, seus pesos e a base de cálculo. | US-08 |

### Análise do entendimento

| # | Requisito | Origem |
| --- | --- | --- |
| RF-13 | Apresentar o entendimento do tema em prosa, abrindo com o número que responde à pergunta central. | US-09 |
| RF-14 | Acompanhar todo percentual exibido do respectivo método de apuração. | US-09, US-25 |
| RF-15 | Exibir a distribuição dos desfechos — procedente, parcialmente procedente e improcedente — em figura com a fonte declarada. | US-10 |
| RF-16 | Exibir a evolução anual do alinhamento do tema, acompanhada da frase de tendência. | US-11 |
| RF-17 | Exibir o alinhamento do tema por tribunal. | US-12 |
| RF-18 | Exibir tabela do comportamento de cada tribunal, com decisões, alinhamento e data da última decisão. | US-14 |
| RF-19 | Indicar divergência interna entre as câmaras de um mesmo tribunal. | US-17 |
| RF-20 | Exibir os fundamentos invocados nas decisões, com a frequência e a taxa de acolhimento de cada um. | US-19 |
| RF-21 | Exibir o tempo médio entre o ajuizamento e a decisão no tema. | US-30 |

### Rastreabilidade das decisões

| # | Requisito | Origem |
| --- | --- | --- |
| RF-22 | Exibir amostra auditável dos processos que sustentam o tema, com órgão julgador, data e desfecho. | US-15 |
| RF-23 | Exibir o nome do relator na amostra e na referência da citação. | US-22 |
| RF-24 | Permitir a leitura do inteiro teor da decisão citada. | US-23 |
| RF-25 | Vincular cada afirmação do texto do entendimento ao acórdão que a sustenta, com a lista das decisões citadas ao pé. | US-37 |
| RF-26 | Exibir os precedentes qualificados ligados ao tema — súmula, tema repetitivo e IRDR — distinguindo o vinculante do persuasivo. | US-18 |
| RF-27 | Exibir a doutrina invocada com autor, obra, posição no debate e link para o artigo quando houver. | US-21 |

### Procedência e transparência

| # | Requisito | Origem |
| --- | --- | --- |
| RF-28 | Exibir o escopo TJSP, TJRJ e TJMG em toda tela que apresente dado apurado. | US-24 |
| RF-29 | Exibir fonte, data de extração e método de apuração de cada número, omitindo o número quando a procedência não estiver registrada. | US-25 |
| RF-30 | Informar o que não existe e por quê, sem exibir campo vazio nem valor estimado. | US-26 |
| RF-31 | Informar a data da última atualização do dado e avisar quando ele estiver desatualizado. | US-29 |

### Saída de dados

| # | Requisito | Origem |
| --- | --- | --- |
| RF-32 | Exportar em CSV as decisões que sustentam o tema. | US-27 |
| RF-33 | Copiar a citação do tema já com fonte, data de extração, escopo e método de apuração. | US-28 |

### Consulta em linguagem natural

| # | Requisito | Origem |
| --- | --- | --- |
| RF-34 | Responder perguntas em linguagem natural sobre um tema, em prosa e com os números. | US-34 |
| RF-35 | Trazer, em toda resposta do chatbot, o método de apuração, a fonte, a data de extração, o escopo e o link para os processos. | US-35 |
| RF-36 | Responder que não sabe quando o dado não estiver na base, em vez de produzir um número plausível. | US-36 |
