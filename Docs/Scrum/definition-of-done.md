# Definition of Done (DoD)

### Code and tests

- Code implemented and reviewed by another team member.
- Automated tests written and run (unit and integration), all green in the pipeline.
- Critical behaviour covered by test: score calculation, aggregations and the provenance display rules.

### Data and pipeline

- Versioned migrations applied by the runner in the pipeline; no SQL run by hand in production.
- Idempotent load proven: the same load run twice duplicates no row and inflates no count.
- The ETL runs independently of the API, as a scheduled job in a low-usage window.
- The item's questions are answered by a pre-aggregated OLAP query, not by aggregating over the fact table at request time.

### Product

- Every value displayed, analytical or descriptive, carries its source, extraction date, scope and how it was computed.
- The TJSP, TJRJ and TJMG scope is visible on screen.
- Empty state handled: the screen states what does not exist and why, with no blank field and no invented plausible value.
- Minimum documentation updated (README, data dictionary, table grain).
- Increment demonstrable in the homologation environment, installed on Windows Server behind IIS the same way it will be on the client's server.