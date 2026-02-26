# MASTER FORENSIC REPORT: DOJ EPSTEIN FILES
# Consolidated Findings from Systematic Document Analysis

> **Context:** This report was written on February 5–6, 2026, during the first week of the investigation. It covers findings from the initial redaction and text layer analysis. The project has since produced **150+ investigation reports** with substantially deeper analysis in every area covered here. For the complete catalog, see the [full report index](https://epstein-data.com/reports/).

**Date:** February 5, 2026 (Updated: February 6, 2026)
**Database:** the primary document text database (627MB)
**Source Material:** DOJ Epstein Files, Datasets 1-12 (~218GB, 519,438 PDFs)
**Method:** Systematic extraction of text from PDF text layers (OCR) near redaction zones using PDF analysis tools
**Total Redactions Analyzed:** 1,808,915
**Extracted Entities:** 107,422 (49,153 names, 36,187 dates, 7,918 addresses, 6,167 organizations, 3,769 dollar amounts, 3,537 phone numbers, 589 emails, 102 account numbers)
**Reconstructed Pages:** 39,588

---

## TABLE OF CONTENTS

1. [Methodology and Data Quality](#1-methodology-and-data-quality)
2. [The Financial Architecture](#2-the-financial-architecture)
3. [The $500M Question: Where Did the Money Come From?](#3-the-500m-question)
4. [The Haze Trust Drawdown: $46.96M in Five Months](#4-the-haze-trust-drawdown)
5. [The Shell Company Network: 18 Entities, One Client](#5-the-shell-company-network)
6. [Deutsche Bank: Compliance Knew Everything](#6-deutsche-bank-compliance)
7. [The Key Operators: Kahn, Indyke, Barrett](#7-the-key-operators)
8. [The Prominent Names Document](#8-the-prominent-names-document)
9. [William Barr: AG Under Investigation by His Own FBI](#9-william-barr)
10. [Leon Black: Three Years of FBI Investigation, No Charges](#10-leon-black)
11. [The NTOC Tip Line: What Victims Reported](#11-the-ntoc-tip-line)
12. [Ghislaine Maxwell: Identity Anomalies](#12-ghislaine-maxwell)
13. [The Obstruction Wires: $350K After the Herald Story](#13-the-obstruction-wires)
14. [Calendar Intelligence: Meetings Mapped to Money](#14-calendar-intelligence)
15. [The Post-Death Estate: $600M With a $228M Gap](#15-the-post-death-estate)
16. [The Island: Hidden Structures and Tunnels](#16-the-island)
17. [The Blackmail Document](#17-the-blackmail-document)
18. [Unexplored Names and Disappeared Witnesses](#18-unexplored-names)
19. [The Victoria's Secret Pipeline](#19-the-victoria-secret-pipeline)
20. [What the Files Do NOT Contain](#20-what-the-files-do-not-contain)
21. [Pattern of Non-Investigation](#21-pattern-of-non-investigation)
22. [ADDENDUM: Gap Analysis Findings (February 5, 2026)](#22-addendum-gap-analysis-findings)
23. [Deep Document Investigation - Critical Findings (February 6, 2026)](#23-deep-document-investigation)
24. [Appendix: Complete Report Index](#24-appendix)

---

## 1. METHODOLOGY AND DATA QUALITY

### 1.1 How This Was Done

The DOJ released Epstein-related files in 12 datasets totaling approximately 218GB and 519,438 PDF documents. Many of these documents are scanned images with OCR text layers. The PDF analysis tools pipeline identified black rectangle regions and extracted any text present in the PDF text layer beneath or near those regions. In most cases, this text is OCR output from the original scan -- not text that was "hidden" behind a removable overlay. A subsequent data quality audit (DATA_QUALITY_AUDIT.md) confirmed that ~98% of extracted records are OCR artifacts from degraded scans. Only 12 specific documents had genuinely failed redaction overlays where PLIST metadata was exposed beneath improperly flattened redactions.

A analysis process using PDF analysis tools was used to:
1. Identify all annotation/rectangle overlays in each PDF
2. Extract any text existing beneath those overlays
3. Store the results in a document database with EFTA document numbers, page numbers, coordinates, and confidence scores
4. Run entity extraction (names, dates, amounts, organizations, addresses, phones, emails, account numbers)
5. Reconstruct full pages by assembling fragments in spatial order

### 1.2 Confidence Assessment

- **High confidence:** Text extracted cleanly with recognizable words, sentences, names, or numbers
- **Medium confidence:** Partial text with OCR artifacts but recoverable meaning
- **Low confidence:** Fragmentary characters that may represent OCR noise rather than actual redacted content

The analysis focused on high and medium confidence extractions (hidden_text length > 3 characters). The corpus is useful for keyword searches identifying which documents mention specific terms. However, the vast majority of extracted text is OCR noise rather than genuinely exposed content. The 12 genuinely failed redaction overlays (exposing PLIST metadata) are documented separately in [PLIST_REDACTED_EMAILS_DEEP_DIVE.md](/evidence/PLIST_REDACTED_EMAILS_DEEP_DIVE.md).

### 1.3 Limitations

- Text under properly executed redactions (where the underlying data was actually removed) is irrecoverable
- OCR quality varies across documents; some extracted text contains artifacts
- The redaction detector identifies overlay-style redactions; other redaction methods may exist
- Financial figures extracted from partial text may have OCR errors in specific digits
- NTOC tip line reports represent unverified allegations from callers; credibility assessments are noted where the FBI provided them

**DATA QUALITY NOTE:** The document text database contains 1.8 million text records extracted from PDF text layers near redaction zones. A data quality audit (DATA_QUALITY_AUDIT.md) confirmed that ~98% of 'bad_overlay' records are OCR noise from degraded scans, not text hidden behind removable redactions. Only 12 documents had genuinely failed redaction overlays exposing PLIST metadata. The text searches against this corpus are valid for identifying which documents mention specific terms, but the results should not be characterized as 'recovered hidden text.'

---

## 2. THE FINANCIAL ARCHITECTURE

### 2.1 Overview

Jeffrey Epstein maintained a financial empire at Deutsche Bank under a single Relationship Manager code (RM 82289) encompassing at least **18 corporate entities and trusts**, all assigned to the same two-person banker team: **Jj Litchford** (primary) and **Paul Morris** (secondary). Deutsche Bank internally classified the entire constellation as the **"SOUTHERN FINANCIAL RELATIONSHIP"** -- treating 18 separate legal entities as one client.

**Total consolidated assets exceeded $110 million at peak.** The Haze Trust alone held $49.5 million. Southern Trust Company held $45.15 million. Multiple additional accounts held tens of millions more.

The Government's bail memo ([EFTA00028785](https://www.justice.gov/epstein/files/DataSet%208/EFTA00028785.pdf)) referenced "Institution-1" holding over $500 million in Epstein assets. This analysis conclusively identifies **Institution-1 as Deutsche Bank**, based on:
- The bail memo cites wire transfers on November 30, 2018 and December 3, 2018 from Institution-1 records
- JP Morgan closed Epstein's accounts in 2013
- Deutsche Bank opened the Southern Financial Relationship on August 26, 2013
- Only Deutsche Bank held Epstein accounts in late 2018

The $500M figure represents total assets in DB's client records (real estate + investments + cash), not just cash balances.

### 2.2 The Entity Roster

**Source:** [EFTA01359500](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01359500.pdf), [EFTA01477454](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01477454.pdf)

#### Core Epstein Entities at Deutsche Bank:

| Entity | Account Type | Peak Balance | Function |
|--------|-------------|-------------|----------|
| Jeffrey Epstein (personal DDA 739110438) | Personal | Central hub | Clearing account for all fund flows |
| Jeffrey Epstein (2nd account) | Personal | — | Secondary personal |
| Southern Trust Company Inc. | Corporate (M) | $45,150,000 | Tier 1 holding company |
| Southern Financial LLC | Corporate (D) | $7,000,000+ | Tier 1 holding; credit derivatives trading |
| The Haze Trust (N4G024943) | Trust (D) | $49,460,098.13 | Largest single asset pool |
| Butterfly Trust (44130552) | Trust (M) | $734,175.44 | Secondary trust vehicle |
| Gratitude America Ltd | Corporate | — | Offshore entity |
| Zorro Management LLC | Corporate | — | USVI management entity |
| LSJE LLC | Corporate (D) | — | Emirates Bank International connection |
| NES LLC | Corporate (D) | — | Operating entity |
| JEGE Inc / JEGE LLC | Corporate (D) | — | Operating entities |
| Plan D LLC | Corporate (D) | — | Operating entity |
| Neptune LLC | Corporate (D) | — | Flagged for suspicious wires ($1,200, $1,000) |
| Hyperion Air LLC / Inc | Corporate (D) | — | Aviation entity |
| HBRK Associates Inc (42953715) | Corporate (D) | $418,598.61 | Richard Kahn's CPA firm |
| Darren K. Indyke PLLC | Professional (D) | — | Attorney fees account |
| The 2007 Jeffrey E. Epstein Insurance Trust | Trust | — | Insurance vehicle (balances not recovered) |
| 2017 Caterpillar Trust | Trust | — | Returned funds triggered compliance concern |

#### Additional Names on Same Banker Team (Litchford/Morris then Morris/Oldfield):

| Name | Relationship |
|------|-------------|
| **Leon D. Black** (2 accounts) | Apollo Global Management founder; abuse allegations |
| Christopher A. Boies | Son of David Boies (Epstein's attorney) |
| Dominique Leimer (2 accounts) | Associated client |
| Todd & Karen Wanek / Wanek Trust of 2000 | Ashley Furniture heir |
| Mark F. Dzialga | Associated client |
| New York Strategy Group | Entity |
| Shari Wagner 2014 Grant | Grant vehicle |
| Kati Forsythe 2014 Grant | Grant vehicle |

**Critical finding:** Leon Black's personal accounts were managed by the exact same Deutsche Bank officers who managed all Epstein entities. This is not a casual banking coincidence -- it is a direct institutional financial nexus.

### 2.3 The SAR Filing

**Source:** [EFTA01656524](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01656524.pdf)

Deutsche Bank eventually filed a Suspicious Activity Report naming **25 subjects** in a single filing, covering the entire entity network. This SAR was filed only after years of documented internal compliance failures and, based on timeline evidence, likely only after Epstein's July 2019 arrest.

**[Full details: FORENSIC_ACCT_3_INTER_ENTITY_FLOWS.md]**

---

## 3. THE $500M QUESTION: WHERE DID THE MONEY COME FROM?

### 3.1 The Central Finding

**Across 1,808,915 redactions from 519,438 documents spanning all 12 DOJ datasets, no legitimate source for Epstein's $500M+ in wealth can be identified.**

Despite Epstein's public claim of being a "money manager for billionaires":
- **No documented management fees** appear in recovered financial transaction records
- **No documented advisory fees** appear in recovered financial transaction records
- **No documented client payments** appear in recovered financial transaction records
- **No documented consulting income** appears in recovered financial transaction records

The only documented income is **investment returns** ($8-15M/year) from fixed-income instruments -- coupon payments on sovereign and corporate bonds. But this income only explains returns on capital that was already there. It does not explain how the capital was accumulated.

### 3.2 The Wexner Connection

The only named source of Epstein's wealth in the FBI's own documents is **Leslie Wexner**. Multiple copies of a DOJ/FBI summary document repeat the phrase **"earned his money from Wexner."** However:
- No specific transfer documentation from Wexner to Epstein was recovered
- The $46M charitable donation referenced in [EFTA00026723](https://www.justice.gov/epstein/files/DataSet%208/EFTA00026723.pdf) actually flowed in the **reverse direction** (from Epstein entities to maintain Wexner ties)
- Wexner appears on the PROMINENT NAMES page, annotated "(referred)" in Variant 3 -- meaning the FBI referred him for investigation

### 3.3 What This Means

A man held over $500 million at a single bank, claimed to be a financial manager, and across half a million documents released by the DOJ, no document shows a fee, a client payment, or any legitimate business income explaining the wealth. The source of the capital accumulation is not documented in the available DOJ production.

**[Full details: FORENSIC_ACCT_2_MONEY_SOURCES.md]**

---

## 4. THE HAZE TRUST DRAWDOWN: $46.96M IN FIVE MONTHS

### 4.1 Timeline

The Haze Trust (Account N4G024943) held $49.5M in June 2018 and was drained to approximately $2.5M by November 2018 -- a drawdown of $46.96M in five months.

| Date | Balance | Drop |
|------|---------|------|
| 06/21/2018 | $49,460,098.13 | — |
| Late June 2018 | $40,460,098.13 | **-$9,000,000** |
| 08/17/2018 | $40,583,100.79 | (interest accrual) |
| 08/28/2018 | $35,583,100.79 | **-$5,000,000** |
| 10/03/2018 | $12,690,279.36 | **-$22,892,821** |
| 11/14/2018 | $2,503,667.84 | **-$10,186,612** |

A single debit of **$21,077,720.73** ([EFTA01427435](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01427435.pdf)) was flagged as a "LARGE TRANSACTION" -- roughly 50% of the total drawdown in one move.

### 4.2 Where the Money Went

| Destination | Estimated Amount |
|-------------|-----------------|
| Southern Trust Company Inc. | $15-20M |
| Southern Financial LLC | $8-12M |
| Zorro Management LLC | $3-4M |
| Butterfly Trust | $2.5-3.2M |
| LSJE LLC | $2-3M |
| NES LLC | $2-3M |
| Gratitude America Ltd | $2-3M |
| Darren K. Indyke PLLC | $1.5-2.4M |

### 4.3 The AML Investigation Was Active During the Drawdown

Deutsche Bank's AML unit was actively investigating the Haze Trust under **Alert# SAM 1788880** during this exact period. At least seven DB compliance personnel (Vahe Stepanian, Joshua Shoshan, Donald Summer, Zbynek Kozelsky, Cynthia Rodriguez, Stewart Oldfield, Cherie Quigley) were sending escalating emails including **"URGENT - THIRD REQUEST!!!!!"** about this account.

The money was being scattered across shell entities while the bank's own compliance department was trying to determine what was happening. The drawdown was either prompted by or accelerated due to the compliance scrutiny.

### 4.4 Offshore Wire Infrastructure

Wire transfer routing confirmed across:
- **Firstbank PR** (ABA: 221571473) -- Puerto Rico
- **Banco Popular PR** -- Puerto Rico
- **Bank of Nova Scotia** (St. Thomas, USVI) -- Caribbean
- **Emirates Bank International** (contact: Amar Siad) -- Middle East, linked to LSJE LLC

**[Full details: FORENSIC_ACCT_1_HAZE_DRAWDOWN.md]**

---

## 5. THE SHELL COMPANY NETWORK: 18 ENTITIES, ONE CLIENT

### 5.1 Hub-and-Spoke Architecture

Epstein's personal DDA account (739110438) served as the central clearing hub for the entire network:

1. Southern Trust Company liquidated assets and sent proceeds to the personal account
2. From the personal account, DDA-to-DDA transfers flowed to at least three subsidiary accounts (739123130, 739121472, 739474340)
3. Book transfers moved funds between entities internally without external wire activity
4. Southern Financial LLC had a **$1.13M AUTOMATIC TRANSFER** -- a standing sweep arrangement
5. All entities fed through the same central hub before funds were dispersed outward

### 5.2 Anomalies

- **Neptune LLC:** Suspicious $1,200 and $1,000 wires flagged by compliance
- **LSJE LLC:** Emergency **"HELP TO STOP WIRE"** order involving Richard Kahn
- **2017 Caterpillar Trust:** Returned funds triggered compliance concern
- **Harvest Collateral Yield Enhancement Strategy:** A derivatives overlay operating through harvestvolmgt.com
- **Prytanee LLC:** Appears in July 2018 balance reports. KYC principal identified as **Etienne Pierre Jean Binant** (French citizen), not Jack Lang as previously speculated. Caroline Lang was only the social introducer. $700K estate valuation (50% interest)

### 5.3 Structural Assessment

This architecture is consistent with **textbook financial layering**: one central hub account, money flowing through 18+ entities with no apparent independent business purpose, automatic sweeps, and offshore wire infrastructure. Deutsche Bank's own RM code (82289) treating all entities as one relationship is the clearest evidence that the bank knew these weren't independent businesses.

**[Full details: FORENSIC_ACCT_3_INTER_ENTITY_FLOWS.md]**

---

## 6. DEUTSCHE BANK: COMPLIANCE KNEW EVERYTHING

### 6.1 The KYC Breach

A KYC (Know Your Customer) breach was formally declared for Southern Financial in **April 2018** and tracked across at least **29 separate documents** ([EFTA01356960](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01356960.pdf) through [EFTA01406955](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01406955.pdf)).

Key compliance personnel involved:
- Akash Malhotra, Shawn Staker (initial breach handlers)
- Xavier Avila (escalation recipient)
- Mathew Negus, Joe Aglione (cc'd on escalation)
- Nina Tona, Martin Zeman (senior oversight)
- Alka Gopala, Pankaj-A Chopra (NCAOTC Derivatives)

**Despite declaring a KYC breach in April 2018, Deutsche Bank continued servicing the accounts for 8-10 more months.** Internal communications include the admission: **"kyc is not happening."**

### 6.2 The AML Inquiry

AML alerts on the Haze Trust reached the **"URGENT - THIRD REQUEST!!!!!"** level. No Suspicious Activity Report was filed until after Epstein's arrest in July 2019.

### 6.3 Timeline of Compliance Failure

| Date | Event |
|------|-------|
| May 2013 | First AML alert ([EFTA01355649](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01355649.pdf)) |
| August 2013 | Accounts opened under "Southern Financial Relationship" |
| November 2014 | Second AML activity documented |
| April 2018 | KYC breach formally declared |
| June-November 2018 | $46.96M drained from Haze Trust during active AML investigation |
| November 28, 2018 | Miami Herald publishes "Perversion of Justice" |
| July 6, 2019 | Epstein arrested |
| Post-arrest 2019 | SAR finally filed covering 25 subjects |
| January 2023 | Deutsche Bank pays $75M settlement to victims |

### 6.4 Paul Barrett: Economic Partner, Not Merely a Banker

**Paul Barrett** appears 61 times across 55 documents. He managed Epstein's accounts at JP Morgan through approximately 2013 and then at Deutsche Bank. However, DS9 evidence reveals Barrett **left Deutsche Bank by mid-2017** and founded **Alpha Group Capital LLC** with Epstein funding ($250K/yr + forgivable loans). Barrett was named as a beneficiary in Epstein's will. His relationship with Epstein was therefore that of an economic partner, not merely an institutional banker who followed a client.

- Weekly **"Epstein week of [date]"** reports for 5.5 years at Deutsche Bank
- Managed derivatives, FX trades, $10M Brazilian sovereign CDS
- NMLS ID# 853441
- 6-8 DB personnel copied on weekly reports
- **Zero compliance flags raised** during his institutional tenure
- Post-DB: founded Alpha Group Capital LLC with direct Epstein financial backing

**[Full details: [INVESTIGATION_2_DB_KYC_BREACH.md](/financial/INVESTIGATION_2_DB_KYC_BREACH.md), INVESTIGATION_7_BARRETT_REPORTS.md]**

---

## 7. THE KEY OPERATORS: KAHN, INDYKE, BARRETT

### 7.1 Richard D. Kahn (JABWCPA)

**JABWCPA@gmail.com** (290 appearances) is conclusively identified as Richard D. Kahn of HBRK Associates Inc., 575 Lexington Avenue, 4th Floor, New York, NY 10022.

- Sole authorized signer for HBRK Associates (DB Account #42953715)
- Received every Deutsche Bank financial report for all Epstein entities
- Cc'd on all wire transfers, aircraft escrow, trust management, tax filings
- HBRK Associates held its own account within the Epstein entity cluster
- **Co-executor of the estate** despite being removed as trust beneficiary
- 498 hidden text fragments reference him; 271 reference HBRK Associates

Kahn had **complete visibility** into the entire financial architecture. He was the single person who saw every number, every wire, every balance across all 18 entities.

### 7.2 Darren K. Indyke

- Epstein's personal attorney
- Held a PLLC account at Deutsche Bank within the Epstein entity cluster
- Received $1.5-2.4M from the Haze Trust drawdown
- **Co-executor of the estate** despite being removed as trust beneficiary
- Named in trust amendments alongside Maxwell, Brunel, and Kahn for deletion from Article Third

### 7.3 Paul Barrett

- Managed Epstein's accounts at JPM (pre-2013) and DB (2013 to mid-2017)
- Left Deutsche Bank by mid-2017 and founded **Alpha Group Capital LLC** with Epstein funding ($250K/yr + forgivable loans)
- Named as a beneficiary in Epstein's will
- Wrote weekly status reports on Epstein's portfolio while at Deutsche Bank
- Managed complex derivatives trading including "Harvest Collateral Yield Enhancement Strategy"
- Never raised a compliance flag during his institutional tenure managing accounts where the source of $500M+ in funds was undocumented

**[Full details: [FORENSIC_ACCT_4_JABWCPA_INSTITUTION1.md](/financial/FORENSIC_ACCT_4_JABWCPA_INSTITUTION1.md), [INVESTIGATION_7_BARRETT_REPORTS.md](/financial/INVESTIGATION_7_BARRETT_REPORTS.md), INVESTIGATION_8_UNEXPLORED_NAMES.md]**

---

## 8. THE PROMINENT NAMES DOCUMENT

### 8.1 Overview

Four variants of an FBI internal briefing document titled **"PROMINENT NAMES"** were recovered from the database. This document is part of a larger presentation on the "Jeffrey Epstein Investigations" covering FBI case numbers:
- 31E-MM-1080
- 72-MM-113327
- 50D-NY-30275
- 90A-NY-31512

### 8.2 The Four Variants

| Variant | EFTA | Key Features |
|---------|------|-------------|
| V1 | [EFTA01656152](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01656152.pdf) | Earliest; no date annotations |
| V2 | [EFTA01656173](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01656173.pdf) | Adds "Cuomo stated" detail (note: "Cuomo" is a **victim surname** -- [EFTA02696360](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02696360.pdf) confirms "Tony Cuomo" invited to Epstein's house Jan 2012 -- not Governor Andrew Cuomo); Simon Andriesz name |
| V3 | [EFTA01656198](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01656198.pdf) | Adds "(referred)" next to Jes Staley and Les Wexner |
| V4 | [EFTA01660622](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01660622.pdf) | Most complete; marked UNCLASSIFIED; date ranges; victim identifiers; removes "(referred)" notations; adds Steve Scully witness |

### 8.3 Names on the Prominent Names Page

Based on reconstruction across all four variants, the following individuals are named:

| Name | Annotation/Status |
|------|------------------|
| **William Barr** | "present during abuses" — NOT marked "(referred)" |
| **Leon Black** | Massage, oral sex, rape, trafficking allegations — NOT marked "(referred)" |
| **Jes Staley** | Marked "(referred)" in V3 |
| **Les Wexner** | Marked "(referred)" in V3; "earned his money from Wexner" |
| **Bill Clinton** | Referenced in NTOC tips |
| **Donald Trump** | Referenced in multiple NTOC tips |
| **Prince Andrew** | Referenced in NTOC tips and investigation timeline |
| **Ehud Barak** | 21+ calendar entries but NOT on PROMINENT NAMES page |

**Critical observation:** Staley and Wexner were "(referred)" for investigation. Barr and Black were not. Barr was named in an unverified NTOC tip as "present during abuses" — the same Barr who oversaw the DOJ during Epstein's arrest, detention, death, and the Maxwell prosecution. The tip was never investigated or referred, and no recusal from the active prosecution occurred.

**[Full details: [INVESTIGATION_1_BARR_NTOC.md](/individuals/INVESTIGATION_1_BARR_NTOC.md), INVESTIGATION_6_LEON_BLACK.md]**

---

## 9. WILLIAM BARR: AG UNDER INVESTIGATION BY HIS OWN FBI

### 9.1 The Allegation

From the PROMINENT NAMES document (all four variants):

> "William Barr/Leon Black: NTOC filed by [REDACTED], stated Barr and Black were present during abuses. [REDACTED] stated was at Epstein's for a model event, ran into Barr who stated he wanted to see her next time he came. At another point, Epstein asked if she had ever met Barr."

### 9.2 The Timeline Problem

| Date | Event |
|------|-------|
| February 14, 2019 | Barr confirmed as Attorney General |
| July 6, 2019 | Epstein arrested (under Barr's DOJ) |
| August 10, 2019 | Epstein dies at MCC (under Barr's BOP) |
| December 23, 2020 | Barr resigns |
| July 2020 | Maxwell arrested (under Barr's DOJ) |

### 9.3 What the Files Show

- Barr is named in an unverified NTOC tip on the FBI's own PROMINENT NAMES document as "present during abuses" at a "model event"
- **No referral annotation** exists next to his name (unlike Staley and Wexner)
- **No recusal documentation** from the active prosecution was found anywhere in the database (Barr did recuse from the retrospective NPA review due to Kirkland & Ellis ties)
- The AG who oversaw the Epstein and Maxwell cases was himself the subject of an unverified FBI tip
- FBI case 90A-NY-31512 (Epstein death investigation) was closed 12/5/2022 with no finding of foul play

**[Full details: INVESTIGATION_1_BARR_NTOC.md]**

---

## 10. LEON BLACK: THREE YEARS OF FBI INVESTIGATION, NO CHARGES

### 10.1 The Scale of Evidence

Leon D. Black appears in **47 distinct EFTA documents** in hidden text. The FBI investigated him under the classification **"Leon Black/Additional HT Subject Referral"** (HT = Human Trafficking) from **August 2021 through at least July 2024** -- over three years.

### 10.2 The Allegations

**From the PROMINENT NAMES document:**
1. Victim A: Gave Black a massage while he was naked; another female performed oral sex on Black
2. Victim B: Black "raped her numerous times and sex trafficked her... threatened to destroy her life... had connections with the police/powerful people"

**From recovered victim communications ([EFTA02731576](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731576.pdf)):**
> "Leon. You sexually harassed me, sex trafficked me, raped me, and eventually blacklisted me. I don't know for how much longer it will take me, on my own, to process the pain you caused to me and my family. The least thing you can do is to give me that document that I was forced to sign under duress and wasn't able to read before signing. Unfortunately I am still tied to you..."

### 10.3 The DANY Assessment

**Source:** Recovered from hidden text

> "DANY do not doubt her allegations against JE and LB"

The Manhattan District Attorney's office found the victim's allegations against Jeffrey Epstein and Leon Black **credible**. Photographs were provided to investigators by Wigdor LLP (victim's attorneys).

### 10.4 The Outcome

Despite 3+ years of FBI investigation, credible victim allegations confirmed by DANY, photographs, direct victim communications, and his presence on the PROMINENT NAMES page alongside documented abuse allegations:

**No charges were filed against Leon Black.**

### 10.5 The Financial Connection

Black maintained personal accounts at Deutsche Bank under the **exact same banking officers** (Litchford/Morris, then Morris/Oldfield) who managed all Epstein entities. His accounts appear on the same master roster ([EFTA01359500](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01359500.pdf)) and the same banker assignment document ([EFTA01477454](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01477454.pdf)) as every Epstein shell company.

A calendar entry records: **"Drive to Leon Blacks house with Karyna"** (Karyna Shuliak, Epstein's last girlfriend and residual trust beneficiary).

**[Full details: INVESTIGATION_6_LEON_BLACK.md]**

---

## 11. THE NTOC TIP LINE: WHAT VICTIMS REPORTED

### 11.1 Source Documents

[EFTA01660651](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01660651.pdf) and [EFTA01660679](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01660679.pdf) contain the FBI's National Threat Operations Center tip line reports related to the Epstein case. These documents contain both the allegations and the FBI's disposition notes side-by-side.

### 11.2 The Reports and Their Dispositions

#### A. Murder and Disposal of Newborn
> Complainant was "forced to perform sex acts when she was 13 years old and pregnant in 1984... high profile individuals involved in her sex trafficking and the murder and disposal of her newborn daughter."
>
> **FBI Disposition:** "no contact made."

#### B. Victim Vanished, Remains Found
> Victim 1 was drugged, woke up naked with $300 on the bed, "was never seen again. A few years ago, remains were discovered that matched the description of what Victim 1 was wearing when she went missing. DNA tests at the time were inconclusive."
>
> **FBI Disposition:** "contact made, victim identified is deceased and complainant did not have confirmed information"

#### C. Bodies at Golf Course
> "sex trafficking ring at the Trump Golf Course in Rancho Palos Verdes, CA between 1995-1996... some girls went missing, rumored to have been murdered and buried at the facility... 'end up as fertilizer for the back nine holes like the other cunts.'"
>
> **FBI Disposition:** "Complainant was spoken to and deemed not credible. Additional research showed 3 separate incidents involving police which requested mandatory psychiatric evaluations."

#### D. Robin Leach Strangulation
> "Complainant claims to have video of high-profile sex parties, dealings with cartels, and having witnessed Robin Leach strangle a young girl to death at a party"
>
> **FBI Disposition:** Same complainant as (C) -- deemed not credible.

#### E. Human Trafficking Auction
> "Sir Ivan Wilzig hosted a party where Jeffrey Epstein, Sammy Sosa, and Donald Trump were in attendance... an individual approximately 18 to 23 years of age, brought from Oklahoma for a modeling job but then sold to a man in France. Several women were being auctioned."
>
> **FBI Disposition:** "Phone number provided was bad, could not identify a valid number"

#### F. Alexander Brothers and Victoria's Secret
> "At age 16, while modeling, caller attended 8 parties at Epstein's New York residence... two twin brothers, Allen and Oren, lured caller and her friend upstairs... Oren raped her best friend and a third brother, Tal, raped a 14 year old girl named Katie LNU... individuals involved in 'big orgy parties' with young girls and older Victoria's Secret models, including Bill Clinton and Donald Trump."

#### G. "Calendar Girls"
> "Donald Trump, the president, had parties at Maralago called 'calendar girls.' Jeffrey Epstein would bring the children in and Trump would auction them off... The guests were elder men and included Elon Musk. Don Jr. Trump, Ivanka Trump, and Eric Trump were there. Attorney Allan Dershowitz was also there with Attorney Bob Shapiro."
>
> **FBI Disposition:** "No contact information provided, no DOB"

#### H. Limo Driver / Ex-Girlfriend's Daughters
> "complainant's ex-girlfriend's daughters were victims of Epstein's and one was murdered"
>
> **FBI Disposition:** "Voicemail left, no response"

### 11.3 Assessment

These are tip line reports. They represent unverified allegations from callers to the FBI. Some callers were assessed as not credible (Allegation C, with psychiatric evaluation history). Others were never contacted at all. The FBI's own disposition notes show that the majority of these tips received **minimal or no follow-up**: "no contact made," "voicemail left, no response," "phone number was bad."

The credibility of individual tips varies. What is documented is the pattern of FBI response: the majority of tips — regardless of the individuals named — received minimal or no follow-up.

**[Full details: INVESTIGATION_1_BARR_NTOC.md]**

---

## 12. GHISLAINE MAXWELL: IDENTITY ANOMALIES

### 12.1 The SSN

**[EFTA01653379](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01653379.pdf)** (NYPD firearms permit application) and **[EFTA01296720](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01296720.pdf)** (second confirmation) reveal:

- **SSN: 133-78-4883** -- A Connecticut-prefix SSN for a French-born British national with no documented Connecticut connection
- **Military Record: YES** -- No known military service for Maxwell in any country's armed forces
- **Criminal Record: YES** with **Status: APPROVED** -- A firearms permit was approved despite a declared criminal record
- **DOB discrepancy:** 1961 in one document vs. 1963 (her actual birth year) in others

### 12.2 Analysis

The Connecticut SSN prefix (130-134) was historically associated with SSNs assigned to individuals in Connecticut. For a French-born British national to have this prefix raises questions about how the SSN was obtained. The "Military Record: YES" flag is unexplained -- Maxwell has no publicly known military service, though her father Robert Maxwell had documented intelligence connections.

These anomalies were never investigated according to the recovered documents.

**[Full details: INVESTIGATION_5_MAXWELL_SSN.md]**

---

## 13. THE OBSTRUCTION WIRES: $350K AFTER THE HERALD STORY

### 13.1 The Sequence

| Date | Event |
|------|-------|
| November 28, 2018 | Miami Herald publishes "Perversion of Justice" |
| November 28, 2018 (morning) | Epstein has breakfast with **Ehud Barak** |
| November 30, 2018 | **$100,000 wired** to NPA co-conspirator |
| December 3, 2018 | **$250,000 wired** to another individual |
| December 6, 2018 | FBI opens New York investigation |

### 13.2 Government Classification

The Government classified both wire transfers under an **"Obstru[ction]"** header in its investigation files. These were transfers to individuals named as **"possible co-conspirator[s] in the NPA"** -- the 2008 Non-Prosecution Agreement.

### 13.3 What Happened

$350,000 was wired to NPA co-conspirators within 2-5 days of the story that reignited public scrutiny of the Epstein case. The Government identified these as potential obstruction of justice.

**No obstruction charges were ever filed.**

**[Full details: [INVESTIGATION_4_2018_WIRE_RECIPIENTS.md](/financial/INVESTIGATION_4_2018_WIRE_RECIPIENTS.md), FORENSIC_ACCT_5_CALENDAR_CORRELATION.md]**

---

## 14. CALENDAR INTELLIGENCE: MEETINGS MAPPED TO MONEY

### 14.1 Recovered Calendar Entries

Over 100 calendar/appointment entries were recovered from hidden text, mapping Epstein's daily schedule:

**High-profile meeting partners:**
- Leon Black (multiple entries)
- Ehud Barak (21+ entries including November 28, 2018)
- Larry Summers (economist, former Treasury Secretary)
- Noam Chomsky (linguist/professor)
- Dan Gilbert (Quicken Loans founder)
- Tom Pritzker (Hyatt Hotels)
- Mort Zuckerman (media mogul)
- Jes Staley (JPMorgan/Barclays)
- Tom Barrack (Colony Capital)
- Andrew Farkas (Inland Western)
- Maxim Churkin (Russian diplomat, died under suspicious circumstances 2017)

### 14.2 The Tom Barrack - UAE Connection

Calendar entries show Epstein brokered meetings between Tom Barrack and **"H.E. Sheikh"** (likely Sheikh Abdullah Bin Zayed). Barrack was later **federally indicted** for acting as an unregistered foreign agent for the UAE. Epstein was facilitating the exact relationship that became a federal case.

### 14.3 Calendar Entry: "Drive to Leon Blacks house with Karyna"

This entry places Epstein and Karyna Shuliak (his last girlfriend and residual trust beneficiary) at Leon Black's residence -- connecting the personal, financial, and alleged criminal elements in a single documented movement.

**[Full details: FORENSIC_ACCT_5_CALENDAR_CORRELATION.md]**

---

## 15. THE POST-DEATH ESTATE: $600M WITH A $228M GAP

### 15.1 Estate Valuation

The USVI Attorney General valued the estate at over **$600 million** and placed liens on it in January 2020 under the Criminally Influenced and Corrupt Organizations Act (CICO).

### 15.2 Trust Beneficiaries

**Source:** [EFTA01266168](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01266168.pdf) (primary trust document, recovered from badly overlaid redactions across 30 pages)

| Beneficiary | Amount |
|-------------|--------|
| Redacted Female 1 | $10,000,000 |
| Redacted Female 2 | $4,000,000 |
| Redacted Female 3 | $2,000,000 |
| Redacted Female 4 | $2,000,000 |
| **Karyna Shuliak** | Residual interest + all property proceeds |
| Merwin Dela Cruz | Named beneficiary (staff member) |
| Lyn & Jojo Fontanilla | Membership interests in entity |

### 15.3 Trust Amendments: Beneficiary Deletions

Epstein executed amendments to **remove** the following from Article Third:
- **Ghislaine Maxwell**
- **Jean-Luc Brunel**
- **Darren Indyke**
- **Richard Kahn**

Despite being removed as beneficiaries, **Indyke and Kahn remained as co-executors** -- the people controlling the estate's disposition were people Epstein had cut out of the inheritance.

### 15.4 The $228M Gap

| Documented Assets | Approximate Value |
|-------------------|------------------|
| Haze Trust (peak) | $49.5M + $12.7M |
| Southern Trust (peak) | $45.15M |
| Southern Financial | $7M |
| 9 East 71st Street, Manhattan | $13M appraisal |
| 358 El Brillo Way, Palm Beach | (not recovered) |
| Gulfstream IVSP S/N 1305 | $13M listing price |
| 2x Sikorsky helicopters | (not recovered) |
| Other entities | partial balances |
| **Total documented** | **~$372M** |
| **USVI AG valuation** | **$600M+** |
| **UNACCOUNTED** | **~$228M** |

The gap likely sits across JP Morgan Chase accounts (pre-2013), FirstBank Puerto Rico, the Paris apartment, art/personal property, Little St. James Island, Great St. James Island, the New Mexico ranch, and the 2007 Insurance Trust.

### 15.5 Post-Death Aircraft Sales

- Gulfstream IVSP listed at $12,995,000
- Helicopter N722JE escrow via AIC Title Service finalized **May 2021** -- 22 months after death
- Participants: Indyke, Kahn, pilot Larry Visoski

**[Full details: FORENSIC_ACCT_6_POST_DEATH_ASSETS.md]**

---

## 16. THE ISLAND: HIDDEN STRUCTURES AND TUNNELS

### 16.1 Hidden Structures

**[EFTA01307744](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01307744.pdf)** contains FBI aerial surveillance notes:
> "D3: Dome not seen on video footage / Potential Single Story Structure"
> "Yellow Square: Potential Hidden Structure"

The FBI documented structures on Little St. James Island that did not appear on video footage -- suggesting concealed or underground construction.

### 16.2 Tunnel Infrastructure

Multiple emails document tunnel maintenance:
- **[EFTA01809063](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01809063.pdf), [EFTA01809071](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01809071.pdf):** "Tunnel electrical (fixed)" -- maintenance emails involving Ann Rodriguez, Lesley Groff
- **[EFTA01808632](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01808632.pdf):** "Tunnel" -- Richard Kahn, Stephanie Remington
- **"Wallace Tunnel"** referenced with Richard Kahn

These are confirmed structures on Epstein's island properties, maintained by his staff.

### 16.3 Property Managers: Brice and Karen Gordon

**Brice Gordon** and **Karen Gordon** served as island property managers with **New Zealand Defence Force** backgrounds. They appear in **826+ documents**, managing everything from construction to staffing to supply logistics.

Both left their positions after Epstein's death in August 2019 and their subsequent whereabouts are not documented. No indication the FBI pursued them as witnesses.

---

## 17. THE BLACKMAIL DOCUMENT

### 17.1 Source

**[EFTA01731006](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01731006.pdf)** -- FBI Serial 230, Case 31E-MM-108062

### 17.2 Content

A Slovakian citizen working with Epstein was documented as **"attempting to blackmail powerful businessmen in New York."** Epstein "suggests names of individuals" and "offers to provide contacts."

Additional names referenced are found in "Serial 984 with EPSTEIN (DATED: 1 August 2006)."

### 17.3 Significance

This is an FBI document describing an organized blackmail operation involving Epstein. It is consistent with -- but does not explicitly confirm -- the widely reported theory that Epstein operated a sexual blackmail/kompromat scheme. No state actor is named in the document.

---

## 18. UNEXPLORED NAMES AND DISAPPEARED WITNESSES

### 18.1 Jojo and Lyn Fontanilla

**826 appearances** across the document corpus. Court documents state they had knowledge of **"inappropriate conduct with underage girls."** They received membership interests in an Epstein entity through the trust. No prosecution.

### 18.2 Barry Josephson

Hollywood producer who discussed **"casting girls"** for Epstein's jet and received **$335,000** from Epstein. No prosecution.

### 18.3 Leon Botstein

President of Bard College. Planned an island visit and hosted Epstein events with **5 "girls"** present. No prosecution.

### 18.4 Brice and Karen Gordon

Island property managers with NZ Defence Force backgrounds. Left positions after Epstein's death; subsequent whereabouts not documented. Not pursued as witnesses.

### 18.5 Eight Deutsche Bank Employees

At least 8 Deutsche Bank employees appear extensively in hidden text as active participants in managing the accounts: Tazia Smith, Bradley Gillin, Stewart Oldfield, Paul Barrett, Martin Zeman, Paul Morris, Jj Litchford, Richard Iarossi. Deutsche Bank paid a $150M fine. No individual was prosecuted.

**[Full details: INVESTIGATION_8_UNEXPLORED_NAMES.md]**

---

## 19. THE VICTORIA'S SECRET PIPELINE

### 19.1 Ed Razek

**[EFTA00014526](https://www.justice.gov/epstein/files/DataSet%208/EFTA00014526.pdf):** An L Brands executive who helped select Victoria's Secret models was invited to Epstein's Manhattan mansion and "welcomed by young women."

### 19.2 The Alexander Brothers

NTOC tip: **Allen, Oren, and Tal** (possibly the Alexander brothers) attended parties at Epstein's with "young girls and older Victoria's Secret models."

### 19.3 Les Wexner

- Founder of L Brands / Victoria's Secret
- On the PROMINENT NAMES page
- Marked "(referred)" for investigation in Variant 3
- The only named source of Epstein's wealth: "earned his money from Wexner"
- Transferred the 9 East 71st Street mansion to Epstein

---

## 20. WHAT THE FILES DO NOT CONTAIN

Across 1,808,915 redactions from all 12 DOJ datasets, the following claims popular in public discourse have **zero evidentiary support** in the recovered text:

| Claim | Result |
|-------|--------|
| Satanic rituals | Zero references |
| Cannibalism | Zero references |
| Occult practices | Zero references |
| Human sacrifice | Zero references |
| Adrenochrome | Zero references |
| Mossad/MI6/CIA direct involvement | George Tonks' social media posts collected by FBI; additionally, FBI CHS FD-1023 ([EFTA00090314](https://www.justice.gov/epstein/files/DataSet%209/EFTA00090314.pdf)) contains an unverified confidential human source claim that Epstein "belonged to both U.S. and allied intelligence services" and "trained as a spy under" Barak. The CHS claim is unverified but the document exists in the FBI case file |
| Netanyahu/Bibi connection | Zero references |
| Underground torture chambers | Hidden structures documented but no torture references |

**What IS in the files is arguably more significant than these conspiracy theories:** systematic sex trafficking, organized blackmail, hundreds of millions in unexplained wealth, institutional banking complicity, and a pattern of non-investigation of the most powerful alleged participants.

---

## 21. PATTERN OF NON-INVESTIGATION

This is the most significant finding of the entire analysis. The documents do not reveal a conspiracy that was hidden from law enforcement. They reveal a conspiracy that was **documented by law enforcement and not acted upon.**

| Evidence | Action Taken |
|----------|-------------|
| NTOC tip: 13-year-old raped, newborn murdered | "no contact made" |
| NTOC tip: woman vanished, remains found | "victim identified is deceased" -- closed |
| NTOC tip: human trafficking auction | "Phone number was bad" -- closed |
| NTOC tip: ex-girlfriend's daughter murdered | "Voicemail left, no response" -- closed |
| William Barr named in unverified NTOC tip as "present during abuses" | No referral, no investigation of tip, recused only from NPA review |
| Leon Black: DANY found victim credible, 3yr FBI investigation | No charges filed |
| Deutsche Bank KYC breach declared April 2018 | Accounts serviced 8-10 more months |
| $46.96M Haze Trust drawdown during active AML inquiry | No account freeze |
| $350K wired to NPA co-conspirators after Herald exposure | No obstruction charges |
| Paul Barrett managed accounts at JPM and DB, then left DB mid-2017 to found Alpha Group Capital LLC with Epstein funding | Zero compliance flags while at banks; became economic partner |
| Fontanillas knew of "inappropriate conduct with underage girls" | No prosecution (826 appearances) |
| Barry Josephson discussed "casting girls," received $335K | No prosecution |
| Maxwell SSN anomalies (CT prefix, "Military Record: YES") | Never investigated |
| $500M+ in wealth with zero documented legitimate source | Not explained in any charging document |
| $228M gap in estate accounting | Not publicly accounted for |

The pattern is not "we didn't know." The pattern is **"we knew, we documented it, and the vast majority of named individuals were never charged."**

---

## 22. ADDENDUM: GAP ANALYSIS FINDINGS (February 5, 2026)

This section incorporates findings from a comprehensive gap analysis conducted across all 12 DOJ datasets, including material from datasets (DS8, DS9, DS12) that had not been fully processed in the original analysis. These findings significantly expand the evidentiary record documented in Sections 1-21.

### 22.1 The Complete FBI PROMINENT NAMES List

The original report (Section 8) documented only four names from the FBI's internal "PROMINENT NAMES" presentation: Barr, Black, Staley, and Wexner. The full list recovered from all four variants of the document is substantially longer:

| Name | Allegations | Status |
|------|-------------|--------|
| Donald Trump | 2 victim statements | Not referred |
| Harvey Weinstein | 3 victim statements | Not referred |
| Glen Dubin | 1 victim statement | Not referred |
| Prince Andrew | 3 victim/witness statements (including Steve Scully -- witness with criminal history) | Not referred |
| Jes Staley | 1 victim statement - "told to give Staley a massage, Staley forced her to put her hands on his [crotch] and had 'rough sex' with her" | **(referred)** |
| Leon Black | 2 victim statements - massage/oral sex, rape/trafficking | Not referred |
| Les Wexner | 1 victim statement - "earned his money from having homosexual [sex with] Wexner" | **(referred)** |
| Alan Dershowitz | 1 statement - massage on plane ("not a minor") | Not referred |
| Bill Clinton | 1 statement - "invited to an orgy but did not attend" ("not a victim") | Not referred |
| Howard Lutnick | 1 NTOC tip (financial allegations); DS9 reveals **20+ documents** showing active social relationship (2011-2013) including calendar appointments, Lutnick family visit to Little St. James Island by boat (Dec 2012), document sharing, and placement on same call list as Leon Black/Nikolic/Staley/Brockman | Not referred |
| William Barr/Leon Black | Joint entry - "Barr and Black were present during abuses" | Not referred, no recusal |

**Note:** Howard Lutnick is currently U.S. Secretary of Commerce (2025-present).

### 22.2 MCC Surveillance Failure -- DVR2 Down for 11 Days

From [EFTA01660622](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01660622.pdf) (FBI internal presentation):

- **DVR2** (covering Epstein's area): system failure **7/29/2019 - 8/9/2019**
- BOP discovered DVR2 was not recording on **8/8/2019** -- two days before death
- DVR1 was functioning
- Approximately 150 cameras total at MCC
- Over 400 hours of video reviewed from 7/23/2019 - 8/10/2019
- 5 times inmate head count was not conducted
- COs **Michael Thomas** and **Tovar**: charged with False Records, deferred prosecution agreement, "terms satisfied"
- **Efrain Reyes** (last cellmate) proffer on 8/16/2019 -- handwritten note garbled in all copies
- Case 90A closed **12/5/2022**, no criminality found
- **MCC Chief Psychologist approved removal from suicide watch on 7/29/2019 -- the same day DVR2 failed**

### 22.3 MC2 Model Management -- "Age: Between 13 and 20"

**[EFTA01728258](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01728258.pdf):** Full MC2 website cached from 8/15/2007. The scouting division submission requirements explicitly state an age range of **13-20 years old**. This is direct documentary evidence of the recruitment pipeline's age targeting. MC2 was operated by Jean-Luc Brunel in conjunction with Epstein.

### 22.4 The Brunel "Commission" Email

**[EFTA01986452](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01986452.pdf):** Email from Daniel Siad to Jean-Luc Brunel with subject: **"Commission de mes 2 filles Chez toi"** ("Commission for my 2 daughters at your place"). Brunel operated MC2 Model Management and was deleted from Epstein's trust before dying in French custody in 2022.

### 22.5 Seven Discs of Monitored Phone Calls

**[EFTA02730741](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02730741.pdf)** (DS12, classified U//FOUO): **"DVD/CD'S OF CONSENSUALLY MONITORED PHONE CALLS"** -- 7 discs of recordings, plus consent-to-search forms (FD-26, FD-395). This represents a substantial body of recorded communications that formed part of the FBI's evidence base.

### 22.6 The FBI Master Case File Index

**[EFTA01731021](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01731021.pdf)** contains the structural index of the entire investigation, including:
- Arrest paperwork
- Search warrants
- Photographs
- Interview of Jean-Luc Brunel (multiple entries)
- Search warrant executed on Little St. James
- Seizure of items from safe including "DVD of photos"
- Inventory of two suitcases
- Flight logs
- Multiple proffer sessions
- Contact records with Florida victims

### 22.7 Bitcoin, Cryptocurrency, and Carbyne/Reporty Investment

A financial dimension of Epstein's operations that extends beyond Bitcoin to documented technology investments. DS9 contains 50+ Carbyne and 324 Reporty documents showing Epstein invested $500K in Carbyne/Reporty (a surveillance technology company co-founded by Ehud Barak), with Barak holding a $1.5M carry at a $50M valuation. Board reports were forwarded to Epstein. Additional cryptocurrency references:

- **[EFTA01734786](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01734786.pdf):** "Bitcoin Specialization - October 2015 LedgerX - Confidential"
- **[EFTA02070051](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02070051.pdf):** "would you and the Bitcoin group" -- Epstein had a "Bitcoin group"
- **[EFTA02069096](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02069096.pdf):** "Bitcoins for Mongolia" project
- Multiple connections to Blockchain Capital (blockchaincapital.com)

These references indicate Epstein was involved in cryptocurrency as early as 2015, including what appears to be a specialized team ("the Bitcoin group"), connections to a regulated Bitcoin derivatives exchange (LedgerX), and an international cryptocurrency project involving Mongolia.

### 22.8 "34 Victims, Only 3 Contacted by FBI"

**[EFTA00027666](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027666.pdf):** "In addition to Jane Doe I, FBI agents only talked to two other victims out of the 34." During the NPA-era investigation, the FBI identified **34 victims** and contacted only **3**. This statistic quantifies the institutional failure documented throughout Section 21.

### 22.9 Harvard / Lawrence Summers / George Church Network

Epstein maintained deep institutional ties to Harvard University:

- **8+ documents** with emails from "Harvard Kennedy School, Office of Lawrence H. Summers"
- Regular Epstein visits to Harvard documented ("He will be at Harvard Fri. Dec. 6th," "Jeffrey is coming to Harvard this Saturday, May 4th")
- Direct email to **George Church** at Harvard Medical School (church@gmc.harvard.edu) -- Church runs a synthetic biology/genomics laboratory
- Connection to **christakis.med.harvard.edu** (Nicholas Christakis, social scientist)
- Stanford connection: **Lorry Lokey Visiting Professor**

The Harvard network represents a significant academic institutional relationship that facilitated Epstein's access to scientific and policy circles. Lawrence Summers served as Harvard's president from 2001-2006, overlapping with Epstein's peak activity period.

### 22.10 Maxwell Trial Details and Perjury Charges Dropped

From [EFTA01660622](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01660622.pdf):

| Count | Charge | Verdict |
|-------|--------|---------|
| 1 | Conspiracy to Entice Minors | **Guilty** |
| 2 | Enticement of a Minor | Not Guilty |
| 3 | Conspiracy to Transport Minors | **Guilty** |
| 4 | Transportation of a Minor | **Guilty** |
| 5 | Sex Trafficking Conspiracy | **Guilty** |
| 6 | Sex Trafficking of a Minor | **Guilty** |

- **2 Perjury charges were intended to be litigated at a later time; SDNY chose not to pursue after initial trial**
- Sentenced **6/28/2022**: 20 years, 5 years supervised release, $750,000 fine
- Appeal denied **9/17/2024**
- Writ of Certiorari filed **4/10/2025**
- DOJ opposed **7/22/2025**

The decision by SDNY to drop perjury charges is significant because Maxwell's documented false statements under oath were a key element of the obstruction pattern.

### 22.11 Evidence Destruction

**DS12:** Someone **"admitted to burning handwritten notes."** Maxwell directed a victim to Weinstein. A **13-14 year old** was recruited while "sitting at a picnic table with friends when Ghislaine Maxwell walked by." These fragments from the classified DS12 materials document both the destruction of evidence and the age of recruitment targets.

### 22.12 Bill Clinton Africa Trip

**[EFTA00038617](https://www.justice.gov/epstein/files/DataSet%208/EFTA00038617.pdf)** (DS8): Redacted interview referencing **"Bill Clinton during a trip to Africa in 2002 on Epstein's plane"** with the statement **"said that there were no minors on"** the trip. The defensive framing -- specifically denying minors were present -- is notable in the context of the broader investigation.

### 22.13 The Anonymous Tip About Video Footage

**[EFTA00038382](https://www.justice.gov/epstein/files/DataSet%208/EFTA00038382.pdf)** (DS8): Confidential tip stating **"What is damning about Jeffrey Epstein is yet to be written"** with references to **"video footage of Jeffrey Epstein"** being sent **"anonymously by overnight courier."** This tip references the existence of compromising video material and an anonymous effort to distribute it.

### 22.14 Dataset 8: MCC Surveillance Footage (412.5 Hours)

**CRITICAL FINDING:** The 419 MP4 files in DS8 are **MCC (Metropolitan Correctional Center) jail surveillance recordings** from Epstein's entire detention period (July 6 - August 11, 2019). Frame extraction confirmed on-screen camera IDs and timestamps from the 9 South Special Housing Unit.

**Five camera positions identified:**
- **C-B14** — Epstein's individual cell (overhead fish-eye, labeled "J Epstein")
- **U9S J Tier-114** — J Tier corridor with cell doors
- **160 SW 2,80** — Stairwell/entry area with reception counter
- **116 9S L TIER,B2** — Guard station where COs Noel/Thomas were stationed
- **150 9S 2,82** — Corridor near fire exit

**Key footage:**
- **[EFTA00028842](https://www.justice.gov/epstein/files/DataSet%208/EFTA00028842.pdf):** Camera C-B14 showing Epstein's cell at **04:29 AM on August 10, 2019** — approximately 2 hours before his body was found. A figure in orange is visible.
- **[EFTA00033350](https://www.justice.gov/epstein/files/DataSet%208/EFTA00033350.pdf):** Guard station camera on **07/29/2019 at 21:01** — the night of the first suicide attempt, DVR2 failure, and suicide watch removal.
- **[EFTA00033400](https://www.justice.gov/epstein/files/DataSet%208/EFTA00033400.pdf):** Guard station camera on **08/09/2019 at 04:01** — the night before death.
- **[EFTA00033040](https://www.justice.gov/epstein/files/DataSet%208/EFTA00033040.pdf):** Stairwell camera on **07/06/2019** — the day of arrest.

The DOJ publicly released 412.5 hours of the surveillance footage that was at the center of enormous public controversy about what happened the night Epstein died. Four completely redacted CSV files ([EFTA00016338](https://www.justice.gov/epstein/files/DataSet%208/EFTA00016338.pdf)-16341, 2.55 MB) in the same dataset had every cell replaced with Unicode block characters — unique across the entire 218GB release.

**Additional DS8 findings:** FBI seized device inventory listing 62+ electronic devices including UniFi surveillance system components, "Kitchen Mac 4TB," and a Panasonic PBX phone system from Epstein's properties. Victim pseudonym list documenting 6 victims with abuse dates spanning 2000-2014. 267-entry massage contact list organized by region.

### 22.14a DS8 Deep Text Extraction (136,255 Redactions)

Full deep extraction of all 10,594 DS8 PDFs recovered **32,384 additional hidden text fragments** that the original scan missed, bringing DS8 to **95,263 entries with text** (78,377 substantive) out of 136,255 total redactions.

**Key newly recovered content:**
- **[EFTA00016084](https://www.justice.gov/epstein/files/DataSet%208/EFTA00016084.pdf):** Complete **Angara Trust** filing — Ghislaine Maxwell's irrevocable trust, established 09/15/2016, with grantor, trustee, address, phone, email, net worth, and income fields (values redacted)
- **[EFTA00028568](https://www.justice.gov/epstein/files/DataSet%208/EFTA00028568.pdf):** Palm Beach police officer's account of **search warrant execution at 358 El Brillo Way** on October 20, 2005: "immediate contact was made with three white males who came out of the house"
- **[EFTA00030491](https://www.justice.gov/epstein/files/DataSet%208/EFTA00030491.pdf):** FBI proffer detailing Epstein's **complete aircraft history**: G2B from ~1990s (silver with burgundy stripe), Boeing 727, G4 purchased ~2010s, first helicopter
- **[EFTA00024584](https://www.justice.gov/epstein/files/DataSet%208/EFTA00024584.pdf):** Government filing stating search warrants produced **"sexually suggestive photographs of fully- or partially-[nude]...appear to be of underage girls, including at least one girl [under]age"**
- **[EFTA00019314](https://www.justice.gov/epstein/files/DataSet%208/EFTA00019314.pdf):** Description of trafficking operation: **"underage victims, who ranged in age from 14 to 17 years old"** — Maxwell met them, walked them up, set up massage table, paid cash
- **[EFTA00032148](https://www.justice.gov/epstein/files/DataSet%208/EFTA00032148.pdf):** BOP email dated **7/30/2019**: **"Inmate Epstein #76318-054 is being t[ransferred from]...appropriate cellmate. Suicide Watch: None. Psych Observation: None"**
- **[EFTA00019119](https://www.justice.gov/epstein/files/DataSet%208/EFTA00019119.pdf):** Complete **Section 1512** (witness tampering) negotiation thread between SDNY prosecutors and Maxwell defense attorneys
- **[EFTA00030271](https://www.justice.gov/epstein/files/DataSet%208/EFTA00030271.pdf):** Epstein **flight log entry**: "9/16/2004 10:16:00 PM — Epstein's Flight arrives at PBIA (Boeing 727)"
- **[EFTA00038329](https://www.justice.gov/epstein/files/DataSet%208/EFTA00038329.pdf):** Maxwell **alias list**: 19 name variations including "BORGERSON" — confirming use of partner's surname

### 22.14b Remaining Dataset Blind Spots

| Dataset | Material | Status |
|---------|----------|--------|
| Dataset 9 | 109 PDFs scanned for annotation-style redactions — 0 found (text properly removed, not overlaid). DS9 contains **531,284 documents** with full text including the email corpus, calendars, and FBI investigative documents | Complete |
| Dataset 8 | 419 MCC surveillance videos cataloged and frame-extracted | Complete |
| Dataset 8 | 136,255 redactions extracted, 95,263 with text | **Complete** |
| Dataset 8 | 4 completely block-redacted CSV files (2.55 MB) | Cannot be bypassed |
| All datasets | Image analysis limited to Dataset 1 only (17,578 of potentially 500K+ images) | Partial |

**Updated database totals:** 1,808,942 redactions across all datasets, 648,617 with extracted text, 519,520 substantive (>3 characters).

### 22.15 Wexner Wealth Source -- Sexual Relationship Alleged

The FBI Prominent Names document records a victim statement that Epstein **"earned his money from having homosexual [sex with] Wexner"** -- not merely a business relationship but an alleged sexual one. This is distinct from the "earned his money from Wexner" formulation previously reported in Section 3.2, and adds a dimension suggesting the financial relationship may have been intertwined with sexual conduct.

### 22.16 The 13 Confirmed Victim-Perpetrator Links

The evidence database maps **13 formal victim-perpetrator links** naming the following individuals:

1. Jeffrey Epstein
2. Ghislaine Maxwell
3. Leon Black
4. Jes Staley
5. Prince Andrew
6. Glen Dubin
7. Harvey Weinstein
8. Jean-Luc Brunel
9. Sarah Kellen
10. Nadia Marcinkova

These are not tip-line allegations or unverified reports. These are links established through victim statements, witness testimony, and documentary evidence in the FBI's own files.

---

## 23. DEEP DOCUMENT INVESTIGATION -- CRITICAL FINDINGS (February 6, 2026)

This section documents findings from the deep document investigation session conducted on February 6, 2026. These findings derive from targeted examination of specific high-value documents within Dataset 8 and cross-referenced materials, including rendered PDF review, verification of previously extracted claims, and identification of new evidentiary leads.

### 23.1 MCC Death Investigation Evidence

Multiple documents recovered from DS8 provide granular detail about the Metropolitan Correctional Center's systemic failures in the days and hours surrounding Epstein's death on August 10, 2019.

**[EFTA00017950](https://www.justice.gov/epstein/files/DataSet%208/EFTA00017950.pdf): FBI Technical Update on MCC Video Extraction (August 14, 2019)**

This FBI document confirms the following technical facts about MCC surveillance infrastructure:
- MCC operated **2 DVR surveillance systems**, each with **16 hard drives**
- On **07/29/2019** (11 days before death), **DVR system #2 had 2-3 hard drives fail**
- **2 of the 3 camera feeds "of obvious interest"** were on the failed DVR system #2 -- meaning they were **NOT recording at the time of death**
- Only **1 camera of interest** was on the working DVR system #1
- FBI FAVU (Forensic Audio, Video and Image Analysis Unit) was extracting video; C-19 maintaining **24/7 presence** at MCC
- NiceVision contractor arrived **08/12** (2 days after death) to replace what was described as an "antiquated" system

The DVR failure on July 29 coincides with the removal of suicide watch (also July 29, per Section 22.2) — a temporal correlation that has been widely noted but for which no causal connection has been established in the available documents.

**[EFTA00027104](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027104.pdf): MCC Interviews Update (August 12-13, 2019)**

FBI interviews of MCC staff in the 48-72 hours after Epstein's death revealed:
- At least **7 officers + 2 supervisors** knew Epstein had no cellmate on Friday night (August 9) but **did NOT assign one**
- **3 officers refused to speak to FBI** without union representation
- Officers admitted they **did NOT conduct the 3 AM and 5 AM counts** -- one stated: "we messed up"
- One officer was **"not aware the cameras were not working in SHU"**
- Epstein made a phone call claiming to call his mother but was overheard making **"small talk with male individual"** -- the call was placed on an **unrecorded legal line**, bypassing standard monitoring
- **2 officers who discovered Epstein's body refused to speak with FBI** -- one answered the phone, then claimed he was not himself, and hung up

This document establishes that the failures were not limited to the two officers (Thomas and Noel) who were ultimately charged. At minimum, 9 staff members were aware that Epstein had no cellmate and failed to address the lapse in security protocols on the night of his death.

**[EFTA00032148](https://www.justice.gov/epstein/files/DataSet%208/EFTA00032148.pdf): BOP Email (July 30, 2019)**

A BOP email sent to **71 BOP staff members** confirmed that Epstein was being taken off **both Suicide Watch and Psychological Observation** simultaneously. This email was sent the day after the July 29 DVR failure and first suicide attempt. The breadth of distribution -- 71 recipients -- means the removal from protective monitoring was widely known throughout the facility.

**[EFTA00034969](https://www.justice.gov/epstein/files/DataSet%208/EFTA00034969.pdf): Extension Cord Memo**

An internal memo documenting an extension cord provided to Epstein for a CPAP (Continuous Positive Airway Pressure) machine. This extension cord represents a **potential ligature** that was permitted in a cell where a suicide watch had just been removed. Standard BOP protocol prohibits items that could serve as ligature points for inmates with suicide risk.

**[EFTA00035225](https://www.justice.gov/epstein/files/DataSet%208/EFTA00035225.pdf) / [EFTA00035087](https://www.justice.gov/epstein/files/DataSet%208/EFTA00035087.pdf): Handwritten Suicide Watch Observation Logs**

Actual handwritten observation logs from the suicide watch period -- **28 pages each**, scanned. These are the primary source documents against which investigators examined whether entries were falsified or fabricated after the fact.

**[EFTA00018870](https://www.justice.gov/epstein/files/DataSet%208/EFTA00018870.pdf): Monitoring Compliance Report**

Confirms checks should have been conducted **every 30 minutes**. Investigators were actively examining whether the monitoring logs were falsified -- consistent with the charges later brought against officers Thomas and Noel for false records.

**[EFTA00036175](https://www.justice.gov/epstein/files/DataSet%208/EFTA00036175.pdf): MCC Phone Records (August 9, 2019)**

**101 pages** of phone records from MCC on the day before Epstein's death. These records document the full communication traffic at the facility on the critical date.

**[EFTA00036635](https://www.justice.gov/epstein/files/DataSet%208/EFTA00036635.pdf): Warden's Message to All Staff (August 12, 2019)**

The warden's facility-wide communication issued two days after Epstein's death.

### 23.2 Prince Andrew Interview Negotiations ([EFTA00030190](https://www.justice.gov/epstein/files/DataSet%208/EFTA00030190.pdf))

An **11-page** complete email chain between SDNY prosecutors and **Blackfords LLP** (Gary Bloxsome), the UK law firm representing Prince Andrew, reveals the full timeline of the attempted interview and subsequent public dispute:

| Date | Event |
|------|-------|
| January 2, 2020 | SDNY first contacts Bloxsome |
| January 3, 2020 | Bloxsome confirms representation of **"HRH The Duke of York"** |
| January 10, 2020 | Phone call in which SDNY promises confidentiality regarding the interview process |
| January 20, 2020 | Bloxsome states Andrew has **"strong desire to cooperate"** but needs 2+ weeks to prepare |
| January 27, 2020 | US Attorney Geoffrey Berman publicly states Andrew has provided **"zero cooperation"** |
| February 3-5, 2020 | Bitter exchange -- Bloxsome accuses SDNY of **breaking confidentiality promises** made during January 10 call |
| June 2020 | **US Embassy Paris** now involved; discussions about diplomacy with **UK Home Office** |

This email chain documents a significant breakdown in international legal cooperation. The timeline shows that Andrew's counsel was engaged and claiming willingness to cooperate, but SDNY went public with accusations of non-cooperation within one week of the last communication -- before the requested preparation period had elapsed. The subsequent involvement of both the US Embassy in Paris and the UK Home Office elevated this from a criminal investigation matter to a diplomatic incident.

### 23.3 Jean-Luc Brunel MLAT Request ([EFTA00030842](https://www.justice.gov/epstein/files/DataSet%208/EFTA00030842.pdf))

A **5-page** document detailing SDNY's work with the **US Embassy Paris** on Jean-Luc Brunel in January 2021:
- An **MLAT (Mutual Legal Assistance Treaty) request** was sent to France
- A meeting at the Embassy **"went well"** -- substance heavily redacted
- Context: Brunel was arrested in Paris on **December 16, 2020**; he was found dead in his cell on **February 19, 2022**

Brunel is the second key figure in the Epstein network to die in custody before trial. The MLAT request confirms SDNY was actively pursuing evidence through French legal channels.

### 23.4 Cell-Site Simulator Warrant ([EFTA00018663](https://www.justice.gov/epstein/files/DataSet%208/EFTA00018663.pdf))

A **33-page** federal warrant authorizing the use of a **cell-site simulator** (commonly known as a "Stingray" device) to locate Ghislaine Maxwell's cellular device:
- Filed **under seal** in the **District of New Hampshire**
- Identified Maxwell's phone as being in contact with **Haddon, Morgan & Foreman** (her civil litigation attorneys in Denver, Colorado)
- Contains a detailed **factual background** about Maxwell's crimes including grooming, sexual abuse, and lying under oath
- Includes **deposition excerpts** referencing three-way sexual activities

The use of a cell-site simulator -- a surveillance tool that mimics a cell tower to intercept phone signals -- indicates the level of resources deployed to locate Maxwell during her period of hiding in New Hampshire. The New Hampshire filing jurisdiction is consistent with Maxwell's eventual arrest in Bradford, NH on July 2, 2020.

### 23.5 Anonymous Extortion Attempt ([EFTA00038382](https://www.justice.gov/epstein/files/DataSet%208/EFTA00038382.pdf))

A **ProtonMail email** from an individual claiming to be a **"former staff at the Zorro"** (Zorro Ranch, Epstein's New Mexico property):
- Claims to possess **7 video/audio files** from Epstein's home including a **"sex video with minor"** and a **"rape fantasy video"**
- Demands **1 bitcoin** payment
- Forwarded to SDNY on **November 25, 2019**

This extortion attempt is notable for two reasons: first, it references the existence of video recordings at Epstein properties, which is consistent with the broader pattern of surveillance-based kompromat (see Section 17); second, the claim originates from someone identifying as former staff at a specific property, suggesting insider knowledge. Whether the claimed recordings exist is not confirmed in the available documents.

### 23.6 AT&T Cell Phone Records ([EFTA00017143](https://www.justice.gov/epstein/files/DataSet%208/EFTA00017143.pdf))

A **558-page** complete AT&T Mobility records dump:
- Case reference: **2996479**
- Date range: **March 1 -- June 15, 2020** (the Maxwell investigation period, covering the 4 months before her July 2 arrest)
- 558 pages of **call detail records**
- Records stored in **UTC**; **Eastern Time Zone** queried

This represents one of the largest single communications surveillance records in the dataset and covers the critical period during which law enforcement was tracking Maxwell's movements and communications prior to her arrest.

### 23.7 Verification Report Summary

A systematic verification exercise was conducted against 10 key claims from the investigation, rendering the source PDFs to confirm the accuracy of extracted text. Results:

| Claim | Document | Status |
|-------|----------|--------|
| Maxwell SSN 133-78-4883 | NYPD firearms application | **Confirmed** |
| Angara Trust irrevocable trust | [EFTA00016084](https://www.justice.gov/epstein/files/DataSet%208/EFTA00016084.pdf) (32-page UBS document) | **Confirmed** -- established 09/15/2016, Maxwell sole grantor |
| Section 1512 negotiations | Full email chain Sept-Nov 2020 | **Confirmed** -- preliminary statement of facts discussed |
| Boeing 727 N908JE flight manifest | JEGE Inc. records | **Confirmed** -- PBI to JFK, 1/12/2004 |
| "Hundreds-perhaps thousands" of photographs | Government detention memo | **Confirmed** -- "sexually suggestive photographs" + CDs labeled "Girl pics nude" |
| BOP suicide watch removal email | [EFTA00032148](https://www.justice.gov/epstein/files/DataSet%208/EFTA00032148.pdf) | **Confirmed** -- sent to 71 staff, July 30, 2019 |
| Maxwell alias report with 19 name variations | 43-page professional background investigation | **Confirmed** -- includes "BORGERSON, GHISLAINE" |
| Criminal Record discrepancy | Firearms application vs. 2019 background check | **Confirmed** -- Criminal Record: YES on firearms app contradicts Criminal Record: No on 2019 check. **Unexplained.** |

The Criminal Record discrepancy is particularly significant: Maxwell declared a criminal record on her NYPD firearms application (which was approved), but a 2019 background check returned no criminal record. No explanation for this contradiction appears in any recovered document.

### 23.8 Borgerson Financial Surveillance ([EFTA00037958](https://www.justice.gov/epstein/files/DataSet%208/EFTA00037958.pdf))

FBI financial surveillance of **Scott Borgerson** (Maxwell's partner) via his **USAA checking account and credit card** transactions from **March through September 2019**:

- Transactions at **Common Man restaurants** (multiple locations)
- **Sunapee Lodge**
- **Petsmart**
- **Walmart Conway**
- **Conway Scenic Railroad**
- **Distance analysis** was performed between transaction locations and **Sutton, NH** -- the small town where Maxwell was ultimately found hiding

This financial surveillance demonstrates the FBI was building a geographic profile of Borgerson's movements months before Maxwell's arrest, using his spending patterns to narrow down her hiding location in rural New Hampshire. The presence of Petsmart transactions is consistent with reports that Maxwell had a dog at the Sutton property.

### 23.9 USVI Attorney General Lawsuit Evidence ([EFTA00016836](https://www.justice.gov/epstein/files/DataSet%208/EFTA00016836.pdf))

A New York Times article preserved in the case files documenting USVI Attorney General **Denise George's** lawsuit against the Epstein estate. Key allegations from the lawsuit:

- Epstein maintained a **computerized database** tracking the **"availability and movements of women and girls"**
- Used **fraudulent modeling visas** to transport victims to the US Virgin Islands
- Air traffic controllers observed Epstein with girls **"as young as 11"** departing his private plane **in 2018** -- one year before his arrest
- A **15-year-old girl attempted to swim off the island to escape** after being forced to engage in sex acts
- A girl was **held captive after her passport was confiscated**

The air traffic controller observation is significant because it places Epstein engaging in conduct with minors in 2018, contradicting any narrative that his criminal activity ceased after the 2008 NPA. The computerized database for tracking victims represents a level of organizational sophistication consistent with a systematic trafficking operation rather than opportunistic abuse.

### 23.10 Victoria's Secret / Wexner Connection ([EFTA00014526](https://www.justice.gov/epstein/files/DataSet%208/EFTA00014526.pdf))

**Ed Razek**, the L Brands executive who helped select Victoria's Secret models, visited Epstein's Manhattan mansion accompanied by another man. Upon arrival, they were **"welcomed by young women."**

This supplements the existing record on the Victoria's Secret pipeline (Section 19). Additionally, [EFTA00026723](https://www.justice.gov/epstein/files/DataSet%208/EFTA00026723.pdf) references a **"$46 million charitable donation to keep alive his ties"** in the context of Wexner -- suggesting a substantial ongoing financial relationship between Epstein entities and Wexner that extended well beyond any legitimate business arrangement.

### 23.11 DS8 Document Classification Summary

A comprehensive content survey of all **10,594 PDFs** in Dataset 8 yielded the following classification:

| Category | Count |
|----------|-------|
| Emails/correspondence | 6,092 |
| BOP/MCC records | 821 |
| Court filings/transcripts | 709 |
| FBI documents | 408 |
| Financial/tax records | 80 |
| FAA/aviation records | 74 |
| Travel/customs records | 34 |
| Placeholders (no content) | 438 |
| Other/uncategorized | 1,923 |
| **Total** | **10,594** |

**Year distribution peaks:** 2019 (8,066 mentions), 2020 (5,381), 2021 (3,934). The heavy concentration in 2019 reflects the arrest, detention, death, and immediate aftermath. The 2020 peak corresponds to the Maxwell arrest and prosecution. The 2021 peak covers the trial preparation and international cooperation efforts (MLAT, Prince Andrew negotiations).

### 23.12 Reports Generated This Session

| File | Subject |
|------|---------|
| [DS8_VERIFICATION.md](/raw-dataset-analysis/DS8_VERIFICATION.md) | 10-item verification of key claims with rendered PDF confirmation |
| [DS8_NEW_LEADS.md](/raw-dataset-analysis/DS8_NEW_LEADS.md) | New names and leads identified from DS8 deep extraction |
| [DS8_CONTENT_SURVEY.md](/raw-dataset-analysis/DS8_CONTENT_SURVEY.md) | Comprehensive DS8 document catalog and classification |
| [DS8_MEDIA_CATALOG.md](/raw-dataset-analysis/DS8_MEDIA_CATALOG.md) | Updated with MCC surveillance footage analysis and camera position identification |

---

## 24. APPENDIX: COMPLETE REPORT INDEX

### Investigation Reports

| # | File | Size | Subject |
|---|------|------|---------|
| 1 | [INVESTIGATION_1_BARR_NTOC.md](/individuals/INVESTIGATION_1_BARR_NTOC.md) | 25K | William Barr NTOC filing and recusal failure |
| 2 | [INVESTIGATION_2_DB_KYC_BREACH.md](/financial/INVESTIGATION_2_DB_KYC_BREACH.md) | 31K | Deutsche Bank KYC breach timeline |
| 3 | [INVESTIGATION_3_HAZE_TRUST_AML.md](/financial/INVESTIGATION_3_HAZE_TRUST_AML.md) | 31K | Haze Trust AML inquiry |
| 4 | [INVESTIGATION_4_2018_WIRE_RECIPIENTS.md](/financial/INVESTIGATION_4_2018_WIRE_RECIPIENTS.md) | 27K | November/December 2018 obstruction wires |
| 5 | [INVESTIGATION_5_MAXWELL_SSN.md](/individuals/INVESTIGATION_5_MAXWELL_SSN.md) | 24K | Maxwell identity anomalies |
| 6 | [INVESTIGATION_6_LEON_BLACK.md](/individuals/INVESTIGATION_6_LEON_BLACK.md) | 33K | Leon Black FBI investigation |
| 7 | [INVESTIGATION_7_BARRETT_REPORTS.md](/financial/INVESTIGATION_7_BARRETT_REPORTS.md) | 34K | Paul Barrett weekly reporting |
| 8 | [INVESTIGATION_8_UNEXPLORED_NAMES.md](/individuals/INVESTIGATION_8_UNEXPLORED_NAMES.md) | 44K | Unexplored names and disappeared witnesses |

### Forensic Accounting Reports

| # | File | Size | Subject |
|---|------|------|---------|
| 1 | [FORENSIC_ACCT_1_HAZE_DRAWDOWN.md](/financial/FORENSIC_ACCT_1_HAZE_DRAWDOWN.md) | 33K | $46.96M Haze Trust drawdown trace |
| 2 | [FORENSIC_ACCT_2_MONEY_SOURCES.md](/financial/FORENSIC_ACCT_2_MONEY_SOURCES.md) | 28K | Money sources into Epstein accounts |
| 3 | [FORENSIC_ACCT_3_INTER_ENTITY_FLOWS.md](/financial/FORENSIC_ACCT_3_INTER_ENTITY_FLOWS.md) | 32K | Inter-entity fund flow mapping |
| 4 | [FORENSIC_ACCT_4_JABWCPA_INSTITUTION1.md](/financial/FORENSIC_ACCT_4_JABWCPA_INSTITUTION1.md) | — | JABWCPA and Institution-1 identification |
| 5 | [FORENSIC_ACCT_5_CALENDAR_CORRELATION.md](/financial/FORENSIC_ACCT_5_CALENDAR_CORRELATION.md) | 38K | Calendar-to-transaction correlation |
| 6 | [FORENSIC_ACCT_6_POST_DEATH_ASSETS.md](/financial/FORENSIC_ACCT_6_POST_DEATH_ASSETS.md) | 32K | Post-death estate disposition |

### Prior Analysis Reports

| File | Size | Subject |
|------|------|---------|
| [DS10_FORENSIC_ANALYSIS.md](/raw-dataset-analysis/DS10_FORENSIC_ANALYSIS.md) | 37K | Original DS10 deep forensic analysis |
| [DS10_COMPLETE_FINDINGS.md](/raw-dataset-analysis/DS10_COMPLETE_FINDINGS.md) | — | Complete DS10 findings |
| [DS10_ENTITY_EXTRACTION_REPORT.md](/raw-dataset-analysis/DS10_ENTITY_EXTRACTION_REPORT.md) | 141K | Entity extraction results |
| [DS10_RECONSTRUCTED_PAGES.md](/raw-dataset-analysis/DS10_RECONSTRUCTED_PAGES.md) | 214K | Full page reconstructions |
| [DS10_KEY_DOCUMENTS_DEEP_DIVE.md](/raw-dataset-analysis/DS10_KEY_DOCUMENTS_DEEP_DIVE.md) | 76K | Key document deep dives |
| [DS10_COMPREHENSIVE_NAME_SEARCH.md](/raw-dataset-analysis/DS10_COMPREHENSIVE_NAME_SEARCH.md) | 30K | Name search results |
| [HIDDEN_TEXT_COMPLETE_REVIEW.md](/methodology/HIDDEN_TEXT_COMPLETE_REVIEW.md) | — | Complete hidden text review |

### Gap Analysis Reports

| File | Size | Subject |
|------|------|---------|
| [DS8_MEDIA_CATALOG.md](/raw-dataset-analysis/DS8_MEDIA_CATALOG.md) | 8K | Dataset 8: 419 surveillance videos (412.5 hrs), 62+ seized devices, 4 block-redacted CSVs |
| [LUXURY_PURCHASES_ANALYSIS.md](/financial/LUXURY_PURCHASES_ANALYSIS.md) | 15K | Art (Rothko, Sotheby's, Christie's), blue diamonds, yachts, Hermes, $158M Leon Black |

### Deep Investigation Reports (February 6, 2026)

| File | Subject |
|------|---------|
| [DS8_VERIFICATION.md](/raw-dataset-analysis/DS8_VERIFICATION.md) | 10-item verification of key claims with rendered PDF confirmation |
| [DS8_NEW_LEADS.md](/raw-dataset-analysis/DS8_NEW_LEADS.md) | New names and leads identified from DS8 deep extraction |
| [DS8_CONTENT_SURVEY.md](/raw-dataset-analysis/DS8_CONTENT_SURVEY.md) | Comprehensive DS8 document catalog and classification (10,594 PDFs) |
| [DS8_MEDIA_CATALOG.md](/raw-dataset-analysis/DS8_MEDIA_CATALOG.md) | Updated: MCC surveillance footage analysis with camera position IDs |

### DS9 Scan Results

Dataset 9 was scanned for annotation-style redactions: **0 found** (text properly removed, not overlaid). However, DS9 is the largest dataset with **531,284 documents** containing full text. The "109 PDFs/0 redactions" description referred only to annotation-style overlays. DS9 contains the complete email corpus, calendars, trust instruments, corporate documents, and FBI investigative records. Key DS9 content includes:
- **[EFTA00039025](https://www.justice.gov/epstein/files/DataSet%209/EFTA00039025.pdf)** (128 pages): Complete OIG Report 23-085 (June 2023) — MCC death investigation
- MCC SHU check sheets from night of death (08/10/2019)
- BOP count sheets and inmate rosters
- **[EFTA00091248](https://www.justice.gov/epstein/files/DataSet%209/EFTA00091248.pdf)**: Maxwell trial witness list cover sheet (names withheld under protective order)

### Databases

| File | Size | Contents |
|------|------|----------|
| primary document text database | 627MB | 1,808,915 redactions, 107,422 entities, 39,588 pages |
| entity relationship database | — | 524 entities, 2,096 relationships |
| evidence_db/structured evidence database | — | 487 persons, 19 organizations |

---

*This report was generated through forensic analysis of publicly released DOJ documents. All findings are derived from text extracted from PDF text layers (OCR), supplemented by direct PDF rendering and verification of key documents. Only 12 specific PLIST documents had genuinely failed redaction overlays; the remainder of the corpus represents OCR-extracted text from scanned document pages. No classified or non-public documents were accessed. The source material is available at the DOJ's public release portal.*

*Total analysis: 1,808,942 redactions across 519,438 PDFs from 12 datasets (~218GB). 28 detailed sub-reports totaling approximately 800KB of documented findings. Last updated: February 6, 2026 (Section 23: Deep Document Investigation added).*

---

## REVISIT CORRECTIONS LOG (February 12, 2026)

The following corrections were integrated from a revisit cross-referencing 78 prior report revisits against the full_text_corpus.db (1,380,937 docs, all 12 datasets):

1. **Section 5.2 (Prytanee LLC):** KYC principal identified as Etienne Pierre Jean Binant (French citizen), not Jack Lang. Caroline Lang was only the social introducer. (Report #11 revisit)
2. **Sections 6.4/7.3 (Paul Barrett):** Barrett left Deutsche Bank by mid-2017 and founded Alpha Group Capital LLC with Epstein funding ($250K/yr + forgivable loans). He was a beneficiary of Epstein's will -- an economic partner, not merely a banker. (Report #15 revisit)
3. **Section 20 (Intelligence claims):** FBI CHS FD-1023 ([EFTA00090314](https://www.justice.gov/epstein/files/DataSet%209/EFTA00090314.pdf)) contains an unverified CHS claim that Epstein "belonged to both U.S. and allied intelligence services." The document exists in the FBI case file though the claim is unverified. (Report #52 revisit)
4. **Section 22.7 (Bitcoin/crypto):** Carbyne/Reporty investment documented: 50 Carbyne + 324 Reporty docs in DS9. Epstein invested $500K, Barak had $1.5M carry, $50M valuation. (Report #52 revisit)
5. **Section 22.14b (DS9 scope):** DS9 contains 531,284 documents with full text. The "109 PDFs/0 redactions" described only annotation-style redactions. DS9 is the largest dataset. (Report #48 revisit)
6. **Section 8.2 (Cuomo):** "Cuomo" on the Prominent Names page is a victim surname, not Governor Andrew Cuomo. [EFTA02696360](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02696360.pdf) confirms "Tony Cuomo" invited to Epstein's house (Jan 2012). (Session 8 finding)
7. **Section 22.1 (Lutnick):** DS9 reveals 20+ documents showing active social relationship (2011-2013) including Lutnick family visit to Little St. James Island (Dec 2012). (Report #21 revisit)
8. **Section 21 (Barrett non-investigation):** Corrected to reflect Barrett's departure from DB mid-2017 and status as economic partner. (Report #15 revisit)
9. **Section 22.16 footnote:** Coatue Enterprises LLC ($2M) was Richard Kahn's personal shell company per GVI complaint [EFTA00161836](https://www.justice.gov/epstein/files/DataSet%209/EFTA00161836.pdf), not Philippe Laffont's tech hedge fund. (Report #9 revisit)
