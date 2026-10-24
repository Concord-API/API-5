# ETL Documentation

How Ratio turns court decisions and legal scholarship into the `dw` schema that the API reads. This document describes the `API5-Pipeline` repository as it stands on 23 Oct 2026; the code is the source of truth, and the decision identifiers (D-xx) refer to the project docs wiki (`06-operacao/02-decisoes-e-riscos.md`).

## Contents

1. [Objective](#1-objective)
2. [Data sources (Extract)](#2-data-sources-extract)
3. [Transformations (Transform)](#3-transformations-transform)
4. [Data load (Load)](#4-data-load-load)
5. [Tools and technologies](#5-tools-and-technologies)
6. [ETL flow diagram](#6-etl-flow-diagram)
7. [Scheduling and automation](#7-scheduling-and-automation)
8. [Problems found and decisions made](#8-problems-found-and-decisions-made)

## 1. Objective

The ETL collects civil-law decisions from DataJud and legal-scholarship articles from open journal sources, normalises them into a dimensional model, and generates a SQL load file that populates the `dw` schema. The API reads only `dw`, to serve topic search, the strength score and the traceability of every number.

The pipeline runs on our side, never on the client's server. The `dw` schema is created by the API through migrations (DbUp); the pipeline creates only `raw`, `staging` and `etl` in the load database, and delivers data that is already validated and tied to the schema version it was generated for.

Courts collected today: TJSP, TJRJ, TJMG and STJ, civil matters only. STF is in the project scope (October 2026 decision) but the pipeline has no collector for it yet, see [section 8](#8-problems-found-and-decisions-made).

## 2. Data sources (Extract)

| Source | Access | Command | What is collected |
| --- | --- | --- | --- |
| DataJud (CNJ) | Elasticsearch `_search` endpoint, one index per court: `https://api-publica.datajud.cnj.jus.br/api_publica_{court}/_search`, header `Authorization: APIKey <key>` | `python -m pipeline` | Civil cases of `tjsp`, `tjrj`, `tjmg` and `stj`, with all their movements |
| DOAJ | REST, `https://doaj.org/api/search/articles`, no authentication | `python -m pipeline.harvest_doaj [--term T] [--year Y]` | Articles for the 25 search terms in `pipeline/data/doaj_terms.json` |
| SciELO | ArticleMeta API, `https://articlemeta.scielo.org/api/v1/article/`, no authentication | `python -m pipeline.harvest_scielo [--issn I]` | Articles from the 6 ISSNs in `pipeline/data/scielo_issns.json` |
| OAI-PMH | Dublin Core (`oai_dc`) endpoints, no authentication | `python -m pipeline.harvest_oai [--repository R]` | Articles from the 48 journal endpoints in `pipeline/data/oai_sources.json` (47 enabled; one is disabled because its endpoint requires access) |
| STF | Corte Aberta decisions panel (CSV), outside DataJud | not implemented | See section 8 |

DataJud is the only source of decisions; the other three feed the doctrine dimension. Doctrine collectors are separate commands and are not run by `python -m pipeline`; the main command only transforms whatever is already in `raw.doctrine_article`.

### How DataJud is queried

The collection is a deliberate cut, never "everything". The query sent to each court filters at the source:

| Filter | Value |
| --- | --- |
| Case class | `classe.codigo` in the civil classes of the TPU (`pipeline/data/tpu.json`). For STJ, the appeal classes `1032`, `11881`, `1137` and `11956` |
| Subject | `assuntos.codigo` in the codes of one TPU area |
| Decision | `movimentos.codigo` in the 6 verified decision codes (see [section 3.2](#32-movement-outcomes)) |
| Exclusion | any penal subject (`assuntos_penal` in the TPU) is removed with `must_not` |

Each court is queried once per TPU area, with a quota of documents read per court and area:

| Group | TPU area codes | Quota per court and area |
| --- | --- | --- |
| Core | `899`, `1156`, `8826`, `9985`, `14`, `195` | 700 |
| Support | `12480`, `7724`, `10110`, `864`, `9633`, `12734`, `12775` | 250 |

That caps one run at 5,950 documents read per court (6 × 700 + 7 × 250), or 23,800 across the four courts. The quota counts documents read, not only new ones.

Collection behaviour (`pipeline/datajud.py`):

- Pages of 100 documents, sorted by `@timestamp` descending and paginated with `search_after`; timeout of 180 s per request.
- On network error, HTTP 429 or 5xx, the request is retried up to 5 times with a wait of `min(30, 3 × attempt)` seconds. If every attempt fails, collection for that court and area stops for the run and the rows already inserted are kept.
- Collection also stops when the quota is reached, when a page returns no documents, or after 5 consecutive pages with no new document.
- A commit happens after each court and area, so an interrupted run keeps what it collected.
- Each document is stored once in `raw.datajud_case` (`UNIQUE (source, payload_hash)`, where the hash is the SHA-256 of the DataJud `_id`), so collecting again never duplicates a case.

### Top-up of thin themes

`python -m pipeline --top-up` runs a second collection, after the first load, for the subjects of themes that have fewer than 5 judged cases. It reads up to 300 documents per court for those subjects, reloads, and prints how many themes have 5 or more judged cases before and after.

### Doctrine collectors

All three collectors write the article payload as JSONB into `raw.doctrine_article`, idempotently (`UNIQUE (source, payload_hash)`). They wait between requests (0.15 s for DOAJ, 0.3 s for OAI-PMH, 0.05 s for SciELO), retry up to 4 times on network error, 429 or 5xx, and commit after each term, journal or repository.

### Frequency and authentication

| Item | Value |
| --- | --- |
| Frequency | On demand. Someone runs the commands when the team decides to refresh the base |
| DataJud authentication | The CNJ public API key, provided in the `DATAJUD_API_KEY` environment variable |
| Other sources | No authentication |
| Credentials | Environment variables only; `.env` is read with `override=False` and is never committed |

## 3. Transformations (Transform)

Everything below runs in `pipeline/run.py`, in this order: flatten, load dimensions and fact, link doctrine, build themes, seed settings, generate narratives, check integrity, generate the load file.

### 3.1 Flattening DataJud cases

`pipeline/transform.py` turns each raw case into one `staging.case_event` row per movement. `staging.case_event` is truncated and rebuilt from `raw` on every run.

| Rule | Behaviour |
| --- | --- |
| No `numeroProcesso` | The case is dropped |
| Penal subject | The whole case is dropped |
| Class outside the allowed classes for the court | The case is dropped |
| Movement without date, code or name | The movement is skipped (the name falls back to a code-to-name table when the payload has none) |
| Dates | ISO 8601 (with `Z`) and `yyyyMMddHHmmss` are parsed; an unparseable date becomes empty, never an error |
| Court level (`grau`) | `G1` → `First`, `G2` → `Second`, `JE` → `SpecialCourt`, `TR` → `AppealPanel`, `GRAU_UNICO` and `SUP` → `Superior`, `GR` → `Second`. A value outside the map passes through unchanged |
| STJ judging body | The body that decided each movement is resolved to a panel: a named body (`Corte Especial`, `Primeira Turma`, `Segunda Seção`...) is recognised from its text after repairing encoding damage; otherwise the minister's name is matched against the panel membership in `pipeline/data/stj_panels.json`, which has validity dates per minister |

### 3.2 Movement outcomes

DataJud does not publish the result of a judgment as a field; it exists only as a movement. The pipeline therefore counts toward the metric only the movement codes that were checked against the official TPU table:

| Code | Name | Outcome | Polarity (whose claim) |
| --- | --- | --- | --- |
| 219 | Procedência | Granted | author (`pretensao_autor`) |
| 220 | Improcedência | Denied | author |
| 221 | Procedência em Parte | PartiallyGranted | author |
| 237 | Provimento | Granted | appellant (`pretensao_recorrente`) |
| 238 | Provimento em Parte | PartiallyGranted | appellant |
| 239 | Não-Provimento | Denied | appellant |

Every other code enters `dim_movement` as `Neutral` with `code_verified = false`. Neutral movements count for volume and time series, never for outcome percentages. Author-side and appellant-side outcomes must not be added together, which is why each verified code carries a polarity.

### 3.3 Dimensions and fact

`load_dimensions` loads, in this order:

1. Reference data: courts (`TJSP`, `TJRJ`, `TJMG`, `STJ`) and the decision outcomes, seeded from lists in the code. STF will be seeded only when it has data.
2. Verified movements with their outcome and polarity, then case classes, judging bodies and the remaining (neutral) movements.
3. `dim_case`, one row per case number, with court, class, court level, secrecy level and filing date.
4. `dim_subject` (subject name and TPU code, with the TPU area), a guard that aborts if any penal subject got through, and `bridge_case_subject`.
5. `dim_date`, a daily calendar from 1 Jan 1940 to the end of next year.
6. `fact_case_event`, one row per case movement, keyed by `case_number|movement_code|occurred_at` with `ON CONFLICT DO NOTHING`, so reloading never inflates the count (D-13).
7. The case number formatted as `NNNNNNN-DD.AAAA.J.TR.OOOO`, and the link to the court's own page: a direct e-SAJ link for TJSP (the first-instance search for `First` and `SpecialCourt`, the second-instance search for `Second` and `AppealPanel`), and the court's consultation portal for TJRJ, TJMG and STJ.
8. Doctrine articles into `dim_doctrine`.

### 3.4 Doctrine

Each collector's payload has a different shape, so `pipeline/doctrine_transform.py` extracts a common record: title, authors, journal, year, DOI, article URL and subject area.

| Rule | Behaviour |
| --- | --- |
| Text cleaning | HTML entities are decoded up to three times (some sources are double-encoded) and whitespace is collapsed |
| DOI | The `doi.org` or `doi:` prefix is removed and the value lower-cased; anything not starting with `10.` is discarded |
| Duplicates | An article is kept once per DOI and once per (source, URL), the most recently collected first |
| Load | Articles with a DOI are upserted by DOI; the others by (source, URL). A DOI found later is attached to the existing row |

Doctrine is linked to subjects by `pipeline/doctrine_link.py`, with a hybrid rule: the article title and the subject name must be close in embedding space (cosine similarity of at least 0.55, top 10 subjects per article) **and** share distinctive words (at least two when the subject name has two or more, comparing 7-letter prefixes, ignoring stopwords and words under 4 letters). Each link stores `similarity`, `link_method` (`embedding_cosine+lexical`) and `embedding_model`, so it can be audited and tightened later. The table is rebuilt on every run. Embeddings come from `paraphrase-multilingual-MiniLM-L12-v2`, run locally on CPU, with no API key.

### 3.5 Themes

A theme is a layer above the raw TPU subject, so the product can degrade to subject granularity if grouping is discarded.

- Subjects listed in `pipeline/data/theme_merge_groups.json` are merged into the curated theme named there.
- Every other subject becomes its own theme (1:1). Duplicate theme names get a numeric suffix.
- The area of law comes from `pipeline/data/theme_area_rules.json`: first an exact name (109 entries), then keyword rules (14 areas) on the accent-stripped name.
- The public `theme_key` comes from `etl.theme_registry`, which assigns a key the first time a name is seen and never reuses it, so keys stay stable across loads (D-31).
- The official TPU area of a theme is the most frequent TPU area among its subjects. A guard aborts if a theme ends up with no subject.

New merge candidates are proposed, not decided, by `python -m pipeline.propose`: it clusters subject names (agglomerative, cosine distance, threshold 0.20) and prints the groups that are not yet curated, ordered by case volume. A person reads them and records the decision by subject name in `theme_merge_groups.json`. A subject with no decision stays 1:1.

### 3.6 Settings, synonyms and narratives

- `dw.strength_config` is seeded with methodology version `1.0`, coverage of 5 courts, a minimum of 10 judged cases to grade, a divergence of 20 points and a minimum of 5 judged cases for divergence.
- `dw.search_synonym` is rebuilt from `pipeline/data/search_synonyms.json` (14 entries).
- `dw.theme_narrative` is generated by template: the materialized views are refreshed, then each theme gets a lead sentence and a body composed from `dw` numbers. Below the minimum number of judged cases it shows the case count instead of a percentage (D-32). No language model is called anywhere in the load (D-37).

### 3.7 Integrity checks

`pipeline/integrity.py` runs 9 checks and aborts the run with `IntegrityError` if any query returns a row. No load file is written in that case.

| Check | What it catches |
| --- | --- |
| fact without date | A fact whose `date_sk` is empty |
| penal subject | A penal TPU subject inside `dim_subject` |
| theme without subject | A theme with no row in `bridge_theme_subject` |
| theme key outside the registry | A theme whose key and name are not in `etl.theme_registry` |
| decision movement not verified | A movement that counts in the metric but has `code_verified = false` |
| theme summary diverging from the facts | `theme_summary.judged_case_count` different from a recount made straight from the fact |
| provenance diverging from the facts | `data_provenance` row counts different from the facts and doctrine rows |
| judged theme without text | A theme with judged cases and no narrative |
| doctrine link without score or method | A link missing `similarity`, `link_method` or `embedding_model`, or below the threshold |

## 4. Data load (Load)

### Destination model

The destination is PostgreSQL 16 (ICU locale `pt-BR`, extensions `unaccent` and `pg_trgm`). The authoritative definition of `dw` is the API's migration scripts; the pipeline keeps a copy of the schema in `tests/fixtures/dw_schema.sql` for its tests (refreshed by `scripts/refresh_test_schema.py`), which lists:

| Kind | Objects |
| --- | --- |
| Fact | `fact_case_event`, grain: one movement of one case |
| Dimensions | `dim_case`, `dim_case_class`, `dim_court`, `dim_date`, `dim_decision_outcome`, `dim_doctrine`, `dim_judging_body`, `dim_movement`, `dim_subject`, `dim_theme` |
| Bridges | `bridge_case_subject`, `bridge_subject_doctrine`, `bridge_theme_subject` |
| Support tables | `search_synonym`, `strength_config`, `theme_narrative` |
| Materialized views | `case_current_result`, `data_provenance`, `theme_outcome_distribution`, `theme_strength`, `theme_summary` |
| View | `theme_provenance` |

Working schemas in the load database: `raw` (original payloads, kept so a reload never needs to go back to the sources), `staging` (flattened records) and `etl` (the theme registry). Only `dw` goes to the destination.

### Two steps: build, then export

1. **Build, in the load database.** The pipeline writes through upserts (`ON CONFLICT`), so running it twice with the same data changes nothing. It refuses to start if the `dw` schema does not exist: start the API against that database first. It commits before exporting, because `pg_dump` opens its own connection.
2. **Export a load file.** `pipeline/load_file.py` writes one SQL file, by default `ratio-load.sql` (path in `LOAD_FILE_PATH`), with this structure:

| Part | Purpose |
| --- | --- |
| `BEGIN;` | The whole load is one transaction: if anything fails, the destination keeps its previous data |
| Version guard | Compares the last migration the destination applied (`migrations.schema_versions`) with the version the file was generated for, and raises an error if they differ or if the API never migrated the database |
| `TRUNCATE` of every `dw` table with `RESTART IDENTITY CASCADE` | Full reload, no merge |
| Data-only `pg_dump` of the `dw` schema | The data itself |
| `REFRESH MATERIALIZED VIEW` for each view | In dependency order, computed from the catalog |
| `COMMIT;` | |

Next to it the pipeline writes `ratio-load.manifest.json`, with the schema version, the extraction date (latest `extracted_at` in the fact), the row count of every `dw` table, the number of cases decided in more than one court, and the number of STJ decisions whose judging body could not be mapped to a panel or section.

### Publishing a load

`python -m pipeline.publish` packages the load for delivery. It requires the manifest and a clean git working tree, and refuses to publish a tag that already exists.

| Output | Content |
| --- | --- |
| Tag | `load-YYYYMMDD-<schema version>`, from the extraction date and the schema version |
| Assets | `ratio-<tag>.zip` with the SQL file, its `.sha256`, and the manifest |
| Release notes | Schema version, extraction date, pipeline commit and the row count per table |
| Destination | A GitHub release in `Concord-API/API5-Pipeline`, created with the `gh` CLI |

### Applying a load

With the destination database already migrated by the API (start the API against it once):

```bash
psql -d <database> -v ON_ERROR_STOP=1 -f ratio-load.sql
```

A sample load can be generated from fixture data with `python -m pipeline.sample`, on an empty database. It is what the CI uses to prove that the API serves what the pipeline produces.

## 5. Tools and technologies

| Area | Tool |
| --- | --- |
| Language | Python 3.12 |
| Database access | `psycopg2-binary` 2.9.10 (bulk inserts with `execute_values`), `pg_dump` and `psql` |
| HTTP | `requests` 2.32.3, with retry and wait between attempts |
| Configuration | `python-dotenv` 1.2.3 (`.env`) |
| Embeddings | `sentence-transformers` 5.1.2 (in `requirements-nlp.txt`), model `paraphrase-multilingual-MiniLM-L12-v2`, local on CPU |
| Clustering | `scikit-learn` 1.8.0 and `numpy` 2.3.5 |
| Destination | PostgreSQL 16, schema `dw` created by the .NET 10 API (DbUp) |
| Tests and quality | `pytest` 8.3.4, `pytest-cov`, `testcontainers[postgres]` 4.9.0, `ruff` 0.8.4, SonarQube Cloud |
| Automation | GitHub Actions, `gh` CLI for releases |

The embedding dependencies are only needed when there are doctrine articles to link; with none, the encoder is never called, which is why the CI installs only `requirements.txt`.

## 6. ETL flow diagram

```mermaid
flowchart TD
    DJ["DataJud API<br/>TJSP, TJRJ, TJMG, STJ"] -->|"python -m pipeline"| RAWC[("raw.datajud_case")]
    DO["DOAJ, SciELO, OAI-PMH"] -->|"python -m pipeline.harvest_*"| RAWD[("raw.doctrine_article")]
    RAWC -->|"flatten"| STGC[("staging.case_event")]
    RAWD -->|"extract"| STGD[("staging.doctrine_article")]
    STGC --> DW[("dw: dimensions, fact, bridges")]
    STGD --> DW
    DW --> TH["Doctrine links, themes,<br/>strength settings, narratives"]
    TH --> IC{"9 integrity checks"}
    IC -->|"any violation"| STOP["Abort: no load file"]
    IC -->|"clean"| LF["ratio-load.sql + manifest"]
    LF --> REL["GitHub release<br/>zip + sha256"]
    REL --> DEST[("Destination database<br/>migrated by the API")]
```

## 7. Scheduling and automation

The load is manual by decision (D-17): there is no scheduler, no ETL container in production and no alarm for a missed run. The extraction date is shown to users instead, and the integrity checks stop an inconsistent base from being exported.

### Configuration

| Variable | Purpose | Default |
| --- | --- | --- |
| `DATABASE_URL` | Load database, for example `postgresql://user:password@localhost:5432/ratio` | none, required |
| `DATAJUD_API_KEY` | DataJud public key; required unless `--skip-harvest` is used without `--top-up` | none |
| `LOAD_FILE_PATH` | Where the load file is written | `ratio-load.sql` |

### Commands

| Command | What it does |
| --- | --- |
| `python -m pipeline.harvest_doaj`, `harvest_scielo`, `harvest_oai` | Collect doctrine into `raw.doctrine_article`. Optional, and safe to repeat |
| `python -m pipeline` | Collect from DataJud, transform, load, check integrity and write the load file and manifest |
| `python -m pipeline --skip-harvest` | Rebuild everything from what is already in `raw`, without calling DataJud |
| `python -m pipeline --top-up` | As above, plus a second collection for themes with fewer than 5 judged cases |
| `python -m pipeline.propose` | List new subject groups to review; writes nothing to the database |
| `python -m pipeline.publish` | Package the load and create the GitHub release |
| `python -m pipeline.sample` | Generate `ratio-sample.sql` from the fixture, on an empty database |

Errors (missing variable, missing `dw` schema, failed integrity check) go to stderr and exit with status 1. When the collector seems stuck on Windows, run Python unbuffered with `python -u`.

### Run order

1. Start the API against the load database, so it creates `dw` and the migration journal.
2. Optionally run the doctrine collectors.
3. Run `python -m pipeline`, with `--top-up` when thin themes matter.
4. Run `python -m pipeline.propose` and record any new groups in `theme_merge_groups.json`, then run `python -m pipeline --skip-harvest` again.
5. Run `python -m pipeline.publish` and apply the file at the destination.

### Automation that does exist

The `Pipeline CI` workflow (`.github/workflows/ci.yml`) runs on pull requests to `main` and `us*` branches, and on pushes to `main`:

| Job | What it checks |
| --- | --- |
| `tests` | `ruff check` and `pytest` with coverage. Tests start a disposable PostgreSQL through Testcontainers; HTTP is always faked |
| `quality` | SonarQube Cloud quality gate, required on the way to `main` |
| `compatibility` | Builds the API, lets it migrate two empty databases, builds the sample with the pipeline, applies it to the second database, and checks that `/health/ready` answers `Pronto` and `/api/themes` returns themes |

## 8. Problems found and decisions made

| Problem | Decision |
| --- | --- |
| DataJud has no judgment result field | The outcome is read from movements, and only 6 codes checked against the official TPU table count in the metric; every other code is neutral. When in doubt, a code stays out (D-10) |
| Outcome codes have different polarities: 219, 220 and 221 refer to the author's claim, 237, 238 and 239 to the appellant's | Each verified movement carries a polarity, and the two are never added together |
| Embedding similarity alone linked "moral" (philosophy) articles to "dano moral" (the legal institute), scoring them above the correct ones | Doctrine is linked only when similarity and a lexical match both hold; coverage drops, which is the safer direction because an unlinked article is recoverable and a wrongly linked one is not (D-16) |
| Clustering of subject names mixes unrelated subjects | Clustering only proposes; a person curates by subject name, and an uncurated subject stays 1:1 |
| Theme identity changing between loads would break links and bookmarks | A persistent registry (`etl.theme_registry`) gives each theme a stable public key (D-31) |
| One case can be decided in a state court and in the STJ | The manifest counts cases decided in more than one court, and the rule is that such a case counts once, in the court of the last decision (D-41) |
| STJ decisions come with the minister or an internal body, not the panel | The panel is derived from the body name or from the minister's membership dates in `stj_panels.json`; the manifest reports bodies that could not be mapped |
| A numeric percentage over a handful of decisions misleads | Below the minimum number of judged cases, texts show the count instead of a percentage (D-32) |
| A language model in the load would make numbers unverifiable | No model is called in the automatic load; narratives are templates over `dw` numbers, and every number comes from a `SELECT` (D-37) |
| Penal matters are out of the product scope | Penal subjects are excluded at the query, dropped when flattening, guarded at load and checked at the end |
| Loading into a database the API did not migrate would corrupt or fail midway | The pipeline refuses to start without `dw`, and the load file refuses to run on a different schema version |
| Scheduling a load would need infrastructure on the client's server | The load is manual, runs on our side, and ships as a validated file (D-17) |
| STF is not in DataJud (it is not subordinate to the CNJ) | The only open source found is the Corte Aberta decisions panel, as a CSV with no CNJ case number and no TPU subject code. STF would be an instance of its own, and the rule of D-41 cannot reach it. The scope includes STF, but it needs a new collector, a mapping of its movement text to outcomes and of its subjects to themes, and seeding in `dim_court` once there is data. Details are in `03-dados/07-fonte-stf.md` of the docs wiki |
