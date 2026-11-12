# Sprint Backlog — Sprint 2

**Window:** Oct 5 to Oct 25, 2026

**Board:** [GitHub Project](https://github.com/orgs/Concord-API/projects/5) · snapshot of Nov 12, 2026

## Sprint goal

Stories the team commits to delivering. If any of them is not completed, the sprint did not meet its goal.

| ID | Priority | Description | SP | Tasks | Hours | Status |
| --- | --- | --- | ---: | ---: | ---: | --- |
| **US-03** | Must | As a **user**, I want to see in each result the score, the area of law (vara), the thesis title, a short summary, the courts, the volume, the period, the last decision and the favourable percentage, so that I can compare theses before opening any of them | 8 | 11 | 35h | Done |
| **US-04** | Must | As a **user**, I want to filter results by court, period, instance and minimum strength, seeing how many cases each court has, so that I can narrow the list down to my case | 5 | 8 | 18h | Done |
| **US-12** | Must | As a **user**, I want to see the topic's alignment by court, so that I know whether the thesis holds the same in São Paulo, Rio de Janeiro, Minas Gerais and the superior courts (STJ and STF) | 3 | 6 | 12h | Done |
| **US-14** | Must | As a **user**, I want a table of each court's behaviour — decisions, alignment and date of the latest one — so that I can compare my court with the others | 3 | 5 | 7h | Done |
| **US-15** | Must | As a **user**, I want an auditable sample of the cases behind the topic, with panel, date and outcome, so that I can check the cases before citing them | 5 | 9 | 12h | Done |
| **US-17** | Should | As a **user**, I want to know whether the panels of my court are deciding alike, so that I can spot internal divergence before deciding | 5 | 5 | 19h | Done |

## Outside the goal

Stories planned in the sprint that can move to the next one if there is not enough capacity, even though they are priorities.

| ID | Priority | Description | SP | Tasks | Hours | Status |
| --- | --- | --- | ---: | ---: | ---: | --- |
| **US-07** | Must | As a **user**, I want the score to come with a grade in language that already exists in the legal field — Consolidada, Dominante, Em formação, Divergente — so that I do not have to interpret an invented scale | 2 | 4 | 4h | Done |
| **US-11** | Must | As a **user**, I want to see how the topic's alignment evolved year by year, with the trend sentence, so that I know whether the understanding is settling or shifting | 5 | 6 | 9h | Done |

## Sprint summary

| | Total |
| --- | ---: |
| Stories (goal / outside the goal) | 6 / 2 |
| Story points (goal / total) | 29 / 36 |
| Tasks (done / total) | 120 / 120 |
| Hours (done / total) | 273h / 273h |
| Tasks in stories | 54 (116h) |
| Technical Foundation | 28 (62h) |
| Delivery and process | 38 (95h) |

### Hours by assignee

| Assignee | Tasks | Hours | Done |
| --- | ---: | ---: | ---: |
| victorgsnogueira | 39 | 97.5h | 97.5h |
| thiagosabreu | 28 | 49h | 49h |
| RichardCordeiro | 19 | 42h | 42h |
| JoaoBaranov | 19 | 42h | 42h |
| IsaacOliveiraSouza | 13 | 28.5h | 28.5h |
| vp-p | 3 | 11h | 11h |
| joaoandrade17 | 1 | 3h | 3h |

### Hours by layer

| Layer | Hours | Done |
| --- | ---: | ---: |
| Backend | 74h | 74h |
| Frontend | 57h | 57h |
| DevOps | 55h | 55h |
| ETL | 43h | 43h |
| Test | 31h | 31h |
| Docs | 13h | 13h |

_Hours of a task with more than one assignee are split evenly between them._

## Stories and tasks

### US-03 — As a user, I want to see in each result the score, the area of law (vara), the thesis title, a short summary, the courts, the volume, the period, the last decision and the favourable percentage, so that I can compare theses before opening any of them

_8 SP · Must · Done · 11/11 tasks · 35h_

Issue: [#166](https://github.com/Concord-API/API-5/issues/166)

| # | Task | Layer | Assignee | Est. | Status |
| --- | --- | --- | --- | ---: | --- |
| [3.1](https://github.com/Concord-API/API-5/issues/186) | Expose area, title, summary, courts, volume, period, last decision and upheld percentage per result | Backend | RichardCordeiro | 6h | Done |
| [3.2](https://github.com/Concord-API/API-5/issues/187) | Return the short summary of up to two lines per theme | Backend | RichardCordeiro | 3h | Done |
| [3.3](https://github.com/Concord-API/API-5/issues/188) | Return the court acronyms with the exact +N difference | Backend | JoaoBaranov | 3h | Done |
| [3.4](https://github.com/Concord-API/API-5/issues/189) | Build the result item with the area tag and the thesis title | Frontend | RichardCordeiro | 5h | Done |
| [3.5](https://github.com/Concord-API/API-5/issues/190) | Build the AlignmentBar with the count next to it | Frontend | JoaoBaranov | 4h | Done |
| [3.6](https://github.com/Concord-API/API-5/issues/191) | Render the court chips with the +N indicator only when needed | Frontend | JoaoBaranov | 3h | Done |
| [3.7](https://github.com/Concord-API/API-5/issues/192) | Format the numbers in Portuguese and never recompute them | Frontend | RichardCordeiro | 2h | Done |
| [3.8](https://github.com/Concord-API/API-5/issues/193) | Show the count instead of the percentage below the percentage floor | Frontend | RichardCordeiro | 2h | Done |
| [3.9](https://github.com/Concord-API/API-5/issues/194) | Open the theme detail from the result item | Frontend | RichardCordeiro | 2h | Done |
| [3.10](https://github.com/Concord-API/API-5/issues/195) | Test that the item renders every field of the contract | Test | RichardCordeiro | 3h | Done |
| [3.11](https://github.com/Concord-API/API-5/issues/196) | Show the score circle in the result item | Frontend | RichardCordeiro | 2h | Done |

### US-04 — As a user, I want to filter results by court, period, instance and minimum strength, seeing how many cases each court has, so that I can narrow the list down to my case

_5 SP · Must · Done · 8/8 tasks · 18h_

Issue: [#16](https://github.com/Concord-API/API-5/issues/16)

| # | Task | Layer | Assignee | Est. | Status |
| --- | --- | --- | --- | ---: | --- |
| [4.1](https://github.com/Concord-API/API-5/issues/197) | Accept court, period, instance and minimum strength on GET /api/themes | Backend | thiagosabreu | 6h | Done |
| [4.2](https://github.com/Concord-API/API-5/issues/198) | Return the case count per court with the filter options | Backend | thiagosabreu | 4h | Done |
| [4.3](https://github.com/Concord-API/API-5/issues/199) | Offer only the instances that exist in the loaded scope | Backend | RichardCordeiro | 1h | Done |
| [4.4](https://github.com/Concord-API/API-5/issues/200) | Build the filter bar with the court counts | Frontend | RichardCordeiro | 2h | Done |
| [4.5](https://github.com/Concord-API/API-5/issues/201) | Reflect the active filters in the URL | Frontend | RichardCordeiro | 2h | Done |
| [4.6](https://github.com/Concord-API/API-5/issues/202) | Clear every filter and rebuild the list | Frontend | RichardCordeiro | 1h | Done |
| [4.7](https://github.com/Concord-API/API-5/issues/203) | Describe the applied narrowing when nothing matches | Frontend | RichardCordeiro | 1h | Done |
| [4.8](https://github.com/Concord-API/API-5/issues/204) | Test that the filtering happens in the API, never in the browser | Test | RichardCordeiro | 1h | Done |

### US-12 — As a user, I want to see the topic's alignment by court, so that I know whether the thesis holds the same in São Paulo, Rio de Janeiro, Minas Gerais and the superior courts (STJ and STF)

_3 SP · Must · Done · 6/6 tasks · 12h_

Issue: [#221](https://github.com/Concord-API/API-5/issues/221)

| # | Task | Layer | Assignee | Est. | Status |
| --- | --- | --- | --- | ---: | --- |
| [12.1](https://github.com/Concord-API/API-5/issues/235) | Create the alignment-by-court aggregate with merit and appeals apart | Backend | JoaoBaranov | 4h | Done |
| [12.2](https://github.com/Concord-API/API-5/issues/236) | Expose per court the percentage, its n and its polarity label | Backend | JoaoBaranov | 3h | Done |
| [12.3](https://github.com/Concord-API/API-5/issues/237) | Test that the courts add up to the theme total | Test | JoaoBaranov | 1h | Done |
| [12.4](https://github.com/Concord-API/API-5/issues/238) | Build the alignment-by-court list | Frontend | JoaoBaranov | 2h | Done |
| [12.5](https://github.com/Concord-API/API-5/issues/239) | Show a court without judgments as having no data | Frontend | JoaoBaranov | 1h | Done |
| [12.6](https://github.com/Concord-API/API-5/issues/284) | Fix the theme by court migration version and the Acceptance refresh | Backend | JoaoBaranov | 1h | Done |

### US-14 — As a user, I want a table of each court's behaviour — decisions, alignment and date of the latest one — so that I can compare my court with the others

_3 SP · Must · Done · 5/5 tasks · 7h_

Issue: [#167](https://github.com/Concord-API/API-5/issues/167)

| # | Task | Layer | Assignee | Est. | Status |
| --- | --- | --- | --- | ---: | --- |
| [14.1](https://github.com/Concord-API/API-5/issues/205) | Expose the behaviour per court: decisions, alignment and last decision | Backend | victorgsnogueira | 2h | Done |
| [14.2](https://github.com/Concord-API/API-5/issues/206) | Build the behaviour table with the visual rules | Frontend | victorgsnogueira | 2h | Done |
| [14.3](https://github.com/Concord-API/API-5/issues/207) | Scroll a wide table inside its container | Frontend | victorgsnogueira | 1h | Done |
| [14.4](https://github.com/Concord-API/API-5/issues/208) | Flag the amount column as unsourced | Frontend | victorgsnogueira | 1h | Done |
| [14.5](https://github.com/Concord-API/API-5/issues/209) | Show the appeal outcome rate in a superior court row | Backend | victorgsnogueira | 1h | Done |

### US-15 — As a user, I want an auditable sample of the cases behind the topic, with panel, date and outcome, so that I can check the cases before citing them

_5 SP · Must · Done · 9/9 tasks · 12h_

Issue: [#168](https://github.com/Concord-API/API-5/issues/168)

| # | Task | Layer | Assignee | Est. | Status |
| --- | --- | --- | --- | ---: | --- |
| [15.1](https://github.com/Concord-API/API-5/issues/210) | Create the case view behind the theme sample | Backend | thiagosabreu | 1h | Done |
| [15.2](https://github.com/Concord-API/API-5/issues/211) | Expose GET /api/themes/{key}/cases with a stable ordering | Backend | thiagosabreu | 2h | Done |
| [15.3](https://github.com/Concord-API/API-5/issues/212) | Return "N of M decisions" with the sample | Backend | thiagosabreu | 1h | Done |
| [15.4](https://github.com/Concord-API/API-5/issues/213) | Flag a sealed case and hide its data | Backend | thiagosabreu | 1h | Done |
| [15.5](https://github.com/Concord-API/API-5/issues/214) | Return the reporter judge and amount columns empty and flagged | Backend | thiagosabreu | 1h | Done |
| [15.6](https://github.com/Concord-API/API-5/issues/215) | Name the judging body of a superior court in the chamber column | Backend | thiagosabreu | 1h | Done |
| [15.7](https://github.com/Concord-API/API-5/issues/216) | Build the auditable sample table | Frontend | IsaacOliveiraSouza | 3h | Done |
| [15.8](https://github.com/Concord-API/API-5/issues/217) | Link every case number to the court with the formatted number | Frontend | IsaacOliveiraSouza | 1h | Done |
| [15.9](https://github.com/Concord-API/API-5/issues/218) | Test that the ordering is the same between two calls | Test | IsaacOliveiraSouza | 1h | Done |

### US-17 — As a user, I want to know whether the panels of my court are deciding alike, so that I can spot internal divergence before deciding

_5 SP · Should · Done · 5/5 tasks · 19h_

Issue: [#222](https://github.com/Concord-API/API-5/issues/222)

| # | Task | Layer | Assignee | Est. | Status |
| --- | --- | --- | --- | ---: | --- |
| [17.1](https://github.com/Concord-API/API-5/issues/240) | Create the alignment-by-judging-body aggregate | Backend | victorgsnogueira | 4h | Done |
| [17.2](https://github.com/Concord-API/API-5/issues/241) | Flag a panel 20 points away from its court, from 5 judged cases up | Backend | victorgsnogueira | 3h | Done |
| [17.3](https://github.com/Concord-API/API-5/issues/242) | Expose the panels per court with their n, hiding a panel with one judgment | Backend | victorgsnogueira | 4h | Done |
| [17.4](https://github.com/Concord-API/API-5/issues/243) | Test that a court's panels add up to the court total | Test | victorgsnogueira | 3h | Done |
| [17.5](https://github.com/Concord-API/API-5/issues/244) | Build the panel block with the divergence flag | Frontend | victorgsnogueira | 5h | Done |

### US-07 — As a user, I want the score to come with a grade in language that already exists in the legal field — Consolidada, Dominante, Em formação, Divergente — so that I do not have to interpret an invented scale

_2 SP · Must · Done · 4/4 tasks · 4h_

Issue: [#219](https://github.com/Concord-API/API-5/issues/219)

| # | Task | Layer | Assignee | Est. | Status |
| --- | --- | --- | --- | ---: | --- |
| [7.1](https://github.com/Concord-API/API-5/issues/225) | Return the grade only from 10 judged cases up | Backend | IsaacOliveiraSouza | 1h | Done |
| [7.2](https://github.com/Concord-API/API-5/issues/226) | Show the grade next to the score | Frontend | IsaacOliveiraSouza | 1h | Done |
| [7.3](https://github.com/Concord-API/API-5/issues/227) | Show the score without the textual grade below the minimum | Frontend | IsaacOliveiraSouza | 1h | Done |
| [7.4](https://github.com/Concord-API/API-5/issues/228) | Test the band boundaries at 55, 75 and 90 and the minimum of 10 | Test | IsaacOliveiraSouza | 1h | Done |

### US-11 — As a user, I want to see how the topic's alignment evolved year by year, with the trend sentence, so that I know whether the understanding is settling or shifting

_5 SP · Must · Done · 6/6 tasks · 9h_

Issue: [#220](https://github.com/Concord-API/API-5/issues/220)

| # | Task | Layer | Assignee | Est. | Status |
| --- | --- | --- | --- | ---: | --- |
| [11.1](https://github.com/Concord-API/API-5/issues/229) | Create the yearly alignment aggregate per theme | Backend | JoaoBaranov | 2h | Done |
| [11.2](https://github.com/Concord-API/API-5/issues/230) | Expose the yearly series ordered oldest to newest | Backend | JoaoBaranov | 2h | Done |
| [11.3](https://github.com/Concord-API/API-5/issues/231) | Return the trend sentence values from the aggregate | Backend | JoaoBaranov | 1h | Done |
| [11.4](https://github.com/Concord-API/API-5/issues/232) | Build the yearly alignment bars in the side column | Frontend | JoaoBaranov | 2h | Done |
| [11.5](https://github.com/Concord-API/API-5/issues/233) | Highlight the most recent year and skip the years with no result | Frontend | JoaoBaranov | 1h | Done |
| [11.6](https://github.com/Concord-API/API-5/issues/234) | Hide the trend sentence when there is data in a single year | Frontend | JoaoBaranov | 1h | Done |

## Technical Foundation

Tasks with no parent story, numbered `0.Y`: what the sprint needs so the stories have somewhere to run (schema, data pipeline, load path, screen skeleton and fixes found along the way).

_28 tasks · 62h · 28 done_

| # | Task | Layer | Assignee | Est. | Status |
| --- | --- | --- | --- | ---: | --- |
| [0.47](https://github.com/Concord-API/API-5/issues/178) | Top up the harvest for themes with fewer than 5 judged cases | ETL | victorgsnogueira | 6h | Done |
| [0.48](https://github.com/Concord-API/API-5/issues/179) | Add the schema version to the load script and refuse a mismatched database | ETL | victorgsnogueira | 4h | Done |
| [0.49](https://github.com/Concord-API/API-5/issues/180) | Add the load manifest with row counts and the extraction date | ETL | victorgsnogueira | 3h | Done |
| [0.86](https://github.com/Concord-API/API-5/issues/169) | Allow the superior-court level in the court level constraint | Backend | JoaoBaranov | 3h | Done |
| [0.87](https://github.com/Concord-API/API-5/issues/170) | Harvest the STJ civil cases from DataJud | ETL | victorgsnogueira | 6h | Done |
| [0.88](https://github.com/Concord-API/API-5/issues/171) | Map the DataJud instance of STJ cases to the superior-court level | ETL | victorgsnogueira | 2h | Done |
| [0.89](https://github.com/Concord-API/API-5/issues/172) | Map the STJ judging bodies: panels, sections and the Special Court | ETL | victorgsnogueira | 3h | Done |
| [0.90](https://github.com/Concord-API/API-5/issues/173) | Seed the STJ in the court reference data | ETL | victorgsnogueira | 2h | Done |
| [0.91](https://github.com/Concord-API/API-5/issues/174) | Check whether one case is counted both in a state court and in the STJ | Test | victorgsnogueira | 4h | Done |
| [0.92](https://github.com/Concord-API/API-5/issues/175) | Map the source link for STJ cases | ETL | victorgsnogueira | 3h | Done |
| [0.93](https://github.com/Concord-API/API-5/issues/176) | Spike: find a source for STF decisions | ETL | victorgsnogueira | 6h | Done |
| [0.94](https://github.com/Concord-API/API-5/issues/177) | Register the decision on the STF source | Docs | victorgsnogueira | 1h | Done |
| [0.96](https://github.com/Concord-API/API-5/issues/185) | Replace every hand-written court list in the screens with the scope from the API | Frontend | IsaacOliveiraSouza | 1h | Done |
| [0.97](https://github.com/Concord-API/API-5/issues/223) | Add the grade, divergence and coverage settings to the strength configuration | Backend | JoaoBaranov | 3h | Done |
| [0.98](https://github.com/Concord-API/API-5/issues/224) | Seed the new strength settings in the load file | ETL | victorgsnogueira | 2h | Done |
| [0.99](https://github.com/Concord-API/API-5/issues/278) | Harvest the STJ appeals instead of the civil classes | ETL | victorgsnogueira | 1h | Done |
| [0.100](https://github.com/Concord-API/API-5/issues/288) | Discard a movement dated before 1940 or after the collection | ETL | victorgsnogueira | 1h | Done |
| [0.101](https://github.com/Concord-API/API-5/issues/296) | Fix the panels named after a cabinet, the doctrine source names and the repeated doctrine | Backend | victorgsnogueira | 1h | Done |
| [0.102](https://github.com/Concord-API/API-5/issues/298) | Link each theme to the STJ theses that rule on its subjects | ETL | victorgsnogueira | 1h | Done |
| [0.103](https://github.com/Concord-API/API-5/issues/299) | Write the theme opening in plain words | Frontend | victorgsnogueira | 1h | Done |
| [0.104](https://github.com/Concord-API/API-5/issues/300) | Remove the empty amount column and group the missing data notes | Frontend | victorgsnogueira | 1h | Done |
| [0.105](https://github.com/Concord-API/API-5/issues/301) | Show the appeal outcome apart for the state courts and the STJ | Backend | victorgsnogueira | 1h | Done |
| [0.106](https://github.com/Concord-API/API-5/issues/302) | Keep the yearly alignment list inside a scrolling box | Frontend | victorgsnogueira | 1h | Done |
| [0.107](https://github.com/Concord-API/API-5/issues/303) | Paginate the panel list of each court in the analytic base tab | Frontend | thiagosabreu | 1h | Done |
| [0.108](https://github.com/Concord-API/API-5/issues/304) | Keep the divergence note on the same line as the panel rate | Frontend | thiagosabreu | 1h | Done |
| [0.109](https://github.com/Concord-API/API-5/issues/305) | Write the panel names in one consistent case | Frontend | thiagosabreu | 1h | Done |
| [0.110](https://github.com/Concord-API/API-5/issues/306) | Remove the missing source data list from the theme page | Frontend | thiagosabreu | 1h | Done |
| [0.111](https://github.com/Concord-API/API-5/issues/307) | Make the panel pages stand out | Frontend | thiagosabreu | 1h | Done |

## Delivery and process

Tasks `DVP-xx` (CI, deploy, QA, monitoring, database tests) and `PRC-xx` (process), also with no parent story.

_38 tasks · 95h · 38 done_

| # | Task | Front | Layer | Assignee | Est. | Status |
| --- | --- | --- | --- | --- | ---: | --- |
| [DVP-01](https://github.com/Concord-API/API-5/issues/247) | Reuse the test coverage in the quality job instead of running the tests again | CI | DevOps | victorgsnogueira | 3h | Done |
| [PRC-01](https://github.com/Concord-API/API-5/issues/260) | Set up the DVP and PRC task prefixes on the board | — | Docs | joaoandrade17 | 3h | Done |
| [DVP-02](https://github.com/Concord-API/API-5/issues/248) | Validate the pipeline against the API migrations in CI | CI | ETL | victorgsnogueira | 3h | Done |
| [DVP-03](https://github.com/Concord-API/API-5/issues/249) | Run the API and the frontend together with the sample load in an acceptance workflow | CI | DevOps | victorgsnogueira | 6h | Done |
| [DVP-04](https://github.com/Concord-API/API-5/issues/250) | Run the commit checks only on task pull requests and on main, and require the acceptance check to merge into main | CI | DevOps | victorgsnogueira | 3h | Done |
| [DVP-06](https://github.com/Concord-API/API-5/issues/252) | Align the Definition of Done with how the project works today | QA | Docs | RichardCordeiro | 2h | Done |
| [DVP-07](https://github.com/Concord-API/API-5/issues/253) | Add the QA checklist to the pull request template from a US branch to main | QA | Docs | RichardCordeiro | 1h | Done |
| [DVP-08](https://github.com/Concord-API/API-5/issues/254) | Validate real API responses against the frontend zod schemas | QA | Test | RichardCordeiro | 4h | Done |
| [DVP-09](https://github.com/Concord-API/API-5/issues/256) | Create and configure the test virtual machine with every dependency the application needs | Deploy | DevOps | IsaacOliveiraSouza | 6h | Done |
| [DVP-10](https://github.com/Concord-API/API-5/issues/255) | Deploy every release to the test virtual machine automatically | Deploy | DevOps | IsaacOliveiraSouza | 6h | Done |
| [DVP-11](https://github.com/Concord-API/API-5/issues/257) | Document the automated deploy | Deploy | Docs | IsaacOliveiraSouza | 3h | Done |
| [DVP-12](https://github.com/Concord-API/API-5/issues/181) | Publish the load script as a versioned pipeline release | CI | DevOps | IsaacOliveiraSouza, victorgsnogueira | 3h | Done |
| [DVP-13](https://github.com/Concord-API/API-5/issues/182) | Run the API on the homologation server so it creates the schema and the team loads the data file | Deploy | DevOps | IsaacOliveiraSouza, victorgsnogueira | 4h | Done |
| [DVP-15](https://github.com/Concord-API/API-5/issues/258) | Run the database checks in their own CI job | BD | DevOps | JoaoBaranov | 3h | Done |
| [DVP-16](https://github.com/Concord-API/API-5/issues/259) | Document PostgreSQL 16, Testcontainers and DbUp in the database tests | BD | Docs | JoaoBaranov | 2h | Done |
| [DVP-18](https://github.com/Concord-API/API-5/issues/264) | Export metrics with OpenTelemetry only when an OTLP endpoint is configured | Monitoramento | Backend | thiagosabreu | 2h | Done |
| [DVP-19](https://github.com/Concord-API/API-5/issues/265) | Expose warehouse availability and last-extraction age as metrics | Monitoramento | Backend | thiagosabreu | 3h | Done |
| [DVP-20](https://github.com/Concord-API/API-5/issues/266) | Count searches with no result without recording the query text | Monitoramento | Backend | thiagosabreu | 1h | Done |
| [DVP-21](https://github.com/Concord-API/API-5/issues/267) | Send the API logs over OTLP when configured | Monitoramento | Backend | thiagosabreu | 1h | Done |
| [DVP-22](https://github.com/Concord-API/API-5/issues/268) | Test the metrics and logs contract | Monitoramento | Test | thiagosabreu | 2h | Done |
| [DVP-23](https://github.com/Concord-API/API-5/issues/269) | Write the WinSW definitions and the Windows configuration for Prometheus and Loki | Monitoramento | DevOps | thiagosabreu | 2h | Done |
| [DVP-24](https://github.com/Concord-API/API-5/issues/270) | Write the install script for Alloy, Prometheus, Loki and Grafana | Monitoramento | DevOps | thiagosabreu | 3h | Done |
| [DVP-25](https://github.com/Concord-API/API-5/issues/271) | Prepare the client's Postgres with pg_stat_statements and a monitoring user | Monitoramento | DevOps | thiagosabreu | 2h | Done |
| [DVP-26](https://github.com/Concord-API/API-5/issues/272) | Collect Windows, IIS, service and Postgres metrics in Alloy | Monitoramento | DevOps | thiagosabreu | 2h | Done |
| [DVP-27](https://github.com/Concord-API/API-5/issues/273) | Probe /health and /health/ready every minute from Alloy | Monitoramento | DevOps | thiagosabreu | 1h | Done |
| [DVP-28](https://github.com/Concord-API/API-5/issues/274) | Configure Grafana for offline use with a single admin account | Monitoramento | DevOps | thiagosabreu | 1h | Done |
| [DVP-29](https://github.com/Concord-API/API-5/issues/275) | Provision the Prometheus and Loki data sources | Monitoramento | DevOps | thiagosabreu | 1h | Done |
| [DVP-30](https://github.com/Concord-API/API-5/issues/276) | Provision the overview, API, data, database and server dashboards as code | Monitoramento | DevOps | thiagosabreu | 3h | Done |
| [DVP-31](https://github.com/Concord-API/API-5/issues/277) | Validate the Alloy and Prometheus configuration in CI | Monitoramento | DevOps | thiagosabreu | 2h | Done |
| [DVP-32](https://github.com/Concord-API/API-5/issues/279) | Write the sample load to a fixed file name | CI | DevOps | victorgsnogueira | 1h | Done |
| [DVP-33](https://github.com/Concord-API/API-5/issues/280) | Require the Sonar quality gate on the way to main | CI | DevOps | victorgsnogueira | 1h | Done |
| [DVP-34](https://github.com/Concord-API/API-5/issues/281) | Add the Sonar quality gate to the Definition of Done | QA | Docs | RichardCordeiro | 1h | Done |
| [DVP-35](https://github.com/Concord-API/API-5/issues/285) | Make the QA checklist a self-review by the story’s author | QA | DevOps | RichardCordeiro | 1h | Done |
| [DVP-36](https://github.com/Concord-API/API-5/issues/289) | Run the API against a disposable PostgreSQL in the integration tests | Testes | Test | vp-p | 5h | Done |
| [DVP-37](https://github.com/Concord-API/API-5/issues/290) | Test the theme search and detail endpoints against the sample load | Testes | Test | vp-p | 4h | Done |
| [DVP-38](https://github.com/Concord-API/API-5/issues/291) | Test the theme panels endpoint against the sample load | Testes | Test | vp-p | 2h | Done |
| [DVP-40](https://github.com/Concord-API/API-5/issues/293) | Send the API logs only to the file and OTLP, and read the warehouse metrics after the migration | Monitoramento | Backend | thiagosabreu | 1h | Done |
| [DVP-41](https://github.com/Concord-API/API-5/issues/297) | Exclude the migration scripts from the Sonar duplication check | CI | DevOps | victorgsnogueira | 1h | Done |
