# Epstein Files: Forensic Analysis Library
## Independent Analysis of the 218GB DOJ Jeffrey Epstein File Release

### About This Repository

This repository contains 100+ forensic analysis reports derived from the U.S. Department of Justice's release of Jeffrey Epstein investigation files -- 218GB across 12 datasets, comprising 519,438+ PDFs. The analysis involved systematic review of 3.4M+ document text records, OCR-extracted text, 21,859 cataloged images, and cross-referenced entity relationships (524 entities, 2,096 connections).

Every factual claim in these reports traces back to specific EFTA document numbers (Epstein Files Task Force Archive). Click any linked EFTA number to attempt to view the original PDF on justice.gov. See the [DOJ Link Status](#doj-link-status) section below for current availability.

**This is not opinion or speculation.** These reports synthesize what the documents themselves say, with sourcing. Where conclusions are drawn, the supporting evidence chain is cited. Where evidence is ambiguous, that is noted.

---

### For Congressional Staff

| Document | Description |
|----------|-------------|
| [CONGRESSIONAL_READING_GUIDE.md](CONGRESSIONAL_READING_GUIDE.md) | Prioritized document list for the DOJ reading room |
| [CONGRESS_RAW_EFTA_LIST.md](CONGRESS_RAW_EFTA_LIST.md) | Complete EFTA document numbers with descriptions |

---

### How to Read EFTA Citations

Every `EFTA########` number is a unique DOJ document identifier. Throughout these reports, EFTA numbers are hyperlinked to the DOJ's original PDF hosting location:

```
https://www.justice.gov/epstein/files/DataSet%20{N}/EFTA{########}.pdf
```

See the [EFTA Dataset Mapping](#efta-number-to-dataset-mapping) table at the bottom of this file to determine which dataset contains a given EFTA number.

---

## Investigation Reports

### Overview & Executive Summaries

| Report | Description |
|--------|-------------|
| [FINAL_INVESTIGATION_REPORT](overview/FINAL_INVESTIGATION_REPORT.md) | Definitive 10-session investigation synthesis. 400+ EFTA citations, $755M traced, 30+ named individuals. Prosecution-referral grade. |
| [INSTITUTIONAL_FAILURE_NARRATIVE](overview/INSTITUTIONAL_FAILURE_NARRATIVE.md) | "The Architecture of Impunity" -- 7-chapter prosecutorial failure narrative, 1996-2024, 80+ EFTA citations. |
| [MASTER_REPORT](overview/MASTER_REPORT.md) | Consolidated findings from systematic document analysis of the full 627MB text corpus. |
| [PHASE1_GAP_DETECTION](overview/PHASE1_GAP_DETECTION.md) | Gap detection and counterfactual analysis -- identifying what's missing from the record. |
| [PHASE2_LEVER_TRACEBACK](overview/PHASE2_LEVER_TRACEBACK.md) | Who had the power to shield whom. Agency failures, financial concealment, academic legitimization. |
| [PHASE3_HIDDEN_DOMAINS](overview/PHASE3_HIDDEN_DOMAINS.md) | Hidden domain connections. 90+ queries across 1.8M+ redaction records, DS10, knowledge graph, and OCR text recordss. |
| [PHASE4_BRIEFING_KIT](overview/PHASE4_BRIEFING_KIT.md) | Congressional briefing kit. Prepared for staff use, based on 3.4M redaction records. |
| [SESSION9_MASTER_FINDINGS](overview/SESSION9_MASTER_FINDINGS.md) | Session 9 master findings -- continued forensic investigation. |
| [ANALYSIS_SUMMARY](overview/ANALYSIS_SUMMARY.md) | Key findings summary from the January 2026 DOJ release, anchored to SDNY prosecution memo. |
| [UNEXPLORED_DOCUMENT_MINING](overview/UNEXPLORED_DOCUMENT_MINING.md) | Deep-search of under-examined areas: camera-in-clock, T-160 VHS tapes, MCC DVR, crypto network, 48 diamonds, CSAM found 2023. |

### Financial Forensics (19 reports)

| Report | Description |
|--------|-------------|
| [FORENSIC_ACCT_1_HAZE_DRAWDOWN](financial/FORENSIC_ACCT_1_HAZE_DRAWDOWN.md) | Tracing the Haze Trust $41.7M drawdown from $49.5M to ~$7.7M (June 2018 - February 2019). |
| [FORENSIC_ACCT_2_MONEY_SOURCES](financial/FORENSIC_ACCT_2_MONEY_SOURCES.md) | Tracing the sources of Epstein's wealth. No legitimate source for $500M+ identified in the record. |
| [FORENSIC_ACCT_3_INTER_ENTITY_FLOWS](financial/FORENSIC_ACCT_3_INTER_ENTITY_FLOWS.md) | Inter-entity fund flows across the Epstein shell company network. |
| [FORENSIC_ACCT_4_JABWCPA_INSTITUTION1](financial/FORENSIC_ACCT_4_JABWCPA_INSTITUTION1.md) | Identification of JABWCPA email (CPA Richard Kahn) and Institution-1 (Deutsche Bank). |
| [FORENSIC_ACCT_5_CALENDAR_CORRELATION](financial/FORENSIC_ACCT_5_CALENDAR_CORRELATION.md) | Cross-referencing meeting/calendar data with financial transactions. |
| [FORENSIC_ACCT_6_POST_DEATH_ASSETS](financial/FORENSIC_ACCT_6_POST_DEATH_ASSETS.md) | Post-death disposition of $600M+ estate: 14 entities, Indyke/Kahn as co-executors. |
| [SHELL_ENTITY_MAP](financial/SHELL_ENTITY_MAP.md) | Complete map of 95+ Epstein shell entities across 10 categories under RM CODE 82289. |
| [SHELL_ENTITY_DARK_MONEY_INVESTIGATION](financial/SHELL_ENTITY_DARK_MONEY_INVESTIGATION.md) | 57 additional entities beyond the 95+ baseline map: JEEPERS INC, ELLMAX LLC, Rothschild pipeline. |
| [TRANSACTION_CHAIN_AUCTION_TO_DESTINATION](financial/TRANSACTION_CHAIN_AUCTION_TO_DESTINATION.md) | Complete forensic trace: $30.5M in Sotheby's/Christie's auction proceeds through Haze Trust to Valar, Honeycomb, Boothbay, Plan D. |
| [TRANSACTION_CHAIN_BLACK_ART_MACHINE](financial/TRANSACTION_CHAIN_BLACK_ART_MACHINE.md) | Prosecutorial narrative: 15 chains tracing $168M Black-to-Epstein, art machine / trafficking machine structural unity. |
| [TRANSACTION_CHAIN_THIRD_PARTY_ART](financial/TRANSACTION_CHAIN_THIRD_PARTY_ART.md) | Third-party art-related money flows: Prytanee LLC, Rothschild $25M, Tudor $13.5M, Gratitude America, David Mitchell $526K. |
| [INVESTIGATION_2_DB_KYC_BREACH](financial/INVESTIGATION_2_DB_KYC_BREACH.md) | Deutsche Bank KYC breach timeline for Southern Financial LLC / Epstein. |
| [INVESTIGATION_3_HAZE_TRUST_AML](financial/INVESTIGATION_3_HAZE_TRUST_AML.md) | Haze Trust AML inquiry -- Deutsche Bank's anti-money laundering process for Epstein's largest trust vehicle. |
| [INVESTIGATION_4_2018_WIRE_RECIPIENTS](financial/INVESTIGATION_4_2018_WIRE_RECIPIENTS.md) | November/December 2018 wire recipients -- post-Miami Herald payments. |
| [INVESTIGATION_7_BARRETT_REPORTS](financial/INVESTIGATION_7_BARRETT_REPORTS.md) | Paul Barrett's weekly reports as Deutsche Bank relationship manager on the Epstein account. |
| [DILORIO_APOLLO_WHISTLEBLOWER](financial/DILORIO_APOLLO_WHISTLEBLOWER.md) | Christopher J. DiLorio SEC whistleblower complaint -- Apollo/Epstein/Kushner connections, ESWW shell company. |
| [WECHSLER_BLACK_TRUST_INVESTIGATION](financial/WECHSLER_BLACK_TRUST_INVESTIGATION.md) | Brad Wechsler (Elysium Management), J BLACK Trust payments, $30.5M BV70 circular loan structure. |
| [LUXURY_PURCHASES_ANALYSIS](financial/LUXURY_PURCHASES_ANALYSIS.md) | Luxury purchases, lifestyle spending, and high-value acquisitions analysis. |
| [WOW_GOLD_IGE_BANNON_SEARCH](financial/WOW_GOLD_IGE_BANNON_SEARCH.md) | NEGATIVE: Zero evidence of WoW gold / IGE / virtual currency money laundering across 3.5M+ records. |

### Named Individual Investigations (18 reports)

| Report | Description |
|--------|-------------|
| [LEON_BLACK_PROSECUTION_FAILURE](individuals/LEON_BLACK_PROSECUTION_FAILURE.md) | Complete prosecution failure timeline: SDNY + Manhattan DA failed to charge despite 4+ victims, FBI 302s, $62.5M USVI settlement. |
| [LUTNICK_DUBIN_INVESTIGATION](individuals/LUTNICK_DUBIN_INVESTIGATION.md) | Howard Lutnick (single NTOC tip, financial only) and Glen Dubin (54 documents, "lent out" testimony, Eva complicit, 34+ flights). |
| [WILLIAM_BARR_INVESTIGATION](individuals/WILLIAM_BARR_INVESTIGATION.md) | 55+ documents: NTOC tip, father hired Epstein at Dalton, Kirkland & Ellis conflict, split recusal, death investigation oversight. |
| [RUEMMLER_DEEP_DIVE](individuals/RUEMMLER_DEEP_DIVE.md) | Former Obama White House Counsel: 29 documents, "Clinton Obama unnecessary implication" warning, career broker relationship through May 2019. |
| [SENATOR_MITCHELL_INVESTIGATION](individuals/SENATOR_MITCHELL_INVESTIGATION.md) | Former Senate Majority Leader: 4 evidentiary pillars, 2 independent victims, Groff/State Dept call, Mitchell's own admission. |
| [MITCHELL_CASCADE_INVESTIGATION](individuals/MITCHELL_CASCADE_INVESTIGATION.md) | David J. Mitchell (estate co-executor): $580.5K wires, fragmentation pattern, "Cascade" code name, Mandelson connection. Separate from Senator Mitchell. |
| [ROTHSCHILD_INVESTIGATION](individuals/ROTHSCHILD_INVESTIGATION.md) | Ariane de Rothschild's untraceable aderfam.ch channel. $25M in 2 wires bracketing EdR $45M DOJ penalty. Both $25M principals now dead. |
| [DAVID_SHAW_INVESTIGATION](individuals/DAVID_SHAW_INVESTIGATION.md) | D.E. Shaw & Co.: Limited exposure, proposed as dinner guest only. Science dinner network architecture mapped. |
| [JUNKERMANN_MC2_INVESTIGATION](individuals/JUNKERMANN_MC2_INVESTIGATION.md) | Nicole Junkermann: 10+ year relationship, Leon Black intro brokered, Jan 2019 island trip. MC2 stranding Russian girls in Milan, recruiting ages 13-20. |
| [MARCINKOVA_INVESTIGATION](individuals/MARCINKOVA_INVESTIGATION.md) | Nadia Marcinkova: ZERO results for full name (systematic identity protection). $100K Aviloop wire 2 days after Miami Herald. 124 flights. NPA protected. |
| [INVESTIGATION_1_BARR_NTOC](individuals/INVESTIGATION_1_BARR_NTOC.md) | William Barr NTOC filing deep dive -- forensic analysis of the tip and associated evidence. |
| [INVESTIGATION_5_MAXWELL_SSN](individuals/INVESTIGATION_5_MAXWELL_SSN.md) | Maxwell NYPD firearms permit anomalies: CT-prefix SSN, military/criminal record flags. |
| [INVESTIGATION_6_LEON_BLACK](individuals/INVESTIGATION_6_LEON_BLACK.md) | Leon Black: 47 EFTA docs, NTOC filing, HT Subject Referral, "DANY do not doubt her allegations." |
| [INVESTIGATION_8_UNEXPLORED_NAMES](individuals/INVESTIGATION_8_UNEXPLORED_NAMES.md) | 18 previously under-examined names: comprehensive forensic analysis. |
| [ALEXANDER_WANDTKE_NSALEM_INVESTIGATION](individuals/ALEXANDER_WANDTKE_NSALEM_INVESTIGATION.md) | Alexander brothers (currently on trial SDNY Jan 2026 for sex trafficking 60+ women), Max Wandtke (ghost), North Salem wedding evidence. |
| [RUSSIAN_WOMAN_SCOTT_IDENTIFICATION](individuals/RUSSIAN_WOMAN_SCOTT_IDENTIFICATION.md) | Identification attempt: woman likely Uzbek (WIUT), possibly "Nina K." (25+ docs). "Scott" unidentified. |
| [UNNAMED_PERSONS_INVESTIGATION](individuals/UNNAMED_PERSONS_INVESTIGATION.md) | Foreign president (Ehud Barak), AOL cluster, 34 journal names mapped, Wigdor corroboration. |
| [DUBAI_SULAYEM_INVESTIGATION](individuals/DUBAI_SULAYEM_INVESTIGATION.md) | Sultan bin Sulayem directed DP World SVP to contact Epstein's USVI attorney re "port of St Croix." Victim names "Sultan from Dubai." 40+ docs. |

### Victim Analysis (4 reports)

| Report | Description |
|--------|-------------|
| [ALLRED_VICTIM_INTERVIEW](victims/ALLRED_VICTIM_INTERVIEW.md) | Complete 30-page FBI evidence package: victim met Epstein at 17, 4 assaults before 18, 2 rapes, harem ideology, Brunel companion. |
| [VICTIM_CENSUS](victims/VICTIM_CENSUS.md) | Minimum 60-80 individually identified victims, likely 200+, USVI civil suit says "hundreds." |
| [VICTIM_LEADS_VERIFICATION](victims/VICTIM_LEADS_VERIFICATION.md) | Re-verification of Leads 7-12 including major correction on flight log modification claim. |
| [TRAFFICKING_ROUTES_INVESTIGATION](victims/TRAFFICKING_ROUTES_INVESTIGATION.md) | Aircraft fleet, weekly cycling routes, MC2 recruitment ages 13-20, pilots modified flight logs, victim "database," CBP bypass. |

### Evidence & Digital Forensics (9 reports)

| Report | Description |
|--------|-------------|
| [DEVICE_FORENSICS_COMPLETE](evidence/DEVICE_FORENSICS_COMPLETE.md) | 70+ devices, 2005 computer NEVER searched, DVR failure 12 days pre-death, 6 machines unexported Oct 2020. |
| [PLIST_FORENSIC_SEARCH](evidence/PLIST_FORENSIC_SEARCH.md) | 460+ Apple Mail PLIST metadata documents, 2 email accounts, 9-year date range (2009-2018). |
| [PLIST_REDACTED_EMAILS_DEEP_DIVE](evidence/PLIST_REDACTED_EMAILS_DEEP_DIVE.md) | 12 failed redaction overlays exposing PLIST XML: Russian/Uzbek woman, neuroscience dinner, Groff calling State Dept for Mitchell. |
| [PLIST_TIMESTAMP_TRANSACTION_CORRELATION](evidence/PLIST_TIMESTAMP_TRANSACTION_CORRELATION.md) | 420 timestamps vs financial dates: Tudor $13.5M strongest correlation, 99-day blackout Nov 2018-Feb 2019. |
| [EFTA00004800_DEEP_DIVE](evidence/EFTA00004800_DEEP_DIVE.md) | FBI "Book 17" evidence binder: 98 pages of CDs/DVDs, "grapes" files blacked out alongside CSAM, ~50+ unscanned media items. |
| [BLACKOUT_PERIOD_INVESTIGATION](evidence/BLACKOUT_PERIOD_INVESTIGATION.md) | 99-day email silence (Nov 2018 - Feb 2019): Epstein flew 8+ flights, paid $100K/$250K, trafficked victims. Signal/WhatsApp/PGP refs found. |
| [MAXWELL_FIREARMS_LICENSE_INVESTIGATION](evidence/MAXWELL_FIREARMS_LICENSE_INVESTIGATION.md) | Maxwell NYPD firearms license application investigation. |
| [EVIDENCE_COMPILATION](evidence/EVIDENCE_COMPILATION.md) | Master evidence table: named individuals with documented victim interactions and legal status. |
| [GABRIELLA_RICO_JIMENEZ_INVESTIGATION](evidence/GABRIELLA_RICO_JIMENEZ_INVESTIGATION.md) | NO connection found to Epstein. Jimenez incident Aug 2009 in Monterrey. ZERO hits across all document collections. |

### Intelligence Connections (4 reports)

| Report | Description |
|--------|-------------|
| [ISRAEL_DEEP_DIVE_V2](intelligence/ISRAEL_DEEP_DIVE_V2.md) | Definitive Israel report: Barak 25+ docs, 301 E 66th nexus, Kohn letters, NTOC tips. Infrastructure consistent with intel operation but no explicit service connection. |
| [ISRAELI_INTELLIGENCE_DEEP_DIVE](intelligence/ISRAELI_INTELLIGENCE_DEEP_DIVE.md) | Initial Israeli intelligence connections investigation across all document collections. |
| [BIOTECH_SCIENCE_NETWORK_INVESTIGATION](intelligence/BIOTECH_SCIENCE_NETWORK_INVESTIGATION.md) | Biotech, science, and AI investment network: 95+ queries, Brockman/Edge pipeline, Church, Lloyd, Krauss, Minsky connections. |
| [POWER_OVERLAP_SEALED_FILINGS_INVESTIGATION](intelligence/POWER_OVERLAP_SEALED_FILINGS_INVESTIGATION.md) | Power overlap, sealed filings, and evidence suppression patterns. 100+ searches across 4 document collections. |

### Institutional Failures (3 reports)

| Report | Description |
|--------|-------------|
| [PROSECUTION_FAILURES_ANALYSIS](institutional/PROSECUTION_FAILURES_ANALYSIS.md) | Comprehensive documentation of failed prosecutions: NPA architecture, Acosta deposition, Dershowitz self-immunity, CVRA violations, 15+ named individuals. |
| [CBP_CORRUPTION_INVESTIGATION](institutional/CBP_CORRUPTION_INVESTIGATION.md) | CBP officer Badge #CAS03223 self-incriminated, 7+ years clearing Epstein's aircraft at St. Thomas. FBI proffer sessions Oct-Nov 2020. |
| [CBP_RUEMMLER_REMAINING_LEADS](institutional/CBP_RUEMMLER_REMAINING_LEADS.md) | CBP officer expanded investigation, Ruemmler full 15-email trail, remaining unidentified leads. |

### Art World (4 reports)

| Report | Description |
|--------|-------------|
| [ART_INVESTIGATION_COMPLETE](art/ART_INVESTIGATION_COMPLETE.md) | Unified art investigation: $30.5M auction proceeds, Leon Black $2.7B collection, 54 named art world figures, 100+ EFTA citations. 80KB, 72 sections. |
| [ART_INVESTIGATION_OCR_IMAGES](art/ART_INVESTIGATION_OCR_IMAGES.md) | Sub-report: 53 searches across OCR text and image records for art-related evidence. |
| [ART_INVESTIGATION_REDACTIONS](art/ART_INVESTIGATION_REDACTIONS.md) | Sub-report: 165 queries across 3.4M redaction records for art-related content. |
| [ART_INVESTIGATION_WEB_RESEARCH](art/ART_INVESTIGATION_WEB_RESEARCH.md) | Sub-report: 40+ web sources, 16 sections of open-source intelligence on Epstein art connections. |

### Methodology & Data Quality (10 reports)

| Report | Description |
|--------|-------------|
| [DATA_QUALITY_AUDIT](methodology/DATA_QUALITY_AUDIT.md) | Audit of "bad_overlay" redaction records -- confirmed ~98% are OCR noise from degraded scans. |
| [EVIDENCE_RELIABILITY_AUDIT](methodology/EVIDENCE_RELIABILITY_AUDIT.md) | Impact assessment: how "bad_overlay" OCR noise affects investigation report reliability. |
| [REDACTION_ASYMMETRY_ANALYSIS](methodology/REDACTION_ASYMMETRY_ANALYSIS.md) | 179,139 redactions analyzed: victim names properly redacted, powerful associates frequently recoverable under bad overlays. |
| [DEFECTIVE_REDACTION_FINDINGS](methodology/DEFECTIVE_REDACTION_FINDINGS.md) | Defective redactions in 2022 Virgin Islands civil case Exhibit 1 — text visible beneath incompetent overlay. |
| [REDACTION_TEXT_LAYER_ANALYSIS](methodology/REDACTION_TEXT_LAYER_ANALYSIS.md) | Definitive proof: Dec 19 PDFs use invisible OCR text layer (Tr=3). Black boxes are baked JPEG pixels, not PDF overlays. |
| [DEC2025_REDACTION_COMPARISON](methodology/DEC2025_REDACTION_COMPARISON.md) | Comparison of December 19, 2025 DOJ release redactions between original and re-released versions. |
| [HIDDEN_TEXT_COMPLETE_REVIEW](methodology/HIDDEN_TEXT_COMPLETE_REVIEW.md) | Complete review of text extracted from document text layers across the entire EFTA corpus. |
| [LEAD_VERIFICATION_REPORT](methodology/LEAD_VERIFICATION_REPORT.md) | Deep forensic review via direct PDF reading, cross-referenced with document text records. |
| [LEAD_VERIFICATION_PART1](methodology/LEAD_VERIFICATION_PART1.md) | Leads 1-6 verified. Key corrections: CBP proffer was cooperating witness, not the officer; Austrian passport agent never called back. |
| [LEAD_VERIFICATION_PART2](methodology/LEAD_VERIFICATION_PART2.md) | Leads 7-12 verified. Major correction: flight log modification claim was INVERTED in prior notes. |

### Conspiracy Theory Debunking (5 reports)

| Report | Description |
|--------|-------------|
| [CONSPIRACY_THEORY_SEARCH_MISC](conspiracy-debunking/CONSPIRACY_THEORY_SEARCH_MISC.md) | Exhaustive search for miscellaneous internet theories across 218GB, 519,438 PDFs. |
| [CONSPIRACY_THEORY_SEARCH_OCCULT](conspiracy-debunking/CONSPIRACY_THEORY_SEARCH_OCCULT.md) | NEGATIVE: Zero evidence of satanic rituals, adrenochrome, or blood drinking across 3.5M+ records. |
| [CONSPIRACY_THEORY_SEARCH_PIZZAGATE](conspiracy-debunking/CONSPIRACY_THEORY_SEARCH_PIZZAGATE.md) | NEGATIVE: Zero evidence supporting Pizzagate or related theories across 519,438 PDFs. |
| [FOUR_CHAN_PARAMEDIC_INVESTIGATION](conspiracy-debunking/FOUR_CHAN_PARAMEDIC_INVESTIGATION.md) | 4chan death leak: hard drives removed from SHU at 10:15 PM, guard DPAs then charges dismissed, FBI captured 8+ screenshots. |
| [ONLINE_EVIDENCE_INVESTIGATION](conspiracy-debunking/ONLINE_EVIDENCE_INVESTIGATION.md) | r/maxwellhill screenshot in FBI case serial, social media led to Maxwell via Borgerson-Angara-Tidewood shells. |

### Raw Dataset Analysis (11 reports)

| Report | Description |
|--------|-------------|
| [DS10_COMPLETE_FINDINGS](raw-dataset-analysis/DS10_COMPLETE_FINDINGS.md) | Dataset 10 complete scan: 503,154 PDFs, 1,629,776 redaction rows. FBI "Prominent Names" briefing recovered here. |
| [DS10_COMPREHENSIVE_NAME_SEARCH](raw-dataset-analysis/DS10_COMPREHENSIVE_NAME_SEARCH.md) | Comprehensive name search across the DS10 document text records. |
| [DS10_ENTITY_EXTRACTION_REPORT](raw-dataset-analysis/DS10_ENTITY_EXTRACTION_REPORT.md) | 107,422 entities extracted from 529,061 text records: 49K names, 36K dates, 8K addresses. |
| [DS10_FORENSIC_ANALYSIS](raw-dataset-analysis/DS10_FORENSIC_ANALYSIS.md) | Deep forensic analysis of the full 1,808,915-row document text corpus. |
| [DS10_INTERIM_FINDINGS](raw-dataset-analysis/DS10_INTERIM_FINDINGS.md) | Interim findings from Dataset 10 scan (~15% complete at time of writing). |
| [DS10_KEY_DOCUMENTS_DEEP_DIVE](raw-dataset-analysis/DS10_KEY_DOCUMENTS_DEEP_DIVE.md) | Document-by-document analysis of recovered hidden text from key DS10 documents. |
| [DS10_RECONSTRUCTED_PAGES](raw-dataset-analysis/DS10_RECONSTRUCTED_PAGES.md) | 39,588 reconstructed pages from spatially-ordered redaction fragments; 4M+ characters recovered. |
| [DS8_CONTENT_SURVEY](raw-dataset-analysis/DS8_CONTENT_SURVEY.md) | Dataset 8 comprehensive content survey: 10,594 PDFs across 11 subdirectories. |
| [DS8_MEDIA_CATALOG](raw-dataset-analysis/DS8_MEDIA_CATALOG.md) | Dataset 8 media catalog: 11,034 files, 419 surveillance MP4s (412.5 hours), 438 native files. |
| [DS8_NEW_LEADS](raw-dataset-analysis/DS8_NEW_LEADS.md) | New leads and investigative threads extracted from Dataset 8. |
| [DS8_VERIFICATION](raw-dataset-analysis/DS8_VERIFICATION.md) | Source document cross-referencing: verifying redaction analysis claims against original PDFs. |

---

## EFTA Number to Dataset Mapping

Use this table to determine which DOJ dataset contains a given EFTA number, or to construct the DOJ URL manually.

| Dataset | EFTA Range Start | EFTA Range End | URL Pattern |
|---------|-----------------|----------------|-------------|
| 1 | EFTA00000001 | EFTA00003158 | `DataSet%201/EFTA{########}.pdf` |
| 2 | EFTA00003159 | EFTA00003857 | `DataSet%202/EFTA{########}.pdf` |
| 3 | EFTA00003858 | EFTA00005586 | `DataSet%203/EFTA{########}.pdf` |
| 4 | EFTA00005705 | EFTA00008320 | `DataSet%204/EFTA{########}.pdf` |
| 5 | EFTA00008409 | EFTA00008528 | `DataSet%205/EFTA{########}.pdf` |
| 6 | EFTA00008529 | EFTA00008998 | `DataSet%206/EFTA{########}.pdf` |
| 7 | EFTA00009016 | EFTA00009664 | `DataSet%207/EFTA{########}.pdf` |
| 8 | EFTA00009676 | EFTA00039023 | `DataSet%208/EFTA{########}.pdf` |
| 9 | EFTA00039025 | EFTA01262781 | `DataSet%209/EFTA{########}.pdf` |
| 10 | EFTA01262782 | EFTA02205654 | `DataSet%2010/EFTA{########}.pdf` |
| 11 | EFTA02205655 | EFTA02730264 | `DataSet%2011/EFTA{########}.pdf` |
| 12 | EFTA02730265 | EFTA02731783 | `DataSet%2012/EFTA{########}.pdf` |

**Base URL:** `https://www.justice.gov/epstein/files/`

**Note:** There are small gaps between some datasets (e.g., Dataset 4 ends at 8320, Dataset 5 starts at 8409). EFTAs falling in gaps are mapped to the nearest lower dataset.

---

## DOJ Link Status

As of February 2026, the DOJ has taken down most or all files from the justice.gov Epstein library. The main page (justice.gov/epstein) returns HTTP 403, and individual EFTA PDFs return HTTP 404. This occurred after the DOJ acknowledged redaction failures that exposed victim-identifying information in "several thousand documents" ([ABC News](https://abcnews.go.com/US/epstein-files-doj-thousand-documents-mistakenly-identified-victims/story?id=129787942), [OPB](https://www.opb.org/article/2025/12/21/doj-releases-additional-epstein-files-as-it-removes-others/), [PBS](https://www.pbs.org/newshour/politics/at-least-16-files-disappear-from-doj-site-for-epstein-documents-including-trump-photo)).

EFTA links in these reports remain as canonical references to the DOJ's document identifiers. The underlying documents can be accessed through:
- The complete 218GB archive torrent (archived independently)
- Congressional reading rooms
- FOIA requests referencing specific EFTA numbers

A programmatic audit of all 6,297 unique EFTA URLs linked in these reports confirmed that 0 of 12 datasets currently return HTTP 200 from justice.gov.

---

## Methodology

All analysis was performed against four primary document collections built from the raw PDF corpus:

| Collection | Records | Contents |
|------------|---------|----------|
| Primary document text | 1,808,942 | Text extracted from document text layers, document summaries, reconstructed pages, extracted entities |
| Dataset 10 document text | 1,629,776 | Dataset 10 specific text extraction |
| OCR-extracted text | 38,955 | Full-page OCR text from scanned documents |
| Image catalog | 21,859 | Cataloged images with descriptions |
| Entity relationships | 524 entities, 2,096 connections | Cross-referenced entities and their relationships |

For methodology details, data quality assessment, and reliability audits, see the [Methodology & Data Quality](#methodology--data-quality-10-reports) section above.

---

## Disclaimer

These reports constitute independent forensic analysis of publicly released government documents. They are not legal advice, not government publications, and not affiliated with any law enforcement agency. All findings are derived from documents released by the U.S. Department of Justice and are cited to specific EFTA document numbers that can be independently verified.

Where the evidence is ambiguous or inconclusive, that is stated explicitly. Where claims from prior reporting were found to be incorrect upon verification, corrections are documented (see Lead Verification reports). Negative findings (searches that returned zero results) are reported with equal rigor to positive findings.

This repository does not contain any original source documents, victim-identifying information, or classified material. It contains only analysis and citations.
