# Epstein Files: Forensic Analysis Library
## Independent Analysis of the 218GB DOJ Jeffrey Epstein File Release

Disclaimer: I am not an investigative journalist, I am a data scientist. *All* content within this repo must be taken with a grain of salt: it has not been independently verified by a human. It is primarily the result of Claude Opus 4.6 reviewing the searchable database I have established at: https://github.com/rhowardstone/Epstein-research-data

Remember, there is a *reason* why journalists and investigators are so heavily trained and trusted. There are extensive protocols they take in order to ensure the information they put out is vetted. The average person does *not* have these skills. Do not reach *any* conclusions based solely on the content in this repo. The underlying data is available, and all source documents should be linked directly. If you see any inaccuracies, broken links, or anything else fishy - please don't hesitate to reach out by opening an issue.

Similarly, *please* remember to take care of yourself if you choose review these things. Be very careful when looking through this stuff. There is extensive training that people go through who do this for a living to make sure they properly self-care, decompress, and take breaks. It is *very* easy to get carried away, very easy to have emotional reactions. For example, data scientists who read CSAM-adjacent material are subject to mandatory maximum shift lengths, mandatory group therapy and debrief sessions with others who are going through the same data. Be good to yourself, be with friends, and **do not just pour through it without taking solid breaks**.

The content is intended **only for people 18+**, and only **at your own peril**. I am hoping a structured, indexed, organized set of documents makes the "click-bait jump scares" less traumatizing than those we are seeing on social media. Second-hand PTSD is a real phenomenon, and you do not want to live with some of the descriptions and images within this dataset in your head for the rest of time.

### About This Repository

This repository contains 150+ forensic analysis reports derived from the U.S. Department of Justice's release of Jeffrey Epstein investigation files — 194.5 GB across 12 datasets, comprising 1,380,937 PDFs (2,731,785 pages, 3.18 billion characters of text), plus 3,226 non-PDF native files (video, audio, spreadsheets). The analysis involved full-text extraction and FTS5 indexing of every page, 2,587,102 redaction records, 1,530 audio/video transcripts, a 1,536-person entity registry, and cross-referenced entity relationships (524 entities, 2,096 connections).

Every factual claim in these reports traces back to specific EFTA document numbers (Epstein Files Task Force Archive). Click any linked EFTA number to attempt to view the original PDF on justice.gov.

**This is not opinion or speculation.** These reports synthesize what the documents themselves say, with sourcing. Where conclusions are drawn, the supporting evidence chain is cited. Where evidence is ambiguous, that is noted. If you notice any problems, please raise an ISSUE on this repository and it will be attended to promptly.

---

### For Congressional Staff

| Document | Description |
|----------|-------------|
| [CONGRESSIONAL_READING_GUIDE.md](CONGRESSIONAL_READING_GUIDE.md) | Prioritized document list for the DOJ reading room (original 90 documents) |
| [CONGRESS_RAW_EFTA_LIST.md](CONGRESS_RAW_EFTA_LIST.md) | Complete EFTA document numbers with descriptions |
| [CONGRESSIONAL_FOLLOWUP_NEW_FINDINGS.md](CONGRESSIONAL_FOLLOWUP_NEW_FINDINGS.md) | **NEW:** 60 additional critical documents from the full-corpus revisit (DS9-12) — includes FBI FD-1023, current government officials, co-conspirator list, Wexner deposition evidence |
| [CONGRESSIONAL_ADDENDUM.md](CONGRESSIONAL_ADDENDUM.md) | Supplement: key corrections from the 225-issue factual accuracy audit, DS9 MCC death investigation documents, and March-July 2025 FBI evidence review conclusions |
| [congressional_priority_list.md](congressional_priority_list.md) | DOJ reading room priority list: documents ranked by "predator name reveal" score to maximize identification of redacted perpetrators during limited in-person review time |

---

### How to Read EFTA Citations

Every `EFTA########` number is a unique DOJ document identifier. Throughout these reports, EFTA numbers are hyperlinked to the DOJ's original PDF hosting location:

```
https://www.justice.gov/epstein/files/DataSet%20{N}/EFTA{########}.pdf
```

