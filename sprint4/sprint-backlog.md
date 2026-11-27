# Sprint Backlog — Sprint 4

**Window:** Nov 23 to Dec 11, 2026

**Board:** [GitHub Project](https://github.com/orgs/Concord-API/projects/5) · snapshot of Nov 27, 2026

**Definitions:** [Definition of Ready](../Docs/Scrum/definition-of-ready.md) · [Definition of Done](../Docs/Scrum/definition-of-done.md)

## Sprint goal

> **The user sees which topics have shifted in the last two years and how the topic's cases were decided before and after the STJ's thesis; Ratio runs on the client's server with the monitoring installed, the path from the search to the topic is validated end to end before and after the fair on Dec 3, and each DevOps front has its documentation in API-5.**

Stories the team commits to delivering. If any of them is not completed, the sprint did not meet its goal.

| ID | Priority | Description | SP | Tasks | Hours | Status |
| --- | --- | --- | ---: | ---: | ---: | --- |
| **US-42** | Should | As a **user**, I want to see which topics have shifted in the last two years, with the rate and the case count of each period, so that I know which understandings are turning before I rely on older decisions | 8 | 7 | 18h | To do |
| **US-43** | Should | As a **user**, I want to see on the topic's yearly chart the date the STJ judged the related repetitive theme, and how the topic's cases were decided before and after it, so that I know whether the courts changed course after the binding thesis | 8 | 7 | 16h | To do |

## Sprint summary

| | Total |
| --- | ---: |
| Stories (goal / outside the goal) | 2 / 0 |
| Story points (goal / total) | 16 / 16 |
| Tasks (done / total) | 1 / 25 |
| Hours (done / total) | 6h / 66h |
| Tasks in stories | 14 (34h) |
| Delivery and process | 11 (32h) |

### Hours by assignee

| Assignee | Tasks | Hours | Done |
| --- | ---: | ---: | ---: |
| unassigned | 14 | 34h | 0h |
| joaoandrade17 | 7 | 9h | 0h |
| RichardCordeiro | 2 | 7h | 6h |
| vp-p | 2 | 6h | 0h |
| IsaacOliveiraSouza | 2 | 5h | 0h |
| victorgsnogueira | 2 | 3h | 0h |
| JoaoBaranov | 1 | 1h | 0h |
| thiagosabreu | 1 | 1h | 0h |

_Hours of a task with more than one assignee are split evenly between them._

### Hours by layer

| Layer | Hours | Done |
| --- | ---: | ---: |
| Backend | 17h | 0h |
| Docs | 17h | 0h |
| DevOps | 12h | 6h |
| Frontend | 11h | 0h |
| Test | 9h | 0h |

## Burndown

![Sprint 4 burndown](burndown.png)

Remaining hours per day, from the board's `Status` field and each task's hours. Status on Nov 27, 2026.

## Stories and tasks

### US-42 — As a user, I want to see which topics have shifted in the last two years, with the rate and the case count of each period, so that I know which understandings are turning before I rely on older decisions

_8 SP · Should · To do · 0/7 tasks · 18h_

Issue: [#426](https://github.com/Concord-API/API-5/issues/426)

| # | Task | Layer | Assignee | Est. | Status |
| --- | --- | --- | --- | ---: | --- |
| [42.1](https://github.com/Concord-API/API-5/issues/427) | Compute each topic's upheld rate in the earlier and the recent window | Backend | — | 4h | To do |
| [42.2](https://github.com/Concord-API/API-5/issues/428) | Keep only the shifts that pass the two-proportion test | Backend | — | 2h | To do |
| [42.3](https://github.com/Concord-API/API-5/issues/429) | Expose the shifting topics with both rates, n, direction, source and extraction date | Backend | — | 3h | To do |
| [42.4](https://github.com/Concord-API/API-5/issues/430) | Build the shifting topics block on the home page | Frontend | — | 4h | To do |
| [42.5](https://github.com/Concord-API/API-5/issues/431) | Show the shift in the result item and in the theme header | Frontend | — | 2h | To do |
| [42.6](https://github.com/Concord-API/API-5/issues/432) | Test that a shift under the n floor or not significant never shows | Test | — | 2h | To do |
| [42.7](https://github.com/Concord-API/API-5/issues/433) | Document the shift rule in the dimensional model docs | Docs | — | 1h | To do |

### US-43 — As a user, I want to see on the topic's yearly chart the date the STJ judged the related repetitive theme, and how the topic's cases were decided before and after it, so that I know whether the courts changed course after the binding thesis

_8 SP · Should · To do · 0/7 tasks · 16h_

Issue: [#434](https://github.com/Concord-API/API-5/issues/434)

| # | Task | Layer | Assignee | Est. | Status |
| --- | --- | --- | --- | ---: | --- |
| [43.1](https://github.com/Concord-API/API-5/issues/435) | Pick the related repetitive theme of each topic by the highest declared similarity | Backend | — | 2h | To do |
| [43.2](https://github.com/Concord-API/API-5/issues/436) | Compute the topic's upheld rate before and after the precedent's judgment date | Backend | — | 4h | To do |
| [43.3](https://github.com/Concord-API/API-5/issues/437) | Expose the before and after with the precedent, its date, both n, source and link method | Backend | — | 2h | To do |
| [43.4](https://github.com/Concord-API/API-5/issues/438) | Mark the precedent's judgment date on the yearly chart | Frontend | — | 3h | To do |
| [43.5](https://github.com/Concord-API/API-5/issues/439) | Write the before and after sentence below the chart | Frontend | — | 2h | To do |
| [43.6](https://github.com/Concord-API/API-5/issues/440) | Test the topic without enough cases on either side of the date | Test | — | 2h | To do |
| [43.7](https://github.com/Concord-API/API-5/issues/441) | Document the before and after rule in the dimensional model docs | Docs | — | 1h | To do |

## Delivery and process

Tasks `DVP-xx` (CI, deploy, QA, monitoring, database tests and documentation), also with no parent story.

_11 tasks · 32h · 1 done_

| # | Task | Front | Layer | Assignee | Est. | Status |
| --- | --- | --- | --- | --- | ---: | --- |
| [DVP-14](https://github.com/Concord-API/API-5/issues/183) | Add the end-to-end smoke test from search to theme detail | Testes | Test | vp-p | 5h | To do |
| [DVP-65](https://github.com/Concord-API/API-5/issues/376) | Document the database process in the API-5 repository | Docs | Docs | joaoandrade17, JoaoBaranov | 2h | To do |
| [DVP-68](https://github.com/Concord-API/API-5/issues/380) | Install the monitoring on the server after the first deploy | Deploy | DevOps | IsaacOliveiraSouza | 4h | To do |
| [DVP-79](https://github.com/Concord-API/API-5/issues/409) | Document the CI process in the API-5 repository | Docs | Docs | victorgsnogueira, joaoandrade17 | 2h | To do |
| [DVP-80](https://github.com/Concord-API/API-5/issues/410) | Document the deploy process in the API-5 repository | Docs | Docs | IsaacOliveiraSouza, joaoandrade17 | 2h | To do |
| [DVP-81](https://github.com/Concord-API/API-5/issues/411) | Document the QA process in the API-5 repository | Docs | Docs | RichardCordeiro, joaoandrade17 | 2h | To do |
| [DVP-82](https://github.com/Concord-API/API-5/issues/412) | Document the monitoring process in the API-5 repository | Docs | Docs | thiagosabreu, joaoandrade17 | 2h | To do |
| [DVP-83](https://github.com/Concord-API/API-5/issues/413) | Document the test process in the API-5 repository | Docs | Docs | joaoandrade17, vp-p | 2h | To do |
| [DVP-84](https://github.com/Concord-API/API-5/issues/414) | Define the documentation standard and the folder structure of the API-5 repository | Docs | Docs | joaoandrade17 | 3h | To do |
| [DVP-85](https://github.com/Concord-API/API-5/issues/419) | Report the stalled work every weekday in an API-5 issue | QA | DevOps | RichardCordeiro | 6h | Done |
| [DVP-86](https://github.com/Concord-API/API-5/issues/442) | Refresh the pipeline schema fixture and publish the load at the new schema version | BD | DevOps | victorgsnogueira | 2h | To do |
