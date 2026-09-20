# Requisitos Funcionais

O que o produto faz, derivado do [Product Backlog](Scrum/product-backlog.md). Todo
requisito remete à história de usuário de que se origina.

## Busca e descoberta

| # | Requisito | Origem |
| --- | --- | --- |
| FR-01 | Buscar temas a partir de texto livre em português, devolvendo temas jurídicos curados e não processos. | US-01 |
| FR-02 | Executar a busca full-text tolerando ausência de acentos e erros de digitação. | US-01 |
| FR-03 | Exibir, junto de cada tema, o assunto TPU de que ele vem, para que a granularidade do resultado fique explícita. | US-01 |
| FR-04 | Ordenar os resultados pelo score de força, em ordem decrescente, desempatando por volume de decisões. | US-02 |
| FR-05 | Filtrar os resultados por tribunal, período, instância e força mínima, de forma combinável. | US-04 |
| FR-06 | Exibir o número de processos por tribunal nas opções do filtro. | US-04 |
| FR-07 | Exibir consultas frequentes sugeridas na tela inicial, extraídas de dados reais do escopo carregado. | US-38 |

## Apresentação do tema

| # | Requisito | Origem |
| --- | --- | --- |
| FR-08 | Exibir, em cada resultado, o score, a área do direito, o título da tese, o resumo, os tribunais, o volume, o período, a última decisão e o percentual favorável. | US-03 |

## Score de força

| # | Requisito | Origem |
| --- | --- | --- |
| FR-10 | Calcular um score de força de 0 a 100 para cada tema, a partir de concordância, volume, cobertura e recência. | US-06 |
| FR-11 | Classificar o score em um grau: Consolidada, Dominante, Em formação ou Divergente. | US-07 |
| FR-12 | Omitir o grau textual abaixo do número mínimo de julgados, exibindo apenas o score. | US-07 |
| FR-13 | Permitir abrir a composição do score — os quatro componentes, seus pesos e a base de cálculo. | US-08 |

## Análise do entendimento

| # | Requisito | Origem |
| --- | --- | --- |
| FR-14 | Apresentar o entendimento do tema em prosa, abrindo com o número que responde à pergunta central. | US-09 |
| FR-15 | Acompanhar todo percentual exibido da contagem de processos (`n`) a partir da qual ele foi calculado. | US-09, US-25 |
| FR-16 | Exibir a distribuição dos resultados — procedente, parcialmente procedente e improcedente — em uma figura com a fonte declarada. | US-10 |
| FR-17 | Exibir a evolução anual do alinhamento do tema, com a frase de tendência. | US-11 |
| FR-18 | Exibir o alinhamento do tema por tribunal. | US-12 |
| FR-19 | Exibir uma tabela do comportamento de cada tribunal, com decisões, alinhamento e a data da decisão mais recente. | US-14 |
| FR-20 | Sinalizar divergência interna entre as câmaras de um mesmo tribunal. | US-17 |
| FR-21 | Exibir os fundamentos invocados nas decisões, com a frequência e a taxa de acolhimento de cada um. | US-19 |
| FR-22 | Exibir o tempo típico decorrido entre a distribuição e a decisão no tema. | US-30 |

## Rastreabilidade das decisões

| # | Requisito | Origem |
| --- | --- | --- |
| FR-23 | Exibir uma amostra auditável dos processos por trás do tema, com câmara, data e resultado. | US-15 |
| FR-26 | Vincular cada afirmação do texto do entendimento ao acórdão que a sustenta, com a lista de decisões citadas ao pé. | US-37 |
| FR-28 | Exibir a doutrina relacionada ao tema, com autor, obra, o score de similaridade da associação e link para o artigo quando houver. | US-21 |

## Procedência e transparência

| # | Requisito | Origem |
| --- | --- | --- |
| FR-29 | Exibir o escopo TJSP, TJRJ e TJMG em toda tela que apresenta dado calculado. | US-24 |
| FR-30 | Exibir a fonte, a data de extração e o método por trás de cada número, omitindo o número quando a procedência não está registrada. | US-25 |
| FR-31 | Declarar o que não existe e por quê, sem exibir campo vazio nem valor estimado. | US-26 |
| FR-32 | Informar quando o dado foi atualizado pela última vez e alertar quando ele estiver desatualizado. | US-29 |

## Saída de dados

| # | Requisito | Origem |
| --- | --- | --- |
| FR-33 | Exportar para CSV as decisões que sustentam o tema, no servidor, correspondendo ao que a tela exibe para o mesmo filtro. | US-27 |
| FR-34 | Copiar a citação do tema já com fonte, data de extração, escopo e `n`. | US-28 |

## Consulta em linguagem natural

| # | Requisito | Origem |
| --- | --- | --- |
| FR-35 | Responder perguntas em linguagem natural sobre um tema, em prosa e com os números, sobre os mesmos agregados que as telas usam. | US-34 |
| FR-36 | Trazer, em toda resposta do chatbot, a fonte, a data de extração, o escopo e o link para os processos. | US-35 |
| FR-37 | Responder que não sabe quando o dado não está na base, em vez de produzir um número plausível. | US-36 |