# Definition of Done (DoD)

### Code and tests

- Code implemented and reviewed by another team member.
- Automated tests written and run (unit and integration), all green in the pipeline.
- Critical behaviour covered by test: score calculation, aggregations and the provenance display rules.

### Data and pipeline

- The `dw` schema changes only through versioned migrations, applied by the API on startup; no DDL is run by hand in any environment.
- Idempotent load proven: the same load run twice duplicates no row and inflates no count.
- The load runs on our side, by hand and independently of the API; homologation and production receive only the load file it produces, with the integrity tests empty.
- The item's questions are answered by a pre-aggregated OLAP query, not by aggregating over the fact table at request time.

### Product

- Every value displayed, analytical or descriptive, carries its source, extraction date, scope and how it was computed.
- The TJSP, TJRJ, TJMG, STJ and STF scope is visible on screen.
- Empty state handled: the screen states what does not exist and why, with no blank field and no invented plausible value.
- Minimum documentation updated (README, data dictionary, table grain).
- Increment demonstrable in the homologation environment, installed on Windows Server behind IIS the same way it will be on the client's server.