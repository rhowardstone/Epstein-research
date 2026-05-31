# FORENSIC ACCOUNTING REPORT NO. 3
# INTER-ENTITY FUND FLOWS: EPSTEIN SHELL COMPANY NETWORK

**Classification:** Forensic Financial Analysis
**Database:** the primary document text database (1,808,915 redactions; 107,422 extracted entities; 39,588 reconstructed pages)
**Date of Analysis:** 2026-02-05
**Analyst:** Independent Forensic Researcher
**Subject:** Jeffrey E. Epstein -- Deutsche Bank Relationship Manager Code 82289

---

## EXECUTIVE SUMMARY

Analysis of text extracted from the DOJ Epstein files reveals a sophisticated multi-entity financial architecture maintained at Deutsche Bank under a single Relationship Manager code (RM 82289). At least **19 entities** operated as an interconnected fund pool (the original count of 18 has been revised upward with the identification of **Jeepers, Inc.** as a significant entity in the DS11 revisit), managed by bankers Jj Litchford (primary) and Paul Morris (secondary), with day-to-day operations handled by Stewart Oldfield and Bradley Gillin. The entire structure was organized under the umbrella designation "SOUTHERN FINANCIAL RELATIONSHIP" -- meaning Deutsche Bank treated all sub-entities as a single client relationship.

**Key findings:**
- Total consolidated assets exceeded **$110 million** across all entities at peak. **CORRECTION (Revisit):** DS11 email from Richard Kahn ([EFTA02671293](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02671293.pdf)) shows the top 3 entities alone held **$159,125,000** as of October 2015 (Southern Trust $82.5M + Haze Trust $47.375M + Southern Financial $29.25M). A June 2013 master valuation ([EFTA02678941](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02678941.pdf)) shows total portfolio of **$319,455,302** including partnerships and investments. The original $110M estimate was based on incomplete DB balance reports and significantly understated actual holdings.
- THE HAZE TRUST alone held **$49.5 million** at peak in its DBAGNY sub-account (Account N4G024943), plus investment positions in a separate Brokerage sub-account
- SOUTHERN TRUST COMPANY, INC. held **$82.5 million** at peak (10/31/2015 per [EFTA02671293](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02671293.pdf)). The original report identified only $45.15M (09/30/16), which was 11 months later and reflected intervening disbursements
- Inter-entity DDA-to-DDA fund transfers occurred via account 739110438 (Epstein personal) to at least three subsidiary accounts
- Book transfers moved funds between entities without external wire activity
- A derivatives overlay ("Harvest Collateral Yield Enhancement Strategy") operated through the structure
- The "2017 CATERPILLAR TRUST" appears as an additional entity with returned funds generating compliance concern

---

## 1. THE COMPLETE ENTITY MAP

### 1.1 Master Account Roster ([EFTA01359500](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01359500.pdf))

A recovered Deutsche Bank internal account roster reveals the full relationship under a single banker team. All accounts were assigned to:
- **Primary Officer:** Jj Litchford
- **Secondary Officer:** Paul Morris

**Entities on the roster:**

| # | Entity Name | Account Type | Relationship Tier |
|---|------------|-------------|------------------|
| 1 | JEFFREY EPSTEIN (personal) | N (Personal) | Principal |
| 2 | JEFFREY EPSTEIN (2nd account) | N (Personal) | Principal |
| 3 | SOUTHERN TRUST COMPANY, INC. | M (Corporate) | Tier 1 Holding |
| 4 | SOUTHERN FINANCIAL LLC | D (Corporate) | Tier 1 Holding |
| 5 | NEPTUNE, LLC | D (Corporate) | Tier 2 Operating |
| 6 | HYPERION AIR, LLC | D (Corporate) | Tier 2 Operating |
| 7 | JEGE, INC | D (Corporate) | Tier 2 Operating |
| 8 | PLAN D, LLC | D (Corporate) | Tier 2 Operating |
| 9 | JEGE, LLC | D (Corporate) | Tier 2 Operating |
| 10 | THE 2007 JEFFREY E. EPSTEIN [Trust] | Trust | Trust Vehicle |
| 11 | DARREN K. INDYKE PLLC | D (Professional) | Legal Nexus |
| 12 | LEON D. BLACK (2 accounts) | N (Personal) | Associated Client |
| 13 | DOMINIQUE LEIMER (2 accounts) | N (Personal) | Associated Client |
| 14 | CHRISTOPHER A. BOIES | N (Personal) | Associated Client |
| 15 | TODD & KAREN WANEK JTWROS | N (Personal) | Associated Client |

**Source:** [EFTA01359500](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01359500.pdf) -- Deutsche Bank internal account management record

### 1.2 Extended Entity Network ([EFTA01477454](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01477454.pdf))

A Morris/Oldfield banker assignment document reveals the FULL breadth of entities managed:

**Core Epstein Entities:**
- JEFFREY EPSTEIN (personal)
- SOUTHERN FINANCIAL LLC ("SOUTHERN FIN")
- SOUTHERN TRUST COMPANY ("SOUTHERN TRU")
- NEPTUNE LLC
- HYPERION AIR LLC / HYPERION AIR INC
- JEGE INC
- JEGE LLC
- NES LLC
- PLAN D LLC
- DARREN K. INDYKE PLLC
- HBRK ASSOCIATES INC ("HBRK ASSOCIA")
- BUTTERFLY TRUST
- GRATITUDE AMERICA [LTD]
- ZORRO MANAGEMENT LLC / ZORRO DEVELOPMENT CORP
- JSC INTERIORS LLC
- MORT, INC
- 55W 2007 LLC / SSW LLC
- GEW 2007 LLC
- CRW 2007 LLC / CRW 2009 LLC

**Additional Managed Names (same banker team):**
- LEON D. BLACK
- CHRISTOPHER BOIES
- DOMINIQUE LEIMER
- WANEK TRUST OF 2000 / TODD R. WANEK
- NEW YORK STRATEGY GROUP
- MARK F. DZIALGA
- THE NATIONAL ORGANIZATION [FOR WOMEN?]
- SHARI WAGNER 2014 GRANT
- KATI FORSYTHE 2014 GRANT

**Source:** [EFTA01477454](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01477454.pdf) -- Morris/Oldfield banker assignment master list

### 1.3 SAR Subject Listing ([EFTA01656524](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01656524.pdf))

A Suspicious Activity Report listing identifies **25 subjects** in a single filing:

1. AVILOOP LLC
2. [Redacted]
3. BUTTERFLY TRUST
4. [Redacted]
5. DARREN K INDYKE PLLC
6-7. [Redacted]
8. HBRK ASSOCIATES INC
9. [Redacted]
10. HYPERION AIR LLC
11. INDYKE [personal]
12. JEGE LLC
13. JSC INTERIORS LLC
14. [Redacted]
15. KLEIN
16. LSJE LLC
17-18. [Redacted]
19. NEPTUNE LLC
20. PLAN D LLC
21. SAIPHLR
22. SOUTHERN COUNTRY INTERNATIONAL
23. SOUTHERN FINANCIAL LLC
24. SOUTHERN TRUST COMPANY [INC.]
25. ZORRO MANAGEMENT LLC

**Key Observation:** This SAR covers 25 subjects in a single suspicious activity filing -- an extraordinarily large filing that indicates regulators viewed the entire network as a single suspicious operation.

---

## 2. CONSOLIDATED BALANCE SNAPSHOTS

### 2.1 "Large, Zero and Negative Balances" Reports

Deutsche Bank generated periodic internal reports under RM CODE 82289 flagging account balances. These recovered snapshots provide point-in-time views of the entire entity network.

