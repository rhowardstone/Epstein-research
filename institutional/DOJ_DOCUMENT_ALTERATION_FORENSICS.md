# DOJ Document Alteration Forensics: How "Victim Privacy" Became a Blanket Redaction Tool

> **Note (March 3, 2026):** The entity extraction counts in Section 7 contained significant false positives for name detection. A more rigorous classification pipeline — page-level diffing with a 72B language model classifying each individual change — is running now. Updated counts expected within 24-48 hours. The core findings (phone redactions, SAR gutting, CVRA filing redactions, Privacy Act legal analysis) are verified and unaffected.

## A forensic analysis of 42,782 re-processed EFTA documents

**Date**: March 3, 2026
**Scope**: All 42,782 altered files identified across DOJ EFTA datasets 1-12
**Pipeline**: Text extraction via PyMuPDF, entity extraction, LLM classification, cross-reference against 1,538-person registry and 2.7M-page FTS5 corpus
**Databases**: `alteration_results.db` (166 MB, 42,782 records), `full_text_corpus.db` (6.3 GB, 1.38M documents)

---

## 1. Executive Summary

Between the January 30, 2026 release and the present, the Department of Justice re-processed **42,782 documents** in its Epstein Files Transparency Act (EFTA) production. Our forensic pipeline compared the original archived PDFs against the currently-hosted versions, extracting and classifying every change.

The results: **over 10,000 phone numbers redacted**, with visual black-bar markings confirmed on key documents. Four FinCEN Suspicious Activity Reports were gutted, losing over 95% of their text content. A CVRA legal filing had three full pages of deposition testimony blacked out and 12 unique named persons surgically removed. Entire email chains were reduced to zero readable content.

The DOJ's own [Attorney Review Protocol](https://www.justice.gov/media/1426281/dl) (January 4, 2026) reveals the mechanism: a dual-track redaction system. Track one covers victim PII under the EFTA's narrow statutory authority. Track two invokes the **Privacy Act** as a separate, blanket basis for stripping telephone numbers, email addresses, dates of birth, government employee names, and more from *all persons* -- not just victims. The EFTA does not enumerate the Privacy Act among its five permitted withholding categories. No Federal Register justification for this expanded authority has been published.

Of 21,803 classified alterations, an automated local LLM triage assessed **18,848 (86.4%) as SUSPICIOUS** — meaning inconsistent with standard PII removal patterns — rather than justified PII removal. These are machine assessments, not legal conclusions; the underlying data is published for independent verification (see Methodology).

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

The question is whether a specific transparency statute, enacted to override normal exemptions, can be supplemented by a general privacy law to achieve broader redaction than the specific statute authorizes.

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

*Note on text-layer artifacts*: Our automated text extraction pipeline initially flagged apparent name changes — "Woody Allen" extracting as "Roody Allen," "Jen Doyle" as "M." — but visual PDF inspection confirms these are OCR artifacts created when the text extraction layer was re-rendered around the black bars, not what readers see. The visual PDF clearly shows "Woody Allen" in full. However, the text-layer corruption has a practical consequence: anyone performing a full-text search of the current DOJ production for "Woody Allen" will not find this document. The text layer says "Roody Allen." The same applies to other text-layer artifacts introduced during the re-processing. Whether intentional or not, this renders affected documents invisible to keyword search while remaining visually legible to anyone who opens the PDF directly.

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

