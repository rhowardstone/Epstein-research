# The Hidden Numbering System: What Secondary Bates Stamps Reveal About the Epstein File Production

## Summary

The DOJ's Epstein Files production contains a hidden layer of information: secondary Bates numbering stamps on individual pages that reveal how documents were sourced, processed, and filtered before public release.

Analysis of these stamps across Datasets 9 through 12 identifies multiple distinct document streams, each with its own pre-production numbering system. Two numbering systems are independently trackable:

1. **EFTA_R1_** (FBI device extractions, DS10/DS11): 2.21 million pages reviewed, 970,000 released (43.8%), **1.26 million withheld (57.0%)**
2. **EFTA_** (SDNY production sequence, DS9/DS10): 269,394 pages reviewed, 67,493 released (25.1%), **201,901 withheld (74.9%)**

Combined, the two trackable systems reveal **1.46 million pages** that were reviewed and stamped but not included in the public production.

## How This Was Found

Many pages in the EFTA production carry not just their final EFTA production number (e.g., `EFTA01927584`) but also one or more secondary stamps immediately above it. These secondary stamps use different formats depending on where the document originated. A typical page might look like:

```
3501.000-121                                           [discovery reference]
SUBJECT TO PROTECTIVE ORDER PARAGRAPHS 7, 8, 9, 10    [court order]
SDNY_00006393                                          [SDNY case number]
EFTA_00000478                                          [earlier EFTA number]
EFTA00134897                                           [final EFTA number]
```

The secondary stamps were extracted from the OCR text layer of 2.56 million pages across DS9, DS10, DS11, and DS12 using pattern matching against the `full_text_corpus.db` database. 1,192,725 pages carry at least one identifiable secondary stamp.

## The Numbering Systems

### System 1: EFTA_R1_ (FBI Device Extractions)

**968,304 pages across 645,222 documents in DS10/DS11**

The largest system. Pages carry a stamp in the format `EFTA_R1_00374571`, where the 8-digit number represents the page's position in the "R1" (Release 1 or Review 1) numbering sequence.

**Content:** Emails and messages extracted from Epstein's electronic devices and cloud accounts. The communications use the `jeevacation@gmail.com` email address (Epstein's personal Gmail) and include personal emails between Epstein and associates, staff communications (Lesley Groff, Ann Rodriquez), iMessage extractions (identifiable by Apple plist XML metadata), and sent/received correspondence with named individuals.

**Distribution:** DS10 (323,539 docs) and DS11 (321,683 docs). DS11 is 97% R1-stamped material.

**Gap analysis:**

| Metric | Value |
|--------|-------|
| R1 number range | 11 to 2,214,168 |
| Total R1 positions (span) | 2,214,161 pages |
| Pages actually produced | 969,970 |
| Pages withheld (gaps in R1 sequence) | 1,262,316 |
| Withholding rate | 57.0% |
| Number of separate gaps | 240,799 |
| Largest single gap | 19,937 consecutive pages |

The 240,799 gaps break down as:

| Gap size | Number of gaps | Total missing pages |
|----------|---------------|-------------------|
| 1-5 pages | 193,506 | 408,925 |
| 6-20 pages | 41,165 | 389,962 |
| 21-100 pages | 5,291 | 195,498 |
| 101-500 pages | 775 | 139,301 |
| 501-2,000 pages | 44 | 39,419 |
| 2,001-10,000 pages | 17 | 69,274 |
| 10,001+ pages | 1 | 19,937 |

The majority of gaps are small (1-5 pages), consistent with individual emails or short threads removed during review. The withholding rate is uniform across the entire R1 corpus, with every 100,000-page region having between 37,000 and 89,000 pages withheld. No R2, R3, or subsequent review stamps exist.

### System 2: EFTA_ (SDNY Production Sequence)

**79,419 pages across 10,850 documents in DS9/DS10/DS11/DS12**