#### Snapshot A: 09/30/2016 ([EFTA01381029](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01381029.pdf))
| Entity | Category | Balance |
|--------|----------|---------|
| SOUTHERN TRUST COMPANY, INC. | M | **$45,151,615.37** |

*Peak balance observed for Southern Trust.*

#### Snapshot B: 06/21/2018 ([EFTA01381246](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01381246.pdf))
| Entity | Category | Balance |
|--------|----------|---------|
| JEFFREY EPSTEIN | N | $1,224,163.61 |
| HYPERION AIR, LLC | D | $347,674.83 |
| PLAN D, LLC | D | [partially redacted] |
| JEGE, LLC | D | $299,328.13 |
| DARREN K. INDYKE PLLC | D | $243,363.55 |
| HBRK ASSOCIATES, INC | D | $211,289.05 |
| SOUTHERN TRUST COMPANY, INC. | M | [OCR degraded] |
| BUTTERFLY TRUST | M | $733,701.04 |
| GRATITUDE AMERICA, LTD | M | $323,223.15 |
| DARREN K. INDYKE PLLC (2nd acct) | M | $267,972.25 |
| THE HAZE TRUST | D | **$49,460,098.13** |
| SOUTHERN FINANCIAL LLC | D | $532,186.86 |
| SOUTHERN TRUST COMPANY, INC. | D | $102,625.90 |

*Peak balance observed for The Haze Trust: $49.46M.*

#### Snapshot C: 08/17/2018 ([EFTA01381149](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01381149.pdf))
| Entity | Category | Balance |
|--------|----------|---------|
| JEFFREY EPSTEIN | N | $1,243,515.74 |
| SOUTHERN FINANCIAL LLC | D | $376,315.00 |
| PLAN D, LLC | O | $326,685.34 |
| JEGE, LLC | D | $285,583.43 |
| DARREN K. INDYKE PLLC | D | $259,740.02 |
| HBRK ASSOCIATES, INC | D | $149,498.33 |
| NES LLC | D | $264,466.13 |
| GRATITUDE AMERICA, LTD | N | $2,075,025.07 |
| ZORRO MANAGEMENT, LLC | O | $424,475.56 |
| THE HAZE TRUST | D | $2,503,667.84 |
| SOUTHERN TRUST COMPANY, INC. | [M] | [OCR degraded] |
| BUTTERFLY TRUST | [M] | $704,736.63 |
| GRATITUDE AMERICA, LTD (2nd) | [M] | $323,679.36 |
| DARREN K. INDYKE PLLC (2nd) | [M] | $268,350.45 |
| THE HAZE TRUST (2nd acct) | D | **$40,583,100.79** |
| SOUTHERN FINANCIAL LLC (2nd) | [D] | $534,440.04 |
| SOUTHERN TRUST COMPANY, INC. | [D] | $102,917.53 |

**CRITICAL OBSERVATION:** Multiple entities (Haze Trust, Southern Financial, Southern Trust, Darren K. Indyke PLLC, Gratitude America) appear TWICE in the same report with different account categories (D vs M, or two D accounts). This means each entity maintained **multiple accounts** at Deutsche Bank -- e.g., The Haze Trust had at least two accounts, one showing $2.5M and another showing $40.6M.

#### Snapshot D: 08/28/2018 ([EFTA01413971](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01413971.pdf))
| Entity | Category | Balance |
|--------|----------|---------|
| SOUTHERN FINANCIAL LLC | D | $1,376,315.00 |
| NES, LLC | D | $252,123.92 |
| LSJE, LLC | D | $240,223.25 |
| ZORRO MANAGEMENT, LLC | D | [partially recovered] |
| SOUTHERN TRUST COMPANY, INC. | M | $1,485,501.88 |
| THE HAZE TRUST | D | **$35,583,100.79** |
| SOUTHERN FINANCIAL LLC (2nd) | D | $534,440.04 |

#### Snapshot E: 10/03/2018 ([EFTA01431991](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01431991.pdf))
| Entity | Category | Balance |
|--------|----------|---------|
| SOUTHERN [FINANCIAL] | [D] | [OCR degraded] |
| NEPTUNE, LLC | D | $366,477.90 |
| HYPERION AIR, LLC | D | $147,203.75 |
| PLAN D, LLC | D | $225,444.72 |
| JEGE, LLC | D | $255,684.99 |
| DARREN K. INDYKE PLLC | D | $184,512.01 |
| NES, LLC | D | $149,710.54 |
| ZORRO MANAGEMENT, LLC | D | $124,356.26 |
| THE HAZE TRUST | D | $2,503,667.84 |
| SOUTHERN TRUST COMPANY, INC. | M | $2,470,113.49 |
| BUTTERFLY TRUST | M | $705,802.21 |
| GRATITUDE AMERICA, LTD | M | $314,162.94 |
| DARREN K. INDYKE PLLC (2nd) | M | $268,754.26 |
| THE HAZE TRUST (2nd acct) | D | **$12,690,279.36** |
| SOUTHERN FINANCIAL LLC | D | $1,536,739.37 |
| SOUTHERN TRUST COMPANY, INC. | D | $103,227.37 |

#### Snapshot F: 11/14/2018 ([EFTA01430931](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01430931.pdf))
| Entity | Category | Balance |
|--------|----------|---------|
| JEFFREY EPSTEIN | N | $4,378,298.11 |
| SOUTHERN FINANCIAL LLC | D | [OCR degraded] |
| NEPTUNE, LLC | D | $276,010.83 |
| HYPERION AIR, LLC | D | $147,203.75 |
| PLAN D, LLC | D | $789,557.84 |
| JEGE, LLC | D | $239,917.66 |
| DARREN K. INDYKE PLLC | D | $116,631.92 |
| NES, LLC | D | $252,347.66 |
| ZORRO MANAGEMENT LLC | D | $265,245.21 |
| THE HAZE TRUST | D | $2,503,667.84 |

#### Snapshot G: Undated, ~Late 2018 ([EFTA01430750](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01430750.pdf))
| Entity | Category | Balance |
|--------|----------|---------|
| JEFFREY EPSTEIN | N | $2,340,530.11 |
| SOUTHERN FINANCIAL LLC | D | $1,187,706.86 |
| HYPERION AIR, LLC | D | $147,203.75 |
| PLAN D, LLC | D | $218,453.14 |
| JEGE, LLC | D | $255,684.99 |
| DARREN K. INDYKE PLLC | D | $167,897.44 |
| NES, LLC | D | $114,217.89 |
| GRATITUDE AMERICA, LTD | N | $2,025,366.25 |
| ZORRO MANAGEMENT LLC | D | $118,575.62 |
| THE HAZE TRUST | D | $2,503,667.84 |
| SOUTHERN TRUST COMPANY, INC. | M | $2,470,113.49 |
| BUTTERFLY TRUST | M | $705,802.21 |
| SOUTHERN FINANCIAL LLC (2nd) | D | $1,536,739.37 |
| SOUTHERN TRUST COMPANY, INC. | D | $103,227.37 |

#### Snapshot H: Undated, Highest Aggregates ([EFTA01430852](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01430852.pdf))
| Entity | Category | Balance |
|--------|----------|---------|
| JEFFREY EPSTEIN | N | $2,507,267.47 |
| JEGE, LLC | D | $463,079.08 |
| DARREN K. INDYKE PLLC | D | $439,904.52 |
| HBRK ASSOCIATES, INC | D | $418,598.61 |
| SOUTHERN TRUST COMPANY, INC. | M | [OCR: ~$1.15M?] |
| GRATITUDE AMERICA, LTD | M | $365,988.50 |
| THE HAZE TRUST | D | **$49,233,909.70** |
| SOUTHERN FINANCIAL LLC | D | **$7,013,127.50** |
| SOUTHERN TRUST COMPANY, INC. | D | **$4,096,966.10** |

