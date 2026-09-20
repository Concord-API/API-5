# Functional Requirements
 
What the product does, derived from the [Product Backlog](Scrum/product-backlog.md). Every
requirement traces back to the user story it comes from.
 
## Search and discovery
 
| # | Requirement | Origin |
| --- | --- | --- |
| FR-01 | Search topics from free text in Portuguese, returning curated legal topics and not cases. | US-01 |
| FR-02 | Run the full-text search tolerating missing accents and typing errors. | US-01 |
| FR-03 | Show, with each topic, the TPU subject it comes from, so the granularity of the result is explicit. | US-01 |
| FR-04 | Order results by the strength score, descending, breaking ties by decision volume. | US-02 |
| FR-05 | Filter results by court, period, instance and minimum strength, combinable. | US-04 |
| FR-06 | Show the number of cases per court in the filter options. | US-04 |
| FR-07 | Show suggested frequent queries on the home screen, drawn from real data in the loaded scope. | US-38 |
 
## Topic presentation
 
| # | Requirement | Origin |
| --- | --- | --- |
| FR-08 | Show, in each result, the score, the area of law, the thesis title, the summary, the courts, the volume, the period, the last decision and the favourable percentage. | US-03 |
 
## Strength score
 
| # | Requirement | Origin |
| --- | --- | --- |
| FR-10 | Compute a 0-to-100 strength score for each topic, from agreement, volume, coverage and recency. | US-06 |
| FR-11 | Classify the score into a grade: Consolidada, Dominante, Em formação or Divergente. | US-07 |
| FR-12 | Withhold the textual grade below the minimum number of judgments, showing the score alone. | US-07 |
| FR-13 | Allow opening the score's composition — the four components, their weights and the basis of calculation. | US-08 |
 
## Analysis of the understanding
 
| # | Requirement | Origin |
| --- | --- | --- |
| FR-14 | Present the topic's understanding in prose, opening with the number that answers the central question. | US-09 |
| FR-15 | Accompany every percentage displayed with the case count (`n`) it was computed from. | US-09, US-25 |
| FR-16 | Show the distribution of outcomes — upheld, partially upheld and dismissed — in a figure with the source stated. | US-10 |
| FR-17 | Show the yearly evolution of the topic's alignment, with the trend sentence. | US-11 |
| FR-18 | Show the topic's alignment per court. | US-12 |
| FR-19 | Show a table of each court's behaviour, with decisions, alignment and the date of the latest decision. | US-14 |
| FR-20 | Flag internal divergence between the panels of the same court. | US-17 |
| FR-21 | Show the grounds invoked in the decisions, with the frequency and acceptance rate of each. | US-19 |
| FR-22 | Show the typical elapsed time between filing and decision on the topic. | US-30 |
 
## Traceability of decisions
 
| # | Requirement | Origin |
| --- | --- | --- |
| FR-23 | Show an auditable sample of the cases behind the topic, with panel, date and outcome. | US-15 |
| FR-26 | Tie each statement in the understanding text to the ruling that supports it, with the list of cited decisions at the foot. | US-37 |
| FR-28 | Show the legal scholarship related to the topic, with author, work, the similarity score of the association and a link to the article when there is one. | US-21 |
 
## Provenance and transparency
 
| # | Requirement | Origin |
| --- | --- | --- |
| FR-29 | Show the TJSP, TJRJ and TJMG scope on every screen that presents computed data. | US-24 |
| FR-30 | Show the source, extraction date and method behind each number, omitting the number when provenance is not recorded. | US-25 |
| FR-31 | State what does not exist and why, without showing an empty field or an estimated value. | US-26 |
| FR-32 | State when the data was last updated and warn when it is stale. | US-29 |
 
## Data output
 
| # | Requirement | Origin |
| --- | --- | --- |
| FR-33 | Export to CSV the decisions that support the topic, server-side, matching what the screen shows for the same filter. | US-27 |
| FR-34 | Copy the topic's citation already carrying source, extraction date, scope and `n`. | US-28 |
 
## Natural-language querying
 
| # | Requirement | Origin |
| --- | --- | --- |
| FR-35 | Answer natural-language questions about a topic, in prose and with the numbers, over the same aggregates the screens use. | US-34 |
| FR-36 | Bring, in every chatbot answer, the source, the extraction date, the scope and the link to the cases. | US-35 |
| FR-37 | Answer that it does not know when the data is not in the base, instead of producing a plausible number. | US-36 |
