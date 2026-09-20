Detailed DoR and acceptance criteria for all 29 stories in the
[Product Backlog](../../README.md#-product-backlog), in backlog order. Scenarios are written in BDD, as
the [Definition of Ready](definition-of-ready.md) requires.
 
Each header carries priority, epic, estimate, sprint, state and dependencies. Domain values
stay in Portuguese (`NFR-20`), so terms such as *Consolidada* and *súmula* appear as they do
on screen.
 
---
 
# Sprint 1
 
---
 
### US-01 — Natural-language topic search
`Must` · E1 · 8 SP · Sprint 1 · ready · depends on —
 
> As a **user**, I want to type my case's topic in natural language and get curated legal
> topics — not a list of cases — so that I can find out how it is being decided without
> digging through one ruling at a time.
 
**Business rules**
 
- The search accepts free text in Portuguese and returns **topics**, never individual cases.
- Full-text search in Postgres, tolerant to missing accents and typing errors.
- A query with fewer than 3 characters is not submitted.
- An empty search is not an error: it returns the highest-volume topics.
- A topic with no computed judgment does not appear — a topic without an outcome answers nothing.
**Data**
 
- `search term`: text, required, minimum 3 characters.
- `topic id`, `topic title`: required.
- `search vector`: Portuguese full-text index, generated at load time.
**Messages**
 
- Confirmation: "N temas encontrados para «termo»."
- Error: "Digite ao menos 3 caracteres para buscar."
- Empty: "Nenhum tema encontrado para «termo» no escopo TJSP, TJRJ e TJMG."
**Acceptance criteria**
 
```gherkin
Scenario: Search an existing topic
Given there are computed topics in the base
When the user types "inscrição indevida em cadastro de inadimplentes"
Then the system shows a list of legal topics, and no item in the list is an individual case
 
Scenario: Search without accents
Given the topic "Inscrição indevida" exists
When the user types "inscricao indevida"
Then the system returns that same topic
 
Scenario: Search with a typing error
Given the topic "Dano moral por negativação indevida" exists
When the user types "negativacao indevda"
Then the system recovers the topic by similarity instead of returning empty
 
Scenario: Search with no match
Given there is no matching topic in the base
When the user searches "contrato de arrendamento de satélite"
Then the system explains the TJSP, TJRJ and TJMG scope and suggests rephrasing
 
Scenario: Empty search
Given the user submits the search with no term
When the search runs
Then the system returns the highest-volume topics
 
Scenario: Share the search
Given the user has submitted a search
When the term appears in the URL
Then reloading the page or opening the link reproduces the same search
```
 
---
 
### US-02 — Results ordered by strength of understanding
`Must` · E1 · 2 SP · Sprint 1 · ready · depends on US-01, US-06
 
> As a **user**, I want results ordered by how settled the understanding is, and not by text
> relevance, so that I find first what supports my thesis.
 
**Business rules**
 
- Default ordering is by the strength score, descending, and the screen states it.
- Ties are broken by the larger decision volume; text relevance is used only to decide which topics enter the list, never to order it.
- The volume behind each score is visible next to it.
**Acceptance criteria**
 
```gherkin
Scenario: Default ordering
Given a set of results
When the list is displayed
Then it is ordered by strength score, descending, and the screen states that
 
Scenario: Tie on the score
Given two topics with the same score
When the list is assembled
Then the tie is broken by decision volume, and text relevance is not displayed
 
Scenario: High volume, open dispute
Given a topic with a large volume and decisions split evenly
When the results appear
Then it does not sit at the top on volume alone
 
Scenario: High score, low volume
Given a topic with a high score and very few judgments
When it appears in the list
Then the volume behind it is visible next to the score
```
 
---
 
### US-09 — Read the understanding in prose
`Must` · E3 · 8 SP · Sprint 1 · ready · depends on US-06
 
> As a **user**, I want to read the topic's understanding in prose, opening with the number
> that answers the question and with the case count (`n`) next to every percentage, so that
> I understand the pattern without opening a table.
 
**Business rules**
 
- The topic header carries the score, the grade, the area tag, the thesis title and the metadata line: cases, courts, period and last decision.
- The text opens with a highlight line that already contains the number answering the question, with its `n`.
- Every number in the body is accompanied by its `n`, and none of them is computed on screen.
- Below **2** judged cases a topic shows the case **count** instead of a percentage: "1 decisão", never "100%". The threshold is read from the methodology configuration, not fixed in the interface.
- While automatic generation of the prose does not exist, the summary is the **curated** text per decision 20, and the data records that it is curated.
- Blocks whose source is not confirmed — ruling quotation, full-text button, citation markers, cited-decision footer — do not appear, and their place explains why.
**Acceptance criteria**
 
```gherkin
Scenario: Opening line answers the question
Given a topic with computed data
When its summary is rendered
Then the first highlight line contains the number that answers the question, with its n
 
Scenario: Topic below the percentage floor
Given a topic with a single judged case
When its summary is rendered
Then it shows the count of judged cases and no percentage

Scenario: Every percentage carries its n
Given any percentage in the body of the text
When it is displayed
Then the case count it was computed from is displayed with it
 
Scenario: Nothing is computed on screen
Given the text and its numbers come from aggregates
When the page renders
Then no number is calculated in the frontend
 
Scenario: Unsourced block
Given the ruling quotation depends on full decision text, which has no confirmed source
When the page renders
Then the quotation block does not appear and its place explains why, linking to the limitations page
 
Scenario: Footer declares provenance
Given the page was fed by one or more sources
When the footer renders
Then it lists every source, the extraction date and the methodology version
```
 
---
 
### US-10 — See the outcome distribution as a figure
`Must` · E3 · 5 SP · Sprint 1 · awaiting decision 3 · depends on US-09
 
> As a **user**, I want to see the distribution of outcomes for the topic in a figure with
> the source stated, so that I can see at a glance how much is upheld, partially upheld and
> dismissed.
 
**Business rules**
 
- The figure shows counts and percentages per outcome category. Below **2** judged cases it shows counts only, with no percentage.
- It is numbered, sits in the flow of the text — never in a card grid — and carries the source underneath.
- Without a stated source the figure is not rendered at all.
- The treatment of partially upheld claims (decision 3) is declared where the number is computed.
- Visual rules: rectangular bars, no radius, no axis, no grid, no tooltip.
**Acceptance criteria**
 
```gherkin
Scenario: Distribution with counts and percentages
Given a topic with computed outcomes
When the figure is rendered
Then each outcome category shows its count and its percentage
 
Scenario: Figure without a source
Given a figure whose source is not declared
When the page is assembled
Then the figure is not rendered
 
Scenario: Amount figure has no source
Given the awarded-amount range depends on full decision text, which has no source
When the page renders
Then the amount figure does not appear and its place explains why
```
 
---

### US-13 — Share the link to the tab I am on
`Could` · E3 · 5 SP · Sprint 1 · ready · depends on US-09
 
> As a **user**, I want the tab I am viewing to be reflected in the URL, so that I can send
> a colleague the exact link to the part I want to show.
 
**Business rules**
 
- The active tab is part of the URL and is visually distinguishable per the design system.
- Browser history follows tab changes.
**Acceptance criteria**
 
```gherkin
Scenario: Switch tabs
Given the user switches tabs
When the tab changes
Then the URL changes to reflect the active tab
 
Scenario: Open a shared link
Given a link carrying the analytical base tab
When it is opened
Then the page opens already on that tab
 
Scenario: Browser back
Given the user has switched tabs
When they press the browser's back button
Then they return to the previous tab, not out of the topic
```
 
---

### US-21 — Know what to cite beyond case law
`Must` · E4 · 8 SP · Sprint 1 · ready · depends on —

> As a **user**, I want to see the legal scholarship related to the topic, with author, work
> and a link to the article when there is one, so that I know what to cite beyond case law.

**Business rules**

- The association between scholarship and topic is **computed by semantic similarity** over the titles, with a declared threshold. It is not scholarship invoked by any decision, and the screen never presents it as such.
- Each entry carries the similarity score of its association and the model that produced it, so the reader can judge the link.
- Each entry carries author, work and, for an **article**, a link to where it is published, preferably with a stable identifier.
- A **book** appears as a text reference — author, title, edition, chapter. **Never as a PDF**: copyrighted work is not hosted.
- A topic with no association above the threshold shows no block, and its place explains why (`US-26`).
**Acceptance criteria**

```gherkin
Scenario: The association declares what it is
Given a topic with linked scholarship
When the block is rendered
Then it states that the link is by semantic similarity, with its threshold, and no entry is presented as cited by a court

Scenario: Article with a stable link
Given an article entry
When it is displayed
Then it carries a link to where it is published

Scenario: Book as a text reference
Given a book entry
When it is displayed
Then it appears as author, title, edition and chapter, with no hosted PDF

Scenario: Topic with no scholarship above the threshold
Given a topic whose associations all fall below the declared threshold
When the page renders
Then the block does not appear and its place explains why
```

---

### US-24 — Know the coverage scope
`Must` · E5 · 2 SP · Sprint 1 · ready · depends on —
 
> As a **user**, I want every screen to make clear that the data covers TJSP, TJRJ and TJMG,
> so that I do not draw a nationwide conclusion from a percentage that reflects three states.
 
**Business rules**
 
- The scope is visible **without interaction** — not hidden in a tooltip.
- The text names the courts and uses no internal technical vocabulary.
- The court list is not fixed text scattered through the interface: if decision 2 changes the scope, the statement follows.
**Acceptance criteria**
 
```gherkin
Scenario: Scope visible on every screen with numbers
Given the results screen and both detail tabs
When each of them renders
Then the territorial scope is visible without interaction
 
Scenario: Scope changes
Given decision 2 changes the scope
When the screens render
Then the statement reflects the new coverage, from a single source
```
 
---
 
### US-25 — Know the source and date of every number
`Must` · E5 · 3 SP · Sprint 1 · ready · depends on —
 
> As a **user**, I want to know the source and the extraction date of every number I am
> seeing, so that I know exactly what I am citing.
 
**Business rules**
 
- Where a page is fed by more than one source, the footer lists **all** of them; two blocks from different sources each declare their own.
- The extraction date comes from the loaded data, never from the server clock at request time.
- A block with no available provenance **is not displayed** — provenance is a requirement, not an ornament.
- The methodology version used to compute the metrics is displayed with the provenance.
**Acceptance criteria**
 
```gherkin
Scenario: Source and date on every screen with numbers
Given the results screen and both detail tabs
When each of them renders
Then the source and the extraction date are stated
 
Scenario: Several sources on one page
Given the page was fed by more than one source
When the footer renders
Then every source is listed, not only the main one
 
Scenario: Block without provenance
Given a block whose provenance is not available
When the page renders
Then that block is not displayed
 
Scenario: Date comes from the data
Given a page rendered today from a load run last week
When the extraction date is displayed
Then it shows the load's date, not today's
```
 
---
 
### US-26 — See "no data" explained instead of an empty field
`Must` · E5 · 3 SP · Sprint 1 · ready · depends on —
 
> As a **user**, I want the screen to tell me what does not exist and why, instead of showing
> an empty field or a plausible value, so that I do not build a filing on data that does not
> exist.
 
**Business rules**
 
- Three distinct messages, each with its own text: **the source does not provide this**, **the data has not been loaded yet**, and **it does not apply to this topic**. The generic message is never used.
- An empty list returned by the API is content, not an error, and never an invented placeholder.
- An unsourced field inside a table: the column does not appear, or appears explicitly flagged — never with a value.
**Acceptance criteria**
 
```gherkin
Scenario: Block with no confirmed source
Given any block without a confirmed source today
When the topic detail renders
Then it states what does not exist and why, with a path to the full explanation
 
Scenario: Empty list from the API
Given the API returns an empty list
When the screen renders
Then the empty state is content, with no invented placeholder
 
Scenario: The right message for each situation
Given each of the three situations
When the screen renders
Then it shows the matching message, never the generic one
```
 
---
 
# Sprint 2
 
---
 
### US-03 — Compare theses in the result list
`Must` · E1 · 8 SP · Sprint 2 · ready · depends on US-01, US-06
 
> As a **user**, I want to see in each result the score, the area of law, the thesis title, a
> short summary, the courts, the volume, the period, the last decision and the favourable
> percentage, so that I can compare theses before opening any of them.
 
**Business rules**
 
- Each item carries: score in a circle with `/100`, area tag, thesis title, a summary of up to two lines, court acronyms, number of cases, period, date of the last decision and the favourable percentage with its alignment bar.
- The favourable percentage carries its `n` on the same line. Below **2** judged cases the item shows the count instead of a percentage.
- When a topic has more courts than the chips shown, a `+N` indicator shows exactly the difference; when they all fit, the indicator is not rendered.
- Numbers are formatted in Portuguese (12.418, not 12,418) and are never recomputed on screen.
**Acceptance criteria**
 
```gherkin
Scenario: A complete result item
Given a topic in the result list
When the item is rendered
Then it shows score, area, title, summary, courts, volume, period, last decision and favourable percentage
 
Scenario: Percentage without a basis
Given the favourable percentage is displayed
When the item renders
Then its n is visible on the same line
 
Scenario: More courts than chips
Given a topic with more courts than the chips shown
When the item renders
Then a +N indicator shows exactly the difference
 
Scenario: Open the topic
Given a result item
When the user clicks it
Then the topic detail opens
```
 
---
 
### US-04 — Filter results to the shape of my case
`Must` · E1 · 5 SP · Sprint 2 · awaiting decision 2 · depends on US-03
 
> As a **user**, I want to filter results by court, period, instance and minimum strength,
> seeing how many cases each court has, so that I can narrow the list down to my case.
 
> **Moved from Sprint 1 to Sprint 2 on 20/09/2026.** It filters the result list `US-03`
> builds, so it was allocated a sprint ahead of what it depends on. It now sits immediately
> after `US-03`, and decision 2 — do STJ and STF enter the scope? — is due at the Sprint 2
> planning on 05/10 rather than inside Sprint 1.
 
**Business rules**
 
- Filters combine and are applied by the API; the list is never filtered in the browser.
- The court filter shows each court's case count, coming from the API.
- The instance filter offers only the instances that exist in the loaded scope.
- Active filters are reflected in the URL so a narrowed view can be shared.
**Messages**
 
- Empty result: the screen describes the filters applied and offers the path to clear them.
**Acceptance criteria**
 
```gherkin
Scenario: Filter by court with counts
Given the courts in scope
When the court filter is rendered
Then each court shows its case count, coming from the API
 
Scenario: Instance filter with state courts only
Given decision 2 keeps the scope at state courts
When the instance filter is rendered
Then the "Superior" option is not shown
 
Scenario: Apply and share
Given the user has chosen filters
When they apply them
Then the list is rebuilt by the API and the filters appear in the URL
 
Scenario: Clear filters
Given filters are applied
When the user clears them
Then every filter returns to its default and the list is rebuilt
 
Scenario: Narrowing with no results
Given a filter combination with no result
When it is applied
Then the screen describes the applied narrowing and offers a way to clear it
```
 
---
 
### US-38 — Query suggestions on the home screen
`Could` · E1 · 2 SP · Sprint 2 · ready · depends on US-01
 
> As a **user**, I want suggested frequent queries on the home screen, so that I understand
> what kind of question the tool answers before typing my own.
 
**Business rules**
 
- Suggestions come from real data in the loaded scope, never from a fixed list in the code.
- They are natural-language topics, reinforcing what US-01 teaches about what is searched here.
- With no suggestions available, the area simply does not appear — no empty space, no error text.
**Acceptance criteria**
 
```gherkin
Scenario: Click a suggestion
Given the home screen shows suggestions
When the user clicks one
Then the search runs with that term
 
Scenario: No suggestions available
Given there are no suggestions to show
When the home screen renders
Then the suggestions area is not rendered at all
```
 
---
 
### US-06 — The 0-to-100 score
`Must` · E2 · 8 SP · Sprint 2 · awaiting decision 4 · depends on —
 
> As a **user**, I want a 0-to-100 score telling me how settled the understanding on the
> topic is, so that I know whether the thesis is worth arguing or is an open fight.
 
**Business rules**
 
- The score combines four components — agreement, volume, coverage and recency — with weights summing to 1.0.
- The score is **deterministic**: same base, same score, and no component is a model's opinion.
- A topic with no computed judgment gets no score and does not appear.
- Known limitations are recorded where the user reaches the score breakdown — in particular that recency uses only the year of the last decision, not recent density.
**Acceptance criteria**
 
```gherkin
Scenario: Evenly split topic
Given a topic decided half one way and half the other
When the score is computed
Then agreement is 0
 
Scenario: Unanimous topic
Given a topic decided the same way in every judgment
When the score is computed
Then agreement is 1
 
Scenario: Volume above saturation
Given a topic with volume above the saturation point
When the score is computed
Then more decisions do not increase the score
 
Scenario: Stale thesis
Given a topic whose last decision is old enough
When the score is computed
Then recency is 0
 
Scenario: Coverage before recalibration
Given decision 4 has not been taken
When a topic is displayed
Then no score is shown
 
Scenario: Reference example
Given the reference example published in the wiki
When the automated test runs
Then it reproduces exactly that example's score
```
 
---
 
### US-07 — The grade in legal language
`Must` · E2 · 2 SP · Sprint 2 · awaiting decision 14 · depends on US-06
 
> As a **user**, I want the score to come with a grade in language that already exists in the
> legal field — Consolidada, Dominante, Em formação, Divergente — so that I do not have to
> interpret an invented scale.
 
**Business rules**
 
- Each score band maps to one of the four grades, and the grade appears next to the score.
- There is a **minimum number of judgments** (decision 14) below which the score is shown without the textual grade — a thesis with 95% agreement over eight judgments would otherwise borrow an authority eight cases do not support.
- All four labels are terms that already exist in legal vocabulary; the product invents none.
**Acceptance criteria**
 
```gherkin
Scenario: Grade next to the score
Given a topic with enough judgments
When the score is displayed
Then the matching grade is displayed next to it
 
Scenario: Below the minimum
Given a topic with high agreement but fewer judgments than the minimum
When the score is displayed
Then it appears without the textual grade
```
 
---
 
### US-08 — Audit the score's composition
`Must` · E2 · 3 SP · Sprint 2 · ready · depends on US-06
 
> As a **user**, I want to open the score's composition — the four components, their weights
> and the basis of calculation — so that I can cite the statistic knowing exactly where it
> comes from.
 
**Business rules**
 
- The breakdown shows the four components with their value and weight, plus the basis: judgments, favourable, unfavourable, number of courts and the year of the last decision.
- The breakdown is reachable in the interface — not hidden, not API-only.
- The methodology and the weights are documented and reachable from the screen.
**Acceptance criteria**
 
```gherkin
Scenario: Open the breakdown
Given a displayed score
When the user opens its composition
Then they see the four components with value and weight, and the basis of calculation
 
Scenario: Nothing recomputed
Given the score arrives ready from the API
When the screen renders
Then neither the components nor the total are recomputed
```
 
---
 
### US-11 — See the alignment evolve over time
`Must` · E3 · 5 SP · Sprint 2 · ready · depends on US-09
 
> As a **user**, I want to see how the topic's alignment evolved year by year, with the trend
> sentence, so that I know whether the understanding is settling or shifting.
 
**Business rules**
 
- The series runs oldest to most recent, with the most recent year highlighted.
- The trend sentence reads "X% → Y% in the predominant direction", both values coming from the aggregate — not computed on screen.
- A year with no computed result has no empty bar.
- With data in a single year, the trend sentence is not shown — there are no two points to compare.
**Acceptance criteria**
 
```gherkin
Scenario: Yearly series
Given a topic with results across several years
When the series is rendered
Then it runs from oldest to most recent, with the most recent year highlighted
 
Scenario: Year with no result
Given a year with no computed result
When the series is rendered
Then there is no empty bar for that year
 
Scenario: Single year
Given a topic with data in one year only
When the series is rendered
Then the trend sentence is not displayed
```
 
---
 
### US-12 — See the alignment per court
`Must` · E3 · 3 SP · Sprint 2 · ready · depends on US-09
 
> As a **user**, I want to see the topic's alignment by court, so that I know whether the
> thesis holds the same in São Paulo, Rio and Minas.
 
**Business rules**
 
- Each court in scope shows its percentage in the predominant direction, with its `n` available next to it.
- A court with no computed judgment does not appear with zero percent — it appears as having no data, or does not appear.
**Acceptance criteria**
 
```gherkin
Scenario: Alignment per court
Given a topic with decisions in more than one court
When the list is rendered
Then each court shows its percentage in the predominant direction, with its n
 
Scenario: Court without judgments
Given a court with no computed judgment on the topic
When the list is rendered
Then it does not appear with zero percent
 
Scenario: Numbers add up
Given the sum of the courts
When compared with the topic total
Then the numbers match
```
 
---
 
### US-14 — Compare each court's behaviour
`Must` · E4 · 3 SP · Sprint 2 · ready · depends on US-12
 
> As a **user**, I want a table of each court's behaviour — decisions, alignment and date of
> the latest one — so that I can compare my court with the others.
 
**Business rules**
 
- Per court: number of decisions, alignment and date of the last decision.
- The median awarded amount depends on full decision text and has no source: that column does not appear, or appears flagged as unsourced — never with a value.
- Visual rules: serif text, monospace numbers right-aligned, small-caps header, no zebra striping, no vertical borders.
- A table wider than its container scrolls **inside it**; the page never scrolls horizontally.
**Acceptance criteria**
 
```gherkin
Scenario: Behaviour per court
Given a topic with decisions in more than one court
When the table is rendered
Then each row shows decisions, alignment and the date of the last decision
 
Scenario: Unsourced column
Given the median amount has no confirmed source
When the table is rendered
Then that column does not appear, or appears flagged as unsourced
 
Scenario: Wide table
Given a table wider than its container
When it is rendered
Then it scrolls inside the container and the page does not scroll horizontally
```
 
---
 
### US-15 — Check the sample of cases behind the topic
`Must` · E4 · 5 SP · Sprint 2 · ready · depends on US-09
 
> As a **user**, I want an auditable sample of the cases behind the topic, with panel, date
> and outcome, so that I can check the cases before citing them.
 
**Business rules**
 
- Each row carries case number, panel, date and computed outcome.
- Reporting judge and amount have no confirmed source: those columns come **empty and flagged**, never filled.
- A case under seal is flagged and no sealed data is exposed.
- The default ordering is declared and stable between visits, and the sample states how many rows it shows out of how many in total ("N of M decisions").
**Acceptance criteria**
 
```gherkin
Scenario: Auditable sample
Given a topic with computed cases
When the sample is rendered
Then each row shows case number, panel, date and outcome
 
Scenario: Unsourced columns
Given reporting judge and amount have no confirmed source
When a row is rendered
Then those columns are empty and flagged, never filled
 
Scenario: Case under seal
Given a case under seal
When it appears in the sample
Then it is flagged and no sealed data is exposed
 
Scenario: Stable ordering
Given the same query run twice
When the sample is rendered
Then the order is the same
```
 
---
 
### US-17 — Know whether the court's panels diverge
`Should` · E4 · 5 SP · Sprint 2 · ready · depends on US-14
 
> As a **user**, I want to know whether the panels of my court are deciding alike, so that I
> can spot internal divergence before deciding.
 
**Business rules**
 
- Per court, the alignment of each panel, with each panel's `n` visible next to the percentage.
- A panel with a single judgment does not appear — an isolated case is noise, not divergence.
- A panel departing from its own court's pattern is flagged.
**Acceptance criteria**
 
```gherkin
Scenario: Alignment per panel
Given a court with decisions across several panels
When the block is rendered
Then each panel shows its alignment and its n
 
Scenario: Panel with a single judgment
Given a panel with one judgment only
When the block is rendered
Then that panel does not appear
 
Scenario: Divergent panel
Given a panel departing from its own court's pattern
When the block is rendered
Then the divergence is flagged
 
Scenario: Numbers add up
Given the sum of a court's panels
When compared with that court's total
Then the numbers match
```
 
---
 
### US-19 — Pick the argument that wins most
`Could` · E4 · 8 SP · Sprint 2 · source to verify · depends on —
 
> As a **user**, I want to see the grounds invoked in the topic's decisions, with the
> frequency and the acceptance rate of each one, so that I can pick the argument that wins
> most and avoid the one that always loses.
 
**DoR precondition:** a verified route to full decision text in the three courts, plus a
written answer on the feasibility of extracting grounds — cost, quality against manual
checking, and auditability. Without decision text there are no grounds to extract.
 
**Business rules**
 
- Each ground carries its nature (statute, case law, súmula, defence thesis), in how many decisions it was cited and its acceptance rate.
- Where extraction is automated, it is possible to trace which decisions a ground was identified in.
- **Frequency and acceptance rate come from counting over the data**, never from the model.
**Acceptance criteria**
 
```gherkin
Scenario: Grounds with frequency and acceptance
Given a topic with extracted grounds
When the block is rendered
Then each ground shows its nature, its citation count and its acceptance rate
 
Scenario: Traceable extraction
Given an automatically extracted ground
When the user checks it
Then they can see in which decisions it was identified
 
Scenario: The model does not count
Given a model took part in the extraction
When the numbers are displayed
Then none of them came from the model
```
 
---
 
### US-37 — See the ruling behind each statement
`Could` · E4 · 8 SP · Sprint 2 · source to verify · depends on —
 
> As a **user**, I want to see in the understanding text the ruling that supports each
> statement, with the full reference and the list of cited decisions at the foot, so that I
> can cite the same decision.
 
**DoR precondition:** a verified route to full decision text. Without it there is no headnote
to quote.
 
**Business rules**
 
- A statement supported by a specific decision carries a clickable citation marker that leads to the matching entry in the cited-decisions list.
- Each entry carries case number, panel, date and a one-line synthesis.
- Every cited decision exists in the base — no citation is generated without backing.
- Where full text is unavailable for a decision, there is no dead button.
**Acceptance criteria**
 
```gherkin
Scenario: Citation marker
Given a statement supported by a specific decision
When the user reads the text
Then there is a clickable citation marker next to it
 
Scenario: Reach the cited decision
Given the user clicks the marker
When the click happens
Then they reach the matching entry in the cited-decisions list
 
Scenario: No citation without backing
Given any cited decision
When it is displayed
Then it exists in the base
```
 
---
 
# Sprint 3
 
---
 
### US-27 — Export the topic's decisions
`Should` · E5 · 5 SP · Sprint 3 · ready · depends on US-15
 
> As a **user**, I want to export to CSV the decisions that support the topic, so that I can
> work the data outside the tool.
 
**Business rules**
 
- The file is generated by the server from the same data as the screen — never assembled in the browser.
- It contains the same rows the screen would show for the same filter: no divergence between screen and file.
- The file states source, extraction date and territorial scope.
- An unsourced field comes as an empty column, never filled.
- There is a declared row ceiling, and the interface says what it is instead of failing without explanation.
**Acceptance criteria**
 
```gherkin
Scenario: Export matches the screen
Given a topic with a filter applied
When the user exports to CSV
Then the file contains the same rows the screen would show for that filter
 
Scenario: File states its provenance
Given an exported file
When it is opened
Then it states source, extraction date and territorial scope
 
Scenario: Portuguese spreadsheet
Given a spreadsheet configured in Portuguese
When the file is opened
Then numbers, dates and accented characters render correctly
 
Scenario: Volume above the ceiling
Given a topic with more decisions than the export ceiling
When the user exports
Then the interface states the ceiling instead of failing silently
```
 
---
 
### US-28 — Copy the citation ready to paste
`Should` · E5 · 3 SP · Sprint 3 · ready · depends on US-25
 
> As a **user**, I want to copy the topic's citation already with the source, the extraction
> date, the scope and the `n`, so that I can paste it without retyping.
 
**Business rules**
 
- The copied text is plain text, one or two lines, with no formatting markup and no line break that forces re-editing.
- Nothing without backing enters the citation.
- There is a visible confirmation that the copy happened.
**Acceptance criteria**
 
```gherkin
Scenario: Copy and paste
Given the user copies the topic's citation
When they paste it
Then it contains the number, the n, the source, the extraction date and the territorial scope
 
Scenario: Visible confirmation
Given the citation was copied
When the user looks at the screen
Then there is a visible confirmation of the action
 
Scenario: Unsourced block
Given a block without a source
When the citation is assembled
Then nothing without backing enters it
```
 
---
 
### US-29 — Know whether the data is current
`Should` · E5 · 3 SP · Sprint 3 · awaiting decision 16 · depends on US-25
 
> As a **user**, I want to know when the data was last updated, and to be warned when it is
> stale, so that I do not rely on a months-old snapshot.
 
**Business rules**
 
- Every screen with a number shows the date of the last extraction.
- Past the threshold set in decision 16, there is an explicit warning that the data is stale.
- After a load has failed for days, the product must not present stale data looking current — that is the worst case for someone citing it.
**Acceptance criteria**
 
```gherkin
Scenario: Extraction date visible
Given any screen showing numbers
When it renders
Then the date of the last extraction is visible
 
Scenario: Stale data
Given the last extraction is older than the defined threshold
When the user opens the screen
Then there is an explicit warning that the data is stale
 
Scenario: Load failing for days
Given the load has failed for several days
When the user uses the product
Then it does not present stale data with the appearance of current data
```
 
---
 
### US-30 — Know how long it takes to reach a decision
`Could` · E6 · 8 SP · Sprint 3 · awaiting decision 1 · depends on —
 
> As a **user**, I want to know how long it usually takes from filing to decision on this
> topic, so that I can calibrate my client's expectation.
 
**DoR precondition:** decision 1 must have chosen the **movement** grain. With a judgment
grain this metric cannot be computed, and the story leaves the backlog instead of being
delivered as an approximation.
 
**Business rules**
 
- The metric shows the central tendency of the elapsed time between filing and decision, with its `n`.
- Cases without a decision do not enter, and that is stated — the average of those already decided is not the average of all.
- The metric's breakdown (per court, per instance) is declared, and the caveat that this is observed time in the loaded scope, not a forecast, is visible.
**Acceptance criteria**
 
```gherkin
Scenario: Elapsed time with its basis
Given a topic with decided cases
When the metric is displayed
Then it shows the central tendency with its n
 
Scenario: Undecided cases
Given cases still without a decision
When the metric is computed
Then they do not enter, and the screen states it
 
Scenario: Not a forecast
Given the metric is displayed
When the user reads it
Then the caveat that it is observed time, not a forecast, is visible
```
 
---
 
### US-34 — Ask in natural language
`Should` · E7 · 13 SP · Sprint 3 · awaiting decision 18 · depends on US-01, US-09
 
> As a **user**, I want to ask a chatbot about a topic in natural language and get the answer
> in prose with the numbers, for the questions that no screen filter answers.
 
**DoR precondition:** stable aggregates, and the screens' queries already exposed as validated
parameterised functions with no free SQL. Before that, the chatbot would
answer numbers the screens do not yet confirm.
 
**Business rules**
 
- **Every number in an answer comes from a query**; the model only interprets the question and writes the prose.
- The chatbot uses the same queries as the screens, so the same question asked in both places returns identical numbers.
- The chatbot describes what the data shows. It does not give legal advice: "the claim was upheld in 82% of cases" is data; "file this action" is not the product.
- The chatbot appears where decision 18 places it.
**Acceptance criteria**
 
```gherkin
Scenario: A question no filter answers
Given a question such as "is this topic more favourable in SP or in MG?"
When the user asks it
Then they get an answer in prose with the numbers
 
Scenario: Same numbers as the screen
Given the same question asked on the screen and in the chat
When both answer
Then the numbers are identical
 
Scenario: No legal advice
Given the user asks for advice
When the chatbot answers
Then it describes what the data shows and does not tell the user what to do
```
 
---
 
### US-35 — Be able to check what the chatbot answered
`Should` · E7 · 5 SP · Sprint 3 · ready · depends on US-34
 
> As a **user**, I want every chatbot answer to bring the `n`, the source, the extraction
> date, the scope and the link to the cases, so that I can check it before using it.
 
**Business rules**
 
- Every percentage in an answer carries its `n`; every number carries its source and extraction date.
- A statement about a topic carries a path to the cases behind it.
- A question about "the Brazilian courts" is answered for the courts in scope, **saying how many they are** — never suggesting national coverage.
- There is an evaluation suite of known-answer questions, checked against the direct query, running in CI. It is a **precondition for exposing the chatbot**.
**Acceptance criteria**
 
```gherkin
Scenario: Percentage with its basis
Given any percentage in an answer
When it is displayed
Then it carries its n, its source and its extraction date
 
Scenario: Question implying national coverage
Given a question about "the Brazilian courts"
When it is answered
Then the answer covers the courts in scope and says how many they are
 
Scenario: Evaluation suite catches divergence
Given a known-answer question whose number diverges from the direct query
When the suite runs in CI
Then it fails
```
 
---
 
### US-36 — Get "I don't know" instead of an invented number
`Should` · E7 · 3 SP · Sprint 3 · ready · depends on US-34
 
> As a **user**, I want the chatbot to say it does not know when the data is not in the base,
> so that I do not get a plausible, invented number.
 
**Business rules**
 
- Where the data is not in the base, the answer explicitly says so.
- The chatbot invents no case law for a topic that does not exist in the base.
- Every number in an answer corresponds to a value returned by one of those query functions — checked by the evaluation suite, which fails if a number has no such origin.
**Acceptance criteria**
 
```gherkin
Scenario: Data not in the base
Given a question whose data is not in the base
When it is answered
Then the answer explicitly says that data is not there
 
Scenario: Topic that does not exist
Given a topic that does not exist in the base
When the user asks about it
Then the chatbot invents no case law
 
Scenario: Block without a confirmed source
Given a question about a block with no confirmed source
When it is answered
Then the answer says it is outside the data scope, and why
 
Scenario: Every number traced to a query
Given an answer containing numbers
When the evaluation suite runs
Then every number matches a value returned by a query function, and the suite fails otherwise