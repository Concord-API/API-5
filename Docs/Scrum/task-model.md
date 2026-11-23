# Task model

How the team's work is recorded on the **API V Tasks** board: what a user story is, what a task
is, where work that belongs to no story goes, and how each item is written. The criterion for a
story to enter the Sprint is in the [DoR](definition-of-ready.md), and the criterion for it to
leave, in the [DoD](definition-of-done.md).

## Hierarchy

Every item on the board is in one of these two places:

- **A user story** (`US-XX`), with its tasks as sub-issues. The tasks are the real work: they hold
  the assignee and the hours.
- **A container**, when the work belongs to no story. There are two:
  [Technical Foundation](#technical-foundation) and [DevOps](#devops).

The ID of each item is unique across the whole project and is never renumbered, because it goes
into the branch name (see [Branches](../../README.md#branches)).

## Containers

### Technical Foundation

The technical base of the product that is not a user story: the Data Warehouse schema, the
pipeline, the frontend skeleton, reference data and source investigations.

| | |
| --- | --- |
| Task ID | `0.Y` — the `0` takes the place of the story number (`0.12`, `0.113`) |
| Base branch | `us0` |
| Examples | `0.12 Create the dw schema migration and apply it on API startup`, `0.112 Spike: find a lawful source of court rulings with summary for the courts in scope` |

### DevOps

Everything that takes the product from the code to the server and keeps it running: continuous
integration, deploy, quality, monitoring, tests, database, and the documentation of all of it.

| | |
| --- | --- |
| Task ID | `DVP-NN`, sequential (`DVP-01`, `DVP-02`…) |
| Base branch | `us0`, the same as the Technical Foundation |
| Front | the board's `Frente` field: `CI`, `Deploy`, `QA`, `Monitoramento`, `Testes`, `BD` or `Docs` |
| Example | `DVP-75 Cache the search filter options until the next load` |

DevOps has no base branch of its own. A DevOps task that produces commits gets its own task branch,
created from `us0` and merged back into it, like the `0.Y` tasks. A base branch just for DevOps
would have nothing to integrate, because each DevOps task stands on its own.

A DevOps task with no branch is also normal, for example a setting changed outside GitHub: it
exists to record the work and the hours, and its card is moved by hand.

## User story

- **Title:** `US-XX — ` followed by the full text of the story in English, not shortened, the same
  as in the sprint backlog.
- **Type:** `User Story`.
- **Fields:** `Priority`, `Effort (SP)` and `Sprint`. The body stays empty.
- **No assignee and no layer label.** The tasks are what get the story done, and more than one
  person can work on the tasks of the same story.

## Task

### ID and title

- **ID:** `X.Y`, where `X` is the story number (the tasks of US-01 are `1.1`, `1.2`…). In the
  containers, `0.Y` or `DVP-NN`.
- **Title:** short, imperative and **in English**, with no layer tag (the layer is the label).
  Example: `39.9 Explain in the case view what does not exist and why`.

### Description

Only when the title is not enough. As separate lines, never a paragraph, each one starting with
one of these labels:

| Label | What it says |
| --- | --- |
| `Data:` | the field, rule or data the task deals with |
| `Message:` | the exact text shown to the user |
| `Verifies:` | what the test or the criterion proves when the task is done |
| `Depends:` | the tasks or decisions it depends on |

The text of the lines can be in Portuguese or in English. Only the title has a strict pattern.

Example:

```
39.9 Explain in the case view what does not exist and why

Data: caso ou tribunal sem dado carregado diz o que falta e por quê (US-26): sem campo vazio, sem enchimento, sem link
Message: TJRJ e TJMG: "Os dados deste processo não estão disponíveis no Ratio: a consulta pública do {tribunal} só pode ser feita com captcha."
Depends: 39.6
```

### Hours

- Every task has hours in the `Horas` field, and **always under 8h**.
- A task over 8h is split into two or more.

### Documentation

The documentation of a task is **a task of its own**, with the `Docs` label, the same front and the
same assignee, and `Depends:` pointing to the task it documents. This keeps the writing hours out
of the technical task.

### Fields

| Field | Value |
| --- | --- |
| Type | `Task` |
| Assignee | whoever does the task |
| Label | the layer of the work: `Backend`, `Frontend`, `ETL`, `Test`, `DevOps` or `Docs` |
| `Sprint` | the Sprint in which the task is done |
| `Horas` | the estimate, under 8h |
| `Status` | `Todo` → `In Progress` → `Review` → `Done` |
| `Frente` | DevOps tasks only |

`Priority` and `Effort (SP)` belong to the user story only.

Every new task is born on the board with `Status` set to `Todo`. An issue created outside the
board and only later added to it has no status and shows up in no column.

## Golden rule

Every task answers, even if implicitly: ***what has to be true once it is done?*** Whoever reads it
must be able to judge whether it is done without going back to the DoR.
