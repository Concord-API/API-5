# Sprint Backlog — Sprint 3

**Janela:** 02/11 a 22/11/2026

**Board:** [GitHub Project](https://github.com/orgs/Concord-API/projects/5) · snapshot de 12/11/2026

## Meta da sprint

Stories que o time se compromete a entregar. Se alguma não for concluída, a sprint não atingiu a meta.

| ID | Prioridade | Descrição | SP | Tasks | Horas | Status |
| --- | --- | --- | ---: | ---: | ---: | --- |
| **US-13** | Could | Como **usuário**, quero que a aba que estou vendo seja refletida na URL, para enviar a um colega o link exato da parte que quero mostrar | 5 | 3 | 6h | Concluído |
| **US-39** | Should | Como **usuário**, quero ver os dados de cada processo da amostra dentro do Ratio, extraídos do site do próprio tribunal, para conferir o processo sem sair do produto | 5 | 11 | 35h | A fazer |
| **US-40** | Should | Como **usuário**, quero ver os julgados que compõem a jurisprudência do tema, com tribunal, órgão julgador, data, ementa e link para a página do tribunal, no mesmo padrão de tabela dos processos, para ler como os tribunais decidiram e não apenas contar os casos | 8 | 8 | 23h | A fazer |
| **US-41** | Should | Como **usuário**, quero ver os precedentes qualificados relacionados ao tema — súmulas, temas repetitivos, IRDR, IAC e repercussão geral —, com tipo, número, tribunal, tese e situação, para saber o que vincula os tribunais neste tema e não apenas como eles têm decidido | 8 | 8 | 21h | A fazer |

## Fora da meta

Stories planejadas na sprint, mas que podem passar para a próxima se não houver capacidade, mesmo sendo prioridade.

| ID | Prioridade | Descrição | SP | Tasks | Horas | Status |
| --- | --- | --- | ---: | ---: | ---: | --- |
| **US-27** | Should | Como **usuário**, quero exportar para CSV as decisões que sustentam o tema, para trabalhar os dados fora da ferramenta | 5 | 6 | 9h | A fazer |
| **US-28** | Should | Como **usuário**, quero copiar a citação do tema já com a fonte, a data de extração, o escopo e o `n`, para colar sem redigitar | 3 | 3 | 5h | A fazer |

## Resumo da sprint

| | Total |
| --- | ---: |
| Stories (meta / fora da meta) | 4 / 2 |
| Story points (meta / total) | 26 / 34 |
| Tasks (concluídas / total) | 25 / 68 |
| Horas (feitas / total) | 71h / 197h |
| Tasks em stories | 39 (99h) |
| Technical Foundation | 2 (10h) |
| Entrega e processo | 27 (88h) |

### Horas por responsável

| Responsável | Tasks | Horas | Concluído |
| --- | ---: | ---: | ---: |
| sem responsável | 35 | 98h | 0h |
| thiagosabreu | 24 | 67h | 53h |
| JoaoBaranov | 5 | 19h | 15h |
| vp-p | 2 | 7h | 0h |
| victorgsnogueira | 1 | 3h | 3h |
| joaoandrade17 | 1 | 3h | 0h |

### Horas por camada

| Camada | Horas | Concluído |
| --- | ---: | ---: |
| ETL | 51h | 0h |
| DevOps | 42h | 33h |
| Backend | 30h | 9h |
| Frontend | 24h | 6h |
| Docs | 24h | 8h |
| Test | 23h | 12h |
| — | 3h | 3h |

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

_5 SP · Should · A fazer · 0/11 tasks · 35h_

Issue: [#329](https://github.com/Concord-API/API-5/issues/329)

| # | Task | Camada | Responsável | Est. | Status |
| --- | --- | --- | --- | ---: | --- |
| [39.1](https://github.com/Concord-API/API-5/issues/343) | Harvest the case data from the TJSP site | ETL | — | 5h | A fazer |
| [39.2](https://github.com/Concord-API/API-5/issues/344) | Harvest the case data from the TJRJ site | ETL | — | 5h | A fazer |
| [39.3](https://github.com/Concord-API/API-5/issues/345) | Harvest the case data from the TJMG site | ETL | — | 5h | A fazer |
| [39.4](https://github.com/Concord-API/API-5/issues/346) | Harvest the case data from the STJ site | ETL | — | 4h | A fazer |
| [39.5](https://github.com/Concord-API/API-5/issues/347) | Load the case details and public movements into the warehouse | ETL | — | 4h | A fazer |
| [39.6](https://github.com/Concord-API/API-5/issues/348) | Expose a case's details and movements by its number | Backend | — | 3h | A fazer |
| [39.7](https://github.com/Concord-API/API-5/issues/349) | Remove the court link and the portal hint from the case sample | Frontend | — | 1h | A fazer |
| [39.8](https://github.com/Concord-API/API-5/issues/350) | Build the case view opened from the sample | Frontend | — | 4h | A fazer |
| [39.9](https://github.com/Concord-API/API-5/issues/351) | Explain in the case view what does not exist and why | Frontend | — | 1h | A fazer |
| [39.10](https://github.com/Concord-API/API-5/issues/352) | Test that no party, lawyer or sealed data reaches the case response | Test | — | 2h | A fazer |
| [39.11](https://github.com/Concord-API/API-5/issues/353) | Document the court site sources in the ETL docs | Docs | — | 1h | A fazer |

### US-40 — Como usuário, quero ver os julgados que compõem a jurisprudência do tema, com tribunal, órgão julgador, data, ementa e link para a página do tribunal, no mesmo padrão de tabela dos processos, para ler como os tribunais decidiram e não apenas contar os casos

_8 SP · Should · A fazer · 0/8 tasks · 23h_

Issue: [#330](https://github.com/Concord-API/API-5/issues/330)

| # | Task | Camada | Responsável | Est. | Status |
| --- | --- | --- | --- | ---: | --- |
| [40.1](https://github.com/Concord-API/API-5/issues/354) | Harvest the rulings from the verified source | ETL | — | 6h | A fazer |
| [40.2](https://github.com/Concord-API/API-5/issues/355) | Load the rulings into the warehouse with the summary as published | ETL | — | 4h | A fazer |
| [40.3](https://github.com/Concord-API/API-5/issues/356) | Tie each ruling to the topic by CNJ number or by declared similarity | ETL | — | 4h | A fazer |
| [40.4](https://github.com/Concord-API/API-5/issues/357) | Expose the topic's rulings with "N of M", source and extraction date | Backend | — | 3h | A fazer |
| [40.5](https://github.com/Concord-API/API-5/issues/358) | Build the rulings table in the Base analítica tab | Frontend | — | 3h | A fazer |
| [40.6](https://github.com/Concord-API/API-5/issues/359) | Explain in the block why a court has no rulings | Frontend | — | 1h | A fazer |
| [40.7](https://github.com/Concord-API/API-5/issues/360) | Test the rulings ordering and the court without a source | Test | — | 1h | A fazer |
| [40.8](https://github.com/Concord-API/API-5/issues/361) | Document the rulings source in the ETL docs | Docs | — | 1h | A fazer |

### US-41 — Como usuário, quero ver os precedentes qualificados relacionados ao tema — súmulas, temas repetitivos, IRDR, IAC e repercussão geral —, com tipo, número, tribunal, tese e situação, para saber o que vincula os tribunais neste tema e não apenas como eles têm decidido

_8 SP · Should · A fazer · 0/8 tasks · 21h_

Issue: [#331](https://github.com/Concord-API/API-5/issues/331)

| # | Task | Camada | Responsável | Est. | Status |
| --- | --- | --- | --- | ---: | --- |
| [41.1](https://github.com/Concord-API/API-5/issues/362) | Harvest the qualified precedents of the courts in scope from the verified source | ETL | — | 6h | A fazer |
| [41.2](https://github.com/Concord-API/API-5/issues/363) | Add type, status date, suspension and leading cases to the precedent dimension | Backend | — | 3h | A fazer |
| [41.3](https://github.com/Concord-API/API-5/issues/364) | Tie each precedent to the topic by similarity over question and thesis | ETL | — | 4h | A fazer |
| [41.4](https://github.com/Concord-API/API-5/issues/365) | Expose the topic's related precedents | Backend | — | 2h | A fazer |
| [41.5](https://github.com/Concord-API/API-5/issues/366) | Build the precedents block with cancelled ones marked | Frontend | — | 3h | A fazer |
| [41.6](https://github.com/Concord-API/API-5/issues/367) | Explain in the block why a topic has no related precedent | Frontend | — | 1h | A fazer |
| [41.7](https://github.com/Concord-API/API-5/issues/368) | Test that labour and electoral precedents are not loaded | Test | — | 1h | A fazer |
| [41.8](https://github.com/Concord-API/API-5/issues/369) | Document the precedents source in the ETL docs | Docs | — | 1h | A fazer |

### US-27 — Como usuário, quero exportar para CSV as decisões que sustentam o tema, para trabalhar os dados fora da ferramenta

_5 SP · Should · A fazer · 2/6 tasks · 9h_

Issue: [#327](https://github.com/Concord-API/API-5/issues/327)

| # | Task | Camada | Responsável | Est. | Status |
| --- | --- | --- | --- | ---: | --- |
| [27.1](https://github.com/Concord-API/API-5/issues/334) | Expose the theme's decisions as CSV with the same filter as the sample | Backend | thiagosabreu | 3h | Concluído |
| [27.2](https://github.com/Concord-API/API-5/issues/335) | Write the source, extraction date and scope at the top of the file | Backend | thiagosabreu | 1h | Concluído |
| [27.3](https://github.com/Concord-API/API-5/issues/336) | Encode the file for a Portuguese spreadsheet | Backend | thiagosabreu | 1h | Em revisão |
| [27.4](https://github.com/Concord-API/API-5/issues/337) | Cap the exported rows and return the ceiling | Backend | — | 1h | A fazer |
| [27.5](https://github.com/Concord-API/API-5/issues/338) | Add the export button with the ceiling message | Frontend | — | 2h | A fazer |
| [27.6](https://github.com/Concord-API/API-5/issues/339) | Test that the file has the same rows as the screen | Test | — | 1h | A fazer |

### US-28 — Como usuário, quero copiar a citação do tema já com a fonte, a data de extração, o escopo e o `n`, para colar sem redigitar

_3 SP · Should · A fazer · 0/3 tasks · 5h_

Issue: [#328](https://github.com/Concord-API/API-5/issues/328)

| # | Task | Camada | Responsável | Est. | Status |
| --- | --- | --- | --- | ---: | --- |
| [28.1](https://github.com/Concord-API/API-5/issues/340) | Build the theme citation from sourced numbers only | Backend | — | 2h | A fazer |
| [28.2](https://github.com/Concord-API/API-5/issues/341) | Add the copy-citation button with a visible confirmation | Frontend | — | 2h | A fazer |
| [28.3](https://github.com/Concord-API/API-5/issues/342) | Test that the citation has no markup, no forced line break and no unsourced block | Test | — | 1h | A fazer |

## Technical Foundation

Tasks sem story-mãe, numeradas `0.Y`: o que a sprint precisa para que as stories tenham onde rodar (schema, pipeline de dados, caminho de carga, esqueleto de tela e correções encontradas pelo caminho).

_2 tasks · 10h · 0 concluídas_

| # | Task | Camada | Responsável | Est. | Status |
| --- | --- | --- | --- | ---: | --- |
| [0.112](https://github.com/Concord-API/API-5/issues/332) | Spike: find a lawful source of court rulings with summary for the courts in scope | Backend | — | 6h | A fazer |
| [0.113](https://github.com/Concord-API/API-5/issues/333) | Spike: verify the Pangea/BNP terms of use and endpoint for qualified precedents | ETL | — | 4h | A fazer |

## Entrega e processo

Tasks `DVP-xx` (CI, deploy, QA, monitoramento, testes de banco) e `PRC-xx` (processo), também sem story-mãe.

_27 tasks · 88h · 20 concluídas_

| # | Task | Frente | Camada | Responsável | Est. | Status |
| --- | --- | --- | --- | --- | ---: | --- |
| [DVP-14](https://github.com/Concord-API/API-5/issues/183) | Add the end-to-end smoke test from search to theme detail | Testes | Test | vp-p | 5h | A fazer |
| [DVP-39](https://github.com/Concord-API/API-5/issues/292) | Document where the API integration tests live and which CI job runs them | Testes | Docs | vp-p | 2h | A fazer |
| [DVP-42](https://github.com/Concord-API/API-5/issues/309) | Export traces with OpenTelemetry when configured | Monitoramento | Backend | thiagosabreu | 2h | Concluído |
| [DVP-43](https://github.com/Concord-API/API-5/issues/310) | Instrument Npgsql and drop the health endpoints from traces | Monitoramento | Backend | thiagosabreu | 2h | Concluído |
| [DVP-44](https://github.com/Concord-API/API-5/issues/311) | Add the span id to the file log | Monitoramento | Backend | thiagosabreu | 1h | Concluído |
| [DVP-45](https://github.com/Concord-API/API-5/issues/312) | Test the traces contract | Monitoramento | Test | thiagosabreu | 2h | Concluído |
| [DVP-46](https://github.com/Concord-API/API-5/issues/313) | Add Tempo to the installation: WinSW, configuration and script | Monitoramento | DevOps | thiagosabreu | 3h | Concluído |
| [DVP-47](https://github.com/Concord-API/API-5/issues/314) | Provision the Tempo data source with trace-to-log correlation | Monitoramento | DevOps | thiagosabreu | 2h | Concluído |
| [DVP-48](https://github.com/Concord-API/API-5/issues/315) | Collect the reverse proxy access logs in Alloy | Monitoramento | DevOps | thiagosabreu | 2h | Concluído |
| [DVP-49](https://github.com/Concord-API/API-5/issues/316) | Configure the proxy log and delete files older than 15 days | Monitoramento | DevOps | thiagosabreu | 2h | Concluído |
| [DVP-50](https://github.com/Concord-API/API-5/issues/317) | Provision the alert rules | Monitoramento | DevOps | thiagosabreu | 5h | Concluído |
| [DVP-51](https://github.com/Concord-API/API-5/issues/318) | Publish Grafana under /monitoramento/ through the reverse proxy | Monitoramento | DevOps | thiagosabreu | 4h | A fazer |
| [DVP-52](https://github.com/Concord-API/API-5/issues/319) | Run Alloy, Prometheus, Loki, Tempo and Grafana on the homologation environment | Monitoramento | DevOps | thiagosabreu | 6h | Concluído |
| [DVP-53](https://github.com/Concord-API/API-5/issues/320) | Collect homologation Postgres metrics with pg_stat_statements through a monitor-only role | Monitoramento | DevOps | thiagosabreu | 3h | Concluído |
| [DVP-54](https://github.com/Concord-API/API-5/issues/321) | Hand the observability folder to the release package | Monitoramento | DevOps | thiagosabreu | 3h | Concluído |
| [DVP-55](https://github.com/Concord-API/API-5/issues/322) | Measure the stack on the VM and add RAM, disk and retention to the machine specification | Monitoramento | Docs | thiagosabreu | 3h | Concluído |
| [DVP-56](https://github.com/Concord-API/API-5/issues/323) | Write the observability documentation in the new API-5 structure | Monitoramento | Docs | thiagosabreu | 4h | A fazer |
| [DVP-57](https://github.com/Concord-API/API-5/issues/324) | Document installing, accessing and updating the monitoring in the manuals | Monitoramento | Docs | thiagosabreu | 5h | Concluído |
| [DVP-58](https://github.com/Concord-API/API-5/issues/325) | Add the observability checks to the installation rehearsal | Monitoramento | Test | thiagosabreu | 2h | Concluído |
| [DVP-59](https://github.com/Concord-API/API-5/issues/370) | Run a k6 load test against the API in the acceptance workflow | CI | DevOps | victorgsnogueira | 3h | Concluído |
| [DVP-60](https://github.com/Concord-API/API-5/issues/371) | Send the k6 results to Prometheus and show them on a Grafana dashboard | Monitoramento | DevOps | thiagosabreu | 5h | A fazer |
| [DVP-61](https://github.com/Concord-API/API-5/issues/372) | Test an incremental upgrade of a database that already has data | BD | Test | JoaoBaranov | 5h | Concluído |
| [DVP-62](https://github.com/Concord-API/API-5/issues/373) | Test that a load failing after the truncate leaves the previous data intact | BD | Test | JoaoBaranov | 3h | Concluído |
| [DVP-63](https://github.com/Concord-API/API-5/issues/374) | Detect drift between the pipeline schema fixture and the backend migrations | BD | DevOps | JoaoBaranov | 4h | Concluído |
| [DVP-64](https://github.com/Concord-API/API-5/issues/375) | Write the database deployment, backup and recovery checklist for the client server | BD | Docs | JoaoBaranov | 4h | A fazer |
| [DVP-65](https://github.com/Concord-API/API-5/issues/376) | Document the database process in the API-5 repository | Docs | Docs | joaoandrade17 | 3h | A fazer |
| [DVP-66](https://github.com/Concord-API/API-5/issues/377) | Validate the migration tool against repeated versions | BD | — | JoaoBaranov | 3h | Concluído |
