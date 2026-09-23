# Ratio
> (do latim: razão, fundamento). De *ratio decidendi* — o fundamento determinante de uma
> decisão judicial, o que de fato se repete e se torna padrão.

Veja a versão em inglês da documentação [aqui](../../README.md)

![home](../../Assets/home.jpeg)

## Sumário
- [Introdução](#introdução)
- [Principais funcionalidades](#principais-funcionalidades)
- [Product Backlog](#product-backlog)
  - [Disitribuição por Sprint](#distribuição-por-sprint)
  - [Escala de Estimativa](#escala-de-estimativa)
- [Critérios de Aceitação](Docs/pt_br/Scrum/acceptance-criteria.md)
- [DoD](Docs/pt_br/Scrum/definition-of-done.md)
- [DoR](Docs/pt_br/Scrum/definition-of-ready.md)
- [Meta do produto](Docs/pt_br/Scrum/product-goal.md)
- [Requisitos Funcionais](Docs/pt_br/functional-requirements.md)
- [Requisitos Não Funcionais](Docs/pt_br/non-functional-requirements.md)
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
- **Acesso à jurisprudência e à doutrina relacionadas** — para manter tudo rastreável, todo processo por trás de um tema leva de volta ao tribunal, e a doutrina relacionada a ele continua acessível.

# Product Backlog

| ID | Prioridade | Descrição | Estimativa | Sprint |
| --- | --- | --- | --- | --- |
| **US-01** | Must | Como **usuário**, quero digitar o tema do meu caso em linguagem natural e receber temas jurídicos curados — não uma lista de processos — para descobrir como ele vem sendo decidido sem garimpar um acórdão por vez | 8 | Sprint 1 |
| **US-02** | Must | Como **usuário**, quero os resultados ordenados por quão consolidado está o entendimento, e não por relevância de texto, para encontrar primeiro o que sustenta minha tese | 2 | Sprint 1 |
| **US-09** | Must | Como **usuário**, quero ler o entendimento do tema em prosa, abrindo com o número que responde à pergunta e com a contagem de casos ao lado de cada percentual, para entender o padrão sem abrir uma tabela | 8 | Sprint 1 |
| **US-10** | Must | Como **usuário**, quero ver a distribuição de resultados do tema em uma figura com a fonte declarada, para ver de relance quanto é procedente, parcialmente procedente e improcedente | 5 | Sprint 1 |
| **US-21** | Must | Como **usuário**, quero ver a doutrina relacionada ao tema, com autor, obra e link para o artigo quando houver, para saber o que citar além da jurisprudência | 8 | Sprint 1 |
| **US-24** | Must | Como **usuário**, quero que toda tela deixe claro que os dados cobrem TJSP, TJRJ e TJMG, para não tirar uma conclusão nacional de um percentual que reflete três estados | 2 | Sprint 1 |
| **US-25** | Must | Como **usuário**, quero saber a fonte e a data de extração de todo número que estou vendo, para saber exatamente o que estou citando | 3 | Sprint 1 |
| **US-26** | Must | Como **usuário**, quero que a tela me diga o que não existe e por quê, em vez de mostrar um campo vazio ou um valor plausível, para não construir uma peça sobre dado que não existe | 3 | Sprint 1 |
| **US-03** | Must | Como **usuário**, quero ver em cada resultado o score, a área do direito, o título da tese, um resumo curto, os tribunais, o volume, o período, a última decisão e o percentual favorável, para comparar teses antes de abrir qualquer uma delas | 8 | Sprint 2 |
| **US-04** | Must | Como **usuário**, quero filtrar os resultados por tribunal, período, instância e força mínima, vendo quantos processos cada tribunal tem, para restringir a lista ao meu caso | 5 | Sprint 2 |
| **US-06** | Must | Como **usuário**, quero um score de 0 a 100 dizendo o quanto o entendimento sobre o tema está consolidado, para saber se a tese vale ser defendida ou é uma briga aberta | 8 | Sprint 2 |
| **US-07** | Must | Como **usuário**, quero que o score venha com uma classificação em linguagem que já existe no meio jurídico — Consolidada, Dominante, Em formação, Divergente — para não ter de interpretar uma escala inventada | 2 | Sprint 2 |
| **US-08** | Must | Como **usuário**, quero abrir a composição do score — os quatro componentes, seus pesos e a base de cálculo — para citar a estatística sabendo exatamente de onde ela vem | 3 | Sprint 2 |
| **US-11** | Must | Como **usuário**, quero ver como o alinhamento do tema evoluiu ano a ano, com a frase de tendência, para saber se o entendimento está se firmando ou mudando | 5 | Sprint 2 |
| **US-12** | Must | Como **usuário**, quero ver o alinhamento do tema por tribunal, para saber se a tese se sustenta igual em São Paulo, Rio de Janeiro e Minas Gerais | 3 | Sprint 2 |
| **US-14** | Must | Como **usuário**, quero uma tabela do comportamento de cada tribunal — decisões, alinhamento e data da mais recente — para comparar o meu tribunal com os outros | 3 | Sprint 2 |
| **US-15** | Must | Como **usuário**, quero uma amostra auditável dos processos por trás do tema, com câmara, data e resultado, para conferir os casos antes de citá-los | 5 | Sprint 2 |
| **US-17** | Should | Como **usuário**, quero saber se as câmaras do meu tribunal estão decidindo igual, para identificar divergência interna antes de decidir | 5 | Sprint 2 |
| **US-27** | Should | Como **usuário**, quero exportar para CSV as decisões que sustentam o tema, para trabalhar os dados fora da ferramenta | 5 | Sprint 3 |
| **US-28** | Should | Como **usuário**, quero copiar a citação do tema já com a fonte, a data de extração, o escopo e o `n`, para colar sem redigitar | 3 | Sprint 3 |
| **US-29** | Should | Como **usuário**, quero saber quando os dados foram atualizados pela última vez, e ser avisado quando estiverem defasados, para não me apoiar em um retrato de meses atrás | 3 | Sprint 3 |
| **US-13** | Could | Como **usuário**, quero que a aba que estou vendo seja refletida na URL, para enviar a um colega o link exato da parte que quero mostrar | 5 | Sprint 1 |
| **US-38** | Could | Como **usuário**, quero sugestões de consultas frequentes na tela inicial, para entender que tipo de pergunta a ferramenta responde antes de digitar a minha | 2 | Sprint 2 |
| **US-19** | Could | Como **usuário**, quero ver os fundamentos invocados nas decisões do tema, com a frequência e a taxa de acolhimento de cada um, para escolher o argumento que mais vence e evitar o que sempre perde | 8 | Sprint 2 |
| **US-37** | Could | Como **usuário**, quero ver no texto do entendimento o acórdão que sustenta cada afirmação, com a referência completa e a lista de decisões citadas ao pé, para poder citar a mesma decisão | 8 | Sprint 2 |
| **US-30** | Could | Como **usuário**, quero saber quanto tempo normalmente se leva do ajuizamento à decisão neste tema, para calibrar a expectativa do meu cliente | 8 | Sprint 3 |
| **US-34** | Could | Como **usuário**, quero perguntar a um chatbot sobre um tema em linguagem natural e receber a resposta em prosa com os números, para as perguntas que nenhum filtro de tela responde | 13 | Sprint 3 |
| **US-35** | Could | Como **usuário**, quero que toda resposta do chatbot traga o `n`, a fonte, a data de extração, o escopo e o link para os processos, para poder conferir antes de usar | 5 | Sprint 3 |
| **US-36** | Could | Como **usuário**, quero que o chatbot diga que não sabe quando o dado não está na base, para não receber um número plausível e inventado | 3 | Sprint 3 |

## Distribuição por sprint

| Sprint | Janela | Histórias | Pontos |
| --- | --- | --- | --- |
| **Sprint 1** | 07/09 – 27/09 | 9 | 44 |
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
- **Feature branching + uma branch por user story**
- **main:** branch principal e estável do projeto. Recebe merge a cada user story concluída, após revisão e aprovação.
- **usX** (ex.: `us1`, `us9`, `us21`): cada user story tem sua própria branch base, com o número da US sem zero à esquerda, onde se integram todas as tasks daquela história.
- **us0:** a branch base do **Technical Foundation** — as tasks `0.Y` (schema, pipeline, esqueleto do frontend), que não pertencem a nenhuma user story.
- **id-da-task-nome-da-task-com-hifens-no-lugar-dos-espacos:** cada task tem sua própria branch, criada a partir da branch da user story a que pertence e mergeada de volta nela. O nome é o ID da task seguido do título dela no board, sem referência à user story — o ID já diz a que história ela pertence (`1.1` é da US-01, `0.12` do Technical Foundation). Sem acento, crase, aspas ou barra. Exemplo: `0.12-Create-the-dw-schema-migration-and-apply-it-on-API-startup`
- **Proteção:** ninguém dá push direto na `main` nem numa branch `usX`. Toda mudança entra por pull request, a partir de uma branch de task.
- **Repositório de documentação:** como as branches deste repositório não estão vinculadas a tarefas, seguem um padrão diferente. Levam o nome da aplicação, a palavra "**DOCS**" e uma descrição do que está sendo feito — por exemplo, `RATIO-DOCS-Definition-of-Done`, `RATIO-DOCS-Product-Backlog`
### Commits
**Todo commit em qualquer repositório deste projeto deve ser escrito em inglês.**
Cada commit deve ser pequeno, descritivo e direto, seguindo a convenção semântica:

- `feat:` descrição da nova funcionalidade
- `fix:` correção de bug ou comportamento inesperado
- `refactor:` melhoria de código sem mudança de comportamento
- `docs:` atualização de documentação
- `test:` adição ou alteração de testes do projeto — unidade, integração, contrato, ponta a ponta
- `chore:` configuração, build ou manutenção

O commit leva **só a linha do assunto**, sem corpo descritivo.

Exemplo: `feat: add semantic search by legal topic`

### Releases
Todo pull request para a `main` leva **exatamente um** label `release:*`. É ele que decide a versão `vX.Y.Z` publicada no merge. A release é criada automaticamente depois que o CI da `main` passa.

| Label | Quando usar | Efeito na versão | Exemplo |
|---|---|---|---|
| `release:sprint` | último PR para a `main` da sprint (a entrega da sprint) | sobe o **X** e zera Y e Z | `v1.2.1` → `v2.0.0` |
| `release:us` | user story concluída (PR `usX` → `main`) | sobe o **Y** e zera o Z | `v1.2.1` → `v1.3.0` |
| `release:fix` | correção que vai direto para a `main` | sobe o **Z** | `v1.2.1` → `v1.2.2` |
| `release:none` | mudança sem efeito para o cliente (CI, documentação) | não publica release | — |

- **X** conta as sprints entregues, **Y** as user stories entregues desde a última sprint e **Z** as correções desde a última user story.
- A versão sobe de sprint **no fim** dela: o `release:sprint` vai no último PR da sprint para a `main`. Se no fim não sobrar PR de user story, abre-se um PR só da entrega com esse label.
- Task não gera versão, porque o PR dela vai para a `usX`, não para a `main`. Correção dentro de uma user story em andamento também não: ela entra na própria `usX`.
- Antes da primeira entrega, as versões ficam em `0.Y.Z`. A primeira sprint entregue gera a `v1.0.0`.
- Cada repositório tem a própria numeração: a `v1.2.0` do backend não corresponde à `v1.2.0` do frontend.

Exemplo de uma sprint:

| Evento | Label | Versão |
|---|---|---|
| US-01 concluída | `release:us` | `v0.1.0` |
| correção na `main` | `release:fix` | `v0.1.1` |
| US-02 concluída | `release:us` | `v0.2.0` |
| última US da sprint 1 | `release:sprint` | `v1.0.0` |
| primeira US da sprint 2 | `release:us` | `v1.1.0` |
