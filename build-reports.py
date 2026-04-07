#!/usr/bin/env python3
"""
Build static HTML reports from the epstein-research GitHub repo.
Reads markdown files, renders to HTML with site styling, generates index.

Usage:
    python3 build-reports.py [repo_dir] [output_dir]

Defaults:
    repo_dir:   /opt/datasette-data/reports-repo
    output_dir: /opt/datasette-data/reports-html
"""

import os, sys, re, html, subprocess, json
from pathlib import Path
from datetime import datetime, timezone
from email.utils import format_datetime

try:
    import markdown
except ImportError:
    print("Installing markdown library...")
    os.system(f"{sys.executable} -m pip install markdown")
    import markdown

REPO_DIR = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/opt/datasette-data/reports-repo")
OUT_DIR = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("/opt/datasette-data/reports-html")

# Category display names and order
CATEGORIES = {
    "overview": "Executive Summaries",
    "financial": "Financial Forensics",
    "individuals": "Individual Investigations",
    "evidence": "Evidence & Device Forensics",
    "congressional": "Congressional Briefings",
    "institutional": "Institutional Failures",
    "intelligence": "Intelligence Networks",
    "government-officials": "Government Officials",
    "victims": "Victim Census & Routes",
    "art": "Art Market Investigation",
    "internet-theories": "Internet Theories",
    "pqg_lines_of_investigation": "Prosecutorial Query Graph",
    "raw-dataset-analysis": "Dataset Analysis",
    "scientists": "Science Network",
    "methodology": "Methodology & Data Quality",
    "audits": "Factual Audits",
    "recovered_corrupted_pdfs": "Recovered Documents",
    "social-networks": "Social Network Analysis",
}

