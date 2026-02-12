# Corpus Inventory & Evidence Chain

## What This Document Is

This is the foundational accounting of every piece of source material underlying this
investigation. Every report in this repository traces back to specific documents within
the corpus described here. If you want to verify a claim, this is where you start.

**Bottom line:** 1,380,937 PDF documents containing 2,731,785 pages and 3.18 billion
characters of text, plus 3,234 media files, 1,530 audio/video transcripts, 2,587,102
redaction records, and a 1,536-person entity registry. All derived from 194.5 GB of
publicly released U.S. Department of Justice files.

---

## Source Material

All source data was released by the U.S. Department of Justice at
[justice.gov/epstein](https://www.justice.gov/epstein/) between December 2025 and
February 2026. Bulk downloads were obtained from [archive.org](https://archive.org)
mirrors of the DOJ release. No data was obtained through leaks, hacking, FOIA requests,
or any non-public channel.

### DOJ Release Timeline

| Dataset | Release Date | Size | Format |
|---------|-------------|------|--------|
| DS1-7 | December 19, 2025 | ~3.0 GB | Individual PDFs on justice.gov |
| DS8 | January 17, 2026 | ~1.8 GB | ZIP archive |
| DS9 | January 30, 2026 | ~103.6 GB | tar.bz2 archive |
| DS10 | February 3, 2026 | ~68.3 GB | ZIP archive |
| DS11 | February 6, 2026 | ~26.8 GB | ZIP archive |
| DS12 | February 10, 2026 | ~0.1 GB | Individual PDFs |

---

## Complete Document Inventory

### PDF Documents by Dataset

| DS | Documents | Pages | Characters | Size (GB) | EFTA Range | Blank Pages |
|----|----------:|------:|-----------:|----------:|------------|------------:|
| 1 | 3,156 | 3,156 | 171,072 | 1.24 | EFTA00000001 – EFTA00003158 | 0 |
| 2 | 574 | 699 | 46,593 | 0.62 | EFTA00003159 – EFTA00003857 | 0 |
| 3 | 67 | 1,847 | 275,943 | 0.58 | EFTA00003858 – EFTA00005586 | 0 |
| 4 | 152 | 2,704 | 3,364,909 | 0.35 | EFTA00005705 – EFTA00008320 | 0 |
| 5 | 120 | 120 | 46,862 | 0.06 | EFTA00008409 – EFTA00008528 | 0 |
| 6 | 13 | 487 | 491,355 | 0.05 | EFTA00008529 – EFTA00008998 | 0 |
| 7 | 17 | 660 | 720,756 | 0.10 | EFTA00009016 – EFTA00009664 | 0 |
| 8 | 10,593 | 29,343 | 38,733,380 | 1.78 | EFTA00009676 – EFTA00039023 | 0 |
| 9 | 531,284 | 1,223,761 | 1,557,581,456 | 94.51 | EFTA00039025 – EFTA01262781 | 32 |
| 10 | 503,154 | 950,101 | 1,060,544,619 | 68.32 | EFTA01262782 – EFTA02212882 | 0 |
| 11 | 331,655 | 517,382 | 513,671,715 | 26.75 | EFTA02212883 – EFTA02730262 | 0 |
| 12 | 152 | 1,525 | 1,658,327 | 0.12 | EFTA02730265 – EFTA02731783 | 0 |
| **Total** | **1,380,937** | **2,731,785** | **3,177,306,987** | **194.5** | EFTA00000001 – EFTA02731783 | **32** |

**Disk-to-database reconciliation:** Every PDF file on disk has a corresponding entry
in the database. Zero discrepancies across 11 of 12 datasets. DS8 has one duplicate
file (EFTA00022173 exists in two subdirectories at identical size — a packaging artifact,
not a data issue).

### EFTA Number Gaps

EFTA numbers are not contiguous. The DOJ did not release every number — there are gaps
within each dataset's range. For example, DS9 spans EFTA00039025 to EFTA01262781
(a range of 1,223,757 possible numbers) but contains only 531,284 documents. These gaps
are part of the DOJ's release structure, not missing data on our end. The same pattern
holds across all datasets.

### Media Files (Non-PDF)

| Type | Count | Primary Location | Description |
|------|------:|-----------------|-------------|
| .avi | 1,529 | DS9 | MCC/surveillance video clips (no audio) |
| .mp4 | 255 | DS8, DS9 | Surveillance video, longer-form recordings |
| .m4a | 78 | DS9 | Audio recordings (phone calls, interviews) |
| .vob | 10 | DS9 | DVD video objects |
| .m4v | 10 | DS9 | Video files |
| .wav | 9 | DS9 | Audio recordings |
| .mov | 8 | DS9 | QuickTime video |
| .wmv | 5 | DS9 | Windows Media video |
| .mp3 | 2 | DS9 | Audio files |
| .xlsx/.xls | 11 | DS8 | Spreadsheets (victim pseudonym lists, device inventories) |
| .csv | 4 | DS8 | Fully redacted tabular data (every cell blacked out) |
| Other | ~322 | DS8, DS10, DS11 | Miscellaneous native files |
| **Total** | **~3,234** | | |

### Zero-Page Documents (Corrupted/Non-Standard PDFs)

Five documents across the entire corpus returned zero extractable pages from standard
PDF tools. Byte-level forensic analysis revealed these are not simply corrupted — they
are forensic disk image fragments and truncated scans. All five have been recovered.
See [CORRUPTED_PDF_FORENSICS](../evidence/CORRUPTED_PDF_FORENSICS.md) for full details.

| EFTA | Size | What It Actually Is | Recovered Content |
|------|------|--------------------|--------------------|
| EFTA00593870 | 46 KB | Null-padded PDF (64% zeroed) | Page 1 of CVRA motion (*Jane Doe #1 & #2 v. US*) |
| EFTA00597207 | 883 KB | Disk image with Apple Address Book | 8 contacts + iPhone 5s photo (Aug 2014, LSJ) |
| EFTA00645624 | 35 KB | Truncated Sharp scanner fax | Epstein fee dispute legal memo (Apr 2015) |
| EFTA01175426 | 827 KB | Truncated linearized PDF | 10-page court trust order (Zaffaroni/Packard) |
| EFTA01220934 | 1.1 MB | Raw Windows disk image fragment | Cached web images, application files (not case-relevant) |

---

## Derived Databases

All analysis in this repository is built on four databases derived from the source PDFs.

### full_text_corpus.db (6.08 GB)

The primary analytical database. Contains the full text of every page of every document.

| Table | Records | Description |
|-------|--------:|-------------|
| `documents` | 1,380,937 | One row per PDF: EFTA number, dataset, file path, page count, file size |
| `pages` | 2,731,785 | One row per page: EFTA number, page number, full text content, character count |
| `pages_fts` | 2,731,785 | FTS5 full-text search index over all page text |

**How it was built:** PyMuPDF (`fitz`) text extraction on every PDF. For scanned documents,
this captures the invisible OCR text layer (rendering mode Tr=3) that the DOJ's scanning
vendor applied. Documents where PyMuPDF returned zero text were flagged for manual review
(this is how the 5 corrupted PDFs were identified).

### redaction_analysis_v2.db (0.95 GB)

Spatial analysis of every redaction rectangle in the corpus, with the text found at
each redaction's coordinates.

| Table | Records | Description |
|-------|--------:|-------------|
| `redactions` | 2,587,102 | Every redaction: position, type, hidden text, confidence |
| `document_summary` | 638,416 | Per-document redaction counts and flags |
| `reconstructed_pages` | 39,588 | Pages rebuilt from spatially-ordered redaction fragments |
| `extracted_entities` | 107,422 | Named entities extracted from reconstructed text |

**Important caveat:** The vast majority of `bad_overlay` redaction records (~98%) are
OCR noise — the scanner's OCR engine attempted to read black redaction bars and produced
garbage text. Only 12 documents contain genuinely failed redactions (Apple Mail PLIST
metadata exposed behind incompletely flattened overlays). See
[DATA_QUALITY_AUDIT](DATA_QUALITY_AUDIT.md) and [EVIDENCE_RELIABILITY_AUDIT](EVIDENCE_RELIABILITY_AUDIT.md)
for the full audit. The redaction database remains useful as a searchable index of text
found near redaction zones, but its `hidden_text` field should not be interpreted as
"recovered secret content."

### transcripts.db (2.5 MB)

GPU-transcribed audio/video content using faster-whisper large-v3 on NVIDIA A100.

| Metric | Value |
|--------|------:|
| Total entries | 1,530 |
| With speech content | 375 |
| Total words transcribed | 92,153 |
| Silent/surveillance skipped | 1,155 |

Pre-screening classified 2,581 unique media files: 903 were processed, 1,633 were skipped
(silent surveillance footage — 77+ hours of MCC/facility video with no audio stream).

Notable content: BOP Warden OIG interview, 3 MCC prison phone calls, 20+ Grand Jury
testimony recordings, Deepak Chopra voicemails.

### persons_registry.json

Unified entity registry merging three sources: our pipeline extraction, la-rana-chicana
community research CSV, and the knowledge_graph.db entity table.

| Metric | Value |
|--------|------:|
| Total persons | 1,536 |
| With aliases | 203 |
| With descriptions | 237 |
| With 100+ document hits | 693 |
| With 10-99 document hits | 409 |

---

## What's NOT in This Corpus

For transparency, here is what we do NOT have access to:

1. **Sealed court filings** — Multiple cases have sealed dockets (SDNY, SDFL, USVI).
   We only analyze publicly released material.
2. **Grand jury transcripts** (full text) — We have audio recordings of some testimony
   sessions (transcribed in transcripts.db) but not official transcripts.
3. **Classified intelligence material** — References to intelligence connections are
   derived from what appears in the public DOJ files, not from classified sources.
4. **Victim statements beyond what DOJ released** — The DOJ's release is selective.
   Many victim interviews, depositions, and statements referenced in the documents are
   not included in the EFTA corpus.
5. **The "missing" EFTA numbers** — 692,473 EFTA numbers in DS9's range are not present.
   Whether these represent withheld documents, unimaged evidence, or simply unused
   numbers in the task force's tracking system is unknown.
6. **Post-February 10, 2026 releases** — This inventory reflects data through DS12.
   Additional datasets may be released.

---

## Verification

Anyone can independently verify any finding in this repository:

1. **Obtain the source PDFs** from [justice.gov/epstein](https://www.justice.gov/epstein/)
   or the archive.org mirrors linked in each report
2. **Check any EFTA citation** by constructing the URL:
   `https://www.justice.gov/epstein/files/DataSet%20{N}/EFTA{########}.pdf`
3. **Reproduce the text extraction** using PyMuPDF: `fitz.open(path)[page].get_text()`
4. **Reproduce the redaction analysis** using the methodology in
   [REDACTION_TEXT_LAYER_ANALYSIS](REDACTION_TEXT_LAYER_ANALYSIS.md)

The EFTA-to-dataset mapping table is in the main [README](../README.md#efta-number-to-dataset-mapping).

---

## Processing Pipeline

```
DOJ PDFs (194.5 GB, 1.38M files)
    │
    ├─→ PyMuPDF text extraction ──→ full_text_corpus.db (6.08 GB)
    │       └─→ FTS5 full-text search index
    │
    ├─→ Redaction rectangle analysis ──→ redaction_analysis_v2.db (0.95 GB)
    │       ├─→ Reconstructed pages (39,588)
    │       └─→ Entity extraction (107,422 entities)
    │
    ├─→ Media file pre-screening + GPU transcription ──→ transcripts.db
    │
    ├─→ Person registry unification ──→ persons_registry.json (1,536 persons)
    │
    └─→ Byte-level forensic recovery of 5 zero-page PDFs
            └─→ recovered_corrupted_pdfs/ (Apple Address Book, LSJ photo, etc.)
```

All processing was performed locally. No documents were uploaded to cloud services
or third-party APIs for analysis. Text extraction, OCR, transcription, and entity
extraction were all run on local hardware.