A separate system from R1. Pages carry a stamp in the format `EFTA_00057769` (underscore, no "R1" prefix). This numbering begins at `EFTA_00000001`, which appears on a Bureau of Prisons money transfer report from MCC New York ([EFTA00134541](https://www.justice.gov/epstein/files/DataSet%209/EFTA00134541.pdf)). It is the literal first page of the SDNY production.

**Content:** BOP custody records, MCC commissary receipts, inmate housing logs, FBI 302s, confidential human source reports (FD-1023), victim correspondence, protective-order material from the Maxwell case, and SDNY investigative files.

**Distribution:** DS9 (18,491 pages), DS10 (59,174 pages), DS11 (1,563 pages), DS12 (191 pages).

**Gap analysis:**

| Metric | Value |
|--------|-------|
| EFTA_ number range | 0 to 269,393 |
| Pages present | 67,493 |
| Pages missing (gaps) | 201,901 |
| Coverage | 25.1% |
| Withholding rate | 74.9% |

The SDNY production sequence has a higher withholding rate than R1. Only one in four pages from the original SDNY production appears in the public EFTA release. The densest coverage is in the 120,000-160,000 range (30-52% present); the sparsest is in the 30,000-50,000 range (under 1% present).

Many EFTA_ pages also carry an `SDNY_` case number (e.g., `SDNY_00006393`) that increments alongside the EFTA_ number but is offset by one, confirming the two systems were applied to the same pages simultaneously.

### System 3: JPM-SDNY- (JPMorgan Chase Bank Records)

**50,319 pages across ~49,000 documents, primarily in DS10**

Pages carry a stamp like `JPM-SDNY-00063190` along with the header "Confidential Treatment Requested by JPMorgan Chase." These are bank records produced by JPMorgan Chase in response to SDNY subpoenas.

**Content:** Account statements, transaction records, KYC documents, internal bank correspondence, wire transfer records, and compliance documents related to Epstein's JPMorgan accounts.

**Location:** Concentrated in DS10 (49,870 pages) with 449 pages in DS9, in the EFTA 1,299,930 to 1,656,686 range. 86% of these documents also carry SDNY_GM stamps.

### System 4: DB-SDNY- (Deutsche Bank Records)

**68,041 pages across ~55,000 documents, primarily in DS10**

Pages carry a stamp like `DB-SDNY-0000085`. These are bank records produced by Deutsche Bank in response to SDNY subpoenas. (OCR frequently misreads "DB" as "OB", "DI3", or "06".)

**Content:** Account records, correspondence, compliance documents, and transaction records related to Epstein's Deutsche Bank accounts (including the Butterfly Trust and other entities).

**Location:** Concentrated in DS10 (64,232 pages) with 3,809 pages in DS9, in the EFTA 1,282,009 to 1,462,305 range. Most also carry SDNY_GM stamps.

### System 5: SDNY_GM (Maxwell Case Stamps)

**185,165 pages across ~115,000 documents**

Pages carry a stamp like `SDNY_GM_00278490`. "GM" refers to Ghislaine Maxwell. This stamp was applied by the SDNY prosecution team during the Maxwell case (United States v. Maxwell).

Unlike the other systems, SDNY_GM frequently appears alongside bank stamps. 42,603 documents carry both JPM-SDNY and SDNY_GM stamps. 54,064 carry both DB-SDNY and SDNY_GM stamps. Only ~16,000 documents carry SDNY_GM as their sole secondary stamp; these represent the prosecution team's own investigative files.

### System 6: 3501.xxx-xxx (Discovery References)

**5,023 pages across ~1,178 documents in DS9**

A litigation support reference number in the format `3501.045-008`. These appear alongside the `EFTA_` and `SDNY_` stamps on protective-order material. The `3501` prefix is the FBI case file serial numbering for the Epstein/Maxwell investigation — each serial represents one witness, victim, or investigative thread. These documents are consistently marked `SUBJECT TO PROTECTIVE ORDER PARAGRAPHS 7, 8, 9, 10, 15, and 17` from the Maxwell case.

For a detailed analysis of the 3501 serial system — including which FBI interview records (FD-302s) are present versus missing from the production — see [Missing FBI 302s: A Gap Analysis](FBI_302_MISSING_SERIALS_DOSSIER.md). That analysis identifies 136 interview serials, 3 with zero documents in the production, and demonstrates (using serial 3501.045 as a case study) that more than half the sub-records listed in the government's own disclosure index do not appear in the published files.

## How the Streams Relate

The stamps reveal a layered production pipeline. Documents flowed through multiple organizations, each applying their own numbering, before receiving final EFTA production numbers.

**Bank records** were first stamped by the producing bank (JPM-SDNY or DB-SDNY), then received and re-stamped by the SDNY Maxwell prosecution team (SDNY_GM), and finally assigned EFTA production numbers. These are concentrated in DS10.

**SDNY investigative files** (BOP records, FBI reports, victim correspondence) were stamped with SDNY case numbers and EFTA_ sequential numbers simultaneously, then some received discovery references (3501.xxx) during litigation review, and finally all were assigned final EFTA production numbers. These span DS9 and DS10.

**FBI device extractions** (emails, iMessages) followed a separate path through the R1 review process before receiving EFTA production numbers. These appear in the upper range of DS10 and nearly all of DS11.

**Near-zero overlap exists between the R1 stream and the SDNY/bank streams.** Only 14 documents out of 645,222 carry both EFTA_R1_ and any other secondary stamp — likely OCR artifacts. These were independent processing pipelines that were merged at the final production stage.

## Combined Withholding Analysis

| System | Source | Pages Reviewed | Pages Released | Pages Withheld | Rate |
|--------|--------|---------------|----------------|----------------|------|
| EFTA_R1_ | FBI extractions | 2,214,161 | 969,970 | 1,262,316 | 57.0% |
| EFTA_ | SDNY production | 269,394 | 67,493 | 201,901 | 74.9% |
| **Total** | | **2,483,555** | **1,037,463** | **1,464,217** | **58.9%** |

1.46 million pages were reviewed and numbered but not included in the public production. This figure covers only the two systems where gap analysis is possible. The bank stamps (JPM-SDNY, DB-SDNY) and the SDNY_GM stamps do not lend themselves to the same gap analysis because we cannot determine their original production span.

**Possible explanations for the gaps include:**

- Attorney-client privilege (communications with lawyers)
- Grand jury secrecy (Rule 6(e) material)
- Duplicate documents (the same email extracted from multiple devices/folders)
- Material outside the production scope
- Protective order restrictions
- Law enforcement sensitivity (ongoing investigations)

The uniform distribution of R1 gaps is consistent with systematic review processes such as deduplication and privilege screening. The higher withholding rate in the SDNY production (74.9% vs 57.0%) may reflect the different nature of the material (investigative files vs. email) or different review criteria.

## Data Files

The complete cross-reference data is available as CSV files suitable for analysis in Excel or any spreadsheet tool:

- **`all_secondary_stamps.csv`** (1,192,725 rows): Every page in DS9-12 that carries a secondary stamp, with columns for all six numbering systems. One row per page.
- **`r1_crossref.csv`** (645,222 rows): Document-level R1 mapping (page 0 only), with EFTA number, R1 number, dataset, and page count.
- **`efta_underscore_crossref.csv`** (68,406 rows): EFTA_ (SDNY sequence) mapping with final EFTA number, page number, EFTA_ number, and SDNY_ number.

Column definitions for `all_secondary_stamps.csv`:

| Column | Description |
|--------|-------------|
| final_efta | The published EFTA production number |
| dataset | Dataset number (9, 10, 11, or 12) |
| total_pages | Total pages in this document |
| page_number | Page number within the document (0-indexed) |
| r1_number | EFTA_R1_ stamp number (FBI review sequence) |
| sdny_efta_number | EFTA_ stamp number (SDNY production sequence) |
| sdny_case_number | SDNY_ stamp number (SDNY case sequence) |
| jpm_sdny_number | JPM-SDNY- stamp number (JPMorgan production) |
| db_sdny_number | DB-SDNY- stamp number (Deutsche Bank production) |
| sdny_gm_number | SDNY_GM_ stamp number (Maxwell case) |
| discovery_ref | 3501.xxx-xxx discovery reference |

## Methodology

All analysis was performed against `full_text_corpus.db`, a 6.3 GB SQLite database containing OCR-extracted text from all 2,770,154 pages of the EFTA production. Secondary stamps were identified using regular expression pattern matching against the text layer of each page. OCR artifacts (misread characters, spacing errors) were accounted for using fuzzy matching patterns that tolerate common OCR substitutions (D/O, B/6/I3, N/M, Y/C).

For R1 gap analysis, each document's R1 stamp on page 0 was treated as the starting page number, and the document's total page count was used to determine the R1 range it occupies. For EFTA_ gap analysis, each individual page's stamp was used directly since the EFTA_ numbers increment per-page.

A small number of outlier values (154 R1 numbers above 3,000,000 and 110 EFTA_ numbers above 400,000) were excluded as likely OCR errors where extra digits were appended to the stamp. The core ranges (R1: 11-2,214,168; EFTA_: 0-269,393) contain 99.8% of all detected stamps and are internally consistent.

---

## See Also

- **[Missing FBI 302s: A Gap Analysis](FBI_302_MISSING_SERIALS_DOSSIER.md)** — Detailed analysis of the `3501.xxx` serial system (System 6 above), identifying specific FBI interview records that the government's own indices say exist but that do not appear in the production.
- **[Corpus Inventory](../methodology/CORPUS_INVENTORY.md)** — Complete evidence chain for the 1,380,937 PDFs and 2,731,785 pages that make up the EFTA production.

---

*This analysis relies on Claude Code running Opus 4.6, which can make mistakes. All underlying data is available for independent verification.*
