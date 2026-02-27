# Epstein Files: Forensic Analysis Library
## Independent Analysis of the 218GB DOJ Jeffrey Epstein File Release

Disclaimer: I am not an investigative journalist, I am a data scientist. *All* content within this repo must be taken with a grain of salt: it has not been independently verified by a human. It is primarily the result of Claude Opus 4.6 reviewing the searchable database I have established at: https://github.com/rhowardstone/Epstein-research-data

Remember, there is a *reason* why journalists and investigators are so heavily trained and trusted. There are extensive protocols they take in order to ensure the information they put out is vetted. The average person does *not* have these skills. Do not reach *any* conclusions based solely on the content in this repo. The underlying data is available, and all source documents should be linked directly. If you see any inaccuracies, broken links, or anything else fishy - please don't hesitate to reach out by opening an issue.

Similarly, *please* remember to take care of yourself if you choose review these things. Be very careful when looking through this stuff. There is extensive training that people go through who do this for a living to make sure they properly self-care, decompress, and take breaks. It is *very* easy to get carried away, very easy to have emotional reactions. For example, data scientists who read CSAM-adjacent material are subject to mandatory maximum shift lengths, mandatory group therapy and debrief sessions with others who are going through the same data. Be good to yourself, be with friends, and **do not just pour through it without taking solid breaks**.

The content is intended **only for people 18+**, and only **at your own peril**. I am hoping a structured, indexed, organized set of documents makes the "click-bait jump scares" less traumatizing than those we are seeing on social media. Second-hand PTSD is a real phenomenon, and you do not want to live with some of the descriptions and images within this dataset in your head for the rest of time.

### About This Repository

This repository contains 150+ forensic analysis reports derived from the U.S. Department of Justice's release of Jeffrey Epstein investigation files -- 194.5 GB across 12 datasets, comprising 1,380,937 PDFs (2,731,785 pages, 3.18 billion characters of text), plus 3,226 non-PDF native files (video, audio, spreadsheets). The analysis involved full-text extraction and FTS5 indexing of every page, 2,587,102 redaction records, 1,530 audio/video transcripts, a 1,536-person entity registry, and cross-referenced entity relationships (524 entities, 2,096 connections).

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

