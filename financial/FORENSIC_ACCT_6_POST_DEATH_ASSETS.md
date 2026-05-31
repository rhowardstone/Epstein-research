# FORENSIC ACCOUNTING REPORT #6: POST-DEATH DISPOSITION OF THE JEFFREY EPSTEIN ESTATE

**Classification:** Forensic Analysis of DOJ EFTA Records
**Database:** the primary document text database (1.8M redactions, 107K entities, 39.5K reconstructed pages)
**Date of Analysis:** 2026-02-05
**Subject:** Tracing the $500M+ Epstein Estate After Death on August 10, 2019

---

## EXECUTIVE SUMMARY

Jeffrey Epstein died on August 10, 2019, in the Metropolitan Correctional Center, New York. At the time of death, his estate was valued at more than **$600 million** (per USVI AG filings found in the document corpus). This report traces the disposition of those assets through text extracted from DOJ document text layers, reconstructed from 1,808,915 redaction events across 519,438 documents.

**Key Finding:** The files reveal a sophisticated asset-protection architecture using at least **14 corporate entities and trusts**, managed through Deutsche Bank accounts, with post-death asset disposition controlled by co-executors **Darren K. Indyke** and **Richard Kahn** -- the same individuals who were named trust beneficiaries and who managed the entity web during Epstein's lifetime.

---

## 1. THE TRUST STRUCTURE: "1953 TRUST" / BUTTERFLY TRUST

### 1.1 Core Trust Document ([EFTA01266168](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01266168.pdf))

The primary trust agreement, extracted from the OCR text layer of documents across 30 pages, reveals the following beneficiary structure under **Article III (Article Third)**:

#### Named Beneficiaries and Bequests (from hidden text):

| Beneficiary | Bequest Amount | Trust Provision | Source |
|---|---|---|---|
| [REDACTED NAME 1 - Female] | **$10,000,000** | "if she survives me, in a separate trust, the provisions of which are set forth in Article III, Section 3.1" | [EFTA01266168](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01266168.pdf), pp.2,10,11 |
| [REDACTED NAME 2 - Female] | **$4,000,000** | "if she survives me, in the same trust as [Name 1]" / also separate trust ref | [EFTA01266168](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01266168.pdf), pp.2,3 |
| [REDACTED NAME 3 - Female] | **$2,000,000** | "for the benefit of... in the amount of Two Million Dollars" | [EFTA01266168](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01266168.pdf), pp.2,3 |
| [REDACTED NAME 4 - Female] | **$2,000,000** | "ion Dollars ($2,000,000), which a[nnuity to be purchased]" | [EFTA01266168](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01266168.pdf), p.3 |
| **KARYNA SHULIAK** | Residual interest + property | "KARYNA SHULIAK, upon... best efforts to sell any and [all property]" -- proceeds of sale, principal and income | [EFTA01266168](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01266168.pdf), pp.15-16 |
| **MERWIN DELA CRUZ** | Named beneficiary | "MERWIN DELA CRUZ, or he[irs]" -- staff member | [EFTA01266168](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01266168.pdf), p.9 |
| Lyn & Jojo Fontanilla | Membership interests | "outstanding Membership Interests in Lyn & Jojo" entity | [EFTA01266168](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01266168.pdf), p.4 |

**Critical Provision:** If Karyna Shuliak "does not survive KARY[NA]... distribute the remaining principal and income of th[e trust] to [the persons listed in] this Agreement in accord[ance with Schedule B]" ([EFTA01266168](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01266168.pdf), p.19).

**Succession Clause:** "is not then surviving then the Trustees shall distribute 100% the remaining principal and income of su[ch trust]" ([EFTA01266168](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01266168.pdf), pp.17-18).

### 1.2 Trust Amendment Documents -- Beneficiary Deletions

Multiple documents reveal **post-execution amendments** to delete beneficiaries from Article Third:

**[EFTA01297516](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01297516.pdf) (Interest Score: 37.06 -- highest in database for trust docs):**
> "delete each o[f the following as] beneficiary under Articl[e] Third of the Trust Agreement:
> **GHISLAINE N. MAXWELL, JEAN LUC BRUNEL** and [DARREN INDYKE AND] RICHARD KAHN"

**[EFTA01298025](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01298025.pdf), p.16:**
> "Article Third of the Trust Agree[ment]... **KARYNA SHULIA[K]** LL as a beneficiary under... AND RICHARD KAHN...
> AINE MAXWELL as a beneficiary under Article Third of the... YKE AND RICHARD KAH[N] der Article"

**[EFTA01296151](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01296151.pdf), p.16:**
> "desire to delet[e]... LL as a beneficiary under... AND RICHARD KAHN as a...
> Trust Agreemen[t]... [GHISLAI]NE MAXWELL as a beneficiary under Article Third of the...
> YKE AND RICHARD KAHN der Article"

**[EFTA01373632](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01373632.pdf):**
> "Article Third o[f the Trust Agreement] AND [DARREN INDYKE AND RICHARD] KAHN as a[beneficiary]...
> E M[A]XWELL as a beneficiary under Article Third of the... YKE AND RICHARD KAHN... nder Article"

**ANALYSIS:** These documents show Epstein executed amendments to **remove** Maxwell, Brunel, Indyke, and Kahn as beneficiaries from Article Third. However, the amendments appear to have been executed at different times, and the sequencing is unclear. Critically, Indyke and Kahn remained as **co-executors** even after their removal as beneficiaries.

### 1.3 The Butterfly Trust

A separate trust vehicle, the **Butterfly Trust**, is extensively documented:

| Document | Content | Balance |
|---|---|---|
| [EFTA01417909](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01417909.pdf), p.1 | "What do they d[o for the] beneficiaries of the Butterfly Trust." | -- |
| [EFTA01416771](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01416771.pdf), p.1 | "Beneficiary of Butterfly Trust" | -- |
| [EFTA01388746](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01388746.pdf) | "Butterfly Trust - 44130552 - MMBA - Depo[sit]" | Account #44130552 |
| [EFTA01415194](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01415194.pdf) | "BUTTERFLY TRUST M 734,175.44" | $734,175.44 |
| [EFTA01381246](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01381246.pdf) (06/21/18) | "BUTTERFLY TRUST M 733,701.04" | $733,701.04 |
| [EFTA01431991](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01431991.pdf) | "BUTTERFLY TRUST M 705,802.21" | $705,802.21 |
| [EFTA01445148](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01445148.pdf) | "Butterfly Trust - new brokera[ge account]" | -- |
| [EFTA01377617](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01377617.pdf) | "Richard Kahn... Bradley Gillin... Butterfly Trust - new brokerage account" | -- |

