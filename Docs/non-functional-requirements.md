# Non-Functional Requirements

They apply to every story and are enforced in the
[Definition of Done](Scrum/definition-of-done.md).

## Data and pipeline

| # | Requirement |
| --- | --- |
| NFR-01 | Data is stored in a Data Warehouse with dimensional modelling (fact table, dimensions and a bridge table for N:N relationships), with the grain declared in writing. |
| NFR-02 | Every value displayed, analytical or descriptive, states its source and how it was computed (for every topic). |
| NFR-03 | Versioned migrations, applied by a runner in the pipeline. Never SQL by hand in production. |
| NFR-04 | There is a complete ETL pipeline, runnable independently of the other components. |
| NFR-05 | The load is idempotent: running it twice with the same data duplicates no row and inflates no count. |
| NFR-06 | The ETL runs as a scheduled job, outside the API's lifecycle, in a low-usage window. |
| NFR-07 | The product's questions are answered by pre-aggregated OLAP queries — summary per topic, per year, per court, per panel — refreshed at the end of each load, and not by aggregating over the fact table at request time. |
| NFR-08 | Full-text search is in Portuguese, inside Postgres, tolerating missing accents and typing errors. |
| NFR-09 | The application runs on the client's Windows Server, inside their intranet. No component depends on a cloud service to operate. |
| NFR-10 | The web layer is served behind **IIS**, the client's current standard, without depending on IIS-specific features — putting **NGINX** on the same server in its place must not require changing the application. |
| NFR-11 | PostgreSQL runs on the client's own server. No case data leaves their network. |
| NFR-12 | The application works with no internet access at runtime. The **ETL is the only component that needs outbound access**, through a configurable host allowlist or proxy; while that access is down, the product keeps serving the data already loaded and declares its extraction date. |
| NFR-15 | The capacity required is declared before installation: CPU, RAM and disk, including the growth from stored decision texts, so the client's IT can size the server. |
| NFR-16 | The application is operable without cloud tooling: structured logs on the server, a liveness probe and a readiness probe that reports the age of the last extraction, and an 1alarm that reaches a person when the ETL fails or does not run in its window. |
| NFR-17 | Access is restricted to the intranet — no exposure to the internet. |
| NFR-18 | Any external language-model provider is **optional and declared**. Disabling it does not break the rest of the application, and while it is enabled there is an audit log of every conversation, a defined retention policy and a usage and cost cap per question. |
| NFR-19 | No secret in the repository: connection strings, API keys and credentials come from environment configuration on the client's server. A missing required variable makes the application fail fast, naming the variable. |

## Language and compliance

| # | Requirement |
| --- | --- |
| NFR-20 | Identifiers in English, domain values in Portuguese. Text visible to the user is in Portuguese, including labels and error messages. |
| NFR-21 | LGPD and cases under seal: no personal data is indexed beyond what the official source exposes, a case under seal is flagged and never displayed, and where full decision texts are stored the terms of use of each court and the personal data inside those texts are checked and recorded. |

---