---

## 3. INTER-ENTITY FUND FLOW ANALYSIS

### 3.1 DDA-to-DDA Internal Transfers (Fedwire Range [EFTA01482000](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01482000.pdf)-01530000)

The personal Epstein account (DDA# 000000739110438) served as the **central hub** for inter-entity transfers:

| EFTA# | Transfer Description | From Account | To Account |
|-------|---------------------|-------------|-----------|
| [EFTA01482909](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01482909.pdf) | Funds Transferred From DDA | 739110438 (Epstein) | [destination redacted] |
| [EFTA01482935](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01482935.pdf) | Funds Transferred From DDA | 739110438 (Epstein) | [destination redacted] |
| [EFTA01482950](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01482950.pdf) | Funds Transferred From DDA | 739110438 (Epstein) | **739123130** |
| [EFTA01482967](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01482967.pdf) | Funds Transferred From DDA | 739110438 (Epstein) | **739121472** |
| [EFTA01483039](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01483039.pdf) | Funds Transferred From DDA | 739110438 (Epstein) | **739474340** |

**Additional flow:** An asset account transfer was also observed:
- [EFTA01483035](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01483035.pdf): "From Asset Ac# **Q30171005** To DDA Ac# 000000739110438"

**CRITICAL:** Asset account **Q30171005** is confirmed as belonging to **SOUTHERN TRUST COMPANY, INC.** (Source: [EFTA01583582](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01583582.pdf), [EFTA01584675](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01584675.pdf), [EFTA01584982](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01584982.pdf) -- Morgan Online Administration Tool records). This means **Southern Trust Company liquidated assets and sent proceeds to Epstein's personal account**.

Account 739121472 appears in multiple records with "LETTER FROM CLIENT" and "AS REQUESTED" notations ([EFTA01497326](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01497326.pdf), [EFTA01497327](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01497327.pdf), [EFTA01497375](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01497375.pdf)), suggesting this was a managed account where transfers were made at the client's direction.

### 3.2 Book Transfers (Internal Bank Movements)

Book transfers -- movements within the same bank that bypass the wire system -- were documented:

| EFTA# | Description | Counterparty/Detail |
|-------|-------------|-------------------|
| [EFTA01483362](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01483362.pdf) | 03/30 Book Transfer | A/C: Zorro Trust, New York, NY |
| [EFTA01527665](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01527665.pdf) | 11/16 Book Transfer | Zorro Trust |
| [EFTA01482759](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01482759.pdf) | Book Transfer | NC: STRANGHAYES HOLDING |
| [EFTA01483094](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01483094.pdf) | Book Transfer | NC: Banc[o...] |
| [EFTA01483269](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01483269.pdf) | 10/28 Book Transfer | MC: Banco |
| [EFTA01483341](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01483341.pdf) | Book Transfer | A/C: The[...] |
| [EFTA01524814](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01524814.pdf) | 05/30 Book Transfer | NC: Samantha K Harris, New York, NY |
| [EFTA01528492](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01528492.pdf) | 06/14 Book Transfer | A/C: Gulfstream A[erospace] |
| [EFTA01437262](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01437262.pdf) | BOOK TRANSFER D[ebit] | [In context of OUTGOING MONEY from entity account] |
| [EFTA01482368](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01482368.pdf) | Book Transfer Debit | [Multiple] |
| [EFTA01482375](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01482375.pdf) | Book Transfer Debit | [Multiple] |
| [EFTA01524219](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01524219.pdf) | Book Transfer Debit | [From entity account] |

**Key observation:** Book transfers to ZORRO TRUST appear in both the Epstein personal account statements and the Zorro entity statements, confirming bidirectional money flow. The Gulfstream book transfer connects to aviation operations (JEGE, LLC / HYPERION AIR).

### 3.3 Internal Transfer of Funds / Automatic Transfers

| EFTA# | Description |
|-------|-------------|
| [EFTA01482260](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01482260.pdf) | 03/18 Internal Transfer of Funds, As Requested |
| [EFTA01482271](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01482271.pdf) | 04/05 Internal Transfer of Funds, As Requested |
| [EFTA01482474](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01482474.pdf) | Internal Funds Transfer |
| [EFTA01482494](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01482494.pdf) | Internal Funds Transfer |
| [EFTA01482500](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01482500.pdf) | Internal Funds Transfer |
| [EFTA01482650](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01482650.pdf) | Internal Funds Transfer - JEFFREY E EPSTEIN |
| [EFTA01528427](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01528427.pdf) | Internal Transfer of Funds |
| [EFTA01528444](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01528444.pdf) | Internal Transfer |
| [EFTA01414982](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01414982.pdf) | SOUTHERN FINANCIAL LLC $1,132,731.96 -- **AUTOMATIC TRNSFR C** |

**CRITICAL:** The AUTOMATIC TRNSFR notation on the Southern Financial LLC entry ([EFTA01414982](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01414982.pdf)) indicates a **standing automatic sweep** -- likely a cash management arrangement where funds were automatically transferred between Southern Financial and another entity (probably Epstein personal or Southern Trust) on a scheduled basis.

### 3.4 Fedwire Transfers to/from Entity Names

| EFTA# | Wire Description | Entity Referenced |
|-------|-----------------|------------------|
| [EFTA01482283](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01482283.pdf) | 05/29 Fedwire Debit Via: Wells Fargo NA/121000248 | NC: **Zorro Development Corp.** |
| [EFTA01482300](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01482300.pdf) | 07/03 Fedwire Debit Via: Mfrs Buf/022000046 | NC: International Jet Interiors -- Ref. **Jege** |
| [EFTA01524478](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01524478.pdf) | Fedwire Debit Via: Citibank West | **Nes LIc** [NES LLC] / Direct Debit |
| [EFTA01482300](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01482300.pdf) | Fedwire Debit to Firstbank Puerto Rico | Fao **Lsje, LLC** |
| [EFTA01527665](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01527665.pdf) | Fedwire Debit Via: multiple banks | A/C: **Lsj LLC** [LSJE] |

### 3.5 The "SOUTHERN FINANCIAL RELATIONSHIP" Structure

A critical recovered record ([EFTA01427242](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01427242.pdf)) explicitly identifies the hierarchical structure:

```
Stewart Oldfield
SOUTHERN FINANCIAL RELATIONSHIP -- Darren K. Indyke PLLC
                                    DARREN K. INDYKE PLLC

Stewart Oldfield
SOUTHERN FINANCIAL RELATIONSHIP -- JEGE, Inc
                                    JEGE, INC -- 6100 [Red Road address]
```

This confirms that **SOUTHERN FINANCIAL LLC was the parent/umbrella relationship** under which other entities were nested. Additional records confirm:
- JEGE, LLC was added to the SOUTHERN FINANCIAL RELATIONSHIP on **2/17/2015** ([EFTA01398741](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01398741.pdf)), managed by Paul Morris
- GRATITUDE AMERICA was part of the "SOUTHERN FINANCIAL RELATIONSHIP" ([EFTA01477330](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01477330.pdf))
- The relationship was activated **10/19/2015** ([EFTA01477330](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01477330.pdf))

---

## 4. ENTITY-BY-ENTITY ANALYSIS

### 4.1 THE HAZE TRUST (Account N4G024943)
- **Peak Balance:** $49,460,098.13 (06/21/18)
- **Account:** N4G024943, also referenced as SAM1788880 (AML case ID)
- **Multiple accounts:** At least 2 DDAs -- one showing ~$2.5M and another showing $40-49M
- **AML inquiries:** Subject of extensive compliance investigation ([EFTA01413743](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01413743.pdf), [EFTA01414223](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01414223.pdf), [EFTA01414241](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01414241.pdf)) involving Cynthia Rodriguez, Stewart Oldfield, Joshua Shoshan, Donald Summer, Cherie Quigley, Zbynek Kozelsky, and the AML Compliance Inquiries team
- **Balance trajectory:** $49.46M (06/18) -> $40.58M (08/17/18) -> $35.58M (08/28/18) -> $12.69M (10/03/18) -> $2.50M (11/14/18)
- **Drain rate:** $46.96 MILLION withdrawn in approximately 5 months (June-November 2018)

### 4.2 SOUTHERN TRUST COMPANY, INC.
- **Peak Balance:** $45,151,615.37 (09/30/16)
- **Asset Account:** Q30171005 (confirmed via Morgan Online Administration Tool)
- **Multiple categories:** Appeared as both M (managed) and D in reports
- **Fund transfers FROM:** Asset account Q30171005 transferred to Epstein personal DDA 739110438
- **Balance range:** $102,625 - $45,151,615
- **Second balance observation:** $43,785,615.37 (another date in 2016, [EFTA01381103](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01381103.pdf))

### 4.3 SOUTHERN FINANCIAL LLC (Account N4G-026161)
- **Peak Balance:** $7,013,127.50
- **Account Number:** N4G-026161 (confirmed via email subjects)
- **AUTOMATIC TRANSFER:** $1,132,731.96 automatic transfer documented
- **Balance range:** $376,315 - $7,013,127
- **Subject of periodic review:** "2018 Periodic Review of Accts Southern Financial" ([EFTA01406280](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01406280.pdf))

### 4.4 NEPTUNE, LLC (Account xxx3424/xxx342)
- **Account ending:** xxx3424 (or xxx342)
- **Peak Balance:** ~$366,477.90
- **Monthly balance tracking (from consolidated snapshots):**
  - $250,390.13 (one snapshot)
  - $156,217.67 / $165,204.86 / $137,953.37 (various months)
  - $155,820.43 / $155,275.32 (close together)
  - $209,812.70 / $182,205.85 / $135,620.37
  - $276,010.83 (11/14/18)
  - $366,477.90 (10/03/18)
- **Suspicious wires:** Email chain regarding "Neptune $1200 and $1000 wires" involving Natalie Barak, Richard Kahn, Stewart Oldfield, and Bradley Gillin ([EFTA01425378](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01425378.pdf), [EFTA01426627](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01426627.pdf), [EFTA01435069](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01435069.pdf))
- **Bank statements:** Extensive monthly statements from 1/2012 through at least 2/2014 ([EFTA01496441](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01496441.pdf)-01496643)
- **Corporate Resolution:** Subject of corporate resolution inquiry ([EFTA01430266](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01430266.pdf))
- **Property management:** "Property manager at Neptune" ([EFTA01920341](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01920341.pdf)) -- suggesting Neptune held real property
- **High risk review:** Subject of "Periodic Review of High Risk" combined with another entity (GCIS# referenced)

### 4.5 HYPERION AIR, LLC / INC
- **Balance:** Stable at $147,203.75 across multiple snapshots (suggests a maintenance/reserve account)
- **Purpose:** Aviation -- "Sikorsky Statement - Hyperion Air" ([EFTA01334323](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01334323.pdf))
- **Bank statements:** Extensive monthly statements ([EFTA01494290](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01494290.pdf)-01494836)
- **Entity evolution:** Changed from "HYPERION AIR INC" to "HYPERION AIR LLC"
- **KYC inquiry:** [EFTA01426009](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01426009.pdf)

### 4.6 JEGE, LLC / JEGE, INC
- **Balance range:** $239,917 - $463,079
- **Address:** 6100 Red Road [Miami area]
- **Aircraft:** N908JE Boeing registered to JEGE INC
- **Aircraft sale:** N722JE escrow through AIC Title Service, involving Darren Indyke and Richard Kahn ([EFTA01334323](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01334323.pdf))
- **Fedwire:** International Jet Interiors payment "Ref. Jege" ([EFTA01482300](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01482300.pdf))
- **Added to Southern Financial Relationship:** 2/17/2015 via Paul Morris, with Indyke added as POA in February 2014

### 4.7 PLAN D, LLC
- **Balance range:** $218,453 - $789,557
- **Peak:** $789,557.84 (11/14/18)

### 4.8 NES, LLC
- **Balance range:** $114,217 - $563,000 (approximate upper from context)
- **Direct debit:** NES LLC referenced in Fedwire debit via Citibank ([EFTA01524478](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01524478.pdf))
- **Fedwire confirmation:** Outgoing wire from NES entity confirmed

### 4.9 DARREN K. INDYKE PLLC
- **Balance range:** $116,631 - $439,904
- **TWO accounts:** Appears twice in consolidated reports (one "D" category, one "M" category)
- **D account range:** $116,631 - $439,904
- **M account:** Stable ~$267,972 - $268,754
- **PBS transaction:** 06/21/2017 -- PBS (Pending Bank Sweep?) record ([EFTA01419809](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01419809.pdf))
- **Wire authorization:** JEE wire to Kellerhals involving Litchford, Kahn, Indyke ([EFTA01346198](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01346198.pdf))
- **Legal entity relationship:** Explicitly placed under "SOUTHERN FINANCIAL RELATIONSHIP" ([EFTA01427242](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01427242.pdf))

### 4.10 HBRK ASSOCIATES, INC
- **Balance range:** $149,498 - $418,598
- **Purpose:** Accounting services (per SAR, [EFTA01656524](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01656524.pdf))

### 4.11 GRATITUDE AMERICA, LTD
- **Balance range:** $314,162 - $4,300,000+ (approximate from context)
- **Two accounts:** One "N" (up to $2,075,025) and one "M" (~$323,000)
- **Within Southern Financial Relationship** ([EFTA01477330](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01477330.pdf))

### 4.12 ZORRO MANAGEMENT, LLC / ZORRO DEVELOPMENT CORP / ZORRO TRUST
- **Balance range:** $118,575 - $464,682
- **Fedwire:** 05/29 wire via Wells Fargo to Zorro Development Corp ([EFTA01482283](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01482283.pdf))
- **Book transfers:** Two confirmed book transfers TO Zorro Trust ([EFTA01483362](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01483362.pdf), [EFTA01527665](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01527665.pdf))
- **Property:** Zorro Ranch, P.O. Box 567, Stanley, NM 87056 / 49 Zorro Ranch Road
- **PBS record:** 06/21/2017 ([EFTA01419809](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01419809.pdf))
- **Real property purchase:** "Purchase by Zorro Trust of certain real property and appurtenant" ([EFTA01503431](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01503431.pdf) area)

### 4.13 BUTTERFLY TRUST
- **Balance range:** $700,000 - $734,175
- **Remarkably stable:** $705,802.21 across multiple snapshots
- **Category:** M (managed/trust account)

### 4.14 LSJE, LLC
- **Balance range:** $172,419 - $501,905
- **Wire activity:** Active outgoing wires -- email subject "HELP TO STOP WIRE FROM LSJE TO [destination]" involving Richard Kahn and Bradley Gillin ([EFTA01417218](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01417218.pdf), [EFTA01426081](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01426081.pdf), [EFTA01426305](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01426305.pdf))
- **Fedwire to Puerto Rico:** Wire to Firstbank Puerto Rico "Fao Lsje, LLC" ([EFTA01483362](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01483362.pdf))
- **GCIS review:** Combined with another entity ([EFTA01362517](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01362517.pdf): "GCIS#483882 & LSJE")
- **Outgoing wire:** "LSJE Outgoing Wire" to unspecified recipient ([EFTA01403413](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01403413.pdf))
- **Monthly bonuses:** "LSJE bonus for Sept" ([EFTA01737736](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01737736.pdf)) -- suggests payroll/compensation function
- **Plant orders:** Multiple "Plant Order - LSJE LLC" references -- possibly landscape/property maintenance

### 4.15 PRYTANEE, LLC
- **Balance:** $197,XXX.14 (partially OCR-degraded, [EFTA01415196](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01415196.pdf))
- **Date:** 07/20/18 snapshot
- **Purpose:** Certificates requested ("Forms and Prytanee certificates")

### 4.16 THE 2017 CATERPILLAR TRUST
- **Appeared in RM 82289 reports** ([EFTA01423664](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01423664.pdf))
- **"Returned funds to Caterpillar"** -- Multiple email chains ([EFTA01372227](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01372227.pdf), [EFTA01372590](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01372590.pdf), [EFTA01383963](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01383963.pdf), [EFTA01383964](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01383964.pdf), [EFTA01384822](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01384822.pdf), [EFTA01425048](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01425048.pdf))
- **Participants:** Brigid Macias, Bradley Gillin, Richard Kahn, Darren Indyke, Stewart Oldfield
- **Two accounts:** "The 2017 Caterpillar Trust 2 accounts" ([EFTA01430999](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01430999.pdf))
- **KYC issues:** "Caterpillar KYC" inquiry ([EFTA01421324](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01421324.pdf))
- **Case number:** Case#13959886 ([EFTA01408771](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01408771.pdf))

### 4.17 HELICOPTER 1029 LLC
- **Serial Number:** sn 760750 (Sikorsky S-76C)
- **Sale activity:** "Sale of the Sikorsky S76C helicopter" ([EFTA01339374](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01339374.pdf))
- **Helicopter resale:** Associated with helicopterresales.com

### 4.18 AVILOOP LLC
- **Listed as Subject 1 of 25 in SAR**
- **Bank statements:** [EFTA01525616](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01525616.pdf)-01525878

---

## 5. DERIVATIVES AND STRUCTURED PRODUCTS

### 5.1 Harvest Collateral Yield Enhancement Strategy (CYES)

- **Manager:** Harvest Volatility Management (www.harvestvolmgt.com)
- **Product:** "Harvest Collateral Yield Enhancement Strategy" -- a derivatives overlay
- **Deutsche Bank internal name:** "DB Harvest Collateral Yield Enhancement Strategy"
- **Key contacts:** Stewart Oldfield, Paul Barrett (DB trader), Kyle Vaughn
- **Email trail:** Extensive communications about the strategy ([EFTA01385614](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01385614.pdf) through [EFTA01438047](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01438047.pdf))
- **Updates:** "Harvest CYES Update" emails sent to Stewart Oldfield ([EFTA01435880](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01435880.pdf))
- **ALPHAGROUP connection:** Communications reference "ALPHAGROUP" in same context ([EFTA01386013](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01386013.pdf))
- **PLN Roll:** Paul Barrett handled "PLN Roll" (structured note rollovers) for the Epstein relationship ([EFTA01413882](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01413882.pdf), [EFTA01426766](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01426766.pdf)), coordinated with Martin Zeman, Davide-A Sferrazza, and Xavier Avila

**Assessment:** The Harvest CYES was likely deployed on the SOUTHERN TRUST COMPANY or HAZE TRUST portfolio (the two largest accounts), using Deutsche Bank's advisory infrastructure. The strategy appears to have been a collateralized options overlay generating yield on the multi-million dollar holdings.

### 5.2 New Derivatives Account

- Extensive email chain about opening a "New Derivatives account" ([EFTA01355903](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01355903.pdf)-01356122)
- Involved: Keith Buckholz, Srikanta Gouda, Nitin-X Singh, CRM-PWM Derivatives team, Collateral Admin-NY, FX Middle Office
- This was a DB Private Wealth Management derivatives account

---

## 6. FUND FLOW DIAGRAM

### 6.1 The Hub-and-Spoke Architecture

```
                            EXTERNAL SOURCES
                                  |
                                  v
                     +-----------------------+
                     |   JEFFREY EPSTEIN     |
                     |   Personal Account    |
                     |   DDA: 739110438      |
                     |   Balance: $1.2-4.4M  |
                     +----------+------------+
                                |
            DDA-to-DDA Transfers (Documented)
                                |
           +--------------------+--------------------+
           |                    |                    |
           v                    v                    v
    DDA: 739123130       DDA: 739121472       DDA: 739474340
    [Entity Unknown]     [Entity Unknown]     [Entity Unknown]
                         "Letter from Client"
                         "As Requested"

============================================================
   TIER 1: MASTER HOLDING ENTITIES
============================================================

  +---------------------------+     +---------------------------+
  | SOUTHERN TRUST CO., INC.  |     |  THE HAZE TRUST           |
  | Peak: $45.15M             |     |  Account: N4G024943       |
  | Asset Acct: Q30171005     |     |  Peak: $49.46M            |
  | Category: M (Managed)     |     |  Category: D              |
  |                           |     |  DRAIN: $49.5M -> $2.5M   |
  |  Transfers assets TO -->  |     |  in 5 months (mid-2018)   |
  |  Epstein personal DDA     |     |                           |
  +---------------------------+     +---------------------------+
           |                                    |
           | Automatic transfers                | Balance drawdowns
           v                                    v
  +---------------------------+
  | SOUTHERN FINANCIAL LLC    |
  | Account: N4G-026161       |
  | Peak: $7.01M              |
  | AUTOMATIC TRNSFR: $1.13M  |
  | "Umbrella Relationship"   |
  +---------------------------+
           |
           | SOUTHERN FINANCIAL RELATIONSHIP
           | (All sub-entities nested under this)
           |
============================================================
   TIER 2: OPERATING ENTITIES
============================================================

  +------------------+  +------------------+  +------------------+
  | NEPTUNE, LLC     |  | HYPERION AIR     |  | PLAN D, LLC      |
  | Acct: xxx3424    |  | LLC/INC          |  |                  |
  | Bal: $106-366K   |  | Bal: $147,203    |  | Bal: $218-790K   |
  | Wire: $1200,$1000|  | (STABLE-reserve) |  |                  |
  | Property mgmt    |  | Aviation/Sikorsky|  |                  |
  +------------------+  +------------------+  +------------------+

  +------------------+  +------------------+  +------------------+
  | JEGE, LLC/INC    |  | NES, LLC         |  | LSJE, LLC        |
  | Bal: $240-463K   |  | Bal: $114-563K   |  | Bal: $172-502K   |
  | Aircraft N908JE  |  | Fedwire to       |  | Wires to PR      |
  | Jet Interiors    |  | Citibank         |  | STOP WIRE order   |
  | N722JE escrow    |  |                  |  | Monthly bonuses   |
  +------------------+  +------------------+  +------------------+

  +------------------+  +------------------+  +------------------+
  | ZORRO MGMT, LLC  |  | HBRK ASSOC, INC  |  | DARREN K. INDYKE |
  | Bal: $119-465K   |  | Bal: $149-419K   |  | PLLC             |
  | Zorro Ranch, NM  |  | Accounting svcs  |  | Bal: $117-440K   |
  | Book transfers   |  |                  |  | 2 accounts (D+M) |
  | from Epstein     |  |                  |  | Legal nexus       |
  | Fedwire via WF   |  |                  |  | Under S.Fin Rel.  |
  +------------------+  +------------------+  +------------------+

============================================================
   TIER 3: TRUST/CHARITABLE ENTITIES
============================================================

  +------------------+  +------------------+
  | BUTTERFLY TRUST  |  | GRATITUDE        |
  | Bal: ~$705K      |  | AMERICA, LTD     |
  | (Very stable)    |  | Bal: $314K-$2.1M |
  | Category: M      |  | 2 accounts       |
  +------------------+  +------------------+

============================================================
   TIER 4: ADDITIONAL ENTITIES
============================================================

  +------------------+  +------------------+  +------------------+
  | PRYTANEE, LLC    |  | 2017 CATERPILLAR |  | HELICOPTER 1029  |
  | Bal: ~$197K      |  | TRUST (2 accts)  |  | LLC              |
  | Certificates     |  | Returned funds   |  | Sikorsky S-76C   |
  +------------------+  | KYC issues       |  | sn 760750        |
                        +------------------+  +------------------+

  +------------------+  +------------------+  +------------------+
  | AVILOOP LLC      |  | JSC INTERIORS    |  | CRW 2009 LLC     |
  |                  |  | LLC              |  | Bal: $251,903    |
  +------------------+  +------------------+  +------------------+

  +------------------+  +------------------+
  | 55W 2007 LLC     |  | GEW 2007 LLC     |
  | (SSW LLC)        |  |                  |
  +------------------+  +------------------+
```

### 6.2 Documented Inter-Entity Flow Directions

```
SOUTHERN TRUST CO. (Asset Q30171005)
    -------> EPSTEIN PERSONAL (DDA 739110438)  [Asset liquidation]

EPSTEIN PERSONAL (DDA 739110438)
    -------> DDA 739123130  [Unknown entity]
    -------> DDA 739121472  [Unknown entity, "letter from client"]
    -------> DDA 739474340  [Unknown entity]
    -------> ZORRO TRUST    [Book transfers x2]

SOUTHERN FINANCIAL LLC
    -------> [AUTOMATIC TRNSFR $1,132,731.96]  [Standing sweep]

LSJE, LLC
    -------> Firstbank Puerto Rico  [Fedwire]
    -------> [STOPPED WIRE - destination redacted]

EPSTEIN PERSONAL
    -------> ZORRO DEVELOPMENT CORP  [Fedwire via Wells Fargo]
    -------> International Jet Interiors (ref JEGE)  [Fedwire]
    -------> Nautilus Inc  [Fedwire via Firstbank PR]

NES LLC
    -------> [Fedwire via Citibank West]

NEPTUNE LLC
    -------> $1,200 wire  [recipients redacted]
    -------> $1,000 wire  [recipients redacted]

[ENTITY UNKNOWN]
    -------> STRANGHAYES HOLDING  [Book Transfer]

[ENTITY]
    -------> Gulfstream Aerospace  [Book Transfer]
```

---

## 7. KEY FORENSIC FINDINGS

### 7.1 The Haze Trust Rapid Drawdown (June-November 2018)

The most striking fund flow pattern is the **$46.96 million drawdown** of The Haze Trust in approximately 5 months:

| Date | Haze Trust Balance (Primary) | Change |
|------|---------------------------|--------|
| 06/21/2018 | $49,460,098.13 | -- |
| 08/17/2018 | $40,583,100.79 | -$8,876,997 |
| 08/28/2018 | $35,583,100.79 | -$5,000,000 |
| 10/03/2018 | $12,690,279.36 | -$22,892,821 |
| 11/14/2018 | $2,503,667.84 | -$10,186,612 |

**Total drained: ~$46,956,430**

This drawdown coincides with the period when Deutsche Bank was preparing to exit the Epstein relationship. The $5,000,000 exact round-number drop between 08/17 and 08/28 suggests a single large transfer. The massive $22.9M drop in October 2018 could indicate bulk asset liquidation and transfer.

### 7.2 Caterpillar Trust -- Returned Funds Compliance Issue

Multiple email chains discuss "returned funds to Caterpillar" -- funds that were sent to the Caterpillar Trust but were returned/rejected. Key participants:
- **Brigid Macias** (DB operations)
- **Bradley Gillin** (DB compliance/operations)
- **Richard Kahn** (Epstein CFO)
- **Darren Indyke** (Epstein attorney)

The Caterpillar Trust had **2 accounts** (confirmed: "The 2017 Caterpillar Trust 2 accounts") and was subject to a separate KYC review (Case#13959886). The returned funds suggest either the receiving bank rejected the transfer or compliance holds were placed.

### 7.3 Neptune LLC Wire Anomalies

The "$1200 and $1000 wires" from Neptune LLC ([EFTA01425378](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01425378.pdf), [EFTA01426627](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01426627.pdf), [EFTA01435069](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01435069.pdf)) are unusually small for a corporate account. These small, round-number wires from an entity holding $100K-$366K could indicate:
- Test transactions before larger transfers
- Regular small payments (rent, services)
- Structuring to avoid reporting thresholds (though at $1200/$1000, this would be far below the $10K CTR threshold)

### 7.4 LSJE Wire Emergency

Three separate email records document a frantic "HELP TO STOP WIRE FROM LSJE TO [destination]" message involving Richard Kahn and Bradley Gillin. The urgency and the fact that it was copied to multiple people suggest either:
- A wire was sent to the wrong recipient
- A compliance hold was being triggered
- Funds were being redirected at the last moment

### 7.5 The Indyke PLLC Nexus

Darren K. Indyke PLLC maintained **two separate accounts** at Deutsche Bank:
1. A "D" category account (balance: $116K-$440K)
2. An "M" category account (balance: ~$268K, very stable)

The stable M-account suggests a trust or escrow function. The volatile D-account suggests an operating account receiving and disbursing funds. Indyke was explicitly placed under the "SOUTHERN FINANCIAL RELATIONSHIP" alongside JEGE, INC -- confirming his accounts were treated as part of the Epstein entity network, not as an independent law practice account.

### 7.6 Bank Accounts Closing (2018)

Multiple references to "bank accounts closing" ([EFTA01376270](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01376270.pdf), [EFTA01387487](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01387487.pdf), [EFTA01430770](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01430770.pdf)) involving Darren Indyke, Stewart Oldfield, and Bradley Gillin suggest a coordinated closure:
- "Re: 2 bank accounts closing" ([EFTA01387487](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01387487.pdf))
- "accounts closing [C]" marked as confidential ([EFTA01430770](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01430770.pdf))
- "Securities offered thro[ugh]" in same email context -- suggesting securities were being liquidated as part of the closing process

### 7.7 Consolidated Financial Position (Estimated Peak)

| Entity | Estimated Peak Balance |
|--------|----------------------|
| THE HAZE TRUST | $49,460,098 |
| SOUTHERN TRUST COMPANY, INC. | $45,151,615 |
| SOUTHERN FINANCIAL LLC | $7,013,128 |
| GRATITUDE AMERICA, LTD | $2,075,025 |
| JEFFREY EPSTEIN (personal) | $4,378,298 |
| PLAN D, LLC | $789,558 |
| BUTTERFLY TRUST | $734,175 |
| LSJE, LLC | $501,906 |
| NES, LLC | $563,000 (est.) |
| JEGE, LLC | $463,079 |
| DARREN K. INDYKE PLLC (combined) | $708,659 |
| ZORRO MANAGEMENT, LLC | $464,683 |
| HBRK ASSOCIATES, INC | $418,599 |
| NEPTUNE, LLC | $366,478 |
| PLAN D, LLC | $326,685 |
| CRW 2009 LLC | $251,903 |
| PRYTANEE, LLC | $197,000 (est.) |
| HYPERION AIR, LLC | $147,204 |
| **ESTIMATED TOTAL** | **$113,000,000+** |

*Note: Not all entities reached peak simultaneously. This represents aggregate maximum across all observed accounts.*

---

## 8. COMPLIANCE AND REGULATORY FLAGS

### 8.1 AML Investigations

- **THE HAZE TRUST:** Subject of extensive AML inquiry -- Alert# SAM1788880 ([EFTA01369019](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01369019.pdf))
- **NEPTUNE, LLC:** "Periodic Review of High Risk" entity ([EFTA01378765](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01378765.pdf), [EFTA01386946](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01386946.pdf))
- **LSJE, LLC:** Combined GCIS review (GCIS#483882) ([EFTA01362517](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01362517.pdf))
- **2017 CATERPILLAR TRUST:** Case#13959886 ([EFTA01408771](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01408771.pdf))
- **SOUTHERN FINANCIAL LLC:** "2018 Periodic Review of Accts" ([EFTA01406280](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01406280.pdf))

### 8.2 The 25-Subject SAR Filing

The SAR at [EFTA01656524](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01656524.pdf) named 25 subjects in a single filing -- an extraordinary scope that indicates Deutsche Bank's compliance team ultimately viewed the entire network as suspicious. The SAR notes:
- "debits to account"
- "consist of two checks totaling $100"
- Reference to "Case LLP" -- possibly a legal matter

### 8.3 Daily Deposit Reports

RM0082289 Daily Deposit Reports were generated and sent to Stewart Oldfield, Bradley Gillin, Robert Dicerbo, and Arthur Tremblay ([EFTA01413851](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01413851.pdf)) -- indicating the account activity required daily monitoring.

---

## 9. ASSOCIATED INDIVIDUALS AND EXTERNAL CONNECTIONS

### 9.1 Key Personnel at Deutsche Bank
- **Jj Litchford** -- Primary account officer for ALL entities
- **Paul Morris** -- Secondary account officer for ALL entities
- **Stewart Oldfield** -- Day-to-day relationship manager
- **Bradley Gillin** -- Operations/compliance coordinator
- **Paul Barrett** -- Derivatives trader (PLN Rolls, Harvest CYES)
- **Martin Zeman** -- Trading support
- **Davide-A Sferrazza** -- Trading support
- **Xavier Avila** -- Trading support
- **Liam Osullivan** -- Involved in Southern Financial account issues
- **Joshua Shoshan** -- AML case handler
- **Cynthia Rodriguez** -- AML case handler

### 9.2 Key Personnel at Epstein Organization
- **Darren Indyke** -- Attorney, POA on accounts, account holder
- **Richard Kahn** -- CFO, authorized wire instructions
- **Brigid Macias** -- Operations (Caterpillar Trust funds, AFEX euros)

### 9.3 External Connections
- **Firstbank PR** (routing: 221571473) -- Multiple wires to Puerto Rico entities (LSJE, Nautilus)
- **Wells Fargo** (routing: 121000248) -- Wires to Zorro Development Corp
- **Citibank West** -- NES LLC Fedwire debit
- **Banco Popular PR** -- Multiple wires
- **Gulfstream Aerospace** -- Book transfer (aircraft purchase/maintenance)
- **International Jet Interiors** -- Fedwire (JEGE/aircraft interiors)
- **STRANGHAYES HOLDING** -- Book transfer recipient
- **Nautilus Inc** -- Fedwire via Firstbank PR
- **Bell Helicopter / Sikorsky** -- Aircraft purchases
- **Samantha K Harris** -- Book transfer recipient ($?)

---

## 10. CONCLUSIONS

### 10.1 Entity Structure and Opacity

The Epstein financial network at Deutsche Bank was a **hub-and-spoke structure** with multiple structural layers:

1. **Layer 1 (Hub):** Jeffrey Epstein personal account (DDA 739110438) served as the central clearing account
2. **Layer 2 (Primary Holdings):** Southern Trust ($45M) and The Haze Trust ($49M) held the bulk of assets
3. **Layer 3 (Operating Entities):** ~12 entities with $100K-$7M each handled specific functions (aviation, real estate, legal, property management)
4. **Layer 4 (Trust/Charitable):** Butterfly Trust and Gratitude America functioned as charitable/trust vehicles
5. **Layer 5 (Additional vehicles):** Caterpillar Trust, Prytanee LLC, Aviloop LLC, and others served specialized purposes

All entities were **managed by the same banker team**, **nested under a single "Southern Financial Relationship,"** and appeared on a **single consolidated balance report** -- meaning Deutsche Bank was fully aware these were not independent entities but a single coordinated operation.

### 10.2 Money Movement Patterns

- **Downward flow:** Assets in Southern Trust (Q30171005) were liquidated and sent to Epstein personal, then distributed to sub-entities
- **Lateral flow:** Book transfers and internal transfers moved money between entities without leaving the bank
- **Automatic sweeps:** Standing automatic transfer arrangements (Southern Financial $1.13M) maintained entity balances
- **External wires:** Fedwires to Puerto Rico (LSJE, Nautilus), Wells Fargo (Zorro), and Citibank (NES) moved money outside Deutsche Bank

### 10.3 The 2018 Wind-Down

The data strongly suggests a **coordinated wind-down in 2018:**
- The Haze Trust was drained from $49.5M to $2.5M between June and November 2018
- "Bank accounts closing" emails in 2018
- "Securities offered through" references in closing context
- Southern Trust declined from $45M (2016) to low millions by late 2018

This wind-down preceded Epstein's July 2019 arrest by approximately 6-12 months, raising the question of whether the drawdown was in anticipation of legal exposure.

---

## APPENDIX A: SOURCE DOCUMENT INDEX

| EFTA Number | Document Type | Key Content |
|-------------|--------------|-------------|
| [EFTA01359500](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01359500.pdf) | Account Roster | Full entity/banker assignment table |
| [EFTA01381029](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01381029.pdf) | Balance Report | Southern Trust $45.15M (09/30/16) |
| [EFTA01381103](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01381103.pdf) | Balance Report | Southern Trust $43.79M |
| [EFTA01381149](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01381149.pdf) | Balance Report | Full constellation, 08/17/18 |
| [EFTA01381246](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01381246.pdf) | Balance Report | Full constellation, 06/21/18 |
| [EFTA01413971](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01413971.pdf) | Balance Report | Partial constellation, 08/28/18 |
| [EFTA01414982](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01414982.pdf) | Transaction | Southern Financial AUTOMATIC TRNSFR |
| [EFTA01430750](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01430750.pdf) | Balance Report | Full constellation, late 2018 |
| [EFTA01430852](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01430852.pdf) | Balance Report | Haze Trust $49.2M, S.Fin $7.0M |
| [EFTA01430931](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01430931.pdf) | Balance Report | Full constellation, 11/14/18 |
| [EFTA01431991](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01431991.pdf) | Balance Report | Full constellation, 10/03/18 |
| [EFTA01427242](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01427242.pdf) | Relationship Map | Southern Financial Relationship structure |
| [EFTA01477330](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01477330.pdf) | Relationship Map | Southern Financial Relationship activation |
| [EFTA01477454](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01477454.pdf) | Banker Assignment | Morris/Oldfield full entity list |
| [EFTA01656524](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01656524.pdf) | SAR Filing | 25 subjects named |
| [EFTA01482909](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01482909.pdf)-01483039 | Bank Statements | DDA-to-DDA transfers from 739110438 |
| [EFTA01583582](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01583582.pdf) | Admin Tool | Southern Trust asset acct Q30171005 |
| [EFTA01425378](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01425378.pdf) | Email | Neptune $1200/$1000 wires |
| [EFTA01417218](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01417218.pdf) | Email | STOP WIRE FROM LSJE emergency |
| [EFTA01339374](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01339374.pdf) | Records | Helicopter 1029 LLC, Sikorsky S-76C |
| [EFTA01383964](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01383964.pdf) | Email | Returned funds to Caterpillar |
| [EFTA01430999](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01430999.pdf) | Email | Caterpillar Trust 2 accounts |
| [EFTA01388936](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01388936.pdf) | Email | Harvest Collateral Yield Enhancement Strategy |
| [EFTA01387049](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01387049.pdf) | Reference | www.harvestvolmgt.com |

---

---

## ADDENDUM: DS9/DS11 REVISIT FINDINGS (2026-02-12)

### Jeepers, Inc. -- The 19th Entity (Glenn Dubin Conduit)

DS11 reveals Jeepers, Inc. as a significant entity with $22-28M in assets and a direct financial connection to Glenn Dubin. Under an "Assignment of Economic Interest Agreement dated August 1, 2011," Dubin assigned his Fortress Value Recovery Fund interest to Jeepers (an Epstein entity). Kahn managed ongoing distributions: "per agreement all money goes to [Dubin] until he receives back the 4,375,302 he just sent to jeepers thereafter jeepers keeps 100% of all distributions" ([EFTA02359292](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02359292.pdf)). [EFTA00165822](https://www.justice.gov/epstein/files/DataSet%209/EFTA00165822.pdf) (DS9) confirms JEEPERSINC alongside other Epstein entities on Deutsche Bank trading authorization with account N4G024935.

### Multi-Bank Architecture (5+ Banks)

[EFTA02711200](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02711200.pdf) (DS11) reveals the entity network operated across at least 5 banks: Deutsche Bank (majority), First Bank (Puerto Rico), UBS, BNP Paribas, and Wells Fargo. Southern Trust held $70.8M at Deutsche Bank and $828K at First Bank. Jeepers held $22.7M at Deutsche Bank. The original report focused exclusively on Deutsche Bank.

### Haze Trust: Giacometti Sculpture ($18-27.5M)

DS11 reveals the Haze Trust also held a Giacometti sculpture ("Figure moyenne II") with a Christie's auction estimate of $18-25M ([EFTA02654666](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02654666.pdf)) and a guarantee offer of $20M ([EFTA02389513](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02389513.pdf)). A Braque and the Giacometti were purchased for $30M total but estimated at only $19-22M at resale, generating a $7-10M non-deductible personal loss ([EFTA02654984](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02654984.pdf)). Leon Black personally advised on Paris storage at Chenue warehouse ([EFTA02350093](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02350093.pdf)). His art advisor Heather Gray (Elysium Management) managed the sales.

### Caterpillar Trust: 2-Year GRAT

DS11 and DS9 reveal the Caterpillar Trust was a 2-year grantor retained annuity trust (GRAT) established January 3, 2017, with Lesley Groff and Daphne Wallace as trustees. Groff asked: "What is the Caterpillar Trust for?" Klein replied: "Asset that we should sell and need a bank account to park money" ([EFTA02238206](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02238206.pdf)). At closure (March 2019), $2.16M was moved to a new Butterfly Trust account at Morgan Stanley ([EFTA02636559](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02636559.pdf)). Trust instrument ([EFTA01255393](https://www.justice.gov/epstein/files/DataSet%209/EFTA01255393.pdf)) confirms termination clause directing balance to The 2013 Butterfly Trust.

### LSJE LLC: Personal Spending Vehicle

DS11 reveals LSJE was heavily used for personal purchases directed by Karyna Shuliak: Chinese furniture ($4,850 + $15,300, Heshan Ruihui), Balinese art (Miroku/Nikini Art Indonesia), Swiss finishing school tuition (Institut Villa Pierrefeu, 34,510 CHF), rattan furniture for St. Thomas, a pool for the USVI property, and a wire that bounced through Alfa Bank Russia ([EFTA02629919](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02629919.pdf)).

### Ariane de Rothschild: Contingent Fee to Southern Trust

[EFTA02493823](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02493823.pdf) (DS11): Epstein negotiated a contingent fee with Ariane de Rothschild: "ariane pays southern trust (my co). based on final settlement with DOJ. payment between 150-200 -- 5 million, 100-150. 10 million, under 100 25 million." Kathy Ruemmler (former Obama White House Counsel) provided legal advice on the structure. The reference to "rothschild baer" and a "liquidity event" suggests Epstein was advising on restructuring of the Edmond de Rothschild Group.

### Aviloop LLC: Nadia Marcinkova Financial Support

DS11 documents regular Aviloop wires from JEE personal accounts, a $50K furnished apartment ([EFTA02726121](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02726121.pdf)), income classification discussions ($43,876 since February 2018), and consideration for involvement in a Gulfstream IV sale ([EFTA02617189](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02617189.pdf), November 2018).

### Payroll Analysis: 116+ Employees, $9.5M/Year

[EFTA02397369](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02397369.pdf) (DS11): "JEE 2010 Payroll & Benefits Analysis" shows 12 entities employing 116+ people at $9.5M total. Island Grounds Inc. was the largest (69 employees, $2.8M). DKI PLLC (Darren K. Indyke) paid 2 employees $1.66M (averaging $832K each).

### Summary Table: Revised vs. Original Estimates

| Finding | Original Report | DS9/DS11 Revised |
|---------|----------------|------------------|
| Peak consolidated assets | ~$113M | $159M+ (Oct 2015); total portfolio $319M (Jun 2013) |
| Number of entities | 18 | 19+ (Jeepers Inc. added) |
| Southern Trust peak | $45.15M (Sep 2016) | $82.5M (Oct 2015) |
| Banking architecture | Deutsche Bank only | 5+ banks (DB, First Bank, UBS, BNP Paribas, Wells Fargo) |
| Haze Trust assets | Financial only | Financial + Giacometti ($18-27.5M) + Braque |
| Caterpillar Trust purpose | Unknown | 2-year GRAT; assets to Butterfly Trust at Morgan Stanley |
| LSJE LLC purpose | Operating entity | Personal spending vehicle for Karyna Shuliak |
| Replacement bank | Not discussed | LGT Bank Liechtenstein cultivated March 2019 |
| Total payroll | Not quantified | $9.5M/year across 116+ employees in 12 entities |
| Gratitude America | Charitable entity | Tax vehicle + $30K payment to NYT reporter Landon Thomas Jr. |
| Jeepers/Dubin | Not profiled | $4.375M backstop + ongoing distributions from Fortress |
| Ariane de Rothschild | Not mentioned | Contingent $5-25M fee to Southern Trust |

---

*This report is based solely on data extracted from the document text layers in the DOJ Epstein document production, supplemented by DS9/DS11 revisit findings (2026-02-12). OCR quality varies; some figures may contain minor transcription artifacts. All balances should be verified against original bank records where available.*

DATA QUALITY NOTE: A data quality audit confirmed that ~98% of 'bad_overlay' records in the redaction database are OCR noise from degraded scans, not text hidden behind removable redactions. Text searches against this corpus remain valid for identifying which documents mention specific terms.

**END OF REPORT**
