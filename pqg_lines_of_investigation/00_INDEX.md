# Prosecutorial Query Graph: Lines of Investigation

## A Structured Analysis of Grand Jury Subpoena Intent vs. Produced Material

*Generated: 2026-02-15*
*Database: prosecutorial_query_graph.db (257 subpoenas, 2,018 demand clauses, 779 investigative gaps)*
*Methodology: Concordance-indexed subpoena riders decomposed into individual demand clauses, matched against production records, scored for fulfillment*
*Standard of citation: Every material factual claim is supported by at least one EFTA document number from the DOJ production, linked to its justice.gov URL*

---

## Premise

Grand jury subpoenas are not evidence. They are the *control plane* of a federal investigation — formal expressions of prosecutorial intent, decomposed into specific data requirements through attached rider clauses. By indexing all 257 subpoenas in the DOJ production, decomposing their 2,018 individual demand clauses, and comparing these demands against the 120 production records in the concordance metadata, it is possible to construct a **prosecutorial query graph**: a verifiable map of what investigators were pursuing, what they received, and where the record goes silent.

This analysis does not rely on testimony, press statements, or narrative interpretation. It relies exclusively on the structural metadata of the legal process itself: subpoena riders (what was demanded), production indexes (what was returned), and the absence of either (what was never asked or never answered).

---

## Summary Statistics

| Metric | Value |
|--------|-------|
| Grand jury subpoenas analyzed | 257 |
| Individual demand clauses decomposed | 2,018 |
| Subpoenas matched to identifiable returns | 133 (51.8%) |
| Subpoenas with no identifiable return | 124 (48.2%) |
| Demand clauses scored as FULFILLED | 849 (42.1%) |
| Demand clauses scored as UNFULFILLED | 105 (5.2%) |
| Demand clauses scored as PARTIAL | 73 (3.6%) |
| Demand clauses scored as UNKNOWN (no linked return) | 991 (49.1%) |
| Subpoenas with fully redacted targets | 27 |
| Investigative gaps identified | 779 |
| 524-day gap in subpoena issuance | July 2017 — December 2018 |

---

## Analytical Framework and Limitations

This analysis documents **structural patterns in the documentary record**. Key interpretive principles:

- **Corpus absence ≠ non-compliance.** The absence of matched returns in the EFTA corpus does not prove a subpoena recipient failed to comply. Returns may have been produced under seal, through separate case numbers, in formats not captured by the concordance system, or excluded from the public DOJ release.
- **Minimal production is standard legal practice.** Any competent attorney advises clients to produce only what is strictly required. Narrow productions, privilege assertions, and extended response timelines are normal — not evidence of obstruction.
- **Prosecutorial discretion is not documented.** The decision of whom to subpoena, what to demand, and when to stop reflects strategy, resources, and information not available in this corpus. The absence of a subpoena does not indicate investigative failure.
- **We present the record; we do not assign blame.** These dossiers document what the data shows. Readers should draw their own conclusions.

---

## Lines of Investigation

Each dossier below is a self-contained analysis of a specific gap in the prosecutorial record. They are ordered by structural significance, not by subject-matter importance.

