# Definition of Ready (DoR)

A single checklist for the team, applied to **every Product Backlog item before it enters a
Sprint**. It answers one question: *is this item ready to be built?*

A story only enters the Sprint when the items below are met.

1. **Business rules detailed** — what the item does, its limits, and what happens on the exception paths.
2. **Data to store defined** — fields, types, whether they are required, and validations; when the item touches the Data Warehouse, the **fact table grain is declared in writing**.
3. **Confirmation, error and warning messages defined** — the exact text of each one.
4. **Screen prototype** — an approved wireframe or navigable screen, when the item has an interface.
5. **Acceptance criteria written in BDD** — at least one scenario per relevant rule, including the exception path.
6. **Provenance declared** — for every number the item displays, where the source comes from is defined.
7. **Source verified**, when the item depends on a source that is not confirmed yet — the investigation happens in refinement and the answer is written down. Without it the item is not committed.