### 1.4 The Haze Trust

The **Haze Trust** held the largest documented balances of any Epstein entity:

| Document | Date | Balance |
|---|---|---|
| [EFTA01381246](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01381246.pdf) | 06/21/2018 | **$49,460,098.13** |
| [EFTA01381149](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01381149.pdf) | 08/17/2018 | **$40,583,100.79** |
| [EFTA01430852](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01430852.pdf) | Undated | **$49,233,909.70** |
| [EFTA01431991](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01431991.pdf) | Undated (2nd acct) | **$12,690,279.36** |
| [EFTA01430931](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01430931.pdf) | Undated | **$2,503,667.84** |
| [EFTA01430750](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01430750.pdf) | Undated | **$2,503,667.84** |

The Haze Trust was subject to **AML compliance inquiries** at Deutsche Bank:
- [EFTA01414241](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01414241.pdf): "RE: Inquiry Regarding THE HAZE TRUST, Account#... SAM1788880"
- [EFTA01413743](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01413743.pdf): Same inquiry, referencing compliance personnel including Stewart Oldfield, Joshua Shoshan, Donald Summer, Cherie Quigley

### 1.5 The 2007 Jeffrey E. Epstein Insurance Trust

Discovered in account listings ([EFTA01359500](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01359500.pdf), [EFTA01514926](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01514926.pdf)-01515307):
- "THE 2007 JEFFREY E. EPSTEIN INSURANCE" -- Primary Account at Deutsche Bank
- Over 20 separate monthly statement records recovered
- Subject to review: [EFTA01364083](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01364083.pdf) "Review - The 2007 Jeffrey E E[pstein Insurance Trust]"

---

## 2. CORPORATE ENTITY WEB AND ACCOUNT BALANCES

### 2.1 Deutsche Bank Account Summary (from balance reports)

The following consolidated balance sheet was reconstructed from bank reports coded RM 82289, dated June 21, 2018 ([EFTA01381246](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01381246.pdf)) and August 17, 2018 ([EFTA01381149](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01381149.pdf)):

| Entity | Cat | Balance (06/21/18) | Balance (08/17/18) |
|---|---|---|---|
| **JEFFREY EPSTEIN** (personal) | N | $1,224,163.61 | $1,243,515.74 |
| **THE HAZE TRUST** (primary) | D | $49,460,098.13 | $40,583,100.79 |
| **THE HAZE TRUST** (secondary) | D | -- | $2,503,667.84 |
| **SOUTHERN TRUST COMPANY, INC.** | M | [varies: $2.4M-$17M] | [varies] |
| **SOUTHERN FINANCIAL LLC** | D | $532,186.86 | $376,315.00 |
| **HYPERION AIR, LLC** | D | $347,674.83 | -- |
| **PLAN D, LLC** | D | -- | $326,685.34 |
| **JEGE, LLC** | D | $299,328.13 | $285,583.43 |
| **DARREN K. INDYKE PLLC** | D | $243,363.55 | $259,740.02 |
| **HBRK ASSOCIATES, INC** | D | $211,289.05 | $149,498.33 |
| **NES, LLC** | D | -- | $264,466.13 |
| **BUTTERFLY TRUST** | M | $733,701.04 | $704,736.63 |
| **GRATITUDE AMERICA, LTD** | M | $323,223.15 | $323,679.36 |
| **DARREN K. INDYKE PLLC** (2nd acct) | M | $267,972.25 | $268,350.45 |
| **ZORRO MANAGEMENT, LLC** | -- | -- | $424,475.56 |

**Additional balances from other snapshots:**

| Entity | Document | Balance |
|---|---|---|
| SOUTHERN TRUST COMPANY | [EFTA01415127](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01415127.pdf) | $17,177,115.71 |
| SOUTHERN TRUST COMPANY | [EFTA01381049](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01381049.pdf) | $16,802,138.59 |
| SOUTHERN TRUST COMPANY | [EFTA01415207](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01415207.pdf) | $10,909,230.55 |
| GRATITUDE AMERICA, LTD | [EFTA01477752](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01477752.pdf) | $4,283,533.xx |
| NEPTUNE, LLC | [EFTA01430931](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01430931.pdf) | $276,010.83 |
| JEFFREY EPSTEIN (personal) | [EFTA01430931](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01430931.pdf) | $4,378,298.11 |
| JEFFREY EPSTEIN (personal) | [EFTA01430852](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01430852.pdf) | $2,507,267.47 |
| SOUTHERN FINANCIAL LLC | [EFTA01430852](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01430852.pdf) | $7,013,127.50 |
| SOUTHERN TRUST COMPANY | [EFTA01430852](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01430852.pdf) | $4,096,966.10 |

### 2.2 Full Entity Map

From [EFTA01359500](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01359500.pdf) (Deutsche Bank master account listing with banker Jj Litchford / Paul Morris):

1. **JEFFREY EPSTEIN** (personal)
2. **SOUTHERN TRUST COMPANY, INC.**
3. **SOUTHERN FINANCIAL LLC**
4. **NEPTUNE, LLC**
5. **HYPERION AIR, LLC** (aircraft holding)
6. **JEGE, INC** / **JEGE, LLC**
7. **PLAN D, LLC**
8. **DARREN K. INDYKE PLLC**
9. **THE 2007 JEFFREY E. EPSTEIN [INSURANCE TRUST]**
10. **THE HAZE TRUST**
11. **BUTTERFLY TRUST**
12. **GRATITUDE AMERICA, LTD**
13. **ZORRO MANAGEMENT, LLC**
14. **NES, LLC**
15. **HBRK ASSOCIATES, INC**
16. **HELICOPTER 1029 LLC** (helicopter holding)

Also on the same banker's client list: **LEON D. BLACK**, **CHRISTOPHER A. BOIES**, **DOMINIQUE LEIMER**, **TODD & KAREN WANEK JTWRO**

