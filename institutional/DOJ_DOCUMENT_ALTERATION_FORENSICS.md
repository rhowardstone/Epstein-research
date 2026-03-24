# DOJ Document Alteration Forensics: How "Victim Privacy" Became a Blanket Redaction Tool

## A forensic analysis of 42,782 re-processed EFTA documents

**Updated**: March 5, 2026
**Scope**: All 42,782 altered files identified across DOJ EFTA datasets 1-12
**Pipeline**: Word-level diffing, pixel-diff visual verification (86,979 pages), page-level LLM classification (152,312 change units)
**Databases**: [`alteration_results.db`](https://github.com/rhowardstone/Epstein-research-data/releases) (8.2 GB, 212,730 change units), [`full_text_corpus.db`](https://github.com/rhowardstone/Epstein-research-data/releases) (6.3 GB, 1.38M documents)

---

## 1. Executive Summary

Between the January 30, 2026 release and the present, the Department of Justice re-processed **42,782 documents** in its Epstein Files Transparency Act (EFTA) production. Our forensic pipeline compared the original archived PDFs against the currently-hosted versions, classifying every individual change at page level.

Of **152,312 classified change units**, only **2.6% were defensible victim PII** redactions. The DOJ removed **16 times more non-PII content than victim-protective content**. Nearly half of all changes (46.9%) were classified as outright content removal — substantive text degraded or visually redacted from the record with no PII basis.

The changes fall into two distinct categories. **Visual redactions** — black bars, page blackouts, and content physically removed from the rendered page — are provable: anyone can compare the original and current PDFs side by side. **Text-layer degradation** — where the visible page appears identical but the invisible OCR text layer has been corrupted or altered — affects searchability: a researcher looking for a keyword will not find these pages even though the content is visually present. Both categories are documented below, and every cited document has been visually verified to distinguish between them.

Among the visual redactions: the DOJ gutted **150+ FinCEN Suspicious Activity Reports**, removing banking intelligence showing Epstein's attorney structuring cash withdrawals below the $10,000 reporting threshold. It applied new black-bar redactions to scheduling emails, stripping every phone number while leaving public figure names visible. It blacked out an entire page of a Gates Foundation internal email found in Epstein's files. It added redaction bars over co-conspirator names in NPA immunity clauses, prosecutor names in legal filings, and victim names in civil complaints.

Among the text-layer degradation: **1,452,264 characters** degraded from Ghislaine Maxwell's American Express Centurion card statements — public trial exhibits from *US v. Maxwell*. The searchable text from Epstein's **entire BOP psychological file** at MCC New York was degraded, including the suicide risk assessment that reads: *"It is unclear at this time if Mr. Epstein had placed the string around his own neck."* An additional **27,026 pages** across the corpus had their invisible text layer degraded while the visible page remained unchanged — rendering them invisible to keyword search.

Cross-document analysis reveals systematic name-scrubbing campaigns targeting specific public figures — confirmed by visual black-bar redactions in legal filings and scheduling emails, and by text-layer degradation in FBI 302s and financial records. The EFTA explicitly prohibits withholding for "embarrassment, reputational harm, or political sensitivity."
The mechanism: the DOJ's own [Attorney Review Protocol](https://www.justice.gov/media/1426281/dl) (January 4, 2026) establishes a dual-track redaction system. Track one covers victim PII under the EFTA's narrow statutory authority. Track two invokes the **Privacy Act** as a separate, blanket basis for stripping telephone numbers, names, and more from *all persons* — not just victims. The EFTA does not enumerate the Privacy Act among its five permitted withholding categories. No Federal Register justification for this expanded authority has been published.

---

## 2. What the Law Says vs. What the DOJ Did

### The EFTA's Five Permitted Withholding Categories

The Epstein Files Transparency Act (Pub. L. 119-38, 139 Stat. 656) enumerates exactly five categories of information that may be withheld or redacted. Quoting Section 2(c)(1), as reproduced in the DOJ's own [production letter](https://www.justice.gov/opa/media/1426091/dl):

> *"(A) contain personally identifiable information of victims or victims' personal and medical files and similar files the disclosure of which would constitute a clearly unwarranted invasion of personal privacy; (B) depict or contain child sexual abuse materials (CSAM) as defined under 18 U.S.C. 2256 and prohibited under 18 U.S.C. 2252-2252A; (C) would jeopardize an active federal investigation or ongoing prosecution, provided that such withholding is narrowly tailored and temporary; [or] (D) depict or contain images of death, physical abuse, or injury of any person."*

The fifth category — (E), information classified under Executive order for national defense or foreign policy — exists in the statute but the DOJ stated no files are being withheld on that basis.

The statute also prohibits redaction on certain grounds. Section 2(b):

> *"No record shall be withheld, delayed, or redacted on the basis of embarrassment, reputational harm, or political sensitivity, including to any government official, public figure, or foreign dignitary."*

### What the DOJ Portal Says

The DOJ's [Epstein Files portal](https://www.justice.gov/epstein) describes its redaction basis more broadly: *"all reasonable efforts have been made to review and redact personal information pertaining to victims, other private individuals, and protect sensitive materials from disclosure."* The phrase "other private individuals" does not appear in the EFTA's text, which limits PII redaction to "victims" and their "personal and medical files."

### What the Protocol Actually Instructs

The DOJ's [Attorney Review Protocol](https://www.justice.gov/media/1426281/dl) (January 4, 2026) goes further still. Section II.C.1, titled **"Privacy Act Redactions,"** instructs reviewers (Protocol, lines 323-344):

> *"You must also redact PII that may be present in the documents:*
> *- Names of Government employees (AUSAs and DOJ, law enforcement, BOP employees, OIG employees, contractors at USAO/FBI, etc.), except [those in Senate-confirmed positions, public affairs officers, and the two prosecuted BOP guards]*
> *- Names of confidential sources or cooperating witnesses*
> *- Email addresses*
> *- Dates of birth*
> *- Personal street addresses [..., except Epstein's known addresses]*
> *- **Telephone numbers***
> *- Social security numbers (SSN)*
> *- Driver's license numbers, passport numbers, license plate numbers, VINs*
> *- Bank/financial account numbers, credit card numbers*
> *- Other ID numbers (badge number, medical ID number, taxpayer ID number)"*

Brackets indicate exceptions omitted for brevity; the full Protocol text enumerates them. The instruction applies to **all persons** -- not just victims. The telephone number of a former Prime Minister of Norway gets the same treatment as a victim's phone number. The name of every FBI agent, every AUSA, every BOP employee is stripped unless they hold a Senate-confirmed position or are one of the other enumerated exceptions.

The Protocol further instructs specific handling for Epstein and Maxwell (Protocol, lines 347-350):

> *"For Epstein (and any of his entities), redact his SSN and any phone numbers. Do not redact anything else, including his email addresses."*
> *"For Maxwell, do not redact her name but redact the rest of her PII, including her email address(es), and PHI."*

### The Gap

The EFTA's victim PII exception is narrow: it protects "personally identifiable information of *victims*." The Privacy Act redaction track protects the PII of *everyone*. The EFTA does not list the Privacy Act among its five permitted withholding categories. The DOJ acknowledges the distinction by labeling them separately in the Protocol -- Section II.B for "Victim Information," Section II.C.1 for "Privacy Act Redactions."

The question is whether a specific transparency statute, enacted to override normal exemptions, can be supplemented by a general privacy law to achieve broader redaction than the specific statute authorizes. Reasonable legal minds may disagree, but the tension between the two frameworks is evident in the data.

---

## 3. The Smoking Gun: EFTA00339454

[EFTA00339454](https://www.justice.gov/epstein/files/DataSet%209/EFTA00339454.pdf) | [Original (JDrive)](https://jmail.world/drive/vol00009-efta00339454-pdf)

This is Lesley Groff's scheduling email covering September 22 through October 31, 2015. Direct visual comparison of the [original archived PDF](https://jmail.world/drive/vol00009-efta00339454-pdf) against the [current DOJ-hosted version](https://www.justice.gov/epstein/files/DataSet%209/EFTA00339454.pdf) reveals a dual operation: OCR quality improvements combined with PII redaction.

### What the Visual PDFs Show

The current DOJ version contains **visible black-bar redactions** applied directly to the PDF — not just text-layer changes. Every phone number in the schedule has been covered with a black bar. Several private individual names have also been black-bar redacted. Meanwhile, public figure names remain fully visible.

### Phone Numbers: Visual Black-Bar Redactions

| Person | Original (Readable) | Current (Visual) |
|--------|---------------------|------------------|
| Kjell Magne Bondevik (former PM of Norway) | `(011 47 480 82 630)` | **[BLACK BAR]** |
| Woody Allen & Soon-Yi Previn | `(917 402-7204)` | **[BLACK BAR]** |
| Noam & Valeria Chomsky | `(617-697-4348)` | **[BLACK BAR]** |
| Joi Ito (MIT Media Lab) | `(415 290-4618)` | **[BLACK BAR]** |
| Barnaby Marsh (Templeton Foundation) | `(484 919-8677)` | **[BLACK BAR]** |
| Jen Doyle | `(781308-3269)` | **[BLACK BAR]** |
| Justin Nelson | `(917 747-1452)` | **[BLACK BAR]** |
| Dr. Speaker | `(212 832-2020)` | **[BLACK BAR]** |
| Dr. Magnani's office | `212 688 1090` | **[BLACK BAR]** |
| Remi Brazet | `(+33 6 11 11 59 12)` | **[BLACK BAR]** |

Every phone number on the schedule — spanning all six pages, covering ten different people — was redacted with a visual black bar. The names of the public figures remain legible next to the empty parentheses. The text extraction layer reads `()` or `(MM` under these bars, but what a reader sees is a deliberate redaction mark.

### Name Redactions: Private Individuals Only

| Original | Current (Visual) | Context |
|----------|------------------|---------|
| `Jen Doyle` | **[BLACK BAR]** | Private individual, former Epstein employee |
| `Aurelija` | **[BLACK BAR]** | Private individual, travel booking |
| `Maria` (with Valdson) | **[BLACK BAR]** | Private individual |
| `Tess` (with Lyn, Jojo) | **[BLACK BAR]** | Private individual, staff member |
| `Birthday` / `Birthday` (Oct 11, 14) | **[BLACK BAR]** | Likely victim DOBs |

Public figure names — Woody Allen, Bondevik, Chomsky, Joi Ito, Barnaby Marsh, Dr. Speaker, Leon Botstein — are all **fully legible** in the current DOJ version. Only private individuals had their names black-bar redacted.

*Note on text-layer artifacts*: Our automated text extraction pipeline initially flagged apparent name changes — "Woody Allen" extracting as "Roody Allen," "Jen Doyle" as "M." — but visual PDF inspection confirms these are OCR artifacts created when the text extraction layer was re-rendered around the black bars, not what readers see. The visual PDF clearly shows "Woody Allen" in full. However, the text-layer corruption has a practical consequence: anyone performing a full-text search of the current DOJ production for "Woody Allen" will not find this document. The text layer says "Roody Allen." Whether intentional or not, this renders affected documents invisible to keyword search while remaining visually legible to anyone who opens the PDF directly.

### OCR Quality Improvements in the Same Pass

The re-processing also improved text quality, confirming this was a deliberate re-review:

| Original (Archived) | Current (DOJ) |
|---------------------|----------------|
| `From: ==la` (black bar over sender) | `From: Lesley Groff <` (name now visible) |
| `12:40pm & Bebe to arrive STT` | `12:40pm Lesley & Bebe to arrive STT` |
| `Larty Ylsoski` | `Larry Visoski` |
| `Kjell Maine Bondevik` | `Kjell Magne Bondevik` |
| `Julien Ve:glas` | `Julien Verglas` |

The original DOJ release had Lesley Groff's name hidden behind a black bar in the From: field. The current version **restores** her name — the DOJ corrected an over-redaction. Similarly, "12:40pm & Bebe" (Groff's name missing) became "12:40pm Lesley & Bebe." These corrections show the DOJ both *adding* transparency (un-redacting the sender's name) and *restricting* it (redacting phone numbers) in the same re-processing pass.

### Birthday Redactions: Defensible

The birthday entries — "Reminder: Birthday" on Oct 11 and Oct 14 — were replaced with black bars. These are likely victim dates of birth: the names attached to these dates were already redacted from other documents, and removing the date-without-name prevents DOB cross-referencing. This is defensible victim protection.

The birthday redactions demonstrate the DOJ *can* do targeted, contextual victim protection when it chooses to. The blanket phone-number stripping is a separate, broader operation applied on top of the targeted work.

### The Inconsistency That Proves the Pattern

On the same page as the redacted numbers, one entry survived untouched:

> `12:30pm LUNCH w/Yau (617 999-4128)`

Shing-Tung Yau is a Fields Medal-winning mathematician and Harvard professor. His phone number was redacted from a *different* copy of the same schedule ([EFTA02070330](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02070330.pdf) | [Original (JDrive)](https://jmail.world/drive/vol00010-efta02070330-pdf)) — **visually verified: ALL phone numbers on that page confirmed covered with black-bar redactions**, including Yau (617 999-4128), Marvin Minsky (617 935 6235), Martin Nowak (617 496-3999), Valeria's cell (617 697-4348), and others. Names remain visible but every phone number is blacked out. Yet the same Yau entry survives — visually readable, with no black bar — in EFTA00339454. The DOJ's redaction process was inconsistent: it caught the number in one copy but missed it in another.

### Systematic Pattern Across Scheduling Emails

EFTA00339454 is not an isolated case. Seven scheduling emails in the EFTA00339438-00339545 range show identical alteration patterns:

| EFTA | Original Chars | Current Chars | Change | Classification |
|------|---------------|---------------|--------|---------------|
| [EFTA00339438](https://www.justice.gov/epstein/files/DataSet%209/EFTA00339438.pdf) | 2,480 | 2,366 | -4.6% | NAME_REMOVAL |
| [EFTA00339454](https://www.justice.gov/epstein/files/DataSet%209/EFTA00339454.pdf) | 3,607 | 3,436 | -4.7% | NAME_REMOVAL |
| [EFTA00339460](https://www.justice.gov/epstein/files/DataSet%209/EFTA00339460.pdf) | 1,827 | 1,783 | -2.4% | NAME_REMOVAL |
| [EFTA00339474](https://www.justice.gov/epstein/files/DataSet%209/EFTA00339474.pdf) | 3,410 | 3,231 | -5.2% | NAME_REMOVAL |
| [EFTA00339477](https://www.justice.gov/epstein/files/DataSet%209/EFTA00339477.pdf) | 3,730 | 3,444 | -7.7% | NAME_REMOVAL |
| [EFTA00339480](https://www.justice.gov/epstein/files/DataSet%209/EFTA00339480.pdf) | 3,801 | 3,524 | -7.3% | NAME_REMOVAL |
| [EFTA00339545](https://www.justice.gov/epstein/files/DataSet%209/EFTA00339545.pdf) | 7,533 | 7,568 | +0.5% | NAME_REMOVAL |

Every email in the thread had the same treatment: phone numbers black-bar redacted, private individual names redacted. In one variant, even a child's name ("Ty" in "Ty's football game") was redacted.

---

## 4. The FinCEN SAR Gutting

The Protocol's instruction for Suspicious Activity Reports is explicit and total (Protocol, lines 389-390):

> *"SARs: redact; choose 'z_Redacted in Full' and make a note of it in the 'RN-Redaction' freeform text field."*

Our pipeline identified **156 separate FinCEN SAR documents** in the EFTA01650000-01660000 range with substantive content stripped — over **300,000 characters** of banking intelligence removed across 1,533 change units.

### What the SARs Contained

These are not abstractions. The stripped narratives describe specific financial crimes:

**Deutsche Bank — BSA: 31000150359182**: Epstein's attorney Darren Indyke *"has routinely cashed a $7,500 check"* from Epstein's account on a monthly basis. Deutsche Bank flagged this as **structured transactions** — deliberate splitting below the $10,000 Currency Transaction Report threshold. A companion filing (BSA: 31000092290333) documented Indyke bringing *two* checks to the teller window: $7,500 from Epstein's account plus $4,000 from Indyke's attorney account — *"structured at $11,500 split across two accounts."* A third filing (BSA: 31000110544793) noted Deutsche Bank had *"previously filed CTRs on the cash withdrawal activities of Indyke exceeding $10,000 on 05/28/2014, 02/16/2016, and 12/21/2016."*

[EFTA01656437](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01656437.pdf) | [Original (JDrive)](https://jmail.world/drive/vol00010-efta01656437-pdf)

**TD Bank — BSA: 31000155070501**: HBRK Associates Inc (Richard Kahn's entity) received a $100,000 suspicious check plus **$847,838** in suspicious wire transfers from Deutsche Bank Trust account 542953715.

[EFTA01656524](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01656524.pdf) | [Original (JDrive)](https://jmail.world/drive/vol00010-efta01656524-pdf)

**TD Bank — BSA: 31000155725098**: Law enforcement contact identified as **Alex Rossmiller, DOJ SDNY**. Wires to *"Darren K Indyke PLCC IOLA Trust Account"* totaling **$12,657,830.34** — described as *"escrow for legal."*

[EFTA01656415](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01656415.pdf) | [Original (JDrive)](https://jmail.world/drive/vol00010-efta01656415-pdf)

**Charles Schwab — BSA: 31000150416250**: Richard Kahn wire reversals. Three accounts opened in April 2019, funded by wire deposits. Kahn attempted to retract: *"the terms that I accepted are not agreeable, I want to retract the wire."*

[EFTA01656452](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01656452.pdf) | [Original (JDrive)](https://jmail.world/drive/vol00010-efta01656452-pdf)

**JPMorgan Chase — BSA: 31000150420301**: Filed post-arrest (July 6, 2019). *"Suspicious payments based on amounts, frequency and counterparties"* involving Epstein at his St. Thomas address.

[EFTA01656566](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01656566.pdf) | [Original (JDrive)](https://jmail.world/drive/vol00010-efta01656566-pdf)

### The Original Documents

The four SARs cited in the original version of this report remain verified:

| EFTA | Original Chars | Current Chars | Removed | Filing Context |
|------|---------------|---------------|---------|----------------|
| [EFTA01656524](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01656524.pdf) | 72,738 | 3,322 | **95.4%** | TD Bank, HBRK Associates, Deutsche Bank wires |
| [EFTA01656500](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01656500.pdf) | 30,797 | 1,264 | **95.9%** | Alpha Group Capital, Edge Foundation, Harvard |
| [EFTA01656415](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01656415.pdf) | 29,753 | 1,241 | **95.8%** | Charles Schwab / TD Bank, $12.6M IOLA wire |
| [EFTA01656452](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01656452.pdf) | 24,252 | 1,034 | **95.7%** | Charles Schwab, Kahn wire reversals |

Original JDrive versions: [EFTA01656524](https://jmail.world/drive/vol00010-efta01656524-pdf) | [EFTA01656500](https://jmail.world/drive/vol00010-efta01656500-pdf) | [EFTA01656415](https://jmail.world/drive/vol00010-efta01656415-pdf) | [EFTA01656452](https://jmail.world/drive/vol00010-efta01656452-pdf)

### The Legal Question

SARs are filed under the Bank Secrecy Act (31 U.S.C. § 5318(g)). They carry confidentiality protections. But the EFTA was enacted specifically to override normal exemptions for the Epstein files. The Protocol cites no EFTA category for SAR redaction -- it simply instructs blanket removal with a freeform note.

The EFTA's "active investigation" exception (§ 2(c)(1)(C)) requires that withholding be "narrowly tailored and temporary." Full redaction of 156 SARs is neither narrow nor temporary. The SARs describe completed banking activity from 2014-2019, investigated by banks that have already settled with regulators. The structured cash transactions, the $12.6M trust wire, the post-arrest suspicious payments — all of this is historical banking intelligence, not ongoing investigative material.

---

## 5. What the DOJ Stripped

Beyond phone numbers and SARs, the completed pipeline identified categories of content removal that no EFTA exception covers.

### Maxwell's Financial Footprint: 1.45 Million Characters

[EFTA01684802](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01684802.pdf) | [Original (JDrive)](https://jmail.world/drive/vol00010-efta01684802-pdf)

The single largest document alteration in the corpus. **1,137 pages** of Ghislaine Maxwell's American Express statements through entity **ELLMAX LLC** — Centurion Card (Black Card) from July 2010 through late 2016, Business Gold Rewards Card, and OPEN Savings account. Every transaction degraded in the text layer: T-Mobile payments, Fandango tickets ($29.00), Google Services, "MB F DOG SHOWS INFO, GREENSBORO NC" ($73.89), foreign transaction fees. Account balances: $7,555, $9,004.25, $13,628.02, $23,813.68. One statement notes: *"Account cancelled at your request"* (September 2016).

SDNY evidence markers are visible throughout: `SDNY_GM_00326307`, `SDNY_GM_00328313` — these are public trial exhibits from *US v. Maxwell*.

**Visual verification**: The rendered pages appear **visually identical** between original and current versions. This is text-layer degradation, not visual redaction — the statements look the same when opened, but the searchable text has been corrupted. A researcher searching for "ELLMAX" or specific transaction amounts will not find these pages in the current DOJ production.

### Epstein's BOP Psychological File at MCC

[EFTA00047963](https://www.justice.gov/epstein/files/DataSet%209/EFTA00047963.pdf) | [Original (JDrive)](https://jmail.world/drive/vol00009-efta00047963-pdf)

Although many initial findings about this 1,000-page document were false positives (filtered by visual verification — see Section 10), the surviving verified changes are significant. The searchable text layer was degraded across **176 pages** of BOP psychological and medical records totaling **161,686 characters**. The visible pages appear unchanged — this is text-layer degradation affecting searchability, not visual redaction. The degraded content includes:

**Suicide risk assessments:**
- **07/09/2019**: First intake assessment. *"Inmate Epstein has various risk factors for suicidality including a high profile case with media attention, sex offense/trafficking charges, pre-trial status."* Classified CARE1-MH. (3,510+ chars)
- **07/23/2019**: The day of the first incident. *"It is unclear at this time if Mr. Epstein had placed the string around his own neck."* Also: *"Mr. Epstein told the staff watching him that his cellmate tried to kill him, which Mr. Epstein did not tell this writer."* (3,145+ chars)
- **08/01/2019**: Nineteen days before death. *"The US Marshals asked him to sign a form that noted Mr. Epstein has 'suicidal tendencies.' Mr. Epstein seemed surprised... He denied stating he was suicidal."* (7,362 chars across pp.508-510)

**Last clinical contacts:** 10+ intervention notes from 07/08/2019 through **08/08/2019** — two days before death. Each note 2,000-3,500 characters. All degraded in text layer.

**Tartaglione connection:** *"MCC New York administrators initially housed Mr. Epstein with Mr. Tartaglione as both had high profile cases... less likely to assault or otherwise try to extort Mr. Epstein."* Tartaglione (former cop charged with quadruple murder) *"notified staff immediately when he realized Mr. Epstein first made a possible suicide attempt/gesture on July 23, 2019."* Senior Officer memo from the night of the incident: *"On July 23, 2019 at approximately 1:27 AM while assigned to the Special Housing Unit..."*

**Biographical reconstruction (p.588):** Epstein's career history — dismissed from teaching in 1976, limited partner at Bear Stearns dismissed for "unknown policy violations" in 1981, relationship with Steven Hoffenberg (convicted Ponzi scheme operator), sole client at J. Epstein & Company who "granted him power of attorney," accused of "misappropriating funds — more than 46 million dollars."

These are not victim personal files. They are BOP institutional records about a deceased convicted sex offender, prepared for official review. The text layer was degraded, making them unfindable by keyword search — a researcher looking for "suicide risk assessment" or "cellmate tried to kill him" in the EFTA corpus will not find these pages, even though the words are visually present on the page.

### CVRA Master Case File: The NPA Paper Trail

[EFTA00184224](https://www.justice.gov/epstein/files/DataSet%209/EFTA00184224.pdf) | [Original (JDrive)](https://jmail.world/drive/vol00009-efta00184224-pdf)

The complete paper trail of how the 2007 Non-Prosecution Agreement was negotiated. 921 classified change units, 410 pages with real visual changes. **Visually verified**: new black-bar redactions confirmed over co-conspirator names (Sarah Kellen, Adriana Ross, Nadia Marcinkova on p.33), AUSA Maria Villafana's name (p.37), and "Giuffre" in case captions (p.83). Content stripped includes:

- **p.197**: *"The Mar-A-Lago Club"* and *"as a changing room assistant"* — the recruitment venue
- **p.200**: *"Thailand. While thousands of miles away from Defendant on this extended trip alone for the first time in more than four years, Plaintiff met, fell in love, and married a young man. She escaped from Defendant's abuse..."*
- **pp.500-501**: NPA signature pages — *"Epstein asserts and certifies..."* with AUSA Villafana, attorneys Sanchez and Lefcourt
- **pp.561-566**: Brad Edwards' sworn declaration (6 pages, 10,000+ chars each) describing government concealment of the NPA from victims: *"I was not informed that previously, in September 2007, the U.S. Attorney's Office had reached an agreement not to file federal charges"*
- **p.663**: AUSA Acosta email: *"In mid August 2007, your defense team, dissatisfied with my staff's review of the case, asked..."*

These are public court filings from Case 9:08-cv-80736-KAM. The DOJ is stripping the searchable text from sworn declarations describing its own prior misconduct.

### Deposition Testimony About Bill Clinton

[EFTA00159250](https://www.justice.gov/epstein/files/DataSet%209/EFTA00159250.pdf) | [Original (JDrive)](https://jmail.world/drive/vol00009-efta00159250-pdf)

**Visually verified**: additional black-bar redactions confirmed on p.52. An entire page of deposition testimony stripped as NON_PII CONTENT_REMOVAL:

> **Q. Is it also your understanding that Bill Clinton played somewhat of a role in helping Jeffrey Epstein out of the trouble that he would have been in related to his sexual interactions with minor females?**
> A. I refuse to answer.

> **Q. Did Jeffrey Epstein tell you that you need to cooperate if you want the protection that me and my connections can give you for this activity?**
> A. I refuse to answer.

This is sworn testimony in a legal proceeding about a former President's alleged involvement. The EFTA specifically prohibits withholding on the basis of "embarrassment, reputational harm, or political sensitivity, including to any government official, public figure, or foreign dignitary."

### NTOC Alexander Brothers Report (Post-EFTA)

[EFTA01660679](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01660679.pdf) | [Original (JDrive)](https://jmail.world/drive/vol00010-efta01660679-pdf)

A DOJ internal email chain from **August 6, 2025** — after the EFTA was signed — requesting an NTOC (National Threat Operations Center) report on "the Alexander brother allegations." Content stripped includes allegations of *"big orgy parties with her, other young girls, and older Victoria's Secret models, including Bill Clinton,"* rape allegations against the Alexander brothers, and a reference to *"Jeffrey Epstein, Sammy Sosa, and Donald [Trump]"* hosting a party together.

### Epstein's Financial Architecture

**Deutsche Bank KYC for ZOITO Management LLC:**
[EFTA01282143](https://www.justice.gov/epstein/files/DataSet%209/EFTA01282143.pdf) | [Original (JDrive)](https://jmail.world/drive/vol00009-efta01282143-pdf)

Deutsche Bank new account opening (March 7, 2017), listing two existing accounts: *"The Haze Trust - Deposit"* and *"Butterfly Trust - Deposit."* Darren Indyke named as account representative. Deutsche Bank PEP questionnaire asking whether the client is a *"Politically Exposed Person"* with a connection to *"Prince."* SDNY evidence markers: `DB-SONY-0000260` / `SDNY_GM_00037435`.

**Epstein's Internal Financial Ledger:**
[EFTA01308282](https://www.justice.gov/epstein/files/DataSet%209/EFTA01308282.pdf) | [Original (JDrive)](https://jmail.world/drive/vol00009-efta01308282-pdf)

Accounting entries showing: Les Wexner $1,100,000 | Ghislaine Maxwell $21,182 | NY Strategy Group $723,125 | Highbridge Capital $33,560,762 | SA8 Capital Partners $7,031,426 | portfolio total **$202,189,381** | Reverse Repo $75,000,000. All degraded in text layer as NON_PII. **Visual verification**: pages appear **visually identical** — text-layer degradation only.

**Leon D. Black Trust Account:**
[EFTA00002012](https://www.justice.gov/epstein/files/DataSet%201/EFTA00002012.pdf) | [Original (JDrive)](https://jmail.world/drive/vol00001-efta00002012-pdf)

Bank of America statement for LEON D BLACK / DEBRA BLACK, Trust "B." **Visually verified**: black-bar redaction expanded over account/routing number area. Dollar amounts degraded in text layer: $3,295,278.44, $6,025,000.00, $17,146,592.73, ending balance $848,411.77.

**Apollo Cash Flow Projections:**
[EFTA00295586](https://www.justice.gov/epstein/files/DataSet%209/EFTA00295586.pdf) | [Original (JDrive)](https://jmail.world/drive/vol00009-efta00295586-pdf)

"Cash Flow Assumptions July 7 2015" by R. Joslin: Apollo distributions per share, *"70 HOURS OF REIMBURSEMENT/CHARTER FROM APOLLO"* (Apollo subsidizing Epstein's plane), boat charter economics, GRAT structure. Dollar amounts: $25,747,696 | $79,745,381 | $153,308,781 | $(211,676,464). All degraded in text layer. **Visual verification**: pages appear **visually identical** — text-layer degradation only.

### VIP Contact Lists

[EFTA01621272](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01621272.pdf) | [EFTA02591199](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02591199.pdf) | [EFTA00696251](https://www.justice.gov/epstein/files/DataSet%209/EFTA00696251.pdf)

Three documents containing the same handwritten/typed first-name contact list: *"churkin, gates, boris, tetje, jes, leon, mort, sergey thiel, burns, reid reid joi tom larry."*

Decoded: Vitaly Churkin (late Russian UN Ambassador), Bill Gates, Jes Staley (Barclays CEO), Leon Black (Apollo), Mort Zuckerman (NY Daily News), Peter Thiel, Reid Hoffman (LinkedIn), Joi Ito (MIT Media Lab), Larry Summers (Treasury/Harvard).

**Related:** [EFTA01963880](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01963880.pdf) | [Original (JDrive)](https://jmail.world/drive/vol00010-efta01963880-pdf) — Epstein email to Terje Rod-Larsen (former UN Special Coordinator): *"Svet will be coordinating all sept meeting, gates, jagland, mongolia, summers, ehud, etc."* **Visually verified**: new black-bar redactions confirmed over "Svet" and related names in the To: field and email body.

### Flight Records, Helicopters, and Phone Tolls

**Hyperion Air Sikorsky S-76C++**: [EFTA02727497](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02727497.pdf) | [Original (JDrive)](https://jmail.world/drive/vol00011-efta02727497-pdf) — 1,598 change units, 538,816 characters degraded in text layer. Complete helicopter purchase agreement for Epstein's aviation entity. **Visual verification**: pages appear **visually identical** — text-layer degradation only.

**Aircraft Security Agreements**: [EFTA01329795](https://www.justice.gov/epstein/files/DataSet%209/EFTA01329795.pdf) — 1,475 change units, 630,383 characters. Aircraft financing: $8,125,000 in outstanding principal, UCC filings, mortgage documentation.

**Phone Toll Records (2005-2006)**: [EFTA01705727](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01705727.pdf) and [EFTA01705827](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01705827.pdf) — 1,907 change units, 111,993 characters. Call detail records from the peak trafficking period, showing calls from New York, Palm Beach, West Palm Beach, Charlotte Amalie, Miami, and Jacksonville. Every called number, timestamp, and duration degraded in text layer.

**AT&T/Cingular Records (Martin Golick)**: [EFTA01316243](https://www.justice.gov/epstein/files/DataSet%209/EFTA01316243.pdf) — 977 change units, 255,470 characters. Cell tower locations showing precise movement patterns across Palm Beach, New York, Charlotte Amalie, and Jacksonville (2005-2008).

### Device Forensics

**Epstein's iMessage Archive**: [EFTA00783989](https://www.justice.gov/epstein/files/DataSet%209/EFTA00783989.pdf) | [Original (JDrive)](https://jmail.world/drive/vol00009-efta00783989-pdf) — Mac filesystem paths showing iMessage conversations: `/Users/jee/Library/Messages/Archive/2019-03-04/Joi Ito on 2019-01-20` — proving Epstein was messaging Joi Ito as late as January 2019, six months before arrest. **Visual verification**: pages appear **visually identical** — text-layer degradation only.

**Skype Chat Logs**: [EFTA01209464](https://www.justice.gov/epstein/files/DataSet%209/EFTA01209464.pdf) / [EFTA01217687](https://www.justice.gov/epstein/files/DataSet%209/EFTA01217687.pdf) — 2013 conversations between Joichi Ito (jeevacation), Reid Hoffman (reidhoffman), and others. Discussion of "arab deception" and synthetic biology with Joe Jacobson.

**Photo Filename Catalog**: [EFTA00004577](https://www.justice.gov/epstein/files/DataSet%201/EFTA00004577.pdf) | [Original (JDrive)](https://jmail.world/drive/vol00001-efta00004577-pdf) — folder paths from Epstein's devices: *"St Trop/Clinton Morroco. Nude"* alongside *"Nudes070.JPG"* through *"Nudes104.JPG."* **Visual verification**: all four cited pages (pp.23, 27, 37, 40) appear **visually identical** — text-layer degradation only. The evidence catalog showing how photos were organized and labeled has been rendered unsearchable.

### The Groff De-Redaction Pattern

Across dozens of documents, Lesley Groff's name is being **revealed** (un-redacted) in current versions while other names in the same documents are **newly redacted**. This appears in EFTA02074911, EFTA02110792, EFTA02240144, EFTA02144326, EFTA02054900, EFTA02239160, EFTA00462039, EFTA01866656, EFTA01769960, and more.

This is the strongest evidence of a **selective, name-by-name redaction review** rather than automated blanket processing. The DOJ made a deliberate decision to un-redact Groff as a "known public figure" (Epstein's convicted executive assistant) while simultaneously adding PII redactions for other individuals in the same documents.

### Epstein's Trust Document: Public Probate, Stripped Anyway

[EFTA00098341](https://www.justice.gov/epstein/files/DataSet%209/EFTA00098341.pdf) | [Original (JDrive)](https://jmail.world/drive/vol00009-efta00098341-pdf)

Epstein's trust agreement — a public probate document filed in the U.S. Virgin Islands — had beneficiary names and dollar amounts altered in the text layer:

| Beneficiary | Bequest | Role |
|-------------|---------|------|
| Lesley Katherine Groff | $2,000,000 | Executive assistant (convicted) |
| Lawrence Paul Visoski Jr. | $2,000,000 | Chief pilot |
| David Rogers | $1,000,000 | Pilot |
| Celina Edith Dubin | 20+ references, full trust provisions | Glenn Dubin's daughter |
| Eva Andersson Dubin | Named, address 9 E. 71st Street | Glenn Dubin's wife |
| Marcinkova | Named | Co-conspirator (NPA immunity) |
| Kahn/Indyke families | LISA KAHN 5%, MAX G. KAHN 5%, SAMANTHA M. INDYKE, HANNAH E. INDYKE | Attorneys' families |

Visually verified (p.5): some names were actually **un-redacted** in the current version (David Rogers, Lesley Katherine Groff, Karyna Shuliak revealed) while others were newly redacted. The full trust provisions for Celina Edith Dubin (pp.13-15, 26) — *"operating expenses for any property... held in trust for the benefit of CELINA EDITH DUBIN"* — were degraded in the text layer.

This is a public document. Epstein's will was filed in probate court. The DOJ is redacting names of pilots, housekeepers, co-conspirators, and attorneys' family members from a record that is already publicly available.

### CVRA Legal Filing: Virginia Giuffre's Name Stripped 30+ Times

[EFTA00039421](https://www.justice.gov/epstein/files/DataSet%209/EFTA00039421.pdf) | [Original (JDrive)](https://jmail.world/drive/vol00009-efta00039421-pdf)

A 222-page CVRA legal filing with systematic content removal:

| Person/Content | Pages |
|---------------|-------|
| Virginia Giuffre (name stripped) | 83, 87-88, 90-92, 98, 100, 143-145, 149-151, 156, 160, 163, 170, 173-174 |
| Kellen/Ross/Marcinkova (co-conspirators) | 33 |
| AUSA Villafana | 37, 46 |
| Victim testimony | p.184: *"defendant introduced Minor Victim-3 to Epstein"* |
| Legal arguments | p.211: *"Government has informed defense counsel of witness 'M.'"* |

Giuffre is a public figure — she was the named plaintiff in *Giuffre v. Maxwell* (15-cv-7433). Kellen, Ross, and Marcinkova are named co-conspirators. Villafana is a federal prosecutor. The DOJ stripped all of their names from a public court filing.

### Shell Companies and International Wire Transfers

**LVIV Enterprises LLC:**
[EFTA00795708](https://www.justice.gov/epstein/files/DataSet%209/EFTA00795708.pdf) | [Original (JDrive)](https://jmail.world/drive/vol00009-efta00795708-pdf)

JPMorgan Chase bank statement for **LVIV Enterprises LLC**, 121 E 69th St Apt 2, New York NY 10021 — one block from Epstein's mansion at 9 E 71st St. Transaction details degraded in text layer (Jan-Feb 2015):
- Wire to **ING Bank Slaski SA, Katowice, Poland** — "Building Final Payment In Full"
- Wire to **Public Joint Stock CO Ukrsotsbank, Kiev, Ukraine** — "For Legal Services"
- Two payments to **Withers Bergman LLP** (Epstein's law firm)

An Epstein-linked shell company named after a Ukrainian city, making international wires to Poland and Ukraine through JPMorgan Chase. **Visual verification**: pages appear **visually identical** — text-layer degradation only.

**Sberbank Russia Wire:**
[EFTA01363123](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01363123.pdf) | [Original (JDrive)](https://jmail.world/drive/vol00010-efta01363123-pdf)

FIS Prime Compliance wire transfer alert: Jeffrey Epstein via LEGAL MONETIZATION to **Sberbank of Russia**. Beneficiary: Nikolay Aleksandrovich Syrnov. $1,700. **Visually verified**: new black-bar redactions confirmed over Activity number, Location ID, and administrative tracking fields. Core party information remains visible.

### TLO Background Investigation Report

[EFTA01256987](https://www.justice.gov/epstein/files/DataSet%209/EFTA01256987.pdf) | [Original (JDrive)](https://jmail.world/drive/vol00009-efta01256987-pdf)

A 318-page law enforcement data-broker intelligence report on Epstein, pulled **12/06/2018 at 05:39 PM** — the day before the SDNY indictment was unsealed. Contains all known addresses, business affiliations (FINANCIAL STRATEGY GROUP, INC.), phone listings, associate names, criminal records, and partial SSN references. **360 NON_PII content removals.** **Visual verification**: pages appear substantively identical with only minor rendering differences — text-layer degradation only. This is a law enforcement investigative tool's output about the *target* of the investigation.

### Foundation Donation Records

[EFTA01265496](https://www.justice.gov/epstein/files/DataSet%209/EFTA01265496.pdf) | [Original (JDrive)](https://jmail.world/drive/vol00009-efta01265496-pdf)

293 pages of Salesforce CRM donation tracking records for the **Epstein Foundation** (81,473 characters degraded in text layer). Individual donations tracked ($5,000, $2,000 entries), "Presidents Discretionary CLOSED" designations, campaign tracking data. Entries reference "Villard House 457 Madison Avenue" (Harvard Club of New York) and date back to 12/11/1998. **Visual verification**: pages appear **visually identical** — text-layer degradation only. The financial mechanism by which Epstein bought institutional access — rendered unsearchable.

### Flight Logs, CBP Records, and Passenger Manifests

[EFTA02727130](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02727130.pdf) | [Original (JDrive)](https://jmail.world/drive/vol00011-efta02727130-pdf)

367 pages containing aircraft flight logs, Private Air booking confirmations (Feb 19, 2019: passengers EPSTEIN JEFFREY EDWARD, RODGERS DAVID NEVILLE, VISOSKI LAWRENCE III), and **CBP (Customs & Border Protection) encounter records** with target surveillance dates in July 2019 — just before arrest. Passport #566672615, class of admission, arrival dates all degraded in text layer.

[EFTA01262537](https://www.justice.gov/epstein/files/DataSet%209/EFTA01262537.pdf) | [Original (JDrive)](https://jmail.world/drive/vol00009-efta01262537-pdf)

Private jet flight logs with crew ("Larry Visoski"), passenger names, flight routes, departure/arrival details. **246 NON_PII content removals.** **Visual verification**: pages appear **visually identical** — text-layer degradation only. The exact kind of evidence Congress mandated release of under the EFTA.

### Handwritten Notes and Investigation Material

**"34 Girls Wexner, IRS":**
[EFTA00518681](https://www.justice.gov/epstein/files/DataSet%209/EFTA00518681.pdf) | [Original (JDrive)](https://jmail.world/drive/vol00009-efta00518681-pdf)

Handwritten notes (pp.60-61): *"jean luc = 34 girls wexner, irs"* — linking Jean-Luc Brunel, 34 girls, Wexner, and IRS scrutiny. Also: *"young post docs. internet writer scientific american, researchers."* Classified NON_PII CONTENT_REMOVAL. **Visual verification**: pages appear **visually identical** on both pp.60 and 61 — text-layer degradation only.

**Flight notes with public figure names:**
[EFTA00153942](https://www.justice.gov/epstein/files/DataSet%209/EFTA00153942.pdf) | [Original (JDrive)](https://jmail.world/drive/vol00009-efta00153942-pdf)

Handwritten interview notes referencing flight logs: Trip #934 lists *"JE, GM, Trump, Marc Ep., Eva, Glenn Dubin/Chef"*; Trip #935: *"JE/GM Dershowitz."* All passenger names redacted.

**AUSA celebrates Epstein plea:**
[EFTA00193954](https://www.justice.gov/epstein/files/DataSet%209/EFTA00193954.pdf) | [Original (JDrive)](https://jmail.world/drive/vol00009-efta00193954-pdf)

p.465 — AUSA Anne Schultz email to AUSA Villafana: *"Alex told me this morning that Epstein had pled. That is wonderful. I never thought we'd see the day. You deserve all the credit for this. If it had not been for you, he would have gotten away with it."* A prosecutor celebrating a plea deal in an official DOJ email. Not PII. Text-layer degradation — searchability affected even though the visual page appears unchanged.

### Deepak Chopra Network (15+ Documents)

The Chopra connection spans at least 15 documents across the EFTA00445xxx-00458xxx and EFTA008xxxxx ranges:

| EFTA | Content Stripped |
|------|-----------------|
| [EFTA00445560](https://www.justice.gov/epstein/files/DataSet%209/EFTA00445560.pdf) | *"Good morning Deepak. I will be your contact to help set up and coordinate all!"* |
| [EFTA00446298](https://www.justice.gov/epstein/files/DataSet%209/EFTA00446298.pdf) | Groff to Carolyn Rangel (Chopra LLC President): *"Re: Jeffrey Epstein"* — *"we are off to Israel tomorrow"* |
| [EFTA00446294](https://www.justice.gov/epstein/files/DataSet%209/EFTA00446294.pdf) | Book promotion: *"Deepak Chopra and Menas Kafatos explore... their new book You Are The Universe"* |
| [EFTA00458560](https://www.justice.gov/epstein/files/DataSet%209/EFTA00458560.pdf) | *"speaking on the microbiome"* — Chopra event planning |
| [EFTA00814813](https://www.justice.gov/epstein/files/DataSet%209/EFTA00814813.pdf) | Calendar: *"12:00pm TENTATIVE Appt w/Deepak Chopra"* |
| [EFTA00821256](https://www.justice.gov/epstein/files/DataSet%209/EFTA00821256.pdf) | Contact: *"Deepak Chopra, 2013 Costa Del Mar Road, Carlsbad CA"* |

Epstein was actively coordinating with Chopra's organization as late as **February-March 2017** — post-conviction. Lesley Groff served as liaison. The DOJ's text layer shows "Deepak Chopra LLC," Rangel's name, phone numbers, URLs (www.deepakchopra.com), and Chopra's home address degraded across all 15+ documents. None of this is victim PII. **Visual verification**: EFTA00446294, EFTA00446298, and EFTA00458560 appear **visually identical** — text-layer degradation only. EFTA00445560 and EFTA00814813 show **confirmed visual changes** — but in the *reverse* direction: Lesley Groff's name was *revealed* (un-redacted) in the current version where the original had her identity blacked out.

### Deutsche Bank Employee Distribution List

[EFTA01426543](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01426543.pdf) | [Original (JDrive)](https://jmail.world/drive/vol00010-efta01426543-pdf)

Outstanding Official Checks Report listing approximately **60+ Deutsche Bank employees** with @db.com email addresses — the internal distribution list for Epstein's private banking unit. **Visually verified**: every @db.com email address replaced with heavy black redaction bars in the current version. Employee names remain partially visible but all email addresses are blacked out.

### Public Media Articles Stripped from Trial Exhibits

[EFTA01297125](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01297125.pdf) | [Original (JDrive)](https://jmail.world/drive/vol00010-efta01297125-pdf)

Wikipedia printout and New York Magazine article (nymag.com/nymetro/news/people/n_7912/) entered as Maxwell trial exhibits. Names degraded in text layer: Ghislaine Maxwell, Kevin Spacey, Bill Clinton, Donald Trump, Virginia Roberts. SDNY evidence markers: `DB-SDNY-0022833`. **Visual verification**: pages appear **visually identical** — text-layer degradation only. These are publicly available articles that anyone can read online — the text layer was degraded in the *trial exhibit copies*, making them unfindable by name search.

[EFTA02729228](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02729228.pdf) | [Original (JDrive)](https://jmail.world/drive/vol00011-efta02729228-pdf)

Published media reporting about the Epstein-Wexner relationship: *"Sources say Epstein proved that he could be useful to Wexner as well, with 'fresh' ideas about investments."* **Visual verification**: pages appear **visually identical** — text-layer degradation only.

---

## 6. Cross-Document Public Figure Patterns

Beyond individual document alterations, the pipeline reveals patterns of name removal targeting specific public figures across multiple documents.

*Note: Every EFTA cited below can be compared against its original via the JDrive archive. The JDrive URL pattern is: `https://jmail.world/drive/vol{DATASET_5DIGIT}-efta{8DIGITS}-pdf` — e.g., Dataset 9 EFTA00277521 → `vol00009-efta00277521-pdf`. Dataset numbers are listed in the tables.*

### Trump / Mar-a-Lago (7 Documents)

| EFTA | Content Stripped |
|------|-----------------|
| [EFTA00277521](https://www.justice.gov/epstein/files/DataSet%209/EFTA00277521.pdf) p.5 | FBI 302: victim *"began working at Donald Trump's Mar-A-Lago Club... employed as baby sitter and later as a locker... therapist... approached by..."* |
| [EFTA00091904](https://www.justice.gov/epstein/files/DataSet%209/EFTA00091904.pdf) p.2 | FBI 302: someone *"met DONALD TRUMP at MAR-A-LAGO in approximately 1..."* |
| [EFTA00622303](https://www.justice.gov/epstein/files/DataSet%209/EFTA00622303.pdf) p.5 | Katie Johnson lawsuit: *"Plaintiff... asks the court for relief against the Defendants, **Donald J. Trump and Jeffrey E. Epstein**, in the amount of **$100,000,000.00**"* — **visually verified: black bars confirmed** |
| [EFTA00793971](https://www.justice.gov/epstein/files/DataSet%209/EFTA00793971.pdf) p.8 | *"**Acosta is now Trump's secretary of labor.** Epstein, 65, reached the non-prosecution deal with Acosta's..."* |
| [EFTA00143524](https://www.justice.gov/epstein/files/DataSet%209/EFTA00143524.pdf) p.8 | *"IS ALSO THE GIRL THAT HAS ACCUSED YOUR LATE WIFE MR TRUMP, THE MOTHER..."* |
| [EFTA00143993](https://www.justice.gov/epstein/files/DataSet%209/EFTA00143993.pdf) p.27 | *"BIDEN, PLMN, TRUMP"* — names list |
| [EFTA00153942](https://www.justice.gov/epstein/files/DataSet%209/EFTA00153942.pdf) p.17 | Handwritten flight notes: *"JE, GM, Trump, Marc Ep., Eva, Glenn Dubin/Chef"* |

All classified NON_PII CONTENT_REMOVAL. **Visual verification**: The Katie Johnson lawsuit (EFTA00622303) shows **confirmed visual black-bar redactions** over the plaintiff's name and signature. The Acosta/Trump article (EFTA00793971) shows **confirmed new black-bar redactions** over names. However, the FBI 302 pages (EFTA00277521 p.5, EFTA00091904 pp.2-3) and the Biden/Trump names list (EFTA00143993 p.27) appear **visually identical** between original and current versions — text-layer degradation only. The EFTA prohibits withholding on the basis of "political sensitivity, including to any... public figure."

### Dershowitz (6 Documents)

| EFTA | Content Stripped |
|------|-----------------|
| [EFTA00092643](https://www.justice.gov/epstein/files/DataSet%209/EFTA00092643.pdf) p.1 | *"Alan D... $10,000... Bank... 2968 002M"* — bank account + dollar amount |
| [EFTA00105307](https://www.justice.gov/epstein/files/DataSet%209/EFTA00105307.pdf) p.1 | *"Alan Dershowitz... $10,000"* + *"four co-conspirators given immunity"* |
| [EFTA00092647](https://www.justice.gov/epstein/files/DataSet%209/EFTA00092647.pdf) pp.9-13 | Media article citations: YouTube, Fox News, NY Magazine URLs about Dershowitz |
| [EFTA00188608](https://www.justice.gov/epstein/files/DataSet%209/EFTA00188608.pdf) p.342 | *"abuse minors despite Alan Dershowitz being a"* |
| [EFTA00190116](https://www.justice.gov/epstein/files/DataSet%209/EFTA00190116.pdf) p.22 | Alan Dershowitz name stripped |
| [EFTA00213048](https://www.justice.gov/epstein/files/DataSet%209/EFTA00213048.pdf) p.95 | *"Dershowitz also stated that Ms."* |

Financial records, co-conspirator immunity references, and media article citations about a public figure. **Visual verification**: EFTA00092643 and EFTA00105307 show **confirmed visual black-bar redactions** over bank account numbers in the Dershowitz payment tables. The remaining documents were not individually rendered for this verification pass. Dershowitz's Epstein connections have been extensively litigated in federal court and reported in public media.

### Dubin Family (5 Documents)

| EFTA | Content Stripped |
|------|-----------------|
| [EFTA00149112](https://www.justice.gov/epstein/files/DataSet%209/EFTA00149112.pdf) pp.0,8 | Glenn Dubin + children Maye, Celina, Jordan |
| [EFTA00159250](https://www.justice.gov/epstein/files/DataSet%209/EFTA00159250.pdf) p.42 | Glenn Dubin (2x) — same deposition as Clinton testimony |
| [EFTA00090773](https://www.justice.gov/epstein/files/DataSet%209/EFTA00090773.pdf) p.35 | Glen Dubin, Eva Anderson, Manuela |
| [EFTA00098341](https://www.justice.gov/epstein/files/DataSet%209/EFTA00098341.pdf) pp.9-26 | Celina Edith Dubin 20+ times (trust provisions) |
| [EFTA00153942](https://www.justice.gov/epstein/files/DataSet%209/EFTA00153942.pdf) p.17 | Flight notes: *"Eva, Glenn Dubin/Chef"* |

Glenn Dubin is a billionaire hedge fund manager. Eva Andersson-Dubin is a former Miss Sweden. Both are public figures whose relationship with Epstein has been extensively reported. **Visual verification**: EFTA00149112 p.8 shows **confirmed visual black-bar redactions** over Glenn Dubin and children's names. The trust provisions for their daughter Celina are from a public probate document.

### Jes Staley / Barclays (3 Documents)

| EFTA | Content Stripped |
|------|-----------------|
| [EFTA00090717](https://www.justice.gov/epstein/files/DataSet%209/EFTA00090717.pdf) p.0 | *"accusations against Jes Staley, the CEO of Barclays Bank, of violent"* — text-layer degradation |
| [EFTA00143736](https://www.justice.gov/epstein/files/DataSet%209/EFTA00143736.pdf) p.0 | *"Melissa Biden Re: Jess Staley"* — email subject — text-layer degradation |
| [EFTA00145723](https://www.justice.gov/epstein/files/DataSet%209/EFTA00145723.pdf) pp.60,101 | "Jess" name degraded in text layer |

Staley resigned as Barclays CEO in 2021 over his Epstein connections. The FCA investigation into his relationship with Epstein is public record. **Visual verification**: EFTA00090717 p.0, EFTA00143736 p.0, and EFTA00145723 pp.60,101 all appear **visually identical** between original and current versions — text-layer degradation only.

### Prince Andrew FBI 302 Series

Multiple FBI 302 victim interviews received expanded redactions describing encounters with Prince Andrew:

| EFTA | Content |
|------|---------|
| [EFTA00553414](https://www.justice.gov/epstein/files/DataSet%209/EFTA00553414.pdf) | Victim describes Prince Andrew encounter at Club Tramp London, sexual abuse details |
| [EFTA01142533](https://www.justice.gov/epstein/files/DataSet%209/EFTA01142533.pdf) p.16 | Maxwell approaching victim for shopping, introduction to Prince Andrew, Club Tramp |
| [EFTA01699136](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01699136.pdf) p.19 | Maxwell taking victim shopping, Prince Andrew at Maxwell's London townhome |
| [EFTA01836550](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01836550.pdf) | Email discussing "The Duke" sexual assault allegations |
| [EFTA00081180](https://www.justice.gov/epstein/files/DataSet%209/EFTA00081180.pdf) p.22 | Published article citation stripped: *"Prince Andrew's Friend, Ghislaine Maxwell, Some Underage Girls..."* |

Prince Andrew settled Virginia Giuffre's civil lawsuit in 2022. His Epstein connections are among the most extensively reported aspects of the case. *Note: the FBI 302 documents in this series (EFTA00553414, EFTA01142533, EFTA01699136) were flagged as visual false positives in our automated pixel-diff verification, suggesting text-layer degradation rather than visual redaction. The published article citation (EFTA00081180) was not individually rendered for this pass.*

### Clinton / Maxwell Additional Material

Beyond the deposition testimony cited in Section 5:

[EFTA00091904](https://www.justice.gov/epstein/files/DataSet%209/EFTA00091904.pdf) p.3 — FBI 302: witness describes *"BILL CLINTON with MAXWELL present. CLINTON asked 'What do you do?'. MAXWELL told..."* The substance of Maxwell's response was degraded in the text layer. **Visual verification**: pages appear **visually identical** — text-layer degradation only.

[EFTA00004577](https://www.justice.gov/epstein/files/DataSet%201/EFTA00004577.pdf) pp.23-27, 37 — Photo filename catalog from Epstein's devices: folder path *"St Trop/Clinton Morroco. Nude"* alongside *"Nudes070.JPG"* through *"Nudes104.JPG."* These are filenames — metadata showing how Epstein organized his photo collection — not the photos themselves. **Visual verification**: pages appear **visually identical** — text-layer degradation only.

[EFTA01613198](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01613198.pdf) | [Original (JDrive)](https://jmail.world/drive/vol00010-efta01613198-pdf) — Gates Foundation internal memorial email: *"Bill and Melinda Gates — We were deeply saddened to learn that our friend, mentor, and advisor Sam Dryden died this morning."* Found in Epstein's documents. **Visually verified**: the **entire page has been blacked out** — replaced with a solid black rectangle in the current version. Only a timestamp ("03:46:30 pm") remains visible at the bottom. This is the most extreme visual alteration in the corpus — a complete page blackout of a Gates Foundation email.

---

## 7. Systematic Patterns

### Government Employee Name Scrubbing

The Protocol instructs blanket redaction of government employee names (lines 325-331). In practice:

| Official | Removals | Documents | Role |
|----------|----------|-----------|------|
| R. Alexander Acosta | 18+ | 8+ | U.S. Attorney (NPA signatory) |
| Ann Marie Villafana | 6+ | 4+ | AUSA (lead Epstein prosecutor) |
| Jeff Sloman | 13+ | 6+ | Chief AUSA |
| Jason Swergold | 15+ | 6+ | AUSA SDNY (post-arrest) |
| Adam Johnson | 60+ | 40+ | BOP official |
| Stephanie Scannell | 30+ | 27+ | BOP official |
| Nesbitt Kuyrkendall | 4+ | 2+ | FBI Special Agent |
| John Kerwin / Guido Modano | 10+ | 5+ | OIG Agents |

On [EFTA00213048](https://www.justice.gov/epstein/files/DataSet%209/EFTA00213048.pdf), Acosta's name was removed from **15 consecutive pages** of NPA-related filings. On page 12, "R. ALEXANDER ACOSTA UNITED STATES ATTORNEY" was replaced with gibberish "IMPIMPRIEY." On [EFTA00076068](https://www.justice.gov/epstein/files/DataSet%209/EFTA00076068.pdf), AUSA Villafana's name was redacted from the NPA signature page itself — while Acosta's name remained visible.

### Co-Conspirator Name Scrubbing

Sarah Kellen, Adriana Ross, and Nadia Marcinkova were named as co-conspirators in the NPA and granted immunity. The DOJ is stripping their names from documents that *identify them as co-conspirators*:

- [EFTA00040089](https://www.justice.gov/epstein/files/DataSet%209/EFTA00040089.pdf) p.6: *"any potential co-conspirators of Epstein, including but not limited to Sarah Kellen, Adriana Ross, Nadia Martinkova"* — **visually verified: confirmed black-bar redactions** over Kellen, Ross, and Marcinkova; Lesley Groff remains unredacted
- [EFTA00081015](https://www.justice.gov/epstein/files/DataSet%209/EFTA00081015.pdf): Kellen's name removed from **12 pages** of a civil RICO filing: *"Sarah Kellen, participated in an enterprise"*
- [EFTA00209781](https://www.justice.gov/epstein/files/DataSet%209/EFTA00209781.pdf) p.6: *"witness, subject, or target of the Epstein investigation, including Sarah Kellen, Ghislaine Maxwell, Nadia Marcinkova, Lesley Groff, Louella Ruboyo, Larry Morrison..."* — **visually verified: confirmed black-bar redactions** over multiple names

Total: Sarah Kellen 26 removals across 23 documents. The LLM classifier consistently misclassified these as VICTIM_PII or PRIVACY_ACT_PII. Kellen and Marcinkova are convicted/immunized co-conspirators, not victims.

### Cross-Document Email Sender Scrubbing

The DOJ created an email-header scrubbing operation that removes sender/recipient names across hundreds of documents:

| Name | Removals | Documents |
|------|----------|-----------|
| Elen capri (De Souza Ferreira) | 281 | 113 |
| Margherita | 156 | 76 |
| Irina | 125 | 87 |
| Anastasiya Siro(ochenko) | 140 | 69 |
| Aurelija | 142 | 64 |
| balerina simona | 101 | 34 |
| Claire Brugirard | 72 | 33 |
| Sarah Kellen | 26 | 23 |

The practical effect: you can no longer search the EFTA corpus for "who was emailing Epstein about X." Email chains become anonymous correspondence. Whether these individuals are victims, associates, or employees, the pattern converts a searchable email archive into an unsearchable one.

### FBI Evidence and Investigative Infrastructure

[EFTA00162461](https://www.justice.gov/epstein/files/DataSet%209/EFTA00162461.pdf): An FBI Office of General Counsel email (August 2023) ordering preservation of Epstein investigation files was stripped entirely: *"I will be amending the litigation hold or sending out new litigation holds. To the extent there are any physical files regarding the relevant investigations into Epstein/Maxwell (50D-NY-3027571), please make sure they are not destroyed."* This reveals FBI case number 50D-NY-3027571, a victim's 5F95 tort claim alleging FBI negligence, and active litigation holds on physical evidence.

[EFTA01248438](https://www.justice.gov/epstein/files/DataSet%209/EFTA01248438.pdf): FBI FD-340 chain-of-custody forms for physical evidence — 99 pages, 52,338 characters stripped.

[EFTA00095751](https://www.justice.gov/epstein/files/DataSet%209/EFTA00095751.pdf) | [Original (JDrive)](https://jmail.world/drive/vol00009-efta00095751-pdf): The evidence catalog for *US v. Maxwell* — descriptions of what was produced to defense, including FBI interview 302s, police reports, and attorney correspondence. **Visual verification**: pages appear **visually identical** — text-layer degradation only. The evidence catalog for the most significant sex trafficking trial of the decade has been rendered unsearchable.

Additional FBI infrastructure stripped from the record:
- [EFTA00161367](https://www.justice.gov/epstein/files/DataSet%209/EFTA00161367.pdf) p.3: FBI/DOJ internal investigative update — Dell laptop decrypted by STKU, Samsung phone EDAU extraction, CART/CAIR processing status across multiple field offices.
- [EFTA00161394](https://www.justice.gov/epstein/files/DataSet%209/EFTA00161394.pdf) p.1: FBI VCAC (Violent Crimes Against Children) case update (31E-NY-3027574) — Virgin Islands evidence imaging, Pittsburgh HIGH PRIORITY CI case, Martinsburg RA referenced.
- [EFTA00174374](https://www.justice.gov/epstein/files/DataSet%209/EFTA00174374.pdf) p.0: FBI email re: "Brasilia Visit" (UNCLASSIFIED//FOUO, Aug 24, 2023) — FBI international liaison names (Grimm, DeLong, Betancez, Kelley, Whitaker, Buckschier), Legat Gonzalez.
- [EFTA00622303](https://www.justice.gov/epstein/files/DataSet%209/EFTA00622303.pdf) p.3: DOJ internal email chain from **July 3, 2025** (post-EFTA) about file transfer. Stanley Woodward (OAG/JMD) coordinating thumb drives and SharePoint access.

### Text-Layer Degradation (27,026 Pages)

This category is distinct from visual redaction — and may be the most significant finding of this report. Of 51,262 change units marked as `visual_false_positive` by pixel-diff verification — meaning the visible page looks identical between versions — **27,026 were classified by the LLM as NON_PII CONTENT_REMOVAL**. The invisible OCR text layer has been degraded even though the page itself appears the same.

The practical result: the page *looks* normal, but the text that search engines and researchers use to find content has been corrupted. A researcher searching the EFTA corpus by keyword will not find these pages. Our own visual verification of cited documents confirms this pattern across dozens of high-profile findings: Maxwell AmEx statements, Epstein's financial ledger, Apollo cash flow projections, flight logs, Foundation donation records, the "34 girls wexner" handwritten notes, Jes Staley documents, Trump/Clinton FBI 302s, grand jury proceedings, and public media articles all appear **visually identical** between original and current versions while their text layers have degraded.

We cannot determine from our analysis whether this degradation is intentional or a side effect of OCR re-processing. What we can say is that the effect is the same: 27,026 pages of the EFTA corpus have been rendered invisible to keyword search. This is the hidden iceberg beneath the 40,870 pages with confirmed visual changes.

### Entire Prosecution Team Stripped

[EFTA00205380](https://www.justice.gov/epstein/files/DataSet%209/EFTA00205380.pdf) | [Original (JDrive)](https://jmail.world/drive/vol00009-efta00205380-pdf)

p.8: *"Jeffrey H. Sloman, Matt Menchel, Andy Lourie, Ann Marie Villafana, Dexter Lee, and Bruce Reinhart and state prosecutors Dahlia Weiss, Lana Belolovek, and others involved in the Ep[stein case]."* The complete roster of federal AND state prosecutors who handled the Epstein case — all stripped in a single passage. **Visually verified**: new black-bar redactions confirmed covering the last three lines of paragraph 21, obscuring the complete list of prosecutors.

[EFTA00179797](https://www.justice.gov/epstein/files/DataSet%209/EFTA00179797.pdf) p.193: Five USAFLS prosecutors stripped from a DOJ read-receipt email: Senior Robert, Acosta Alex, Sloman Jeff, Lee Dexter, Atkinson Karen.

### Co-Conspirator Immunity Lists

Additional documents where co-conspirator names are stripped from passages that *identify them as co-conspirators*:

- [EFTA00084871](https://www.justice.gov/epstein/files/DataSet%209/EFTA00084871.pdf) p.7: *"identity or location of co-conspirators of JEFFREY EPSTEIN, including SARAH KELLEN and GHISLAINE MAXWELL"* — **visually verified: confirmed black-bar redaction** over SARAH KELLEN; GHISLAINE MAXWELL remains visible
- [EFTA00095506](https://www.justice.gov/epstein/files/DataSet%209/EFTA00095506.pdf) p.7: Same text (duplicate filing) — **visually verified: same confirmed redaction pattern**
- [EFTA00105307](https://www.justice.gov/epstein/files/DataSet%209/EFTA00105307.pdf) p.1: *"four co-conspirators given immunity in connection with Epstein's [NPA]"* — **visually verified: confirmed black-bar redactions** over account numbers in Dershowitz payment table
- [EFTA00215373](https://www.justice.gov/epstein/files/DataSet%209/EFTA00215373.pdf) p.0: Non-Prosecution Agreement text — **visually verified: confirmed black-bar redactions** over names Shawna R., Tatum M., and Courtney W., plus "R. Alexander Acosta" redacted from signature block

### Grand Jury Proceedings Scrubbed

| EFTA | Content Stripped |
|------|-----------------|
| [EFTA00085291](https://www.justice.gov/epstein/files/DataSet%209/EFTA00085291.pdf) p.23 | *"The sworn testimony of [redacted] was taken before the **Federal Grand Jury, West Palm Beach Division**... on the 27th day of February"* |
| [EFTA00079911](https://www.justice.gov/epstein/files/DataSet%209/EFTA00079911.pdf) p.9 | *"**SDNY Grand Jury Subpoena Dated July 5, 2019**"* — the 2019 federal grand jury subpoena |
| [EFTA01247417](https://www.justice.gov/epstein/files/DataSet%209/EFTA01247417.pdf) p.1 | *"**(U//FOUO) TO DOCUMENT SERVICE OF GRAND JURY SUBPOENA**"* — law enforcement sensitive |
| [EFTA00222670](https://www.justice.gov/epstein/files/DataSet%209/EFTA00222670.pdf) p.41 | *"**Grand Jury No. 07-103 (WPB)**"* — the original Palm Beach grand jury number |
| [EFTA00223748](https://www.justice.gov/epstein/files/DataSet%209/EFTA00223748.pdf) pp.19,23 | *"Grand Jury B, excluding any testimony regarding those six victims"* |
| [EFTA01660651](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01660651.pdf) p.3 | Confidential Grand Jury Material: Jane Doe #7 overt acts, dates, defendants |

Grand jury numbers, subpoena service records, and procedural text — none of which constitute PII — systematically degraded in the text layer. **Visual verification**: EFTA00085291 pp.23,75, EFTA00079911 p.9, EFTA01247417 p.1, and EFTA01660651 p.3 all appear **visually identical** between original and current versions — text-layer degradation only.

### CVRA Case Number Systematic Erasure

[EFTA00189425](https://www.justice.gov/epstein/files/DataSet%209/EFTA00189425.pdf) | [EFTA00210202](https://www.justice.gov/epstein/files/DataSet%209/EFTA00210202.pdf)

Crime Victims' Rights Act notification letters — 458 pages combined. The case number **08-80736-CIV-MARRA** (Courtney Wild's public CVRA civil case) was systematically stripped from every page. EFTA00189425 alone has 261+ NON_PII content removals of this case number. Case 08-80736-CIV-MARRA is a public federal court case, fully docketed on PACER. Not PII by any definition.

### NPA-Era Email Chains

Large batches of NPA negotiation correspondence had government contact information stripped:

| EFTA | Pages Changed | Description |
|------|--------------|-------------|
| [EFTA00227225](https://www.justice.gov/epstein/files/DataSet%209/EFTA00227225.pdf) | 139 | *"Civil Cases Involving Jeffrey Epstein"* — Brad Edwards, Lefkowitz, Estrada |
| [EFTA00225378](https://www.justice.gov/epstein/files/DataSet%209/EFTA00225378.pdf) | 122 | *"Operation Leap Year"* travel authorization + Villafana-attorney email chain |
| [EFTA00230208](https://www.justice.gov/epstein/files/DataSet%209/EFTA00230208.pdf) | 101 | DOJ internal emails re: Jeffrey Epstein (2007), *"letter to AUSA"* |
| [EFTA00233059](https://www.justice.gov/epstein/files/DataSet%209/EFTA00233059.pdf) | 88 | Hearing before Judge Marra — Roy Black / Jay Lefkowitz correspondence |

The dominant alteration pattern: AUSA Villafana's phone/fax (561 209-1047 / 561 820-8777) stripped from every email signature, prosecutor names stripped, FBI agent names/phones stripped, and new redaction boxes added to already-public CVRA court filings.

### BOP Tartaglione Prosecutor Correspondence

Within the BOP email archives, specific prosecutor-defense attorney exchanges about Epstein's cellmate were stripped:

- [EFTA00041963](https://www.justice.gov/epstein/files/DataSet%209/EFTA00041963.pdf) p.575: Jason Swergold (SDNY AUSA) email to BOP, CC: Aida Leisenring (aleisenring@barketepstein.com), Subject: *"Statements by Mr. Tartaglione"* — prosecutor asking about what Tartaglione said happened
- [EFTA00041963](https://www.justice.gov/epstein/files/DataSet%209/EFTA00041963.pdf) p.903: Bruce Barket (Tartaglione's lawyer): *"Maurene and I are available on Wednesday at 2:30"* — Maurene Comey (SDNY AUSA, James Comey's daughter) involved in the Tartaglione matter
- [EFTA00041963](https://www.justice.gov/epstein/files/DataSet%209/EFTA00041963.pdf) p.931: *"Re: Tartaglione and MCC"* — prosecutor-lawyer correspondence about events at MCC

---

## 8. The Privacy Act Conflict

The structural problem is straightforward.

The EFTA enumerates exactly five categories of permitted withholding. The Privacy Act is not one of them. The DOJ's Protocol creates what amounts to a sixth category — "Privacy Act Redactions" — and applies it as a separate authority.

### Specific Statute Overrides General

The principle of *lex specialis derogat legi generali* -- a specific statute overrides a general one -- is directly relevant. The EFTA was enacted specifically to compel disclosure of the Epstein files. It enumerated specific exceptions. When Congress wanted to allow withholding, it said so. When it wanted to prohibit withholding on certain bases, it said that too (§ 2(b): no redaction for "embarrassment, reputational harm, or political sensitivity").

The JFK Records Act (44 U.S.C. § 2107) -- the model for the EFTA -- has been interpreted the same way. When Congress enacted a specific transparency statute, it intended to override the normal exemption framework, not to be supplemented by it.

### The DOJ Is Its Own Judge

The Protocol was written by the Office of the Deputy Attorney General. The redactions are applied by DOJ contract reviewers. The assessment of what constitutes "Privacy Act" information versus "EFTA-excepted" information is made internally, with no external review mechanism specified in the Protocol.

Section 2(b) of the EFTA prohibits redaction on the basis of "embarrassment, reputational harm, or political sensitivity, including to any government official, public figure, or foreign dignitary." When the phone number of a former Prime Minister of Norway is stripped from a scheduling email, the distinction between "Privacy Act compliance" and "embarrassment prevention" becomes difficult to maintain.

### Federal Register Justification

Section 2(c)(2) of the EFTA mandates that "[a]ll redactions must be accompanied by a written justification published in the Federal Register and submitted to Congress." As of this writing, the [Democracy Defenders Fund](https://www.democracydefendersfund.org/epstein-files) -- which tracks EFTA compliance -- reports no such justification published. A direct search of the [2026 Federal Register index](https://www.federalregister.gov/index/2026/justice-department) for the Justice Department confirms no entry related to the Epstein Files Transparency Act, EFTA redactions, or the Privacy Act basis appears as of March 5, 2026 — more than three months after the statute's enactment and over a month after the final document release.

---

## 9. Scale

### Classification Breakdown (152,312 Classified Change Units)

| Classification | Count | % |
|---------------|-------|---|
| CONTENT_REMOVAL | 71,403 | 46.9% |
| OCR_IMPROVEMENT | 26,494 | 17.4% |
| NAME_REDACTION | 24,696 | 16.2% |
| MIXED | 19,704 | 12.9% |
| EMAIL_REDACTION | 4,361 | 2.9% |
| PHONE_REDACTION | 2,093 | 1.4% |
| METADATA_CHANGE | 2,084 | 1.4% |
| ACCOUNT_REDACTION | 634 | 0.4% |
| ADDRESS_REDACTION | 569 | 0.4% |
| DOB_REDACTION | 179 | 0.1% |
| SSN_REDACTION | 45 | 0.03% |

### Justification Breakdown

| Justification | Count | % |
|---------------|-------|---|
| NON_PII | 63,491 | 41.7% |
| MIXED | 30,693 | 20.2% |
| OCR_IMPROVEMENT | 26,568 | 17.4% |
| PRIVACY_ACT_PII | 24,084 | 15.8% |
| VICTIM_PII | 3,963 | **2.6%** |
| AMBIGUOUS | 3,431 | 2.3% |

**Only 2.6% of classified changes are defensible victim PII.** The DOJ removed 16 times more non-PII content than victim-protective content.

### Pipeline Status

| Status | Count |
|--------|-------|
| Classified (done) | 152,312 |
| Visual false positive | 51,262 |
| Parse error | 6,232 |
| False positive | 2,384 |
| Error | 464 |
| Skip (corrupt) | 76 |
| **Total** | **212,730** |

### Visual Verification (86,979 Pages)

| Verdict | Pages | % |
|---------|-------|---|
| Real visual change | 40,870 | 47.0% |
| OCR reprocessing noise | 22,455 | 25.8% |
| Identical | 13,808 | 15.9% |
| Ambiguous | 9,817 | 11.3% |

### Top 10 Documents by Content Stripped

| EFTA | Characters | Description | Verify |
|------|------------|-------------|--------|
| [EFTA01684802](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01684802.pdf) | 1,452,264 | Maxwell AmEx Centurion statements | [Original](https://jmail.world/drive/vol00010-efta01684802-pdf) |
| [EFTA01329795](https://www.justice.gov/epstein/files/DataSet%209/EFTA01329795.pdf) | 630,383 | Aircraft inventory security agreements | [Original](https://jmail.world/drive/vol00009-efta01329795-pdf) |
| [EFTA02727497](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02727497.pdf) | 538,816 | Hyperion Air / Sikorsky helicopter | [Original](https://jmail.world/drive/vol00011-efta02727497-pdf) |
| [EFTA01316243](https://www.justice.gov/epstein/files/DataSet%209/EFTA01316243.pdf) | 255,470 | AT&T/Cingular phone records | [Original](https://jmail.world/drive/vol00009-efta01316243-pdf) |
| [EFTA00047963](https://www.justice.gov/epstein/files/DataSet%209/EFTA00047963.pdf) | 161,686 | BOP psychological file / MCC death investigation | [Original](https://jmail.world/drive/vol00009-efta00047963-pdf) |
| [EFTA01265496](https://www.justice.gov/epstein/files/DataSet%209/EFTA01265496.pdf) | 81,473 | Epstein Foundation donation records | [Original](https://jmail.world/drive/vol00009-efta01265496-pdf) |
| [EFTA02727130](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02727130.pdf) | 67,078 | Flight logs + Private Air bookings + CBP | [Original](https://jmail.world/drive/vol00011-efta02727130-pdf) |
| [EFTA01705727](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01705727.pdf) | 61,934 | Phone toll records (2005-2006) | [Original](https://jmail.world/drive/vol00010-efta01705727-pdf) |
| [EFTA01705827](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01705827.pdf) | 50,059 | Phone toll records (2005-2006) | [Original](https://jmail.world/drive/vol00010-efta01705827-pdf) |
| [EFTA00184224](https://www.justice.gov/epstein/files/DataSet%209/EFTA00184224.pdf) | ~60,000 | CVRA master case file | [Original](https://jmail.world/drive/vol00009-efta00184224-pdf) |

### Removed Entity Counts (Cross-Referenced)

| Entity Type | Count | Unique Documents |
|-------------|-------|-----------------|
| Phone numbers | 11,287 | 1,838 |
| Email addresses | 10,188 | 6,822 |
| Street addresses | 2,332 | 1,200 |
| Account numbers | 119 | 89 |

---

## 10. Methodology

### Pipeline Architecture

1. **Manifest**: Altered file list from the [geeken.dev archive comparison tool](https://justice.geeken.dev/), which maintains per-document changelogs comparing original DOJ archives against current versions.

2. **PDF download**: Both archived (original) and current versions of each altered file.

3. **Word-level diffing**: Text extraction via PyMuPDF, word-level diff with `SequenceMatcher`. Changes grouped into page-level "change units" — contiguous blocks of related modifications.

4. **Visual verification (v3)**: Both PDF versions rendered at 150 DPI. Pixel-level difference computed per page. Spatial concentration (bounding-box coverage) used to distinguish real content changes (localized, <55% bbox) from OCR reprocessing noise (diffuse, >55% bbox). Run on all 86,979 pages across 100 workers. Of these, 40,870 (47.0%) showed real visual changes; 22,455 (25.8%) were OCR reprocessing noise where the text layer changed but the visible page was identical; 13,808 (15.9%) were pixel-identical. The 51,262 change units on non-changed pages were filtered out before classification.

5. **LLM classification**: Each surviving change unit classified by a 32-billion-parameter language model (Qwen 32B, running locally via vLLM). Classification axes: change type (CONTENT_REMOVAL, NAME_REDACTION, PHONE_REDACTION, etc.) and justification (NON_PII, PRIVACY_ACT_PII, VICTIM_PII, MIXED, AMBIGUOUS). **Caveat**: These are automated assessments, not legal determinations.

6. **Visual inspection**: 2,190 rendered document pairs (64% of 3,441 candidates) visually inspected via Claude to confirm black-bar redactions, page blackouts, and other visual changes. **Additionally, every document cited in this report** (76 rendered pages across 56 documents) was visually verified by rendering the original and current PDFs at 150 DPI and comparing them side by side. This verification revealed that many text-layer changes do not correspond to visible alterations — a critical distinction noted throughout the report.

### Limitations

- **Text-layer degradation vs. visual redaction**: This report distinguishes between two categories of alteration. *Visual redactions* — black bars, page blackouts, content physically removed — are visible to any reader comparing PDFs. *Text-layer degradation* — where the visible page appears identical but the invisible OCR text layer has been corrupted — affects searchability only. We cannot determine from our analysis whether text-layer degradation is intentional or a side effect of OCR re-processing. Both categories are documented, and each cited document is marked accordingly.
- **LLM classification is automated.** The 32B model misclassifies some co-conspirator names as VICTIM_PII and some government employee names as defensible PRIVACY_ACT_PII. The justification breakdown should be treated as approximate.
- **The "original" versions** are from the geeken.dev archive, captured shortly after the January 30, 2026 release.

### Verification

Every EFTA number cited was verified against [`full_text_corpus.db`](https://github.com/rhowardstone/Epstein-research-data/releases) for correct dataset assignment. All DOJ URLs confirmed accessible (HTTP 302 → 200 behind age gate). All JDrive URLs confirmed accessible. Protocol quotes verified against the [DOJ's published memorandum](https://www.justice.gov/media/1426281/dl). Statute quotes verified against the DOJ's [production letter](https://www.justice.gov/opa/media/1426091/dl). **All 56 documents cited in this report were visually verified** by rendering original and current PDF pages at 150 DPI and comparing them side by side. Of 76 rendered pages: 37 showed confirmed visual changes (black bars, page blackouts, content removal); 33 appeared visually identical (text-layer degradation only); 6 showed minor rendering differences with no substantive change. SAR BSA numbers verified from removed text content. Financial figures verified against source text in change units.

---

## 11. See Also

- [DOJ Attorney Review Protocol](https://www.justice.gov/media/1426281/dl) -- the January 4, 2026 memorandum establishing the redaction framework
- [Epstein Files Transparency Act](https://www.congress.gov/119/plaws/publ38/PLAW-119publ38.pdf) -- Pub. L. 119-38, 139 Stat. 656
- [DOJ Epstein Files Portal](https://www.justice.gov/epstein) -- the production site
- [geeken.dev Archive Comparison](https://justice.geeken.dev/) -- the tool that identified altered files
- [Democracy Defenders Fund EFTA Tracker](https://www.democracydefendersfund.org/epstein-files) -- compliance monitoring
- [DOJ Document Removal Audit](../institutional/DEATH_INVESTIGATION_DOCUMENT_REMOVAL.md) -- separate analysis of documents removed entirely (404s), not altered

### Reproducibility Data

The following datasets underlie this report and are [available on GitHub](https://github.com/rhowardstone/Epstein-research-data/tree/main/alteration_analysis) for independent analysis:

| File | Rows | Contents |
|------|------|----------|
| [`change_units_FINAL.csv`](https://github.com/rhowardstone/epstein-research/blob/main/institutional/change_units_FINAL.csv) | 205,958 | Every classified change unit with before/after text, classification, justification, DOJ URL, and JDrive URL |
| [`removed_entities_export.csv`](https://github.com/rhowardstone/Epstein-research-data/blob/main/alteration_analysis/removed_entities_export.csv) | 146,210 | Every entity detected as removed, with corpus hit counts and registry matches |
| [`visual_inspections_final.csv`](https://github.com/rhowardstone/epstein-research/blob/main/institutional/visual_inspections_final.csv) | 2,190 | Claude visual inspection results for rendered document pairs |
| [`alteration_results.db`](https://github.com/rhowardstone/Epstein-research-data/releases) | 212,730 units | Full SQLite database with diff text, pixel-diff results, LLM analyses (183 MB gzipped, in v5.1 release) |

The LLM classifications were produced by a 32B-parameter model and should be treated as automated triage. We encourage researchers to verify individual findings against the source PDFs, which are accessible via both justice.gov and the [JDrive archive](https://jmail.world/drive). Any EFTA cited in this report can be independently compared using the [geeken.dev side-by-side viewer](https://justice.geeken.dev/).

---

*This report analyzes documents in their capacity as public records released under federal transparency law. All names cited are confirmed public figures appearing in official schedules, court filings, or financial regulatory documents. No victim names, pseudonym-to-name mappings, or victim-identifying details are included. Phone numbers are cited only for confirmed public figures whose contact with Epstein is already a matter of public record.*

*The DOJ's alteration of these documents was identified by third-party archive comparison tools and verified through automated text-layer diffing, pixel-level visual verification, and manual PDF inspection. The original (pre-alteration) versions remain accessible through the JDrive archive.*