# Reports to feature on homepage — larger pool, JS picks random subset per visit
# Hand-written descriptions for homepage cards (auto-extraction is unreliable)
FEATURED = {
    "overview/MASTER_REPORT.md":
        "Consolidated findings from 2.73M pages across 12 DOJ datasets — financial networks, shell entities, key operators, and prosecution failures.",
    "financial/SHELL_ENTITY_MAP.md":
        "Complete map of 95+ shell entities under Deutsche Bank RM CODE 82289, compiled from 6 forensic sources.",
    "evidence/DEVICE_FORENSICS_COMPLETE.md":
        "Analysis of all digital devices seized from Epstein properties — phones, computers, hard drives, and server infrastructure.",
    "financial/FORENSIC_ACCT_2_MONEY_SOURCES.md":
        "Tracing the origins of Epstein's wealth through hidden text, extracted entities, and reconstructed financial pages.",
    "individuals/INVESTIGATION_6_LEON_BLACK.md":
        "Leon Black's $158M+ in payments to Epstein, Apollo Global Management ties, and three years of FBI investigation.",
    "internet-theories/CONSPIRACY_THEORY_SEARCH_PIZZAGATE.md":
        "Exhaustive search of 1.38M documents finds zero evidence for Pizzagate claims. Here's what the data actually shows.",
    "institutional/PROSECUTION_FAILURES_ANALYSIS.md":
        "Systematic pattern of prosecution failures spanning two decades — dropped leads, narrowed investigations, and buried evidence.",
    "overview/INSTITUTIONAL_FAILURE_NARRATIVE.md":
        "How a trafficking operation involving dozens of co-conspirators was allowed to function for over two decades.",
    "evidence/BLACKOUT_PERIOD_INVESTIGATION.md":
        "Investigation of the 99-day gap in Apple Mail metadata — flights, payments, and victim contacts during Nov 2018 – Feb 2019.",
    "financial/INVESTIGATION_2_DB_KYC_BREACH.md":
        "Deutsche Bank's internal compliance timeline — how KYC failures enabled years of suspicious transactions.",
    "intelligence/ISRAEL_DEEP_DIVE_V2.md":
        "Definitive analysis of Israeli connections within the 218GB DOJ corpus — Ehud Barak, defense contracts, and intelligence ties.",
    "intelligence/FBI_INTELLIGENCE_INVESTIGATIONS.md":
        "The FBI had at least five intelligence cases on Epstein — foreign intelligence, election influence, and external agency coordination at SECRET//ORCON//NOFORN.",
    "individuals/WILLIAM_BARR_INVESTIGATION.md":
        "William Barr in the FBI files — NTOC filing, recusal decisions, and MCC oversight during Epstein's final days.",
    "individuals/ROTHSCHILD_INVESTIGATION.md":
        "Multi-year relationship between Epstein and the Edmond de Rothschild banking group — trust structures and financial flows.",
    "financial/SHELL_ENTITY_DARK_MONEY_INVESTIGATION.md":
        "57 newly identified entities and money flow channels beyond the known 95+ entity map.",
    "victims/VICTIM_CENSUS.md":
        "Victim count compilation across 5 sources — FBI investigations, prosecution memos, Jane Doe designations, and NPA references.",
    "victims/TRAFFICKING_ROUTES_INVESTIGATION.md":
        "Multi-modal transportation network moving victims across state and international borders — flights, properties, and recruitment.",
    "evidence/PLIST_FORENSIC_SEARCH.md":
        "Apple Mail PLIST metadata extraction — email patterns, contact networks, and device forensic artifacts from seized computers.",
    "individuals/MITCHELL_CASCADE_INVESTIGATION.md":
        "David Mitchell — co-executor, trustee, real estate partner, and operator of the Life Hotel. 4,701 documents, $580K+ in wire transfers, and a 12:51 AM email about 'Cascade.'",
    "individuals/SENATOR_MITCHELL_INVESTIGATION.md":
        "Former Senate Majority Leader George Mitchell — victim allegations, flight evidence, financial connections, and public denials.",
    "financial/FORENSIC_ACCT_3_INTER_ENTITY_FLOWS.md":
        "Inter-entity fund flows across 19+ shell companies under Deutsche Bank — $319M in consolidated assets at peak.",
    "individuals/MARCINKOVA_INVESTIGATION.md":
        "Nadia Marcinkova's trajectory from alleged trafficking victim to licensed pilot — one of the most anomalous figures in the files.",
    "evidence/FOUR_CHAN_PARAMEDIC_INVESTIGATION.md":
        "The 4chan post 45 minutes before ABC News broke Epstein's death — verified timeline and evidence analysis.",
    "institutional/CBP_CORRUPTION_INVESTIGATION.md":
        "Customs and Border Protection failures — how Epstein's private flights evaded normal inspection protocols.",
    "institutional/MIDNIGHT_911_CALL_INVESTIGATION.md":
        "Midnight 911 call at 358 El Brillo Way (Aug 2002) — three CAD record anomalies: no narrative, no EMS dispatch, no disposition.",
    "congressional/CONGRESSIONAL_SUBPOENA_GUIDE.md":
        "64 witnesses, 426 EFTA citations, practical procedures — every subpoena target, every document demand, every obstacle and countermeasure for the House Oversight investigation.",
    "congressional/DEPOSITION_ANALYSIS_INDYKE.md":
        "What Epstein's personal attorney said under oath — 6.8 hours of sworn testimony analyzed against 2.77M pages. NPA co-conspirator input, computer hard drives with PIs, $725K structured cash, sham marriage admissions, and the 'Kool-Aid' moment.",
    "congressional/DEPOSITION_ANALYSIS_KAHN.md":
        "What Epstein's accountant said under oath — 5.9 hours of sworn testimony analyzed against 2.77M pages. Bill Gates visa letters, victim settlement carve-outs (Black, Staley), Forums LLC/Clinton, bank impersonation, and disputed Jane Doe 4 testimony.",
    "congressional/WITNESS_BRIEF_INDYKE.md":
        "Deposition prep for Darren K. Indyke — Epstein's personal attorney, co-executor, and trustee of a $577M estate. 70+ EFTA citations: $800K cash withdrawals, $12.6M IOLA trust, 13.7M ruble Moscow wire, witness tampering evidence, and 20 evidence-backed deposition questions.",
    "congressional/WITNESS_BRIEF_KAHN.md":
        "Deposition prep for Richard D. Kahn — Epstein's accountant, HBRK Associates co-principal, and co-executor. $159M in managed entity balances, $47.3M TD Bank SAR, $50K cash withdrawal, $23M to USVI escrow, the employment lock-in provision that silenced witnesses for two years, and 20 deposition questions.",
    "evidence/1B136_INVESTIGATION.md":
        "The FBI rushed 34 agents to review an 85 GB Epstein hard drive after congressional pressure — escalating to the Director, AG, and DAG. Then it left 10.5 terabytes of backup tapes untouched, citing warrant requirements. 44 source documents.",
    "institutional/ZORRO_RANCH_INVESTIGATION_HALT.md":
        "How SDNY prosecutors ordered New Mexico to cease its sex trafficking investigation into Zorro Ranch in July 2019 — one month before Epstein's death. No search warrant was ever executed. The ranch was not searched until March 2026.",
    "pqg_lines_of_investigation/00_INDEX.md":
        "257 grand jury subpoenas decomposed into 2,018 demand clauses — mapping what prosecutors asked for vs. what they received.",
    # Previously empty descriptions — ensure all reports have one
    "congressional/CONGRESSIONAL_FOLLOWUP_NEW_FINDINGS.md":
        "Critical documents uncovered in the full-corpus revisit of Datasets 9-12, absent from the original Congressional Reading Guide.",
    "art/ART_INVESTIGATION_OCR_IMAGES.md":
        "Art market forensics — Sotheby's, Christie's transactions, Leon Black's $1B+ collection, and the $558M estate inventory.",
    "audits/FACTUAL_ACCURACY_AUDIT.md":
        "Fact-check of investigation claims against source documents, prompted by Reddit moderator feedback.",
    "internet-theories/CONSPIRACY_THEORY_SEARCH_MISC.md":
        "Systematic search for miscellaneous internet conspiracy theories across all 1.38M documents. Each claim rated by evidence strength.",
    "government-officials/DEMOCRAT_HOUSE.md":
        "Full-corpus search results for all 216 Democratic U.S. House members — categorized by mention type and context.",
    "government-officials/DEMOCRAT_SENATE.md":
        "Full-corpus search results for all Democratic U.S. Senators — direct involvement, investigation references, and false positives.",
    "government-officials/EXECUTIVE_BRANCH.md":
        "Executive branch officials found in the Epstein files — Cabinet members, agency heads, and White House staff.",
    "government-officials/INDEPENDENT_SENATE.md":
        "Full-corpus search results for Independent U.S. Senators in the Epstein document corpus.",
    "government-officials/REPUBLICAN_HOUSE.md":
        "Full-corpus search results for all Republican U.S. House members — categorized by mention type and context.",
    "government-officials/REPUBLICAN_SENATE.md":
        "Full-corpus search results for all Republican U.S. Senators — direct references, investigation context, and media mentions.",
    "individuals/RUSSIAN_WOMAN_SCOTT_IDENTIFICATION.md":
        "Identifying the Russian/Eastern European woman and 'Scott' from Epstein's 2011 emails — rambler.ru traces and document cross-references.",
    "methodology/HIDDEN_TEXT_COMPLETE_REVIEW.md":
        "Complete review of text extracted from invisible OCR layers across all datasets — victim statements, financial records, and entity names.",
    "methodology/LEAD_VERIFICATION_PART1.md":
        "Re-verification of previously closed investigative leads against original source PDFs across four databases.",
    "raw-dataset-analysis/DS10_COMPREHENSIVE_NAME_SEARCH.md":
        "Name-by-name search across 434K DS10 records — the 'Prominent Names' internal FBI document and NTOC tip analysis.",
    "raw-dataset-analysis/DS10_KEY_DOCUMENTS_DEEP_DIVE.md":
        "Document-by-document extraction of key DS10 records including the FBI internal case briefing.",
    "raw-dataset-analysis/DS10_RECONSTRUCTED_PAGES.md":
        "Reconstructed page content from 1.8M redaction entries — spatial reordering of OCR fragments into readable pages.",
    "raw-dataset-analysis/DS8_NEW_LEADS.md":
        "New leads from Dataset 8 — witness tampering pleas, Prince Andrew threads, financial entities, and victim abuse patterns.",
    "raw-dataset-analysis/DS8_VERIFICATION.md":
        "Source document cross-referencing for DS8 claims — Maxwell firearms records, financial transfers, and embassy connections.",
    "overview/FINAL_INVESTIGATION_REPORT.md":
        "Prosecution-referral-grade summary of the entire 218GB corpus — 400+ EFTA citations across financial, trafficking, and institutional findings.",
    "art/ART_INVESTIGATION_COMPLETE.md":
        "Complete art market forensic compilation — 218+ queries across all databases plus open-source auction records and gallery connections.",
    "raw-dataset-analysis/DS10_FORENSIC_ANALYSIS.md":
        "Deep forensic analysis of the primary redaction database — 1.8M redactions, 107K entities, and 39K reconstructed pages.",
    # Batch 3: weak auto-extracted descriptions
    "raw-dataset-analysis/DS10_COMPLETE_FINDINGS.md":
        "Complete findings from Dataset 10 — the primary FBI investigation database with 503K documents spanning the full Epstein probe.",
    "individuals/KHANNA_SIX_NAMES_INVESTIGATION.md":
        "Investigation of six names disclosed in a key document — identity verification, cross-referencing, and significance assessment.",
    "individuals/ALEXANDER_WANDTKE_NSALEM_INVESTIGATION.md":
        "Tip investigation: Alexander Wandtke and the North Salem property connection — FBI intake records and follow-up analysis.",
    "financial/TRANSACTION_CHAIN_THIRD_PARTY_ART.md":
        "Third-party money flows through Epstein entities disguised as art transactions — auction records, gallery payments, and shell company routes.",
    "raw-dataset-analysis/DS10_INTERIM_FINDINGS.md":
        "Interim analysis of Dataset 10 during the initial full-corpus scan — key documents flagged for deep investigation.",
    "raw-dataset-analysis/DS8_CONTENT_SURVEY.md":
        "Content survey of Dataset 8 — DOJ/USAO internal communications, media files, and native spreadsheet records.",
    "raw-dataset-analysis/DS8_MEDIA_CATALOG.md":
        "Catalog of 11,034 media files in Dataset 8 — photographs, audio recordings, and video evidence across three directories.",
    "evidence/PLIST_TIMESTAMP_TRANSACTION_CORRELATION.md":
        "Correlating Apple Mail PLIST timestamps with financial transactions — 420 emails mapped against Deutsche Bank wire records.",
    "financial/WECHSLER_BLACK_TRUST_INVESTIGATION.md":
        "Wechsler and Black trust structures — email correspondence, payment arrangements, and fiduciary relationships with Epstein entities.",
    "overview/ANALYSIS_SUMMARY.md":
        "Summary of key analytical findings — SDNY prosecution memos, co-conspirator investigation scope, and evidence overview.",
    "methodology/DATA_QUALITY_AUDIT.md":
        "Data quality assessment of the extraction pipeline — overlay accuracy, OCR error rates, and character-level validation across all datasets.",
    "methodology/EVIDENCE_RELIABILITY_AUDIT.md":
        "Reliability audit of extracted evidence — source verification, framing corrections, and confidence ratings for key claims.",
    "individuals/UNNAMED_PERSONS_INVESTIGATION.md":
        "Investigation of unnamed individuals referenced in key victim testimony — cross-referenced against flight logs and financial records.",
    "victims/ALLRED_VICTIM_INTERVIEW.md":
        "FBI FD-340c evidence intake and victim interview records — attorney-facilitated disclosures and investigative follow-up documentation.",
    "scientists/DAVID_SHAW_INVESTIGATION.md":
        "David E. Shaw investigation — billionaire D.E. Shaw & Co. founder, financial ties to Epstein, and scientific funding network overlap.",
    "internet-theories/CONSPIRACY_THEORY_SEARCH_OCCULT.md":
        "Exhaustive search for occult and ritual abuse claims across 3.5M+ records and 4 databases. Evidence assessment for each theory.",
    "FRENCH_CONNECTION_INVESTIGATION.md":
        "Guide to EFTA corpus evidence for French investigators — the modeling pipeline, Avenue Foch, Jack Lang/Prytanee LLC, Fabrice Aidan, Frederic Chaslin, and Deutsche Bank financial flows.",
    "social-networks/REUBEN_BROTHERS_SIREN_CHERNOY.md":
        "David and Simon Reuben introduced to Epstein via Peggy Siegal in March 2010 — the same day a warning about Michael Chernoy arrived. Deutsche Bank flagged 'Reuben Brothers Ltd' as RED.",
    "social-networks/ST_BARTHS_2010_GUEST_LIST.md":
        "All 43 names on Peggy Siegal's Christmas 2010 St. Barths guest list searched across 2.7M pages — from Ghislaine Maxwell to Bobby Kotick, Harvey Weinstein to Jean Pigozzi.",
    "social-networks/PEGGY_SIEGAL_PIPELINE.md":
        "How Hollywood's premiere party planner became Epstein's social engineering pipeline — 10 confirmed introductions, dinner guest curation, Prince Andrew events, and a $100K birthday gift.",
    "social-networks/PIGOZZI_EDGE_FOUNDATION.md":
        "Jean Pigozzi and the Edge Foundation science dinners — 259 documents tracing crude exchanges about women, 76 exclusive dinners with Bezos/Gates/Brin, Maxwell testimony about Brin's birthday on Pigozzi's island, and Jean-Luc Brunel texting from Panama.",
    "social-networks/KOTICK_ACTIVISION.md":
        "Bobby Kotick's decade-long relationship with Epstein and Maxwell — 308 documents from flirtatious 2004 emails to dinners at 9 East 71st, an island invitation, and a SpaceX trip where Epstein forwarded a billionaire's home address to unnamed women.",
    "social-networks/GEFFEN_INVESTIGATION.md":
        "371 documents reveal Epstein as the social switchboard Bill Gates used to reach David Geffen — a two-year pursuit involving JPMorgan, Warren Buffett's office, and the St. Barths yacht circuit, all routed through a convicted sex offender.",
    "institutional/DOJ_DOCUMENT_ALTERATION_FORENSICS.md":
        "42,782 documents secretly re-processed after release — 146,190 entities stripped, FinCEN SARs gutted, three pages of Dershowitz deposition testimony blacked out. The DOJ's own Protocol reveals a dual-track redaction system that invokes the Privacy Act beyond the EFTA's five statutory categories.",
    "institutional/DOJ_DOCUMENT_REMOVAL_AUDIT.md":
        "78,234 documents silently removed from justice.gov — 10 case studies including BOP death records, FBI death investigation, Starr's lobbying fax, the grand jury outline, and 2,153 pages of phone records. Plus evidence of quiet partial restoration.",
    "institutional/STT_AVIATION_INFRASTRUCTURE_CONTROL.md":
        "Epstein's private aviation ecosystem at St. Thomas — shell entities, fuel wars, an FBO acquisition attempt, informants at the Jet Center, and the governor's wife leaking Port Authority intel. When Black Diamond Capital tried to buy the Jet Center, Epstein's pilot surveilled their Learjet within hours.",
    "institutional/DEA_OCDETF_INVESTIGATION.md":
        "A 69-page DEA target profile reveals 'Operation Chain Reaction' — 15 targets, $50M in suspicious transfers, 10 federal agencies. Cross-referenced against 2.73M pages: SLK Designs payroll shell (438 docs), Hyperion Air entity web (3,802 docs), unexplained Secret Service double-query, and Epstein's lawyer calling Angel Watch 89 days before arrest.",
    "institutional/USVI_FINANCIAL_SERVICES_LEGISLATION.md":
        "A 284-page financial services bill drafted by Epstein's private Wall Street attorney for the USVI Governor — designed to replicate Ireland's corporate tax structures in the Virgin Islands. Epstein forwarded the bill; Governor Mapp replied 'Got it, thanks.' The bill has never been reported.",
    "individuals/BARNABY_MARSH_INVESTIGATION.md":
        "A John Templeton Foundation executive managed an $11M grant to Harvard, structured co-funding with Epstein's shell entity Enhanced Education, and was named second-in-line successor trustee of a $577M estate. 2,831 documents across a decade of continuous contact.",
    "individuals/EMAD_HANNA_HBRK_INVESTIGATION.md":
        "HBRK Associates — the unreported operational hub managing 39+ entities across six properties. Richard Kahn's trajectory from 'Project Manager' to co-trustee of a $577M estate, the two-year employment lock-in, and $84.5M in managed accounts. 35,919 documents, zero media coverage.",
    "institutional/HELPFULEXPERTS_INVESTIGATION.md":
        "The first grand jury subpoena in the SDNY Epstein investigation targeted a ghost domain — helpfulexperts.com — under wire fraud statutes, 17 months before the publicly reported start of the investigation. A Google Workspace email domain registered since 2006 with zero internet footprint, still maintained as of December 2025.",
    "institutional/DEATH_INVESTIGATION_DOCUMENT_REMOVAL.md":
        "What 1,987 pages of removed federal records reveal about the investigation of Jeffrey Epstein's death — FBI witness interviews, BOP operational logs, incident reports, and the 18 camera hard drives seized from MCC. Two documents restored February 24, 2026; sixteen remain offline.",
    "institutional/GERMAN_FINANCIAL_NETWORK.md":
        "37,756 documents reveal Deutsche Bank's internal team, €30M in currency options while KYC was incomplete, the Sal. Oppenheim bank rescue play (with Jes Staley leaking JPMorgan intel), a €150M German steel financing pitch, and a Nobel laureate invited to lunch — the unreported institutional pipeline between Epstein and German finance.",
    "individuals/SHAHER_ABDULHAK_MR_EVIL_INVESTIGATION.md":
        "Identifying 'Mr. Evil' — the codename used across 57 documents for Yemeni billionaire Shaher Abdulhak. Epstein brokered meetings between Abdulhak and Steve Bannon to lobby on the Yemen War Powers Act, and pitched Abdulhak to Pompeo's State Department as someone who could flip Yemeni factions from Iran.",
    "individuals/ROBERT_TRIVERS_INVESTIGATION.md":
        "78 documents trace the decade-long dependency between one of the most influential evolutionary biologists since Darwin and a convicted sex offender — funding pipelines through shell entities, research direction control, the Chapman University expulsion, a private confession that it was 'a bit more than massages,' and a 2023 FBI FinCEN deconfliction request that no outlet has reported.",
    "institutional/VILLA_ARABESQUE_BOEING_727_INVESTIGATION.md":
        "The Jaffe family of Horseshoe Bay, Texas negotiated to buy the 'Lolita Express' Boeing 727 for $1.5M through Epstein's attorney Darren Indyke in 2016. Four years later, an anonymous FBI tip reported the same family's Acapulco villa for sex trafficking — but the Bureau closed the tip without connecting it to the Boeing 727 documents already in their own case file.",
    "institutional/EPSTEIN_STORAGE_UNITS_INVESTIGATION.md":
        "Seven storage facilities across Florida, New York, and New Jersey — holding computers removed before a search warrant, forensically cloned by the man at the center of the Bitcoin/Satoshi Nakamoto controversy, subpoenaed by a grand jury that never received them, and never searched by the FBI. Plus Maxwell's unreported River Edge, NJ units. Full merchant IDs and addresses for every facility.",
    "institutional/ITALIAN_CONNECTIONS_INVESTIGATION.md":
        "Three Italian threads across ~450 documents: Berlusconi political access via Osborne and 'Valentini' (the 'Mr. B isn't without his own issues' exchange), Bannon's 2018 Italy tour with Epstein as real-time political advisor, and Eduardo Teodorani-Fabbri — the Agnelli nephew who called Epstein 'Master' for eight years while serving as SVP at CNH Industrial. Plus the Elkann 'new target' cultivation strategy, Briatore/Maxwell's Sardinia circuit, and Epstein's direct role founding Hedosophia.",
    "institutional/SECONDARY_BATES_STAMP_ANALYSIS.md":
        "The DOJ production contains a hidden layer: secondary Bates stamps on 1.19 million pages revealing six pre-production numbering systems. Gap analysis of two trackable systems (FBI device extractions and SDNY production) shows 1.46 million pages were reviewed and stamped but withheld — 57% of FBI extractions and 75% of SDNY investigative files never made it into the public release. Includes JPMorgan, Deutsche Bank, and Maxwell case stamp pipelines.",
    "institutional/FBI_302_MISSING_SERIALS_DOSSIER.md":
        "The FBI's own indices within the EFTA production list more interview records than were actually published. Cross-referencing three key documents — the 136-interview serial index, the 63-page prosecution disclosure index, and the master serial log — identifies specific FD-302s that were produced to the Maxwell defense but never included in the public files. Case study: 8 of 15 sub-records missing for a single victim serial, including 3 of 4 FBI interview reports.",
    "individuals/PSEUDONYM_CODENAME_REGISTRY.md":
        "Every pseudonym, codename, email alias, and encrypted channel in the 2.77M-page corpus — 13 confirmed codenames, 85+ internet claims verified, 22 debunked with specific EFTA evidence, and 273 citations fact-checked against the database. Includes the Dr. Evil identification (Dr. Steven Victor), MEGAMELSY = Melanie Walker, MacGyver = Benjamin Brafman counter-analysis, Disney princess exchange, entity shells, plain-text passwords, and systematic debunking of Beefeater food codes and Sekolapedia conspiracy claims.",
    "individuals/BILL_CLINTON_INVESTIGATION.md":
        "How the Clinton-Epstein relationship actually functioned: Maxwell as intermediary, Band as operational counterpart, Epstein as diplomatic back-channel. The motorcade-to-plane pipeline, a $250K payment request routed through Maxwell, Google founders at Epstein's house vetted by Clinton's office, Ivory Coast military airbase access, and the coordinated January 2015 denial campaign. 41 EFTA citations, 6 unreported threads.",
    "individuals/MEDICAL_PROFESSIONALS_INVESTIGATION.md":
        "48 physicians, dentists, and medical providers across 23,000+ EFTA documents. The Moskowitz gonorrhea thread (mandated reporting evasion), Dr. Evil's $20K free-treatment pipeline, $725 hair consultations and Black Amex receipts for young women, the Columbia dental education pipeline, a psychiatrist sued by an Epstein accuser, zero medical subpoenas issued, and the Mount Sinai institutional network. Every claim cited to specific EFTA documents.",
}

SKIP_FILES = {
    "COMMUNITY_PLATFORMS.md",
    "scratchpad_maxwell_external_procurement_pipeline.md",
}
# Living documents that shouldn't show a publish date
NO_DATE_FILES = {
    "CLAUDE.md",
    "WRITING_GUIDE.md",
    "METHODOLOGY.md",
}
START_HERE_FILE = "README.md"  # Rendered as a prominent banner above categories