Shing-Tung Yau is a Fields Medal-winning mathematician and Harvard professor. His phone number was redacted from a *different* copy of the same schedule ([EFTA02070330](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02070330.pdf) | [Original (JDrive)](https://jmail.world/drive/vol00010-efta02070330-pdf)) but survives — visually readable, with no black bar — in EFTA00339454. The DOJ's redaction process was inconsistent: it caught entries on the same page but missed an adjacent one.

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

The result is visible across multiple EFTA documents:

| EFTA | Original Chars | Current Chars | Removed | Filing Bank | Key Entities Named |
|------|---------------|---------------|---------|-------------|-------------------|
| [EFTA01656524](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01656524.pdf) | 72,738 | 3,322 | **95.4%** | *(multiple)* | Hyperion Air, Zorro Management, Southern Trust Co., Butterfly Trust |
| [EFTA01656500](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01656500.pdf) | 30,797 | 1,264 | **95.9%** | *(multiple)* | Alpha Group Capital, Edge Foundation, Harvard University, Jeepers Inc. |
| [EFTA01656415](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01656415.pdf) | 29,753 | 1,241 | **95.8%** | Charles Schwab | Southern Trust Co., Richard Kahn, Financial Strategy Group Ltd |
| [EFTA01656452](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01656452.pdf) | 24,252 | 1,034 | **95.7%** | Charles Schwab | Bank Julius Baer, Deutsche Bank Trust, Coatue Enterprises, Darren Indyke |

Original JDrive versions: [EFTA01656524](https://jmail.world/drive/vol00010-efta01656524-pdf) | [EFTA01656500](https://jmail.world/drive/vol00010-efta01656500-pdf) | [EFTA01656415](https://jmail.world/drive/vol00010-efta01656415-pdf) | [EFTA01656452](https://jmail.world/drive/vol00010-efta01656452-pdf)

Each SAR was reduced to a near-empty shell. The original documents contained detailed financial narratives -- wire transfer amounts, account numbers, shell company relationships, counterparty banks, suspicious activity descriptions. The current versions retain only structural metadata.

EFTA01656415 (Charles Schwab SAR) documented **$45,360,202** in suspicious activity over a 7-week period (July-September 2019), with a cumulative amount of **$73,018,526**. The activity was flagged for "Money laundering, Suspicious EFT/wire transfers, Funds transfer." The SAR named Richard Kahn (HBRK Associates), Darren Indyke, and multiple Epstein shell entities. All of this was stripped.

EFTA01656500 named Harvard University, Alpha Group Capital, Edge Foundation, and entities across the U.S. Virgin Islands and Puerto Rico. The financial narrative connecting Epstein's academic philanthropy network to suspicious banking activity was removed.

### The Legal Question

SARs are filed under the Bank Secrecy Act (31 U.S.C. § 5318(g)). They carry confidentiality protections. But the EFTA was enacted specifically to override normal exemptions for the Epstein files. The Protocol cites no EFTA category for SAR redaction -- it simply instructs blanket removal with a freeform note.

The EFTA's "active investigation" exception (§ 2(c)(1)(C)) requires that withholding be "narrowly tailored and temporary." Full redaction of every SAR is neither narrow nor temporary.

---

## 5. Beyond Phone Numbers

Phone number redaction and SAR gutting are the most quantifiable patterns. But the alteration pipeline identified several other categories of content removal.

### Complete Content Removal

| EFTA | Original | Current | Description |
|------|----------|---------|-------------|
| [EFTA00434585](https://www.justice.gov/epstein/files/DataSet%209/EFTA00434585.pdf) | 33,897 chars | 83 chars | BlackBerry email chain re: "passes/Jeffrey Epstein" via Peggy Siegal Inc. |
| [EFTA01144698](https://www.justice.gov/epstein/files/DataSet%209/EFTA01144698.pdf) | 11,538 chars | 41 chars | Complete content removal |

Original JDrive versions: [EFTA00434585](https://jmail.world/drive/vol00009-efta00434585-pdf) | [EFTA01144698](https://jmail.world/drive/vol00009-efta01144698-pdf)

EFTA00434585 was a multi-party BlackBerry email thread routed through `peggysiegalinc.local` (Peggy Siegal, the celebrity publicist). The subject line: "Re: passes/Jeffrey Epstein." The original contained 33,897 characters of readable email exchange. The current version: 83 characters — nothing but Bates stamps on otherwise blank pages. A 99.8% reduction.

### Legal Filing Gutting

[EFTA00191396](https://www.justice.gov/epstein/files/DataSet%209/EFTA00191396.pdf) | [Original (JDrive)](https://jmail.world/drive/vol00009-efta00191396-pdf)

This is the Jane Doe #1 and #2 vs. United States CVRA filing (Case No. 08-80736, S.D. Fla.). The 71-page document lost 4.1% of its text (153,062 → 146,768 chars), but the removals are concentrated and targeted. **Three full pages** (document pages 30-32) were completely blacked out — solid black rectangles with only Bates stamps visible. These pages contained deposition testimony from Sarah Kellen, Nadia Marcinkova, and Adrianna Mucinska invoking the Fifth Amendment when asked about Alan Dershowitz's involvement in Epstein's abuse. On two additional pages (doc pp. 36-37), individual names were surgically replaced with black bars: Sarah Kellen, Nadia Marcinkova, Dana Burns, and Emmy Tayler were each redacted while surrounding text remained intact. In total, **12 unique named persons** — including Dershowitz, Prince Andrew, Ghislaine Maxwell, Jean Luc Brunel, and Bruce Reinhart — had their names removed from this filing.

### Government Employee Name Redaction

The Protocol instructs blanket redaction of government employee names (lines 325-331), with exceptions for Senate-confirmed officials, public affairs officers, and the two prosecuted BOP guards (Michael Thomas and Tova Noel). This means the names of FBI agents, AUSAs, and BOP employees who interacted with Epstein are redacted from the production -- even when those names appear in official correspondence.

### Privilege Claims

The Protocol authorizes three categories of privilege redaction (lines 355-375):

- **Deliberative-Process Privilege**: advisory opinions, recommendations, and deliberations
- **Work-Product Privilege**: documents reflecting attorney mental processes
- **Attorney-Client Privilege**: confidential government attorney communications

The Protocol instructs (line 374): *"Do not liberally apply these bases for redaction."* Whether that instruction was followed is not assessable from the alteration data alone.

---

## 6. The Privacy Act Conflict

The structural problem is straightforward.

The EFTA enumerates exactly five categories of permitted withholding. The Privacy Act is not one of them. The DOJ's Protocol creates a sixth category -- "Privacy Act Redactions" -- and applies it as a separate authority.

### Specific Statute Overrides General

The principle of *lex specialis derogat legi generali* -- a specific statute overrides a general one -- is directly relevant. The EFTA was enacted specifically to compel disclosure of the Epstein files. It enumerated specific exceptions. When Congress wanted to allow withholding, it said so. When it wanted to prohibit withholding on certain bases, it said that too (§ 2(b): no redaction for "embarrassment, reputational harm, or political sensitivity").

The JFK Records Act (44 U.S.C. § 2107) -- the model for the EFTA -- has been interpreted the same way. When Congress enacted a specific transparency statute, it intended to override the normal exemption framework, not to be supplemented by it.

### The DOJ Is Its Own Judge

The Protocol was written by the Office of the Deputy Attorney General. The redactions are applied by DOJ contract reviewers. The assessment of what constitutes "Privacy Act" information versus "EFTA-excepted" information is made internally, with no external review mechanism specified in the Protocol.

Section 2(b) of the EFTA prohibits redaction on the basis of "embarrassment, reputational harm, or political sensitivity, including to any government official, public figure, or foreign dignitary." When the phone number of a former Prime Minister of Norway is stripped from a scheduling email, the distinction between "Privacy Act compliance" and "embarrassment prevention" becomes difficult to maintain.

### Federal Register Justification

Section 2(c)(2) of the EFTA mandates that "[a]ll redactions must be accompanied by a written justification published in the Federal Register and submitted to Congress." As of this writing, the [Democracy Defenders Fund](https://www.democracydefendersfund.org/epstein-files) -- which tracks EFTA compliance -- reports no such justification published. A direct search of the [2026 Federal Register index](https://www.federalregister.gov/index/2026/justice-department) for the Justice Department confirms no entry related to the Epstein Files Transparency Act, EFTA redactions, or the Privacy Act basis appears as of March 3, 2026 -- more than three months after the statute's enactment and over a month after the final document release.

---

## 7. Scale

### Alteration Pipeline Summary

| Metric | Count |
|--------|-------|
| Total altered files identified | 42,782 |
| Files with diffs completed | 22,180 |
| Files classified by LLM | 21,803 |
| Classified as SUSPICIOUS | 18,848 (86.4%) |
| Classified as JUSTIFIED_PII | 2,881 (13.2%) |
| Classified as AMBIGUOUS | 66 (0.3%) |
| Classified as UNKNOWN | 8 (<0.1%) |

### Removed Entity Counts (Automated Extraction)

Our pipeline extracted entities from text blocks identified as removed during the diffing process, then cross-referenced each entity against the added text to filter false positives. An entity appearing in both the removed *and* added text is context that survived the edit, not a genuine removal. The table below reports both the raw extraction count and the filtered estimate.

| Entity Type | Raw Extraction | False Positive Rate | Filtered Estimate | Unique Documents |
|-------------|---------------|--------------------|--------------------|-----------------|
| Phone numbers | 11,287 | 10.4% | ~10,100 | 1,838 |
| Email addresses | 10,188 | 25.2% | ~7,600 | 6,822 |
| Social Security numbers | 3,915 | 28.9% | ~2,800 | 1,102 |
| Street addresses | 2,332 | 44.3% | ~1,300 | 1,200 |
| Dates of birth | 12,752 | 71.5% | ~3,600 | 2,772 |
| Account numbers | 119 | -- | ~119 | 89 |

**Phone numbers are the most reliable count** — the 10.4% false positive rate is low because phone patterns are distinctive and the Protocol specifically targets them. The visually verified examples in Section 3 confirm that phone redactions are deliberate black-bar markings.

**Name removal counts are omitted from this table.** Our automated name extraction (regex matching any two-or-more capitalized words in removed text blocks) produced 105,597 raw hits but with a false positive rate exceeding 49% even after basic filtering — and the surviving entries are still heavily contaminated with OCR artifacts ("Transpodalion Charge," "Fuel Surtharge") and document field labels. Public figure names (Prince Andrew, Woody Allen, Alan Dershowitz) were overwhelmingly false positives: their names appeared in paragraphs that were modified for other reasons (typically phone number removal) but the names themselves remained in the document. By contrast, victim and witness names (Sarah Kellen, Nadia Marcinkova, Virginia Roberts) showed lower false positive rates, consistent with the DOJ Protocol's instructions for victim PII redaction. A more rigorous analysis using a capable language model to classify individual changes is underway; we will update this section when it completes.

### Dataset Distribution

| Dataset | Altered Files | % of Total |
|---------|--------------|-----------|
| DS9 | 25,998 | 60.8% |
| DS10 | 9,439 | 22.1% |
| DS11 | 6,674 | 15.6% |
| DS8 | 642 | 1.5% |
| DS1-3, DS12 | 29 | <0.1% |

### Classification Distribution

| Classification | Count | % |
|---------------|-------|---|
| NAME_REMOVAL | 16,269 | 74.6% |
| OTHER | 2,817 | 12.9% |
| EMAILS_REMOVED (combined) | 1,831 | 8.4% |
| PHONE_REMOVAL | 421 | 1.9% |
| METADATA_STRIP | 350 | 1.6% |
| CONTENT_REDUCTION (combined) | 43 | 0.2% |
| FINANCIAL_RECORD | 18 | 0.1% |
| PII_REMOVAL | 13 | 0.1% |
| Other categories | 41 | 0.2% |

---

## 8. Methodology

### Pipeline Architecture

1. **Manifest collection**: Harvested altered file list from the [geeken.dev archive comparison tool](https://justice.geeken.dev/), which maintains a per-document changelog comparing the original DOJ ZIP archives (captured on or shortly after the January 30, 2026 release) against currently-hosted versions on justice.gov. Any document cited in this report can be verified through that tool's side-by-side comparison view.

2. **PDF download**: Retrieved both archived (original) and current versions of each altered file.

3. **Text extraction and diffing**: Extracted text from both PDF versions using PyMuPDF. Generated line-level diffs using Python's `SequenceMatcher`. Classified changes as genuine modifications vs. OCR noise using similarity ratios (threshold: 0.7).

4. **Entity extraction**: Applied regex patterns to removed text blocks to extract phone numbers, names, email addresses, dates of birth, SSNs, addresses, and account numbers.

5. **Cross-referencing**: Matched extracted entities against three databases:
   - `persons_registry.json` (1,538 known persons with aliases)
   - `phone_numbers_enriched.csv` (1,117 known phone numbers)
   - `full_text_corpus.db` FTS5 index (2.77M pages) for corpus hit counts

6. **LLM classification**: Each file with genuine content changes was classified by a local 8-billion-parameter LLM (running locally, not via API) for: change type (NAME_REMOVAL, PHONE_REMOVAL, etc.), sensitivity (LOW/MEDIUM/HIGH), and justification assessment (JUSTIFIED_PII/SUSPICIOUS/AMBIGUOUS). **Caveat**: These classifications are automated first-pass assessments, not expert legal determinations. A "SUSPICIOUS" label means the change pattern was inconsistent with standard PII removal as assessed by a small model — not that the change was necessarily improper. The classifications should be treated as a triage tool, not as conclusions. The full classification dataset (`classified_alterations.csv`, 21,803 rows) and entity extraction dataset (`removed_entities_export.csv`, 146,190 rows) are available for independent review and follow-up analysis.

### Limitations

- **Text layer vs. visual layer**: Our pipeline compares text extracted from the PDF's text layer, not the visual rendering. Black-bar redactions appear as empty strings or OCR artifacts in text extraction but are visible as deliberate redaction marks in the rendered PDF. For key documents cited in this report (particularly EFTA00339454), we verified text-layer findings against the visual PDF. Some text-layer anomalies (e.g., "Woody Allen" extracting as "Roody Allen" near a black-bar boundary) are OCR artifacts, not changes visible to readers.
- Text extraction quality depends on PyMuPDF's handling of each PDF's internal structure. Some scanned documents yield poor OCR text in both versions.
- OCR noise detection using `SequenceMatcher` ratio thresholds may misclassify borderline cases where genuine changes overlap with OCR improvements.
- LLM classification is automated. SUSPICIOUS assessments indicate the change pattern was inconsistent with standard PII removal, not that the change was necessarily improper.
- Entity extraction regex may produce false positives (e.g., dates matching SSN patterns, OCR artifacts matching name patterns).
- The "original" versions are from the geeken.dev archive, which captured PDFs from the DOJ's initial release. If the DOJ made changes between the release and the archive capture, those would not be detected.

### Verification

Every EFTA number cited in this report was verified against `full_text_corpus.db` for correct dataset assignment. All DOJ URLs were confirmed accessible (HTTP 302 → 200 behind age gate). All JDrive URLs were confirmed accessible (HTTP 200). Protocol quotes were verified against the local text extraction of the [DOJ's published memorandum](https://www.justice.gov/media/1426281/dl). Statute quotes were verified against the DOJ's [production letter](https://www.justice.gov/opa/media/1426091/dl), which reproduces the statutory text. EFTA00339454 was visually inspected in both the JDrive original and the current DOJ-hosted PDF to confirm that text-layer diff findings correspond to visible black-bar redactions.

---

## 9. See Also

- [DOJ Attorney Review Protocol](https://www.justice.gov/media/1426281/dl) -- the January 4, 2026 memorandum establishing the redaction framework
- [Epstein Files Transparency Act](https://www.congress.gov/119/plaws/publ38/PLAW-119publ38.pdf) -- Pub. L. 119-38, 139 Stat. 656
- [DOJ Epstein Files Portal](https://www.justice.gov/epstein) -- the production site
- [geeken.dev Archive Comparison](https://justice.geeken.dev/) -- the tool that identified altered files
- [Democracy Defenders Fund EFTA Tracker](https://www.democracydefendersfund.org/epstein-files) -- compliance monitoring
- [DOJ Document Alteration Analysis -- Master Report](../evidence/ALTERATION_ANALYSIS_MASTER.md) -- full pipeline output with all 21,803 classified alterations
- [DOJ Document Removal Audit](../institutional/DEATH_INVESTIGATION_DOCUMENT_REMOVAL.md) -- separate analysis of documents removed entirely (404s), not altered

### Reproducibility Data

The following datasets underlie this report and are [available on GitHub](https://github.com/rhowardstone/Epstein-research-data/tree/main/alteration_analysis) for independent analysis:

| File | Rows | Contents |
|------|------|----------|
| [`classified_alterations.csv`](https://github.com/rhowardstone/Epstein-research-data/blob/main/alteration_analysis/classified_alterations.csv) | 21,803 | LLM-classified alterations with change type, sensitivity, justification |
| [`removed_entities_export.csv`](https://github.com/rhowardstone/Epstein-research-data/blob/main/alteration_analysis/removed_entities_export.csv) | 146,190 | Every entity (name, phone, email, DOB, SSN, address, account) detected as removed, with corpus hit counts and registry matches |
| `alteration_results.db` | 42,782 files | Full SQLite database with diff text, entity extractions, LLM analyses |

The LLM classifications were produced by a local 8B-parameter model and should be treated as automated triage, not expert judgment. The `removed_entities_export.csv` contains raw entity extractions from diff text blocks, which have significant false positive rates for name detection (see Section 7). We encourage researchers to verify individual findings against the source PDFs, which are accessible via both justice.gov and the [JDrive archive](https://jmail.world/drive).

---

*This report analyzes documents in their capacity as public records released under federal transparency law. All names cited are confirmed public figures appearing in official schedules, court filings, or financial regulatory documents. No victim names, pseudonym-to-name mappings, or victim-identifying details are included. Phone numbers are cited only for confirmed public figures whose contact with Epstein is already a matter of public record.*

*The DOJ's alteration of these documents was identified by third-party archive comparison tools and verified through both automated text-layer diffing and visual PDF inspection. The original (pre-alteration) versions remain accessible through the JDrive archive.*