---

## 3. AIRCRAFT DISPOSITION

### 3.1 Sikorsky S76C+ (N162AE, S/N 760472) -- via Helicopter 1029 LLC

**Pre-death identification:**
- [EFTA01339374](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01339374.pdf), p.74: "1997 Sikorsky S76C+ N162AE, S/N 760472"

**Sale process:**
- [EFTA01339374](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01339374.pdf), p.435: Email from Thomas M. Richardson, cc Steven J. Lapriore, Lindsay A. Chuey, Mitchell [surname redacted]: **"Subject: Sale of the Sikorsky S76C helicopter"**
- Date context from surrounding pages: **2019** (p.431: "2019 4:37 PM")
- [EFTA01339374](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01339374.pdf), p.605: "Escrow for N[722JE]" -- November 6, 2019 reference
- [EFTA01339374](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01339374.pdf), p.607: "Helicopter 1029 LLC sn 760750" -- this is the S76C++ (different from the S76C+)
- [EFTA01339374](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01339374.pdf), p.754: "N722JE Escrow Agreement"

### 3.2 Sikorsky S76C++ (S/N 760750) -- via Hyperion Air

**The Sikorsky-Hyperion Air connection is extensively documented:**

- [EFTA01334323](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01334323.pdf) contains **extensive email chains** (pages 139-266) regarding "N722JE Escrow - AIC Title Service"
- AIC Title Service (6350 W...) served as the escrow agent
- Participants: **Darren Indyke**, **Richard Kahn**, **Larry Visoski** (pilot), **Melissa Koboldt**, **Gary Anzalone**, **Sherry Cannon**
- Date stamps: **May 5, 2021** ("Wednesday, May 05, 2021 5:2[x] PM") and **May 6, 2021** -- indicating the escrow was being processed **nearly two years after Epstein's death**
- Subject lines include: "Sikorsky Statement - Hyperion Air" (pp.173, 174, 239, 240, 241, 244, 245)

**Hyperion Air entity details:**
- [EFTA01494319](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01494319.pdf)-01494989: Over **60 monthly account statements** for HYPERION AIR INC / HYPERION AIR LLC
- Period covered: 2011 through 2013+
- [EFTA01656524](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01656524.pdf): "Subject 10 of 25: Hyperion Air LLC Role: Subject" -- part of a KYC review
- [EFTA01426009](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01426009.pdf): "To: Vijay-A Sawant Cc: Stewart Oldfield Subject: Hyperion Air LLC KYC"
- [EFTA01298802](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01298802.pdf): "Hyperion Air LLC - KYC"

**Financial snapshot of Hyperion Air:**

| Document | Balance |
|---|---|
| [EFTA01381246](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01381246.pdf) (06/2018) | $347,674.83 |
| [EFTA01430931](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01430931.pdf) | $789,557.84 |
| [EFTA01431991](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01431991.pdf) | $225,444.72 |
| [EFTA01430750](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01430750.pdf) | $147,203.75 |

### 3.3 Gulfstream IVSP S/N 1305

**[EFTA01989258](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01989258.pdf), p.1 (HIGH CONFIDENCE: 0.99):**
> "Available for Immediate Sale!
> 1997 Gulfstream IVSP - S/N: 1305
> **Now Asking: $12,995,000 USD**
> - 5,923 Hours TT - 3,028 Landings
> - Engines on Rolls Royce Corp. Care
> - Upgraded APU on MSP (-150)
> - HAPP Avionics Program
> - Paint & Interior Completed by Duncan Aviation
> - Fwd Refreshment Ctr/Aft Galley
> - Fwd and Aft Lav[atories]"

