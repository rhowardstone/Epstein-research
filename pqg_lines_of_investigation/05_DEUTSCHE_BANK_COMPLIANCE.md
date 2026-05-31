# Line of Investigation 05: Deutsche Bank Production Analysis

## Executive Summary

Deutsche Bank received a single grand jury subpoena on July 11, 2019 — five days after Epstein's arrest — containing 27 demand clauses covering a decade of banking records. The substantive production fulfilled 8 of 9 evaluated demand clauses, totaling 96,019 pages received on September 29, 2020. Four additional 3-page "Reproduction" transmittal documents followed in December 2020. The PQG's clause-level analysis identifies one structural gap: Clause 5, requesting identification records for all account holders, is the only demand that went entirely unfulfilled across all returns. The PQG could only evaluate 9 of the 27 demand clauses — clauses 10 through 27 were never parsed into the analysis pipeline.

---

## 1. The Subpoena

A single grand jury subpoena, dated July 11, 2019, addressed to:

> Deutsche Bank AG, New York Branch / Deutsche Bank Securities Inc.
> Attn: Andrew Stemmer
> 60 Wall Street, New York, NY 10005

The subpoena appears at four EFTA locations in the corpus — identical copies stored across different production batches:

| EFTA | Dataset |
|------|---------|
| [EFTA00022527](https://www.justice.gov/epstein/files/DataSet%208/EFTA00022527.pdf) | DS8 |
| [EFTA00095467](https://www.justice.gov/epstein/files/DataSet%209/EFTA00095467.pdf) | DS8 |
| [EFTA00097178](https://www.justice.gov/epstein/files/DataSet%209/EFTA00097178.pdf) | DS8 |
| [EFTA00105868](https://www.justice.gov/epstein/files/DataSet%209/EFTA00105868.pdf) | DS9 |

Statutes cited: **18 U.S.C. sections 1591** (sex trafficking), **1594(c)** (conspiracy to commit sex trafficking), and **2422(b)** (coercion/enticement of minor to travel for illegal sexual activity).

The cover letter ([EFTA00022527](https://www.justice.gov/epstein/files/DataSet%208/EFTA00022527.pdf), page 0) notes: *"Please note that this is an expedited request for a time-sensitive matter."*

---

## 2. The 27 Demand Clauses

The rider specifies records for **Jeffrey Epstein** (DOB 01/20/53, SSN 090-44-3348) and any "related or affiliated accounts," covering the period **January 1, 2010 to the present** (July 2019).

The rider instructs Deutsche Bank to include *"related or affiliated accounts identified by name, address, Social Security Number(s), Employer Identification Number(s), driver's license number(s), financial account number(s), corporate/d.b.a records, Tax Identification Number(s), internal investigative findings or other means."*

### Clauses 1-9 (Parsed by PQG)

| # | Demand | PQG Data Class |
|---|--------|---------------|
| 1 | KYC filings, submissions, forms, requests, supplements, Q&A | bank_records |
| 2 | Account opening/closing records, applications, signature cards, ID, corporate resolutions | bank_records |
| 3 | Monthly or periodic statements and/or transcripts | bank_records |
| 4 | Signature cards and documents reflecting authorized individuals | bank_records |
| 5 | Names, addresses, SSNs, and/or EINs of all account holders | identification |
| 6 | Loan and/or lines of credit applications and files | bank_records |
| 7 | All deposit and withdrawal items | bank_records |
| 8 | Deposit records including slips, items deposited, source of funds documentation | bank_records |
| 9 | Withdrawal/deposit records including drafts, wire transfers, destination/disposition of funds | bank_records |

### Clauses 10-27 (Not Parsed by PQG — extracted from raw document text)

| # | Demand |
|---|--------|
| 10 | Cancelled checks (front and back) |
| 11 | Debit and credit memoranda and related documents |
| 12 | All cashier's checks, bank checks, teller checks, certified checks, money orders, traveler's checks |
| 13 | Credit card accounts |
| 14 | Loan files including applications, financial statements, credit reports, appraisals, promissory notes, mortgages, security agreements, repayment records |
| 15 | Safe deposit records including applications, signature cards, access records |
| 16 | Currency transaction reports (IRS Forms 4789) and regulatory/law enforcement reports |
| 17 | Account opening documents including photocopies of ID, SSN card |
| 18 | All correspondence to/from/relating to accounts or account holders, including recorded customer service calls and correspondence with regulatory/law enforcement authorities |
| 19 | Memoranda, notes, or records of telephone conversations associated with accounts |
| 20 | Internal memoranda and reports |
| 21 | Computer records/logs of communication or attempted communication with the customer |
| 22 | Customer service call logs |
| 23 | Trust accounts |
| 24 | Email addresses associated with accounts/account holders |
| 25 | All surveillance video and/or photographs of transactions |
| 26 | Corporate resolutions, certifications of incorporation, business certificates, partnership agreements |
| 27 | All correspondence (electronic or otherwise) including memoranda, emails, and text messages referencing items 1-26 or financial interests involving the identified individuals/entities |

The full rider text is at [EFTA00022527](https://www.justice.gov/epstein/files/DataSet%208/EFTA00022527.pdf), pages 2-3.

### PQG Parsing Gap

The PQG's clause decomposition only captured clauses 1-9, missing clauses 10-27 entirely. This means **18 of 27 demand clauses have no fulfillment analysis**. The "28 unfulfilled" figure reported in the investigative gaps table is a per-return metric (9 clauses evaluated against 5 returns = 45 evaluations, of which 28 were marked UNFULFILLED), not a count of 28 unmet demand clauses.

---

## 3. The Production

### Timeline

| Event | Date | Lag |
|-------|------|-----|
| Subpoena issued | July 11, 2019 | — |
| Return date | July 25, 2019 | +14 days |
| Substantive production received | September 29, 2020 | +14 months |
| "Reproduction" transmittals received | December 16-18, 2020 | +17 months |

A 96,019-page production typically requires extensive document review and privilege screening, which may account for some or all of the delay between the return date and actual production.

### Production Detail

| Production | SDNY Bates Range | EFTA Start | Pages | Date Received | Description |
|-----------|-----------------|------------|-------|---------------|-------------|
| Substantive | SDNY_GM_00174967 - SDNY_GM_00270985 | [EFTA00081924](https://www.justice.gov/epstein/files/DataSet%209/EFTA00081924.pdf) | 96,019 | Sep 29, 2020 | "Deutsche Bank records" |
| Reproduction 1 | SDNY_GM_02742184 - SDNY_GM_02742186 | [EFTA00016032](https://www.justice.gov/epstein/files/DataSet%208/EFTA00016032.pdf) | 3 | Dec 18, 2020 | Reproduction, Deutsche Bank materials |
| Reproduction 2 | SDNY_GM_02742184 - SDNY_GM_02742186 | [EFTA00072714](https://www.justice.gov/epstein/files/DataSet%209/EFTA00072714.pdf) | 3 | Dec 18, 2020 | Reproduction, Deutsche Bank materials |
| Reproduction 3 | SDNY_GM_02742184 - SDNY_GM_02742186 | [EFTA00078383](https://www.justice.gov/epstein/files/DataSet%209/EFTA00078383.pdf) | 3 | Dec 16, 2020 | Reproduction, Deutsche Bank materials |
| Reproduction 4 | SDNY_GM_02742184 - SDNY_GM_02742186 | [EFTA00078387](https://www.justice.gov/epstein/files/DataSet%209/EFTA00078387.pdf) | 3 | Dec 18, 2020 | Reproduction, Deutsche Bank materials |
| **Total** | | | **96,031** | | |

The four "Reproduction" returns share the same SDNY Bates range (SDNY_GM_02742184-02742186) but are stored at different EFTA locations. These appear to be cover letters or transmission records, not substantive banking documents.

---

## 4. Clause-Level Fulfillment Analysis

The PQG evaluated clauses 1-9 against 5 returns (the substantive production plus 4 reproduction transmittals). The pattern is consistent:

| Clause | Demand Summary | Fulfilled By | Unfulfilled By | Partial |
|--------|---------------|-------------|----------------|---------|
| 1 | KYC filings | Returns 9, 13 | Returns 10, 11, 12 | — |
| 2 | Account opening/closing | Returns 9, 13 | Returns 10, 11, 12 | — |
| 3 | Monthly statements | Returns 9, 13 | Returns 10, 11, 12 | — |
| 4 | Signature cards/authorized persons | Returns 9, 13 | Returns 10, 11, 12 | — |
| **5** | **Names, addresses, SSNs, EINs** | **None** | **Returns 9-12** | **Return 13** |
| 6 | Loan/credit line files | Returns 9, 13 | Returns 10, 11, 12 | — |
| 7 | Deposit/withdrawal items | Returns 9, 13 | Returns 10, 11, 12 | — |
| 8 | Deposit slips/source of funds | Returns 9, 13 | Returns 10, 11, 12 | — |
| 9 | Wire transfers/fund destinations | Returns 9, 13 | Returns 10, 11, 12 | — |

Returns 10, 11, and 12 are the 3-page Reproduction transmittals, which contain no banking keywords and are consistently marked UNFULFILLED. This is expected — they are cover letters, not substantive records.

Returns 9 and 13 correspond to pages within the substantive production. These fulfilled 8 of 9 evaluated clauses.

**Clause 5 is the sole exception.** The demand for "names, addresses, social security numbers, and/or employer identification numbers of all account holders" received only PARTIAL fulfillment from the substantive production — 2 of 20 sampled pages contained identification-related keywords (at [EFTA00081933](https://www.justice.gov/epstein/files/DataSet%209/EFTA00081933.pdf):p3 and [EFTA00081937](https://www.justice.gov/epstein/files/DataSet%209/EFTA00081937.pdf):p3, matching "identification" and "photograph").

---

## 5. Context: The Deutsche Bank Relationship

The subpoena's significance extends beyond its demand-and-response structure. Deutsche Bank's relationship with Epstein is among the most extensively documented in the broader corpus.

From prior investigation reports based on the EFTA corpus:

- **40+ accounts** under RM CODE 82289, including the Haze Trust ($40.5M balance as of August 2018), Southern Financial, Butterfly Trust, and numerous shell entities
- **Same relationship officers** (Jj Litchford, Paul Morris) managed Epstein accounts, Leon Black's Elysium accounts, and other high-value client relationships simultaneously
- Internal KYC documentation showing the bank classified Epstein as "High Risked" while continuing to process transactions
- Internal compliance records including "kyc is not happening" communications and "URGENT - THIRD REQUEST!!!!!" AML escalation messages
- A 25-entity Suspicious Activity Report (SAR) filed on the Epstein account complex

The subpoena's request for "internal memoranda and reports" (Clause 20) and "correspondence with any regulatory or law enforcement authority" (Clauses 18-19) would encompass these compliance records. Whether the production included these categories of records cannot be determined from the PQG data.

---

## 6. What Cannot Be Assessed

1. **Clauses 10-27 have no fulfillment analysis.** The PQG did not parse these 18 demands into its evaluation pipeline. Whether Deutsche Bank produced cancelled checks, credit card records, safe deposit access logs, currency transaction reports, internal memoranda, customer service call logs, trust account records, or surveillance footage cannot be determined from the PQG data alone.

2. **The 96,019-page production has not been comprehensively sampled.** The PQG's fulfillment scoring used 20-page samples. For a 96,019-page production, this represents a 0.02% sample rate. The production likely contains material responsive to many unfulfilled clauses that the sampling algorithm missed.

3. **The scope of "related or affiliated accounts" is unknown.** The rider requested all accounts associated with Epstein, including through corporate/d.b.a. records and "internal investigative findings." Whether Deutsche Bank identified and produced records for the full constellation of Epstein-related entities under RM CODE 82289 — or only the accounts directly in Epstein's name — cannot be determined without reviewing the production cover letter.

4. **The 14-month production delay is not explained** in the available records. Whether this reflects the volume of responsive records, internal legal review, negotiations with prosecutors, or resistance to production is not documented in the corpus.

---

## 7. Investigative Gaps

The PQG flagged 4 investigative gaps for Deutsche Bank, all identical (one per subpoena copy):

- **Gap Type**: PARTIAL_RESPONSE
- **Severity**: HIGH
- **Description**: "16 clauses fulfilled, 28 unfulfilled, 1 partial. Missing data classes: bank_records, identification."

As noted in Section 2, the "28 unfulfilled" count reflects per-return evaluations (clauses × returns), not 28 distinct unmet demands. The actual gap is narrower: Clause 5 (identification) is partially unfulfilled, and clauses 10-27 are unevaluated.

---

## Verification Instructions

- Subpoena and rider: [EFTA00022527](https://www.justice.gov/epstein/files/DataSet%208/EFTA00022527.pdf) (6 pages: cover letter, subpoena face, rider pages 1-2, non-disclosure request, custodian declaration)
- Substantive production begins at: [EFTA00081924](https://www.justice.gov/epstein/files/DataSet%209/EFTA00081924.pdf)
- Reproduction transmittals: [EFTA00016032](https://www.justice.gov/epstein/files/DataSet%208/EFTA00016032.pdf), [EFTA00072714](https://www.justice.gov/epstein/files/DataSet%209/EFTA00072714.pdf), [EFTA00078383](https://www.justice.gov/epstein/files/DataSet%209/EFTA00078383.pdf), [EFTA00078387](https://www.justice.gov/epstein/files/DataSet%209/EFTA00078387.pdf)
- Fulfillment evidence pages: [EFTA00081933](https://www.justice.gov/epstein/files/DataSet%209/EFTA00081933.pdf):p3 (identification keywords), [EFTA00081937](https://www.justice.gov/epstein/files/DataSet%209/EFTA00081937.pdf):p3 (photograph match)

---

*This dossier is part of the Prosecutorial Query Graph Lines of Investigation series. See [00_INDEX.md](00_INDEX.md) for methodology and the complete list of dossiers.*
