# Ratio 
> (Latin: reason, ground). From ratio decidendi — the determining ground of a judicial
> decision, what actually repeats and becomes a pattern.

![home](Assets/home.jpeg)

## Contents
- [Introduction](#introduction)
- [Key Features](#key-features)
- [Team](#team)
- [How to contribute](#how-to-contribute)
  - [Branches](#branches)
  - [Commits](#commits)

## Introduction
Ratio sets out to eliminate the manual, fragmented work of case law analysis that keeps lawyers and judges from reliably identifying where the courts stand on a given thesis — letting them quickly assess its acceptance, recurrence and degree of consolidation to ground legal decisions and strategies. It does so by centralising and analysing case law, precedents and legal scholarship from TJSP, TJRJ and TJMG in a legal Data Warehouse, with semantic search by topic and the generation of indicators and decision patterns traceable back to their original sources.
 
## Key Features
- **Topic search in natural language** — the user describes the case in their own words and gets the legal topic already identified, without having to build search syntax or know the technical name of the thesis.
- **Consolidated decision pattern** — acceptance rate, case volume and courts involved, computed automatically. Removes the manual tabulation of decisions in a spreadsheet.
- **Strength score for the understanding** — shows how settled (or how unstable) that pattern is, weighing agreement between decisions, volume, coverage and recency.
- **Traceability** — every number displayed leads back to its source and extraction date; no metric is invented or computed in the dark.
- **Multi-court coverage** — centralised data from TJSP, TJRJ and TJMG, the three courts with the highest case volume in the country.
- **Access to related precedents and scholarship** — to keep everything traceable, all the precedents and scholarly works used to summarise a topic remain reachable.

# Product Backlog
| ID | Priority | Description | Estimate | Sprint |
| --- | --- | --- | --- | --- |
| **US-01** | Must | As a **user**, I want to type my case's topic in natural language and get curated legal topics — not a list of cases — so that I can find out how it is being decided without digging through one ruling at a time | 8 | Sprint 1 |
| **US-02** | Must | As a **user**, I want results ordered by how settled the understanding is, and not by text relevance, so that I find first what supports my thesis | 2 | Sprint 1 |
| **US-04** | Must | As a **user**, I want to filter results by court, period, instance and minimum strength, seeing how many cases each court has, so that I can narrow the list down to my case | 5 | Sprint 1 |
| **US-09** | Must | As a **user**, I want to read the topic's understanding in prose, opening with the number that answers the question and with the case count next to every percentage, so that I understand the pattern without opening a table | 8 | Sprint 1 |
| **US-10** | Must | As a **user**, I want to see the distribution of outcomes for the topic in a figure with the source stated, so that I can see at a glance how much is upheld, partially upheld and dismissed | 5 | Sprint 1 |
| **US-18** | Could | As a **user**, I want to see the qualified precedents linked to the topic — súmula, repetitive theme, IRDR — distinguishing what is legally binding from what is merely persuasive, so that I know what binds me | 8 | Sprint 1 |
| **US-21** | Must | As a **user**, I want to see the legal scholarship invoked, with author, work and its position in the debate, with a link to the article when there is one, so that I know what to cite beyond case law | 8 | Sprint 1 |
| **US-23** | Could | As a **user**, I want to read the full text of the cited decision on the application, so that I can check the context before using it | 5 | Sprint 1 |
| **US-24** | Must | As a **user**, I want every screen to make clear that the data covers TJSP, TJRJ and TJMG, so that I do not draw a nationwide conclusion from a percentage that reflects three states | 2 | Sprint 1 |
| **US-25** | Must | As a **user**, I want to know the source and the extraction date of every number I am seeing, so that I know exactly what I am citing | 3 | Sprint 1 |
| **US-26** | Must | As a **user**, I want the screen to tell me what does not exist and why, instead of showing an empty field or a plausible value, so that I do not build a filing on data that does not exist | 3 | Sprint 1 |
| **US-03** | Must | As a **user**, I want to see in each result the score, the area of law, the thesis title, a short summary, the courts, the volume, the period, the last decision and the favourable percentage, so that I can compare theses before opening any of them | 8 | Sprint 2 |
| **US-38** | Could | As a **user**, I want suggested frequent queries on the home screen, so that I understand what kind of question the tool answers before typing my own | 2 | Sprint 2 |
| **US-06** | Must | As a **user**, I want a 0-to-100 score telling me how settled the understanding on the topic is, so that I know whether the thesis is worth arguing or is an open fight | 8 | Sprint 2 |
| **US-07** | Must | As a **user**, I want the score to come with a grade in language that already exists in the legal field — Consolidada, Dominante, Em formação, Divergente — so that I do not have to interpret an invented scale | 2 | Sprint 2 |
| **US-08** | Must | As a **user**, I want to open the score's composition — the four components, their weights and the basis of calculation — so that I can cite the statistic knowing exactly where it comes from | 3 | Sprint 2 |
| **US-11** | Must | As a **user**, I want to see how the topic's alignment evolved year by year, with the trend sentence, so that I know whether the understanding is settling or shifting | 5 | Sprint 2 |
| **US-12** | Must | As a **user**, I want to see the topic's alignment by court, so that I know whether the thesis holds the same in São Paulo, Rio de Janeiro and Minas Gerais | 3 | Sprint 2 |
| **US-14** | Must | As a **user**, I want a table of each court's behaviour — decisions, alignment and date of the latest one — so that I can compare my court with the others | 3 | Sprint 2 |
| **US-15** | Must | As a **user**, I want an auditable sample of the cases behind the topic, with panel, date and outcome, so that I can check the cases before citing them | 5 | Sprint 2 |
| **US-17** | Should | As a **user**, I want to know whether the panels of my court are deciding alike, so that I can spot internal divergence before deciding | 5 | Sprint 2 |
| **US-19** | Could | As a **user**, I want to see the grounds invoked in the topic's decisions, with the frequency and the acceptance rate of each one, so that I can pick the argument that wins most and avoid the one that always loses | 8 | Sprint 2 |
| **US-22** | Could | As a **user**, I want the reporting judge's name in the sample and in the citation reference, so that I can assemble the complete citation | 5 | Sprint 2 |
| **US-37** | Could | As a **user**, I want to see in the understanding text the ruling that supports each statement, with the full reference and the list of cited decisions at the foot, so that I can cite the same decision | 8 | Sprint 2 |
| **US-27** | Should | As a **user**, I want to export to CSV the decisions that support the topic, so that I can work the data outside the tool | 5 | Sprint 3 |
| **US-28** | Should | As a **user**, I want to copy the topic's citation already with the source, the extraction date, the scope and the `n`, so that I can paste it without retyping | 3 | Sprint 3 |
| **US-29** | Should | As a **user**, I want to know when the data was last updated, and to be warned when it is stale, so that I do not rely on a months-old snapshot | 3 | Sprint 3 |
| **US-30** | Could | As a **user**, I want to know how long it usually takes from filing to decision on this topic, so that I can calibrate my client's expectation | 8 | Sprint 3 |
| **US-34** | Should | As a **user**, I want to ask a chatbot about a topic in natural language and get the answer in prose with the numbers, for the questions that no screen filter answers | 13 | Sprint 3 |
| **US-35** | Should | As a **user**, I want every chatbot answer to bring the `n`, the source, the extraction date, the scope and the link to the cases, so that I can check it before using it | 5 | Sprint 3 |
| **US-36** | Should | As a **user**, I want the chatbot to say it does not know when the data is not in the base, so that I do not get a plausible, invented number | 3 | Sprint 3 |

## Sprint distribution

| Sprint | Window | Stories | Points |
| --- | --- | --- | --- |
| **Sprint 1** | 07/09 – 27/09 | 13 | 62 |
| **Sprint 2** | 05/10 – 25/10 | 13 | 65 |
| **Sprint 3** | 02/11 – 22/11 | 7 | 40 |

## MoSCoW

| Priority | Meaning |
| --- | --- |
| **Must** | Required for the delivery. Without it the product does not meet its main objective and is not assessable. Prioritised ahead of everything else. |
| **Should** | Important for a complete delivery. The product still works without it, but its absence is a real loss of quality, usability or coverage. Enters if there is capacity left after the Musts. |
| **Could** | Desirable improvement. Adds value but does not compromise the delivery if left out. First group to be cut when time or capacity gets tight. |
| **Won't** | Out of this delivery. Analysed and deliberately not built in this cycle — recorded in [Out of scope](#out-of-scope) so it does not come back as a surprise. |

## Estimation scale

| SP | Meaning | Layers | Uncertainty |
| --- | --- | --- | --- |
| **1** | isolated tweak: one text, one bit of formatting | 1 | none |
| **2** | the last piece of something another story already delivered | 1 | none |
| **3** | self-contained work in one layer: a block, a table, a component | 1 | none |
| **5** | two layers, or a rule someone has to define | 2 | some |
| **8** | goes from the database to the screen, or the team has never done it | 3+ | real |
| **13** | large **and** uncertain — top of the scale, a candidate for splitting in refinement | all | high |

## Team
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
        <td align="center">Developer</td>
        <td align="center"><a href="https://github.com/JoaoBaranov"><img src="https://cdn.simpleicons.org/github/181717" alt="GitHub" width="22" /></a></td>
      </tr>
      <tr>
        <td align="center">Victor Nogueira</td>
        <td align="center">Developer</td>
        <td align="center"><a href="https://github.com/victorgsnogueira"><img src="https://cdn.simpleicons.org/github/181717" alt="GitHub" width="22" /></a></td>
      </tr>
      <tr>
        <td align="center">Richard Cordeiro</td>
        <td align="center">Developer</td>
        <td align="center"><a href="https://github.com/RichardCordeiro"><img src="https://cdn.simpleicons.org/github/181717" alt="GitHub" width="22" /></a></td>
      </tr>
      <tr>
        <td align="center">Isaac Oliveira</td>
        <td align="center">Developer</td>
        <td align="center"><a href="https://github.com/IsaacOliveiraSouza"><img src="https://cdn.simpleicons.org/github/181717" alt="GitHub" width="22" /></a></td>
      </tr>
      <tr>
        <td align="center">Thiago Abreu</td>
        <td align="center">Developer</td>
        <td align="center"><a href="https://github.com/thiagosabreu"><img src="https://cdn.simpleicons.org/github/181717" alt="GitHub" width="22" /></a></td>
      </tr>
    </tbody>
  </table>
</div>

## How to contribute
### Branches
- **Feature branching + one branch per sprint**
- **main:** the project's main, stable branch. It only receives merges at the end of each sprint, after review and approval.
- **sprintX** (e.g. sprint1, sprint2, sprint3): each sprint has its own base branch, where every feature built during that cycle is integrated.
- **parenttask-subtask-task-name-with-dashes-if-it-has-spaces:** for every new feature or fix, a dedicated branch is created off the current sprint branch. The branch is named after the task on the board. Example: `RATIO-35-0.1-Implement-API-documentation`
- **Documentation repository:** since the branches in this repository are not tied to tasks, they follow a different pattern. They carry the application name, the word "**DOCS**" and a description of what is being done — for example, `RATIO-DOCS-Definition-of-Done`, `RATIO-DOCS-Product-Backlog`
### Commits
**Every commit to any repository in this project must be written in English.**  
Each commit should be small, descriptive and to the point, following the semantic convention:
 
- `feat:` description of the new feature
- `fix:` bug fix or unexpected behaviour
- `refactor:` code improvement with no change in behaviour
- `docs:` documentation update
- `chore:` configuration, build or maintenance work
Example: `feat: add semantic search by legal topic`
 
The number of commits is used as an indicator of individual contribution and sprint progress, making the flow of work in the repository traceable.