# Files moved between directories — preserve their original git dates
MOVED_FILES = {
    "evidence/FOUR_CHAN_PARAMEDIC_INVESTIGATION.md": "conspiracy-debunking/FOUR_CHAN_PARAMEDIC_INVESTIGATION.md",
    "evidence/ONLINE_EVIDENCE_INVESTIGATION.md": "conspiracy-debunking/ONLINE_EVIDENCE_INVESTIGATION.md",
    "internet-theories/CONSPIRACY_THEORY_SEARCH_MISC.md": "conspiracy-debunking/CONSPIRACY_THEORY_SEARCH_MISC.md",
    "internet-theories/CONSPIRACY_THEORY_SEARCH_OCCULT.md": "conspiracy-debunking/CONSPIRACY_THEORY_SEARCH_OCCULT.md",
    "internet-theories/CONSPIRACY_THEORY_SEARCH_PIZZAGATE.md": "conspiracy-debunking/CONSPIRACY_THEORY_SEARCH_PIZZAGATE.md",
    "scientists/DAVID_SHAW_INVESTIGATION.md": "individuals/DAVID_SHAW_INVESTIGATION.md",
    "scientists/BIOTECH_SCIENCE_NETWORK_INVESTIGATION.md": "intelligence/BIOTECH_SCIENCE_NETWORK_INVESTIGATION.md",
    "congressional/CONGRESSIONAL_FOLLOWUP_NEW_FINDINGS.md": "CONGRESSIONAL_FOLLOWUP_NEW_FINDINGS.md",
    "congressional/CONGRESSIONAL_READING_GUIDE.md": "CONGRESSIONAL_READING_GUIDE.md",
    "congressional/CONGRESS_RAW_EFTA_LIST.md": "CONGRESS_RAW_EFTA_LIST.md",
    "congressional/CONGRESSIONAL_ADDENDUM.md": "CONGRESSIONAL_ADDENDUM.md",
    "congressional/congressional_priority_list.md": "congressional_priority_list.md",
    "congressional/CONGRESSIONAL_SUBPOENA_GUIDE.md": "institutional/CONGRESSIONAL_SUBPOENA_GUIDE.md",
}

# Earliest provable dates for reports written before the 2026-02-18 bulk git push.
# Evidence: zip export timestamps (all 2026-02-12 07:23) + Python script mtimes (Feb 5).
# Files NOT listed here were added after Feb 12 and have accurate git dates.
DATE_OVERRIDES = {
    # --- 3 files provably existing by Feb 5 (referenced in Python scripts with that mtime) ---
    "raw-dataset-analysis/DS10_KEY_DOCUMENTS_DEEP_DIVE.md": "2026-02-05",
    "methodology/DEC2025_REDACTION_COMPARISON.md": "2026-02-05",
    "raw-dataset-analysis/DS10_ENTITY_EXTRACTION_REPORT.md": "2026-02-05",
    # --- All remaining files from the Feb 12 export zip ---
    "congressional/CONGRESSIONAL_FOLLOWUP_NEW_FINDINGS.md": "2026-02-12",
    "congressional/CONGRESSIONAL_READING_GUIDE.md": "2026-02-12",
    "congressional/CONGRESS_RAW_EFTA_LIST.md": "2026-02-12",
    "art/ART_INVESTIGATION_COMPLETE.md": "2026-02-12",
    "art/ART_INVESTIGATION_OCR_IMAGES.md": "2026-02-12",
    "art/ART_INVESTIGATION_REDACTIONS.md": "2026-02-12",
    "art/ART_INVESTIGATION_WEB_RESEARCH.md": "2026-02-12",
    "evidence/BLACKOUT_PERIOD_INVESTIGATION.md": "2026-02-12",
    "evidence/CORRUPTED_PDF_FORENSICS.md": "2026-02-12",
    "evidence/DEVICE_FORENSICS_COMPLETE.md": "2026-02-12",
    "evidence/EFTA00004800_DEEP_DIVE.md": "2026-02-12",
    "evidence/EVIDENCE_COMPILATION.md": "2026-02-12",
    "evidence/FOUR_CHAN_PARAMEDIC_INVESTIGATION.md": "2026-02-12",
    "evidence/GABRIELLA_RICO_JIMENEZ_INVESTIGATION.md": "2026-02-12",
    "evidence/MAXWELL_FIREARMS_LICENSE_INVESTIGATION.md": "2026-02-12",
    "evidence/ONLINE_EVIDENCE_INVESTIGATION.md": "2026-02-12",
    "evidence/PLIST_FORENSIC_SEARCH.md": "2026-02-12",
    "evidence/PLIST_REDACTED_EMAILS_DEEP_DIVE.md": "2026-02-12",
    "evidence/PLIST_TIMESTAMP_TRANSACTION_CORRELATION.md": "2026-02-12",
    "financial/DILORIO_APOLLO_WHISTLEBLOWER.md": "2026-02-12",
    "financial/FORENSIC_ACCT_1_HAZE_DRAWDOWN.md": "2026-02-12",
    "financial/FORENSIC_ACCT_2_MONEY_SOURCES.md": "2026-02-12",
    "financial/FORENSIC_ACCT_3_INTER_ENTITY_FLOWS.md": "2026-02-12",
    "financial/FORENSIC_ACCT_4_JABWCPA_INSTITUTION1.md": "2026-02-12",
    "financial/FORENSIC_ACCT_5_CALENDAR_CORRELATION.md": "2026-02-12",
    "financial/FORENSIC_ACCT_6_POST_DEATH_ASSETS.md": "2026-02-12",
    "financial/INVESTIGATION_2_DB_KYC_BREACH.md": "2026-02-12",
    "financial/INVESTIGATION_3_HAZE_TRUST_AML.md": "2026-02-12",
    "financial/INVESTIGATION_4_2018_WIRE_RECIPIENTS.md": "2026-02-12",
    "financial/INVESTIGATION_7_BARRETT_REPORTS.md": "2026-02-12",
    "financial/LUXURY_PURCHASES_ANALYSIS.md": "2026-02-12",
    "financial/SHELL_ENTITY_DARK_MONEY_INVESTIGATION.md": "2026-02-12",
    "financial/SHELL_ENTITY_MAP.md": "2026-02-12",
    "financial/TRANSACTION_CHAIN_AUCTION_TO_DESTINATION.md": "2026-02-12",
    "financial/TRANSACTION_CHAIN_BLACK_ART_MACHINE.md": "2026-02-12",
    "financial/TRANSACTION_CHAIN_THIRD_PARTY_ART.md": "2026-02-12",
    "financial/WECHSLER_BLACK_TRUST_INVESTIGATION.md": "2026-02-12",
    "financial/WOW_GOLD_IGE_BANNON_SEARCH.md": "2026-02-12",
    "government-officials/DEMOCRAT_HOUSE.md": "2026-02-12",
    "government-officials/DEMOCRAT_SENATE.md": "2026-02-12",
    "government-officials/EXECUTIVE_BRANCH.md": "2026-02-12",
    "government-officials/INDEPENDENT_SENATE.md": "2026-02-12",
    "government-officials/JUDICIAL_BRANCH.md": "2026-02-12",
    "government-officials/REPUBLICAN_HOUSE.md": "2026-02-12",
    "government-officials/REPUBLICAN_SENATE.md": "2026-02-12",
    "individuals/ALEXANDER_WANDTKE_NSALEM_INVESTIGATION.md": "2026-02-12",
    "individuals/DUBAI_SULAYEM_INVESTIGATION.md": "2026-02-12",
    "individuals/INVESTIGATION_1_BARR_NTOC.md": "2026-02-12",
    "individuals/INVESTIGATION_5_MAXWELL_SSN.md": "2026-02-12",
    "individuals/INVESTIGATION_6_LEON_BLACK.md": "2026-02-12",
    "individuals/INVESTIGATION_8_UNEXPLORED_NAMES.md": "2026-02-12",
    "individuals/JUNKERMANN_MC2_INVESTIGATION.md": "2026-02-12",
    "individuals/KHANNA_SIX_NAMES_INVESTIGATION.md": "2026-02-12",
    "individuals/LEON_BLACK_PROSECUTION_FAILURE.md": "2026-02-12",
    "individuals/LUTNICK_DUBIN_INVESTIGATION.md": "2026-02-12",
    "individuals/MARCINKOVA_INVESTIGATION.md": "2026-02-12",
    "individuals/MITCHELL_CASCADE_INVESTIGATION.md": "2026-02-12",
    "individuals/ROTHSCHILD_INVESTIGATION.md": "2026-02-12",
    "individuals/RUEMMLER_DEEP_DIVE.md": "2026-02-12",
    "individuals/RUSSIAN_WOMAN_SCOTT_IDENTIFICATION.md": "2026-02-12",
    "individuals/SENATOR_MITCHELL_INVESTIGATION.md": "2026-02-12",
    "individuals/UNNAMED_PERSONS_INVESTIGATION.md": "2026-02-12",
    "individuals/WILLIAM_BARR_INVESTIGATION.md": "2026-02-12",
    "institutional/CBP_CORRUPTION_INVESTIGATION.md": "2026-02-12",
    "institutional/CBP_RUEMMLER_REMAINING_LEADS.md": "2026-02-12",
    "institutional/PROSECUTION_FAILURES_ANALYSIS.md": "2026-02-12",
    "intelligence/ISRAELI_INTELLIGENCE_DEEP_DIVE.md": "2026-02-12",
    "intelligence/ISRAEL_DEEP_DIVE_V2.md": "2026-02-12",
    "intelligence/POWER_OVERLAP_SEALED_FILINGS_INVESTIGATION.md": "2026-02-12",
    "internet-theories/CONSPIRACY_THEORY_SEARCH_MISC.md": "2026-02-12",
    "internet-theories/CONSPIRACY_THEORY_SEARCH_OCCULT.md": "2026-02-12",
    "internet-theories/CONSPIRACY_THEORY_SEARCH_PIZZAGATE.md": "2026-02-12",
    "methodology/CORPUS_INVENTORY.md": "2026-02-12",
    "methodology/DATA_QUALITY_AUDIT.md": "2026-02-12",
    "methodology/DEFECTIVE_REDACTION_FINDINGS.md": "2026-02-12",
    "methodology/EVIDENCE_RELIABILITY_AUDIT.md": "2026-02-12",
    "methodology/HIDDEN_TEXT_COMPLETE_REVIEW.md": "2026-02-12",
    "methodology/LEAD_VERIFICATION_PART1.md": "2026-02-12",
    "methodology/LEAD_VERIFICATION_PART2.md": "2026-02-12",
    "methodology/LEAD_VERIFICATION_REPORT.md": "2026-02-12",
    "methodology/REDACTION_ASYMMETRY_ANALYSIS.md": "2026-02-12",
    "methodology/REDACTION_TEXT_LAYER_ANALYSIS.md": "2026-02-12",
    "overview/ANALYSIS_SUMMARY.md": "2026-02-12",
    "overview/FINAL_INVESTIGATION_REPORT.md": "2026-02-12",
    "overview/INSTITUTIONAL_FAILURE_NARRATIVE.md": "2026-02-12",
    "overview/MASTER_REPORT.md": "2026-02-12",
    "overview/PHASE1_GAP_DETECTION.md": "2026-02-12",
    "overview/PHASE2_LEVER_TRACEBACK.md": "2026-02-12",
    "overview/PHASE3_HIDDEN_DOMAINS.md": "2026-02-12",
    "overview/PHASE4_BRIEFING_KIT.md": "2026-02-12",
    "overview/SESSION9_MASTER_FINDINGS.md": "2026-02-12",
    "overview/UNEXPLORED_DOCUMENT_MINING.md": "2026-02-12",
    "raw-dataset-analysis/DS10_COMPLETE_FINDINGS.md": "2026-02-12",
    "raw-dataset-analysis/DS10_COMPREHENSIVE_NAME_SEARCH.md": "2026-02-12",
    "raw-dataset-analysis/DS10_FORENSIC_ANALYSIS.md": "2026-02-12",
    "raw-dataset-analysis/DS10_INTERIM_FINDINGS.md": "2026-02-12",
    "raw-dataset-analysis/DS10_RECONSTRUCTED_PAGES.md": "2026-02-12",
    "raw-dataset-analysis/DS8_CONTENT_SURVEY.md": "2026-02-12",
    "raw-dataset-analysis/DS8_MEDIA_CATALOG.md": "2026-02-12",
    "raw-dataset-analysis/DS8_NEW_LEADS.md": "2026-02-12",
    "raw-dataset-analysis/DS8_VERIFICATION.md": "2026-02-12",
    "recovered_corrupted_pdfs/README.md": "2026-02-12",
    "scientists/BIOTECH_SCIENCE_NETWORK_INVESTIGATION.md": "2026-02-12",
    "scientists/DAVID_SHAW_INVESTIGATION.md": "2026-02-12",
    "victims/ALLRED_VICTIM_INTERVIEW.md": "2026-02-12",
    "victims/TRAFFICKING_ROUTES_INVESTIGATION.md": "2026-02-12",
    "victims/VICTIM_CENSUS.md": "2026-02-12",
    "victims/VICTIM_LEADS_VERIFICATION.md": "2026-02-12",
}


def get_git_dates(repo_dir):
    """Get first-commit (added) date for each file via git log."""
    dates = {}
    try:
        result = subprocess.run(
            ["git", "log", "--diff-filter=A", "--format=%aI", "--name-only", "--", "*.md"],
            cwd=repo_dir, capture_output=True, text=True, timeout=30
        )
        lines = result.stdout.strip().split("\n")
        current_date = None
        for line in lines:
            line = line.strip()
            if not line:
                continue
            if line.startswith("20") and "T" in line:
                current_date = line  # Full ISO timestamp (e.g. 2026-02-26T07:09:37-05:00)
            elif current_date and line.endswith(".md"):
                dates[line] = current_date
    except Exception:
        pass
    # Fallback: for any .md file in repo without a date, use git log --follow to trace renames
    try:
        for md_path in sorted(Path(repo_dir).rglob("*.md")):
            rel = str(md_path.relative_to(repo_dir))
            if rel.startswith(".") or rel.startswith("_"):
                continue
            if rel not in dates and md_path.name not in NO_DATE_FILES:
                follow = subprocess.run(
                    ["git", "log", "--follow", "--format=%aI", "--diff-filter=A", "--", rel],
                    cwd=repo_dir, capture_output=True, text=True, timeout=10
                )
                for fline in follow.stdout.strip().split("\n"):
                    fline = fline.strip()
                    if fline.startswith("20") and "T" in fline:
                        dates[rel] = fline  # oldest add date via --follow
    except Exception:
        pass
    # Carry forward dates for files moved between directories
    for new_path, old_path in MOVED_FILES.items():
        if new_path not in dates and old_path in dates:
            dates[new_path] = dates[old_path]
    # Apply date overrides — earliest provable existence date takes precedence
    for path, override_date in DATE_OVERRIDES.items():
        override_iso = f"{override_date}T00:00:00-05:00"
        if path not in dates or dates[path][:10] > override_date:
            dates[path] = override_iso
    return dates