See the [EFTA Dataset Mapping](#efta-number-to-dataset-mapping) table at the bottom of this file to determine which dataset contains a given EFTA number.

---

## Investigation Reports

### Early Investigation Summaries

> **Note:** These reports were written in January–February 2026 during the first weeks of the investigation. They remain accurate but do not reflect the full scope of findings from the 150+ reports that followed. For the complete catalog, browse the sections below or visit the [full report index](https://epstein-data.com/reports/).

| Report | Description |
|--------|-------------|
| [FINAL_INVESTIGATION_REPORT](overview/FINAL_INVESTIGATION_REPORT.md) | Early investigation synthesis (Feb 7, 2026). 400+ EFTA citations, $755M traced, 30+ named individuals. Covers first two weeks of findings only — see later reports for deeper analysis. |
| [INSTITUTIONAL_FAILURE_NARRATIVE](overview/INSTITUTIONAL_FAILURE_NARRATIVE.md) | "The Architecture of Impunity" -- 7-chapter prosecutorial failure narrative, 1996-2024, 80+ EFTA citations. |
| [MASTER_REPORT](overview/MASTER_REPORT.md) | Early findings (Feb 5, 2026) from initial redaction and text layer analysis of the 627MB text corpus. |
| [PHASE1_GAP_DETECTION](overview/PHASE1_GAP_DETECTION.md) | Gap detection and counterfactual analysis -- identifying what's missing from the record. |
| [PHASE2_LEVER_TRACEBACK](overview/PHASE2_LEVER_TRACEBACK.md) | Who had the power to shield whom. Agency failures, financial concealment, academic legitimization. |
| [PHASE3_HIDDEN_DOMAINS](overview/PHASE3_HIDDEN_DOMAINS.md) | Hidden domain connections. 90+ queries across 1.8M+ redaction records, DS10, knowledge graph, and OCR text recordss. |
| [PHASE4_BRIEFING_KIT](overview/PHASE4_BRIEFING_KIT.md) | Congressional briefing kit. Prepared for staff use, based on 3.4M redaction records. |
| [SESSION9_MASTER_FINDINGS](overview/SESSION9_MASTER_FINDINGS.md) | Supplemental findings: art forensics, trafficking routes, device forensics, prosecution failures, CBP corruption, 4chan/online evidence. |
| [ANALYSIS_SUMMARY](overview/ANALYSIS_SUMMARY.md) | First-look findings (Jan 2026) from the initial DOJ release, anchored to SDNY prosecution memo. |
| [UNEXPLORED_DOCUMENT_MINING](overview/UNEXPLORED_DOCUMENT_MINING.md) | Deep-search of under-examined areas: camera-in-clock, T-160 VHS tapes, MCC DVR, crypto network, 48 diamonds, CSAM found 2023. |

### Financial Forensics (19 reports)

| Report | Description |
|--------|-------------|
| [FORENSIC_ACCT_1_HAZE_DRAWDOWN](financial/FORENSIC_ACCT_1_HAZE_DRAWDOWN.md) | Tracing the Haze Trust $41.7M drawdown from $49.5M to ~$7.7M (June 2018 - February 2019). |
| [FORENSIC_ACCT_2_MONEY_SOURCES](financial/FORENSIC_ACCT_2_MONEY_SOURCES.md) | Tracing the sources of Epstein's wealth. No legitimate source for $500M+ identified in the record. |
| [FORENSIC_ACCT_3_INTER_ENTITY_FLOWS](financial/FORENSIC_ACCT_3_INTER_ENTITY_FLOWS.md) | Inter-entity fund flows across the Epstein shell company network. |
| [FORENSIC_ACCT_4_JABWCPA_INSTITUTION1](financial/FORENSIC_ACCT_4_JABWCPA_INSTITUTION1.md) | Identification of JABWCPA (Jeanne Anne Brennan Wiebracht, CPA — **de-redacted via DS9**) and Institution-1 (Deutsche Bank). Richard Kahn confirmed as `rkahn` email. |
| [FORENSIC_ACCT_5_CALENDAR_CORRELATION](financial/FORENSIC_ACCT_5_CALENDAR_CORRELATION.md) | Cross-referencing meeting/calendar data with financial transactions. |
| [FORENSIC_ACCT_6_POST_DEATH_ASSETS](financial/FORENSIC_ACCT_6_POST_DEATH_ASSETS.md) | Post-death disposition of $600M+ estate: 14 entities, Indyke/Kahn as co-executors. |
| [SHELL_ENTITY_MAP](financial/SHELL_ENTITY_MAP.md) | Complete map of 95+ Epstein shell entities across 10 categories under RM CODE 82289. |
| [SHELL_ENTITY_DARK_MONEY_INVESTIGATION](financial/SHELL_ENTITY_DARK_MONEY_INVESTIGATION.md) | 57 additional entities beyond the 95+ baseline map: JEEPERS INC, ELLMAX LLC, Rothschild pipeline. |
| [TRANSACTION_CHAIN_AUCTION_TO_DESTINATION](financial/TRANSACTION_CHAIN_AUCTION_TO_DESTINATION.md) | Complete forensic trace: $30.5M in Sotheby's/Christie's auction proceeds through Haze Trust to Valar, Honeycomb, Boothbay, Plan D. |
| [TRANSACTION_CHAIN_BLACK_ART_MACHINE](financial/TRANSACTION_CHAIN_BLACK_ART_MACHINE.md) | Prosecutorial narrative: 15 chains tracing $168M Black-to-Epstein, art machine / trafficking machine structural unity. |
| [TRANSACTION_CHAIN_THIRD_PARTY_ART](financial/TRANSACTION_CHAIN_THIRD_PARTY_ART.md) | Third-party art-related money flows: Prytanee LLC (**corrected:** Etienne Pierre Jean Binant, not Jack Lang), Rothschild $25M, Tudor $13.5M, Gratitude America, David Mitchell $526K. |
| [INVESTIGATION_2_DB_KYC_BREACH](financial/INVESTIGATION_2_DB_KYC_BREACH.md) | Deutsche Bank KYC breach timeline for Southern Financial LLC / Epstein. |
| [INVESTIGATION_3_HAZE_TRUST_AML](financial/INVESTIGATION_3_HAZE_TRUST_AML.md) | Haze Trust AML inquiry -- Deutsche Bank's anti-money laundering process for Epstein's largest trust vehicle. |
| [INVESTIGATION_4_2018_WIRE_RECIPIENTS](financial/INVESTIGATION_4_2018_WIRE_RECIPIENTS.md) | November/December 2018 wire recipients -- post-Miami Herald payments. |
| [INVESTIGATION_7_BARRETT_REPORTS](financial/INVESTIGATION_7_BARRETT_REPORTS.md) | Paul Barrett's weekly reports as Deutsche Bank relationship manager on the Epstein account. |
| [DILORIO_APOLLO_WHISTLEBLOWER](financial/DILORIO_APOLLO_WHISTLEBLOWER.md) | Christopher J. DiLorio SEC whistleblower complaint -- Apollo/Epstein/Kushner connections, ESWW shell company. |
| [WECHSLER_BLACK_TRUST_INVESTIGATION](financial/WECHSLER_BLACK_TRUST_INVESTIGATION.md) | Brad Wechsler (Elysium Management), J BLACK Trust **identified as Leon Black discretionary gift trust** (created April 2014 at Epstein's direction), $30.5M BV70 circular loan structure. DS9 yielded complete trust agreement chain. |
| [LUXURY_PURCHASES_ANALYSIS](financial/LUXURY_PURCHASES_ANALYSIS.md) | Luxury purchases, lifestyle spending, and high-value acquisitions analysis. |
| [WOW_GOLD_IGE_BANNON_SEARCH](financial/WOW_GOLD_IGE_BANNON_SEARCH.md) | NEGATIVE: Zero evidence of WoW gold / IGE / virtual currency money laundering across 3.5M+ records. |

### Named Individual Investigations (20 reports)

| Report | Description |
|--------|-------------|
| [LEON_BLACK_PROSECUTION_FAILURE](individuals/LEON_BLACK_PROSECUTION_FAILURE.md) | Complete prosecution failure timeline: SDNY + Manhattan DA failed to charge despite 4+ victims, FBI 302s, $62.5M USVI settlement. |
| [LUTNICK_DUBIN_INVESTIGATION](individuals/LUTNICK_DUBIN_INVESTIGATION.md) | Howard Lutnick (single NTOC tip, financial only) and Glen Dubin (54 documents, "lent out" testimony, Eva described as present, 34+ flights). |
| [WILLIAM_BARR_INVESTIGATION](individuals/WILLIAM_BARR_INVESTIGATION.md) | 55+ documents: NTOC tip, father hired Epstein at Dalton, Kirkland & Ellis conflict, split recusal, death investigation oversight. **Corrected:** OIG did publish its report in June 2023 (125+ pages located in DS9). Evan Barr (Fried Frank) distinguished from AG William Barr — separate individual with direct Epstein attorney-client relationship. |
| [RUEMMLER_DEEP_DIVE](individuals/RUEMMLER_DEEP_DIVE.md) | Former Obama White House Counsel: 29 documents, "Clinton Obama unnecessary implication" warning, career broker relationship through May 2019. |
| [SENATOR_MITCHELL_INVESTIGATION](individuals/SENATOR_MITCHELL_INVESTIGATION.md) | Former Senate Majority Leader: 4 evidentiary pillars, 2 independent victims, Groff/State Dept call, Mitchell's own admission. |
| [MITCHELL_CASCADE_INVESTIGATION](individuals/MITCHELL_CASCADE_INVESTIGATION.md) | David J. Mitchell (estate co-executor): $580.5K wires, fragmentation pattern, "Cascade" code name, Mandelson connection. Separate from Senator Mitchell. |
| [ROTHSCHILD_INVESTIGATION](individuals/ROTHSCHILD_INVESTIGATION.md) | Ariane de Rothschild's untraceable aderfam.ch channel. $25M in 2 wires bracketing EdR $45M DOJ penalty. Both $25M principals now dead. |
| [JUNKERMANN_MC2_INVESTIGATION](individuals/JUNKERMANN_MC2_INVESTIGATION.md) | Nicole Junkermann: 4,182 docs (expanded from 10+ in DS1-8), 10+ year relationship, Leon Black intro brokered, Jan 2019 island trip. MC2 stranding Russian girls in Milan, recruiting ages 13-20. |
| [MARCINKOVA_INVESTIGATION](individuals/MARCINKOVA_INVESTIGATION.md) | Nadia Marcinkova: near-zero results for full name in redaction databases (1 hit in DS10; may reflect effective redactions, first-name usage, or tool limitations). $100K Aviloop wire 2 days after Miami Herald. 124 flights. NPA protected. |
| [INVESTIGATION_1_BARR_NTOC](individuals/INVESTIGATION_1_BARR_NTOC.md) | William Barr NTOC filing deep dive -- forensic analysis of the tip and associated evidence. |
| [INVESTIGATION_5_MAXWELL_SSN](individuals/INVESTIGATION_5_MAXWELL_SSN.md) | Maxwell NYPD firearms permit anomalies: CT-prefix SSN, military/criminal record flags. |
| [INVESTIGATION_6_LEON_BLACK](individuals/INVESTIGATION_6_LEON_BLACK.md) | Leon Black: 47 EFTA docs, NTOC filing, HT Subject Referral, "DANY do not doubt her allegations." |
| [INVESTIGATION_8_UNEXPLORED_NAMES](individuals/INVESTIGATION_8_UNEXPLORED_NAMES.md) | 18 previously under-examined names: comprehensive forensic analysis. |
| [ALEXANDER_WANDTKE_NSALEM_INVESTIGATION](individuals/ALEXANDER_WANDTKE_NSALEM_INVESTIGATION.md) | Alexander brothers (currently on trial SDNY Jan 2026 for sex trafficking 60+ women), Max Wandtke (ghost), North Salem wedding evidence. |
| [RUSSIAN_WOMAN_SCOTT_IDENTIFICATION](individuals/RUSSIAN_WOMAN_SCOTT_IDENTIFICATION.md) | Identification attempt: woman likely Uzbek (WIUT), possibly "Nina K." (25+ docs). "Scott" unidentified. |
| [UNNAMED_PERSONS_INVESTIGATION](individuals/UNNAMED_PERSONS_INVESTIGATION.md) | Foreign president (Ehud Barak), AOL cluster, 34 journal names mapped, Wigdor corroboration. |
| [DUBAI_SULAYEM_INVESTIGATION](individuals/DUBAI_SULAYEM_INVESTIGATION.md) | Sultan bin Sulayem directed DP World SVP to contact Epstein's USVI attorney re "port of St Croix." Victim names "Sultan from Dubai." 40+ docs. |
| [KHANNA_SIX_NAMES_INVESTIGATION](individuals/KHANNA_SIX_NAMES_INVESTIGATION.md) | The six men whose names were redacted by the FBI and read onto the House floor by Rep. Ro Khanna on Feb 10, 2026: Nuara, Mikeladze, Leonov, Caputo, Sultan bin Sulayem, and Wexner. 20-person co-conspirator list analysis. |
| [JACQUI_SAFRA_INVESTIGATION](individuals/JACQUI_SAFRA_INVESTIGATION.md) | Jacob "Jacqui" Safra: Swiss billionaire (~$5B), Safra banking dynasty. 100+ EFTA docs via Brockman/Edge Foundation pipeline. Jerusalem "Sherover House" property negotiation, financial opportunity discussions. No criminal nexus. |

### International Investigations (1 report)

| Report | Description |
|--------|-------------|
| [FRENCH_CONNECTION_INVESTIGATION](FRENCH_CONNECTION_INVESTIGATION.md) | Epstein's operations in France: Jean-Luc Brunel/MC2/Karin Models recruitment pipeline, 22 Avenue Foch (SCI JEP), Jack Lang & Prytanee LLC $5.2M art vehicle, UN diplomat Fabrice Aidan brokering Gulf royalty meetings, conductor Frederic Chaslin, Deutsche Bank wires through Societe Generale and BNP Paribas. Written as a guide for French investigators. |

### Victim Analysis (4 reports)

| Report | Description |
|--------|-------------|
| [ALLRED_VICTIM_INTERVIEW](victims/ALLRED_VICTIM_INTERVIEW.md) | Complete 30-page FBI evidence package: victim met Epstein at 17, 4 assaults before 18, 2 rapes, harem ideology, Brunel companion. |
| [VICTIM_CENSUS](victims/VICTIM_CENSUS.md) | Minimum 60-80 individually identified victims, likely 200+, USVI civil suit says "hundreds." |
| [VICTIM_LEADS_VERIFICATION](victims/VICTIM_LEADS_VERIFICATION.md) | Re-verification of Leads 7-12 including major correction on flight log modification claim. |
| [TRAFFICKING_ROUTES_INVESTIGATION](victims/TRAFFICKING_ROUTES_INVESTIGATION.md) | Aircraft fleet, weekly cycling routes, MC2 recruitment ages 13-20, **corrected:** pilots did not retroactively add names to logs (explaining incomplete records), victim availability tracking, CBP bypass. |

### Evidence & Digital Forensics (11 reports)

| Report | Description |
|--------|-------------|
| [DEVICE_FORENSICS_COMPLETE](evidence/DEVICE_FORENSICS_COMPLETE.md) | 70+ devices, 2005 computer forensic image never examined by federal authorities (PBCSO may have examined the original), DVR failure 12 days pre-death, 6 machines unexported Oct 2020. |
| [PLIST_FORENSIC_SEARCH](evidence/PLIST_FORENSIC_SEARCH.md) | 460+ Apple Mail PLIST metadata documents, 2 email accounts, 9-year date range (2009-2018). |
| [PLIST_REDACTED_EMAILS_DEEP_DIVE](evidence/PLIST_REDACTED_EMAILS_DEEP_DIVE.md) | 12 failed redaction overlays exposing PLIST XML: Russian/Uzbek woman, neuroscience dinner, Groff calling State Dept for Mitchell. |
| [PLIST_TIMESTAMP_TRANSACTION_CORRELATION](evidence/PLIST_TIMESTAMP_TRANSACTION_CORRELATION.md) | 420 timestamps vs financial dates: Tudor $13.5M strongest correlation. **Note:** The "99-day blackout" originally reported here was corrected — DS9 shows continuous email activity. |
| [[EFTA00004800](https://www.justice.gov/epstein/files/DataSet%203/EFTA00004800.pdf)_DEEP_DIVE](evidence/EFTA00004800_DEEP_DIVE.md) | FBI "Book 17" evidence binder: 98 pages of CDs/DVDs, "grapes" files blacked out alongside CSAM, ~50+ unscanned media items. |
| [BLACKOUT_PERIOD_INVESTIGATION](evidence/BLACKOUT_PERIOD_INVESTIGATION.md) | Investigation of the Nov 2018 - Feb 2019 period. Originally reported as 99-day email silence, **corrected**: DS9 shows continuous email activity throughout. The gap was a PLIST extraction artifact. Epstein flew 8+ flights, paid $100K/$250K during this period. |
| [MAXWELL_FIREARMS_LICENSE_INVESTIGATION](evidence/MAXWELL_FIREARMS_LICENSE_INVESTIGATION.md) | Maxwell NYPD firearms license application investigation. |
| [EVIDENCE_COMPILATION](evidence/EVIDENCE_COMPILATION.md) | Master evidence table: named individuals with documented victim interactions and legal status. |
| [CORRUPTED_PDF_FORENSICS](evidence/CORRUPTED_PDF_FORENSICS.md) | **NEW:** Byte-level recovery of 5 "corrupted" DS9 PDFs. **Apple Address Book with 8 contacts** (Epstein attorney, known associates, Senegalese political figure, PI firm) + **iPhone 5s photo from Little Saint James, Aug 2014.** No prior public reporting. [Recovered files](recovered_corrupted_pdfs/github_release/) |
| [GABRIELLA_RICO_JIMENEZ_INVESTIGATION](evidence/GABRIELLA_RICO_JIMENEZ_INVESTIGATION.md) | NO connection found to Epstein. Jimenez incident Aug 2009 in Monterrey. ZERO hits across all document collections. |
| [FOUR_CHAN_PARAMEDIC_INVESTIGATION](evidence/FOUR_CHAN_PARAMEDIC_INVESTIGATION.md) | 4chan death leak: hard drives removed from SHU at 10:15 PM, guard DPAs then charges dismissed, FBI captured 8+ screenshots. |
| [ONLINE_EVIDENCE_INVESTIGATION](evidence/ONLINE_EVIDENCE_INVESTIGATION.md) | r/maxwellhill screenshot in FBI case serial, social media led to Maxwell via Borgerson-Angara-Tidewood shells. |

### Scientists & Academic Network (3 reports)

| Report | Description |
|--------|-------------|
| [SCIENCE_NETWORK_COMPREHENSIVE_AUDIT](scientists/SCIENCE_NETWORK_COMPREHENSIVE_AUDIT.md) | **NEW:** Full-corpus audit of 35+ scientists with Epstein connections. 10,000+ documents across uninvestigated individuals. FBI FinCEN investigation of Robert Trivers, 8 Nobel laureates, Biden's Science Advisor (Eric Lander), Global Viral/Metabiota founder (Nathan Wolfe), and mega-event guest lists. |
| [BIOTECH_SCIENCE_NETWORK_INVESTIGATION](scientists/BIOTECH_SCIENCE_NETWORK_INVESTIGATION.md) | Original biotech/science report: Brockman/Edge pipeline, Nowak ($6.5M), Chomsky (trust management), Hillis (Zorro Ranch), Krauss, Church, Lloyd, Ito, Boyden, Marsh. |
| [DAVID_SHAW_INVESTIGATION](scientists/DAVID_SHAW_INVESTIGATION.md) | D.E. Shaw & Co.: Limited exposure, proposed as dinner guest only. Science dinner network architecture mapped. |

### Intelligence Connections (3 reports)

**Key document: [EFTA00090314](https://www.justice.gov/epstein/files/DataSet%209/EFTA00090314.pdf)** — FBI Confidential Human Source report (FD-1023 format), filed under intelligence product case numbers ("INTELPRODS"). The CHS states that Epstein "belonged to both U.S. and allied intelligence services," "trained as a spy under" former Israeli PM Ehud Barak, and that "Mossad would then call Dershowitz to debrief" after Epstein-related calls. This is an unverified CHS report — not an FBI conclusion — but it is an official DOJ document preserved in the FBI case file. See [ISRAEL_DEEP_DIVE_V2](intelligence/ISRAEL_DEEP_DIVE_V2.md) Section B for full analysis.

| Report | Description |
|--------|-------------|
| [ISRAEL_DEEP_DIVE_V2](intelligence/ISRAEL_DEEP_DIVE_V2.md) | Definitive Israel report: Barak 3,756 docs, Carbyne 50 docs, Reporty 324 docs, 301 E 66th nexus, Kohn letters. **FBI CHS FD-1023 ([EFTA00090314](https://www.justice.gov/epstein/files/DataSet%209/EFTA00090314.pdf)) states Epstein "belonged to both U.S. and allied intelligence services" and "trained as a spy under" Barak.** Barak-Epstein exchange (Dec 2018): "you should make clear that i dont work for mossad :)" / "unfortunately, not." |
| [ISRAELI_INTELLIGENCE_DEEP_DIVE](intelligence/ISRAELI_INTELLIGENCE_DEEP_DIVE.md) | Initial Israeli intelligence connections investigation across all document collections. Revised: FD-1023 intelligence claims now documented; original "zero hits for Mossad" corrected. |
| [POWER_OVERLAP_SEALED_FILINGS_INVESTIGATION](intelligence/POWER_OVERLAP_SEALED_FILINGS_INVESTIGATION.md) | Power overlap, sealed filings, and evidence suppression patterns. 100+ searches across 4 document collections. Section 9.3 corrected: intelligence connection documented via CHS FD-1023 but unverified at FBI conclusion level. |

### Institutional Failures (6 reports)

| Report | Description |
|--------|-------------|
| [SECONDARY_BATES_STAMP_ANALYSIS](institutional/SECONDARY_BATES_STAMP_ANALYSIS.md) | **NEW:** The DOJ production contains secondary Bates stamps on 1.19M pages revealing six pre-production numbering systems. Gap analysis shows 1.46 million pages were reviewed and stamped but withheld — 57% of FBI device extractions and 75% of SDNY investigative files never made it into the public release. |
| [FBI_302_MISSING_SERIALS_DOSSIER](institutional/FBI_302_MISSING_SERIALS_DOSSIER.md) | **NEW:** The FBI's own indices list more interview records than were published. Cross-referencing three key documents identifies specific FD-302s produced to the Maxwell defense but absent from public files. Case study: 8 of 15 sub-records missing for one victim, including 3 of 4 FBI interview reports. |
| [PROSECUTION_FAILURES_ANALYSIS](institutional/PROSECUTION_FAILURES_ANALYSIS.md) | Comprehensive documentation of failed prosecutions: NPA architecture, blanket co-conspirator immunity expansion, Acosta deposition, CVRA violations, 15+ named individuals. |
| [CBP_CORRUPTION_INVESTIGATION](institutional/CBP_CORRUPTION_INVESTIGATION.md) | CBP officer **Timothy Routch** (Badge #CAS03223, **de-redacted via DS9**) self-incriminated, 7+ years clearing Epstein's aircraft at St. Thomas. FBI proffer sessions Oct-Nov 2020. |
| [CBP_RUEMMLER_REMAINING_LEADS](institutional/CBP_RUEMMLER_REMAINING_LEADS.md) | CBP officer expanded investigation, Ruemmler full 15-email trail, remaining unidentified leads. |
| [MIDNIGHT_911_CALL_INVESTIGATION](institutional/MIDNIGHT_911_CALL_INVESTIGATION.md) | CAD record anomalies at 358 El Brillo Way: Aug 21, 2002 midnight 911 call logged as "SICK PERSON/FIRST AID" — no narrative, no EMS, no disposition code. Five copies across four datasets all consistent in what they lack. |

### Art World (4 reports)

| Report | Description |
|--------|-------------|
| [ART_INVESTIGATION_COMPLETE](art/ART_INVESTIGATION_COMPLETE.md) | Unified art investigation: $30.5M auction proceeds, Leon Black $2.7B collection, 54 named art world figures, 100+ EFTA citations. 80KB, 72 sections. |
| [ART_INVESTIGATION_OCR_IMAGES](art/ART_INVESTIGATION_OCR_IMAGES.md) | Sub-report: 53 searches across OCR text and image records for art-related evidence. |
| [ART_INVESTIGATION_REDACTIONS](art/ART_INVESTIGATION_REDACTIONS.md) | Sub-report: 165 queries across 3.4M redaction records for art-related content. |
| [ART_INVESTIGATION_WEB_RESEARCH](art/ART_INVESTIGATION_WEB_RESEARCH.md) | Sub-report: 40+ web sources, 16 sections of open-source intelligence on Epstein art connections. |

### Methodology & Data Quality (13 reports)

| Report | Description |
|--------|-------------|
| [CORPUS_INVENTORY](methodology/CORPUS_INVENTORY.md) | **Complete evidence chain:** 1,380,937 PDFs, 2,731,785 pages, 194.5 GB across 12 datasets. Per-dataset accounting, derived databases, media inventory, processing pipeline, verification instructions. Start here to understand the source material. |
| [MISSING_EFTA_ANALYSIS](methodology/MISSING_EFTA_ANALYSIS.md) | Page-based gap detection across all 12 datasets. Exploits the EFTA numbering system (each page = one EFTA number) to account for every document. 31 gaps recovered from DOJ server or forensic carving; 4 confirmed as pages within multi-page PDFs via concordance files; 1 recovered from Wayback Machine after DOJ deleted it Dec 23, 2025. **All 2,731,783 EFTA page-numbers accounted for — 100% complete.** |
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
| [FACTUAL_ACCURACY_AUDIT](audits/FACTUAL_ACCURACY_AUDIT.md) | 225-issue factual accuracy audit across ~50 report files in 43 phases. Key corrections: Barrack acquittal (was listed as convicted), 99-day blackout disproved (DS9 shows continuous email), flight log modification claim inverted, legal conclusion language corrected throughout. |

### Internet Theories (3 reports)

| Report | Description |
|--------|-------------|
| [CONSPIRACY_THEORY_SEARCH_MISC](internet-theories/CONSPIRACY_THEORY_SEARCH_MISC.md) | Exhaustive search for miscellaneous internet theories across 218GB, 519,438 PDFs. |
| [CONSPIRACY_THEORY_SEARCH_OCCULT](internet-theories/CONSPIRACY_THEORY_SEARCH_OCCULT.md) | NEGATIVE: Zero evidence of satanic rituals, adrenochrome, or blood drinking across 3.5M+ records. |
| [CONSPIRACY_THEORY_SEARCH_PIZZAGATE](internet-theories/CONSPIRACY_THEORY_SEARCH_PIZZAGATE.md) | NEGATIVE: Zero evidence supporting Pizzagate or related theories across 519,438 PDFs. |

### Government Officials Corpus Search (7 reports)

Full-corpus search of all 537 current members of Congress (119th Congress), 77 executive branch officials, and 503 Article III federal judges (sourced from the Federal Judicial Center's biographical directory). Every name was searched as an exact quoted phrase across all 1,380,937 documents. Officials with significant hit counts received deeper context analysis to distinguish genuine connections from news mentions.

| Report | Description |
|--------|-------------|
| [DEMOCRAT_HOUSE](government-officials/DEMOCRAT_HOUSE.md) | 216 Democratic House members: 2 DIRECT connections (Plaskett, DeGette), 1 INVESTIGATION, 2 MIXED, 1 FALSE POSITIVE. |
| [DEMOCRAT_SENATE](government-officials/DEMOCRAT_SENATE.md) | 45 Democratic Senators: 2 MIXED (Schumer donation/return, Warner media project list). |
| [REPUBLICAN_HOUSE](government-officials/REPUBLICAN_HOUSE.md) | 221 Republican House members: 1 MIXED (Loudermilk — different person), 2 FALSE POSITIVES (John James, Scott Fitzgerald). |
| [REPUBLICAN_SENATE](government-officials/REPUBLICAN_SENATE.md) | 53 Republican Senators: 2 MIXED (McConnell declined donation, Rick Scott routine govt doc), 1 FALSE POSITIVE (Jim Justice). |
| [INDEPENDENT_SENATE](government-officials/INDEPENDENT_SENATE.md) | 2 Independent Senators (Sanders, King): news coverage only. |
| [EXECUTIVE_BRANCH](government-officials/EXECUTIVE_BRANCH.md) | 77 officials: 8 DIRECT connections (Musk, Bannon, Lutnick, Burns, Trump, Kushner, Rice, Monaco). Key finding: William Burns (future CIA Director) had direct email exchanges with Epstein in 2014 ([EFTA00869068](https://www.justice.gov/epstein/files/DataSet%209/EFTA00869068.pdf), [EFTA01748726](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01748726.pdf), [EFTA01001666](https://www.justice.gov/epstein/files/DataSet%209/EFTA01001666.pdf)); Epstein brokered a Burns-Thiel introduction ([EFTA02370150](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02370150.pdf)) and mentioned "bill gates in on the 5th" in a message to Burns ([EFTA01001666](https://www.justice.gov/epstein/files/DataSet%209/EFTA01001666.pdf)). |
| [JUDICIAL_BRANCH](government-officials/JUDICIAL_BRANCH.md) | 503 federal judges (all SCOTUS + 301 circuit + 191 key district): No SCOTUS justice has direct Epstein connection. Elena Kagan (58 docs) linked via Harvard poetry project Epstein funded. Stephanie Thacker (now 4th Circuit) was former CEOS deputy who formally criticized DOJ's Epstein case handling. |

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

### Prosecutorial Query Graph Dossiers (11 reports)

Structured analysis of 257 grand jury subpoenas, decomposed into 2,018 individual demand clauses, matched against production records, and scored for fulfillment. Built from `prosecutorial_query_graph.db`. See the [index](pqg_lines_of_investigation/00_INDEX.md) for methodology and summary statistics.

| Dossier | Description |
|---------|-------------|
| [00_INDEX](pqg_lines_of_investigation/00_INDEX.md) | Master index: 257 subpoenas, 2,018 demand clauses, 779 investigative gaps. 48.2% of subpoenas have no identifiable return in the corpus. |
| [01_TEMPORAL_BLACKOUT](pqg_lines_of_investigation/01_TEMPORAL_BLACKOUT.md) | The 524-day subpoena gap: why did the grand jury stop issuing subpoenas for 17 months (July 2017 - December 2018)? |
| [02_REDACTED_TARGETS](pqg_lines_of_investigation/02_REDACTED_TARGETS.md) | The 27 fully-redacted subpoena targets: who are the entities behind the blacked-out names? |
| [03_TECH_COMPANY_GAPS](pqg_lines_of_investigation/03_TECH_COMPANY_GAPS.md) | 21 subpoenas to technology companies; only 5 matched to identifiable returns. |
| [04_TRAVEL_RECORDS_GAP](pqg_lines_of_investigation/04_TRAVEL_RECORDS_GAP.md) | Travel records production gaps: airlines, FBOs, and charter companies. |
| [05_DEUTSCHE_BANK_COMPLIANCE](pqg_lines_of_investigation/05_DEUTSCHE_BANK_COMPLIANCE.md) | Deutsche Bank production analysis: what was demanded vs. what was produced. |
| [06_FINANCIAL_NO_RETURNS](pqg_lines_of_investigation/06_FINANCIAL_NO_RETURNS.md) | Financial institutions subpoenaed with no identifiable returns in the corpus. |
| [07_INDIVIDUAL_SUBPOENAS](pqg_lines_of_investigation/07_INDIVIDUAL_SUBPOENAS.md) | Individuals under subpoena: named persons served with grand jury demands. |
| [08_CRYPTO_DEAD_END](pqg_lines_of_investigation/08_CRYPTO_DEAD_END.md) | The cryptocurrency gap: subpoenas to crypto exchanges with no matched returns. |
| [09_CORRECTIONAL_DEATH_INVESTIGATION](pqg_lines_of_investigation/09_CORRECTIONAL_DEATH_INVESTIGATION.md) | Correctional records gaps and the death investigation: BOP, MCC, and medical examiner subpoenas. |
| [10_SCOPE_EVOLUTION](pqg_lines_of_investigation/10_SCOPE_EVOLUTION.md) | Prosecutorial scope evolution: how the investigation's focus shifted over time. |

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

**[NATIVE_FILES_CATALOG.csv](NATIVE_FILES_CATALOG.csv)** — Complete inventory of all 3,226 non-PDF native files (video, audio, spreadsheets, images) across the DOJ release. Each row includes: EFTA number, dataset, file extension, size, DOJ PDF link, transcription status, word count, duration, and description. Open in Excel or any spreadsheet application. Every non-PDF file has a corresponding PDF placeholder on DOJ; native files include 419 MCC surveillance videos (412+ hours), grand jury audio, prison phone calls, FBI interview recordings, and financial spreadsheets.

For the complete evidence chain -- what data exists, where it came from, and how to verify any finding -- see [CORPUS_INVENTORY](methodology/CORPUS_INVENTORY.md). For methodology details, data quality assessment, and reliability audits, see the [Methodology & Data Quality](#methodology--data-quality-12-reports) section above.

Processed data collection: https://github.com/rhowardstone/Epstein-research-data

---

## Community Platforms & Research Tools

See **[COMMUNITY_PLATFORMS.md](COMMUNITY_PLATFORMS.md)** for a comprehensive directory of 78+ platforms, tools, and resources for searching and analyzing the Epstein files. Includes government sources, search platforms, network visualization tools, AI/RAG tools, datasets, and community hubs.

---

## Processing Tools

All processing scripts (36+ Python tools) used to build the databases live in the data repo: **[Epstein-research-data/tools/](https://github.com/rhowardstone/Epstein-research-data/tree/main/tools)**

---

## Disclaimer

These reports constitute independent forensic analysis of publicly released government documents. They are not legal advice, not government publications, and not affiliated with any law enforcement agency. All findings are derived from documents released by the U.S. Department of Justice and are cited to specific EFTA document numbers that can be independently verified.

Where the evidence is ambiguous or inconclusive, that is stated explicitly. Where claims from prior reporting were found to be incorrect upon verification, corrections are documented (see Lead Verification reports). Negative findings (searches that returned zero results) are reported with equal rigor to positive findings.

This repository does not contain any original source documents, victim-identifying information, or classified material. It contains only analysis and citations.
