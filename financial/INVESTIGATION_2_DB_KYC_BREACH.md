# INVESTIGATION LINE 2: DEUTSCHE BANK KYC BREACH TIMELINE

## Forensic Analysis of the Southern Financial LLC / Jeffrey Epstein Know Your Customer (KYC) Compliance Failure

**Investigator:** Independent Forensic Researcher
**Database:** the primary document text database (1,808,915 redactions; 107,422 extracted entities; 39,588 reconstructed pages)
**Date of Report:** 2026-02-05
**Classification:** Investigative Working Document

---

## EXECUTIVE SUMMARY

This investigation reconstructs the internal Deutsche Bank (DB) compliance timeline surrounding the Know Your Customer (KYC) breach for **Southern Financial LLC** (internal code: **SOUTHFINANMD**), an Epstein-controlled entity. Analysis of text extracted from OCR layers of DOJ production documents reveals that DB's AML/KYC compliance apparatus identified a KYC breach on or around **April 16, 2018**, triggering an escalation chain involving at least 10 named compliance personnel. Despite this formal breach identification, DB had been servicing the Epstein relationship since **August 26, 2013** -- and critically, **continued servicing the accounts for months after the breach was formally identified**. The bank was not fined until **July 2020** ($150M by NYDFS), more than two years after the internal breach discovery.

The evidence establishes that DB maintained the Epstein banking relationship for approximately **five years** (2013-2018) despite:
- An initial RDC (Reputational Due Diligence Check) alert on Jeffrey Epstein generated as early as **May 29, 2013** -- before the Southern Financial account was even fully onboarded
- Multiple KYC case reviews that were escalated, reassigned, and delayed
- A formal KYC breach declaration in **April 2018**
- Continued account activity (including credit derivatives trading with notional values of USD 10mm+) throughout the breach period

---

## METHODOLOGY

All findings derive from text extracted from document text layers in DOJ-produced PDF documents, cross-referenced with extracted entities and reconstructed page content. EFTA numbers serve as unique document identifiers. Confidence scores for OCR recovery are noted where relevant.

---

## CHRONOLOGICAL TIMELINE

### Phase 1: Account Opening and Initial Red Flags (2013)

#### May 29, 2013 -- First KYC/AML Alert Generated
- **[EFTA01355649](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01355649.pdf)** (p.0): `PWMUS AMLKYCklb 05/29/2013 11 43 AM`
- The DB AML/KYC system (PWMUS AMLKYC) generated an alert on May 29, 2013 at 11:43 AM, before the Southern Financial relationship was formally established. This was routed through the centralized AML/KYC mailbox: `pwmus.amlkyc@db.com` ([EFTA01299281](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01299281.pdf)).