MD_EXTENSIONS = ["tables", "fenced_code", "toc", "nl2br", "sane_lists"]
MD_EXT_CONFIGS = {
    "toc": {"slugify": lambda value, separator: re.sub(
        r"[^\w\s-]", "", value.strip().lower()
    ).replace(" ", separator).strip(separator)}
}


def extract_title(md_text, filename):
    """Extract first heading or derive from filename."""
    m = re.search(r"^#\s+(.+)$", md_text, re.MULTILINE)
    if m:
        # Strip markdown formatting from title
        title = m.group(1).strip()
        title = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", title)  # [text](url) → text
        title = re.sub(r"\*\*(.+?)\*\*", r"\1", title)
        title = re.sub(r"\*(.+?)\*", r"\1", title)
        return title
    # Fallback: filename
    name = filename.replace("_", " ").replace("-", " ")
    name = re.sub(r"\.md$", "", name, flags=re.I)
    return name.title()


def extract_description(md_text, max_len=120):
    """Extract first meaningful paragraph as description."""
    # Try to find an Executive Summary section first — best source of descriptions
    exec_match = re.search(r"^##\s+(?:EXECUTIVE\s+)?SUMMARY\b.*?\n(.+?)(?:\n##|\n---|\Z)",
                           md_text, re.MULTILINE | re.DOTALL | re.IGNORECASE)
    if exec_match:
        # Use the executive summary section text instead
        section_text = exec_match.group(1).strip()
    else:
        section_text = md_text.strip()

    lines = section_text.split("\n")
    para = []
    started = False
    for line in lines:
        stripped = line.strip()
        if not started:
            if not stripped or stripped.startswith("#") or stripped.startswith("---"):
                continue
            if re.match(r"^[\[|>]", stripped):  # bracket, table row, blockquote
                continue
            if re.match(r"^[-*]\s", stripped):  # list item
                continue
            if re.match(r"^\d+\.\s", stripped):  # numbered list
                continue
            # Strip markdown bold/italic before checking
            plain = re.sub(r"\*+", "", stripped).strip()
            # Skip key:value metadata — colon within first 35 chars, 1-4 words before it
            colon_m = re.match(r"^([^:]{1,35}):\s", plain)
            if colon_m and len(colon_m.group(1).split()) <= 5:
                continue
            started = True
            para.append(stripped)
        else:
            if stripped == "" or stripped.startswith("#"):
                break
            para.append(stripped)
    text = " ".join(para)
    # Strip markdown formatting
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"\*(.+?)\*", r"\1", text)
    text = re.sub(r"`(.+?)`", r"\1", text)
    text = re.sub(r"\[(.+?)\]\(.+?\)", r"\1", text)
    if len(text) > max_len:
        text = text[:max_len].rsplit(" ", 1)[0] + "..."
    return text


def rewrite_efta_links(html_text):
    """Rewrite justice.gov EFTA PDF links to our viewer pages."""
    # Match href="https://www.justice.gov/epstein/files/DataSet%20NN/EFTA########.pdf"
    html_text = re.sub(
        r'href="https?://(?:www\.)?justice\.gov/epstein/files/DataSet%20\d+/(EFTA\d{8})\.pdf"',
        r'href="/\1"',
        html_text,
    )
    # Also catch variants without %20 (DataSet+N, DataSet_N, etc.)
    html_text = re.sub(
        r'href="https?://(?:www\.)?justice\.gov/epstein/files/DataSet[%_+\s]\d+/(EFTA\d{8})\.pdf"',
        r'href="/\1"',
        html_text,
    )
    return html_text


def linkify_efta(html_text):
    """Turn EFTA and HOUSE_OVERSIGHT numbers into links, skipping those already inside <a> tags."""
    result = []
    in_a = 0
    # Split HTML into tags vs text content
    parts = re.split(r"(<[^>]+>)", html_text)
    for part in parts:
        if part.startswith("<"):
            if re.match(r"<a[\s>]", part, re.I):
                in_a += 1
            elif re.match(r"</a>", part, re.I):
                in_a = max(0, in_a - 1)
            result.append(part)
        elif in_a > 0:
            # Inside an <a> tag — don't linkify
            result.append(part)
        else:
            # Plain text — safe to linkify (link to our viewer, not search)
            part = re.sub(
                r"\b(EFTA\d{8})\b",
                r'<a href="https://epstein-data.com/\1" target="_blank" rel="noopener">\1</a>',
                part,
            )
            part = re.sub(
                r"\b(HOUSE_OVERSIGHT_\d{6})\b",
                r'<a href="https://epstein-data.com/\1" target="_blank" rel="noopener">\1</a>',
                part,
            )
            result.append(part)
    return "".join(result)


def fix_efta_links(html_text):
    """Ensure all EFTA/HOUSE_OVERSIGHT viewer links open in a new tab."""
    # Match <a href="/EFTA..." or <a href="https://epstein-data.com/EFTA..." without target=
    html_text = re.sub(
        r'<a\s+href="(/(?:EFTA\d{8}|HOUSE_OVERSIGHT_\d{6}))"(?![^>]*target=)',
        r'<a href="\1" target="_blank" rel="noopener"',
        html_text,
    )
    html_text = re.sub(
        r'<a\s+href="(https://epstein-data\.com/(?:EFTA\d{8}|HOUSE_OVERSIGHT_\d{6}))"(?![^>]*target=)',
        r'<a href="\1" target="_blank" rel="noopener"',
        html_text,
    )
    return html_text


def fix_md_links(html_text, current_dir):
    """Rewrite .md links to .html links."""
    def replace_link(m):
        href = m.group(1)
        # Only rewrite relative .md links
        if href.startswith("http") or not href.endswith(".md"):
            return m.group(0)
        html_href = href[:-3] + ".html"
        return f'href="{html_href}"'
    return re.sub(r'href="([^"]+\.md)"', replace_link, html_text)


def format_date_display(git_date):
    """Format date for display. Bulk-push reports get 'February 2026', later ones get exact date."""
    if not git_date:
        return ""
    date_part = git_date[:10]  # YYYY-MM-DD from full ISO timestamp
    # The bulk push was 2026-02-18 — those reports were written earlier but we can't prove exact dates
    if date_part == "2026-02-18":
        return "February 2026"
    # For reports added after the bulk push, we have real git dates
    try:
        dt = datetime.strptime(date_part, "%Y-%m-%d")
        return dt.strftime("%B %-d, %Y")
    except (ValueError, TypeError):
        return ""


def render_report(md_text, title, description, category, category_label, rel_path, date_display="", git_date=""):
    """Render a report page."""
    md_obj = markdown.Markdown(extensions=MD_EXTENSIONS, extension_configs=MD_EXT_CONFIGS)
    body = md_obj.convert(md_text)
    body = rewrite_efta_links(body)
    body = linkify_efta(body)
    body = fix_efta_links(body)
    body = fix_md_links(body, os.path.dirname(rel_path))

    date_html = ""
    date_meta = ""
    if date_display:
        date_html = f'<div class="r-date">{html.escape(date_display)}</div>'
    if git_date:
        date_meta = f'<meta property="article:published_time" content="{html.escape(git_date)}">'

    # report_path for chat widget: "individuals/BILL_CLINTON_INVESTIGATION" (no .md)
    rp = rel_path.rsplit(".", 1)[0] if "." in rel_path else rel_path

    return REPORT_TEMPLATE.format(
        title=html.escape(title),
        description=html.escape(description or title),
        category=html.escape(category),
        category_label=html.escape(category_label),
        body=body,
        date_html=date_html,
        date_meta=date_meta,
        report_path=rp,
    )


def render_index(reports_by_cat, start_here=None):
    """Render the index page."""
    sections = ""
    # "Start Here" banner for README
    if start_here:
        sections += '<div class="ri-start-here">\n'
        sections += f'<a href="{html.escape(start_here["href"])}">\n'
        sections += '<span class="ri-start-label">Start Here</span>\n'
        sections += f'<span class="ri-start-title">{html.escape(start_here["title"])}</span>\n'
        if start_here.get("description"):
            sections += f'<span class="ri-start-desc">{html.escape(start_here["description"])}</span>\n'
        sections += '</a>\n</div>\n'
    for cat_key in CATEGORIES:
        if cat_key not in reports_by_cat:
            continue
        cat_label = CATEGORIES[cat_key]
        reports = sorted(reports_by_cat[cat_key], key=lambda r: r["title"])
        sections += f'<div class="ri-section" id="cat-{cat_key}">\n'
        sections += f'<h2><a href="#cat-{cat_key}" class="ri-section-link">{html.escape(cat_label)}<span class="ri-link-icon" title="Copy link to this section">#</span></a></h2>\n'
        sections += f'<div class="ri-grid">\n'
        for r in reports:
            desc = html.escape(r["description"]) if r["description"] else ""
            date_str = r.get("date_display", "")
            added = html.escape(r.get("git_date", ""))
            eftas = r.get("efta_count", 0)
            words = r.get("word_count", 0)
            sections += f'<a class="ri-card" href="{html.escape(r["href"])}" data-added="{added}" data-eftas="{eftas}" data-words="{words}" data-cat="{html.escape(cat_label)}">\n'
            sections += f'  <div class="ri-title">{html.escape(r["title"])}</div>\n'
            if desc:
                sections += f'  <div class="ri-desc">{desc}</div>\n'
            if date_str:
                sections += f'  <div class="ri-card-date">{html.escape(date_str)}</div>\n'
            sections += f'</a>\n'
        sections += f'</div>\n</div>\n'

    # Handle uncategorized
    for cat_key in sorted(reports_by_cat.keys()):
        if cat_key in CATEGORIES:
            continue
        cat_label = cat_key.replace("-", " ").replace("_", " ").title()
        reports = sorted(reports_by_cat[cat_key], key=lambda r: r["title"])
        sections += f'<div class="ri-section" id="cat-{cat_key}">\n'
        sections += f'<h2><a href="#cat-{cat_key}" class="ri-section-link">{html.escape(cat_label)}<span class="ri-link-icon" title="Copy link to this section">#</span></a></h2>\n'
        sections += f'<div class="ri-grid">\n'
        for r in reports:
            desc = html.escape(r["description"]) if r["description"] else ""
            date_str = r.get("date_display", "")
            added = html.escape(r.get("git_date", ""))
            eftas = r.get("efta_count", 0)
            words = r.get("word_count", 0)
            sections += f'<a class="ri-card" href="{html.escape(r["href"])}" data-added="{added}" data-eftas="{eftas}" data-words="{words}" data-cat="{html.escape(cat_label)}">\n'
            sections += f'  <div class="ri-title">{html.escape(r["title"])}</div>\n'
            if desc:
                sections += f'  <div class="ri-desc">{desc}</div>\n'
            if date_str:
                sections += f'  <div class="ri-card-date">{html.escape(date_str)}</div>\n'
            sections += f'</a>\n'
        sections += f'</div>\n</div>\n'

    return INDEX_TEMPLATE.format(
        sections=sections,
        count=sum(len(v) for v in reports_by_cat.values()),
        cat_count=len(reports_by_cat),
    )


# ===== Templates =====

