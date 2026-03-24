# Epstein Phone Records: The Unredacted Window

## Summary

The EFTA corpus contains **970 phone record documents spanning 27,690 pages** — call detail records, cell tower data, subscriber information, and phone bills from multiple carriers. Roughly 43% of these documents were redacted. But a production inconsistency between Dataset 9 and Dataset 10 left **46 AT&T cell phone bills completely unredacted** in DS9, while the same records in DS10 were redacted. This gap exposes **25 months of Epstein's itemized call records** (May 2004 through July 2006), covering the entire Palm Beach police investigation, FBI involvement, and non-prosecution agreement negotiation period.

From these unredacted bills, we extracted **1,179 unique phone numbers** and **8,173 total call records**. We identified approximately 20 numbers by cross-referencing the corpus — emails, FBI 302s, subpoenas, and business records — without needing any external lookup service.

A separate 2,153-page document ([EFTA01242527](https://www.justice.gov/epstein/files/DataSet%209/EFTA01242527.pdf)) contains Epstein's **office landline records** (212-750-1176), also in DS9, also with **zero redactions**. This document contains calls to the Trump Organization and the Clinton Foundation — 5 calls to Trump Org and 10 calls to the Clinton Foundation across three different Epstein phone lines.

The full extracted phone number dataset (1,117 numbers with call counts and geographic data) is available as a [CSV in our data repository](https://github.com/rhowardstone/Epstein-research-data/blob/main/phone_numbers_enriched.csv).

---

## Methodology

### Inventory

We performed a full-text search of the 2.77 million pages in [`full_text_corpus.db`](https://github.com/rhowardstone/Epstein-research-data/releases) for phone-record indicators: carrier names (AT&T, Cingular, Sprint, T-Mobile, Verizon), document types (subpoena, cell site, subscriber), and billing terminology. Each document was classified into 25 categories (AT&T bills, cell site records, call detail records, subscriber information, etc.) and stored in a structured inventory.

### Redaction Cross-Reference

Every phone record EFTA was cross-referenced against our [`redaction_analysis_v2.db`](https://github.com/rhowardstone/Epstein-research-data/releases) database (2.59 million detected redactions). For each document, we counted proper redactions (black bars), text-near-bar OCR leaks, and white rectangles. The result is a per-document redaction profile showing which phone records were protected and which were exposed.

### Phone Number Extraction and Enrichment

Phone numbers were extracted via regex from the unredacted DS9 bills (AT&T account 0043811863). Each number was validated and enriched using Python's `phonenumbers` library — an offline database that provides geographic location, carrier, line type, and timezone without any rate limits or API calls. The enriched dataset contains 1,117 valid numbers after filtering toll-free, directory assistance, and OCR-error entries.

### Number Identification

We identified phone numbers by searching the full corpus for each number, then reading the surrounding context. An email that says "call me at 212-772-9416" identifies the sender. An FBI internal email titled "Maxwell's cell number" that links 917-520-3106 to the Terramar Project identifies the subscriber. A car service booking that says "Jeffrey Epstein in: (917) 868-6145" identifies the passenger. No external reverse-lookup services were used for any identifications in this report — every attribution comes from documents in the EFTA corpus.

---

## The DS9 / DS10 Redaction Inconsistency

Epstein's AT&T Wireless phone bills (account **0043811863**) were produced in both Dataset 9 and Dataset 10. The redaction treatment was not consistent:

| Dataset | Documents | Redacted | Unredacted |
|---------|-----------|----------|------------|
| DS8 | 2 | 1 | 1 |
| **DS9** | **46** | **0** | **46** |
| **DS10** | **83** | **78** | **5** |
| DS99 | 1 | 0 | 1 |

All 46 DS9 copies have zero redactions. 78 of 83 DS10 copies were redacted. These are the same underlying phone records — the same AT&T account, the same billing periods, the same call data — processed through two different production pipelines with different redaction decisions.

The unredacted DS9 bills cover **May 2004 through July 2006**: 25 unique billing months, 925 pages of itemized call records. Each page lists every call with date, time, number dialed, location, duration, and rate.

This window covers the entire arc of the Palm Beach investigation (launched March 2005), FBI involvement (mid-2006), and the non-prosecution agreement negotiation period.

### What Was Redacted (and Why It Matters)

Cell site location information (CSLI) — tower data showing Epstein's physical location — was the most aggressively redacted category, averaging **756 redactions per document**. The single most-redacted document is [EFTA01310387](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01310387.pdf) (DS10, 129 pages): AT&T subscriber information for Jeffrey Epstein, with 8,050 redactions across 128 pages.

Two FBI documents — [EFTA01073204](https://www.justice.gov/epstein/files/DataSet%209/EFTA01073204.pdf) and [EFTA01182476](https://www.justice.gov/epstein/files/DataSet%209/EFTA01182476.pdf) — are "FOI/PA Deleted Page Information Sheets" documenting **853 pages** of phone records the FBI explicitly removed under exemptions b6, b7C, and b7D.

Even the redacted documents leak data. Our OCR analysis detected **10,182 text-near-bar instances** where text bleeds past redaction bars. [EFTA01334722](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01334722.pdf) leaks call locations: fragments like "PALMBEACH FL", "EW YORK NY", "OSTON MA", "AMBRKNE MA" (Cambridge), "NOLULU HI" (Honolulu), "otile FRA" (France), and "ROOKLYN NY" are visible beside the redaction bars.

---

## Epstein's Phone Lines

The corpus reveals at least seven phone numbers associated with Epstein:

| Number | Type | Source |
|--------|------|--------|
| **(917) 855-3363** | Primary cell (AT&T acct 0043811863) | Header on every cell bill. Now registered to **Sarah Kellen** per current reverse lookup. |
| **(917) 868-6145** | Cell — same account | [EFTA02043883](https://epstein-data.com/full_text_corpus/pages?efta_number=EFTA02043883) (DS10): car service booking — "Jeffrey Epstein in: (917) 868-6145" |
| **(917) 913-6283** | Cell — same account | Separate "VOICE USAGE" section in bills |
| **(561) 655-7626** | Palm Beach | [EFTA01928016](https://epstein-data.com/full_text_corpus/pages?efta_number=EFTA01928016) (DS10): email from "Jeffrey E." to Greg Wyler — "561 655 7626" as callback |
| **(212) 750-9895** | Office — 457 Madison Ave FL 4 | [EFTA01582864](https://epstein-data.com/full_text_corpus/pages?efta_number=EFTA01582864) (DS10): Dun & Bradstreet record for "Intercontinental Asset Group" |
| **(212) 750-1176** | Office landline | [EFTA01242527](https://www.justice.gov/epstein/files/DataSet%209/EFTA01242527.pdf) (DS9) p0: "LOCAL USAGE REPORT, Phone #: 2127501176" |
| **(212) 772-9416** | Line in Epstein phone records | [EFTA01242527](https://www.justice.gov/epstein/files/DataSet%209/EFTA01242527.pdf) (DS9): billing records in same document. Also associated with **David Stern** — see [EFTA01928007](https://epstein-data.com/full_text_corpus/pages?efta_number=EFTA01928007) |
| **(212) 535-6833** | Line in Epstein phone records | [EFTA01242527](https://www.justice.gov/epstein/files/DataSet%209/EFTA01242527.pdf) (DS9): billing records in same document. Also identified as **Maxwell's office** — see [EFTA02088364](https://epstein-data.com/full_text_corpus/pages?efta_number=EFTA02088364) |
| **(212) 879-9366** | Another line | [EFTA01242527](https://www.justice.gov/epstein/files/DataSet%209/EFTA01242527.pdf) (DS9) p1588: "Telephone # 2128799366" |

The primary cell number (917-855-3363) appearing under Sarah Kellen's name today is notable. Kellen was Epstein's scheduler and assistant during the period covered by these bills. Whether the number was originally Epstein's and transferred to Kellen, or was always assigned to her and used as "Epstein's line" for call-routing purposes, is unclear from the records alone.

---

## The Inner Circle: Identified Numbers

These identifications come entirely from cross-referencing phone numbers against documents within the EFTA corpus — emails, FBI 302s, subpoenas, car service bookings, and business filings.

### Ghislaine Maxwell — Two Numbers

| Number | Type | Evidence |
|--------|------|----------|
| **(917) 520-3106** | Cell | [EFTA00097135](https://epstein-data.com/full_text_corpus/pages?efta_number=EFTA00097135) (DS9): FBI internal email titled "Maxwell's cell number" — T-Mobile subscriber = **Terramar Project, Inc** (owned by Maxwell), UPS store at 139A Charles St, Boston. Saved as **"Ghislaine"** in Epstein's seized phone. Also: [EFTA00079292](https://epstein-data.com/full_text_corpus/pages?efta_number=EFTA00079292) (DS9) p2: grand jury subpoena rider listing Maxwell identifiers — phone (917) 520-3106, email GMAX1@ELLMAX.COM |
| **(212) 535-6833** | Office | [EFTA02088364](https://epstein-data.com/full_text_corpus/pages?efta_number=EFTA02088364) (DS10): email asking for "Ghislaine's number" — reply: "(212) 535-6833 office... Dana is her assistant" |

Maxwell's cell (216 calls in the dataset) and office line appear throughout the call logs. On several dates, Epstein's office called both numbers on the same day.

### Staff and Associates

| Number | Calls | Identity | Evidence |
|--------|-------|----------|----------|
| **(646) 286-7000** | 39 | **Lesley Groff** (executive assistant) | [EFTA02715374](https://epstein-data.com/full_text_corpus/pages?efta_number=EFTA02715374) (DS11) |
| **(718) 707-9090** | 96 | **Citicar** (car service) | [EFTA01898783](https://epstein-data.com/full_text_corpus/pages?efta_number=EFTA01898783) (DS10): "Thank you for choosing CITICAR for your travel needs" |
| **(340) 775-8100** | 29 | **LSJE, LLC** (Little St. James entity) | [EFTA00003047](https://www.justice.gov/epstein/files/DataSet%201/EFTA00003047.pdf) (DS1): employee records, 6100 Red Hook Quarters Suite B-3 |
| **(561) 662-3098** | 29 | **Sunshine Services Unlimited** | [EFTA00203748](https://epstein-data.com/full_text_corpus/pages?efta_number=EFTA00203748) (DS9): account name on bills |
| **(212) 772-9416** | 57 | **David Stern** / **Boris Nikolic** | [EFTA01928007](https://epstein-data.com/full_text_corpus/pages?efta_number=EFTA01928007) (DS10): email from "Jeffrey E." — "new york 212 772 9416 now" |
| **(917) 975-4500** | 80 | **"Jojo"** | [EFTA02592280](https://epstein-data.com/full_text_corpus/pages?efta_number=EFTA02592280) (DS11): number listed as "1-917-975-4500 Jojo" in email thread between "Jeffrey E." and Alice de Rothschild |
| **(212) 288-4844** | — | **Darren Indyke** (attorney/trustee) | [EFTA01616338](https://epstein-data.com/full_text_corpus/pages?efta_number=EFTA01616338) (DS10): Indyke address "6030 Le Lac Road, Boca Raton" |
| **(212) 772-9222** | — | **Dr. Kruger** | [EFTA02693795](https://epstein-data.com/full_text_corpus/pages?efta_number=EFTA02693795) (DS11): "Spoke to Dr. Kruger. He says it takes a full 5 business days for results to come back" |
| **(917) 476-9463** | 136 | **Nadia Marcinko** (pilot, NPA immunity recipient) | [Buzzfile business listing](http://www.buzzfile.com/business/Aviloop-LLC-917-476-9463) for Aviloop LLC at this number. Corpus: text messages between Epstein's cell and this number (EFTA01305875, DS10, p13); JPMorgan wire transfers to Aviloop LLC ([EFTA01589586](https://epstein-data.com/full_text_corpus/pages?efta_number=EFTA01589586), DS10); emails between Epstein and Marcinko discussing Aviloop ([EFTA02032839](https://epstein-data.com/full_text_corpus/pages?efta_number=EFTA02032839), [EFTA01753491](https://epstein-data.com/full_text_corpus/pages?efta_number=EFTA01753491), DS10). Aviloop LLC is Subject 1 of 25 in a gutted FinCEN SAR ([EFTA01656524](https://epstein-data.com/full_text_corpus/pages?efta_number=EFTA01656524), DS10). Registered at 301 E. 66th St. |

### Investigation-Related Numbers

| Number | Calls | Identity | Evidence |
|--------|-------|----------|----------|
| **(917) 204-9696** | 35 | **"Natalie or Anja"** — person of investigative interest | [EFTA00189310](https://epstein-data.com/full_text_corpus/pages?efta_number=EFTA00189310) (DS9) pp32-33: AUSA Villafana's email to Agent Kuyrkendall listing investigative phone numbers — "Natalie or Anja 917-204-9696." This is NOT Villafana's own number (her number was 561-209-1047 per her email signature). |
| **(561) 317-5844** | 38 | Investigation target (subpoenaed) | [EFTA00260322](https://epstein-data.com/full_text_corpus/pages?efta_number=EFTA00260322) (DS9) pp4-14: Palm Beach PD Det. Joe Recarey's sworn subpoena to T-Mobile — "Pursuant to a lawful criminal investigation involving sex with certain minors" (PBPD Case 05-368, January 24, 2006) |

### Partially Identified

| Number | Calls | Identity | Evidence |
|--------|-------|----------|----------|
| **(212) 902-8707** | — | **Goldman Sachs** (exchange confirmed) | Goldman Sachs main switchboard is 212-902-1000 ([GetHuman](https://gethuman.com/phone-number/Goldman-Sachs)); 212-902-8707 is in the same exchange. Called from Epstein's office on Oct 2, 2003 at 4:36 PM — one minute after the Clinton Foundation call at 4:35 PM. No corpus context outside the office bills. |

### Unidentified High-Frequency Numbers

These numbers rank among the most-called in the dataset but have no identifying context in the corpus and zero web presence. They remain unidentified.

| Number | Calls | Location | Notes |
|--------|-------|----------|-------|
| (917) 957-5341 | 335 | New York | Called at 1:30 AM alongside Nadia and Maxwell (EFTA01263776). Called internationally while Epstein was abroad (EFTA01312410). Called 4 times in 32 minutes on Aug 9, 2004. Inner circle — likely a prepaid/personal phone. |
| (646) 232-3311 | 233 | New York | Same late-night calling clusters as 957-5341. Zero web footprint. |
| (786) 246-6607 | 128 | Miami | Called both TO and FROM Epstein's lines (CDR shows incoming calls). FBI subpoena context but no name. |
| (740) 802-4061 | 111 | Marion, OH | Cell tower data shows "MARION OH" — **not** New Albany. Called both TO and FROM Epstein lines. Marion is ~50 miles north of Columbus. |
| (614) 284-1783 | 103 | Columbus, OH | Wireless (New Cingular/AT&T). Columbus is Wexner territory (L Brands HQ). |
| (808) 754-0079 | 74 | Hawaii | Zero web footprint. |
| (310) 210-9944 | 61 | Los Angeles | Zero web footprint. |

The (614) Columbus number is in Wexner's territory; a confirmed New Albany, OH number — (614) 939-6005 — was identified via a DS10 call record showing "(614)939-6005 NEW ALBANY OH" ([EFTA01310123](https://epstein-data.com/full_text_corpus/pages?efta_number=EFTA01310123), DS10, p4). The (740) Marion number is in rural central Ohio and may not be Wexner-related. Both Ohio numbers and the Miami number initiated calls TO Epstein's lines, confirming two-way contact.

---

## Geographic Calling Patterns

The `phonenumbers` library (offline, no rate limits) provided geographic data for all 1,117 valid numbers:

| Region | Area Codes | Call Records | Significance |
|--------|-----------|-------------|--------------|
| **New York City** | 917, 212, 646, 718 | 5,225 | Dominant — 64% of all calls |
| **Palm Beach / S. Florida** | 561 | 732 | Epstein's PB residence |
| **Ohio** | 740, 614, 440 | 362 | Wexner territory (New Albany, Columbus) |
| **U.S. Virgin Islands** | 340 | 164 | Little St. James |
| **Miami** | 786, 305 | 141 | South Florida network |
| **Hawaii** | 808 | 79 | Unknown connection |
| **Massachusetts** | 781, 617 | 61 | Academic connections (Cambridge) |
| **Minneapolis** | 763 | 29 | Unknown connection |
| **California** | 310 | 61 | LA / entertainment |

The Ohio cluster is notable. Three of the top 15 unidentified numbers are Ohio area codes, and we have a confirmed New Albany, OH number — suggesting ongoing, frequent contact with the Wexner orbit throughout 2004-2006.

---

## Office Landline Records: Trump and Clinton

[EFTA01242527](https://www.justice.gov/epstein/files/DataSet%209/EFTA01242527.pdf) is a **2,153-page document** in Dataset 9 containing local usage reports for **multiple phone lines** associated with Epstein. It has **zero redactions** and spans 2003 through 2006. The lines covered include:

- **212-750-1176** — Epstein's primary office landline
- **212-750-9895** — Second office line (Intercontinental Asset Group, 457 Madison Ave)
- **212-772-9416** — A line also associated with David Stern (see above)
- **212-535-6833** — A line also identified as Maxwell's office (see above)
- **212-879-9366** — Another line (Verizon Enterprise Solutions)

The fact that billing records for lines attributed to both David Stern and Ghislaine Maxwell appear in the same consolidated phone record suggests these lines were under Epstein's account or oversight.

### Calls to the Trump Organization

The Trump Organization's main number — **(212) 832-2000** — was confirmed via a press release in the corpus: [EFTA00812159](https://epstein-data.com/full_text_corpus/pages?efta_number=EFTA00812159) (DS9) reads "For more information contact Donald J. Trump (212) 832-2000."

Five calls to Trump Org appear in EFTA01242527, from multiple Epstein lines:

| Date | Time | Epstein Line | Source Page |
|------|------|--------------|-------------|
| January 22, 2003 | 9:32 AM | 212-750-9895 | p316 |
| November 17, 2003 | 12:01 PM | 212-750-9895 | p327 |
| February 2, 2005 | 6:31 PM | 212-772-9416 | p431 |
| February 3, 2005 | 10:57 AM | 212-750-1176 | p219 |
| November 27, 2006 | 11:19 AM | 212-750-1176 | p306 |

The Feb 3, 2005 call lasted 9 minutes — the longest Trump Org call in these records. The others registered zero connected minutes.

A sixth line — 212-879-9366 — shows a call to **Mar-a-Lago** ((561) 832-2600) on February 3, 2005 at 2:00 PM (p1588). The phone record labels the destination as "WpalmbeachFL 561 832-2600"; the Mar-a-Lago attribution comes from external directory verification.

**Important caveat**: A call to an organization's main number does not establish contact with any particular individual. Epstein's office calling (212) 832-2000 could have reached a receptionist, a legal department, an accounting office, or any other extension. The same applies to all organization numbers discussed in this report.

Trump Org does NOT appear in the unredacted cell phone bills (account 0043811863). The Epstein–Trump Org phone contact, at least from these records, was office-to-office.

### Calls to the Clinton Foundation

The Clinton Foundation's publicly listed number — **(212) 348-8882** — appears **10 times** across **three different Epstein phone lines** in EFTA01242527, spanning July 2003 through August 2005:

| # | Date | Time | Epstein Line | Page |
|---|------|------|--------------|------|
| 1 | July 30, 2003 | 9:43 AM | 212-535-6833 | p612 |
| 2 | October 2, 2003 | 4:35 PM | 212-750-1176 | p82 |
| 3 | October 10, 2003 | 10:14 AM | 212-535-6833 | p624 |
| 4 | December 11, 2003 | 2:59 PM | 212-535-6833 | p640 |
| 5 | December 15, 2003 | 3:19 PM | 212-535-6833 | p641 |
| 6 | April 6, 2004 | 3:23 PM | 212-750-1176 | p136 |
| 7 | October 18, 2004 | 3:50 PM | 212-750-9895 | p340 |
| 8 | October 29, 2004 | 3:39 PM | 212-750-1176 | p195 |
| 9 | July 28, 2005 | 4:55 PM | 212-750-1176 | p267 |
| 10 | August 2, 2005 | 3:48 PM | 212-750-1176 | p268 |

Three Epstein lines are represented: the primary office line (212-750-1176, 5 calls), the second office line (212-750-9895, 1 call), and 212-535-6833 (4 calls). The third line — 212-535-6833 — is also the number identified as **Maxwell's office** elsewhere in the corpus (see above). Its billing records appear in the same consolidated phone document, suggesting it was under Epstein's account. Whether calls from this line were placed by Epstein, Maxwell, or staff is unknown.

Nine of the ten calls were placed in the afternoon (2:59 PM – 4:55 PM); only the July 30, 2003 call was a morning call (9:43 AM), and it was the only one with a measured connected duration (2 minutes).

This number was verified as the Clinton Foundation via [their public contact page](https://www.clintonfoundation.org/contact/), [Dun & Bradstreet](https://www.dnb.com/business-directory/company-profiles.bill_hillary__chelsea_clinton_foundation.b3b561c0b41ec9d90c6e75bd0146320e.html), and [ZoomInfo](https://www.zoominfo.com/c/clinton-foundation/38589798).

The same caveats apply: a call to the Foundation's main number doesn't identify who answered. And note that most of these calls registered zero minutes of connected time ($0.075 charge) — these may be unanswered calls, calls to voicemail, or calls too short to register on the billing system.

Two calls to (212) 348-6751 (October 31 and November 11, 2003) and one to (212) 348-2489 (November 19, 2003) share the Harlem 348 exchange with the Clinton Foundation but are **unverified** — they could be any businesses or residences in that exchange area.

---

## February 2–3, 2005: Trump, Wexner, Mar-a-Lago

February 2, 2005 produced **56 calls** from Epstein's office — the busiest day in the landline dataset. The concentration of identifiable numbers is striking:

| Time | Number | Identity |
|------|--------|----------|
| 8:21 AM | (917) 855-3363 | Kellen/cell |
| 9:58 AM | (917) 204-9696 | "Natalie or Anja" (investigative interest) |
| 10:13 AM | (917) 204-9696 | Same — 2nd call |
| 10:54 AM | (917) 204-9696 | Same — 3rd call |
| 11:33 AM | (917) 204-9696 | Same — 4th call |
| 4:49 PM | (614) 939-6005 | **New Albany, OH (Wexner orbit)** — from line 212-879-9366 |
| 4:50 PM | (212) 772-9416 | **David Stern** |
| 4:51 PM | (646) 286-7000 | **Lesley Groff** |
| **6:31 PM** | **(212) 832-2000** | **Trump Organization** |
| 8:18 PM | (212) 879-9366 | Epstein's second line |
| 9:39 PM | (917) 204-9696 | "Natalie or Anja" — 5th call |
| 9:47 PM | (917) 855-3363 | Kellen/cell (last call) |

Five calls to a number identified in AUSA Villafana's investigative phone list as belonging to "Natalie or Anja" — a person of interest in the Epstein investigation. Four calls clustered in the morning, then a final call at 9:39 PM. The same day included calls to New Albany, OH (Wexner territory), David Stern, Lesley Groff, and the Trump Organization.

The following day — February 3, 2005 — the pattern continued:

| Time | Number | Identity |
|------|--------|----------|
| 10:57 AM | (212) 832-2000 | **Trump Organization** |
| 11:37 AM | (212) 772-9416 | **David Stern** |
| 1:22 PM | (917) 520-3106 | **Maxwell** |
| 1:54 PM | (917) 520-3106 | Maxwell (2nd call) |
| 2:00 PM | (561) 832-2600 | **Mar-a-Lago** — from line 212-879-9366 |

Mar-a-Lago's number (561-832-2600) was confirmed via [Yelp](https://www.yelp.com/biz/the-mar-a-lago-club-palm-beach), [Dun & Bradstreet](https://www.dnb.com/business-directory/company-profiles.mar-a-lago_club_llc.971ef0c60d76ac152011a1071cd973d9.html), and [CallerCenter](https://www.callercenter.com/561-832-2600.html). The phone record itself labels the destination only as "WpalmbeachFL" — the Mar-a-Lago attribution comes from external verification of the number.

This was February 2005 — one month before the Palm Beach Police Department officially opened its investigation into Epstein in March 2005. In a 48-hour window, Epstein's office contacted Trump Org twice, Mar-a-Lago once, a New Albany, OH number in Wexner's territory, Maxwell twice, and David Stern twice.

---

## November 27, 2006: During the NPA Negotiation

The last Trump Org call in the dataset falls on November 27, 2006 — during the non-prosecution agreement negotiation period:

| Time | Number | Identity |
|------|--------|----------|
| 10:25 AM | (212) 772-9222 | Dr. Kruger |
| 11:13 AM | (212) 249-1122 | Unidentified |
| **11:19 AM** | **(212) 832-2000** | **Trump Organization** |
| 11:36 AM | (212) 535-6833 | Maxwell (landline) |
| 12:59 PM | (917) 855-3363 | Kellen/cell |

Trump Org, then Maxwell 17 minutes later.

---

## What's Still Missing

### The 853 Deleted Pages

FBI documents [EFTA01073204](https://www.justice.gov/epstein/files/DataSet%209/EFTA01073204.pdf) and [EFTA01182476](https://www.justice.gov/epstein/files/DataSet%209/EFTA01182476.pdf) are Deleted Page Information Sheets documenting **853 pages** removed under FOIA exemptions b6, b7C, and b7D. These are phone records the FBI chose to withhold entirely, not just redact.

### The Redaction Leaks

Even where redactions were applied, our automated analysis found **10,182 instances** of text bleeding past redaction bars. These "text-near-bar" artifacts reveal partial phone numbers, call locations, FBI case routing information, and timestamps. A comprehensive extraction of these leaks may yield additional identifiable data.

### 1,117 Numbers, ~20 Identified

We identified approximately 20 numbers from corpus context. The remaining ~1,097 — including the #2 and #3 most-called numbers — remain unidentified. A CNAM (Caller Name) lookup service would cost roughly $12 for the full set and could identify many of these numbers, particularly landlines and business lines.

---

## Data

- **Phone number dataset**: [phone_numbers_enriched.csv](https://github.com/rhowardstone/Epstein-research-data/blob/main/phone_numbers_enriched.csv) — 1,117 unique numbers with call counts, geographic data, and carrier information
- **Redaction cross-reference**: [`phone_records_redaction_crossref.csv`](https://github.com/rhowardstone/epstein-research/blob/main/evidence/phone_records_redaction_crossref.csv) — 970 phone record documents with redaction counts
- **Full phone records inventory**: [`phone_records_inventory.json`](https://github.com/rhowardstone/epstein-research/blob/main/evidence/phone_records_inventory.json) — structured catalog of all 970 documents by category

**Disclaimer on phone number data:** All phone numbers in the CSV were extracted from publicly available federal documents on justice.gov (the DOJ's EFTA production). The geographic location, carrier, and line type columns were generated using Python's `phonenumbers` library, an open-source offline database based on public numbering plan (NANPA/ITU) assignments. This data reflects **current** numbering plan information — not necessarily the carriers or subscribers from 2004–2006 when these calls were placed. Phone numbers change hands. A number that was Epstein's in 2005 may belong to someone entirely unrelated today. Do not use this data to contact or harass anyone.

## Key Source Documents

| EFTA | Dataset | Description | Link |
|------|---------|-------------|------|
| EFTA01242527 | 9 | Office landline records (212-750-1176), 2,153 pages, zero redactions | [justice.gov](https://www.justice.gov/epstein/files/DataSet%209/EFTA01242527.pdf) / [OCR](https://epstein-data.com/full_text_corpus/pages?efta_number=EFTA01242527) |
| EFTA00201533 | 9 | Unredacted cell bill — December 2004 | [justice.gov](https://www.justice.gov/epstein/files/DataSet%209/EFTA00201533.pdf) / [OCR](https://epstein-data.com/full_text_corpus/pages?efta_number=EFTA00201533) |
| EFTA00097135 | 9 | FBI email: "Maxwell's cell number" — identifies (917) 520-3106 | [justice.gov](https://www.justice.gov/epstein/files/DataSet%209/EFTA00097135.pdf) / [OCR](https://epstein-data.com/full_text_corpus/pages?efta_number=EFTA00097135) |
| EFTA00079292 | 9 | Grand jury subpoena rider — Maxwell identifiers | [justice.gov](https://www.justice.gov/epstein/files/DataSet%209/EFTA00079292.pdf) / [OCR](https://epstein-data.com/full_text_corpus/pages?efta_number=EFTA00079292) |
| EFTA00260322 | 9 | T-Mobile subpoena — Det. Recarey, PBPD Case 05-368 | [justice.gov](https://www.justice.gov/epstein/files/DataSet%209/EFTA00260322.pdf) / [OCR](https://epstein-data.com/full_text_corpus/pages?efta_number=EFTA00260322) |
| EFTA01310387 | 10 | Most-redacted phone record (8,050 redactions, 129pp) | [justice.gov](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01310387.pdf) |
| EFTA01334722 | 10 | Redaction leak document — location data bleeds through | [justice.gov](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01334722.pdf) |
| EFTA00189310 | 9 | Villafana email — investigative phone list ("Natalie or Anja") | [justice.gov](https://www.justice.gov/epstein/files/DataSet%209/EFTA00189310.pdf) / [OCR](https://epstein-data.com/full_text_corpus/pages?efta_number=EFTA00189310) |
| EFTA00812159 | 9 | Press release confirming Trump Org number | [justice.gov](https://www.justice.gov/epstein/files/DataSet%209/EFTA00812159.pdf) / [OCR](https://epstein-data.com/full_text_corpus/pages?efta_number=EFTA00812159) |
| EFTA01073204 | 9 | FBI Deleted Page Sheet — 853 pages withheld | [justice.gov](https://www.justice.gov/epstein/files/DataSet%209/EFTA01073204.pdf) |

## External Sources

| Claim | Source |
|-------|--------|
| (212) 348-8882 = Clinton Foundation | [Clinton Foundation contact page](https://www.clintonfoundation.org/contact/), [Dun & Bradstreet](https://www.dnb.com/business-directory/company-profiles.bill_hillary__chelsea_clinton_foundation.b3b561c0b41ec9d90c6e75bd0146320e.html), [ZoomInfo](https://www.zoominfo.com/c/clinton-foundation/38589798) |
| (561) 832-2600 = Mar-a-Lago Club | [Yelp](https://www.yelp.com/biz/the-mar-a-lago-club-palm-beach), [Dun & Bradstreet](https://www.dnb.com/business-directory/company-profiles.mar-a-lago_club_llc.971ef0c60d76ac152011a1071cd973d9.html), [CallerCenter](https://www.callercenter.com/561-832-2600.html), [AllBiz](https://www.allbiz.com/business/mar-a-lago-561-832-2600) |
| Les Wexner built New Albany, OH | [Wikipedia](https://en.wikipedia.org/wiki/New_Albany,_Ohio) |
