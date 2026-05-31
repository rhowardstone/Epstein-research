# Dossier 02: The 27 Redacted Targets

## Who Are the Entities Behind the Fully-Redacted Subpoena Targets?

*Part of the [Prosecutorial Query Graph: Lines of Investigation](./00_INDEX.md)*
*Generated: 2026-02-15*
*Source: prosecutorial_query_graph.db (257 subpoenas, 2,018 demand clauses)*

---

## Executive Summary

Twenty-nine subpoenas in the DOJ production have redacted, null, or empty target fields. Two of these are not actually subpoenas (an email and an FBI weekly report mis-classified by the extraction pipeline), leaving **27 genuine subpoenas with concealed targets**.

These 27 subpoenas contain a combined 334 demand clauses across 408 pages. None has any matched return in the production — every clause is scored UNKNOWN for fulfillment. Two documents stand out by volume: [EFTA01688067](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01688067.pdf) (246 pages containing 16 separate rider blocks, each to a different redacted individual) and [EFTA01227226](https://www.justice.gov/epstein/files/DataSet%209/EFTA01227226.pdf) (100 pages, an FBI forfeiture subfile referencing Epstein's USVI corporate entities).

Despite the identity redactions, structural analysis of the rider clauses, statutes cited, dates, and page counts reveals that these subpoenas fall into at least seven distinct functional clusters. The rider text, statute citations, and temporal context often reveal the *category* of target even when the name is hidden.

---

## The 27 Redacted Subpoenas

| # | EFTA | Date (OCR) | Pages | Clauses | Statutes | Cluster |
|---|------|------------|-------|---------|----------|---------|
| 1 | [EFTA00018874](https://www.justice.gov/epstein/files/DataSet%208/EFTA00018874.pdf) | Aug 28, 2019 | 2 | 8 | 371, 1001, 1519 | A |
| 2 | [EFTA00018955](https://www.justice.gov/epstein/files/DataSet%208/EFTA00018955.pdf) | Aug 15, 2019 | 2 | 8 | 371, 1001, 1519 | A |
| 3 | [EFTA00079989](https://www.justice.gov/epstein/files/DataSet%209/EFTA00079989.pdf) | Aug 5, 2019 | 4 | 1 | — | Misc |
| 4 | [EFTA00080523](https://www.justice.gov/epstein/files/DataSet%209/EFTA00080523.pdf) | Jul 8, 2020 | 4 | 7 | — | C |
| 5 | [EFTA00092639](https://www.justice.gov/epstein/files/DataSet%209/EFTA00092639.pdf) | Jul 7, 2020 | 4 | 7 | — | C |
| 6 | [EFTA00092821](https://www.justice.gov/epstein/files/DataSet%209/EFTA00092821.pdf) | Aug 15, 2019 | 2 | 8 | 371, 1001, 1519 | A |
| 7 | [EFTA00092823](https://www.justice.gov/epstein/files/DataSet%209/EFTA00092823.pdf) | Aug 15, 2019 | 2 | 8 | 371, 1001, 1519 | A |
| 8 | [EFTA00092825](https://www.justice.gov/epstein/files/DataSet%209/EFTA00092825.pdf) | Aug 15, 2019 | 2 | 8 | 371, 1001, 1519 | A |
| 9 | [EFTA00092827](https://www.justice.gov/epstein/files/DataSet%209/EFTA00092827.pdf) | Aug 15, 2019 | 2 | 8 | 371, 1001, 1519 | A |
| 10 | [EFTA00092829](https://www.justice.gov/epstein/files/DataSet%209/EFTA00092829.pdf) | Aug 15, 2019 | 2 | 8 | 371, 1001, 1519 | A |
| 11 | [EFTA00092831](https://www.justice.gov/epstein/files/DataSet%209/EFTA00092831.pdf) | Aug 15, 2019 | 2 | 8 | 371, 1001, 1519 | A |
| 12 | [EFTA00092833](https://www.justice.gov/epstein/files/DataSet%209/EFTA00092833.pdf) | Aug 15, 2019 | 2 | 8 | 371, 1001, 1519 | A |
| 13 | [EFTA00092835](https://www.justice.gov/epstein/files/DataSet%209/EFTA00092835.pdf) | Aug 15, 2019 | 2 | 8 | 371, 1001, 1519 | A |
| 14 | [EFTA00092837](https://www.justice.gov/epstein/files/DataSet%209/EFTA00092837.pdf) | Aug 15, 2019 | 2 | 8 | 371, 1001, 1519 | A |
| 15 | [EFTA00092839](https://www.justice.gov/epstein/files/DataSet%209/EFTA00092839.pdf) | Aug 15, 2019 | 2 | 8 | 371, 1001, 1519 | A |
| 16 | [EFTA00092845](https://www.justice.gov/epstein/files/DataSet%209/EFTA00092845.pdf) | Aug 15, 2019 | 2 | 8 | 371, 1001, 1519 | A |
| 17 | [EFTA00092847](https://www.justice.gov/epstein/files/DataSet%209/EFTA00092847.pdf) | Aug 15, 2019 | 2 | 8 | 371, 1001, 1519 | A |
| 18 | [EFTA00123525](https://www.justice.gov/epstein/files/DataSet%209/EFTA00123525.pdf) | Aug 30, 2019 | 4 | 2 | 1791, 201 | D |
| 19 | [EFTA00123547](https://www.justice.gov/epstein/files/DataSet%209/EFTA00123547.pdf) | Aug 12, 2019 | 2 | 9 | 371, 1001, 1519 | B |
| 20 | [EFTA00123549](https://www.justice.gov/epstein/files/DataSet%209/EFTA00123549.pdf) | Aug 12, 2019 | 2 | 9 | 371, 1001, 1519 | B |
| 21 | [EFTA00123551](https://www.justice.gov/epstein/files/DataSet%209/EFTA00123551.pdf) | Aug 12, 2019 | 2 | 9 | 371, 1001, 1519 | B |
| 22 | [EFTA00153628](https://www.justice.gov/epstein/files/DataSet%209/EFTA00153628.pdf) | Jan 23, 2020 | 4 | 4 | — | G |
| 23 | [EFTA00172165](https://www.justice.gov/epstein/files/DataSet%209/EFTA00172165.pdf) | Sep 9, 2020 | 3 | 7 | 841, 846, 201, 1791, 1956 | E |
| 24 | [EFTA01227226](https://www.justice.gov/epstein/files/DataSet%209/EFTA01227226.pdf) | Jun 24, 2019 | 100 | 13 | — | F |
| 25 | [EFTA01688067](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01688067.pdf) | Aug 15, 2019 | 246 | 128 | 371, 1001, 1519 | H |
| 26 | [EFTA02729866](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02729866.pdf) | Aug 12, 2019 | 2 | 9 | 371, 1001, 1519 | B |
| 27 | [EFTA02729868](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02729868.pdf) | Aug 12, 2019 | 2 | 9 | 371, 1001, 1519 | B |

**Excluded (mis-classified):**
- [EFTA00074084](https://www.justice.gov/epstein/files/DataSet%209/EFTA00074084.pdf): Email about USAA & AMEX Maxwell subpoenas (Dec 11, 2019), not a subpoena
- [EFTA01655033](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01655033.pdf): FBI forensic accountant weekly report (May 6, 2021), not a subpoena

---

## Cluster Analysis

### Cluster A: Individual Witnesses — "All Materials Relating to Jeffrey Epstein"

**Subpoenas:** 14 standalone + 16 within [EFTA01688067](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01688067.pdf) = up to **30 individuals**
**Statutes:** 18 U.S.C. 371 (Conspiracy), 1001 (False Statements), 1519 (Obstruction / Document Destruction)
**Dates:** August 15–28, 2019 (5–18 days after Epstein's death)
**Appearance dates:** August 20, 2019 at 10:00 a.m.
**Signed by:** Geoffrey S. Berman, United States Attorney

This is the largest cluster. All share an identical 8-clause structure:

| Clauses | Content |
|---------|---------|
| 1–4 | **Advice of Rights** — right to refuse self-incriminating answers, right to counsel, right to appointed counsel |
| 5–6 | **Document production scope** — all responsive documents including computers, email, iCloud, servers, cellphones, foreign jurisdictions |
| 7 | **Privilege log** — any withheld documents must be logged with dates, authors, recipients, subject matter |
| 8 | **"All materials relating to Jeffrey Epstein"** — text messages, emails, social media, documents, notes |

The Advice of Rights (clauses 1–4) is significant: it is read to individual witnesses or potential targets, not to corporations. These subpoenas were issued to people, not institutions.

The 12 consecutive EFTA numbers ([EFTA00092821](https://www.justice.gov/epstein/files/DataSet%209/EFTA00092821.pdf)–00092847, skipping even numbers) suggest a batch issuance — likely 12 individuals subpoenaed on the same day in a coordinated action.

The statutes cited — conspiracy, false statements, and obstruction — indicate the grand jury was investigating potential interference with the Epstein case, not the underlying trafficking offenses (which would cite 18 U.S.C. 1591/1594).

#### The 246-Page Compilation: [EFTA01688067](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01688067.pdf)

[EFTA01688067](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01688067.pdf) is a 246-page compilation document. Its first page is an FBI FD-302 (investigative report) dated October 9, 2019, describing a letter returned to MCC marked "J. Epstein, Manhattan Correctional, NYC NY 10007," addressed to **Larry Nassar** at a Federal Bureau of Prisons facility in Tucson, Arizona. The letter was postmarked August 13, 2019 — three days after Epstein's death. According to the FBI, the stamp and stationery were "not available for purchase at MCC" and "there were no logs kept regarding incoming or outgoing mail for Jeffrey Epstein."

Following the FD-302, the document contains 16 separate Grand Jury Subpoena riders, each to a different redacted individual. OCR of the divider pages between riders captures partial name fragments:

| Block | OCR Fragment |
|-------|-------------|
| 1 | "Grand Jury Subpoena to**a**, dated August 15, 2019" |
| 2 | "Grand Jury Subpoena to **I.** dated August 15, 2019" |
| 3 | "Grand Jury Subpoena to **E. a** dated August 15, 2019" |
| 4 | "Grand Jury Subpoena to**la** dated August 15, 2019" |
| 5 | "Grand Jury Subpoena **KAM.** dated August 15, 2019" |
| 6 | "Grand Jury Subpoena t**e** dated August 15, 2019" |
| 7 | "Grand Jury Subpoena t**a**, dated August 15, 2019" |
| 8 | "Grand Jury Subpoena t**e** dated August 15, 2019" |
| 9–16 | Further fragments, mostly single characters |

These OCR fragments are artifacts of partial redaction and are insufficient for identification, but they confirm that each block targets a distinct individual.

### Cluster B: Death-Night Location Subpoenas

**Subpoenas:** 5 ([EFTA00123547](https://www.justice.gov/epstein/files/DataSet%209/EFTA00123547.pdf), [EFTA00123549](https://www.justice.gov/epstein/files/DataSet%209/EFTA00123549.pdf), [EFTA00123551](https://www.justice.gov/epstein/files/DataSet%209/EFTA00123551.pdf), [EFTA02729866](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02729866.pdf), [EFTA02729868](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02729868.pdf))
**Statutes:** 18 U.S.C. 371, 1001, 1519
**Date:** August 12, 2019 (2 days after Epstein's death)
**Appearance date:** August 16, 2019

These subpoenas add a ninth clause to the standard 8-clause template:

> "All materials regarding, and sufficient to establish, **your location and activities** between [start time] on August 9, 2019 and 12 p.m. on August 10, 2019, including but not limited to any texts, emails, or communications sent or received during that time period, and any location or GPS data reflecting your location during that time period."

The time windows vary across the five subpoenas:

| EFTA | Start Time | End Time |
|------|------------|----------|
| [EFTA00123547](https://www.justice.gov/epstein/files/DataSet%209/EFTA00123547.pdf) | 4:00 p.m., Aug 9 | 12:00 p.m., Aug 10 |
| [EFTA00123549](https://www.justice.gov/epstein/files/DataSet%209/EFTA00123549.pdf) | 2:00 p.m., Aug 9 | 12:00 p.m., Aug 10 |
| [EFTA00123551](https://www.justice.gov/epstein/files/DataSet%209/EFTA00123551.pdf) | 8:00 a.m., Aug 9 | 12:00 p.m., Aug 10 |
| [EFTA02729866](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02729866.pdf) | 2:00 p.m., Aug 9 | 12:00 p.m., Aug 10 |
| [EFTA02729868](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02729868.pdf) | 8:00 a.m., Aug 9 | 12:00 p.m., Aug 10 |

[EFTA02729866](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02729866.pdf) duplicates the time window of [EFTA00123549](https://www.justice.gov/epstein/files/DataSet%209/EFTA00123549.pdf); [EFTA02729868](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02729868.pdf) duplicates [EFTA00123551](https://www.justice.gov/epstein/files/DataSet%209/EFTA00123551.pdf). These may represent duplicate filings (the DS12 copies are the later-released versions). If so, three distinct individuals were subpoenaed, each covering a different shift or access window around the night of Epstein's death.

The varying start times (8 a.m., 2 p.m., 4 p.m.) suggest the targets had different roles or schedules relative to MCC operations on August 9–10, 2019. The end time is uniform (noon August 10), consistent with the approximate time Epstein's body was found.

### Cluster C: Property Transaction — Granite Reality LLC / Bradford, NH

**Subpoenas:** 2 ([EFTA00080523](https://www.justice.gov/epstein/files/DataSet%209/EFTA00080523.pdf), [EFTA00092639](https://www.justice.gov/epstein/files/DataSet%209/EFTA00092639.pdf))
**Date:** July 7–8, 2020
**Target:** Attorneys (redacted names)
**Signed by:** Audrey Strauss

Both subpoenas demand documents relating to a property purchase in Bradford, New Hampshire by "Granite Reality, LLC" (or "Granite Realty, LLC"). The rider specifies:

> "All non-privileged documents relating to the Transaction, including, without limitation: (a) any and all financial records, including records related to any and all transfers of funds; (b) any and all title records; (c) any and all closing documents; (d) any and all records regarding the ownership of the Property; (e) any and all records related to the formation of any limited liability companies or trusts; and **(f) any and all records related to or referencing Ghislaine Maxwell.**"

The explicit reference to Ghislaine Maxwell and the Bradford, NH location connect these subpoenas to Maxwell's arrest at a 156-acre property in Bradford, New Hampshire on July 2, 2020 — five to six days before these subpoenas were issued.

### Cluster D: MCC Guards — Noel & Thomas via Credit Bureau

**Subpoena:** 1 ([EFTA00123525](https://www.justice.gov/epstein/files/DataSet%209/EFTA00123525.pdf))
**Statutes:** 18 U.S.C. 1791 (Contraband in Prison), 201 (Bribery)
**Date:** August 30, 2019
**Target:** Experian Consumer Affairs (Rick Haas, Custodian of Records)
**Appearance:** September 13, 2019

This subpoena requests credit reports for two named individuals:

- **Tova A. Noel** (DOB and SSN redacted)
- **Michael A. Thomas** (DOB and SSN redacted)

Noel and Thomas were the two MCC correctional officers assigned to Epstein's unit on the night of his death. Both were later charged with falsifying prison records (United States v. Noel, 19-cr-830, SDNY). The credit-bureau subpoena indicates investigators examined their financial records for evidence of bribery or unexplained income.

### Cluster E: MCC Employee "Benson" — Drug Trafficking Investigation

**Subpoena:** 1 ([EFTA00172165](https://www.justice.gov/epstein/files/DataSet%209/EFTA00172165.pdf))
**Statutes:** 21 U.S.C. 841 (Drug Trafficking), 846 (Drug Conspiracy); 18 U.S.C. 201 (Bribery), 1791 (Contraband), 1956 (Money Laundering)
**Date:** September 9, 2020
**Signed by:** Audrey Strauss

This subpoena targets a pseudonymous MCC employee referred to as "Benson" and demands:

- All text messages, emails, iMessages, and WhatsApp messages with any MCC inmate
- All communications with any MCC employee
- All records of bank accounts, credit cards, and peer-to-peer money transfer accounts

The statute combination — drug trafficking, bribery, contraband, and money laundering — indicates this subpoena relates to criminal activity within MCC, potentially connected to the broader investigation of conditions at the facility where Epstein died. The personal appearance requirement and the specificity of the communication demands suggest "Benson" was a target, not merely a witness.

### Cluster F: USVI Corporate Entities — Forfeiture

**Subpoena:** 1 ([EFTA01227226](https://www.justice.gov/epstein/files/DataSet%209/EFTA01227226.pdf))
**Date:** August 7, 2019 (rider date); June 24, 2019 (FBI EC opening forfeiture subfile)
**Case ID:** 31E-NY-3027571-FF — "EPSTEIN, JEFFREY; CHILD SEX TRAFFICKING"
**Pages:** 100

This 100-page document opens with an FBI Electronic Communication requesting a forfeiture subfile, then demands corporate records for three USVI entities:

- **Maple, Inc.** — 9100 Havensight, Port of Sales, Suite 15/16, St. Thomas 00802, USVI
- **Laurel, Inc.** — same address
- **Nautilus, Inc.** — same address

Maple, Inc. is identified on page 2 as the owner of **9 East 71st Street, New York, NY 10021** — Epstein's Manhattan mansion. The subpoena requests articles of incorporation, officer/director/owner identification, and regularly filed statements for each entity.

The shared address (9100 Havensight, Suite 15/16) places all three entities at Epstein's St. Thomas office complex — the same location associated with multiple Epstein shell companies documented elsewhere in the production.

### Cluster G: Airline Records — Maxwell Travel

**Subpoena:** 1 ([EFTA00153628](https://www.justice.gov/epstein/files/DataSet%209/EFTA00153628.pdf))
**Date:** January 23, 2020
**Target:** American Airlines, Corporate Security (Ft. Worth, TX)

This subpoena requests travel records for:

> "Ghislaine Maxwell, a/k/a Ghislaine Borgerson"

across two date ranges:
- January 1, 1994 through December 31, 1998
- July 1, 2019 through date of service

The 1994–1998 window covers the period of Maxwell's most active involvement in Epstein's operations. The 2019 window covers the period after Epstein's arrest and death, when Maxwell was evading law enforcement before her July 2020 arrest.

---

## Aggregate Statistics

### Returns and Fulfillment

| Metric | Value |
|--------|-------|
| Total redacted subpoenas | 27 |
| Total demand clauses | 334 |
| Matched returns | **0** |
| Fulfillment status: UNKNOWN | 334 (100%) |

No redacted-target subpoena has any identifiable return in the production. This is a structurally inevitable result: without knowing the target, entity-based matching cannot be performed. The PQG's four matching strategies (explicit reference, concordance cross-reference, entity-temporal matching, content keyword matching) all require an identifiable target name.

### Date Distribution

| Date (from OCR) | Count |
|-----------------|-------|
| August 5, 2019 | 1 |
| August 12, 2019 | 5 |
| August 15, 2019 | 14 |
| August 28, 2019 | 1 |
| August 30, 2019 | 1 |
| January 23, 2020 | 1 |
| June 24, 2019 | 1 |
| July 7–8, 2020 | 2 |
| September 9, 2020 | 1 |

Twenty-two of 27 redacted subpoenas cluster in August 2019 — the month of Epstein's death and the most intense subpoena activity in the entire production.

### Statute Distribution

| Statute | Count | Purpose |
|---------|-------|---------|
| 18 U.S.C. 371 | 22 | Conspiracy |
| 18 U.S.C. 1001 | 22 | False Statements |
| 18 U.S.C. 1519 | 22 | Obstruction / Document Destruction |
| 18 U.S.C. 201 | 2 | Bribery |
| 18 U.S.C. 1791 | 2 | Contraband in Prison |
| 18 U.S.C. 1956 | 1 | Money Laundering |
| 21 U.S.C. 841 | 1 | Drug Trafficking |
| 21 U.S.C. 846 | 1 | Drug Conspiracy |

The dominant statute pattern (371/1001/1519) indicates the grand jury was focused on **obstruction and cover-up**, not on the underlying sex-trafficking charges (18 U.S.C. 1591/1594). The two correctional-specific subpoenas (Clusters D and E) cite bribery and contraband statutes, consistent with investigating corruption at MCC.

---

## Structural Observations

1. **The redacted subpoenas are overwhelmingly directed at individuals, not institutions.** The Advice of Rights clauses (right to refuse self-incriminating testimony, right to counsel) appear in 22 of 27 subpoenas. These clauses are constitutionally required when subpoenaing individuals who may themselves be targets or subjects.

2. **The demand pattern is broad but unspecific.** Unlike the institutional subpoenas (which demand account records, transaction histories, or call detail records), the individual subpoenas demand "all materials relating to Jeffrey Epstein" without data-class specificity. This is consistent with early-stage investigation of persons whose connection to the case was known but whose specific role was not yet characterized.

3. **The August 15, 2019 batch is the largest coordinated subpoena action in the production.** Between the 12 consecutive standalone subpoenas ([EFTA00092821](https://www.justice.gov/epstein/files/DataSet%209/EFTA00092821.pdf)–00092847) and the 16 riders compiled in [EFTA01688067](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01688067.pdf), up to 28 individuals were subpoenaed on the same date — five days after Epstein's death. All cite obstruction statutes.

4. **The death-night location subpoenas target three distinct time windows.** The varying start times (8 a.m., 2 p.m., 4 p.m.) with a uniform end time (noon August 10) suggest the targets had different shift schedules or access periods relative to MCC operations.

5. **The Granite Reality / Bradford, NH subpoenas connect to Maxwell's arrest.** Issued 5–6 days after Maxwell's July 2, 2020 arrest at a Bradford, NH property, these subpoenas explicitly demand records "related to or referencing Ghislaine Maxwell."

6. **Zero returns for any redacted subpoena.** This is first and foremost a structural limitation: the PQG's matching strategies require an identifiable target name, and redacted targets cannot be matched to returns. Beyond this, returns may have been produced under seal or through separate case numbers not included in the public release. Non-compliance remains a possibility but cannot be distinguished from these other explanations using the available data.

---

## Open Questions

- **Who are the 28+ individuals subpoenaed on August 15, 2019?** The Advice of Rights language is consistent with these individuals being classified as subjects or targets under DOJ guidelines, though this language is sometimes used prophylactically for witnesses as well. Were they MCC staff, Epstein associates, or both?
- **Were returns produced under seal?** The complete absence of matched returns for all 27 subpoenas may indicate that responses were filed separately and not included in the public DOJ production.
- **What is the content of [EFTA01227226](https://www.justice.gov/epstein/files/DataSet%209/EFTA01227226.pdf)'s remaining 97 pages?** Only the first 3 pages (FBI EC and property identification) are characterized in the research data. The remaining pages of this 100-page forfeiture document likely contain additional corporate entity records.
- **Was "Benson" charged?** The drug trafficking and money laundering statutes in the MCC employee subpoena indicate a serious criminal investigation. Public records do not clarify whether this investigation resulted in prosecution.

---

## Verification Instructions

Key verification targets:

- **Cluster A template:** Open any of [EFTA00092821](https://www.justice.gov/epstein/files/DataSet%209/EFTA00092821.pdf)–[EFTA00092847](https://www.justice.gov/epstein/files/DataSet%209/EFTA00092847.pdf) to confirm the 8-clause Advice of Rights + "all materials" structure
- **Death-night time windows:** [EFTA00123547](https://www.justice.gov/epstein/files/DataSet%209/EFTA00123547.pdf) (clause 9), [EFTA00123549](https://www.justice.gov/epstein/files/DataSet%209/EFTA00123549.pdf) (clause 9), [EFTA00123551](https://www.justice.gov/epstein/files/DataSet%209/EFTA00123551.pdf) (clause 9)
- **Nassar letter FD-302:** [EFTA01688067](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01688067.pdf), page 1
- **Forfeiture / Maple Inc.:** [EFTA01227226](https://www.justice.gov/epstein/files/DataSet%209/EFTA01227226.pdf), pages 1–2
- **Noel & Thomas credit reports:** [EFTA00123525](https://www.justice.gov/epstein/files/DataSet%209/EFTA00123525.pdf)
- **"Benson" drug investigation:** [EFTA00172165](https://www.justice.gov/epstein/files/DataSet%209/EFTA00172165.pdf)
- **Maxwell travel / Granite Reality:** [EFTA00153628](https://www.justice.gov/epstein/files/DataSet%209/EFTA00153628.pdf), [EFTA00080523](https://www.justice.gov/epstein/files/DataSet%209/EFTA00080523.pdf)

---

*Previous: [Dossier 01: The 524-Day Subpoena Gap](./01_TEMPORAL_BLACKOUT.md)*
*Next: [Dossier 03: Tech Company Production Gaps](./03_TECH_COMPANY_GAPS.md)*
