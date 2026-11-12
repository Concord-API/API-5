# Sprint Backlog — Sprint 1

**Window:** Sep 7 to Sep 27, 2026

**Board:** [GitHub Project](https://github.com/orgs/Concord-API/projects/5) · snapshot of Nov 12, 2026

## Sprint goal

Stories the team commits to delivering. If any of them is not completed, the sprint did not meet its goal.

| ID | Priority | Description | SP | Tasks | Hours | Status |
| --- | --- | --- | ---: | ---: | ---: | --- |
| **US-01** | Must | As a **user**, I want to type my case's topic in natural language and get curated legal topics — not a list of cases — so that I can find out how it is being decided without digging through one ruling at a time | 8 | 13 | 49h | Done |
| **US-02** | Must | As a **user**, I want results ordered by how settled the understanding is, and not by text relevance, so that I find first what supports my thesis | 2 | 6 | 20h | Done |
| **US-09** | Must | As a **user**, I want to read the topic's understanding in prose, opening with the number that answers the question and with the case count next to every percentage, so that I understand the pattern without opening a table | 8 | 9 | 35h | Done |
| **US-21** | Must | As a **user**, I want to see the legal scholarship related to the topic, with author, work and a link to the article when there is one, so that I know what to cite beyond case law | 8 | 9 | 25h | Done |
| **US-24** | Must | As a **user**, I want every screen to make clear that the data covers TJSP, TJRJ and TJMG, so that I do not draw a nationwide conclusion from a percentage that reflects three states | 2 | 3 | 9h | Done |
| **US-25** | Must | As a **user**, I want to know the source and the extraction date of every number I am seeing, so that I know exactly what I am citing | 3 | 7 | 23h | Done |
| **US-26** | Must | As a **user**, I want the screen to tell me what does not exist and why, instead of showing an empty field or a plausible value, so that I do not build a filing on data that does not exist | 3 | 6 | 17h | Done |

## Outside the goal

Stories planned in the sprint that can move to the next one if there is not enough capacity, even though they are priorities.

| ID | Priority | Description | SP | Tasks | Hours | Status |
| --- | --- | --- | ---: | ---: | ---: | --- |
| **US-10** | Must | As a **user**, I want to see the distribution of outcomes for the topic in a figure with the source stated, so that I can see at a glance how much is upheld, partially upheld and dismissed | 5 | 6 | 21h | Done |

## Sprint summary

| | Total |
| --- | ---: |
| Stories (goal / outside the goal) | 7 / 1 |
| Story points (goal / total) | 34 / 39 |
| Tasks (done / total) | 79 / 79 |
| Hours (done / total) | 279h / 279h |
| Tasks in stories | 59 (199h) |
| Technical Foundation | 20 (80h) |
| Delivery and process | 0 (0h) |

### Hours by assignee

| Assignee | Tasks | Hours | Done |
| --- | ---: | ---: | ---: |
| victorgsnogueira | 44 | 157h | 157h |
| RichardCordeiro | 13 | 43h | 43h |
| thiagosabreu | 6 | 30h | 30h |
| JoaoBaranov | 8 | 28h | 28h |
| IsaacOliveiraSouza | 8 | 21h | 21h |

### Hours by layer

| Layer | Hours | Done |
| --- | ---: | ---: |
| Backend | 104h | 104h |
| Frontend | 85h | 85h |
| ETL | 53h | 53h |
| Test | 16h | 16h |
| DevOps | 11h | 11h |
| Docs | 10h | 10h |

## Stories and tasks

### US-01 — As a user, I want to type my case's topic in natural language and get curated legal topics — not a list of cases — so that I can find out how it is being decided without digging through one ruling at a time

_8 SP · Must · Done · 13/13 tasks · 49h_

Issue: [#14](https://github.com/Concord-API/API-5/issues/14)

| # | Task | Layer | Assignee | Est. | Status |
| --- | --- | --- | --- | ---: | --- |
| [1.1](https://github.com/Concord-API/API-5/issues/36) | Add the Portuguese text-search configuration with accent removal | Backend | victorgsnogueira | 3h | Done |
| [1.2](https://github.com/Concord-API/API-5/issues/37) | Add the generated search columns and their indexes to the theme dimension | Backend | IsaacOliveiraSouza | 3h | Done |
| [1.3](https://github.com/Concord-API/API-5/issues/38) | Create the theme search function combining text and trigram similarity | Backend | RichardCordeiro | 6h | Done |
| [1.4](https://github.com/Concord-API/API-5/issues/39) | Create the synonym table and expand the query with it | Backend | RichardCordeiro | 4h | Done |
| [1.5](https://github.com/Concord-API/API-5/issues/40) | Create `GET /api/themes` returning themes, never cases | Backend | thiagosabreu | 6h | Done |
| [1.6](https://github.com/Concord-API/API-5/issues/41) | Reject a query shorter than 3 characters with the Portuguese message | Backend | IsaacOliveiraSouza | 2h | Done |
| [1.7](https://github.com/Concord-API/API-5/issues/42) | Return the highest-volume themes when the query is empty | Backend | IsaacOliveiraSouza | 3h | Done |
| [1.8](https://github.com/Concord-API/API-5/issues/43) | Exclude themes without judged cases from the search | Backend | victorgsnogueira | 2h | Done |
| [1.9](https://github.com/Concord-API/API-5/issues/44) | Curate the synonym seed from real queries | ETL | victorgsnogueira | 3h | Done |
| [1.10](https://github.com/Concord-API/API-5/issues/45) | Build the home screen with the search field | Frontend | victorgsnogueira | 6h | Done |
| [1.11](https://github.com/Concord-API/API-5/issues/46) | Wire the results route to GET /api/themes | Frontend | RichardCordeiro | 5h | Done |
| [1.12](https://github.com/Concord-API/API-5/issues/47) | Reflect the search term in the URL | Frontend | RichardCordeiro | 3h | Done |
| [1.13](https://github.com/Concord-API/API-5/issues/48) | Show the count message and the empty message with the declared scope | Frontend | RichardCordeiro | 3h | Done |

### US-02 — As a user, I want results ordered by how settled the understanding is, and not by text relevance, so that I find first what supports my thesis

_2 SP · Must · Done · 6/6 tasks · 20h_

Issue: [#15](https://github.com/Concord-API/API-5/issues/15)

| # | Task | Layer | Assignee | Est. | Status |
| --- | --- | --- | --- | ---: | --- |
| [2.1](https://github.com/Concord-API/API-5/issues/49) | Create the strength aggregate with the four components | Backend | thiagosabreu | 6h | Done |
| [2.2](https://github.com/Concord-API/API-5/issues/50) | Test that the score is recomputed from zero and matches the exposed value | Test | JoaoBaranov | 4h | Done |
| [2.3](https://github.com/Concord-API/API-5/issues/51) | Order the theme list by strength score, descending | Backend | JoaoBaranov | 3h | Done |
| [2.4](https://github.com/Concord-API/API-5/issues/52) | Break ties by decision volume | Backend | victorgsnogueira | 2h | Done |
| [2.5](https://github.com/Concord-API/API-5/issues/53) | Return the judged count next to every score | Backend | IsaacOliveiraSouza | 2h | Done |
| [2.6](https://github.com/Concord-API/API-5/issues/54) | Show the ordering label and the volume next to the score | Frontend | RichardCordeiro | 3h | Done |

### US-09 — As a user, I want to read the topic's understanding in prose, opening with the number that answers the question and with the case count next to every percentage, so that I understand the pattern without opening a table

_8 SP · Must · Done · 9/9 tasks · 35h_

Issue: [#17](https://github.com/Concord-API/API-5/issues/17)

| # | Task | Layer | Assignee | Est. | Status |
| --- | --- | --- | --- | ---: | --- |
| [9.3](https://github.com/Concord-API/API-5/issues/57) | Add the theme narrative table with the text origin | Backend | JoaoBaranov | 3h | Done |
| [9.4](https://github.com/Concord-API/API-5/issues/58) | Generate the narrative from the aggregates in the load | ETL | victorgsnogueira | 6h | Done |
| [9.5](https://github.com/Concord-API/API-5/issues/59) | Write counts, not percentages, below the percentage floor | ETL | victorgsnogueira | 3h | Done |
| [9.6](https://github.com/Concord-API/API-5/issues/60) | Expose header, lead and body in GET /api/themes/{key} | Backend | JoaoBaranov | 5h | Done |
| [9.7](https://github.com/Concord-API/API-5/issues/61) | Return 404 with a Portuguese message for an unknown theme key | Backend | IsaacOliveiraSouza | 2h | Done |
| [9.8](https://github.com/Concord-API/API-5/issues/62) | Build the theme header with score, area tag and metadata line | Frontend | victorgsnogueira | 5h | Done |
| [9.9](https://github.com/Concord-API/API-5/issues/63) | Build the article column of the Resumo tab | Frontend | victorgsnogueira | 6h | Done |
| [9.10](https://github.com/Concord-API/API-5/issues/64) | Print the judged count next to every percentage in the text | Frontend | victorgsnogueira | 3h | Done |
| [9.11](https://github.com/Concord-API/API-5/issues/65) | Replace the unsourced blocks with an explanation of their absence | Frontend | victorgsnogueira | 2h | Done |

### US-21 — As a user, I want to see the legal scholarship related to the topic, with author, work and a link to the article when there is one, so that I know what to cite beyond case law

_8 SP · Must · Done · 9/9 tasks · 25h_

Issue: [#22](https://github.com/Concord-API/API-5/issues/22)

| # | Task | Layer | Assignee | Est. | Status |
| --- | --- | --- | --- | ---: | --- |
| [21.1](https://github.com/Concord-API/API-5/issues/73) | Harvest doctrine from DOAJ | ETL | victorgsnogueira | 2h | Done |
| [21.2](https://github.com/Concord-API/API-5/issues/74) | Harvest doctrine from SciELO | ETL | victorgsnogueira | 2h | Done |
| [21.3](https://github.com/Concord-API/API-5/issues/75) | Harvest doctrine from the OAI-PMH repositories | ETL | victorgsnogueira | 2h | Done |
| [21.4](https://github.com/Concord-API/API-5/issues/76) | Normalize and load the doctrine dimension idempotently | ETL | victorgsnogueira | 3h | Done |
| [21.5](https://github.com/Concord-API/API-5/issues/77) | Link doctrine to subjects by semantic similarity above the declared threshold | ETL | victorgsnogueira | 3h | Done |
| [21.6](https://github.com/Concord-API/API-5/issues/78) | Expose the related doctrine block | Backend | thiagosabreu | 5h | Done |
| [21.7](https://github.com/Concord-API/API-5/issues/79) | Return the unavailable reason when a theme has no doctrine above the threshold | Backend | JoaoBaranov | 2h | Done |
| [21.8](https://github.com/Concord-API/API-5/issues/80) | Render the doctrine table with author, work and article link | Frontend | RichardCordeiro | 5h | Done |
| [21.9](https://github.com/Concord-API/API-5/issues/81) | Declare on the block that the link is by similarity, with its threshold | Frontend | RichardCordeiro | 1h | Done |

### US-24 — As a user, I want every screen to make clear that the data covers TJSP, TJRJ and TJMG, so that I do not draw a nationwide conclusion from a percentage that reflects three states

_2 SP · Must · Done · 3/3 tasks · 9h_

Issue: [#24](https://github.com/Concord-API/API-5/issues/24)

| # | Task | Layer | Assignee | Est. | Status |
| --- | --- | --- | --- | ---: | --- |
| [24.1](https://github.com/Concord-API/API-5/issues/83) | Serve the declared scope from a single source | Backend | IsaacOliveiraSouza | 3h | Done |
| [24.2](https://github.com/Concord-API/API-5/issues/84) | Return the scope in every API response | Backend | IsaacOliveiraSouza | 3h | Done |
| [24.3](https://github.com/Concord-API/API-5/issues/85) | Show the scope on the results header and the detail footer, without interaction | Frontend | IsaacOliveiraSouza | 3h | Done |

### US-25 — As a user, I want to know the source and the extraction date of every number I am seeing, so that I know exactly what I am citing

_3 SP · Must · Done · 7/7 tasks · 23h_

Issue: [#25](https://github.com/Concord-API/API-5/issues/25)

| # | Task | Layer | Assignee | Est. | Status |
| --- | --- | --- | --- | ---: | --- |
| [25.1](https://github.com/Concord-API/API-5/issues/89) | Create the global provenance aggregate | Backend | victorgsnogueira | 3h | Done |
| [25.2](https://github.com/Concord-API/API-5/issues/90) | Create the per-theme provenance view | Backend | victorgsnogueira | 3h | Done |
| [25.3](https://github.com/Concord-API/API-5/issues/91) | Expose provenance in every response | Backend | victorgsnogueira | 4h | Done |
| [25.4](https://github.com/Concord-API/API-5/issues/92) | Omit a block that has no provenance | Backend | victorgsnogueira | 3h | Done |
| [25.5](https://github.com/Concord-API/API-5/issues/93) | Build the Provenance component | Frontend | victorgsnogueira | 3h | Done |
| [25.6](https://github.com/Concord-API/API-5/issues/94) | List every source that fed the page in the footer | Frontend | victorgsnogueira | 4h | Done |
| [25.7](https://github.com/Concord-API/API-5/issues/95) | Test that the extraction date comes from the data, not from the clock | Test | victorgsnogueira | 3h | Done |

### US-26 — As a user, I want the screen to tell me what does not exist and why, instead of showing an empty field or a plausible value, so that I do not build a filing on data that does not exist

_3 SP · Must · Done · 6/6 tasks · 17h_

Issue: [#26](https://github.com/Concord-API/API-5/issues/26)

| # | Task | Layer | Assignee | Est. | Status |
| --- | --- | --- | --- | ---: | --- |
| [26.1](https://github.com/Concord-API/API-5/issues/96) | Define the three unavailable reasons in the response contract | Backend | victorgsnogueira | 3h | Done |
| [26.2](https://github.com/Concord-API/API-5/issues/97) | Return the unavailable reason for each sourceless block | Backend | victorgsnogueira | 4h | Done |
| [26.3](https://github.com/Concord-API/API-5/issues/98) | Return an empty list, not an error, when there is nothing to list | Backend | victorgsnogueira | 2h | Done |
| [26.4](https://github.com/Concord-API/API-5/issues/99) | Build the EmptyState component reading the reason from the API | Frontend | victorgsnogueira | 4h | Done |
| [26.5](https://github.com/Concord-API/API-5/issues/100) | Test that no sourceless block renders a placeholder value | Test | victorgsnogueira | 3h | Done |
| [26.6](https://github.com/Concord-API/API-5/issues/101) | Link the unavailable explanation to the limitations page | Frontend | victorgsnogueira | 1h | Done |

### US-10 — As a user, I want to see the distribution of outcomes for the topic in a figure with the source stated, so that I can see at a glance how much is upheld, partially upheld and dismissed

_5 SP · Must · Done · 6/6 tasks · 21h_

Issue: [#18](https://github.com/Concord-API/API-5/issues/18)

| # | Task | Layer | Assignee | Est. | Status |
| --- | --- | --- | --- | ---: | --- |
| [10.2](https://github.com/Concord-API/API-5/issues/67) | Create the outcome distribution aggregate by theme and polarity | Backend | RichardCordeiro | 5h | Done |
| [10.3](https://github.com/Concord-API/API-5/issues/68) | Expose the outcome breakdown separated by category | Backend | thiagosabreu | 4h | Done |
| [10.4](https://github.com/Concord-API/API-5/issues/69) | Build the Figure component requiring the source prop | Frontend | thiagosabreu | 4h | Done |
| [10.5](https://github.com/Concord-API/API-5/issues/70) | Render FIG. 1 as horizontal bars with count and percentage | Frontend | thiagosabreu | 5h | Done |
| [10.6](https://github.com/Concord-API/API-5/issues/71) | Show counts only, with no percentage, below the percentage floor | Frontend | RichardCordeiro | 2h | Done |
| [10.7](https://github.com/Concord-API/API-5/issues/72) | Replace the amount figure with an explanation of the missing source | Frontend | JoaoBaranov | 1h | Done |

## Technical Foundation

Tasks with no parent story, numbered `0.Y`: what the sprint needs so the stories have somewhere to run (schema, data pipeline, load path, screen skeleton and fixes found along the way).

_20 tasks · 80h · 20 done_

| # | Task | Layer | Assignee | Est. | Status |
| --- | --- | --- | --- | ---: | --- |
| [0.12](https://github.com/Concord-API/API-5/issues/102) | Create the `dw` schema migration and apply it on API startup | Backend | victorgsnogueira | 8h | Done |
| [0.13](https://github.com/Concord-API/API-5/issues/133) | Create the pipeline repository that produces the load file | ETL | victorgsnogueira | 8h | Done |
| [0.14](https://github.com/Concord-API/API-5/issues/134) | Set up the frontend skeleton against the API contract | Frontend | victorgsnogueira | 16h | Done |
| [0.69](https://github.com/Concord-API/API-5/issues/136) | Sync the task board from branch and pull request events | DevOps | victorgsnogueira | 5h | Done |
| [0.70](https://github.com/Concord-API/API-5/issues/137) | Map verified movement codes to decision outcomes in the pipeline | ETL | victorgsnogueira | 3h | Done |
| [0.71](https://github.com/Concord-API/API-5/issues/138) | Add the pipeline command that harvests and builds the load file | ETL | victorgsnogueira | 6h | Done |
| [0.72](https://github.com/Concord-API/API-5/issues/139) | Seed the strength configuration in the load file | ETL | victorgsnogueira | 2h | Done |
| [0.73](https://github.com/Concord-API/API-5/issues/140) | Refresh the materialized views in dependency order in the load file | ETL | victorgsnogueira | 2h | Done |
| [0.74](https://github.com/Concord-API/API-5/issues/142) | Draw the conceptual entity-relationship model (MER) of the dw schema | Docs | JoaoBaranov | 5h | Done |
| [0.75](https://github.com/Concord-API/API-5/issues/143) | Draw the physical entity-relationship diagram (DER) of the dw schema | Docs | JoaoBaranov | 5h | Done |
| [0.76](https://github.com/Concord-API/API-5/issues/144) | Generate the calendar dimension in the load | ETL | victorgsnogueira | 1h | Done |
| [0.77](https://github.com/Concord-API/API-5/issues/145) | Harvest only cases with a verified decision movement | ETL | victorgsnogueira | 2h | Done |
| [0.78](https://github.com/Concord-API/API-5/issues/146) | Check the warehouse integrity before writing the load file | Test | victorgsnogueira | 3h | Done |
| [0.79](https://github.com/Concord-API/API-5/issues/147) | Build the pipeline test schema from the backend migrations | Test | victorgsnogueira | 3h | Done |
| [0.80](https://github.com/Concord-API/API-5/issues/148) | Propose subject clusters for curation with local embeddings | ETL | victorgsnogueira | 3h | Done |
| [0.81](https://github.com/Concord-API/API-5/issues/154) | Map the special court and appeal panel levels from DataJud | ETL | victorgsnogueira | 1h | Done |
| [0.82](https://github.com/Concord-API/API-5/issues/155) | Read the pipeline settings from a .env file | ETL | victorgsnogueira | 1h | Done |
| [0.83](https://github.com/Concord-API/API-5/issues/157) | Analyze the backend quality and coverage with SonarQube Cloud | DevOps | RichardCordeiro | 2h | Done |
| [0.84](https://github.com/Concord-API/API-5/issues/158) | Analyze the frontend quality and coverage with SonarQube Cloud | DevOps | RichardCordeiro | 2h | Done |
| [0.85](https://github.com/Concord-API/API-5/issues/159) | Analyze the pipeline quality and coverage with SonarQube Cloud | DevOps | RichardCordeiro | 2h | Done |
