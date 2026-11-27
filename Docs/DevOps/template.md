# <Front name>

<!-- Template of the doc of a DevOps front. Copy this file to <front>/README.md and follow the
writing rules in this folder's README. The comments do not show on GitHub and may stay.

One or two sentences: what this front does in Ratio and what it guarantees. -->

See the portuguese(br) version [here](<link to the Portuguese version>).

| | |
| --- | --- |
| Built by | GitHub login of whoever built it |
| Repositories | where what the front uses lives |
| Tasks | DVP-xx, DVP-yy (with links) |
| Updated on | MMM D, YYYY |

## Overview

<!-- The front's role on the way from the code to the client's server: which fronts it talks to,
what it depends on and what breaks if it stops. If the path has more than three steps, a mermaid
diagram. -->

## What exists

<!-- Everything the front created or configures, and where it is. One item per line.
Secrets and variables: only the name and where it is configured, never the value. -->

| Item | Where it is | What it is for |
| --- | --- | --- |
| `ci.yml` | [`API5-Backend/.github/workflows/ci.yml`](link) | ... |

## How it works

<!-- What triggers it, the order of the steps, what goes in, what comes out and what the result
is. -->

## Decisions

<!-- One subsection per decision: tool, approach, rule or accepted exception. -->

### <The decision in one sentence>

- **Context:** the problem or constraint that led to the decision
- **Alternatives:** what else was considered
- **Why:** the reason for the choice
- **Consequences:** what becomes easier and what becomes harder

## How to

<!-- The tasks whoever carries on will need to do. One subsection per task. More than 10 steps:
it becomes its own file in this folder and only the link stays here. -->

### <Task in the imperative>

**When:** in which situation

**Before you start:** access, tools and versions

1. The step, with the exact command:
   ```
   command
   ```
   Expected output: ...

**How to check:** what shows it worked

**How to undo:** what to do if it goes wrong

## How to tell it is working

<!-- The checks, commands, dashboards or signals that prove the front is healthy. -->

## Known issues

| Symptom | Cause | What to do |
| --- | --- | --- |

## Carrying on

<!-- What was left halfway, the accepted limitations, the suggested improvements and the access
whoever takes over needs to have. -->

## References

<!-- Tasks and PRs that built the front, official documentation of the tools with the version
used, and the docs of the other fronts. -->
