# Sprint Backlog — Sprint 2

**Janela:** 05/10 a 25/10/2026

**Board:** [GitHub Project](https://github.com/orgs/Concord-API/projects/5) · snapshot de 12/11/2026

## Meta da sprint

Stories que o time se compromete a entregar. Se alguma não for concluída, a sprint não atingiu a meta.

| ID | Prioridade | Descrição | SP | Tasks | Horas | Status |
| --- | --- | --- | ---: | ---: | ---: | --- |
| **US-03** | Must | Como **usuário**, quero ver em cada resultado o score, a área do direito (vara), o título da tese, um resumo curto, os tribunais, o volume, o período, a última decisão e o percentual favorável, para comparar teses antes de abrir qualquer uma delas | 8 | 11 | 35h | Concluído |
| **US-04** | Must | Como **usuário**, quero filtrar os resultados por tribunal, período, instância e força mínima, vendo quantos processos cada tribunal tem, para restringir a lista ao meu caso | 5 | 8 | 18h | Concluído |
| **US-12** | Must | Como **usuário**, quero ver o alinhamento do tema por tribunal, para saber se a tese se sustenta igual em São Paulo, Rio de Janeiro, Minas Gerais e nos tribunais superiores (STJ e STF) | 3 | 6 | 12h | Concluído |
| **US-14** | Must | Como **usuário**, quero uma tabela do comportamento de cada tribunal — decisões, alinhamento e data da mais recente — para comparar o meu tribunal com os outros | 3 | 5 | 7h | Concluído |
| **US-15** | Must | Como **usuário**, quero uma amostra auditável dos processos por trás do tema, com câmara, data e resultado, para conferir os casos antes de citá-los | 5 | 9 | 12h | Concluído |
| **US-17** | Should | Como **usuário**, quero saber se as câmaras do meu tribunal estão decidindo igual, para identificar divergência interna antes de decidir | 5 | 5 | 19h | Concluído |

## Fora da meta

Stories planejadas na sprint, mas que podem passar para a próxima se não houver capacidade, mesmo sendo prioridade.

| ID | Prioridade | Descrição | SP | Tasks | Horas | Status |
| --- | --- | --- | ---: | ---: | ---: | --- |
| **US-07** | Must | Como **usuário**, quero que o score venha com uma classificação em linguagem que já existe no meio jurídico — Consolidada, Dominante, Em formação, Divergente — para não ter de interpretar uma escala inventada | 2 | 4 | 4h | Concluído |
| **US-11** | Must | Como **usuário**, quero ver como o alinhamento do tema evoluiu ano a ano, com a frase de tendência, para saber se o entendimento está se firmando ou mudando | 5 | 6 | 9h | Concluído |

## Resumo da sprint

| | Total |
| --- | ---: |
| Stories (meta / fora da meta) | 6 / 2 |
| Story points (meta / total) | 29 / 36 |
| Tasks (concluídas / total) | 120 / 120 |
| Horas (feitas / total) | 273h / 273h |
| Tasks em stories | 54 (116h) |
| Technical Foundation | 28 (62h) |
| Entrega e processo | 38 (95h) |

### Horas por responsável

| Responsável | Tasks | Horas | Concluído |
| --- | ---: | ---: | ---: |
| victorgsnogueira | 39 | 97.5h | 97.5h |
| thiagosabreu | 28 | 49h | 49h |
| RichardCordeiro | 19 | 42h | 42h |
| JoaoBaranov | 19 | 42h | 42h |
| IsaacOliveiraSouza | 13 | 28.5h | 28.5h |
| vp-p | 3 | 11h | 11h |
| joaoandrade17 | 1 | 3h | 3h |

### Horas por camada

| Camada | Horas | Concluído |
| --- | ---: | ---: |
| Backend | 74h | 74h |
| Frontend | 57h | 57h |
| DevOps | 55h | 55h |
| ETL | 43h | 43h |
| Test | 31h | 31h |
| Docs | 13h | 13h |

_As horas de uma task com mais de um responsável são divididas igualmente entre eles._

## Stories e tasks

### US-03 — Como usuário, quero ver em cada resultado o score, a área do direito (vara), o título da tese, um resumo curto, os tribunais, o volume, o período, a última decisão e o percentual favorável, para comparar teses antes de abrir qualquer uma delas

_8 SP · Must · Concluído · 11/11 tasks · 35h_

Issue: [#166](https://github.com/Concord-API/API-5/issues/166)

| # | Task | Camada | Responsável | Est. | Status |
| --- | --- | --- | --- | ---: | --- |
| [3.1](https://github.com/Concord-API/API-5/issues/186) | Expose area, title, summary, courts, volume, period, last decision and upheld percentage per result | Backend | RichardCordeiro | 6h | Concluído |
| [3.2](https://github.com/Concord-API/API-5/issues/187) | Return the short summary of up to two lines per theme | Backend | RichardCordeiro | 3h | Concluído |
| [3.3](https://github.com/Concord-API/API-5/issues/188) | Return the court acronyms with the exact +N difference | Backend | JoaoBaranov | 3h | Concluído |
| [3.4](https://github.com/Concord-API/API-5/issues/189) | Build the result item with the area tag and the thesis title | Frontend | RichardCordeiro | 5h | Concluído |
| [3.5](https://github.com/Concord-API/API-5/issues/190) | Build the AlignmentBar with the count next to it | Frontend | JoaoBaranov | 4h | Concluído |
| [3.6](https://github.com/Concord-API/API-5/issues/191) | Render the court chips with the +N indicator only when needed | Frontend | JoaoBaranov | 3h | Concluído |
| [3.7](https://github.com/Concord-API/API-5/issues/192) | Format the numbers in Portuguese and never recompute them | Frontend | RichardCordeiro | 2h | Concluído |
| [3.8](https://github.com/Concord-API/API-5/issues/193) | Show the count instead of the percentage below the percentage floor | Frontend | RichardCordeiro | 2h | Concluído |
| [3.9](https://github.com/Concord-API/API-5/issues/194) | Open the theme detail from the result item | Frontend | RichardCordeiro | 2h | Concluído |
| [3.10](https://github.com/Concord-API/API-5/issues/195) | Test that the item renders every field of the contract | Test | RichardCordeiro | 3h | Concluído |
| [3.11](https://github.com/Concord-API/API-5/issues/196) | Show the score circle in the result item | Frontend | RichardCordeiro | 2h | Concluído |

### US-04 — Como usuário, quero filtrar os resultados por tribunal, período, instância e força mínima, vendo quantos processos cada tribunal tem, para restringir a lista ao meu caso

_5 SP · Must · Concluído · 8/8 tasks · 18h_

Issue: [#16](https://github.com/Concord-API/API-5/issues/16)

| # | Task | Camada | Responsável | Est. | Status |
| --- | --- | --- | --- | ---: | --- |
| [4.1](https://github.com/Concord-API/API-5/issues/197) | Accept court, period, instance and minimum strength on GET /api/themes | Backend | thiagosabreu | 6h | Concluído |
| [4.2](https://github.com/Concord-API/API-5/issues/198) | Return the case count per court with the filter options | Backend | thiagosabreu | 4h | Concluído |
| [4.3](https://github.com/Concord-API/API-5/issues/199) | Offer only the instances that exist in the loaded scope | Backend | RichardCordeiro | 1h | Concluído |
| [4.4](https://github.com/Concord-API/API-5/issues/200) | Build the filter bar with the court counts | Frontend | RichardCordeiro | 2h | Concluído |
| [4.5](https://github.com/Concord-API/API-5/issues/201) | Reflect the active filters in the URL | Frontend | RichardCordeiro | 2h | Concluído |
| [4.6](https://github.com/Concord-API/API-5/issues/202) | Clear every filter and rebuild the list | Frontend | RichardCordeiro | 1h | Concluído |
| [4.7](https://github.com/Concord-API/API-5/issues/203) | Describe the applied narrowing when nothing matches | Frontend | RichardCordeiro | 1h | Concluído |
| [4.8](https://github.com/Concord-API/API-5/issues/204) | Test that the filtering happens in the API, never in the browser | Test | RichardCordeiro | 1h | Concluído |

### US-12 — Como usuário, quero ver o alinhamento do tema por tribunal, para saber se a tese se sustenta igual em São Paulo, Rio de Janeiro, Minas Gerais e nos tribunais superiores (STJ e STF)

_3 SP · Must · Concluído · 6/6 tasks · 12h_

Issue: [#221](https://github.com/Concord-API/API-5/issues/221)

| # | Task | Camada | Responsável | Est. | Status |
| --- | --- | --- | --- | ---: | --- |
| [12.1](https://github.com/Concord-API/API-5/issues/235) | Create the alignment-by-court aggregate with merit and appeals apart | Backend | JoaoBaranov | 4h | Concluído |
| [12.2](https://github.com/Concord-API/API-5/issues/236) | Expose per court the percentage, its n and its polarity label | Backend | JoaoBaranov | 3h | Concluído |
| [12.3](https://github.com/Concord-API/API-5/issues/237) | Test that the courts add up to the theme total | Test | JoaoBaranov | 1h | Concluído |
| [12.4](https://github.com/Concord-API/API-5/issues/238) | Build the alignment-by-court list | Frontend | JoaoBaranov | 2h | Concluído |
| [12.5](https://github.com/Concord-API/API-5/issues/239) | Show a court without judgments as having no data | Frontend | JoaoBaranov | 1h | Concluído |
| [12.6](https://github.com/Concord-API/API-5/issues/284) | Fix the theme by court migration version and the Acceptance refresh | Backend | JoaoBaranov | 1h | Concluído |

### US-14 — Como usuário, quero uma tabela do comportamento de cada tribunal — decisões, alinhamento e data da mais recente — para comparar o meu tribunal com os outros

_3 SP · Must · Concluído · 5/5 tasks · 7h_

Issue: [#167](https://github.com/Concord-API/API-5/issues/167)

| # | Task | Camada | Responsável | Est. | Status |
| --- | --- | --- | --- | ---: | --- |
| [14.1](https://github.com/Concord-API/API-5/issues/205) | Expose the behaviour per court: decisions, alignment and last decision | Backend | victorgsnogueira | 2h | Concluído |
| [14.2](https://github.com/Concord-API/API-5/issues/206) | Build the behaviour table with the visual rules | Frontend | victorgsnogueira | 2h | Concluído |
| [14.3](https://github.com/Concord-API/API-5/issues/207) | Scroll a wide table inside its container | Frontend | victorgsnogueira | 1h | Concluído |
| [14.4](https://github.com/Concord-API/API-5/issues/208) | Flag the amount column as unsourced | Frontend | victorgsnogueira | 1h | Concluído |
| [14.5](https://github.com/Concord-API/API-5/issues/209) | Show the appeal outcome rate in a superior court row | Backend | victorgsnogueira | 1h | Concluído |

### US-15 — Como usuário, quero uma amostra auditável dos processos por trás do tema, com câmara, data e resultado, para conferir os casos antes de citá-los

_5 SP · Must · Concluído · 9/9 tasks · 12h_

Issue: [#168](https://github.com/Concord-API/API-5/issues/168)

| # | Task | Camada | Responsável | Est. | Status |
| --- | --- | --- | --- | ---: | --- |
| [15.1](https://github.com/Concord-API/API-5/issues/210) | Create the case view behind the theme sample | Backend | thiagosabreu | 1h | Concluído |
| [15.2](https://github.com/Concord-API/API-5/issues/211) | Expose GET /api/themes/{key}/cases with a stable ordering | Backend | thiagosabreu | 2h | Concluído |
| [15.3](https://github.com/Concord-API/API-5/issues/212) | Return "N of M decisions" with the sample | Backend | thiagosabreu | 1h | Concluído |
| [15.4](https://github.com/Concord-API/API-5/issues/213) | Flag a sealed case and hide its data | Backend | thiagosabreu | 1h | Concluído |
| [15.5](https://github.com/Concord-API/API-5/issues/214) | Return the reporter judge and amount columns empty and flagged | Backend | thiagosabreu | 1h | Concluído |
| [15.6](https://github.com/Concord-API/API-5/issues/215) | Name the judging body of a superior court in the chamber column | Backend | thiagosabreu | 1h | Concluído |
| [15.7](https://github.com/Concord-API/API-5/issues/216) | Build the auditable sample table | Frontend | IsaacOliveiraSouza | 3h | Concluído |
| [15.8](https://github.com/Concord-API/API-5/issues/217) | Link every case number to the court with the formatted number | Frontend | IsaacOliveiraSouza | 1h | Concluído |
| [15.9](https://github.com/Concord-API/API-5/issues/218) | Test that the ordering is the same between two calls | Test | IsaacOliveiraSouza | 1h | Concluído |

### US-17 — Como usuário, quero saber se as câmaras do meu tribunal estão decidindo igual, para identificar divergência interna antes de decidir

_5 SP · Should · Concluído · 5/5 tasks · 19h_

Issue: [#222](https://github.com/Concord-API/API-5/issues/222)

| # | Task | Camada | Responsável | Est. | Status |
| --- | --- | --- | --- | ---: | --- |
| [17.1](https://github.com/Concord-API/API-5/issues/240) | Create the alignment-by-judging-body aggregate | Backend | victorgsnogueira | 4h | Concluído |
| [17.2](https://github.com/Concord-API/API-5/issues/241) | Flag a panel 20 points away from its court, from 5 judged cases up | Backend | victorgsnogueira | 3h | Concluído |
| [17.3](https://github.com/Concord-API/API-5/issues/242) | Expose the panels per court with their n, hiding a panel with one judgment | Backend | victorgsnogueira | 4h | Concluído |
| [17.4](https://github.com/Concord-API/API-5/issues/243) | Test that a court's panels add up to the court total | Test | victorgsnogueira | 3h | Concluído |
| [17.5](https://github.com/Concord-API/API-5/issues/244) | Build the panel block with the divergence flag | Frontend | victorgsnogueira | 5h | Concluído |

### US-07 — Como usuário, quero que o score venha com uma classificação em linguagem que já existe no meio jurídico — Consolidada, Dominante, Em formação, Divergente — para não ter de interpretar uma escala inventada

_2 SP · Must · Concluído · 4/4 tasks · 4h_

Issue: [#219](https://github.com/Concord-API/API-5/issues/219)

| # | Task | Camada | Responsável | Est. | Status |
| --- | --- | --- | --- | ---: | --- |
| [7.1](https://github.com/Concord-API/API-5/issues/225) | Return the grade only from 10 judged cases up | Backend | IsaacOliveiraSouza | 1h | Concluído |
| [7.2](https://github.com/Concord-API/API-5/issues/226) | Show the grade next to the score | Frontend | IsaacOliveiraSouza | 1h | Concluído |
| [7.3](https://github.com/Concord-API/API-5/issues/227) | Show the score without the textual grade below the minimum | Frontend | IsaacOliveiraSouza | 1h | Concluído |
| [7.4](https://github.com/Concord-API/API-5/issues/228) | Test the band boundaries at 55, 75 and 90 and the minimum of 10 | Test | IsaacOliveiraSouza | 1h | Concluído |

### US-11 — Como usuário, quero ver como o alinhamento do tema evoluiu ano a ano, com a frase de tendência, para saber se o entendimento está se firmando ou mudando

_5 SP · Must · Concluído · 6/6 tasks · 9h_

Issue: [#220](https://github.com/Concord-API/API-5/issues/220)

| # | Task | Camada | Responsável | Est. | Status |
| --- | --- | --- | --- | ---: | --- |
| [11.1](https://github.com/Concord-API/API-5/issues/229) | Create the yearly alignment aggregate per theme | Backend | JoaoBaranov | 2h | Concluído |
| [11.2](https://github.com/Concord-API/API-5/issues/230) | Expose the yearly series ordered oldest to newest | Backend | JoaoBaranov | 2h | Concluído |
| [11.3](https://github.com/Concord-API/API-5/issues/231) | Return the trend sentence values from the aggregate | Backend | JoaoBaranov | 1h | Concluído |
| [11.4](https://github.com/Concord-API/API-5/issues/232) | Build the yearly alignment bars in the side column | Frontend | JoaoBaranov | 2h | Concluído |
| [11.5](https://github.com/Concord-API/API-5/issues/233) | Highlight the most recent year and skip the years with no result | Frontend | JoaoBaranov | 1h | Concluído |
| [11.6](https://github.com/Concord-API/API-5/issues/234) | Hide the trend sentence when there is data in a single year | Frontend | JoaoBaranov | 1h | Concluído |

## Technical Foundation

Tasks sem story-mãe, numeradas `0.Y`: o que a sprint precisa para que as stories tenham onde rodar (schema, pipeline de dados, caminho de carga, esqueleto de tela e correções encontradas pelo caminho).

_28 tasks · 62h · 28 concluídas_

| # | Task | Camada | Responsável | Est. | Status |
| --- | --- | --- | --- | ---: | --- |
| [0.47](https://github.com/Concord-API/API-5/issues/178) | Top up the harvest for themes with fewer than 5 judged cases | ETL | victorgsnogueira | 6h | Concluído |
| [0.48](https://github.com/Concord-API/API-5/issues/179) | Add the schema version to the load script and refuse a mismatched database | ETL | victorgsnogueira | 4h | Concluído |
| [0.49](https://github.com/Concord-API/API-5/issues/180) | Add the load manifest with row counts and the extraction date | ETL | victorgsnogueira | 3h | Concluído |
| [0.86](https://github.com/Concord-API/API-5/issues/169) | Allow the superior-court level in the court level constraint | Backend | JoaoBaranov | 3h | Concluído |
| [0.87](https://github.com/Concord-API/API-5/issues/170) | Harvest the STJ civil cases from DataJud | ETL | victorgsnogueira | 6h | Concluído |
| [0.88](https://github.com/Concord-API/API-5/issues/171) | Map the DataJud instance of STJ cases to the superior-court level | ETL | victorgsnogueira | 2h | Concluído |
| [0.89](https://github.com/Concord-API/API-5/issues/172) | Map the STJ judging bodies: panels, sections and the Special Court | ETL | victorgsnogueira | 3h | Concluído |
| [0.90](https://github.com/Concord-API/API-5/issues/173) | Seed the STJ in the court reference data | ETL | victorgsnogueira | 2h | Concluído |
| [0.91](https://github.com/Concord-API/API-5/issues/174) | Check whether one case is counted both in a state court and in the STJ | Test | victorgsnogueira | 4h | Concluído |
| [0.92](https://github.com/Concord-API/API-5/issues/175) | Map the source link for STJ cases | ETL | victorgsnogueira | 3h | Concluído |
| [0.93](https://github.com/Concord-API/API-5/issues/176) | Spike: find a source for STF decisions | ETL | victorgsnogueira | 6h | Concluído |
| [0.94](https://github.com/Concord-API/API-5/issues/177) | Register the decision on the STF source | Docs | victorgsnogueira | 1h | Concluído |
| [0.96](https://github.com/Concord-API/API-5/issues/185) | Replace every hand-written court list in the screens with the scope from the API | Frontend | IsaacOliveiraSouza | 1h | Concluído |
| [0.97](https://github.com/Concord-API/API-5/issues/223) | Add the grade, divergence and coverage settings to the strength configuration | Backend | JoaoBaranov | 3h | Concluído |
| [0.98](https://github.com/Concord-API/API-5/issues/224) | Seed the new strength settings in the load file | ETL | victorgsnogueira | 2h | Concluído |
| [0.99](https://github.com/Concord-API/API-5/issues/278) | Harvest the STJ appeals instead of the civil classes | ETL | victorgsnogueira | 1h | Concluído |
| [0.100](https://github.com/Concord-API/API-5/issues/288) | Discard a movement dated before 1940 or after the collection | ETL | victorgsnogueira | 1h | Concluído |
| [0.101](https://github.com/Concord-API/API-5/issues/296) | Fix the panels named after a cabinet, the doctrine source names and the repeated doctrine | Backend | victorgsnogueira | 1h | Concluído |
| [0.102](https://github.com/Concord-API/API-5/issues/298) | Link each theme to the STJ theses that rule on its subjects | ETL | victorgsnogueira | 1h | Concluído |
| [0.103](https://github.com/Concord-API/API-5/issues/299) | Write the theme opening in plain words | Frontend | victorgsnogueira | 1h | Concluído |
| [0.104](https://github.com/Concord-API/API-5/issues/300) | Remove the empty amount column and group the missing data notes | Frontend | victorgsnogueira | 1h | Concluído |
| [0.105](https://github.com/Concord-API/API-5/issues/301) | Show the appeal outcome apart for the state courts and the STJ | Backend | victorgsnogueira | 1h | Concluído |
| [0.106](https://github.com/Concord-API/API-5/issues/302) | Keep the yearly alignment list inside a scrolling box | Frontend | victorgsnogueira | 1h | Concluído |
| [0.107](https://github.com/Concord-API/API-5/issues/303) | Paginate the panel list of each court in the analytic base tab | Frontend | thiagosabreu | 1h | Concluído |
| [0.108](https://github.com/Concord-API/API-5/issues/304) | Keep the divergence note on the same line as the panel rate | Frontend | thiagosabreu | 1h | Concluído |
| [0.109](https://github.com/Concord-API/API-5/issues/305) | Write the panel names in one consistent case | Frontend | thiagosabreu | 1h | Concluído |
| [0.110](https://github.com/Concord-API/API-5/issues/306) | Remove the missing source data list from the theme page | Frontend | thiagosabreu | 1h | Concluído |
| [0.111](https://github.com/Concord-API/API-5/issues/307) | Make the panel pages stand out | Frontend | thiagosabreu | 1h | Concluído |

## Entrega e processo

Tasks `DVP-xx` (CI, deploy, QA, monitoramento, testes de banco) e `PRC-xx` (processo), também sem story-mãe.

_38 tasks · 95h · 38 concluídas_

| # | Task | Frente | Camada | Responsável | Est. | Status |
| --- | --- | --- | --- | --- | ---: | --- |
| [DVP-01](https://github.com/Concord-API/API-5/issues/247) | Reuse the test coverage in the quality job instead of running the tests again | CI | DevOps | victorgsnogueira | 3h | Concluído |
| [PRC-01](https://github.com/Concord-API/API-5/issues/260) | Set up the DVP and PRC task prefixes on the board | — | Docs | joaoandrade17 | 3h | Concluído |
| [DVP-02](https://github.com/Concord-API/API-5/issues/248) | Validate the pipeline against the API migrations in CI | CI | ETL | victorgsnogueira | 3h | Concluído |
| [DVP-03](https://github.com/Concord-API/API-5/issues/249) | Run the API and the frontend together with the sample load in an acceptance workflow | CI | DevOps | victorgsnogueira | 6h | Concluído |
| [DVP-04](https://github.com/Concord-API/API-5/issues/250) | Run the commit checks only on task pull requests and on main, and require the acceptance check to merge into main | CI | DevOps | victorgsnogueira | 3h | Concluído |
| [DVP-06](https://github.com/Concord-API/API-5/issues/252) | Align the Definition of Done with how the project works today | QA | Docs | RichardCordeiro | 2h | Concluído |
| [DVP-07](https://github.com/Concord-API/API-5/issues/253) | Add the QA checklist to the pull request template from a US branch to main | QA | Docs | RichardCordeiro | 1h | Concluído |
| [DVP-08](https://github.com/Concord-API/API-5/issues/254) | Validate real API responses against the frontend zod schemas | QA | Test | RichardCordeiro | 4h | Concluído |
| [DVP-09](https://github.com/Concord-API/API-5/issues/256) | Create and configure the test virtual machine with every dependency the application needs | Deploy | DevOps | IsaacOliveiraSouza | 6h | Concluído |
| [DVP-10](https://github.com/Concord-API/API-5/issues/255) | Deploy every release to the test virtual machine automatically | Deploy | DevOps | IsaacOliveiraSouza | 6h | Concluído |
| [DVP-11](https://github.com/Concord-API/API-5/issues/257) | Document the automated deploy | Deploy | Docs | IsaacOliveiraSouza | 3h | Concluído |
| [DVP-12](https://github.com/Concord-API/API-5/issues/181) | Publish the load script as a versioned pipeline release | CI | DevOps | IsaacOliveiraSouza, victorgsnogueira | 3h | Concluído |
| [DVP-13](https://github.com/Concord-API/API-5/issues/182) | Run the API on the homologation server so it creates the schema and the team loads the data file | Deploy | DevOps | IsaacOliveiraSouza, victorgsnogueira | 4h | Concluído |
| [DVP-15](https://github.com/Concord-API/API-5/issues/258) | Run the database checks in their own CI job | BD | DevOps | JoaoBaranov | 3h | Concluído |
| [DVP-16](https://github.com/Concord-API/API-5/issues/259) | Document PostgreSQL 16, Testcontainers and DbUp in the database tests | BD | Docs | JoaoBaranov | 2h | Concluído |
| [DVP-18](https://github.com/Concord-API/API-5/issues/264) | Export metrics with OpenTelemetry only when an OTLP endpoint is configured | Monitoramento | Backend | thiagosabreu | 2h | Concluído |
| [DVP-19](https://github.com/Concord-API/API-5/issues/265) | Expose warehouse availability and last-extraction age as metrics | Monitoramento | Backend | thiagosabreu | 3h | Concluído |
| [DVP-20](https://github.com/Concord-API/API-5/issues/266) | Count searches with no result without recording the query text | Monitoramento | Backend | thiagosabreu | 1h | Concluído |
| [DVP-21](https://github.com/Concord-API/API-5/issues/267) | Send the API logs over OTLP when configured | Monitoramento | Backend | thiagosabreu | 1h | Concluído |
| [DVP-22](https://github.com/Concord-API/API-5/issues/268) | Test the metrics and logs contract | Monitoramento | Test | thiagosabreu | 2h | Concluído |
| [DVP-23](https://github.com/Concord-API/API-5/issues/269) | Write the WinSW definitions and the Windows configuration for Prometheus and Loki | Monitoramento | DevOps | thiagosabreu | 2h | Concluído |
| [DVP-24](https://github.com/Concord-API/API-5/issues/270) | Write the install script for Alloy, Prometheus, Loki and Grafana | Monitoramento | DevOps | thiagosabreu | 3h | Concluído |
| [DVP-25](https://github.com/Concord-API/API-5/issues/271) | Prepare the client's Postgres with pg_stat_statements and a monitoring user | Monitoramento | DevOps | thiagosabreu | 2h | Concluído |
| [DVP-26](https://github.com/Concord-API/API-5/issues/272) | Collect Windows, IIS, service and Postgres metrics in Alloy | Monitoramento | DevOps | thiagosabreu | 2h | Concluído |
| [DVP-27](https://github.com/Concord-API/API-5/issues/273) | Probe /health and /health/ready every minute from Alloy | Monitoramento | DevOps | thiagosabreu | 1h | Concluído |
| [DVP-28](https://github.com/Concord-API/API-5/issues/274) | Configure Grafana for offline use with a single admin account | Monitoramento | DevOps | thiagosabreu | 1h | Concluído |
| [DVP-29](https://github.com/Concord-API/API-5/issues/275) | Provision the Prometheus and Loki data sources | Monitoramento | DevOps | thiagosabreu | 1h | Concluído |
| [DVP-30](https://github.com/Concord-API/API-5/issues/276) | Provision the overview, API, data, database and server dashboards as code | Monitoramento | DevOps | thiagosabreu | 3h | Concluído |
| [DVP-31](https://github.com/Concord-API/API-5/issues/277) | Validate the Alloy and Prometheus configuration in CI | Monitoramento | DevOps | thiagosabreu | 2h | Concluído |
| [DVP-32](https://github.com/Concord-API/API-5/issues/279) | Write the sample load to a fixed file name | CI | DevOps | victorgsnogueira | 1h | Concluído |
| [DVP-33](https://github.com/Concord-API/API-5/issues/280) | Require the Sonar quality gate on the way to main | CI | DevOps | victorgsnogueira | 1h | Concluído |
| [DVP-34](https://github.com/Concord-API/API-5/issues/281) | Add the Sonar quality gate to the Definition of Done | QA | Docs | RichardCordeiro | 1h | Concluído |
| [DVP-35](https://github.com/Concord-API/API-5/issues/285) | Make the QA checklist a self-review by the story’s author | QA | DevOps | RichardCordeiro | 1h | Concluído |
| [DVP-36](https://github.com/Concord-API/API-5/issues/289) | Run the API against a disposable PostgreSQL in the integration tests | Testes | Test | vp-p | 5h | Concluído |
| [DVP-37](https://github.com/Concord-API/API-5/issues/290) | Test the theme search and detail endpoints against the sample load | Testes | Test | vp-p | 4h | Concluído |
| [DVP-38](https://github.com/Concord-API/API-5/issues/291) | Test the theme panels endpoint against the sample load | Testes | Test | vp-p | 2h | Concluído |
| [DVP-40](https://github.com/Concord-API/API-5/issues/293) | Send the API logs only to the file and OTLP, and read the warehouse metrics after the migration | Monitoramento | Backend | thiagosabreu | 1h | Concluído |
| [DVP-41](https://github.com/Concord-API/API-5/issues/297) | Exclude the migration scripts from the Sonar duplication check | CI | DevOps | victorgsnogueira | 1h | Concluído |
