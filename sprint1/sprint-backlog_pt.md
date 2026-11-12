# Sprint Backlog — Sprint 1

**Janela:** 07/09 a 27/09/2026

**Board:** [GitHub Project](https://github.com/orgs/Concord-API/projects/5) · snapshot de 12/11/2026

## Meta da sprint

Stories que o time se compromete a entregar. Se alguma não for concluída, a sprint não atingiu a meta.

| ID | Prioridade | Descrição | SP | Tasks | Horas | Status |
| --- | --- | --- | ---: | ---: | ---: | --- |
| **US-01** | Must | Como **usuário**, quero digitar o tema do meu caso em linguagem natural e receber temas jurídicos curados — não uma lista de processos — para descobrir como ele vem sendo decidido sem garimpar um acórdão por vez | 8 | 13 | 49h | Concluído |
| **US-02** | Must | Como **usuário**, quero os resultados ordenados por quão consolidado está o entendimento, e não por relevância de texto, para encontrar primeiro o que sustenta minha tese | 2 | 6 | 20h | Concluído |
| **US-09** | Must | Como **usuário**, quero ler o entendimento do tema em prosa, abrindo com o número que responde à pergunta e com a contagem de casos ao lado de cada percentual, para entender o padrão sem abrir uma tabela | 8 | 9 | 35h | Concluído |
| **US-21** | Must | Como **usuário**, quero ver a doutrina relacionada ao tema, com autor, obra e link para o artigo quando houver, para saber o que citar além da jurisprudência | 8 | 9 | 25h | Concluído |
| **US-24** | Must | Como **usuário**, quero que toda tela deixe claro que os dados cobrem TJSP, TJRJ e TJMG, para não tirar uma conclusão nacional de um percentual que reflete três estados | 2 | 3 | 9h | Concluído |
| **US-25** | Must | Como **usuário**, quero saber a fonte e a data de extração de todo número que estou vendo, para saber exatamente o que estou citando | 3 | 7 | 23h | Concluído |
| **US-26** | Must | Como **usuário**, quero que a tela me diga o que não existe e por quê, em vez de mostrar um campo vazio ou um valor plausível, para não construir uma peça sobre dado que não existe | 3 | 6 | 17h | Concluído |

## Fora da meta

Stories planejadas na sprint, mas que podem passar para a próxima se não houver capacidade, mesmo sendo prioridade.

| ID | Prioridade | Descrição | SP | Tasks | Horas | Status |
| --- | --- | --- | ---: | ---: | ---: | --- |
| **US-10** | Must | Como **usuário**, quero ver a distribuição de resultados do tema em uma figura com a fonte declarada, para ver de relance quanto é procedente, parcialmente procedente e improcedente | 5 | 6 | 21h | Concluído |

## Resumo da sprint

| | Total |
| --- | ---: |
| Stories (meta / fora da meta) | 7 / 1 |
| Story points (meta / total) | 34 / 39 |
| Tasks (concluídas / total) | 79 / 79 |
| Horas (feitas / total) | 279h / 279h |
| Tasks em stories | 59 (199h) |
| Technical Foundation | 20 (80h) |
| Entrega e processo | 0 (0h) |

### Horas por responsável

| Responsável | Tasks | Horas | Concluído |
| --- | ---: | ---: | ---: |
| victorgsnogueira | 44 | 157h | 157h |
| RichardCordeiro | 13 | 43h | 43h |
| thiagosabreu | 6 | 30h | 30h |
| JoaoBaranov | 8 | 28h | 28h |
| IsaacOliveiraSouza | 8 | 21h | 21h |

### Horas por camada

| Camada | Horas | Concluído |
| --- | ---: | ---: |
| Backend | 104h | 104h |
| Frontend | 85h | 85h |
| ETL | 53h | 53h |
| Test | 16h | 16h |
| DevOps | 11h | 11h |
| Docs | 10h | 10h |

## Stories e tasks

### US-01 — Como usuário, quero digitar o tema do meu caso em linguagem natural e receber temas jurídicos curados — não uma lista de processos — para descobrir como ele vem sendo decidido sem garimpar um acórdão por vez

_8 SP · Must · Concluído · 13/13 tasks · 49h_

Issue: [#14](https://github.com/Concord-API/API-5/issues/14)

| # | Task | Camada | Responsável | Est. | Status |
| --- | --- | --- | --- | ---: | --- |
| [1.1](https://github.com/Concord-API/API-5/issues/36) | Add the Portuguese text-search configuration with accent removal | Backend | victorgsnogueira | 3h | Concluído |
| [1.2](https://github.com/Concord-API/API-5/issues/37) | Add the generated search columns and their indexes to the theme dimension | Backend | IsaacOliveiraSouza | 3h | Concluído |
| [1.3](https://github.com/Concord-API/API-5/issues/38) | Create the theme search function combining text and trigram similarity | Backend | RichardCordeiro | 6h | Concluído |
| [1.4](https://github.com/Concord-API/API-5/issues/39) | Create the synonym table and expand the query with it | Backend | RichardCordeiro | 4h | Concluído |
| [1.5](https://github.com/Concord-API/API-5/issues/40) | Create `GET /api/themes` returning themes, never cases | Backend | thiagosabreu | 6h | Concluído |
| [1.6](https://github.com/Concord-API/API-5/issues/41) | Reject a query shorter than 3 characters with the Portuguese message | Backend | IsaacOliveiraSouza | 2h | Concluído |
| [1.7](https://github.com/Concord-API/API-5/issues/42) | Return the highest-volume themes when the query is empty | Backend | IsaacOliveiraSouza | 3h | Concluído |
| [1.8](https://github.com/Concord-API/API-5/issues/43) | Exclude themes without judged cases from the search | Backend | victorgsnogueira | 2h | Concluído |
| [1.9](https://github.com/Concord-API/API-5/issues/44) | Curate the synonym seed from real queries | ETL | victorgsnogueira | 3h | Concluído |
| [1.10](https://github.com/Concord-API/API-5/issues/45) | Build the home screen with the search field | Frontend | victorgsnogueira | 6h | Concluído |
| [1.11](https://github.com/Concord-API/API-5/issues/46) | Wire the results route to GET /api/themes | Frontend | RichardCordeiro | 5h | Concluído |
| [1.12](https://github.com/Concord-API/API-5/issues/47) | Reflect the search term in the URL | Frontend | RichardCordeiro | 3h | Concluído |
| [1.13](https://github.com/Concord-API/API-5/issues/48) | Show the count message and the empty message with the declared scope | Frontend | RichardCordeiro | 3h | Concluído |

### US-02 — Como usuário, quero os resultados ordenados por quão consolidado está o entendimento, e não por relevância de texto, para encontrar primeiro o que sustenta minha tese

_2 SP · Must · Concluído · 6/6 tasks · 20h_

Issue: [#15](https://github.com/Concord-API/API-5/issues/15)

| # | Task | Camada | Responsável | Est. | Status |
| --- | --- | --- | --- | ---: | --- |
| [2.1](https://github.com/Concord-API/API-5/issues/49) | Create the strength aggregate with the four components | Backend | thiagosabreu | 6h | Concluído |
| [2.2](https://github.com/Concord-API/API-5/issues/50) | Test that the score is recomputed from zero and matches the exposed value | Test | JoaoBaranov | 4h | Concluído |
| [2.3](https://github.com/Concord-API/API-5/issues/51) | Order the theme list by strength score, descending | Backend | JoaoBaranov | 3h | Concluído |
| [2.4](https://github.com/Concord-API/API-5/issues/52) | Break ties by decision volume | Backend | victorgsnogueira | 2h | Concluído |
| [2.5](https://github.com/Concord-API/API-5/issues/53) | Return the judged count next to every score | Backend | IsaacOliveiraSouza | 2h | Concluído |
| [2.6](https://github.com/Concord-API/API-5/issues/54) | Show the ordering label and the volume next to the score | Frontend | RichardCordeiro | 3h | Concluído |

### US-09 — Como usuário, quero ler o entendimento do tema em prosa, abrindo com o número que responde à pergunta e com a contagem de casos ao lado de cada percentual, para entender o padrão sem abrir uma tabela

_8 SP · Must · Concluído · 9/9 tasks · 35h_

Issue: [#17](https://github.com/Concord-API/API-5/issues/17)

| # | Task | Camada | Responsável | Est. | Status |
| --- | --- | --- | --- | ---: | --- |
| [9.3](https://github.com/Concord-API/API-5/issues/57) | Add the theme narrative table with the text origin | Backend | JoaoBaranov | 3h | Concluído |
| [9.4](https://github.com/Concord-API/API-5/issues/58) | Generate the narrative from the aggregates in the load | ETL | victorgsnogueira | 6h | Concluído |
| [9.5](https://github.com/Concord-API/API-5/issues/59) | Write counts, not percentages, below the percentage floor | ETL | victorgsnogueira | 3h | Concluído |
| [9.6](https://github.com/Concord-API/API-5/issues/60) | Expose header, lead and body in GET /api/themes/{key} | Backend | JoaoBaranov | 5h | Concluído |
| [9.7](https://github.com/Concord-API/API-5/issues/61) | Return 404 with a Portuguese message for an unknown theme key | Backend | IsaacOliveiraSouza | 2h | Concluído |
| [9.8](https://github.com/Concord-API/API-5/issues/62) | Build the theme header with score, area tag and metadata line | Frontend | victorgsnogueira | 5h | Concluído |
| [9.9](https://github.com/Concord-API/API-5/issues/63) | Build the article column of the Resumo tab | Frontend | victorgsnogueira | 6h | Concluído |
| [9.10](https://github.com/Concord-API/API-5/issues/64) | Print the judged count next to every percentage in the text | Frontend | victorgsnogueira | 3h | Concluído |
| [9.11](https://github.com/Concord-API/API-5/issues/65) | Replace the unsourced blocks with an explanation of their absence | Frontend | victorgsnogueira | 2h | Concluído |

### US-21 — Como usuário, quero ver a doutrina relacionada ao tema, com autor, obra e link para o artigo quando houver, para saber o que citar além da jurisprudência

_8 SP · Must · Concluído · 9/9 tasks · 25h_

Issue: [#22](https://github.com/Concord-API/API-5/issues/22)

| # | Task | Camada | Responsável | Est. | Status |
| --- | --- | --- | --- | ---: | --- |
| [21.1](https://github.com/Concord-API/API-5/issues/73) | Harvest doctrine from DOAJ | ETL | victorgsnogueira | 2h | Concluído |
| [21.2](https://github.com/Concord-API/API-5/issues/74) | Harvest doctrine from SciELO | ETL | victorgsnogueira | 2h | Concluído |
| [21.3](https://github.com/Concord-API/API-5/issues/75) | Harvest doctrine from the OAI-PMH repositories | ETL | victorgsnogueira | 2h | Concluído |
| [21.4](https://github.com/Concord-API/API-5/issues/76) | Normalize and load the doctrine dimension idempotently | ETL | victorgsnogueira | 3h | Concluído |
| [21.5](https://github.com/Concord-API/API-5/issues/77) | Link doctrine to subjects by semantic similarity above the declared threshold | ETL | victorgsnogueira | 3h | Concluído |
| [21.6](https://github.com/Concord-API/API-5/issues/78) | Expose the related doctrine block | Backend | thiagosabreu | 5h | Concluído |
| [21.7](https://github.com/Concord-API/API-5/issues/79) | Return the unavailable reason when a theme has no doctrine above the threshold | Backend | JoaoBaranov | 2h | Concluído |
| [21.8](https://github.com/Concord-API/API-5/issues/80) | Render the doctrine table with author, work and article link | Frontend | RichardCordeiro | 5h | Concluído |
| [21.9](https://github.com/Concord-API/API-5/issues/81) | Declare on the block that the link is by similarity, with its threshold | Frontend | RichardCordeiro | 1h | Concluído |

### US-24 — Como usuário, quero que toda tela deixe claro que os dados cobrem TJSP, TJRJ e TJMG, para não tirar uma conclusão nacional de um percentual que reflete três estados

_2 SP · Must · Concluído · 3/3 tasks · 9h_

Issue: [#24](https://github.com/Concord-API/API-5/issues/24)

| # | Task | Camada | Responsável | Est. | Status |
| --- | --- | --- | --- | ---: | --- |
| [24.1](https://github.com/Concord-API/API-5/issues/83) | Serve the declared scope from a single source | Backend | IsaacOliveiraSouza | 3h | Concluído |
| [24.2](https://github.com/Concord-API/API-5/issues/84) | Return the scope in every API response | Backend | IsaacOliveiraSouza | 3h | Concluído |
| [24.3](https://github.com/Concord-API/API-5/issues/85) | Show the scope on the results header and the detail footer, without interaction | Frontend | IsaacOliveiraSouza | 3h | Concluído |

### US-25 — Como usuário, quero saber a fonte e a data de extração de todo número que estou vendo, para saber exatamente o que estou citando

_3 SP · Must · Concluído · 7/7 tasks · 23h_

Issue: [#25](https://github.com/Concord-API/API-5/issues/25)

| # | Task | Camada | Responsável | Est. | Status |
| --- | --- | --- | --- | ---: | --- |
| [25.1](https://github.com/Concord-API/API-5/issues/89) | Create the global provenance aggregate | Backend | victorgsnogueira | 3h | Concluído |
| [25.2](https://github.com/Concord-API/API-5/issues/90) | Create the per-theme provenance view | Backend | victorgsnogueira | 3h | Concluído |
| [25.3](https://github.com/Concord-API/API-5/issues/91) | Expose provenance in every response | Backend | victorgsnogueira | 4h | Concluído |
| [25.4](https://github.com/Concord-API/API-5/issues/92) | Omit a block that has no provenance | Backend | victorgsnogueira | 3h | Concluído |
| [25.5](https://github.com/Concord-API/API-5/issues/93) | Build the Provenance component | Frontend | victorgsnogueira | 3h | Concluído |
| [25.6](https://github.com/Concord-API/API-5/issues/94) | List every source that fed the page in the footer | Frontend | victorgsnogueira | 4h | Concluído |
| [25.7](https://github.com/Concord-API/API-5/issues/95) | Test that the extraction date comes from the data, not from the clock | Test | victorgsnogueira | 3h | Concluído |

### US-26 — Como usuário, quero que a tela me diga o que não existe e por quê, em vez de mostrar um campo vazio ou um valor plausível, para não construir uma peça sobre dado que não existe

_3 SP · Must · Concluído · 6/6 tasks · 17h_

Issue: [#26](https://github.com/Concord-API/API-5/issues/26)

| # | Task | Camada | Responsável | Est. | Status |
| --- | --- | --- | --- | ---: | --- |
| [26.1](https://github.com/Concord-API/API-5/issues/96) | Define the three unavailable reasons in the response contract | Backend | victorgsnogueira | 3h | Concluído |
| [26.2](https://github.com/Concord-API/API-5/issues/97) | Return the unavailable reason for each sourceless block | Backend | victorgsnogueira | 4h | Concluído |
| [26.3](https://github.com/Concord-API/API-5/issues/98) | Return an empty list, not an error, when there is nothing to list | Backend | victorgsnogueira | 2h | Concluído |
| [26.4](https://github.com/Concord-API/API-5/issues/99) | Build the EmptyState component reading the reason from the API | Frontend | victorgsnogueira | 4h | Concluído |
| [26.5](https://github.com/Concord-API/API-5/issues/100) | Test that no sourceless block renders a placeholder value | Test | victorgsnogueira | 3h | Concluído |
| [26.6](https://github.com/Concord-API/API-5/issues/101) | Link the unavailable explanation to the limitations page | Frontend | victorgsnogueira | 1h | Concluído |

### US-10 — Como usuário, quero ver a distribuição de resultados do tema em uma figura com a fonte declarada, para ver de relance quanto é procedente, parcialmente procedente e improcedente

_5 SP · Must · Concluído · 6/6 tasks · 21h_

Issue: [#18](https://github.com/Concord-API/API-5/issues/18)

| # | Task | Camada | Responsável | Est. | Status |
| --- | --- | --- | --- | ---: | --- |
| [10.2](https://github.com/Concord-API/API-5/issues/67) | Create the outcome distribution aggregate by theme and polarity | Backend | RichardCordeiro | 5h | Concluído |
| [10.3](https://github.com/Concord-API/API-5/issues/68) | Expose the outcome breakdown separated by category | Backend | thiagosabreu | 4h | Concluído |
| [10.4](https://github.com/Concord-API/API-5/issues/69) | Build the Figure component requiring the source prop | Frontend | thiagosabreu | 4h | Concluído |
| [10.5](https://github.com/Concord-API/API-5/issues/70) | Render FIG. 1 as horizontal bars with count and percentage | Frontend | thiagosabreu | 5h | Concluído |
| [10.6](https://github.com/Concord-API/API-5/issues/71) | Show counts only, with no percentage, below the percentage floor | Frontend | RichardCordeiro | 2h | Concluído |
| [10.7](https://github.com/Concord-API/API-5/issues/72) | Replace the amount figure with an explanation of the missing source | Frontend | JoaoBaranov | 1h | Concluído |

## Technical Foundation

Tasks sem story-mãe, numeradas `0.Y`: o que a sprint precisa para que as stories tenham onde rodar (schema, pipeline de dados, caminho de carga, esqueleto de tela e correções encontradas pelo caminho).

_20 tasks · 80h · 20 concluídas_

| # | Task | Camada | Responsável | Est. | Status |
| --- | --- | --- | --- | ---: | --- |
| [0.12](https://github.com/Concord-API/API-5/issues/102) | Create the `dw` schema migration and apply it on API startup | Backend | victorgsnogueira | 8h | Concluído |
| [0.13](https://github.com/Concord-API/API-5/issues/133) | Create the pipeline repository that produces the load file | ETL | victorgsnogueira | 8h | Concluído |
| [0.14](https://github.com/Concord-API/API-5/issues/134) | Set up the frontend skeleton against the API contract | Frontend | victorgsnogueira | 16h | Concluído |
| [0.69](https://github.com/Concord-API/API-5/issues/136) | Sync the task board from branch and pull request events | DevOps | victorgsnogueira | 5h | Concluído |
| [0.70](https://github.com/Concord-API/API-5/issues/137) | Map verified movement codes to decision outcomes in the pipeline | ETL | victorgsnogueira | 3h | Concluído |
| [0.71](https://github.com/Concord-API/API-5/issues/138) | Add the pipeline command that harvests and builds the load file | ETL | victorgsnogueira | 6h | Concluído |
| [0.72](https://github.com/Concord-API/API-5/issues/139) | Seed the strength configuration in the load file | ETL | victorgsnogueira | 2h | Concluído |
| [0.73](https://github.com/Concord-API/API-5/issues/140) | Refresh the materialized views in dependency order in the load file | ETL | victorgsnogueira | 2h | Concluído |
| [0.74](https://github.com/Concord-API/API-5/issues/142) | Draw the conceptual entity-relationship model (MER) of the dw schema | Docs | JoaoBaranov | 5h | Concluído |
| [0.75](https://github.com/Concord-API/API-5/issues/143) | Draw the physical entity-relationship diagram (DER) of the dw schema | Docs | JoaoBaranov | 5h | Concluído |
| [0.76](https://github.com/Concord-API/API-5/issues/144) | Generate the calendar dimension in the load | ETL | victorgsnogueira | 1h | Concluído |
| [0.77](https://github.com/Concord-API/API-5/issues/145) | Harvest only cases with a verified decision movement | ETL | victorgsnogueira | 2h | Concluído |
| [0.78](https://github.com/Concord-API/API-5/issues/146) | Check the warehouse integrity before writing the load file | Test | victorgsnogueira | 3h | Concluído |
| [0.79](https://github.com/Concord-API/API-5/issues/147) | Build the pipeline test schema from the backend migrations | Test | victorgsnogueira | 3h | Concluído |
| [0.80](https://github.com/Concord-API/API-5/issues/148) | Propose subject clusters for curation with local embeddings | ETL | victorgsnogueira | 3h | Concluído |
| [0.81](https://github.com/Concord-API/API-5/issues/154) | Map the special court and appeal panel levels from DataJud | ETL | victorgsnogueira | 1h | Concluído |
| [0.82](https://github.com/Concord-API/API-5/issues/155) | Read the pipeline settings from a .env file | ETL | victorgsnogueira | 1h | Concluído |
| [0.83](https://github.com/Concord-API/API-5/issues/157) | Analyze the backend quality and coverage with SonarQube Cloud | DevOps | RichardCordeiro | 2h | Concluído |
| [0.84](https://github.com/Concord-API/API-5/issues/158) | Analyze the frontend quality and coverage with SonarQube Cloud | DevOps | RichardCordeiro | 2h | Concluído |
| [0.85](https://github.com/Concord-API/API-5/issues/159) | Analyze the pipeline quality and coverage with SonarQube Cloud | DevOps | RichardCordeiro | 2h | Concluído |