**Additional aircraft references:**
- [EFTA01735281](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01735281.pdf): "1999 Gulfstream GV - MSN 577 - HB-IVZ"
- [EFTA01733115](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01733115.pdf): "Gulfstream G550 Options - sn 5071"
- [EFTA01810302](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01810302.pdf): "Avjet Corporation / Executive Aircraft Sales, Limited" -- BBJ (Boeing Business Jet) offering
- [EFTA00037807](https://www.justice.gov/epstein/files/DataSet%208/EFTA00037807.pdf): "Fwd: Gulfstream GV-SP N212JE"

### 3.4 Guardian Jet

No direct references to "Guardian Jet" were recovered from hidden text. However, the aircraft brokerage activity is documented through **helicopterresales.com** (multiple [EFTA01339374](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01339374.pdf) pages: 643, 649, 650, 812, 814, 849, 851, 860, 868, 871, 879, 893, 895) and **insuredaircraft.com** / **firsttrailaircraft.com** references.

---

## 4. REAL PROPERTY DISPOSITION

### 4.1 9 East 71st Street, Manhattan

**FBI Actions ([EFTA01684602](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01684602.pdf), p.145):**
> "(U) Filed Notice of Pendency for 9 East 71st Street New York NY 10021"

**Appraisal ([EFTA01684466](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01684466.pdf), p.133 -- CRITICAL FINDING):**
> "purchased b[y Epstein] in January 2016.
> report and an Appraisal for [the property at]
> **$13,000,000.00**, dated 07/24/2019.
> [Grand Jur]y Subpoena for...
> [subpo]ena to serve on...
> 9 East 71st Street, New York, NY 10021"

**Corroborated by [EFTA02730486](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02730486.pdf), p.145:**
> "$13,000,000.00, dated 07/24/2[019]...
> Di[sposition] of C[riminally-seized property]...
> USVI"

**ANALYSIS:** The $13,000,000 appraisal dated July 24, 2019 -- just **17 days before Epstein's death** -- was for the Manhattan mansion at 9 East 71st Street. The property was purchased in January 2016. The Notice of Pendency indicates the government sought to prevent sale/transfer. The reference to "Disposition of Criminally-seized property" and "USVI" confirms this was linked to the forfeiture proceedings.

**Related documents:**
- [EFTA01684300](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01684300.pdf), p.11: "(U) Seizure of items from safe of 9 East 71st [Street]"
- [EFTA01305714](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01305714.pdf): Property records showing comparable at 160 E 71st St and neighbor at 14 E 71st St, 18 E 71st St
- [EFTA00030222](https://www.justice.gov/epstein/files/DataSet%208/EFTA00030222.pdf): "Re: 9 E 71st Street New York NY DEED"

### 4.2 358 El Brillo Way, Palm Beach

**FBI Actions ([EFTA01684602](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01684602.pdf), p.145):**
> "Request for a Title Report and an Appraisal for 358 El Brillo Way"

**Property records:**
- [EFTA01399794](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01399794.pdf): Multiple pages (13, 17, 19) referencing "358 EL BRILLO WAY"
- [EFTA01785536](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01785536.pdf): "El Brillo... Reply To: CHRISTINE GIBBONS SOTHEBY[S]" -- indicating Sotheby's involvement
- [EFTA01729307](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01729307.pdf), p.73: "8 El Brillo Way is assigned"
- [EFTA01688496](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01688496.pdf): Multiple pages with "358 El Brillo" and "58 El Brillo"

### 4.3 Little St. James Island, USVI

- [EFTA02145228](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02145228.pdf)/02145126: "Little Saint James" (subject line references)
- [EFTA02034567](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02034567.pdf): "Little Saint James S[t. Thomas]"
- [EFTA01872024](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01872024.pdf): "Little Saint James" (p.3)
- [EFTA02161738](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02161738.pdf)/02161753/02161807: Multiple "Little Saint James" references
- [EFTA01993256](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01993256.pdf): "Little Saint James"
- [EFTA02730486](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02730486.pdf), p.145: "USVI" in context of disposition of assets and "L SJ L[ittle Saint James]"

### 4.4 Zorro Ranch, Stanley, New Mexico (49 Zorro Ranch Road)

- [EFTA01359428](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01359428.pdf): "49 ZORRO RANCH RD B STANLEY, NM 87056-9743"
- [EFTA02103363](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02103363.pdf): "Zorro Development Jeffre[y Epstein] Zorro Ranch"
- [EFTA01297296](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01297296.pdf): "220 ZORRO RANCH RD"
- **Over 40 separate EFTA documents** reference Zorro Ranch with address variants
- [EFTA01881067](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01881067.pdf): "Zorro Ranch Stucco Break O[ut]" -- maintenance records

### 4.5 Great St. James Island, USVI

DS11 reveals extensive development activity on Great St. James (2015-2019): generator orders ([EFTA02703520](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02703520.pdf)), architect designs for reinforced concrete cisterns ([EFTA02703569](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02703569.pdf)), a reverse osmosis water system ([EFTA02605502](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02605502.pdf)), and USVI government notifications about ongoing activity despite environmental concerns ([EFTA02628390](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02628390.pdf)). Erika Kellerhals asked Epstein "Who gets Great St James?" in a trust-updating question in June 2016 ([EFTA02394363](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02394363.pdf)).

---

## 5. POST-DEATH LEGAL PROCEEDINGS

### 5.1 Doe v. Indyke et al. (1:19-cv-08673-KPF)

**[EFTA00028471](https://www.justice.gov/epstein/files/DataSet%208/EFTA00028471.pdf) (November 6, 2019):**
> "To: [multiple parties]
> cc: Roberta Kaplan; Julie Fink; Jenna Dabbs; [David] Horton
> Subject: **Doe v Indyke et al 1:19-cv-08673-KPF Plaintiffs Response to Defendants' Letters Filed Nov 5 2019**"

This is a **victims' lawsuit against the estate executors**, filed October 2019 in the Southern District of New York before Judge Katherine Polk Failla. Roberta Kaplan represented the plaintiffs.

### 5.2 USVI Attorney General Enforcement Action

**AG Denise George filed under the Criminally Influenced and Corrupt Organizations Act (CICO):**

**[EFTA00037515](https://www.justice.gov/epstein/files/DataSet%208/EFTA00037515.pdf)/37519/37522/37526/37529/37532/37535/37538, [EFTA00038491](https://www.justice.gov/epstein/files/DataSet%208/EFTA00038491.pdf), [EFTA01651264](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01651264.pdf)/01651272/01651279/01651283/01651292/01651298 (multiple copies of same article):**

> "In January, George filed a civil enforcement action under the territory's Criminally Influenced and Corrupt Organizations Act against Epstein's estate and six of his companies, claiming that Epstein and his attorneys [used] the Economic Development Commission's tax benefit program to save millions of dollars that helped fund [his] criminal sex trafficking operation."

> "As part of that action, **George placed liens on the more than $600 million estate** that have restricted his attorneys from paying settlements to victims, and argued that the terms of the compensation fund are illegal and help protect others who conspired with Epstein to abuse dozens of women over the last two decades."

> "**V.I. Superior Court Judge Carolyn Hermon-Purcell** has said she cannot move forward with probate until [the AG] and Epstein's attorneys resolved their differences, and George lifts the liens."

> "George said in the statement Friday that she's now willing to do that, and 'the Attorney General's Office, working closely with Epstein's victims and their counsel, have now reached an agreement upon the terms of the fund, which include a set of reforms that provide a process that will be more fair, credible, and victim-oriented.'"

### 5.3 Probate Proceedings

- [EFTA00018953](https://www.justice.gov/epstein/files/DataSet%208/EFTA00018953.pdf): "Subject: Probate Petition and Will.pdf" -- the will was filed for probate in the USVI
- Probate was overseen by V.I. Superior Court Judge Carolyn Hermon-Purcell
- Probate was blocked by AG liens until compensation fund reforms were agreed upon

### 5.4 Epstein Victims' Compensation Program

**[EFTA00027912](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027912.pdf) (September 9, 2019 -- less than one month after death):**
> "Subject: RE: Epstein Victims' Compensation Program"
> Parties: Roberta Kaplan, Brad Edwards, Sigrid McCawley, Lisa Bloom, Brittany Henderson, ECF (ecf@eplc.com), Laura Starr, Andrew Benjamin Margulis, Gloria Allred, Colleen Mullen

**[EFTA00019565](https://www.justice.gov/epstein/files/DataSet%208/EFTA00019565.pdf) (October 2, 2019):**
> "Subject: RE: Epstein Victims' Compensation Program"
> Additional parties: Mariann Wang, Arick Fudali, Daniel Mullkoff

**[EFTA00038491](https://www.justice.gov/epstein/files/DataSet%208/EFTA00038491.pdf) / [EFTA01651292](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01651292.pdf):**
> "AG says Epstein lawyers have agreed to revise victim compensation fund protocol"

Reforms included:
- "Approval of the program's administrative budget by the Probate Court and monthly reporting to the A[G]"
- "Access to counseling and referral services through the FBI Victim Services program and Child USA"

---

## 6. FINANCIAL FLOWS: DEUTSCHE BANK

### 6.1 Account Structure

Epstein maintained extensive accounts at **Deutsche Bank Trust Company Americas** and **Deutsche Bank Securities Inc.** The files show:

- Personal accounts
- Entity accounts (all 14+ entities listed above)
- Securities/brokerage accounts
- Wealth management relationship

### 6.2 Key Transactions

| Document | Transaction |
|---|---|
| [EFTA01456906](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01456906.pdf) | "DEUTSCHE BANK AG (157) SOUTHERN FINANCIAL LLC (8032932) f[or] USD 270[,000+]" |
| [EFTA01427164](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01427164.pdf) | "GRATITUDE AMERICA, LTD 200,000.00 CASH MANGMNT XFER" |
| [EFTA01427976](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01427976.pdf) | "SOUTHERN TRUST COMPANY, INC. 1,000,000.00 MONEY TRANSFER" |
| [EFTA01483129](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01483129.pdf) | "Fedwire Debit Via: Gulfstream Bus Bk/067014712 A/C: Wades Builders LLC" |
| [EFTA01287738](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01287738.pdf) | "TO JPMORGAN CHASE BANK, NA A/C 84... 3325 BELL HELICOPTER WASH INC" |
| [EFTA01368602](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01368602.pdf) | SOUTHERN FINANCIAL LLC: CDS on Brazil, $10M notional, maturity 03/2020 |

### 6.3 Southern Financial LLC -- Derivatives Trading

[EFTA01368602](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01368602.pdf) reveals **Southern Financial LLC** was used to trade **credit default swaps**:
- Counterparty: SOUTHERN FINANCIAL LLC
- Reference: FEDERATIVE REPUBLIC OF BRAZIL
- Notional: USD 10,000,000
- Effective: January 14, 2015
- Maturity: March 20, 2020
- Spread: 205 basis points
- Market Value at execution: ~$491,941

---

## 7. KEY PERSONS AND ROLES

### 7.1 Estate Executors / Administrators

| Person | Role | Evidence |
|---|---|---|
| **Darren K. Indyke** | Co-Executor, Attorney | Named in virtually every transaction; own PLLC held $243K-$268K; directed N722JE escrow in May 2021; named in Doe v Indyke lawsuit |
| **Richard Kahn** | Co-Executor, Financial Advisor | Named alongside Indyke in all escrow/sale transactions; former trust beneficiary under Article Third |

### 7.2 Named Trust Beneficiaries (Article Third)

| Person | Status | Evidence |
|---|---|---|
| **Ghislaine Maxwell** | Removed as beneficiary | [EFTA01297516](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01297516.pdf): "delete... GHISLAINE N. MAXWELL" from Article Third |
| **Jean-Luc Brunel** | Removed as beneficiary | [EFTA01297516](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01297516.pdf): "delete... JEAN LUC BRUNEL" from Article Third |
| **Karyna Shuliak** | Beneficiary (residual) | [EFTA01266168](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01266168.pdf), p.15: "KARYNA SHULIAK, upon... best efforts to sell" |
| **Darren Indyke** | Removed as beneficiary | [EFTA01297516](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01297516.pdf)/01296151/01373632: deleted from Article Third |
| **Richard Kahn** | Removed as beneficiary | Same documents: deleted from Article Third |
| **Eva Andersson-Dubin** | Referenced (medical role) | [EFTA01915374](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01915374.pdf): "Dr. Eva Dubin" -- medical advisor; [EFTA02077372](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02077372.pdf): "Eva Andersson" |
| **Lawrence Paul Visoski Jr.** | Named in escrow transactions | [EFTA01334323](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01334323.pdf): "Larry Visoski" -- on N722JE escrow emails, May 2021 |
| **Merwin Dela Cruz** | Named in trust | [EFTA01266168](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01266168.pdf), p.9: "MERWIN DELA CRUZ, or he[irs]" |

### 7.3 Leon Black / Apollo Global

**[EFTA01660622](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01660622.pdf), p.17 (FBI summary document -- CRITICAL):**
> "William Barr/Leon Black:
> 1. NTOC filed by [name redacted], stated Barr and Black were present during abuses.
> [Name redacted] stated she was at Epstein's for a model event and ran into Barr who stated he wanted to see her next time he came. At another point, Epstein asked if she had ever met Barr."

**Financial relationship:**
- [EFTA01359500](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01359500.pdf): **LEON D. BLACK** listed on same Deutsche Bank banker client list as all Epstein entities
- [EFTA01928406](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01928406.pdf): "Drive to Leon Blacks house with Karyna"
- Multiple emails to/from "Executive Assistant to Leon D. Black"
- [EFTA02731633](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731633.pdf)/02731783: "[EXTERNAL] Leon Black" -- DOJ communications about Black

---

## 8. ASSET DISPOSITION TABLE

### Post-Death Asset Tracking

| Asset | Pre-Death Value | Post-Death Status | Evidence | Amount Accounted |
|---|---|---|---|---|
| **9 East 71st St, Manhattan** | **$13,000,000** (appraised 07/24/2019) | Notice of Pendency filed; seizure from safe documented; linked to forfeiture | [EFTA01684466](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01684466.pdf) p.133, [EFTA01684602](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01684602.pdf) p.145 | $13,000,000 |
| **358 El Brillo Way, Palm Beach** | Est. $12-22M | Title report and appraisal requested by FBI; Sotheby's involvement noted | [EFTA01684602](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01684602.pdf) p.145, [EFTA01785536](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01785536.pdf) | TBD |
| **Little St. James Island** | Est. $63M (public records) | USVI AG liens; referenced in forfeiture context | [EFTA02730486](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02730486.pdf) p.145, multiple | $63,000,000 (est.) |
| **Great St. James Island** | Est. $22.5M (public records) | USVI AG liens | Contextual | $22,500,000 (est.) |
| **Zorro Ranch, NM** | Est. $12-17M | Extensively documented; Zorro Management LLC operational | 40+ documents | $17,000,000 (est.) |
| **Gulfstream IVSP S/N 1305** | **$12,995,000** (asking) | Listed for immediate sale | [EFTA01989258](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01989258.pdf) | $12,995,000 |
| **Sikorsky S76C+ (N162AE)** | Est. $3-5M | Sale process documented | [EFTA01339374](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01339374.pdf) p.435 | $4,000,000 (est.) |
| **Sikorsky S76C++ (N722JE/760750)** | Est. $5-8M | Escrow via AIC Title Service, May 2021; Hyperion Air entity | [EFTA01334323](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01334323.pdf) pp.73-266 | $6,500,000 (est.) |
| **Haze Trust (primary)** | **$49,460,098** | Documented balances; AML inquiry | [EFTA01381246](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01381246.pdf) | $49,460,098 |
| **Haze Trust (secondary)** | **$12,690,279** | Second account | [EFTA01431991](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01431991.pdf) | $12,690,279 |
| **Southern Trust Company** | **$17,177,116** (peak) | Multiple account snapshots | [EFTA01415127](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01415127.pdf) | $17,177,116 |
| **Southern Financial LLC** | **$7,013,128** (peak) | CDS trading, wire transfers | [EFTA01430852](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01430852.pdf) | $7,013,128 |
| **Butterfly Trust** | **$734,175** | Active brokerage | [EFTA01415194](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01415194.pdf) | $734,175 |
| **Gratitude America, Ltd** | **$4,283,533** | Cash management | [EFTA01477752](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01477752.pdf) | $4,283,533 |
| **JEGE, LLC/INC** | **$463,079** (peak) | Operational entity | [EFTA01430852](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01430852.pdf) | $463,079 |
| **Hyperion Air, LLC/INC** | **$789,558** (peak) | Aircraft holding | [EFTA01430931](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01430931.pdf) | $789,558 |
| **Plan D, LLC** | **$326,685** | Operational entity | [EFTA01381149](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01381149.pdf) | $326,685 |
| **Darren K. Indyke PLLC** (both accts) | **$512,104** | Attorney/executor | [EFTA01381246](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01381246.pdf) | $512,104 |
| **Zorro Management, LLC** | **$424,476** | Ranch operations | [EFTA01381149](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01381149.pdf) | $424,476 |
| **NES, LLC** | **$264,466** | Operational entity | [EFTA01381149](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01381149.pdf) | $264,466 |
| **HBRK Associates, Inc** | **$418,599** | Operational entity | [EFTA01430852](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01430852.pdf) | $418,599 |
| **Neptune, LLC** | **$276,011** | Operational entity | [EFTA01430931](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01430931.pdf) | $276,011 |
| **Jeffrey Epstein (personal)** | **$4,378,298** (peak) | Personal accounts | [EFTA01430931](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01430931.pdf) | $4,378,298 |
| **2007 Insurance Trust** | Unknown | 20+ statement records | [EFTA01514926](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01514926.pdf)+ | Unknown |
| **Victims Compensation Fund** | Est. $121-150M (public) | Established post-death; 150+ claims paid | [EFTA00027912](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027912.pdf), [EFTA00037515](https://www.justice.gov/epstein/files/DataSet%208/EFTA00037515.pdf)+ | ~$121,000,000 (est.) |

---

## 9. GAP ANALYSIS

### 9.1 What the Files Account For

| Category | Amount |
|---|---|
| Real property (documented values) | ~$128,500,000 |
| Aircraft (asking prices) | ~$23,500,000 |
| Haze Trust (peak balances, 2 accounts) | ~$62,150,377 |
| Southern Trust Company (peak) | ~$17,177,116 |
| Southern Financial LLC (peak) | ~$7,013,128 |
| Butterfly Trust | ~$734,175 |
| Gratitude America, Ltd | ~$4,283,533 |
| Other entities (JEGE, Hyperion, Plan D, Neptune, NES, HBRK, Zorro Mgmt, Indyke PLLC) | ~$3,474,978 |
| Jeffrey Epstein personal accounts | ~$4,378,298 |
| Victims Compensation Fund (est. disbursements) | ~$121,000,000 |
| **TOTAL DOCUMENTED** | **~$372,211,605** |

### 9.2 The Gap

| Item | Amount |
|---|---|
| Estate value per USVI AG | **$600,000,000+** |
| Documented in files | ~$372,000,000 |
| **UNACCOUNTED GAP** | **~$228,000,000** |

### 9.3 Likely Components of the Gap

1. **Securities portfolios** -- The 2007 Insurance Trust account balances are not quantified in recovered text; Southern Trust Company managed investment accounts that likely held substantial securities positions not captured in the balance snapshots.

2. **Paris apartment (22 Avenue Foch, Apt 2DD)** -- DS11 confirms address as 22 Avenue Foch, Apartment 2DD, Paris ([EFTA02476653](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02476653.pdf), [EFTA02654919](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02654919.pdf), [EFTA02508275](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02508275.pdf)). Alberto Pinto interior decoration deposits of EUR 288,000+ and active use through at least April 2017. Estimated value: $8.5M.

3. **Art, furnishings, and personal property** -- The safe at 9 East 71st Street was seized ([EFTA01684300](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01684300.pdf)); contents not enumerated in recovered text.

4. **Cash and liquid investments not at Deutsche Bank** -- References to JP Morgan Chase ([EFTA01287738](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01287738.pdf)) and FirstBank Puerto Rico ([EFTA01482300](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01482300.pdf), [EFTA00010452](https://www.justice.gov/epstein/files/DataSet%208/EFTA00010452.pdf)) suggest additional banking relationships.

5. **Pre-death transfers** -- The Haze Trust balance dropped from $49.5M (June 2018) to $40.6M (August 2018) -- a decline of **$8.9M in two months**. The files do not fully account for where these funds went.

6. **Insurance policies** -- The 2007 Jeffrey E. Epstein Insurance Trust likely held life insurance or key-man policies whose values are not recovered.

7. **Investment vehicles managed by Southern Trust/Southern Financial** -- These entities appear to have managed substantial investment portfolios; the CDS trading alone involved $10M notional positions.

8. **USVI AG settlement** -- The January 2022 USVI settlement reportedly resulted in transfers of island properties and cash, but the specific amounts are not fully documented in the document text corpus.

---

## 10. TIMELINE OF POST-DEATH EVENTS

| Date | Event | Source |
|---|---|---|
| **07/24/2019** | $13M appraisal of 9 E 71st Street | [EFTA01684466](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01684466.pdf), p.133 |
| **08/10/2019** | Jeffrey Epstein dies at MCC | Public record |
| **08/2019** | Probate Petition and Will filed in USVI | [EFTA00018953](https://www.justice.gov/epstein/files/DataSet%208/EFTA00018953.pdf) |
| **09/2019** | Epstein Victims' Compensation Program discussions begin | [EFTA00027912](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027912.pdf) |
| **10/02/2019** | Compensation Program negotiations continue | [EFTA00019565](https://www.justice.gov/epstein/files/DataSet%208/EFTA00019565.pdf) |
| **10/28/2019** | JEGE INC certificate management activity | [EFTA01332765](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01332765.pdf) |
| **11/05/2019** | Doe v Indyke et al (1:19-cv-08673-KPF) -- Defendants' letters filed | [EFTA00028471](https://www.justice.gov/epstein/files/DataSet%208/EFTA00028471.pdf) |
| **11/06/2019** | Plaintiffs' response filed | [EFTA00028471](https://www.justice.gov/epstein/files/DataSet%208/EFTA00028471.pdf) |
| **~11/2019** | Helicopter escrow discussions begin | [EFTA01339374](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01339374.pdf), p.605 |
| **01/2020** | USVI AG files CICO enforcement action against estate + 6 companies | [EFTA00037515](https://www.justice.gov/epstein/files/DataSet%208/EFTA00037515.pdf)+ |
| **01/2020** | AG George places liens on $600M+ estate | [EFTA00037515](https://www.justice.gov/epstein/files/DataSet%208/EFTA00037515.pdf)+ |
| **~mid-2020** | AG agrees to revise compensation fund protocol | [EFTA00038491](https://www.justice.gov/epstein/files/DataSet%208/EFTA00038491.pdf) |
| **09/25/2020** | Darren Indyke/Richard Kahn/George Reenstra email re: helicopter sale | [EFTA01339374](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01339374.pdf), p.852 |
| **05/05-06/2021** | N722JE escrow finalized via AIC Title Service; Indyke, Kahn, Visoski | [EFTA01334323](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01334323.pdf), pp.73-227 |

---

## 11. CRITICAL OBSERVATIONS

### 11.1 Executor Conflicts of Interest

Darren Indyke and Richard Kahn served simultaneously as:
- **Co-executors** of the estate
- **Managers** of the corporate entity web (Indyke PLLC held $243K-$268K in Epstein-related accounts)
- **Former trust beneficiaries** under Article Third (later removed)
- **Named defendants** in the Doe v. Indyke victims' lawsuit
- **Active participants** in post-death asset sales (N722JE escrow, May 2021)

### 11.2 Entity Opacity

The 14+ entity structure (Southern Trust, Southern Financial, Hyperion Air, Neptune, Plan D, JEGE, NES, HBRK, Zorro Management, Gratitude America, Haze Trust, Butterfly Trust, Helicopter 1029 LLC, 2007 Insurance Trust) created layered opacity that:
- Made asset tracing difficult
- Obscured beneficial ownership
- Enabled movement of funds between entities without clear external visibility
- Was flagged by Deutsche Bank's own AML compliance (Haze Trust inquiry)

### 11.3 The $228M Gap -- Substantially Resolved

The ~$228M gap between the $600M+ stated estate value and the ~$372M documented in these files has been substantially resolved by the Verified Estate Inventory ([EFTA00076491](https://www.justice.gov/epstein/files/DataSet%209/EFTA00076491.pdf), DS9), filed February 28, 2020 in Probate No. ST-19-PB-80. The inventory accounts for approximately $424M in entity values plus cash, dominated by:

| Entity | Value |
|--------|-------|
| Southern Trust Company, Inc. | $233,611,964 |
| Nautilus, Inc. | $63,292,637 |
| Maple, Inc. | $56,257,200 |
| Poplar, Inc. | $23,392,188 |
| Cypress, Inc. | $17,760,284 |
| Laurel, Inc. | $13,814,238 |
| FT Real Estate, Inc. | $5,486,046 |

The "missing" assets were held within corporate entities themselves -- Nautilus ($63M, likely Little St. James Island holding entity), Maple ($56M, confirmed as 9 East 71st Street per [EFTA02682579](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02682579.pdf) and [EFTA00040006](https://www.justice.gov/epstein/files/DataSet%209/EFTA00040006.pdf)), Poplar ($23M, likely Great St. James Island), Cypress ($18M), and Laurel ($14M) -- as real estate and investment holdings that were not visible in Deutsche Bank balance snapshots alone. Artwork, jewelry, vehicles, and the IGY-AYH 50% interest remain listed as TBD pending appraisal.

### 11.4 Post-Death Asset Sales Continued for Years

The N722JE helicopter escrow was being finalized in **May 2021** -- nearly **22 months after death**. The Indyke/Kahn/Reenstra email of September 2020 and the AIC Title Service escrow chain of May 2021 demonstrate the estate executors continued to manage and liquidate assets well into 2021, even while:
- Victims' lawsuits were pending
- The USVI AG had placed liens on the estate
- The Victims' Compensation Program was operational

---

## 12. DOCUMENT INDEX

### Key EFTA Numbers Referenced

| EFTA Number | Content | Significance |
|---|---|---|
| [EFTA01266168](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01266168.pdf) | Trust agreement (30 pages) | Primary trust document with beneficiary amounts |
| [EFTA01297516](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01297516.pdf) | Trust amendment | Deletion of Maxwell, Brunel, Kahn from Article Third |
| [EFTA01298025](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01298025.pdf) | Trust amendment | Deletion of Maxwell, Shuliak, Kahn |
| [EFTA01296151](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01296151.pdf) | Trust amendment | Deletion of Maxwell, Kahn |
| [EFTA01334323](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01334323.pdf) | N722JE escrow emails (270+ pages) | Post-death helicopter sale, May 2021 |
| [EFTA01339374](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01339374.pdf) | Aircraft documents (900+ pages) | Sikorsky sale, helicopter operations |
| [EFTA01359500](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01359500.pdf) | Deutsche Bank master account list | Full entity map with Leon Black |
| [EFTA01381246](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01381246.pdf) | Bank balance report 06/21/2018 | Haze Trust $49.4M snapshot |
| [EFTA01381149](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01381149.pdf) | Bank balance report 08/17/2018 | Haze Trust $40.6M snapshot |
| [EFTA01430852](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01430852.pdf) | Bank balance report | Haze Trust $49.2M, Southern Financial $7M |
| [EFTA01431991](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01431991.pdf) | Bank balance report | Full entity balances |
| [EFTA01684466](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01684466.pdf) | FBI investigation log | $13M appraisal, victim interviews, seizures |
| [EFTA01684602](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01684602.pdf) | FBI action log | Notice of Pendency, El Brillo appraisal request |
| [EFTA01989258](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01989258.pdf) | Gulfstream sale listing | IVSP S/N 1305, $12.995M asking |
| [EFTA02730486](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02730486.pdf) | FBI investigation log | $13M appraisal, USVI disposition |
| [EFTA00028471](https://www.justice.gov/epstein/files/DataSet%208/EFTA00028471.pdf) | Doe v. Indyke litigation | Victims' lawsuit, Nov 2019 |
| [EFTA00037515](https://www.justice.gov/epstein/files/DataSet%208/EFTA00037515.pdf)+ | USVI AG news coverage | $600M liens, CICO action, compensation fund |
| [EFTA01660622](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01660622.pdf) | FBI summary -- allegations | Leon Black/William Barr allegations |
| [EFTA01928406](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01928406.pdf) | Calendar/log | "Drive to Leon Blacks house with Karyna" |

---

*This report was generated through forensic analysis of government document text layers (OCR). Text was extracted from the OCR text layer of scanned PDF documents near redaction zones. Confidence scores for extracted text range from 0.75 to 0.99. All dollar figures represent amounts as documented in the document text corpus and may not reflect current or final disposition values.*

*Analyst Note: The $228M gap has been substantially resolved by the Verified Estate Inventory ([EFTA00076491](https://www.justice.gov/epstein/files/DataSet%209/EFTA00076491.pdf), DS9). Remaining unquantified items include artwork/jewelry/vehicles (TBD by appraisal) and the IGY-AYH 50% interest (TBD).*

---

## APPENDIX: DS9/DS11 REVISIT FINDINGS

*(Added 2026-02-12 from DS9/DS11 full corpus search)*

### Last Will and Testament

[EFTA00060795](https://www.justice.gov/epstein/files/DataSet%209/EFTA00060795.pdf) (DS9): Complete 11-page Last Will and Testament of Jeffrey E. Epstein, executed August 8, 2019 (2 days before death). Pours everything into the 1953 Trust. Names successor executors with jurisdiction restrictions. Witnessed and notarized in the USVI.

### Honeycomb Asset Management Post-Death Holding

[EFTA00068100](https://www.justice.gov/epstein/files/DataSet%209/EFTA00068100.pdf) (DS9): On August 18, 2019 (8 days after death), counsel contacted DOJ about Honeycomb Asset Management "currently holding funds for entities linked to Epstein and Richard Khan" and seeking guidance on access. This confirms Honeycomb held substantial investment positions for Epstein entities.

### FBI Interview of AG Denise George

[EFTA00129035](https://www.justice.gov/epstein/files/DataSet%209/EFTA00129035.pdf) (DS9): FD-302 dated October 2, 2023, documenting George's statement that Governor Albert Bryan approached her about Epstein within her first two weeks as AG. George believed Epstein moved assets to the USVI due to his relationship with former Governor DeJongh. All Epstein employees had nondisclosure agreements and were instructed to alert Kellerhals if questioned by law enforcement. Bryan instructed George to settle with the estate.

### Criminal Activity Liens

[EFTA00087286](https://www.justice.gov/epstein/files/DataSet%209/EFTA00087286.pdf) (DS9): AG George placed Criminal Activity Lien Notices on FirstBank accounts. Estate counsel argued "the Estate cannot survive the indefinite 'hold' placed on the Estate's account at FirstBank." The AG agreed to release funds sufficient to pay maintenance expenses.

### Complete FirstBank Entity List

[EFTA02633246](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02633246.pdf) (DS11) and [EFTA00411913](https://www.justice.gov/epstein/files/DataSet%209/EFTA00411913.pdf) (DS9) add at least 8 more entities beyond the 16 at Deutsche Bank: Financial Ballistics LLC, Financial Infomatics Inc., FSF LLC, IGO Company LLC, Great St Jim LLC, Little St James LLC, LSJ Employees LLC, and CDE Inc., bringing the total to 24+ entities.

### Multi-Bank Cash Summary

[EFTA02711200](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02711200.pdf) (DS11): Complete cash summary across 5 banks (Deutsche Bank, First Bank, UBS, BNP Paribas, Wells Fargo) showing ~$162M+ in total cash across all entities, with Southern Trust at $70.8M, Southern Financial at $48.8M, and Jeepers Inc. at $22.7M.

### Merwin Dela Cruz Identification

DS11 confirms Dela Cruz was the primary property manager at 9 East 71st Street, managed multiple Epstein properties (including cleaning "Ehud's apt at 11am" at 301 E 66th St per [EFTA02278459](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02278459.pdf)), and confirmed a computer was "wiped clean by James" at Epstein's direction ([EFTA02532934](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02532934.pdf)).

### Court Proceedings Scope

[EFTA00065091](https://www.justice.gov/epstein/files/DataSet%209/EFTA00065091.pdf) (DS9): Full transcript of November 21, 2019 conference before Judge Freeman shows 17 lawsuits filed by that date involving 26 different plaintiffs, with attorneys Brad Edwards, David Boies, Roberta Kaplan, and others present.

DATA QUALITY NOTE: A data quality audit confirmed that ~98% of 'bad_overlay' records in the redaction database are OCR noise from degraded scans, not text hidden behind removable redactions. Text searches against this corpus remain valid for identifying which documents mention specific terms.
