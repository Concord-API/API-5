# Ratio
> (do latim: razão, fundamento). De *ratio decidendi* — o fundamento determinante de uma
> decisão judicial, o que de fato se repete e se torna padrão.

Veja a versão em inglês da documentação [aqui](../../README.md)

![home](../../Assets/home.jpeg)

## Sumário
- [Introdução](#introdução)
- [Principais funcionalidades](#principais-funcionalidades)
- [Time](#time)
- [Como contribuir](#como-contribuir)
  - [Branches](#branches)
  - [Commits](#commits)

## Introdução
O Ratio se propõe a eliminar o trabalho manual e fragmentado de análise de jurisprudência que impede advogados e juízes de identificar com segurança onde os tribunais se posicionam sobre uma tese — permitindo avaliar rapidamente sua aceitação, recorrência e grau de consolidação para fundamentar decisões e estratégias jurídicas. Para isso, centraliza e analisa jurisprudência, precedentes e doutrina do TJSP, TJRJ e TJMG em um Data Warehouse jurídico, com busca semântica por tema e geração de indicadores e padrões decisórios rastreáveis até suas fontes originais.

## Principais funcionalidades
- **Busca de temas em linguagem natural** — o usuário descreve o caso com as próprias palavras e recebe o tema jurídico já identificado, sem precisar montar sintaxe de busca nem saber o nome técnico da tese.
- **Padrão decisório consolidado** — taxa de acolhimento, volume de processos e tribunais envolvidos, calculados automaticamente. Elimina a tabulação manual de decisões em planilha.
- **Score de força do entendimento** — mostra o quanto aquele padrão está consolidado (ou instável), ponderando concordância entre as decisões, volume, cobertura e atualidade.
- **Rastreabilidade** — todo número exibido leva de volta à sua fonte e data de extração; nenhuma métrica é inventada ou calculada no escuro.
- **Cobertura multitribunal** — dados centralizados de TJSP, TJRJ e TJMG, os três tribunais com maior volume processual do país.
- **Acesso a precedentes e doutrina relacionados** — para manter tudo rastreável, todos os precedentes e obras doutrinárias usados para resumir um tema permanecem acessíveis.

# Product Backlog
| ID | Prioridade | Descrição | Estimativa | Sprint |
| --- | --- | --- | --- | --- |
| **US-01** | Must | Como **usuário**, quero digitar o tema do meu caso em linguagem natural e receber temas jurídicos curados — não uma lista de processos — para descobrir como ele vem sendo decidido sem garimpar um acórdão por vez | 8 | Sprint 1 |
| **US-02** | Must | Como **usuário**, quero os resultados ordenados por quão consolidado está o entendimento, e não por relevância de texto, para encontrar primeiro o que sustenta minha tese | 2 | Sprint 1 |
| **US-04** | Must | Como **usuário**, quero filtrar os resultados por tribunal, período, instância e força mínima, vendo quantos processos cada tribunal tem, para restringir a lista ao meu caso | 5 | Sprint 1 |
| **US-09** | Must | Como **usuário**, quero ler o entendimento do tema em prosa, abrindo com o número que responde à pergunta e com a contagem de casos ao lado de cada percentual, para entender o padrão sem abrir uma tabela | 8 | Sprint 1 |
| **US-10** | Must | Como **usuário**, quero ver a distribuição de resultados do tema em uma figura com a fonte declarada, para ver de relance quanto é procedente, parcialmente procedente e improcedente | 5 | Sprint 1 |
| **US-18** | Could | Como **usuário**, quero ver os precedentes qualificados vinculados ao tema — súmula, tema repetitivo, IRDR — distinguindo o que é vinculante do que é meramente persuasivo, para saber o que me obriga | 8 | Sprint 1 |
| **US-21** | Must | Como **usuário**, quero ver a doutrina invocada, com autor, obra e sua posição no debate, com link para o artigo quando houver, para saber o que citar além da jurisprudência | 8 | Sprint 1 |
| **US-23** | Could | Como **usuário**, quero ler o texto integral da decisão citada na aplicação, para conferir o contexto antes de usá-la | 5 | Sprint 1 |
| **US-24** | Must | Como **usuário**, quero que toda tela deixe claro que os dados cobrem TJSP, TJRJ e TJMG, para não tirar uma conclusão nacional de um percentual que reflete três estados | 2 | Sprint 1 |
| **US-25** | Must | Como **usuário**, quero saber a fonte e a data de extração de todo número que estou vendo, para saber exatamente o que estou citando | 3 | Sprint 1 |
| **US-26** | Must | Como **usuário**, quero que a tela me diga o que não existe e por quê, em vez de mostrar um campo vazio ou um valor plausível, para não construir uma peça sobre dado que não existe | 3 | Sprint 1 |
| **US-03** | Must | Como **usuário**, quero ver em cada resultado o score, a área do direito, o título da tese, um resumo curto, os tribunais, o volume, o período, a última decisão e o percentual favorável, para comparar teses antes de abrir qualquer uma delas | 8 | Sprint 2 |
| **US-38** | Could | Como **usuário**, quero sugestões de consultas frequentes na tela inicial, para entender que tipo de pergunta a ferramenta responde antes de digitar a minha | 2 | Sprint 2 |
| **US-06** | Must | Como **usuário**, quero um score de 0 a 100 dizendo o quanto o entendimento sobre o tema está consolidado, para saber se a tese vale ser defendida ou é uma briga aberta | 8 | Sprint 2 |
| **US-07** | Must | Como **usuário**, quero que o score venha com uma classificação em linguagem que já existe no meio jurídico — Consolidada, Dominante, Em formação, Divergente — para não ter de interpretar uma escala inventada | 2 | Sprint 2 |
| **US-08** | Must | Como **usuário**, quero abrir a composição do score — os quatro componentes, seus pesos e a base de cálculo — para citar a estatística sabendo exatamente de onde ela vem | 3 | Sprint 2 |
| **US-11** | Must | Como **usuário**, quero ver como o alinhamento do tema evoluiu ano a ano, com a frase de tendência, para saber se o entendimento está se firmando ou mudando | 5 | Sprint 2 |
| **US-12** | Must | Como **usuário**, quero ver o alinhamento do tema por tribunal, para saber se a tese se sustenta igual em São Paulo, Rio de Janeiro e Minas Gerais | 3 | Sprint 2 |
| **US-14** | Must | Como **usuário**, quero uma tabela do comportamento de cada tribunal — decisões, alinhamento e data da mais recente — para comparar o meu tribunal com os outros | 3 | Sprint 2 |
| **US-15** | Must | Como **usuário**, quero uma amostra auditável dos processos por trás do tema, com câmara, data e resultado, para conferir os casos antes de citá-los | 5 | Sprint 2 |
| **US-17** | Should | Como **usuário**, quero saber se as câmaras do meu tribunal estão decidindo igual, para identificar divergência interna antes de decidir | 5 | Sprint 2 |
| **US-19** | Could | Como **usuário**, quero ver os fundamentos invocados nas decisões do tema, com a frequência e a taxa de acolhimento de cada um, para escolher o argumento que mais vence e evitar o que sempre perde | 8 | Sprint 2 |
| **US-22** | Could | Como **usuário**, quero o nome do relator na amostra e na referência de citação, para montar a citação completa | 5 | Sprint 2 |
| **US-37** | Could | Como **usuário**, quero ver no texto do entendimento o acórdão que sustenta cada afirmação, com a referência completa e a lista de decisões citadas ao pé, para poder citar a mesma decisão | 8 | Sprint 2 |
| **US-27** | Should | Como **usuário**, quero exportar para CSV as decisões que sustentam o tema, para trabalhar os dados fora da ferramenta | 5 | Sprint 3 |
| **US-28** | Should | Como **usuário**, quero copiar a citação do tema já com a fonte, a data de extração, o escopo e o `n`, para colar sem redigitar | 3 | Sprint 3 |
| **US-29** | Should | Como **usuário**, quero saber quando os dados foram atualizados pela última vez, e ser avisado quando estiverem defasados, para não me apoiar em um retrato de meses atrás | 3 | Sprint 3 |
| **US-30** | Could | Como **usuário**, quero saber quanto tempo normalmente se leva do ajuizamento à decisão neste tema, para calibrar a expectativa do meu cliente | 8 | Sprint 3 |
| **US-34** | Could | Como **usuário**, quero perguntar a um chatbot sobre um tema em linguagem natural e receber a resposta em prosa com os números, para as perguntas que nenhum filtro de tela responde | 13 | Sprint 3 |
| **US-35** | Could | Como **usuário**, quero que toda resposta do chatbot traga o `n`, a fonte, a data de extração, o escopo e o link para os processos, para poder conferir antes de usar | 5 | Sprint 3 |
| **US-36** | Could | Como **usuário**, quero que o chatbot diga que não sabe quando o dado não está na base, para não receber um número plausível e inventado | 3 | Sprint 3 |

## Distribuição por sprint

| Sprint | Janela | Histórias | Pontos |
| --- | --- | --- | --- |
| **Sprint 1** | 07/09 – 27/09 | 13 | 62 |
| **Sprint 2** | 05/10 – 25/10 | 13 | 65 |
| **Sprint 3** | 02/11 – 22/11 | 7 | 40 |

## MoSCoW

| Prioridade | Significado |
| --- | --- |
| **Must** | Obrigatório para a entrega. Sem ele o produto não atende ao seu objetivo principal e não é avaliável. Priorizado à frente de tudo. |
| **Should** | Importante para uma entrega completa. O produto ainda funciona sem ele, mas sua ausência é perda real de qualidade, usabilidade ou cobertura. Entra se sobrar capacidade depois dos Must. |
| **Could** | Melhoria desejável. Agrega valor, mas não compromete a entrega se ficar de fora. Primeiro grupo a ser cortado quando tempo ou capacidade aperta. |
| **Won't** | Fora desta entrega. Analisado e deliberadamente não construído neste ciclo — registrado em *Fora de escopo* para não voltar como surpresa. |

## Escala de estimativa

| SP | Significado | Camadas | Incerteza |
| --- | --- | --- | --- |
| **1** | ajuste isolado: um texto, uma formatação | 1 | nenhuma |
| **2** | a última peça de algo que outra história já entregou | 1 | nenhuma |
| **3** | trabalho autocontido em uma camada: um bloco, uma tabela, um componente | 1 | nenhuma |
| **5** | duas camadas, ou uma regra que alguém precisa definir | 2 | alguma |
| **8** | vai do banco até a tela, ou o time nunca fez | 3+ | real |
| **13** | grande **e** incerta — topo da escala, candidata a ser quebrada no refinamento | todas | alta |

## Time
<div align="center">
  <table>
    <thead>
      <tr>
        <th align="center">Integrante</th>
        <th align="center">Função</th>
        <th align="center">GitHub</th>
      </tr>
    </thead>
    <tbody>
          <tr>
        <td align="center">Vinicius de Pádua</td>
        <td align="center">Product Owner</td>
        <td align="center"><a href="https://github.com/orgs/vp-p"><img src="https://cdn.simpleicons.org/github/181717" alt="GitHub" width="22" /></a></td>
      </tr>
      <tr>
        <td align="center">João Vitor Andrade</td>
        <td align="center">Scrum Master</td>
        <td align="center"><a href="https://github.com/joaoandrade17"><img src="https://cdn.simpleicons.org/github/181717" alt="GitHub" width="22" /></a></td>
      </tr>
      <tr>
        <td align="center">João Vitor Baranov</td>
        <td align="center">Desenvolvedor</td>
        <td align="center"><a href="https://github.com/JoaoBaranov"><img src="https://cdn.simpleicons.org/github/181717" alt="GitHub" width="22" /></a></td>
      </tr>
      <tr>
        <td align="center">Victor Nogueira</td>
        <td align="center">Desenvolvedor</td>
        <td align="center"><a href="https://github.com/victorgsnogueira"><img src="https://cdn.simpleicons.org/github/181717" alt="GitHub" width="22" /></a></td>
      </tr>
      <tr>
        <td align="center">Richard Cordeiro</td>
        <td align="center">Desenvolvedor</td>
        <td align="center"><a href="https://github.com/RichardCordeiro"><img src="https://cdn.simpleicons.org/github/181717" alt="GitHub" width="22" /></a></td>
      </tr>
      <tr>
        <td align="center">Isaac Oliveira</td>
        <td align="center">Desenvolvedor</td>
        <td align="center"><a href="https://github.com/IsaacOliveiraSouza"><img src="https://cdn.simpleicons.org/github/181717" alt="GitHub" width="22" /></a></td>
      </tr>
      <tr>
        <td align="center">Thiago Abreu</td>
        <td align="center">Desenvolvedor</td>
        <td align="center"><a href="https://github.com/thiagosabreu"><img src="https://cdn.simpleicons.org/github/181717" alt="GitHub" width="22" /></a></td>
      </tr>
    </tbody>
  </table>
</div>

## Como contribuir
### Branches
- **Feature branching + uma branch por sprint**
- **main:** branch principal e estável do projeto. Só recebe merges no fim de cada sprint, após revisão e aprovação.
- **sprintX** (ex.: sprint1, sprint2, sprint3): cada sprint tem sua própria branch base, onde toda feature construída naquele ciclo é integrada.
- **parenttask-subtask-nome-da-tarefa-com-hifens-se-tiver-espacos:** para cada nova feature ou correção, cria-se uma branch dedicada a partir da branch do sprint atual. A branch recebe o nome da tarefa no board. Exemplo: `RATIO-35-0.1-Implement-API-documentation`
- **Repositório de documentação:** como as branches deste repositório não estão vinculadas a tarefas, seguem um padrão diferente. Levam o nome da aplicação, a palavra "**DOCS**" e uma descrição do que está sendo feito — por exemplo, `RATIO-DOCS-Definition-of-Done`, `RATIO-DOCS-Product-Backlog`
### Commits
**Todo commit em qualquer repositório deste projeto deve ser escrito em inglês.**  
Cada commit deve ser pequeno, descritivo e direto, seguindo a convenção semântica:

- `feat:` descrição da nova funcionalidade
- `fix:` correção de bug ou comportamento inesperado
- `refactor:` melhoria de código sem mudança de comportamento
- `docs:` atualização de documentação
- `chore:` configuração, build ou manutenção

Exemplo: `feat: add semantic search by legal topic`