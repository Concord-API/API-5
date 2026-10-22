# Definition of Done (DoD)

A story is done only when every item below has been verified at the level shown, by the
person shown.

| Level | What happens there |
| --- | --- |
| **Task PR** | PR from a task into `us0` or `usX`: formatting, lint, build, unit and integration tests and the Sonar analysis |
| **Acceptance** | push to `us0` or `usX`: the application is installed on Windows Server behind IIS, starts on an empty database, receives the sample load and answers search and theme detail through IIS |
| **`usX → main` PR** | code review, release label, the Sonar quality gate on the story's code and the story's QA checklist |
| **Push to `main`** | CI and the Sonar quality gate on the integrated code; the release is published only when everything is green |
| **Load** | generation of the load file, on our side |
| **Homologation** | demonstration of the increment to the PO |

### Code and tests

| Item | Where it is verified | Who verifies |
| --- | --- | --- |
| Code implemented and reviewed by another team member. | `usX → main` PR | Code Reviewers |
| Automated tests written and run (unit and integration), all green in the pipeline. | Task PR | task author |
| Critical behaviour covered by test: score calculation, aggregations and the provenance display rules. | Task PR (Sonar coverage) and `usX → main` PR (review) | task author and Code Reviewers |
| SonarQube Cloud quality gate (Sonar way) green on new code: reliability, security and maintainability rated A, coverage of at least 80%, duplication of at most 3% and every security hotspot reviewed. | `usX → main` PR and push to `main` | CI |

### Data and pipeline

| Item | Where it is verified | Who verifies |
| --- | --- | --- |
| The `dw` schema changes only through versioned migrations, applied by the API on startup; no DDL is run by hand in any environment. | Acceptance | CI |
| Idempotent load proven: the same load run twice duplicates no row and inflates no count. | Task PR | task author |
| The load runs on our side, by hand and independently of the API; homologation and production receive only the load file it produces, with the integrity tests empty. | Load | person running the load |
| The item's questions are answered by a pre-aggregated OLAP query, not by aggregating over the fact table at request time. | `usX → main` PR | Code Reviewers |

### Product

| Item | Where it is verified | Who verifies |
| --- | --- | --- |
| Every value displayed, analytical or descriptive, carries its source, extraction date, scope and how it was computed. | `usX → main` PR (QA checklist) | a team member who did not implement the story |
| The TJSP, TJRJ, TJMG, STJ and STF scope is visible on screen. | `usX → main` PR (QA checklist) | a team member who did not implement the story |
| Empty state handled: the screen states what does not exist and why, with no blank field and no invented plausible value. | `usX → main` PR (QA checklist) | a team member who did not implement the story |
| Minimum documentation updated (README, data dictionary, table grain). | `usX → main` PR | Code Reviewers |
| Increment demonstrable in the homologation environment, installed on Windows Server behind IIS the same way it will be on the client's server. | Acceptance (installation) and Homologation (demonstration) | CI and PO |

### Red build

If CI or Acceptance turns red on `us0`, a `usX` or `main`, whoever made the last merge
reverts that merge first and investigates afterwards. Nobody merges on top of a red
branch.

A red Sonar quality gate on the push to `main` turns the `main` CI red, and the release
of that merge is not published.