REPORT_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — Epstein Files</title>
<meta property="og:title" content="{title} — Epstein Files">
<meta property="og:description" content="{description}">
<meta property="og:image" content="https://epstein-data.com/assets/og-card.png">
<meta property="og:type" content="article">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title} — Epstein Files">
<meta name="twitter:image" content="https://epstein-data.com/assets/og-card.png">
{date_meta}
<link rel="alternate" type="application/rss+xml" title="Epstein Files Reports" href="/reports/feed.xml">
<link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Work+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
:root {{
  --ink: #0c0f14; --paper: #f5f2ec; --paper-warm: #ece7dd;
  --accent: #8b2500; --muted: #7a756c; --muted-light: #a8a299;
  --border: #d6d0c5; --border-light: #e6e1d8; --white: #fefdfb;
  --seal-gold: #b8941a;
  --font-display: 'Work Sans', sans-serif;
  --font-body: 'Work Sans', sans-serif;
  --font-mono: 'DM Mono', monospace;
}}
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{ background: var(--paper); color: var(--ink); font-family: var(--font-body); }}
.r-topbar {{
  display: flex; align-items: center; justify-content: space-between;
  padding: 0.65rem 1.25rem; background: var(--ink); color: var(--paper);
  font-family: var(--font-mono); font-size: 0.68rem;
  letter-spacing: 0.12em; text-transform: uppercase;
}}
.r-topbar a {{ color: var(--paper); text-decoration: none; opacity: 0.85; }}
.r-topbar a:hover {{ opacity: 1; text-decoration: underline; }}
.r-topbar-home {{ opacity: 1 !important; font-weight: 500; letter-spacing: 0.08em; }}
.r-topbar-links {{ display: flex; align-items: center; gap: 0.4rem; }}
.r-topbar .bar-dot {{
  width: 4px; height: 4px; background: var(--seal-gold);
  border-radius: 50%; display: inline-block;
}}
.r-nav {{
  max-width: 820px; margin: 0 auto; padding: 1.25rem 1.5rem 0;
  font-size: 0.78rem; color: var(--muted);
  font-family: var(--font-body);
}}
.r-nav a {{ color: var(--accent); text-decoration: none; font-weight: 500; }}
.r-nav a:hover {{ text-decoration: underline; }}
.r-nav .sep {{ margin: 0 0.4rem; color: var(--border); }}
.r-content {{
  max-width: 820px; margin: 0 auto; padding: 1.5rem 1.5rem 3rem;
  font-size: 0.92rem; line-height: 1.75; color: #2a2520;
}}
.r-date {{
  max-width: 820px; margin: 0 auto; padding: 0.5rem 1.5rem 0;
  font-family: var(--font-mono); font-size: 0.68rem;
  color: var(--muted-light); letter-spacing: 0.04em;
}}
.r-ai-notice {{
  max-width: 820px; margin: 0 auto; padding: 0.4rem 1.5rem 0;
  font-family: var(--font-mono); font-size: 0.65rem;
  color: var(--muted-light); line-height: 1.5;
}}
.r-footer-disclaimer {{
  margin-top: 0.75rem; font-size: 0.7rem; color: #a8a299;
  line-height: 1.6; max-width: 600px; margin-left: auto; margin-right: auto;
}}
.r-content h1 {{
  font-family: var(--font-display); font-size: 1.6rem; font-weight: 600;
  color: var(--ink); margin: 0 0 1rem; line-height: 1.3;
  letter-spacing: -0.02em;
}}
.r-content h2 {{
  font-family: var(--font-display); font-size: 1.15rem; font-weight: 600;
  color: var(--ink); margin: 2rem 0 0.75rem;
  padding-bottom: 0.4rem; border-bottom: 1px solid var(--border-light);
}}
.r-content h3 {{
  font-family: var(--font-display); font-size: 1rem; font-weight: 600;
  color: var(--ink); margin: 1.5rem 0 0.5rem;
}}
.r-content h4 {{
  font-family: var(--font-display); font-size: 0.92rem; font-weight: 600;
  color: var(--muted); margin: 1.25rem 0 0.4rem;
  text-transform: uppercase; letter-spacing: 0.03em;
}}
.r-content p {{ margin: 0 0 1rem; }}
.r-content a {{ color: var(--accent); text-decoration: none; }}
.r-content a:hover {{ text-decoration: underline; }}
.r-content strong {{ font-weight: 600; color: var(--ink); }}
.r-content em {{ font-style: italic; }}
.r-content ul, .r-content ol {{ margin: 0 0 1rem 1.5rem; }}
.r-content li {{ margin: 0 0 0.4rem; }}
.r-content blockquote {{
  margin: 1rem 0; padding: 0.75rem 1.25rem;
  border-left: 3px solid var(--seal-gold); background: var(--paper-warm);
  color: var(--muted); font-style: italic;
}}
.r-content code {{
  font-family: var(--font-mono); font-size: 0.82rem;
  background: var(--paper-warm); padding: 1px 5px;
  border: 1px solid var(--border-light);
}}
.r-content pre {{
  background: var(--ink); color: var(--paper); padding: 1rem 1.25rem;
  overflow-x: auto; margin: 1rem 0; font-size: 0.78rem;
  font-family: var(--font-mono); line-height: 1.6;
}}
.r-content pre code {{
  background: none; border: none; padding: 0; color: inherit;
}}
.r-table-wrap {{
  overflow-x: auto; -webkit-overflow-scrolling: touch;
  margin: 1rem 0;
}}
.r-content table {{
  width: 100%; border-collapse: collapse;
  font-size: 0.84rem;
}}
.r-content th, .r-content td {{
  border: 1px solid var(--border-light); padding: 6px 10px; text-align: left;
  overflow-wrap: break-word; word-break: break-word;
}}
.r-content td {{ min-width: 60px; }}
.r-content th {{
  background: var(--paper-warm); font-weight: 600;
  font-family: var(--font-mono); font-size: 0.76rem;
  text-transform: uppercase; letter-spacing: 0.04em;
}}
.r-content hr {{
  border: none; border-top: 1px solid var(--border); margin: 2rem 0;
}}
.r-content img {{ max-width: 100%; height: auto; }}
.r-feedback {{
  max-width: 820px; margin: 0 auto; padding: 0 1.5rem 1.5rem;
}}
.r-feedback details {{ border: 1px solid var(--border-light); }}
.r-feedback summary {{
  cursor: pointer; padding: 0.6rem 1rem;
  font-family: var(--font-mono); font-size: 0.72rem;
  color: var(--muted); letter-spacing: 0.03em;
  text-transform: uppercase; user-select: none;
}}
.r-feedback summary:hover {{ color: var(--ink); }}
.r-feedback form {{
  padding: 0.75rem 1rem 1rem; border-top: 1px solid var(--border-light);
}}
.r-feedback input, .r-feedback textarea {{
  display: block; width: 100%; margin: 0 0 0.5rem;
  padding: 0.45rem 0.6rem; border: 1px solid var(--border);
  background: var(--white); color: var(--ink);
  font-family: var(--font-body); font-size: 0.84rem;
  line-height: 1.5; resize: vertical;
}}
.r-feedback input:focus, .r-feedback textarea:focus {{
  outline: none; border-color: var(--accent);
}}
.r-feedback .cf-row {{ display: flex; align-items: center; gap: 0.75rem; }}
.r-feedback button {{
  padding: 0.4rem 1.1rem; border: 1px solid var(--ink);
  background: var(--ink); color: var(--paper);
  font-family: var(--font-mono); font-size: 0.72rem;
  letter-spacing: 0.06em; text-transform: uppercase;
  cursor: pointer;
}}
.r-feedback button:hover {{ background: #1a1f2e; }}
#cf-status {{
  font-family: var(--font-mono); font-size: 0.72rem; color: var(--muted);
}}
.r-footer {{
  text-align: center; padding: 2rem 1rem; border-top: 1px solid var(--border);
  font-size: 0.72rem; color: var(--muted); font-family: var(--font-mono);
}}
.r-footer a {{ color: var(--muted); text-decoration: none; margin: 0 10px; }}
.r-footer a:hover {{ color: var(--ink); }}
@media (max-width: 600px) {{
  .r-content {{ padding: 1rem; font-size: 0.95rem; line-height: 1.8; }}
  .r-content h1 {{ font-size: 1.3rem; }}
  .r-content h2 {{ font-size: 1.05rem; }}
  .r-content table {{ font-size: 0.8rem; display: table; width: 100%; table-layout: auto; }}
  .r-content th, .r-content td {{ padding: 5px 8px; word-break: break-word; }}
  .r-table-wrap {{ overflow-x: visible; }}
  .r-topbar {{ font-size: 0.6rem; }}
  .r-nav {{ font-size: 0.7rem; padding: 1rem 1rem 0; }}
}}
/* Content recentering when chat panel opens */
.r-content, .r-nav, .r-date, .r-feedback {{ transition: margin-right 0.25s ease; }}
body.chat-open .r-content,
body.chat-open .r-nav,
body.chat-open .r-date,
body.chat-open .r-feedback {{ margin-right: 380px; }}
/* Chat toggle button */
.r-chat-toggle {{
  position: fixed; bottom: 24px; right: 24px; z-index: 1000;
  width: 48px; height: 48px; border-radius: 50%;
  background: var(--ink); color: var(--paper); border: none;
  cursor: pointer; box-shadow: 0 2px 12px rgba(0,0,0,0.2);
  display: flex; align-items: center; justify-content: center;
  transition: background 0.15s, transform 0.15s;
}}
.r-chat-toggle:hover {{ background: #1a1f2e; transform: scale(1.05); }}
.r-chat-toggle svg {{ width: 22px; height: 22px; fill: currentColor; }}
/* Chat side panel */
.r-chat-panel {{
  position: fixed; top: 0; right: -380px; z-index: 1001;
  width: 360px; height: 100vh;
  background: var(--paper); border-left: 1px solid var(--border);
  display: flex; flex-direction: column;
  transition: right 0.25s ease;
  box-shadow: -4px 0 24px rgba(0,0,0,0.08);
}}
.r-chat-panel.open {{ right: 0; }}
.r-chat-header {{
  display: flex; align-items: center; justify-content: space-between;
  padding: 0.75rem 1rem; background: var(--ink); color: var(--paper);
  font-family: var(--font-mono); font-size: 0.72rem;
  letter-spacing: 0.06em; text-transform: uppercase;
  flex-shrink: 0;
}}
.r-chat-close {{
  background: none; border: none; color: var(--paper);
  font-size: 1.4rem; cursor: pointer; padding: 0 4px;
  line-height: 1; opacity: 0.7;
}}
.r-chat-close:hover {{ opacity: 1; }}
/* Chat messages area */
.r-chat-messages {{
  flex: 1; overflow-y: auto; padding: 1rem;
  display: flex; flex-direction: column; gap: 0.5rem;
}}
.r-chat-hint {{
  font-family: var(--font-mono); font-size: 0.72rem;
  color: var(--muted-light); text-align: center;
  line-height: 1.5; padding: 1rem 0;
}}
.r-chat-msg {{
  padding: 0.6rem 0.8rem; font-size: 0.82rem;
  line-height: 1.6; word-break: break-word;
}}
.r-chat-msg-user {{
  background: var(--ink); color: var(--paper);
  align-self: flex-end; max-width: 90%; font-weight: 500;
}}
.r-chat-msg-assistant {{
  background: var(--white); border: 1px solid var(--border);
}}
.r-chat-msg-assistant p {{ margin: 0 0 0.5rem; }}
.r-chat-msg-assistant p:last-of-type {{ margin: 0; }}
.r-chat-msg-assistant strong {{ font-weight: 600; }}
.r-chat-msg-assistant a {{ color: var(--accent); text-decoration: none; }}
.r-chat-msg-assistant a:hover {{ text-decoration: underline; }}
.r-chat-msg-assistant blockquote {{
  border-left: 3px solid var(--border); padding: 0.4rem 0.8rem;
  color: var(--muted); font-style: italic; margin: 0.4rem 0;
}}
.r-chat-msg-assistant h2 {{ font-size: 0.88rem; font-weight: 600; margin: 0.6rem 0 0.3rem; }}
.r-chat-msg-assistant h3 {{ font-size: 0.84rem; font-weight: 600; margin: 0.5rem 0 0.2rem; }}
.r-chat-msg-assistant ul, .r-chat-msg-assistant ol {{ margin: 0.3rem 0 0.5rem 1rem; }}
.r-chat-msg-assistant li {{ margin: 0 0 0.2rem; }}
.r-chat-msg-assistant code {{
  font-family: var(--font-mono); font-size: 0.75rem;
  background: var(--paper-warm); padding: 1px 4px; border: 1px solid var(--border-light);
}}
.r-chat-msg-assistant table {{
  width: 100%; border-collapse: collapse; margin: 0.5rem 0; font-size: 0.75rem;
}}
.r-chat-msg-assistant th, .r-chat-msg-assistant td {{
  border: 1px solid var(--border-light); padding: 3px 6px; text-align: left;
}}
.r-chat-msg-assistant th {{ background: var(--paper); font-weight: 600; font-size: 0.7rem; }}
/* Chat sources */
.r-chat-sources {{
  font-size: 0.66rem; font-family: var(--font-mono);
  margin: 0.5rem 0 0; padding: 0.5rem;
  background: var(--paper); border: 1px solid var(--border-light);
  display: flex; flex-wrap: wrap; gap: 0.2rem 0.5rem;
}}
.r-chat-sources-label {{
  text-transform: uppercase; letter-spacing: 0.06em;
  color: var(--muted); font-weight: 500; width: 100%; margin-bottom: 0.2rem;
}}
.r-chat-sources a {{ color: var(--accent); text-decoration: none; white-space: nowrap; }}
.r-chat-sources a:hover {{ text-decoration: underline; }}
/* Chat model label */
.r-chat-model {{
  font-family: var(--font-mono); font-size: 0.58rem;
  color: var(--muted-light); text-align: right; margin: 0.3rem 0 0;
}}
/* Chat status indicator */
.r-chat-status {{
  font-family: var(--font-mono); font-size: 0.68rem; color: var(--muted);
  display: flex; align-items: center; gap: 0.4rem; padding: 0.3rem 0;
}}
.r-chat-status .dot {{
  width: 5px; height: 5px; background: var(--seal-gold);
  border-radius: 50%; animation: pulse 1.2s ease-in-out infinite;
}}
@keyframes pulse {{ 0%,100% {{ opacity: 0.3; }} 50% {{ opacity: 1; }} }}
/* Chat input area */
.r-chat-input-area {{ flex-shrink: 0; padding: 0.5rem; border-top: 1px solid var(--border-light); }}
.r-chat-input-wrap {{
  display: flex; border: 1px solid var(--border); background: var(--white);
  transition: border-color 0.2s;
}}
.r-chat-input-wrap:focus-within {{ border-color: var(--ink); box-shadow: 0 0 0 1px var(--ink); }}
.r-chat-input {{
  flex: 1; padding: 10px 12px; border: none; outline: none;
  background: transparent; font-family: var(--font-body); font-size: 0.85rem;
  color: var(--ink); resize: none; min-height: 42px; max-height: 120px;
  line-height: 1.5;
}}
.r-chat-input::placeholder {{ color: var(--muted-light); font-style: italic; }}
.r-chat-send {{
  padding: 8px 16px; margin: 3px; background: var(--ink); color: var(--paper);
  border: none; font-family: var(--font-mono); font-size: 0.72rem;
  letter-spacing: 0.06em; text-transform: uppercase; cursor: pointer;
  align-self: flex-end; transition: background 0.15s;
}}
.r-chat-send:hover {{ background: #1a1f2e; }}
.r-chat-send:disabled {{ opacity: 0.4; cursor: not-allowed; }}
/* Mobile: bottom sheet instead of side panel */
@media (max-width: 768px) {{
  .r-chat-panel {{
    position: fixed; bottom: -100vh; left: 0; right: 0;
    width: 100%; height: 55vh; top: auto;
    border-left: none; border-top: 1px solid var(--border);
    transition: bottom 0.3s ease;
  }}
  .r-chat-panel.open {{ bottom: 0; right: 0; }}
  body.chat-open .r-content,
  body.chat-open .r-nav,
  body.chat-open .r-date,
  body.chat-open .r-feedback {{ margin-right: 0; }}
  .r-chat-toggle {{ bottom: 16px; right: 16px; width: 44px; height: 44px; }}
  .r-chat-msg {{ font-size: 0.85rem; }}
  .r-chat-messages {{ padding: 0.75rem; }}
}}
</style>
</head>
<body>
<div class="r-topbar">
  <a href="/" class="r-topbar-home">Home</a>
  <div class="r-topbar-links">
    <a href="https://www.congress.gov/119/plaws/publ38/PLAW-119publ38.htm" target="_blank">EFTA</a>
    <span class="bar-dot"></span>
    <a href="https://www.justice.gov/epstein/doj-disclosures" target="_blank">DOJ Production</a>
  </div>
</div>
<nav class="r-nav">
  <a href="/">Home</a>
  <span class="sep">/</span>
  <a href="/reports/">Reports</a>
  <span class="sep">/</span>
  <a href="/reports/#cat-{category}">{category_label}</a>
  <span class="sep">/</span>
  <span>{title}</span>
</nav>
{date_html}
<div class="r-ai-notice">AI-generated report (Claude, Anthropic) &mdash; iteratively fact-checked against source documents but may contain errors. Verify claims against linked EFTA sources before citing. No affiliation with Anthropic.</div>
<article class="r-content">
{body}
</article>
<div class="r-feedback">
  <details>
    <summary>Flag an error or leave a note</summary>
    <form id="cf" autocomplete="off">
      <input type="text" id="cf-name" placeholder="Name (optional)" maxlength="100">
      <textarea id="cf-body" placeholder="Spotted an error? Have additional context? Let us know." maxlength="5000" rows="3" required></textarea>
      <div class="cf-row">
        <button type="submit">Submit</button>
        <span id="cf-status"></span>
      </div>
    </form>
  </details>
</div>
<div class="r-footer">
  <a href="https://github.com/rhowardstone/Epstein-research-data/">Source Data</a>
  <a href="/reports/">Investigation Reports</a>
  <a href="/reports/feed.xml">RSS Feed</a>
  <a href="https://www.justice.gov/epstein">DOJ EFTA</a>
  <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">CC BY-NC-SA 4.0</a>
  <a href="https://docs.google.com/forms/d/e/1FAIpQLSdY9gkq3z2VsSjdGnOehFsRcqhX29lC0Knr9Lx_uSAo0W5PSg/viewform" target="_blank">Feedback</a>
  <div class="r-footer-disclaimer">
    Independent research project. Not affiliated with the U.S. Department of Justice, FBI, any government agency, or Anthropic. All reports are AI-generated (Claude, Anthropic) and iteratively fact-checked against source documents, but may contain errors.
  </div>
  <div style="margin-top:0.75rem;color:#a8a299;">
    Powered by <a href="https://datasette.io/">Datasette</a>
    &ensp;&middot;&ensp;
    <a href="https://ko-fi.com/rhowardstone">Support this project</a>
  </div>
</div>
<script>
navigator.sendBeacon&&navigator.sendBeacon('/api/hit?p='+encodeURIComponent(location.pathname));
document.querySelectorAll('.r-content table').forEach(function(t){{
  var w=document.createElement('div');w.className='r-table-wrap';
  t.parentNode.insertBefore(w,t);w.appendChild(t);
}});
(function(){{
  var f=document.getElementById('cf'),s=document.getElementById('cf-status');
  if(!f)return;
  f.addEventListener('submit',function(e){{
    e.preventDefault();
    var body=document.getElementById('cf-body').value.trim();
    if(!body)return;
    s.textContent='Sending...';s.style.color='var(--muted)';
    fetch('/api/comment',{{
      method:'POST',
      headers:{{'Content-Type':'application/json'}},
      body:JSON.stringify({{
        page:location.pathname,
        name:document.getElementById('cf-name').value.trim(),
        text:body
      }})
    }}).then(function(r){{
      if(r.ok){{
        s.textContent='Thank you!';s.style.color='var(--accent)';
        document.getElementById('cf-body').value='';
        document.getElementById('cf-name').value='';
      }}else if(r.status===429){{
        s.textContent='Please wait before submitting again.';s.style.color='var(--accent)';
      }}else{{
        s.textContent='Error — please try the Feedback link below.';s.style.color='var(--accent)';
      }}
    }}).catch(function(){{
      s.textContent='Network error.';s.style.color='var(--accent)';
    }});
  }});
}})();
</script>
<button class="r-chat-toggle" id="r-chat-toggle" title="Ask about this report">
  <svg viewBox="0 0 24 24"><path d="M20 2H4c-1.1 0-2 .9-2 2v18l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zm0 14H5.2L4 17.2V4h16v12z"/></svg>
</button>
<div class="r-chat-panel" id="r-chat-panel">
  <div class="r-chat-header">
    <span>Ask about this report</span>
    <button class="r-chat-close" id="r-chat-close">&times;</button>
  </div>
  <div class="r-chat-messages" id="r-chat-messages">
    <p class="r-chat-hint">Ask a question &mdash; the AI has the full report loaded and can also search the full corpus.</p>
  </div>
  <div class="r-chat-input-area">
    <div class="r-chat-input-wrap">
      <textarea class="r-chat-input" id="r-chat-input" placeholder="Ask about this report&hellip;" rows="1"></textarea>
      <button class="r-chat-send" id="r-chat-send">Ask</button>
    </div>
  </div>
</div>
<script src="https://cdn.jsdelivr.net/npm/marked@15.0.7/marked.min.js"></script>
<script>
(function(){{
  var REPORT_PATH = '{report_path}';
  var toggle = document.getElementById('r-chat-toggle');
  var panel = document.getElementById('r-chat-panel');
  var closeBtn = document.getElementById('r-chat-close');
  var input = document.getElementById('r-chat-input');
  var sendBtn = document.getElementById('r-chat-send');
  var messagesEl = document.getElementById('r-chat-messages');
  var allMessages = [];
  var busy = false;

  // --- EFTA linking (same as /ask page) ---
  var EFTA_RANGES = [
    [1, 3158, 1], [3159, 3857, 2], [3858, 5586, 3], [5705, 8320, 4],
    [8409, 8528, 5], [8529, 8998, 6], [9016, 9664, 7], [9676, 39023, 8],
    [39025, 1262781, 9], [1262782, 2205654, 10], [2205655, 2730264, 11],
    [2730265, 2731783, 12]
  ];
  function eftaDataset(num) {{
    for (var i = 0; i < EFTA_RANGES.length; i++) {{
      if (num >= EFTA_RANGES[i][0] && num <= EFTA_RANGES[i][1]) return EFTA_RANGES[i][2];
    }}
    for (var i = EFTA_RANGES.length - 1; i >= 0; i--) {{
      if (num > EFTA_RANGES[i][1]) return EFTA_RANGES[i][2];
    }}
    return null;
  }}
  function eftaDojUrl(efta) {{
    var num = parseInt(efta.replace('EFTA', ''), 10);
    var ds = eftaDataset(num);
    if (!ds) return null;
    return 'https://www.justice.gov/epstein/files/DataSet%20' + ds + '/' + efta + '.pdf';
  }}

  // --- Markdown rendering with EFTA auto-linking ---
  marked.setOptions({{ breaks: true, gfm: true }});
  function renderMd(text) {{
    text = text.replace(/\bEFTA\s+(\d{{8}})\b/g, 'EFTA$1');
    var h = marked.parse(text);
    h = h.replace(/\b(EFTA(\d{{8}}))\b/g, function(m, full, digits) {{
      return '<a href="/' + full + '" title="View in document viewer">' + full + '</a>';
    }});
    h = h.replace(/\b(HOUSE_OVERSIGHT_\d{{6}})\b/g, function(m) {{
      return '<a href="/' + m + '">' + m + '</a>';
    }});
    return h;
  }}

  // --- Sources block builder ---
  function buildSourcesEl(sources) {{
    var srcDiv = document.createElement('div');
    srcDiv.className = 'r-chat-sources';
    var label = document.createElement('div');
    label.className = 'r-chat-sources-label';
    label.textContent = 'Source Documents (' + sources.length + ')';
    srcDiv.appendChild(label);
    var seen = {{}};
    sources.forEach(function(s) {{
      if (s.link) {{
        var a = document.createElement('a');
        a.href = s.link;
        a.textContent = s.source;
        srcDiv.appendChild(a);
        return;
      }}
      if (!s.bates || seen[s.bates]) return;
      seen[s.bates] = true;
      var a = document.createElement('a');
      var dojUrl = s.bates.startsWith('EFTA') ? eftaDojUrl(s.bates) : null;
      a.href = dojUrl || ('/?q=' + encodeURIComponent(s.bates));
      if (dojUrl) {{ a.target = '_blank'; a.rel = 'noopener'; a.title = 'View PDF at justice.gov'; }}
      a.textContent = s.bates;
      if (s.page) a.textContent += ' p.' + s.page;
      srcDiv.appendChild(a);
    }});
    return srcDiv;
  }}

  // --- Autoscroll ---
  function autoScroll() {{
    var t = 80;
    var atBottom = (messagesEl.scrollHeight - messagesEl.scrollTop - messagesEl.clientHeight) < t;
    if (atBottom) messagesEl.scrollTop = messagesEl.scrollHeight;
  }}

  // --- Panel open/close ---
  toggle.addEventListener('click', function(){{
    panel.classList.add('open');
    document.body.classList.add('chat-open');
    toggle.style.display = 'none';
    setTimeout(function(){{ input.focus(); }}, 300);
  }});
  closeBtn.addEventListener('click', function(){{
    panel.classList.remove('open');
    document.body.classList.remove('chat-open');
    toggle.style.display = '';
  }});

  // --- Input handling ---
  input.addEventListener('input', function(){{
    this.style.height = 'auto';
    this.style.height = Math.min(this.scrollHeight, 120) + 'px';
  }});
  input.addEventListener('keydown', function(e){{
    if (e.key === 'Enter' && !e.shiftKey) {{ e.preventDefault(); doSend(); }}
  }});
  sendBtn.addEventListener('click', doSend);

  // --- SSE chat send ---
  function doSend(){{
    if (busy) return;
    var q = input.value.trim();
    if (!q) return;
    busy = true;
    sendBtn.disabled = true;
    input.value = '';
    input.style.height = 'auto';

    // Clear hint on first message
    var hint = messagesEl.querySelector('.r-chat-hint');
    if (hint) hint.remove();

    // User message bubble
    var userMsg = document.createElement('div');
    userMsg.className = 'r-chat-msg r-chat-msg-user';
    userMsg.textContent = q;
    messagesEl.appendChild(userMsg);
    autoScroll();

    // Status indicator
    var statusEl = document.createElement('div');
    statusEl.className = 'r-chat-status';
    statusEl.innerHTML = '<span class="dot"></span> <span class="status-text">Reading report...</span>';
    messagesEl.appendChild(statusEl);
    autoScroll();

    // Assistant message (hidden until first token)
    var assistantMsg = document.createElement('div');
    assistantMsg.className = 'r-chat-msg r-chat-msg-assistant';
    assistantMsg.style.display = 'none';

    allMessages.push({{role: 'user', content: q}});

    var assistantText = '';
    var sourcesData = [];
    var modelName = '';
    var seenBytes = 0;
    var remainder = '';

    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/api/ask');
    xhr.setRequestHeader('Content-Type', 'application/json');

    xhr.onprogress = function(){{
      var newData = xhr.responseText.slice(seenBytes);
      seenBytes = xhr.responseText.length;
      remainder += newData;
      var parts = remainder.split('\\n\\n');
      remainder = parts.pop();
      for (var i = 0; i < parts.length; i++) {{
        var evLines = parts[i].split('\\n');
        var evtType = '', evtData = '';
        for (var j = 0; j < evLines.length; j++) {{
          if (evLines[j].startsWith('event: ')) evtType = evLines[j].slice(7);
          if (evLines[j].startsWith('data: ')) evtData = evLines[j].slice(6);
        }}
        if (!evtType || !evtData) continue;
        var d;
        try {{ d = JSON.parse(evtData); }} catch(e) {{ continue; }}

        if (evtType === 'status') {{
          statusEl.querySelector('.status-text').textContent = d.message;
        }} else if (evtType === 'token') {{
          if (assistantMsg.style.display === 'none') {{
            messagesEl.appendChild(assistantMsg);
            assistantMsg.style.display = '';
            statusEl.style.display = 'none';
          }}
          assistantText += d.text;
          assistantMsg.innerHTML = renderMd(assistantText);
          autoScroll();
        }} else if (evtType === 'done') {{
          sourcesData = d.sources || [];
          modelName = d.model || '';
        }} else if (evtType === 'error') {{
          statusEl.querySelector('.status-text').textContent = 'Error: ' + d.message;
          statusEl.querySelector('.dot').style.background = 'var(--accent)';
        }}
      }}
    }};

    xhr.onloadend = function(){{
      if (assistantText) {{
        assistantMsg.innerHTML = renderMd(assistantText);
        if (sourcesData.length > 0) {{
          assistantMsg.appendChild(buildSourcesEl(sourcesData));
        }}
        if (modelName) {{
          var modelEl = document.createElement('div');
          modelEl.className = 'r-chat-model';
          modelEl.textContent = 'Answered by ' + modelName;
          assistantMsg.appendChild(modelEl);
        }}
        allMessages.push({{role: 'assistant', content: assistantText}});
      }} else {{
        var sTxt = statusEl.querySelector('.status-text');
        if (!sTxt || !sTxt.textContent.startsWith('Error:')) {{
          statusEl.querySelector('.status-text').textContent = 'Something went wrong. Please try again.';
          statusEl.querySelector('.dot').style.background = 'var(--accent)';
        }}
      }}
      if (assistantText) statusEl.remove();
      if (assistantMsg.style.display === 'none') assistantMsg.remove();
      busy = false;
      sendBtn.disabled = false;
      input.focus();
      autoScroll();
    }};

    xhr.send(JSON.stringify({{question: q, report: REPORT_PATH, history: allMessages.slice(0, -1)}}));
  }}
}})();
</script>
</body>
</html>"""


INDEX_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Investigation Reports — Epstein Files</title>
<link rel="alternate" type="application/rss+xml" title="Epstein Files Reports" href="/reports/feed.xml">
<link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Work+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
:root {{
  --ink: #0c0f14; --paper: #f5f2ec; --paper-warm: #ece7dd;
  --accent: #8b2500; --muted: #7a756c; --muted-light: #a8a299;
  --border: #d6d0c5; --border-light: #e6e1d8; --white: #fefdfb;
  --seal-gold: #b8941a;
  --font-display: 'Work Sans', sans-serif;
  --font-body: 'Work Sans', sans-serif;
  --font-mono: 'DM Mono', monospace;
}}
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{ background: var(--paper); color: var(--ink); font-family: var(--font-body); }}
.r-topbar {{
  display: flex; align-items: center; justify-content: space-between;
  padding: 0.65rem 1.25rem; background: var(--ink); color: var(--paper);
  font-family: var(--font-mono); font-size: 0.68rem;
  letter-spacing: 0.12em; text-transform: uppercase;
}}
.r-topbar a {{ color: var(--paper); text-decoration: none; opacity: 0.85; }}
.r-topbar a:hover {{ opacity: 1; text-decoration: underline; }}
.r-topbar-home {{ opacity: 1 !important; font-weight: 500; letter-spacing: 0.08em; }}
.r-topbar-links {{ display: flex; align-items: center; gap: 0.4rem; }}
.r-topbar .bar-dot {{
  width: 4px; height: 4px; background: var(--seal-gold);
  border-radius: 50%; display: inline-block;
}}
.ri-hero {{
  max-width: 900px; margin: 0 auto; padding: 3rem 1.5rem 1.5rem;
  text-align: center;
}}
.ri-hero h1 {{
  font-family: var(--font-display); font-size: 2rem; font-weight: 600;
  color: var(--ink); margin: 0 0 0.5rem; letter-spacing: -0.02em;
}}
.ri-hero p {{
  color: var(--muted); font-size: 0.88rem; max-width: 560px;
  margin: 0 auto; line-height: 1.6;
}}
.ri-hero .ri-count {{
  font-family: var(--font-mono); font-size: 0.72rem;
  color: var(--muted-light); margin-top: 0.5rem;
}}
.ri-main {{ max-width: 900px; margin: 0 auto; padding: 0 1.5rem 3rem; }}
.ri-start-here {{
  margin: 0 0 2.5rem;
}}
.ri-start-here a {{
  display: block; padding: 1.25rem 1.5rem;
  background: var(--ink); color: var(--paper);
  text-decoration: none; transition: background 0.15s;
  border: 1px solid var(--ink);
}}
.ri-start-here a:hover {{ background: #1a1f2e; }}
.ri-start-label {{
  display: inline-block;
  font-family: var(--font-mono); font-size: 0.68rem; font-weight: 500;
  text-transform: uppercase; letter-spacing: 0.12em;
  color: var(--seal-gold); margin-bottom: 0.35rem;
}}
.ri-start-title {{
  display: block;
  font-family: var(--font-display); font-size: 1.1rem; font-weight: 600;
  color: var(--paper); line-height: 1.3;
}}
.ri-start-desc {{
  display: block; margin-top: 0.3rem;
  font-size: 0.78rem; color: var(--muted-light); line-height: 1.5;
}}
.ri-section {{ margin: 0 0 2.5rem; }}
.ri-section h2 {{
  font-family: var(--font-display); font-size: 1.1rem; font-weight: 600;
  color: var(--ink); margin: 0 0 0.75rem; padding-bottom: 0.5rem;
  border-bottom: 2px solid var(--ink); letter-spacing: -0.01em;
}}
.ri-section-link {{
  color: inherit; text-decoration: none;
}}
.ri-section-link:hover {{ color: var(--accent); }}
.ri-link-icon {{
  font-family: var(--font-mono); font-size: 0.8rem; font-weight: 400;
  color: var(--muted-light); margin-left: 6px; opacity: 0;
  transition: opacity 0.15s;
}}
.ri-section-link:hover .ri-link-icon {{ opacity: 1; }}
.ri-grid {{
  display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
  gap: 1px; background: var(--border); border: 1px solid var(--border);
}}
.ri-card {{
  display: block; padding: 14px 16px; background: var(--white);
  text-decoration: none; color: var(--ink); transition: background 0.15s;
}}
.ri-card:hover {{ background: var(--paper-warm); }}
.ri-title {{
  font-family: var(--font-display); font-weight: 600; font-size: 0.84rem;
  margin-bottom: 3px; color: var(--ink); line-height: 1.4;
}}
.ri-desc {{
  font-size: 0.72rem; color: var(--muted); line-height: 1.5;
  display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical;
  overflow: hidden;
}}
.ri-card-date {{
  font-family: var(--font-mono); font-size: 0.62rem;
  color: var(--muted-light); margin-top: 4px; letter-spacing: 0.03em;
}}
.ri-search-form {{
  max-width: 480px; margin: 1.25rem auto 0; display: flex;
  border: 1px solid var(--border); background: var(--white);
  transition: border-color 0.2s, box-shadow 0.2s;
}}
.ri-rss {{
  color: #ee802f; text-decoration: none; font-size: 0.68rem;
  font-family: var(--font-mono); letter-spacing: 0.04em;
  vertical-align: middle;
}}
.ri-rss:hover {{ color: var(--accent); }}
.ri-rss svg {{ vertical-align: -1px; margin-right: 2px; }}
.ri-search-form:focus-within {{ border-color: var(--ink); box-shadow: 0 0 0 1px var(--ink); }}
.ri-search-form input {{
  flex: 1; padding: 10px 14px; border: none; outline: none;
  background: transparent; font-family: var(--font-body);
  font-size: 0.9rem; color: var(--ink);
}}
.ri-search-form input::placeholder {{ color: var(--muted-light); font-style: italic; }}
.ri-search-info {{
  text-align: center; margin: 0.5rem 0 0;
  font-family: var(--font-mono); font-size: 0.72rem; color: var(--muted);
}}
.ri-card.ri-hidden {{ display: none; }}
.ri-section.ri-hidden {{ display: none; }}
/* View toggle + sort controls */
.ri-controls {{
  max-width: 900px; margin: 1.25rem auto 0; padding: 0 1.5rem;
  display: flex; align-items: center; gap: 0.5rem; flex-wrap: wrap;
}}
.ri-view-btns {{ display: flex; gap: 1px; border: 1px solid var(--border); }}
.ri-view-btn {{
  padding: 5px 12px; background: var(--white); border: none; cursor: pointer;
  font-family: var(--font-mono); font-size: 0.68rem; color: var(--muted);
  letter-spacing: 0.04em; text-transform: uppercase;
}}
.ri-view-btn:hover {{ color: var(--ink); }}
.ri-view-btn.active {{ background: var(--ink); color: var(--paper); }}
.ri-sort-btns {{ display: flex; gap: 1px; border: 1px solid var(--border); margin-left: auto; }}
.ri-sort-btn {{
  padding: 5px 10px; background: var(--white); border: none; cursor: pointer;
  font-family: var(--font-mono); font-size: 0.68rem; color: var(--muted);
  letter-spacing: 0.03em;
}}
.ri-sort-btn:hover {{ color: var(--ink); }}
.ri-sort-btn.active {{ background: var(--ink); color: var(--paper); }}
.ri-sort-btns.hidden {{ display: none; }}
/* List view table */
.ri-list-table {{ display: none; max-width: 900px; margin: 0 auto; padding: 0 1.5rem 3rem; }}
.ri-list-table table {{
  width: 100%; border-collapse: collapse; font-size: 0.82rem;
}}
.ri-list-table th {{
  font-family: var(--font-mono); font-size: 0.68rem; font-weight: 500;
  text-transform: uppercase; letter-spacing: 0.06em; color: var(--muted);
  padding: 8px 10px; text-align: left; border-bottom: 2px solid var(--ink);
  cursor: pointer; user-select: none; white-space: nowrap;
}}
.ri-list-table th:hover {{ color: var(--ink); }}
.ri-list-table th .sort-arrow {{ font-size: 0.6rem; margin-left: 3px; }}
.ri-list-table td {{
  padding: 7px 10px; border-bottom: 1px solid var(--border-light);
  vertical-align: top;
}}
.ri-list-table td a {{ color: var(--ink); text-decoration: none; font-weight: 500; }}
.ri-list-table td a:hover {{ color: var(--accent); text-decoration: underline; }}
.ri-list-table td.num {{ text-align: right; font-family: var(--font-mono); font-size: 0.76rem; color: var(--muted); }}
.ri-list-table td.cat {{ font-size: 0.74rem; color: var(--muted); white-space: nowrap; }}
.ri-list-table td.date {{ font-family: var(--font-mono); font-size: 0.74rem; color: var(--muted); white-space: nowrap; }}
.ri-list-table tr.ri-hidden {{ display: none; }}
body.ri-listmode .ri-main {{ display: none; }}
body.ri-listmode .ri-list-table {{ display: block; }}
.ri-sort-btns.hidden {{ display: none !important; }}
@media (max-width: 600px) {{
  .ri-controls {{ gap: 0.35rem; }}
  .ri-list-table {{ padding: 0 0.5rem 2rem; }}
  .ri-list-table table {{ font-size: 0.78rem; }}
  .ri-list-table th, .ri-list-table td {{ padding: 5px 6px; }}
}}
.r-footer {{
  text-align: center; padding: 2rem 1rem; border-top: 1px solid var(--border);
  font-size: 0.72rem; color: var(--muted); font-family: var(--font-mono);
}}
.r-footer a {{ color: var(--muted); text-decoration: none; margin: 0 10px; }}
.r-footer a:hover {{ color: var(--ink); }}
@media (max-width: 600px) {{
  .ri-hero h1 {{ font-size: 1.5rem; }}
  .ri-grid {{ grid-template-columns: 1fr; }}
  .r-topbar {{ font-size: 0.6rem; }}
}}
</style>
</head>
<body>
<div class="r-topbar">
  <a href="/" class="r-topbar-home">Home</a>
  <div class="r-topbar-links">
    <a href="https://www.congress.gov/119/plaws/publ38/PLAW-119publ38.htm" target="_blank">EFTA</a>
    <span class="bar-dot"></span>
    <a href="https://www.justice.gov/epstein/doj-disclosures" target="_blank">DOJ Production</a>
  </div>
</div>
<div class="ri-hero">
  <h1>Investigation Reports</h1>
  <p>Forensic analysis of the DOJ's EFTA production. Each report is built from primary source documents with specific EFTA citations.</p>
  <div class="ri-count">{count} reports across {cat_count} categories &ensp;<a href="/reports/feed.xml" class="ri-rss" title="RSS Feed"><svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 256 256"><circle cx="68" cy="189" r="24" fill="currentColor"/><path d="M160 213h-34a83 83 0 0 0-83-83V96a117 117 0 0 1 117 117Z" fill="none" stroke="currentColor" stroke-width="28" stroke-linecap="round" stroke-linejoin="round"/><path d="M220 213h-34a143 143 0 0 0-143-143V36a177 177 0 0 1 177 177Z" fill="none" stroke="currentColor" stroke-width="28" stroke-linecap="round" stroke-linejoin="round"/></svg> RSS</a></div>
  <div class="ri-search-form">
    <input type="search" id="ri-search" placeholder="Filter reports&hellip;" autocomplete="off" autofocus>
  </div>
  <div class="ri-search-info" id="ri-search-info"></div>
</div>
<div class="ri-controls">
  <div class="ri-view-btns">
    <button class="ri-view-btn active" data-view="grid">Grid</button>
    <button class="ri-view-btn" data-view="list">List</button>
  </div>
  <div class="ri-sort-btns hidden" id="ri-sort-btns">
    <button class="ri-sort-btn active" data-sort="added" data-dir="desc">Newest</button>
    <button class="ri-sort-btn" data-sort="eftas" data-dir="desc">Most Citations</button>
    <button class="ri-sort-btn" data-sort="words" data-dir="desc">Longest</button>
  </div>
</div>
<div class="ri-main">
{sections}
</div>
<div class="ri-list-table" id="ri-list-table">
  <table>
    <thead><tr>
      <th data-col="title">Title <span class="sort-arrow"></span></th>
      <th data-col="cat">Category <span class="sort-arrow"></span></th>
      <th data-col="added">Date <span class="sort-arrow"></span></th>
      <th data-col="eftas">EFTAs <span class="sort-arrow"></span></th>
      <th data-col="words">Words <span class="sort-arrow"></span></th>
    </tr></thead>
    <tbody id="ri-list-body"></tbody>
  </table>
</div>
<div class="r-footer">
  <a href="https://github.com/rhowardstone/Epstein-research-data/">Source Data</a>
  <a href="/reports/">Investigation Reports</a>
  <a href="/reports/feed.xml">RSS Feed</a>
  <a href="https://www.justice.gov/epstein">DOJ EFTA</a>
  <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">CC BY-NC-SA 4.0</a>
  <a href="https://docs.google.com/forms/d/e/1FAIpQLSdY9gkq3z2VsSjdGnOehFsRcqhX29lC0Knr9Lx_uSAo0W5PSg/viewform" target="_blank">Feedback</a>
  <div class="r-footer-disclaimer">
    Independent research project. Not affiliated with the U.S. Department of Justice, FBI, any government agency, or Anthropic. All reports are AI-generated (Claude, Anthropic) and iteratively fact-checked against source documents, but may contain errors.
  </div>
  <div style="margin-top:0.75rem;color:#a8a299;">
    Powered by <a href="https://datasette.io/">Datasette</a>
    &ensp;&middot;&ensp;
    <a href="https://ko-fi.com/rhowardstone">Support this project</a>
  </div>
</div>
<script>
(function() {{
  var input = document.getElementById('ri-search');
  var info = document.getElementById('ri-search-info');
  var cards = Array.from(document.querySelectorAll('.ri-card'));
  var sections = document.querySelectorAll('.ri-section');
  var viewBtns = document.querySelectorAll('.ri-view-btn');
  var sortBtnsWrap = document.getElementById('ri-sort-btns');
  var listBody = document.getElementById('ri-list-body');
  var listHeaders = document.querySelectorAll('.ri-list-table th[data-col]');
  var debounce = null;
  var currentView = localStorage.getItem('ri-view') || 'grid';
  var listSortCol = 'added', listSortDir = 'desc';

  // Section anchor link copy
  document.querySelectorAll('.ri-link-icon').forEach(function(icon) {{
    icon.addEventListener('click', function(e) {{
      e.preventDefault();
      e.stopPropagation();
      var link = icon.closest('.ri-section-link');
      var url = window.location.origin + window.location.pathname + link.getAttribute('href');
      navigator.clipboard.writeText(url).then(function() {{
        icon.textContent = '\u2713';
        setTimeout(function() {{ icon.textContent = '#'; }}, 1200);
      }});
    }});
  }});

  // Build list table rows from card data, linked via _row/_card refs
  var rows = [];
  cards.forEach(function(c) {{
    var title = c.querySelector('.ri-title');
    var added = c.getAttribute('data-added') || '';
    var eftas = parseInt(c.getAttribute('data-eftas') || '0', 10);
    var words = parseInt(c.getAttribute('data-words') || '0', 10);
    var cat = c.getAttribute('data-cat') || '';
    var tr = document.createElement('tr');
    tr.setAttribute('data-added', added);
    tr.setAttribute('data-eftas', eftas);
    tr.setAttribute('data-words', words);
    tr.innerHTML = '<td><a href="' + c.getAttribute('href') + '">' + (title ? title.textContent : '') + '</a></td>'
      + '<td class="cat">' + cat + '</td>'
      + '<td class="date">' + added.slice(0, 10) + '</td>'
      + '<td class="num">' + (eftas || '\u2014') + '</td>'
      + '<td class="num">' + (words ? words.toLocaleString() : '\u2014') + '</td>';
    tr._title = title ? title.textContent.toLowerCase() : '';
    tr._cat = cat.toLowerCase();
    c._row = tr;  // link card → row
    listBody.appendChild(tr);
    rows.push(tr);
  }});

  function setView(v) {{
    currentView = v;
    localStorage.setItem('ri-view', v);
    document.body.classList.toggle('ri-listmode', v === 'list');
    viewBtns.forEach(function(b) {{ b.classList.toggle('active', b.getAttribute('data-view') === v); }});
    if (v === 'grid') {{
      sortBtnsWrap.classList.add('hidden');
    }} else {{
      sortBtnsWrap.classList.remove('hidden');
      sortListTable();
    }}
  }}

  viewBtns.forEach(function(b) {{
    b.addEventListener('click', function() {{ setView(b.getAttribute('data-view')); }});
  }});

  // Sort controls (for grid view — sort all cards by flattening)
  document.querySelectorAll('.ri-sort-btn').forEach(function(b) {{
    b.addEventListener('click', function() {{
      var col = b.getAttribute('data-sort');
      var dir = b.getAttribute('data-dir');
      if (b.classList.contains('active')) {{
        dir = dir === 'desc' ? 'asc' : 'desc';
        b.setAttribute('data-dir', dir);
      }}
      document.querySelectorAll('.ri-sort-btn').forEach(function(x) {{ x.classList.remove('active'); }});
      b.classList.add('active');
      listSortCol = col; listSortDir = dir;
      sortListTable();
    }});
  }});

  // Column header sorting in list view
  listHeaders.forEach(function(th) {{
    th.addEventListener('click', function() {{
      var col = th.getAttribute('data-col');
      if (listSortCol === col) {{
        listSortDir = listSortDir === 'desc' ? 'asc' : 'desc';
      }} else {{
        listSortCol = col;
        listSortDir = (col === 'title' || col === 'cat') ? 'asc' : 'desc';
      }}
      sortListTable();
    }});
  }});

  function sortListTable() {{
    var col = listSortCol, dir = listSortDir;
    rows.sort(function(a, b) {{
      var va, vb;
      if (col === 'title') {{ va = a._title; vb = b._title; }}
      else if (col === 'cat') {{ va = a._cat; vb = b._cat; }}
      else if (col === 'added') {{ va = a.getAttribute('data-added') || ''; vb = b.getAttribute('data-added') || ''; }}
      else {{ va = parseInt(a.getAttribute('data-' + col) || '0', 10); vb = parseInt(b.getAttribute('data-' + col) || '0', 10); }}
      var cmp;
      if (typeof va === 'number' && typeof vb === 'number') {{ cmp = va - vb; }}
      else {{ cmp = String(va).localeCompare(String(vb)); }}
      return dir === 'desc' ? -cmp : cmp;
    }});
    rows.forEach(function(r) {{ listBody.appendChild(r); }});
    // Update header arrows
    listHeaders.forEach(function(th) {{
      var arrow = th.querySelector('.sort-arrow');
      if (th.getAttribute('data-col') === col) {{
        arrow.textContent = dir === 'desc' ? ' \u25BC' : ' \u25B2';
      }} else {{
        arrow.textContent = '';
      }}
    }});
    // Sync sort buttons
    document.querySelectorAll('.ri-sort-btn').forEach(function(b) {{
      b.classList.toggle('active', b.getAttribute('data-sort') === col);
      if (b.getAttribute('data-sort') === col) b.setAttribute('data-dir', dir);
    }});
  }}

  // Filter (works in both views)
  input.addEventListener('input', function() {{
    clearTimeout(debounce);
    debounce = setTimeout(filterReports, 200);
  }});

  function filterReports() {{
    var q = input.value.trim().toLowerCase();
    if (!q) {{
      cards.forEach(function(c) {{ c.classList.remove('ri-hidden'); }});
      sections.forEach(function(s) {{ s.classList.remove('ri-hidden'); }});
      rows.forEach(function(r) {{ r.classList.remove('ri-hidden'); }});
      info.textContent = '';
      return;
    }}
    var words = q.split(/\s+/).filter(function(w) {{ return w.length > 1; }});
    var shown = 0;
    cards.forEach(function(c) {{
      var text = c.textContent.toLowerCase();
      var match = words.every(function(w) {{ return text.indexOf(w) >= 0; }});
      c.classList.toggle('ri-hidden', !match);
      if (c._row) c._row.classList.toggle('ri-hidden', !match);
      if (match) shown++;
    }});
    sections.forEach(function(s) {{
      var visible = s.querySelectorAll('.ri-card:not(.ri-hidden)');
      s.classList.toggle('ri-hidden', visible.length === 0);
    }});
    info.textContent = shown + ' report' + (shown !== 1 ? 's' : '') + ' matching';
  }}

  // Init
  setView(currentView);
  sortListTable();
}})();
</script>
</body>
</html>"""


def main():
    print(f"Building reports from {REPO_DIR} → {OUT_DIR}")

    if not REPO_DIR.exists():
        print(f"Error: repo dir {REPO_DIR} does not exist. Clone it first:")
        print(f"  git clone https://github.com/rhowardstone/epstein-research.git {REPO_DIR}")
        sys.exit(1)

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    reports_by_cat = {}
    total = 0
    git_dates = get_git_dates(REPO_DIR)

    for md_path in sorted(REPO_DIR.rglob("*.md")):
        rel = md_path.relative_to(REPO_DIR)
        rel_str = str(rel)

        # Skip non-report files
        if rel.name in SKIP_FILES:
            continue
        if rel.parts[0].startswith("."):
            continue

        # Determine category
        if len(rel.parts) > 1:
            category = rel.parts[0]
        else:
            category = "overview"

        category_label = CATEGORIES.get(category, category.replace("-", " ").replace("_", " ").title())

        md_text = md_path.read_text(encoding="utf-8", errors="replace")
        title = extract_title(md_text, rel.name)
        description = extract_description(md_text)

        # Compute metadata
        efta_count = len(set(re.findall(r"EFTA\d{8}", md_text)))
        word_count = len(md_text.split())

        # Render HTML
        file_git_date = git_dates.get(rel_str, "")
        date_display = format_date_display(file_git_date)
        html_content = render_report(md_text, title, description, category, category_label, rel_str,
                                     date_display=date_display, git_date=file_git_date)

        # Write output
        if len(rel.parts) > 1:
            out_path = OUT_DIR / rel.with_suffix(".html")
        else:
            out_path = OUT_DIR / rel.with_suffix(".html")

        out_path.parent.mkdir(parents=True, exist_ok=True)
        if out_path.exists() and out_path.read_text(encoding="utf-8") == html_content:
            pass  # unchanged — preserve mtime
        else:
            out_path.write_text(html_content, encoding="utf-8")

        # Track for index
        href = str(rel.with_suffix(".html"))
        if category not in reports_by_cat:
            reports_by_cat[category] = []
        reports_by_cat[category].append({
            "title": title,
            "description": description,
            "href": href,
            "rel_md": rel_str,
            "date_display": date_display,
            "git_date": file_git_date,
            "efta_count": efta_count,
            "word_count": word_count,
        })
        total += 1

    # Extract README as "Start Here" — remove from normal category listing
    start_here = None
    for cat in list(reports_by_cat.keys()):
        for r in reports_by_cat[cat]:
            if r["rel_md"] == START_HERE_FILE:
                start_here = r
                reports_by_cat[cat].remove(r)
                if not reports_by_cat[cat]:
                    del reports_by_cat[cat]
                break
        if start_here:
            break

    # Render index
    index_html = render_index(reports_by_cat, start_here=start_here)
    index_path = OUT_DIR / "index.html"
    if not index_path.exists() or index_path.read_text(encoding="utf-8") != index_html:
        index_path.write_text(index_html, encoding="utf-8")

    # Write featured.json for homepage — ALL reports, hand-written overrides for key ones
    featured = []
    for cat, reports in reports_by_cat.items():
        for r in reports:
            entry = {
                "title": r["title"],
                "description": r["description"],
                "href": r["href"],
                "date_display": r.get("date_display", ""),
                "efta_count": r.get("efta_count", 0),
                "word_count": r.get("word_count", 0),
            }
            if r["rel_md"] in FEATURED:
                entry["description"] = FEATURED[r["rel_md"]]
            if r["rel_md"] in git_dates:
                entry["added"] = git_dates[r["rel_md"]]
            elif r.get("git_date"):
                entry["added"] = r["git_date"]
            featured.append(entry)
    featured_path = OUT_DIR / "featured.json"
    featured_text = json.dumps(featured, indent=2)
    if not featured_path.exists() or featured_path.read_text(encoding="utf-8") != featured_text:
        featured_path.write_text(featured_text, encoding="utf-8")

    # Generate RSS feed
    def parse_iso_to_rfc2822(iso_str):
        """Convert ISO 8601 timestamp to RFC 2822 for RSS pubDate."""
        try:
            # Handle timezone offset like -05:00
            dt = datetime.fromisoformat(iso_str)
            return format_datetime(dt)
        except (ValueError, TypeError):
            return ""

    rss_items = sorted(featured, key=lambda r: r.get("added", ""), reverse=True)
    rss_items = [r for r in rss_items if r.get("added")]

    rss_xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    rss_xml += '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">\n<channel>\n'
    rss_xml += '  <title>Epstein Files Investigation Reports</title>\n'
    rss_xml += '  <link>https://epstein-data.com/reports/</link>\n'
    rss_xml += '  <description>Forensic analysis of the DOJ EFTA production — primary source investigations with specific document citations.</description>\n'
    rss_xml += '  <atom:link href="https://epstein-data.com/reports/feed.xml" rel="self" type="application/rss+xml"/>\n'
    rss_xml += '  <language>en-us</language>\n'
    for r in rss_items:
        pub_date = parse_iso_to_rfc2822(r["added"])
        rss_xml += '  <item>\n'
        rss_xml += f'    <title>{html.escape(r["title"])}</title>\n'
        rss_xml += f'    <link>https://epstein-data.com/reports/{html.escape(r["href"])}</link>\n'
        rss_xml += f'    <guid>https://epstein-data.com/reports/{html.escape(r["href"])}</guid>\n'
        if r.get("description"):
            rss_xml += f'    <description>{html.escape(r["description"])}</description>\n'
        if pub_date:
            rss_xml += f'    <pubDate>{pub_date}</pubDate>\n'
        rss_xml += '  </item>\n'
    rss_xml += '</channel>\n</rss>\n'

    feed_path = OUT_DIR / "feed.xml"
    if not feed_path.exists() or feed_path.read_text(encoding="utf-8") != rss_xml:
        feed_path.write_text(rss_xml, encoding="utf-8")

    print(f"Built {total} reports in {len(reports_by_cat)} categories")
    print(f"Index: {OUT_DIR}/index.html")
    print(f"Featured: {OUT_DIR}/featured.json ({len(featured)} reports)")
    print(f"RSS: {OUT_DIR}/feed.xml ({len(rss_items)} items)")


if __name__ == "__main__":
    main()
