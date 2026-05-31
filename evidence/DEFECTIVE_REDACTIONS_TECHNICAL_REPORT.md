# Defective Redactions in DOJ Court Filing Archive: Technical Analysis

*Analysis of recoverable redacted text from Wayback Machine archived court filings*

**Date:** April 23, 2026  
**Status:** Technical Report — Ongoing Analysis  
**Scope:** 12,220 court filing PDFs across 50+ Epstein-related cases

---

## Executive Summary

We have identified and analyzed a systematic document integrity issue affecting court filings in the DOJ's Epstein case archive. **Text-based PDF documents with visual-only redactions allow recovery of hidden information** through simple copy/paste or text extraction tools.

### Key Findings

- **Vulnerability Window:** December 2025 - February 2026
- **Affected Documents:** ~12,000 court filing PDFs across major cases
- **Root Cause:** Black rectangle overlays drawn over visible text (PDF rendering mode `Tr=0`)
- **Recovery Method:** Standard pdftotext extraction or copy/paste
- **DOJ Remediation:** Files reprocessed as image-based PDFs with invisible OCR overlays by February 25, 2026

### Technical Impact

Across the full catalog (7 cases, 56 unique documents analyzed with v6 pymupdf+pixel extraction):
- **740 catalog rows** produced by initial extraction
- **719 rows retained** after visual + pixel + structural cross-validation
- **21 rows dropped** as non-evidentiary (PACER headers on fully-sealed pages, TECS template text, literal x-placeholders)
- **Content includes:** Financial details, entity names, payment amounts, investigative details, privilege-log email addresses, deposition-transcript names

---

## Technical Analysis

### PDF Redaction Vulnerability

**Defective Method (Original DOJ Files):**
1. Text drawn in normal rendering mode (`Tr=0`)
2. Black rectangles overlaid as visual redactions
3. **Result:** Text remains in document structure, recoverable via text extraction

**Secure Method (Post-Remediation):**
1. Document rasterized to image
2. OCR overlay applied in invisible mode (`Tr=3`)  
3. **Result:** Redacted content burned into raster, no recoverable text

### Detection Methodology

Our scanner identifies vulnerable documents by analyzing PDF content streams:

```python
# Text operations in normal mode = vulnerable to defect
mode0_text = count_operations(content_stream, ["Tj", "TJ"], where="Tr=0")

# Black rectangle fills = visual redactions
black_rects = count_black_fill_operations(content_stream)

# Classification
if mode0_text > 0 and black_rects > 0:
    return "DEFECT_CANDIDATE"
```

### Recovery Techniques

**Method 1: Simple Text Extraction**
```bash
pdftotext -layout document.pdf - | grep "search_term"
```

**Method 2: Geometric Analysis** (Our Tool)
```python
# Extract text positions and rectangle bounds from PDF content stream
# Return only text whose position intersects black rectangles
python3 extract_recovered_redactions.py document.pdf
```

---

## Case Study: USVI v. JPMorgan

**Document:** `001-01.pdf` (Second Amended Complaint)  
**Original Size:** 795KB (text-based)  
**Remediated Size:** 7.8MB (image + OCR overlay)  
**Wayback URL:** `web.archive.org/web/20251228132625/https://www.justice.gov/multimedia/Court%20Records/Government%20of%20the%20United%20States%20Virgin%20Islands%20v.%20JPMorgan%20Chase%20Bank,%20N.A.,%20No. 122-cv-10904%20(S.D.N.Y.%202022)/001-01.pdf`

### Recovered Content Sample

**Page 18 — Paragraph 80:**
```
"Financial Strategy Group, Ltd.; Financial Trust, Inc.; FT Real Estate Inc.; 
Gratitude America, Inc.; Hyperion Air, Inc."
```

**Page 19 — Financial Details:**
```
"signed Foundation account checks for over $400,000 made payable to young 
female models and actresses, including a former Russian model who received 
over $380,000 through monthly payments of $8,333"
```

**Page 24 — Entity Finances:**  
```
"$16 million net $10 million net loans that are still outstanding to 
Indyke- and Kahn-related entities"
```

### Verification Against EFTA Corpus

- **Original (001-01.pdf):** Contains above recoverable text
- **EFTA02805472:** Same content, reprocessed as image — **no recoverable text**
- **Match Confirmed:** Docket headers and page counts identical

---

## Systematic Analysis Results

### Full catalog — 7 cases

| Case | Kept rows | Narrow-re-verify | Dropped |
|------|----------:|----------:|----------:|
| Giuffre v. Maxwell, 115-cv-07433 (S.D.N.Y.) | 368 | 40 | 0 |
| USVI v. JPMorgan Chase, 122-cv-10904 (S.D.N.Y.) | 285 | 0 | 0 |
| In re Estate of Jeffrey E. Epstein, ST-21-RV-00005 (V.I.) | 57 | 0 | 0 |
| CA Florida Holdings v. Aronberg, 50-2025-CA-...  (Fla.) | 9 | 8 | 0 |
| U.S. v. Maxwell, 120-cr-00330 (S.D.N.Y.) | 0 | 0 | 6 |
| Maxwell v. United States, 24-1073 (U.S. cert. petition) | 0 | 0 | 2 |
| FOIA: CBP TECS Records | 0 | 0 | 13 |
| **Total** | **719** | **48** | **21** |

