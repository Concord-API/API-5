# Sprint Backlog — Sprint 3

**Janela:** 02/11 a 22/11/2026

**Board:** [GitHub Project](https://github.com/orgs/Concord-API/projects/5) · snapshot de 22/11/2026

**Definições:** [Definition of Ready](../Docs/pt_br/Scrum/definition-of-ready.md) · [Definition of Done](../Docs/pt_br/Scrum/definition-of-done.md)

## Meta da sprint

> **O usuário confere dentro do Ratio os processos, os julgados e os precedentes por trás do tema, e leva o resultado para o próprio trabalho: exporta as decisões, copia a citação pronta e compartilha o link da aba.**

Stories que o time se compromete a entregar. Se alguma não for concluída, a sprint não atingiu a meta.

| ID | Prioridade | Descrição | SP | Tasks | Horas | Status |
| --- | --- | --- | ---: | ---: | ---: | --- |
| **US-13** | Could | Como **usuário**, quero que a aba que estou vendo seja refletida na URL, para enviar a um colega o link exato da parte que quero mostrar | 5 | 3 | 6h | Concluído |
| **US-39** | Should | Como **usuário**, quero ver os dados de cada processo da amostra dentro do Ratio, extraídos do site do próprio tribunal, para conferir o processo sem sair do produto | 5 | 8 | 21h | Concluído |
| **US-40** | Should | Como **usuário**, quero ver os julgados que compõem a jurisprudência do tema, com tribunal, órgão julgador, data, ementa e link para a página do tribunal, no mesmo padrão de tabela dos processos, para ler como os tribunais decidiram e não apenas contar os casos | 8 | 8 | 23h | Concluído |
| **US-41** | Should | Como **usuário**, quero ver os precedentes qualificados relacionados ao tema — súmulas, temas repetitivos, IRDR, IAC e repercussão geral —, com tipo, número, tribunal, tese e situação, para saber o que vincula os tribunais neste tema e não apenas como eles têm decidido | 8 | 7 | 15h | Concluído |

## Fora da meta

Stories planejadas na sprint, mas que podem passar para a próxima se não houver capacidade, mesmo sendo prioridade.

| ID | Prioridade | Descrição | SP | Tasks | Horas | Status |
| --- | --- | --- | ---: | ---: | ---: | --- |
| **US-27** | Should | Como **usuário**, quero exportar para CSV as decisões que sustentam o tema, para trabalhar os dados fora da ferramenta | 5 | 6 | 9h | Concluído |
| **US-28** | Should | Como **usuário**, quero copiar a citação do tema já com a fonte, a data de extração, o escopo e o `n`, para colar sem redigitar | 3 | 3 | 5h | Concluído |

## Resumo da sprint

| | Total |
| --- | ---: |
| Stories (meta / fora da meta) | 4 / 2 |
| Story points (meta / total) | 26 / 34 |
| Tasks (concluídas / total) | 62 / 62 |
| Horas (feitas / total) | 154h / 154h |
| Tasks em stories | 35 (79h) |
| Technical Foundation | 2 (10h) |
| Entrega e processo | 25 (65h) |

### Horas por responsável

| Responsável | Tasks | Horas | Concluído |
| --- | ---: | ---: | ---: |
| thiagosabreu | 26 | 60h | 60h |
| JoaoBaranov | 10 | 31h | 31h |
| IsaacOliveiraSouza | 11 | 25h | 25h |
| RichardCordeiro | 8 | 20h | 20h |
| victorgsnogueira | 6 | 17h | 17h |
| joaoandrade17 | 1 | 1h | 1h |

### Horas por camada

| Camada | Horas | Concluído |
| --- | ---: | ---: |
| DevOps | 49h | 49h |
| ETL | 31h | 31h |
| Backend | 30h | 30h |
| Frontend | 24h | 24h |
| Test | 16h | 16h |
| Docs | 4h | 4h |

## Burndown

![Burndown da Sprint 3](burndown.png)

Horas restantes por dia, a partir do campo `Status` do board e das horas de cada task. Situação em 22/11/2026.

## Stories e tasks

### US-13 — Como usuário, quero que a aba que estou vendo seja refletida na URL, para enviar a um colega o link exato da parte que quero mostrar

_5 SP · Could · Concluído · 3/3 tasks · 6h_

Issue: [#19](https://github.com/Concord-API/API-5/issues/19)

| # | Task | Camada | Responsável | Est. | Status |
| --- | --- | --- | --- | ---: | --- |
| [13.1](https://github.com/Concord-API/API-5/issues/86) | Validate the tab search param, defaulting to resumo | Frontend | thiagosabreu | 3h | Concluído |
| [13.2](https://github.com/Concord-API/API-5/issues/87) | Update the URL when the active tab changes | Frontend | thiagosabreu | 2h | Concluído |
| [13.3](https://github.com/Concord-API/API-5/issues/88) | Make the browser back button return to the previous tab | Frontend | thiagosabreu | 1h | Concluído |

### US-39 — Como usuário, quero ver os dados de cada processo da amostra dentro do Ratio, extraídos do site do próprio tribunal, para conferir o processo sem sair do produto

_5 SP · Should · Concluído · 8/8 tasks · 21h_

Issue: [#329](https://github.com/Concord-API/API-5/issues/329)

| # | Task | Camada | Responsável | Est. | Status |
| --- | --- | --- | --- | ---: | --- |
| [39.1](https://github.com/Concord-API/API-5/issues/343) | Harvest the case data from the TJSP site | ETL | RichardCordeiro | 5h | Concluído |
| [39.5](https://github.com/Concord-API/API-5/issues/347) | Load the case details and public movements into the warehouse | ETL | thiagosabreu | 4h | Concluído |
| [39.6](https://github.com/Concord-API/API-5/issues/348) | Expose a case's details and movements by its number | Backend | victorgsnogueira | 3h | Concluído |
| [39.7](https://github.com/Concord-API/API-5/issues/349) | Remove the court link and the portal hint from the case sample | Frontend | IsaacOliveiraSouza | 1h | Concluído |
| [39.8](https://github.com/Concord-API/API-5/issues/350) | Build the case view opened from the sample | Frontend | victorgsnogueira | 4h | Concluído |
| [39.9](https://github.com/Concord-API/API-5/issues/351) | Explain in the case view what does not exist and why | Frontend | victorgsnogueira | 1h | Concluído |
| [39.10](https://github.com/Concord-API/API-5/issues/352) | Test that no party, lawyer or sealed data reaches the case response | Test | victorgsnogueira | 2h | Concluído |
| [39.11](https://github.com/Concord-API/API-5/issues/353) | Document the court site sources in the ETL docs | Docs | thiagosabreu | 1h | Concluído |

### US-40 — Como usuário, quero ver os julgados que compõem a jurisprudência do tema, com tribunal, órgão julgador, data, ementa e link para a página do tribunal, no mesmo padrão de tabela dos processos, para ler como os tribunais decidiram e não apenas contar os casos

_8 SP · Should · Concluído · 8/8 tasks · 23h_

Issue: [#330](https://github.com/Concord-API/API-5/issues/330)

| # | Task | Camada | Responsável | Est. | Status |
| --- | --- | --- | --- | ---: | --- |
| [40.1](https://github.com/Concord-API/API-5/issues/354) | Harvest the rulings from the verified source | ETL | IsaacOliveiraSouza | 6h | Concluído |
| [40.2](https://github.com/Concord-API/API-5/issues/355) | Load the rulings into the warehouse with the summary as published | ETL | IsaacOliveiraSouza | 4h | Concluído |
| [40.3](https://github.com/Concord-API/API-5/issues/356) | Tie each ruling to the topic by CNJ number or by declared similarity | ETL | victorgsnogueira | 4h | Concluído |
| [40.4](https://github.com/Concord-API/API-5/issues/357) | Expose the topic's rulings with "N of M", source and extraction date | Backend | JoaoBaranov | 3h | Concluído |
| [40.5](https://github.com/Concord-API/API-5/issues/358) | Build the rulings table in the Base analítica tab | Frontend | JoaoBaranov | 3h | Concluído |
| [40.6](https://github.com/Concord-API/API-5/issues/359) | Explain in the block why a court has no rulings | Frontend | JoaoBaranov | 1h | Concluído |
| [40.7](https://github.com/Concord-API/API-5/issues/360) | Test the rulings ordering and the court without a source | Test | JoaoBaranov | 1h | Concluído |
| [40.8](https://github.com/Concord-API/API-5/issues/361) | Document the rulings source in the ETL docs | Docs | IsaacOliveiraSouza | 1h | Concluído |

### US-41 — Como usuário, quero ver os precedentes qualificados relacionados ao tema — súmulas, temas repetitivos, IRDR, IAC e repercussão geral —, com tipo, número, tribunal, tese e situação, para saber o que vincula os tribunais neste tema e não apenas como eles têm decidido

_8 SP · Should · Concluído · 7/7 tasks · 15h_

Issue: [#331](https://github.com/Concord-API/API-5/issues/331)

| # | Task | Camada | Responsável | Est. | Status |
| --- | --- | --- | --- | ---: | --- |
| [41.2](https://github.com/Concord-API/API-5/issues/363) | Add type, status date, suspension and leading cases to the precedent dimension | Backend | thiagosabreu | 3h | Concluído |
| [41.3](https://github.com/Concord-API/API-5/issues/364) | Tie each precedent to the topic by similarity over question and thesis | ETL | thiagosabreu | 4h | Concluído |
| [41.4](https://github.com/Concord-API/API-5/issues/365) | Expose the topic's related precedents | Backend | thiagosabreu | 2h | Concluído |
| [41.5](https://github.com/Concord-API/API-5/issues/366) | Build the precedents block with cancelled ones marked | Frontend | IsaacOliveiraSouza | 3h | Concluído |
| [41.6](https://github.com/Concord-API/API-5/issues/367) | Explain in the block why a topic has no related precedent | Frontend | IsaacOliveiraSouza | 1h | Concluído |
| [41.7](https://github.com/Concord-API/API-5/issues/368) | Test that labour and electoral precedents are not loaded | Test | IsaacOliveiraSouza | 1h | Concluído |
| [41.8](https://github.com/Concord-API/API-5/issues/369) | Document the precedents source in the ETL docs | Docs | thiagosabreu | 1h | Concluído |

### US-27 — Como usuário, quero exportar para CSV as decisões que sustentam o tema, para trabalhar os dados fora da ferramenta

_5 SP · Should · Concluído · 6/6 tasks · 9h_

Issue: [#327](https://github.com/Concord-API/API-5/issues/327)

| # | Task | Camada | Responsável | Est. | Status |
| --- | --- | --- | --- | ---: | --- |
| [27.1](https://github.com/Concord-API/API-5/issues/334) | Expose the theme's decisions as CSV with the same filter as the sample | Backend | thiagosabreu | 3h | Concluído |
| [27.2](https://github.com/Concord-API/API-5/issues/335) | Write the source, extraction date and scope at the top of the file | Backend | thiagosabreu | 1h | Concluído |
| [27.3](https://github.com/Concord-API/API-5/issues/336) | Encode the file for a Portuguese spreadsheet | Backend | thiagosabreu | 1h | Concluído |
| [27.4](https://github.com/Concord-API/API-5/issues/337) | Cap the exported rows and return the ceiling | Backend | IsaacOliveiraSouza | 1h | Concluído |
| [27.5](https://github.com/Concord-API/API-5/issues/338) | Add the export button with the ceiling message | Frontend | IsaacOliveiraSouza | 2h | Concluído |
| [27.6](https://github.com/Concord-API/API-5/issues/339) | Test that the file has the same rows as the screen | Test | IsaacOliveiraSouza | 1h | Concluído |

### US-28 — Como usuário, quero copiar a citação do tema já com a fonte, a data de extração, o escopo e o `n`, para colar sem redigitar

_3 SP · Should · Concluído · 3/3 tasks · 5h_

Issue: [#328](https://github.com/Concord-API/API-5/issues/328)

| # | Task | Camada | Responsável | Est. | Status |
| --- | --- | --- | --- | ---: | --- |
| [28.1](https://github.com/Concord-API/API-5/issues/340) | Build the theme citation from sourced numbers only | Backend | RichardCordeiro | 2h | Concluído |
| [28.2](https://github.com/Concord-API/API-5/issues/341) | Add the copy-citation button with a visible confirmation | Frontend | RichardCordeiro | 2h | Concluído |
| [28.3](https://github.com/Concord-API/API-5/issues/342) | Test that the citation has no markup, no forced line break and no unsourced block | Test | RichardCordeiro | 1h | Concluído |

## Technical Foundation

Tasks sem story-mãe, numeradas `0.Y`: o que a sprint precisa para que as stories tenham onde rodar (schema, pipeline de dados, caminho de carga, esqueleto de tela e correções encontradas pelo caminho).

_2 tasks · 10h · 2 concluídas_

| # | Task | Camada | Responsável | Est. | Status |
| --- | --- | --- | --- | ---: | --- |
| [0.112](https://github.com/Concord-API/API-5/issues/332) | Spike: find a lawful source of court rulings with summary for the courts in scope | Backend | JoaoBaranov | 6h | Concluído |
| [0.113](https://github.com/Concord-API/API-5/issues/333) | Spike: verify the Pangea/BNP terms of use and endpoint for qualified precedents | ETL | IsaacOliveiraSouza | 4h | Concluído |

## Entrega e processo

Tasks `DVP-xx` (CI, deploy, QA, monitoramento, testes de banco e documentação), também sem story-mãe.

_25 tasks · 65h · 25 concluídas_

| # | Task | Frente | Camada | Responsável | Est. | Status |
| --- | --- | --- | --- | --- | ---: | --- |
| [DVP-42](https://github.com/Concord-API/API-5/issues/309) | Export traces with OpenTelemetry when configured | Monitoramento | Backend | thiagosabreu | 2h | Concluído |
| [DVP-43](https://github.com/Concord-API/API-5/issues/310) | Instrument Npgsql and drop the health endpoints from traces | Monitoramento | Backend | thiagosabreu | 2h | Concluído |
| [DVP-44](https://github.com/Concord-API/API-5/issues/311) | Add the span id to the file log | Monitoramento | Backend | thiagosabreu | 1h | Concluído |
| [DVP-45](https://github.com/Concord-API/API-5/issues/312) | Test the traces contract | Monitoramento | Test | thiagosabreu | 2h | Concluído |
| [DVP-46](https://github.com/Concord-API/API-5/issues/313) | Add Tempo to the installation: WinSW, configuration and script | Monitoramento | DevOps | thiagosabreu | 3h | Concluído |
| [DVP-47](https://github.com/Concord-API/API-5/issues/314) | Provision the Tempo data source with trace-to-log correlation | Monitoramento | DevOps | thiagosabreu | 2h | Concluído |
| [DVP-51](https://github.com/Concord-API/API-5/issues/318) | Publish Grafana under /monitoramento/ through the reverse proxy | Monitoramento | DevOps | thiagosabreu | 4h | Concluído |
| [DVP-52](https://github.com/Concord-API/API-5/issues/319) | Run Alloy, Prometheus, Loki, Tempo and Grafana on the homologation environment | Monitoramento | DevOps | thiagosabreu | 6h | Concluído |
| [DVP-53](https://github.com/Concord-API/API-5/issues/320) | Collect homologation Postgres metrics with pg_stat_statements through a monitor-only role | Monitoramento | DevOps | thiagosabreu | 3h | Concluído |
| [DVP-59](https://github.com/Concord-API/API-5/issues/370) | Run a k6 load test against the API in the acceptance workflow | CI | DevOps | victorgsnogueira | 3h | Concluído |
| [DVP-60](https://github.com/Concord-API/API-5/issues/371) | Send the k6 results to Prometheus and show them on a Grafana dashboard | Monitoramento | DevOps | thiagosabreu | 5h | Concluído |
| [DVP-61](https://github.com/Concord-API/API-5/issues/372) | Test an incremental upgrade of a database that already has data | BD | Test | JoaoBaranov | 5h | Concluído |
| [DVP-62](https://github.com/Concord-API/API-5/issues/373) | Test that a load failing after the truncate leaves the previous data intact | BD | Test | JoaoBaranov | 3h | Concluído |
| [DVP-63](https://github.com/Concord-API/API-5/issues/374) | Detect drift between the pipeline schema fixture and the backend migrations | BD | DevOps | JoaoBaranov | 4h | Concluído |
| [DVP-66](https://github.com/Concord-API/API-5/issues/377) | Validate the migration tool against repeated versions | BD | DevOps | JoaoBaranov | 3h | Concluído |
| [DVP-67](https://github.com/Concord-API/API-5/issues/379) | Fix false schema drift detection for PostgreSQL metadata | BD | DevOps | JoaoBaranov | 2h | Concluído |
| [DVP-69](https://github.com/Concord-API/API-5/issues/381) | Add the board fields that the Radar fills | QA | DevOps | RichardCordeiro | 1h | Concluído |
| [DVP-70](https://github.com/Concord-API/API-5/issues/382) | Add the Radar workflow that collects the data every day | QA | DevOps | RichardCordeiro | 4h | Concluído |
| [DVP-71](https://github.com/Concord-API/API-5/issues/383) | Measure the planning and the execution of each sprint | QA | DevOps | RichardCordeiro | 3h | Concluído |
| [DVP-72](https://github.com/Concord-API/API-5/issues/384) | Build the QA charts in Insights | QA | DevOps | RichardCordeiro | 2h | Concluído |
| [DVP-74](https://github.com/Concord-API/API-5/issues/401) | Remove the Process container and move its only task to DevOps | Docs | Docs | joaoandrade17 | 1h | Concluído |
| [DVP-75](https://github.com/Concord-API/API-5/issues/404) | Cache the search filter options until the next load | Monitoramento | DevOps | thiagosabreu | 1h | Concluído |
| [DVP-76](https://github.com/Concord-API/API-5/issues/405) | Expand the search synonyms once per search | Monitoramento | DevOps | thiagosabreu | 1h | Concluído |
| [DVP-77](https://github.com/Concord-API/API-5/issues/406) | Bound the database connection pool and stop answering 500 when it times out | Monitoramento | DevOps | thiagosabreu | 1h | Concluído |
| [DVP-78](https://github.com/Concord-API/API-5/issues/407) | Extend the API latency histogram beyond 10 s | Monitoramento | DevOps | thiagosabreu | 1h | Concluído |