| # | Dossier | Core Question |
|---|---------|---------------|
| 01 | [The 524-Day Subpoena Gap](./01_TEMPORAL_BLACKOUT.md) | Why did the grand jury stop issuing subpoenas for 17 months (July 2017 — December 2018)? |
| 02 | [The 27 Redacted Targets](./02_REDACTED_TARGETS.md) | Who are the entities behind the 27 fully-redacted subpoena targets, including two with 100+ page rider documents? |
| 03 | [Tech Company Production Gaps](./03_TECH_COMPANY_GAPS.md) | 21 subpoenas to technology companies (Google, Facebook, Apple, Lyft, Square); only 5 matched to returns. Where is the data? |
| 04 | [Travel Records Gap](./04_TRAVEL_RECORDS_GAP.md) | Travel has the lowest fulfillment rate of any data class (66.7% unfulfilled). Structural reasons for the gap are analyzed. |
| 05 | [Deutsche Bank Production Analysis](./05_DEUTSCHE_BANK_COMPLIANCE.md) | 28 unfulfilled clauses vs. 16 fulfilled. Which account classes and time windows did Deutsche Bank exclude? |
| 06 | [Financial Institutions Without Returns](./06_FINANCIAL_NO_RETURNS.md) | Capital One, Wells Fargo, TD Bank, Santander, and others: subpoenaed with 10-17 demand clauses, no identifiable production in the released corpus. |
| 07 | [Individuals Under Subpoena](./07_INDIVIDUAL_SUBPOENAS.md) | Darren Indyke, Richard Kahn, Tova Noel, and 30 other named individuals were directly subpoenaed. What was demanded? |
| 08 | [The Cryptocurrency Gap](./08_CRYPTO_DEAD_END.md) | One subpoena to a cryptocurrency entity, zero returns. Given documented $15M+ crypto investments, what was being investigated? |
| 09 | [Correctional Records Gaps](./09_CORRECTIONAL_DEATH_INVESTIGATION.md) | MCC guard subpoenas, prison records demands, and the death investigation — what correctional data was demanded but not produced? |
| 10 | [Prosecutorial Scope Evolution](./10_SCOPE_EVOLUTION.md) | How did subpoena targets change from 2017 to 2021? Where did investigative curiosity stop? |

---

## Methodology

### Data Sources

1. **Concordance DAT/OPT files** (12 datasets + House Estate + DOJ First Production): Parsed by `pqg_00_extract_concordance.py`, producing [`concordance_complete.db`](https://github.com/rhowardstone/Epstein-research-data/releases) (1,385,519 documents, 2,788,208 pages).

2. **Full text corpus** ([`full_text_corpus.db`](https://github.com/rhowardstone/Epstein-research-data/releases), 6.3 GB): All page-level text from the DOJ production, searchable via FTS5.

3. **Concordance metadata** ([`concordance_complete.db`](https://github.com/rhowardstone/Epstein-research-data/releases)): 1,385,519 documents with production metadata, SDNY Bates ranges, entity descriptions, and date fields.

### Pipeline

- **Step 0:** Complete concordance extraction across all DAT/OPT files, cross-referencing MD5 hashes and filenames between sources.
- **Step 1:** Identification of all 257 RIDER documents via FTS5 search. Decomposition of each rider into individual demand clauses. Classification of each clause into a data class (bank_records, phone_records, email, travel, personnel, video, medical, corporate, identification, property, correctional).
- **Step 2:** Four-strategy matching of subpoenas to returns: (1) explicit reference in production descriptions, (2) concordance cross-reference via House Estate metadata, (3) entity + temporal proximity matching, (4) FTS5 content keyword search.
- **Step 3:** Clause-level fulfillment scoring: for each demand clause, sample pages from linked returns and check for data-class-specific keywords.
- **Step 4:** Graph construction (677 nodes, 2,745 edges) and gap detection across 8 categories.

### Limitations

- **Matching is not exhaustive.** The 48.2% of subpoenas without identified returns may include cases where returns exist but cannot be linked via the available metadata. The absence of a matched return does not prove non-compliance; it proves the production record is insufficient to demonstrate compliance.
- **Fulfillment scoring is keyword-based.** A clause scored as "FULFILLED" means the linked return contains terminology consistent with the demanded data class. It does not mean the return is complete, accurate, or responsive to the specific scope of the clause.
- **Redacted targets cannot be matched.** The 27 subpoenas with redacted targets are structurally unanalyzable for entity-specific matching. Their riders can still be decomposed and their demand profiles characterized.

---

## How to Use This Material

Each dossier is designed to be independently verifiable. Every EFTA citation links directly to the DOJ's hosted document. A reader with access to the DOJ production can:

1. Open any cited EFTA document at its justice.gov URL
2. Navigate to the cited page number
3. Read the rider clause or production record referenced
4. Confirm or challenge the characterization presented here

This is not investigative journalism. It is a structured audit of the legal process, conducted against the government's own production.