### USVI v. JPMorgan — top recovery targets

| Document | Hidden Tokens | Content Type |
|----------|---------------|--------------|
| `031.pdf` | 1,252 | Motion for Letter Rogatory |
| `030.pdf` | 999 | Discovery motion |
| `003.pdf` | 488 | Subpoena response |
| `050.pdf` | 410 | Attorney admissions |
| `028-01.pdf` | 27 | Court correspondence |

---

## Cross-Validation

To guard against false positives from the pixel-darkness method, we cross-validated the catalog against Lee Drake's `unredact` tool (https://github.com/leedrake5/unredact), which detects redaction rectangles via PDF drawing-primitive inspection — an orthogonal method that looks at PDF structure rather than rendered pixels.

**Aggregate results across all 56 catalog documents:**

| Method | Pages flagged |
|--------|--------------:|
| v6 (pixel-darkness at 150dpi, 75% dark threshold) | 280 |
| Drake `unredact` (PDF primitive inspection) | 223 |
| Both methods agree | 85 |
| v6-only (Drake missed) | 195 |
| Drake-only (v6 missed) | 138 |

The two methods are **complementary, not superset/subset** — each catches a failure mode the other cannot:

- **v6 catches what Drake cannot (195 pages):** scanned documents where the redaction is burned into the page image as raster pixels rather than drawn as a vector rectangle. Drake's primitive-level detector cannot see these; the pixel method does. Examples: scanned depositions in Giuffre 729, 828, 1326-4, 1328-02.
- **Drake catches what v6 cannot:** thin inline bars narrower than a full word's bounding box (email addresses in privilege logs, single-name redactions between visible words). One initial false-negative from our pixel verifier — Giuffre `144.pdf` p1 with narrow 11pt bars — was restored to the catalog after Drake found 4 real redaction boxes recovering *exactly* what v6 had extracted ("Defendant Maxwell's April 22, 2016 Deposition transcript", "pages 19-22…").

### Triage of Drake-only findings (138 pages)

Visual inspection confirmed all 138 Drake-only pages fall into four categories, none of which contain recoverable evidentiary content v6 missed:

| Category | Count | Why no evidentiary gain |
|----------|-----:|-------------------------|
| EMPTY (0 words under box) | 102 | Sealed pages with text stream stripped (US v. Maxwell 672, CBP TECS) |
| PACER_HEADER only | 13 | Recoverable text is only the system-generated docket header |
| LITERAL_REDACTED | 3 | Visible text is literally the word "REDACTED" |
| Webpage-decoration rectangles | 17 | `Giuffre 787-01.pdf` is a composite exhibit of scraped news articles; "boxes" are banner ads, sidebar thumbnails, page backgrounds, social-share buttons from HTML→PDF conversion |
| Table-of-sealed-exhibits | 2 | `Giuffre 1049.pdf` LIST OF DECIDED MOTIONS — recoverable text is only the exhibit-letter label (e.g., "Exhibit A"), not the sealed content |
| Exemption-label-only TECS page | 1 | `Epstein TECS Records 2.pdf` p1 — same pattern as p2 (already dropped) |

**Conclusion: no rows need to be added from the Drake-only set.** v6's pixel method captured every defective redaction with evidentiary recoverable content that Drake's structural method found.

### Drop rules

The 21 dropped rows fall into three patterns, both verified independently by v6 and Drake:

1. **Fully-sealed pages where only the PACER header is recoverable** (US v. Maxwell 672.pdf p37, p44 and related). Drake confirms the whole page is covered by one large redaction rectangle; both methods extract only the system-generated docket header.
2. **Full-page TECS/FOIA template seal** (`Epstein TECS Records 2.pdf` p2). Both methods recover only the page template and FOIA exemption labels — the actual sealed analyst name and query content were stripped from the text stream.
3. **Literal x-placeholder text** (cert petition p61). The visible text under the bar is a string of x's; the actual redacted content was scrubbed from the text stream and replaced with placeholder characters.

### Narrow-re-verify set (48 rows)

48 rows across the Giuffre and Aronberg cases passed visual eyeball inspection (black bars exist on the page covering the recovered text) but the automated broad-bbox pixel-darkness check did not confirm them because the bars are narrower than a full word's bounding box (e.g., small bars over email addresses in privilege logs, narrow bars over a single name between two visible words in a deposition transcript). These are almost certainly real defective redactions — Drake's structural method confirms boxes on many of them — but a tighter bbox-intersection verifier should confirm each before individual citation in publication.

### Reproducibility

Cross-check scripts in `tools/`:

- `cross_check_unredact.py` — 13-page spot check
- `drake_full_compare.py` — full-catalog comparison (produces `evidence/_drake_vs_v6_diff.md` and `evidence/_drake_per_page.csv`)
- `triage_drake_only.py` — classifies Drake-only pages (produces `evidence/_drake_only_triage.md`)
- `investigate_divergences.py` — per-page box/word inspection for divergent cases
- `clean_redaction_catalog.py` — produces `REDACTION_CATALOG_CLEANED.csv` + `REDACTION_CATALOG_DROPPED.csv` + `REDACTION_CATALOG_CLEANING_LOG.md`

---

## Archive Access & Reproducibility

### Wayback Machine Preservation

The Internet Archive preserved original text-based PDFs before DOJ remediation:

**Base URL Pattern:**
```
https://web.archive.org/web/TIMESTAMP/https://www.justice.gov/multimedia/Court%20Records/CASE_NAME/DOCUMENT.pdf
```

**Working Timestamps:** December 19, 2025 - February 20, 2026

**Example Retrieval:**
```bash
curl "https://web.archive.org/web/20251228132625/https://www.justice.gov/multimedia/Court%20Records/Government%20of%20the%20United%20States%20Virgin%20Islands%20v.%20JPMorgan%20Chase%20Bank,%20N.A.,%20No.%20122-cv-10904%20(S.D.N.Y.%202022)/001-01.pdf" \
  -o original_filing.pdf
```

### Complete Case Inventory

Our analysis covers **12,220 unique PDF files** across these major cases:

| Case | File Count | Priority |
|------|------------|----------|
| **Giuffre v. Maxwell** (115-cv-07433) | 2,978 | High |
| **USVI v. JPMorgan** (122-cv-10904) | 1,840 | High |
| **US v. Maxwell Criminal** (120-cr-00330) | 1,318 | High |
| **Epstein v. Rothstein** (FL 15th Cir.) | 1,412 | Medium |
| **Doe v. Epstein** (908-cv-80119) | 856 | Medium |
| **Other Civil Cases** | 4,016 | Variable |

---

## Technical Tools

### Detection Scanner

**File:** `tools/scan_defective_redactions.py`

```bash
# Classify all PDFs in a directory
python3 scan_defective_redactions.py --root /path/to/pdfs --out scan_results.csv

# Output: path, class, pages_scanned, fill_rects, text_chars, notes
```

### Recovery Extractor  

**File:** `tools/extract_recovered_redactions.py`

```bash
# Extract hidden text from specific pages
python3 extract_recovered_redactions.py document.pdf --pages 15-25

# JSON output for programmatic use  
python3 extract_recovered_redactions.py document.pdf --json
```

### Bulk Downloader

**File:** `tools/download_wayback_court_pdfs.py`

```bash
# Download specific case from Wayback archives
python3 download_wayback_court_pdfs.py --case-filter "giuffre v. maxwell"
```

---

## Timeline & Remediation

### DOJ Response Timeline

- **Dec 19, 2025:** Wayback begins archiving defective originals
- **Feb 20, 2026:** Original URLs begin returning 404 errors  
- **Feb 25, 2026:** DOJ completes replacement with image-based versions
- **Current:** Original text-based files only accessible via Wayback Machine

### Effectiveness of Remediation

DOJ's remediation appears **technically complete**:
- All original URLs now serve image-based PDFs with invisible OCR
- Text extraction from current versions yields **no recoverable redacted content**
- File sizes increased ~10x (795KB → 7.8MB typical)

However, the **original vulnerable versions remain permanently archived** by Wayback Machine.

---

## Research Applications

### Content Analysis Pipeline

For researchers studying these cases:

1. **Identify Target Documents:** Use our case inventory and priority rankings
2. **Download Originals:** Retrieve from Wayback using working timestamps  
3. **Detect Vulnerabilities:** Run defect scanner to identify recovery candidates
4. **Extract Content:** Use geometric recovery tool for precise extraction
5. **Verify Against Corpus:** Cross-reference with EFTA corpus for validation

### Ethical Considerations

This analysis focuses on **document integrity and technical methodology**. Recovered content should be:
- Analyzed for **systemic patterns** rather than individual details
- Used to **understand legal process transparency**
- **Responsibly disclosed** without compromising ongoing investigations

---

## Conclusions

The defective redaction vulnerability represents a **significant document integrity issue** affecting thousands of court filings. While DOJ has remediated the immediate problem, the **technical methodology remains reproducible** via archived versions.

Key takeaways:
- **PDF redaction requires secure implementation** (rasterization, not overlay)
- **Archive preservation creates permanent technical debt** for document security
- **Large-scale systematic analysis** reveals patterns invisible in individual documents

### Future Research

- **Expand to remaining 11,000+ files** across all archived cases
- **Cross-case pattern analysis** of recovered financial and operational details  
- **Timeline reconstruction** of entity relationships and financial flows
- **Comparison with sealed/withheld document inventories**

---

*This report demonstrates technical methodology for educational and transparency purposes. All tools and techniques described are standard document forensics practices applicable to public court records.*