See the [EFTA Dataset Mapping](#efta-number-to-dataset-mapping) at the bottom of this file to determine which dataset contains a given EFTA number.

---

## Investigation Reports

Browse the [full report index](https://epstein-data.com/reports/) for the complete catalog, or explore by category below.

---

### Overview & Executive Summaries — 10 reports
[`overview/`](overview/)

Early investigation syntheses, gap detection, hidden domain analysis, and congressional briefing materials from the first sweep of the 2.73M-page corpus. Start with the [Final Investigation Report](overview/FINAL_INVESTIGATION_REPORT.md) (400+ EFTA citations, $755M traced, 30+ named individuals) or [The Architecture of Impunity](overview/INSTITUTIONAL_FAILURE_NARRATIVE.md) (7-chapter prosecutorial failure timeline, 1996–2024).

---

### Financial Forensics — 19 reports
[`financial/`](financial/)

Forensic accounting of Epstein's financial architecture: 95+ shell entities, $755M+ traced, Deutsche Bank KYC failures, Haze Trust drawdown, the Leon Black art-money pipeline, and post-death estate disposition. Highlights:
- [Shell Entity Map](financial/SHELL_ENTITY_MAP.md) — complete map of 95+ entities across 10 categories under RM CODE 82289
- [Black Art Machine](financial/TRANSACTION_CHAIN_BLACK_ART_MACHINE.md) — 15 forensic chains tracing $168M Black-to-Epstein, art pipeline and trafficking pipeline as one structure
- [JABWCPA / Institution-1](financial/FORENSIC_ACCT_4_JABWCPA_INSTITUTION1.md) — de-redacted the FBI's pseudonymized CPA and bank via DS9

---

### Named Individuals — 27 reports
[`individuals/`](individuals/)

Investigation dossiers on specific named persons in the Epstein corpus. Covers prosecution failures, financial entanglements, corroborated victim testimony, and de-redacted identities. Highlights:
- [Leon Black Prosecution Failure](individuals/LEON_BLACK_PROSECUTION_FAILURE.md) — SDNY + Manhattan DA failed to charge despite 4+ victims, FBI 302s, $62.5M USVI settlement
- [William Barr](individuals/WILLIAM_BARR_INVESTIGATION.md) — 55+ documents: NTOC tip, father hired Epstein at Dalton, Kirkland & Ellis conflict, split recusal, death investigation oversight
- [Tim Collins Banking Network](individuals/TIM_COLLINS_BANKING_NETWORK.md) — Ripplewood Holdings founder brokered European banking partnerships linking Prince Andrew, Jes Staley, Peter Mandelson, and Ehud Barak through Epstein's network
- [Khanna's Six Names](individuals/KHANNA_SIX_NAMES_INVESTIGATION.md) — the six men whose names were redacted by the FBI and read onto the House floor

Also includes the [Pseudonym/Codename Registry](individuals/PSEUDONYM_CODENAME_REGISTRY.md) — 273 EFTA-cited pseudonyms and code names mapped to real identities.

---

### Social Networks — 6 reports
[`social-networks/`](social-networks/)

How Epstein's social circles overlapped and reinforced each other: Peggy Siegal as the access broker into Manhattan society, David Geffen's art-world orbit, Bobby Kotick's Activision-era contacts, the St. Barths 2010 New Year's guest list, Reuben Brothers/Siren/Chernoy oligarch connections, and Jean Pigozzi's Edge Foundation pipeline.

---

### Intelligence Connections — 4 reports
[`intelligence/`](intelligence/)

Israeli intelligence links, FBI Confidential Human Source reports, Ehud Barak's 3,756-document footprint, Carbyne/Reporty surveillance tech, and power overlap analysis. Key document: [EFTA00090314](https://www.justice.gov/epstein/files/DataSet%209/EFTA00090314.pdf) — FBI CHS states Epstein "belonged to both U.S. and allied intelligence services" and "trained as a spy under" former Israeli PM Barak. See the [definitive Israel report](intelligence/ISRAEL_DEEP_DIVE_V2.md) for full analysis.

---

### Institutional Failures — 17 reports
[`institutional/`](institutional/)

How institutions failed, enabled, or actively participated: prosecution failures, DOJ document removals, CBP corruption, secondary Bates stamp analysis revealing 1.46M pages withheld, FBI 302 missing serials, German financial network architecture, USVI financial services legislation, DEA/OCDETF connections, and more. Highlights:
- [DOJ Document Removal Audit](institutional/DOJ_DOCUMENT_REMOVAL_AUDIT.md) — 68,000+ PDFs removed from justice.gov after initial publication
- [Secondary Bates Stamp Analysis](institutional/SECONDARY_BATES_STAMP_ANALYSIS.md) — six pre-production numbering systems reveal 57% of FBI device extractions never made it into the public release
- [CBP Corruption](institutional/CBP_CORRUPTION_INVESTIGATION.md) — de-redacted the officer who cleared Epstein's aircraft at St. Thomas for 7+ years

---

### Evidence & Digital Forensics — 12 reports
[`evidence/`](evidence/)

Device forensics (70+ devices, a 2005 computer image never examined by federal authorities), Apple Mail PLIST metadata, corrupted PDF byte-level recovery, FBI evidence binder analysis, MCC death investigation evidence, and online evidence trails. Highlights:
- [Device Forensics](evidence/DEVICE_FORENSICS_COMPLETE.md) — DVR failure 12 days pre-death, 6 machines unexported Oct 2020
- [Corrupted PDF Recovery](evidence/CORRUPTED_PDF_FORENSICS.md) — recovered Apple Address Book with 8 contacts and an iPhone 5s photo from Little Saint James, Aug 2014

---

### Scientists & Academic Network — 3 reports
[`scientists/`](scientists/)

Epstein's science funding pipeline through the Brockman/Edge Foundation: 35+ scientists, 10,000+ documents, 8 Nobel laureates, Martin Nowak ($6.5M), Noam Chomsky (trust management), Danny Hillis (Zorro Ranch), Biden Science Advisor Eric Lander, Nathan Wolfe (Global Viral/Metabiota), and FBI FinCEN investigation of Robert Trivers. See the [comprehensive audit](scientists/SCIENCE_NETWORK_COMPREHENSIVE_AUDIT.md).

---

### Victim Analysis — 4 reports
[`victims/`](victims/)

Victim census, trafficking routes, FBI evidence packages, and lead verification. Minimum 60–80 individually identified victims, likely 200+, USVI civil suit says "hundreds." Privacy protections strictly enforced — no real names, pseudonyms only. See [Trafficking Routes](victims/TRAFFICKING_ROUTES_INVESTIGATION.md) for the aircraft fleet, weekly cycling routes, MC2 recruitment (ages 13–20), and CBP bypass mechanics.

---

### Art World — 4 reports
[`art/`](art/)

$30.5M in auction proceeds traced through Haze Trust, Leon Black's $2.7B collection, 54 named art world figures, Sotheby's and Christie's transaction chains. The [unified art investigation](art/ART_INVESTIGATION_COMPLETE.md) (80KB, 100+ EFTA citations) covers it all, with supporting sub-reports on OCR/image evidence, redaction records, and open-source intelligence.

---

### Government Officials — 7 reports
[`government-officials/`](government-officials/)

Full-corpus search of all 537 current members of Congress (119th), 77 executive branch officials, and 503 Article III federal judges. Every name searched as an exact phrase across all 1.38M documents. Key finding in [Executive Branch](government-officials/EXECUTIVE_BRANCH.md): William Burns (future CIA Director) had direct email exchanges with Epstein in 2014; Epstein brokered a Burns-Thiel introduction.

---

### International Investigations

- [French Connection](FRENCH_CONNECTION_INVESTIGATION.md) — Epstein's operations in France: Brunel/MC2/Karin Models recruitment pipeline, 22 Avenue Foch, Jack Lang & Prytanee LLC, UN diplomat Fabrice Aidan, Deutsche Bank wires through French banks. Written as a guide for French investigators.

---

### Internet Theories — 3 reports
[`internet-theories/`](internet-theories/)

Exhaustive corpus searches for popular internet theories: Pizzagate, satanic rituals, adrenochrome, blood drinking, and miscellaneous claims. **All returned NEGATIVE.** Zero supporting evidence across 3.5M+ records and 519,438 PDFs.

---

### Methodology & Data Quality — 14 reports
[`methodology/`](methodology/) and [`audits/`](audits/)

Evidence chain documentation, redaction analysis, data quality audits, lead verification, and corrections. Start with:
- [Corpus Inventory](methodology/CORPUS_INVENTORY.md) — the master evidence chain: what data exists, where it came from, and how to verify any finding
- [Missing EFTA Analysis](methodology/MISSING_EFTA_ANALYSIS.md) — all 2,731,783 page-numbers accounted for, 100% complete
- [Factual Accuracy Audit](audits/FACTUAL_ACCURACY_AUDIT.md) — 225 issues across ~50 reports in 43 phases, every correction documented

---

### Raw Dataset Analysis — 11 reports
[`raw-dataset-analysis/`](raw-dataset-analysis/)

Per-dataset deep dives into DS8 and DS10 — the two datasets containing the bulk of newly released material. Entity extraction (107,422 entities from 529,061 records), name searches, key document deep dives, and 39,588 reconstructed pages from spatially-ordered redaction fragments.

---

### Prosecutorial Query Graph — 11 reports
[`pqg_lines_of_investigation/`](pqg_lines_of_investigation/)

Structured analysis of 257 grand jury subpoenas decomposed into 2,018 individual demand clauses, matched against production records. 48.2% of subpoenas have no identifiable return in the corpus. Covers the 524-day subpoena gap, 27 fully-redacted targets, tech company gaps, Deutsche Bank compliance, crypto dead ends, and correctional death investigation gaps. See the [index](pqg_lines_of_investigation/00_INDEX.md) for methodology.

---

## EFTA Number to Dataset Mapping

Use this table to determine which DOJ dataset contains a given EFTA number, or to construct the DOJ URL manually.

| Dataset | EFTA Range Start | EFTA Range End | URL Pattern |
|---------|-----------------|----------------|-------------|
| 1 | [EFTA00000001](https://www.justice.gov/epstein/files/DataSet%201/EFTA00000001.pdf) | [EFTA00003158](https://www.justice.gov/epstein/files/DataSet%201/EFTA00003158.pdf) | `DataSet%201/EFTA{########}.pdf` |
| 2 | [EFTA00003159](https://www.justice.gov/epstein/files/DataSet%202/EFTA00003159.pdf) | [EFTA00003857](https://www.justice.gov/epstein/files/DataSet%202/EFTA00003857.pdf) | `DataSet%202/EFTA{########}.pdf` |
| 3 | [EFTA00003858](https://www.justice.gov/epstein/files/DataSet%203/EFTA00003858.pdf) | [EFTA00005586](https://www.justice.gov/epstein/files/DataSet%203/EFTA00005586.pdf) | `DataSet%203/EFTA{########}.pdf` |
| 4 | [EFTA00005705](https://www.justice.gov/epstein/files/DataSet%204/EFTA00005705.pdf) | [EFTA00008320](https://www.justice.gov/epstein/files/DataSet%204/EFTA00008320.pdf) | `DataSet%204/EFTA{########}.pdf` |
| 5 | [EFTA00008409](https://www.justice.gov/epstein/files/DataSet%205/EFTA00008409.pdf) | [EFTA00008528](https://www.justice.gov/epstein/files/DataSet%205/EFTA00008528.pdf) | `DataSet%205/EFTA{########}.pdf` |
| 6 | [EFTA00008529](https://www.justice.gov/epstein/files/DataSet%206/EFTA00008529.pdf) | [EFTA00008998](https://www.justice.gov/epstein/files/DataSet%206/EFTA00008998.pdf) | `DataSet%206/EFTA{########}.pdf` |
| 7 | [EFTA00009016](https://www.justice.gov/epstein/files/DataSet%207/EFTA00009016.pdf) | [EFTA00009664](https://www.justice.gov/epstein/files/DataSet%207/EFTA00009664.pdf) | `DataSet%207/EFTA{########}.pdf` |
| 8 | [EFTA00009676](https://www.justice.gov/epstein/files/DataSet%208/EFTA00009676.pdf) | [EFTA00039023](https://www.justice.gov/epstein/files/DataSet%208/EFTA00039023.pdf) | `DataSet%208/EFTA{########}.pdf` |
| 9 | [EFTA00039025](https://www.justice.gov/epstein/files/DataSet%209/EFTA00039025.pdf) | [EFTA01262781](https://www.justice.gov/epstein/files/DataSet%209/EFTA01262781.pdf) | `DataSet%209/EFTA{########}.pdf` |
| 10 | [EFTA01262782](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01262782.pdf) | [EFTA02205654](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02205654.pdf) | `DataSet%2010/EFTA{########}.pdf` |
| 11 | [EFTA02205655](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02205655.pdf) | [EFTA02730264](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02730264.pdf) | `DataSet%2011/EFTA{########}.pdf` |
| 12 | [EFTA02730265](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02730265.pdf) | [EFTA02731783](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731783.pdf) | `DataSet%2012/EFTA{########}.pdf` |

**Base URL:** `https://www.justice.gov/epstein/files/`

**Note:** EFTA numbers are assigned **per page**, not per document. A multi-page document consumes consecutive EFTA numbers — e.g., EFTA00008320 (89 pages) covers Bates numbers 00008320–00008408, and Dataset 5 begins at EFTA00008409. There are **no gaps** between datasets; every apparent gap is accounted for by multi-page documents at dataset boundaries.

---

## Methodology

All analysis was performed locally against databases derived from the raw PDF corpus. No documents were uploaded to cloud services or third-party APIs.

| Database | Size | Records | Contents |
|----------|------|---------|----------|
| full_text_corpus.db | 6.08 GB | 1,380,937 docs / 2,731,785 pages | Full text of every page of every document (PyMuPDF extraction + invisible OCR text layers) |
| redaction_analysis_v2.db | 0.95 GB | 2,587,102 redactions / 638,416 docs | Spatial redaction analysis with text at each redaction's coordinates |
| transcripts.db | 2.5 MB | 1,530 entries (375 with speech) | GPU-transcribed audio/video (faster-whisper large-v3 on A100) |
| persons_registry.json | — | 1,536 persons | Unified entity registry from 3 sources |
| knowledge_graph.db | — | 524 entities / 2,096 connections | Cross-referenced entity relationships |

**[NATIVE_FILES_CATALOG.csv](NATIVE_FILES_CATALOG.csv)** — Complete inventory of all 3,226 non-PDF native files (video, audio, spreadsheets, images) across the DOJ release. Every non-PDF file has a corresponding PDF placeholder on DOJ; native files include 419 MCC surveillance videos (412+ hours), grand jury audio, prison phone calls, FBI interview recordings, and financial spreadsheets.

For the complete evidence chain — what data exists, where it came from, and how to verify any finding — see [Corpus Inventory](methodology/CORPUS_INVENTORY.md).

Processed data collection: https://github.com/rhowardstone/Epstein-research-data

---

## Community Platforms & Research Tools

See **[COMMUNITY_PLATFORMS.md](COMMUNITY_PLATFORMS.md)** for a directory of 78+ platforms, tools, and resources for searching and analyzing the Epstein files — government sources, search platforms, network visualization tools, AI/RAG tools, datasets, and community hubs.

---

## Processing Tools

All processing scripts (36+ Python tools) used to build the databases live in the data repo: **[Epstein-research-data/tools/](https://github.com/rhowardstone/Epstein-research-data/tree/main/tools)**

---

## Disclaimer

These reports constitute independent forensic analysis of publicly released government documents. They are not legal advice, not government publications, and not affiliated with any law enforcement agency. All findings are derived from documents released by the U.S. Department of Justice and are cited to specific EFTA document numbers that can be independently verified.

Where the evidence is ambiguous or inconclusive, that is stated explicitly. Where claims from prior reporting were found to be incorrect upon verification, corrections are documented (see Lead Verification reports). Negative findings (searches that returned zero results) are reported with equal rigor to positive findings.

This repository does not contain any original source documents, victim-identifying information, or classified material. It contains only analysis and citations.