#### June-August 2013 -- RDC Alerts on Jeffrey Epstein
- **[EFTA01299236](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01299236.pdf)** (p.1): `KYC :43 AM RDC Alert Jeffrey Epstein`
- **[EFTA01299294](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01299294.pdf)** (p.1): `06/12/2013 10 54 AM` and `b/29/201.3 11:43 AM Jeffrey Epstein RDC Alert Jeffrey Epstein`
- **[EFTA01299231](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01299231.pdf)** (p.0): `09/03/2013 04:32 PM Richard DKahn rdc alert` and `09/04/2013 11:09 AM`
- Multiple Reputational Due Diligence Check (RDC) alerts were triggered for Jeffrey Epstein, with Richard Kahn (Epstein's attorney and account manager for Southern Financial) specifically flagged. These alerts were processed through the KYC system but did **not** prevent account opening.

#### August 26, 2013 -- Southern Financial Relationship Established
- **[EFTA01472405](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01472405.pdf)** (p.0): `00000483290 483290 0016000000piPnF Banker 8/26/2013 SOUTHERN FINANCIAL RELATIONSHIP Clie`
- The Southern Financial relationship was formally created on August 26, 2013, with banker code 483290. The account was assigned to primary officer **Jj Litchford** and secondary officer **Paul Morris** ([EFTA01359500](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01359500.pdf)).
- **Relationship Management Code: 82289** -- this code is associated with all Epstein-related accounts at DB.

#### September 2013 -- Post-Opening RDC Alert
- **[EFTA01299231](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01299231.pdf)** (p.0): `09/03/2013 04:32 PM Richard DKahn rdc alert`
- Within days of account opening, another RDC alert was generated specifically naming Richard D. Kahn, the manager/trustee of Southern Financial. This alert was acknowledged but did not trigger account closure.

### Phase 2: Active Banking Relationship (2013-2017)

#### November 19, 2014 -- AMLKYC Review
- **[EFTA01360449](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01360449.pdf)** (p.0): `MMUS AMLKYC: 11/19/2014 09 38 AM`
- An AML/KYC review was conducted. The account was not flagged for closure.

#### January 2015 -- Credit Derivatives Trading Active
- **[EFTA01368602](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01368602.pdf)** (p.0): Full credit derivatives transaction details recovered from hidden text:
  - **Counterparty:** SOUTHERN FINANCIAL LLC
  - **Reference:** FEDERATIVE REPUBLIC OF BRAZIL (sovereign credit default swap)
  - **Notional:** USD 10mm (ten million dollars)
  - **Effective date:** 14-Jan-2015
  - **Maturity date:** 20-Mar-2020
  - **Deal rate:** 100, Spread: 205 bps
  - **Market Value:** $491,941
- DS9 provides the complete email record for this trade: **[EFTA00654057](https://www.justice.gov/epstein/files/DataSet%209/EFTA00654057.pdf)** contains the full email header confirming **Daniel Sabba** as the sender, with subject line "Trade Recap - 01/13/2014 - DB Sells $10mm FEDERATIVE REPUBLIC OF BRAZIL 20-Mar-2020 CDS @ 205 with SOUTHERN FINANCIAL LLC (live)" -- executed through DB London Branch. Follow-up at **[EFTA00699505](https://www.justice.gov/epstein/files/DataSet%209/EFTA00699505.pdf)** shows active position management: "With Petrobras downgrade, this closed at 228 / 232 on Friday. When you entered, it was 201 / 205. This is a pnl of approximately $120k."
- This document reveals that DB was actively executing **complex credit derivatives** through an Epstein-controlled entity, with maturities extending to 2020, well beyond any reasonable compliance horizon.

#### January 20, 2015 -- Valuation Statement
- **[EFTA01364928](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01364928.pdf)** (p.0): `Valuation Statement for SOUTHERN FINANCIAL, LLC as at 20 Jan 2015 - Request`
- Regular valuation statements were being generated for the Southern Financial portfolio (Request ID: 182298). Dozens of such statements were recovered spanning 2014-2016 ([EFTA01454985](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01454985.pdf) through [EFTA01459426](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01459426.pdf)).

#### February 17, 2015 -- Southern Financial Relationship Documented
- **[EFTA01398741](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01398741.pdf)** (p.3): `SOUTHERN FINANCIAL RELATIONSHIP 2/17/2015`
- The relationship was formally documented and reviewed.

#### March 31, 2015 -- Brokerage Active
- **[EFTA01475372](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01475372.pdf)** (p.0): `Additional Brokerage Southern Financial LLC 3/31/2015 75 Brokerage (Commissions) 7500`
- Active brokerage commissions being generated.

### Phase 3: KYC Escalation and Breach Discovery (2016-2018)

#### 2016 -- Onboarding Escalation: ONB-1135648 / LKYCGB-160049
- **[EFTA01357153](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01357153.pdf)** (p.0): Key escalation email recovered with high confidence (0.99):
  ```
  To: Zack Bunimovich, AMLUK Reviews, Jesse-J Cruz, James Gladwin,
  Kareen Johnson, Daniel-A Klyashtorny, Nina Tona, [Xavi]er Avila,
  Davide-A Sferrazza
  Subject: RE: Escalation: ONB 1135648 / LKYCGB 160049 / Southern Financi[al]
  ```
- **Case Numbers:**
  - **ONB-1135648** -- Onboarding case number
  - **LKYCGB-160049** -- London KYC Global Banking case number
- **Personnel on this escalation chain:**
  - **Zack Bunimovich** -- KYC analyst
  - **Jesse-J Cruz** -- KYC reviewer
  - **James Gladwin** -- KYC reviewer
  - **Kareen Johnson** -- Compliance
  - **Daniel-A Klyashtorny** -- Compliance
  - **Nina Tona** -- KYC/Compliance lead
  - **Xavier Avila** -- Senior compliance
  - **Davide-A Sferrazza** -- Compliance
  - **Martin Zeman** -- KYC compliance
  - **Ian Salters** -- AMLUK Reviews
  - **Simon Nall** -- Compliance
  - **Devshiji Odedra** -- Compliance
  - **Ricky-x P[atel]** -- Compliance
  - **Nicholas Hislo[p]** -- Compliance

- **[EFTA01363026](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01363026.pdf)** (p.0): `ccount-Openin[g] [Escalat]ion: ONB-1135648 / LKYCGB-160049 / Southern Financial L[LC]`
  - This reveals the escalation was specifically about the **account opening** process, meaning the original onboarding was being questioned.

- **[EFTA01362904](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01362904.pdf)** (p.0): Second major escalation email with the same distribution list, confirming this was a multi-round escalation that was **not quickly resolved**.

#### Concurrent: Southern Financial KYC Documentation Requests
- **[EFTA01362836](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01362836.pdf)** (p.0): `[Sout]hern Financial - KYC D[ocs]`
- **[EFTA01362901](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01362901.pdf)** (p.0): `[Sout]hern Financial - KYC Docs. [I]`
- **[EFTA01363756](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01363756.pdf)** (p.0): `RE: Southern Financial - KYC Docs.[I]`
  - **Personnel:** Liam Osullivan, Davide-A Sferrazza, Joshua Shoshan
- **[EFTA01362751](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01362751.pdf)** (p.0): `[Alastair] Mackinlay, Anthony Lentini, [Souther]n Financial LLC - KYC and credit derivatives/convertible bonds`
  - This reveals that the KYC review extended to the **credit derivatives and convertible bonds** portfolio, meaning compliance was aware of the complex financial instruments being traded.

#### "KYC is not happening" -- Internal Admission
- **[EFTA01362456](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01362456.pdf)** (p.0): `kyc is not happening`
  - A blunt internal admission that the KYC process had stalled or was being blocked.

#### Southern Financial "Reboot"
- **[EFTA01369369](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01369369.pdf)** (p.0): `Southern Financial reboot`
  - After the stalled KYC process, there was an attempt to "reboot" the Southern Financial compliance review, suggesting the original process had failed.

### Phase 4: The KYC Breach Declaration (April 2018)

#### April 16, 2018, 11:56 AM -- KYC Breach Formally Identified
- **[EFTA01363001](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01363001.pdf)** (p.0): `16, 2018, 11:56` with `RE: KYC Breach_SOUTH[FINANMD]`
- **[EFTA01363054](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01363054.pdf)** (p.0): `16, 2018, 11:56` with `RE: KYC Breac[h]_SOUTHFINAN[MD]`
- **[EFTA01406915](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01406915.pdf)** (p.0): `r 16, 2018, 11:56` -- confirming "Apr 16, 2018, 11:56"

The breach was formally declared on **April 16, 2018 at 11:56 AM** via an email chain with the subject line:
```
KYC Breach_SOUTHFINANMD_Southe[rn] Financial, LLC_FFT Location [I]
```

**FFT Location** indicates this was flagged as a **Financial Fraud/Terrorism** location-based compliance issue.

#### April 16, 2018 -- Initial Breach Email Chain
The full email subject, recovered from **[EFTA01362996](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01362996.pdf)** (confidence 0.99):
```
Cc: Joe Aglione, Ian Salters, Nina T[ona], [Pankaj-A C]hopra,
NCAOTC Derivatives, Alka Gopala
Subject: RE: KYC Breach_SOUTHFTNANMD_Southe[r]n Financial, LLC_FFT Loca[tion]
```

**Personnel on the breach notification:**
| Name | Role (Inferred) | EFTA Evidence |
|------|----------------|---------------|
| **Akash Malhotra** | KYC Breach Lead / Sender | [EFTA01406915](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01406915.pdf), [EFTA01406842](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01406842.pdf) |
| **Shawn Staker** | CC'd Compliance | [EFTA01406842](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01406842.pdf), [EFTA01406871](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01406871.pdf) |
| **Xavier Avila** | Primary Recipient (later chain) | [EFTA01406871](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01406871.pdf), [EFTA01406857](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01406857.pdf) |
| **Mathew Negus** | CC'd / Escalation Target | [EFTA01356960](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01356960.pdf), [EFTA01363052](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01363052.pdf) |
| **Joe Aglione** | CC'd Compliance | [EFTA01362996](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01362996.pdf), [EFTA01363052](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01363052.pdf) |
| **Nina Tona** | CC'd / KYC Lead | [EFTA01362996](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01362996.pdf), [EFTA01406857](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01406857.pdf) |
| **Martin Zeman** | CC'd / Compliance | [EFTA01406871](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01406871.pdf) |
| **Alka Gopala** | NCAOTC Derivatives / CC'd | [EFTA01362996](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01362996.pdf), [EFTA01363005](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01363005.pdf) |
| **Pankaj-A Chopra** | CC'd / Derivatives Compliance | [EFTA01399702](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01399702.pdf), [EFTA01406845](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01406845.pdf) |
| **Alastair Mackinlay** | Senior Compliance / Oversight | [EFTA01362751](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01362751.pdf), [EFTA01362965](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01362965.pdf) |
| **Jimmy-H Xu** | CC'd | [EFTA01363001](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01363001.pdf), [EFTA01363052](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01363052.pdf) |
| **Ian Salters** | CC'd / AML Reviews | [EFTA01362996](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01362996.pdf) |

#### April 16, 2018, 5:44 PM -- Continued Breach Discussion
- **[EFTA01358357](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01358357.pdf)** (p.0): `8, 5:44 PM Xavier Avila`
- Xavier Avila was actively engaged in the breach discussion on the same day.

#### April 16, 2018, 7:34 PM -- Evening Email Chain
- **[EFTA01358461](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01358461.pdf)** (p.0): `018.07:34` with `Malhotra Staker M[athew N]E: KYC Breach SOUTH[FINANMD]`
- **[EFTA01362961](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01362961.pdf)** (p.0): `018 07.34` -- confirming the breach discussion continued into the evening.

#### April 17, 2018, 2:53 AM -- Overnight Escalation
- **[EFTA01406845](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01406845.pdf)** (p.0): `pr 17, 2018, 2:53 AM`
- **[EFTA01362995](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01362995.pdf)** (p.0): `7. 2018, 2:53 AM`
- **[EFTA01363053](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01363053.pdf)** (p.0): `7, 2018, 2:53 AM`
- The breach discussion continued through the night with a 2:53 AM email, suggesting **international (London) compliance involvement** was engaged.

#### April 17, 2018, 8:10 AM -- Morning Follow-Up
- **[EFTA01406871](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01406871.pdf)** (p.0): `17, 2018, 08:10`
- Morning follow-up on the breach, with the full distribution list reconfirmed.

#### April 17, 2018, 9:44 AM -- Continued Discussion
- **[EFTA01399702](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01399702.pdf)** (p.0): `7, 2018, 09:44`
- The breach chain continued with additional discussion.

### Phase 5: Post-Breach -- Continued Account Servicing (April-December 2018)

#### Critical Finding: Trading and Account Activity Continued

Despite the formal KYC breach declaration on April 16, 2018, the following evidence demonstrates **continued account servicing:**

**May-October 2018 -- Active Account Balances (RM CODE 82289):**
- **[EFTA01415223](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01415223.pdf)** (05/16/18): Southern Financial LLC - D - $396,015.00
- **[EFTA01415265](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01415265.pdf)** (05/15/18): Southern Financial LLC - D - $396,015.00 + second entry $2,029,601.20
- **[EFTA01415119](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01415119.pdf)** (06/07/18): Southern Financial LLC - D - $396,015.00
- **[EFTA01381246](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01381246.pdf)** (06/21/18): Southern Financial LLC - D - $532,186.86
- **[EFTA01415125](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01415125.pdf)** (06/25/18): Southern Financial LLC - D - $426,615 + $532,186.86
- **[EFTA01415196](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01415196.pdf)** (07/20/18): Southern Financial LLC - D - $533,630.09
- **[EFTA01415140](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01415140.pdf)** (07/25/18): Southern Financial LLC - D - $376,315.00 + $533,630.09
- **[EFTA01381149](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01381149.pdf)** (08/17/18): Jeffrey Epstein - N - $1,243,515.74; Southern Financial LLC - D - $376,315.00
- **[EFTA01413971](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01413971.pdf)** (08/28/18): Southern Financial LLC - D - $1,376,315.00 + $534,440.04
- **[EFTA01427866](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01427866.pdf)** (10/18/18): Southern Financial LLC - D - $1,187,706.86

These are **Large, Zero and Negative Balances** reports generated under RM CODE 82289, confirming the accounts remained **fully operational** for at least **six months** after the breach declaration.

#### 2018 Account Planning -- Business as Usual
- **[EFTA01386924](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01386924.pdf)** (p.0): `2018 Account Planning - 2018 Account Planning - Southern Financial v2.docx`
- A formal 2018 account planning document was created for Southern Financial, indicating the bank was **actively planning future business** with the entity even as the KYC breach remained unresolved.

#### 2018 Periodic Review
- **[EFTA01406280](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01406280.pdf)** (p.1): `RE: 2018 Periodic Review of Accts Southern Financial`
  - **Personnel:** Liam Osullivan, Bradley Gillin, Stewart Oldfield, Mayur Rathod
- A periodic review of the Southern Financial accounts was conducted in 2018, involving senior relationship managers.

#### KYC Case Reviews Continued to Stall
- **[EFTA01378580](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01378580.pdf)** (p.0): `Assistance Required in solving [i]n KYC Case$10194682S [I]` (interest score: 67.64 -- highest of all KYC-related reconstructed pages)
- **KYC Case #01946825** appears across multiple documents ([EFTA01370862](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01370862.pdf), [EFTA01381143](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01381143.pdf), [EFTA01387493](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01387493.pdf), [EFTA01387913](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01387913.pdf), [EFTA01388105](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01388105.pdf), [EFTA01388543](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01388543.pdf), [EFTA01388738](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01388738.pdf)), indicating an open, unresolved case that persisted.
- **KYC Case #01977698** ([EFTA01379999](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01379999.pdf), [EFTA01388746](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01388746.pdf)) -- Another open case.
- **KYC Case #01977695** ([EFTA01379613](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01379613.pdf), [EFTA01381381](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01381381.pdf), [EFTA01387857](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01387857.pdf)) -- Yet another.
- **KYC Case #0165178** ([EFTA01363167](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01363167.pdf)): `Please attach to kyc case 0165178` -- manual document attachment requests indicate a chaotic paper trail.

#### KYC Rejection
- **[EFTA01415323](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01415323.pdf)** (p.0): `KYC has been rejected` with `ayur.rathod@db.com` (Mayur Rathod)
- A KYC case was formally **rejected**, but this did not result in immediate account closure.

- **[EFTA01358825](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01358825.pdf)** (p.0): `ed on Rejected KYC C[ase]`
- Confirmation that KYC cases were being rejected but the relationship continued.

#### September 2018 -- Trade Activity Continues
- **[EFTA01369327](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01369327.pdf)/01369328** (p.0): Trade details prepared on `09/12/2018`
- **[EFTA01414057](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01414057.pdf)** (p.0): `Trade Details -- 09/12/2018 [C]`
- Trading activity continued through September 2018.

#### REASSIGN NEEDED -- Compliance Shuffling
- **[EFTA01408641](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01408641.pdf)** (multiple pages): `***REASSIGN NEEDED***FW: SOUTHERN FINANCIAL LLC - ONB-1010155`
  - **ONB-1010155** -- A second onboarding case number for Southern Financial, different from ONB-1135648
  - The "REASSIGN NEEDED" designation across **21 pages** of email chain indicates the compliance case was being shuffled between personnel, a classic marker of institutional avoidance.

### Phase 6: Account Closure (Late 2018 - Early 2019)

#### December 2018 -- Accounts Begin Closing
- **[EFTA01413997](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01413997.pdf)** (p.2): `12/12/2018` -- date reference in account activity
- **[EFTA01432198](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01432198.pdf)** (RM CODE 82289, 01/14/19): Last known balance report shows Southern Financial LLC still active with balance of $0.00 alongside other Epstein entities (Gratitude America $2,232,836.20; Zorro Management $255,511.05; The Haze Trust $8,789,938.49; Butterfly Trust $357,146.85)

#### February 2019 -- Final Wind-Down
- **[EFTA01432142](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01432142.pdf)** (02/06/19): Southern Financial LLC - D - $2,924,080.14
- This extraordinarily large balance in February 2019 suggests a final settlement or position unwind.

#### CIB Offboard List
- **[EFTA01379375](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01379375.pdf)** (p.0): `he CIB offboard list Clie[nt]`
- **[EFTA01420881](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01420881.pdf)** (p.1): `[C]IB Offboard`
- Evidence that the client was eventually placed on the Corporate & Investment Banking offboard list.

### Phase 7: Regulatory Action (2020)

- On **July 7, 2020**, the New York State Department of Financial Services (NYDFS) imposed a **$150 million fine** on Deutsche Bank for, among other failures, its relationship with Jeffrey Epstein. The Consent Order documented that DB had failed to properly monitor the Epstein relationship and had processed hundreds of millions of dollars in suspicious transactions.

---

## KEY PERSONNEL ANALYSIS

### The Breach Email Chain (April 16-17, 2018)

| Person | Appearances | Role Evidence | First Appearance |
|--------|------------|---------------|-----------------|
| **Akash Malhotra** | 6 EFTAs | Sender of breach emails ("From: Akash Malhotra" - [EFTA01406915](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01406915.pdf)) | [EFTA01358382](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01358382.pdf) |
| **Shawn Staker** | 16+ entries | CC'd on all breach emails, consistent presence | [EFTA01358461](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01358461.pdf) |
| **Xavier Avila** | 30+ entries | Primary recipient in later chain; also on original escalation ONB-1135648 | [EFTA01353544](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01353544.pdf) |
| **Mathew Negus** | 25+ entries | CC'd on breach; involved in SF [I] (Southern Financial) thread extensively | [EFTA01356960](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01356960.pdf) |
| **Joe Aglione** | 5 entries | CC'd on breach notification; NCAOTC connection | [EFTA01358461](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01358461.pdf) |
| **Nina Tona** | 35+ entries | Central compliance figure; on both escalation and breach chains | [EFTA01355937](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01355937.pdf) |
| **Martin Zeman** | 25+ entries | CC'd on breach; KCP Bible action plan; extensive SF involvement | [EFTA01356961](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01356961.pdf) |
| **Alka Gopala** | 8 entries | NCAOTC Derivatives representative on breach chain | [EFTA01358382](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01358382.pdf) |
| **Pankaj-A Chopra** | 15 entries | Derivatives compliance; appears only in later breach docs ([EFTA01399702](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01399702.pdf)+) | [EFTA01399702](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01399702.pdf) |
| **Alastair Mackinlay** | 20+ entries | Senior oversight; on SF [I] thread; Southern Financial LLC ONB-1010155 | [EFTA01356940](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01356940.pdf) |

### Supporting Personnel

| Person | Role Evidence |
|--------|--------------|
| **Jimmy-H Xu** | CC'd on breach escalation to Mathew Negus ([EFTA01363001](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01363001.pdf), [EFTA01363052](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01363052.pdf)) |
| **Ian Salters** | AMLUK Reviews; on both escalation and breach chains |
| **Zack Bunimovich** | KYC analyst; led original ONB-1135648 escalation |
| **James Gladwin** | KYC reviewer on escalation |
| **Kareen Johnson** | Compliance; on escalation chain |
| **Liam Osullivan** | Relationship management; Southern Financial KYC Docs |
| **Joshua Shoshan** | KYC documentation collection |
| **Davide-A Sferrazza** | Compliance; on both escalation and breach |
| **Rita Shteynberg** | Compliance; SF [I] thread |
| **Anthony Lentini** | Compliance; KYC and credit derivatives review |
| **Zbynek Kozelsky** | Southern Financial case handler (026161) |
| **Stewart Oldfield** | Senior relationship manager; 2018 Periodic Review |
| **Bradley Gillin** | Relationship management; Daily Deposit Reports |
| **Mayur Rathod** | KYC reviewer; the person whose KYC review was "rejected" |
| **Lee Rutte** | AML/KYC Escalation Report author ([EFTA01356293](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01356293.pdf)) |
| **Vaishali-P Mehta** | Southern Financial Relationship assessment |
| **Billy Obregon** | KYC Priority List ([EFTA01358471](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01358471.pdf)) |
| **Bella Klein** | Epstein's personal accountant; processed transactions through DB |
| **Richard Kahn** | Epstein's attorney; manager of Southern Financial LLC |

---

## DOCUMENT INVENTORY: KYC BREACH CHAIN

### Core KYC Breach Emails (Subject: "KYC Breach_SOUTHFINANMD_Southern Financial, LLC_FFT Location")

| EFTA Number | Pages | Key Content | Date Evidence |
|-------------|-------|-------------|---------------|
| [EFTA01356960](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01356960.pdf) | 0 | `To: Mathew Ne[gus]... Subject: RE: KYC Breach` | `2015 0R 10` (corrupted) |
| [EFTA01356961](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01356961.pdf) | 0 | `RE: KYC Breach`, Martin Zeman, Alka G[opala] | `16 2018 11 56` |
| [EFTA01358382](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01358382.pdf) | 0 | `Malhotra, Ma[thew] Stake[r] RE: KYC Breach SOUTHFI[NANMD]` | `2018. 07: 4[PM]` |
| [EFTA01358461](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01358461.pdf) | 0 | `Malhotra Staker M[athew] E: KYC Breach SOUTH` | `018.07:34` |
| [EFTA01362961](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01362961.pdf) | 0 | Full subject: `KYC Breach SOUTHFINA[NMD]... FFT Location` | `018 07.34` |
| [EFTA01362996](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01362996.pdf) | 0 | **Most complete header**: Joe Aglione, Ian Salters, Nina Tona, Chopra, NCAOTC Derivatives, Alka Gopala | -- |
| [EFTA01362997](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01362997.pdf) | 0 | Avila, Staker, Alk[a], Marti[n] | -- |
| [EFTA01363001](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01363001.pdf) | 0 | Jimmy-H Xu, Mathew Ne[gus], J[oe] A[g]li[one] | `16, 2018, 11:56` |
| [EFTA01363002](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01363002.pdf) | 0 | `ash Malhotra... RE: KYC Breach_SOUTH[FINANMD]` | -- |
| [EFTA01363004](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01363004.pdf) | 0 | Xavier Avila, Alka Gopal[a] | -- |
| [EFTA01363005](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01363005.pdf) | 0 | Xavier Avila, Alka Gopala | -- |
| [EFTA01363009](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01363009.pdf) | 0 | `Southem Financial, LLC FFT Location [I]` | `17:55` |
| [EFTA01363021](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01363021.pdf) | 0 | Jimmy-H Xu, Alka Go[pala], SOUTHFINANMD | -- |
| [EFTA01363048](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01363048.pdf) | 0 | Xavier Avila, Mathew Negus, Joe Aglione, Nina Ton[a] | `2 53 54 AM` |
| [EFTA01363049](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01363049.pdf) | 0 | Full chain with NCAOTC derivatives | -- |
| [EFTA01363050](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01363050.pdf) | 0 | `[Akas]h Malhotra, [Shaw]n Staker` | -- |
| [EFTA01363052](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01363052.pdf) | 0 | `To: Mathew Ne[gus]... Cc: Joe Aglione Subject: RE; KYC Breach` | -- |
| [EFTA01363054](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01363054.pdf) | 0 | `NCA[OTC], Alka Gopala... KYC Breac[h]_SOUTHFINAN[MD]` | `16, 2018, 11:56` |
| [EFTA01363055](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01363055.pdf) | 0 | Staker, KYC Breach_SOUTH | `17 55` |
| [EFTA01399702](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01399702.pdf) | 0-9 | **9-page email chain**: Akash Malhotra, Shawn Staker, Pankaj-A Chopra | `7, 2018, 09:44` |
| [EFTA01401922](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01401922.pdf) | 0-1 | Xavier Avila, Shawn Staker; `+1 917 8541256` (phone) | -- |
| [EFTA01406842](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01406842.pdf) | 0-1 | `To: Akash Malhotra Cc: Shawn Staker... RE: KYC Breach_SOUT[HFINANMD]` | -- |
| [EFTA01406845](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01406845.pdf) | 0-4 | Full chain with Negus, Pankaj-A Chopra, Zeman | `pr 17, 2018, 2:53 AM` |
| [EFTA01406857](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01406857.pdf) | 0-6 | `To: Xavier Avila Cc: Sha[w]n Staker; Pankaj-A [Chopra]; Gopala; Nina Tona; Martin Zeman` | -- |
| [EFTA01406871](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01406871.pdf) | 0-7 | **Most complete chain**: All personnel, NCAOTC Derivatives | `17, 2018, 08:10` |
| [EFTA01406881](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01406881.pdf) | 0-6 | `To: Akash Malhotra Cc: Shawn Staker... Pankaj-A Chopr[a]; Nina Tona; Mathew Negus` | -- |
| [EFTA01406890](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01406890.pdf) | 0-2 | Xavier Avila, Malhotra, Staker | -- |
| [EFTA01406895](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01406895.pdf) | 0-8 | Full chain, 8 pages | -- |
| [EFTA01406915](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01406915.pdf) | 0-3 | `From: Akash Malhotra` (confirmed sender), `r 16, 2018, 11:56` | Apr 16, 2018 |
| [EFTA01406948](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01406948.pdf) | 0-4 | `To: Akash Malhotra Cc: Shawn Staker... Mathew [Negus]... Pankaj-A Chopr[a]` | -- |
| [EFTA01406955](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01406955.pdf) | 0-6 | Final chain entry in range; all personnel | -- |

### Escalation Chain Documents (ONB-1135648 / LKYCGB-160049)

| EFTA Number | Key Content |
|-------------|-------------|
| [EFTA01357150](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01357150.pdf)-01357168 | Original escalation chain, multiple pages |
| [EFTA01362904](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01362904.pdf)-01362910 | Second round of escalation |
| [EFTA01363024](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01363024.pdf)-01363032 | Account-Opening Escalation |
| [EFTA01400073](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01400073.pdf) | 12-page escalation document |
| [EFTA01400111](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01400111.pdf) | 11-page escalation document |
| [EFTA01406804](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01406804.pdf) | Later escalation |
| [EFTA01406921](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01406921.pdf) | 11-page escalation document |

---

## ANALYTICAL CONCLUSIONS

### 1. The KYC Breach Was Known for Years Before Formal Declaration

The evidence shows a pattern of **incremental awareness**:
- **May 2013**: First AML/KYC alert generated
- **June-September 2013**: Multiple RDC alerts on Jeffrey Epstein and Richard Kahn
- **2016**: Formal escalation of ONB-1135648 / LKYCGB-160049 involving 15+ compliance personnel
- **April 16, 2018**: Formal KYC breach declared

The gap between the 2016 escalation and the 2018 formal breach declaration represents approximately **two years** of institutional delay. The internal admission that "kyc is not happening" ([EFTA01362456](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01362456.pdf)) and the "Southern Financial reboot" ([EFTA01369369](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01369369.pdf)) confirm that the compliance process was stalled and restarted, rather than acted upon.

### 2. DB Continued Servicing Accounts After Breach Identification

The financial records under RM CODE 82289 demonstrate **uninterrupted account activity** from April 2018 through at least January 2019:
- Monthly balance reports continued without interruption
- Southern Financial maintained balances ranging from $289,515 to $2,924,080
- The Haze Trust (another Epstein entity) maintained balances exceeding $49 million
- Trading activity (credit derivatives, trade details) continued through at least September 2018
- A 2018 Account Planning document was created, indicating forward-looking business development

This represents a minimum **8-9 month period** of continued banking services after the KYC breach was formally declared.

### 3. The Compliance Apparatus Was Structurally Overwhelmed

The evidence reveals:
- **At least 3 separate KYC case numbers** (01946825, 01977698, 01977695) were open simultaneously
- **2 separate onboarding case numbers** (ONB-1135648, ONB-1010155) existed for the same entity
- **Multiple REASSIGN NEEDED** flags across 21 pages indicate case shuffling
- The "GM KCP Bible - Action Plan" email thread (10+ documents) suggests compliance was creating procedural documentation rather than taking action
- The "KYC Priority List" ([EFTA01358471](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01358471.pdf)) indicates Southern Financial was one of many problematic accounts being triaged rather than resolved

### 4. NCAOTC Derivatives Involvement Indicates Revenue Motivation

The presence of **NCAOTC Derivatives** (Non-Cleared/OTC Derivatives) personnel (Alka Gopala, Pankaj-A Chopra) on the breach notification chain indicates that the KYC breach had implications for **revenue-generating derivatives trading**. The Brazil sovereign CDS with USD 10mm notional ([EFTA01368602](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01368602.pdf)) demonstrates that Southern Financial was not merely a deposit account but an active **derivatives counterparty** generating significant fees and market exposure.

### 5. The Timeline Demonstrates Systemic Failure, Not Isolated Error

| Milestone | Date | Gap |
|-----------|------|-----|
| First AML/KYC alert | May 29, 2013 | -- |
| Account opened | August 26, 2013 | 89 days after first alert |
| RDC alert on Richard Kahn | September 3, 2013 | 8 days after opening |
| First known escalation (ONB-1135648) | ~2016 | ~3 years of unreviewed activity |
| "KYC is not happening" admission | ~2016-2017 | -- |
| "Southern Financial reboot" | ~2017 | Process restart after failure |
| Formal KYC breach declared | April 16, 2018 | ~5 years after account opening |
| Last known active balance | February 6, 2019 | ~10 months after breach |
| DB fined by NYDFS | July 7, 2020 | ~27 months after breach |

### 6. Failure by Design or Negligence?

The evidence supports a conclusion of **systemic institutional negligence with elements of willful blindness**, rather than a deliberate conspiracy to enable Epstein. Specifically:

**Indicators of negligence:**
- The sheer number of compliance personnel involved (25+) demonstrates that the system was **aware** of the problems
- Multiple escalation chains, case numbers, and reassignments indicate bureaucratic dysfunction rather than suppression
- The "KYC is not happening" and "reboot" references suggest frustration within compliance ranks

**Indicators of willful blindness:**
- The account was opened **despite** pre-existing RDC alerts
- Compliance escalations were **repeatedly delayed, reassigned, and restarted** over a period of years
- The KYC breach declaration did **not** trigger immediate account suspension or closure
- Revenue-generating derivatives trading continued after the breach
- A 2018 Account Planning document was created, indicating the **business side** was planning to grow the relationship even as compliance had declared a breach
- The "SF [I]" coded references (60+ documents) across compliance discussions suggest the Southern Financial issue was a well-known, ongoing concern that became normalized within the institution

**Overall Assessment:** Deutsche Bank's compliance apparatus functioned as a **friction mechanism** rather than a **gatekeeping mechanism**. It generated documentation, escalation chains, and case numbers sufficient to create an appearance of oversight, while the revenue-generating business operations continued unimpeded. The 25+ compliance personnel involved were individually performing their procedural duties, but the system was designed to process compliance as a bureaucratic workflow rather than a binary pass/fail gate. The result was that a convicted sex offender maintained an active, complex banking relationship including derivatives trading for approximately five years, during which time the compliance function generated hundreds of pages of documentation without achieving the fundamental goal of the KYC regime: to actually know and appropriately manage the risk of the customer.

---

## APPENDIX A: Key Email Addresses Recovered

| Email | Context |
|-------|---------|
| `pwmus.amlkyc@db.com` | Central AML/KYC alert system ([EFTA01299281](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01299281.pdf)) |
| `martin.zeman@db.com` | Martin Zeman ([EFTA01387689](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01387689.pdf)) |
| `mathew.negus@db.com` | Mathew Negus ([EFTA01362550](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01362550.pdf) partial) |
| `nina-x.nevidzanska@db.com` | Event management ([EFTA01387242](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01387242.pdf)) |
| `mayur.rathod@db.com` | Mayur Rathod - KYC reviewer ([EFTA01415323](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01415323.pdf)) |
| `emily.craig@db.com` / `craig@db.com` | Emily Craig - KYC HR Clients Remediation ([EFTA01373298](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01373298.pdf)) |
| `amanda.kirby@db.com` | Amanda Kirby ([EFTA01361085](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01361085.pdf)) |
| `daniel.sabba@db.com` | Daniel Sabba - CRM ([EFTA01361127](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01361127.pdf)) |
| `armen.brash@db.com` | Armen Brash ([EFTA01361077](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01361077.pdf)) |
| `catherine.logreco@db.com` | Catherine Logreco ([EFTA01358522](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01358522.pdf)) |
| `cynthia.rodriguez@db.com` | Cynthia Rodriguez ([EFTA01375491](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01375491.pdf)) |
| `corporate.chasing@db.com` | Corporate chasing / escalation group ([EFTA01409736](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01409736.pdf)) |
| `thebranch.staff@db.com` | Branch staff ([EFTA01345701](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01345701.pdf)) |

## APPENDIX B: Epstein Entity Account Balances at DB (RM CODE 82289)

From [EFTA01381246](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01381246.pdf) (06/21/18) -- representative snapshot:
| Entity | Type | Balance |
|--------|------|---------|
| Jeffrey Epstein | N | $1,224,163.61 |
| Hyperion Air, LLC | D | -- |
| Plan D, LLC | D | $347,674.83 |
| JEGE, LLC | D | $299,328.13 |
| Darren K. Indyke PLLC | D | $243,363.55 |
| HBRK Associates, Inc | D | $211,289.05 |
| Southern Trust Company, Inc. | M | -- |
| Butterfly Trust | M | $733,701.04 |
| Gratitude America, Ltd | M | $323,223.15 |
| Darren K. Indyke PLLC - [Trust] | M | $267,972.25 |
| The Haze Trust | D | $49,460,098.13 |
| Southern Financial LLC | D | $532,186.86 |
| Southern Trust Company, Inc. | D | $102,625.90 |

**Total visible balances across Epstein entities: >$53 million** (as of a single date in mid-2018)

## APPENDIX C: EFTA Document Range Summary

| EFTA Range | Document Type | Count |
|------------|--------------|-------|
| [EFTA01298802](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01298802.pdf)-01299318 | Early RDC alerts and KYC system alerts | ~10 |
| [EFTA01355649](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01355649.pdf)-01356961 | KYC HR Remediation, Escalation Reports, initial breach | ~30 |
| [EFTA01357132](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01357132.pdf)-01358461 | Escalation ONB-1135648/LKYCGB-160049, breach chain | ~25 |
| [EFTA01362456](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01362456.pdf)-01364103 | "KYC not happening", breach chain, KYC Docs, case files | ~60 |
| [EFTA01368246](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01368246.pdf)-01369369 | Southern Financial trading, reboot | ~10 |
| [EFTA01370462](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01370462.pdf)-01375877 | RM CODE 82289 reports, KYC cases | ~30 |
| [EFTA01378580](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01378580.pdf)-01388746 | KYC case reviews, 2018 HR KYCs, rejections | ~40 |
| [EFTA01399055](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01399055.pdf)-01402000 | KYC Tracker, breach continuation, SF [I] thread | ~50 |
| [EFTA01406280](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01406280.pdf)-01409736 | Periodic Review, REASSIGN NEEDED, final breach chain | ~40 |
| [EFTA01413971](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01413971.pdf)-01432198 | Account balances, offboard, closure | ~30 |
| [EFTA01454985](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01454985.pdf)-01477330 | Valuation statements, relationship records | ~50 |

**Total KYC breach-related documents identified: ~375+ unique EFTA numbers**

---

## APPENDIX D: DS9/DS11 REVISIT FINDINGS (2026-02-12)

DS9 full-text search reveals substantial new evidence supplementing the DS10-based analysis above. The following corrections and additions apply:

### Correction 1: Derivatives Termination Timeline
DS9 reveals ([EFTA00169436](https://www.justice.gov/epstein/files/DataSet%209/EFTA00169436.pdf)) that the ISDA Master Agreement and GMRA contracts for Southern Financial LLC (PLM 640310/739190) and Southern Trust Company Inc (PLM 640330/752070) were being **terminated in November 2016** -- approximately 17 months before the April 2018 KYC breach. The derivatives book was wound down before the KYC breach, while deposit accounts and other activity continued.

### Correction 2: Revenue Estimate
The civil complaint against Deutsche Bank ([EFTA00161958](https://www.justice.gov/epstein/files/DataSet%209/EFTA00161958.pdf), 163 pages) states that "Deutsche Bank estimated that it would earn between $2,000,000 to $4,000,000 annually" from the Epstein relationship.

### Correction 3: Total Assets Under Management
The original report estimated ~$53M based on single-date balance snapshots. DS9 provides ([EFTA00165748](https://www.justice.gov/epstein/files/DataSet%209/EFTA00165748.pdf)) the total figure: **$220,000,000** in "Total Assets within Bank" for the "Southern Financial Relationship" as of April 8, 2014. An internal email ([EFTA00128826](https://www.justice.gov/epstein/files/DataSet%209/EFTA00128826.pdf)) states: "Jeffrey Epstein is worth roughly $[1]B and currently has about $230MM here at the bank and we are expecting at least another $100MM from him within the next few months... he is a very important client."

### Addition 1: FBI Witness Interviews
- **[EFTA00128765](https://www.justice.gov/epstein/files/DataSet%209/EFTA00128765.pdf)** (15 pages): FBI FD-302 interview of **Amanda Kirby** (8/10/2021), Paul Morris's relationship coordinator. Kirby "felt uncomfortable from day one of EPSTEIN being onboarded as a client," described Morris as "insecure and a back-handed manipulator," confirmed KYC for Epstein was "high risk" and that she identified a trust beneficiary as a co-conspirator but the account was opened anyway.
- **[EFTA00128968](https://www.justice.gov/epstein/files/DataSet%209/EFTA00128968.pdf)** (5 pages): FBI FD-302 interview of **Cherie Quigley** (10/10/2019), AML monitoring officer using the PRIME system. Quigley admitted: "Looking back, maybe a SAR should have been filed on EPSTEIN."

### Addition 2: Paul Morris -- Prince Andrew Dismissal
**[EFTA00128837](https://www.justice.gov/epstein/files/DataSet%209/EFTA00128837.pdf)**: Morris email to Troy Williams (Jan 5, 2015): "Troy the stories about Prince Andrew have been popping up in the press for years. I will post the team if there is anything that has changed." Morris was actively dismissing reputational risk concerns.

### Addition 3: 13.7 Million Ruble Wire to Moscow
**[EFTA00128809](https://www.justice.gov/epstein/files/DataSet%209/EFTA00128809.pdf)**: Wire memo from Darren Indyke to Amanda Kirby instructing a wire of 13,700,000 rubles to AO Raiffeisenbank, Moscow, Russia from an Epstein account. "Please call Bella Klein if you have any questions."

### Addition 4: Key New Personnel
| Person | EFTA | Role |
|--------|------|------|
| Armen Brash | [EFTA00128804](https://www.justice.gov/epstein/files/DataSet%209/EFTA00128804.pdf) | KYC compliance -- discussed escalation with Patrick Harris |
| Monifa Crawford, JD | [EFTA00128810](https://www.justice.gov/epstein/files/DataSet%209/EFTA00128810.pdf) | AML Compliance Officer, DB Securities Inc., Jacksonville FL |
| Cherie Quigley | [EFTA00128968](https://www.justice.gov/epstein/files/DataSet%209/EFTA00128968.pdf) | AML monitoring, PRIME system operator |
| Troy-D Williams | [EFTA00128837](https://www.justice.gov/epstein/files/DataSet%209/EFTA00128837.pdf) | DB compliance, flagged Prince Andrew press to Morris |
| Roddy Moore | [EFTA00169436](https://www.justice.gov/epstein/files/DataSet%209/EFTA00169436.pdf) | Business Risk Management, derivatives termination |

### Addition 5: NYDFS Consent Order
**[EFTA00151495](https://www.justice.gov/epstein/files/DataSet%209/EFTA00151495.pdf)** (37 pages): The complete $150M NYDFS Consent Order, signed by Linda A. Lacewell (Superintendent) and DB Global Head of Litigation Joe Salama. DB agreed not to claim a tax deduction on the penalty and to provide "Full and Complete Cooperation."

### Addition 6: Civil RICO Allegations
**[EFTA00161958](https://www.justice.gov/epstein/files/DataSet%209/EFTA00161958.pdf)** (163 pages): Civil complaint names Charles Packard, Patrick Harris, Paul Morris, and Jan Ford as participants in an "association-in-fact" enterprise that facilitated Epstein's sex trafficking. "Packard and Morris did not make any contemporaneous record of their meeting with Epstein. The reason they did not make a record of Epstein's denials was that any such record would have been utterly implausible."

---

*This report was generated through forensic analysis of text extracted from document text layers of DOJ production documents in the Epstein files. All findings are based on extracted text and should be verified against original source documents where available. DATA QUALITY NOTE: A data quality audit confirmed ~98% of 'bad_overlay' records are OCR noise from degraded scans. Text searches remain valid for identifying document content.*
