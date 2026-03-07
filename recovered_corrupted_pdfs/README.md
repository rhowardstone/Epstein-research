# Corrupted PDF Recovery — Epstein Files Dataset 9

## Overview

Five files in Dataset 9 (DS9) were identified as corrupted or non-standard PDFs that could
not be processed by normal PDF tools (PyMuPDF, Poppler, Ghostscript). Forensic analysis
revealed that **none of these are simply corrupted PDFs** — they are disk image fragments,
truncated scans, and files with other data types saved with `.pdf` extensions during the
forensic imaging process.

All five files were analyzed byte-by-byte, and all recoverable content has been extracted.

## File Inventory

### [EFTA00645624](https://www.justice.gov/epstein/files/DataSet%209/EFTA00645624.pdf) — Sharp Scanner Fax (FULLY RECOVERED)

| Property | Value |
|----------|-------|
| Original size | 35,153 bytes |
| Corruption type | Missing xref table, trailer, and %%EOF marker (truncated) |
| What it is | Single-page CCITT Group 4 fax image from a Sharp scanner |
| Recovery method | Extracted CCITTFaxDecode stream from PDF object 6, wrapped in TIFF header for PIL decoding |

**Content:** Legal memorandum dated April 22, 2015, from W. Chester Brewer Jr. to Jeffrey Epstein,
Darren Indyke, Jack Goldberger, and others. RE: *Jeffrey Epstein vs. Scott Rothstein, Bradley J.
Edwards, et al.* — 15th Judicial Circuit Case No. 502009CA040800XXXXMB. Concerns a UMC hearing
about motion for fees/costs.

**Recovered files:**
- [`EFTA00645624_decoded.png`](https://github.com/rhowardstone/Epstein-research-data/raw/main/recovered_corrupted_pdfs/EFTA00645624/EFTA00645624_decoded.png) — Full-resolution page image (1704x2196 px, bilevel)
- [`EFTA00645624.tiff`](carved_pdfs/EFTA00645624.tiff) — Raw TIFF with CCITT data
- [`EFTA00645624_ocr.txt`](https://github.com/rhowardstone/Epstein-research-data/raw/main/recovered_corrupted_pdfs/EFTA00645624/EFTA00645624_ocr.txt) — Full OCR text
- [`EFTA00645624_ccitt_raw.bin`](carved_pdfs/EFTA00645624_ccitt_raw.bin) — Raw CCITT Group 4 bitstream (31,992 bytes)

**Recovery technique:**
1. Parsed PDF objects manually (no xref available)
2. Located image object 6 with `/Filter/CCITTFaxDecode /DecodeParms<</K -1/Columns 1704/Rows 2196>>`
3. Extracted 31,992 bytes of raw CCITT Group 4 data
4. Constructed TIFF header: little-endian, 1704x2196, 1-bit, CCITT Group 4 compression
5. Opened with PIL, converted to PNG
6. OCR'd with Tesseract

---

### [EFTA01175426](https://www.justice.gov/epstein/files/DataSet%209/EFTA01175426.pdf) — Faxed Court Order (FULLY RECOVERED, 10 of 11 pages)

| Property | Value |
|----------|-------|
| Original size | 826,803 bytes |
| Corruption type | Linearized PDF truncated ~10,735 bytes short; missing main xref/trailer and Pages tree object |
| What it is | 11-page fax of a San Mateo County Superior Court order |
| Recovery method | Direct extraction of CCITT Group 3 fax streams from each page's image object |

**Content:** San Mateo County Superior Court probate order — "Order Approving Modification
of Trust." Involves the Elisa Zaffaroni irrevocable trust (dated April 15, 1989), trustee succession
rules, J.P. Morgan Trust Company as corporate co-trustee, and a $4.1 million principal distribution
for a Tiburon, CA residence. References David Packard and the Zaffaroni family. Faxed from
"Academic Affairs" at 972-883-6764 (UT Dallas area code), dated March 22, 2012/2014.

**Recovered files:**
- [`EFTA01175426_page02.png`](https://github.com/rhowardstone/Epstein-research-data/raw/main/recovered_corrupted_pdfs/EFTA01175426/EFTA01175426_page02.png) through [`_page20.png`](https://github.com/rhowardstone/Epstein-research-data/raw/main/recovered_corrupted_pdfs/EFTA01175426/EFTA01175426_page20.png) — 10 page images (1728x2203 px, bilevel)
- [`EFTA01175426_full_ocr.txt`](https://github.com/rhowardstone/Epstein-research-data/raw/main/recovered_corrupted_pdfs/EFTA01175426/EFTA01175426_full_ocr.txt) — Full OCR text of all pages
- [`EFTA01175426_repaired.pdf`](carved_pdfs/EFTA01175426_repaired.pdf) — Repaired PDF with recovered pages

**Recovery technique:**
1. PyMuPDF, Ghostscript, and pdftoppm all failed (truncated xref)
2. Regex-scanned file for all `/Subtype/Image` objects with CCITTFaxDecode parameters
3. Found 10 image objects with consistent params: W=1728, H=2203, K=0 (Group 3), Cols=1728, EndOfBlock=false
4. For each: extracted raw stream data, built TIFF header with Group 3 1-D compression, decoded with PIL
5. Note: Page 1 (title page) and page 11 may be in the missing ~10KB truncated section

---

### [EFTA01220934](https://www.justice.gov/epstein/files/DataSet%209/EFTA01220934.pdf) — Forensic Disk Image Fragment (FULLY CARVED)

| Property | Value |
|----------|-------|
| Original size | 1,138,878 bytes |
| Corruption type | Not a PDF at all — raw disk image sectors saved as .pdf |
| What it is | Fragment of a Windows PC hard drive containing cached web content, application files, and photos |
| Recovery method | File signature scanning and carving from raw sectors |

**Content:** This is NOT a document. It is a fragment of a forensic disk image (~279 sectors of
4096 bytes) containing miscellaneous files from a Windows computer. The content is a mix of:
- Cached web page images (partially recovered due to sector fragmentation)
- Macromedia Dreamweaver and AutoCAD application files
- Windows system manifests (IE Extension Compatibility, MSAuditEvtLog)
- An Adobe license agreement in Czech
- An Apple Interface Builder plist from a music application
- Apple macOS codec descriptions (GSM, MPEG-4)

The JPEGs show the classic "top half recovered, bottom half garbage" pattern — this is because
each JPEG spans multiple disk sectors, but only the first contiguous run of sectors was captured.
The rest of each JPEG's data was in sectors belonging to other files on the original disk.

**Recovered files:**
- [`EFTA01220934_jpeg1.jpg`](https://github.com/rhowardstone/Epstein-research-data/raw/main/recovered_corrupted_pdfs/EFTA01220934/EFTA01220934_jpeg1.jpg) through [`_jpeg9.jpg`](https://github.com/rhowardstone/Epstein-research-data/raw/main/recovered_corrupted_pdfs/EFTA01220934/EFTA01220934_jpeg9.jpg) — 9 JPEGs carved from disk (2 corrupted, 7 viewable)
  - jpeg2: Small thumbnail (160x120), woman with goggles (scientist/lab worker?)
  - jpeg4: Sky icon (160x44)
  - jpeg5: Low-res stamped document (160x44)
  - jpeg6: Small fragment (264x197), pink/blue image
  - jpeg7: **Harlequin Presents poster — "Heidi Rice" (480x360)** — romance novel cover
  - jpeg8: Image of money/currency (286x384)
  - jpeg9: Tall image (532x922)
  - jpeg1, jpeg3: Corrupted (cannot be opened)
- [`EFTA01220934_gif1.gif`](https://github.com/rhowardstone/Epstein-research-data/raw/main/recovered_corrupted_pdfs/EFTA01220934/EFTA01220934_gif1.gif) — Office/application icons (344x280)
- [`EFTA01220934_png1.png`](https://github.com/rhowardstone/Epstein-research-data/raw/main/recovered_corrupted_pdfs/EFTA01220934/EFTA01220934_png1.png) — Tiny icon (9x9)
- [`EFTA01220934_png2.png`](https://github.com/rhowardstone/Epstein-research-data/raw/main/recovered_corrupted_pdfs/EFTA01220934/EFTA01220934_png2.png) — Small icon (38x12)
- [`EFTA01220934_content.html`](https://github.com/rhowardstone/Epstein-research-data/raw/main/recovered_corrupted_pdfs/EFTA01220934/EFTA01220934_content.html) — Macromedia Dreamweaver tag library dialog (not case-relevant)
- [`EFTA01220934_content.rtf`](https://github.com/rhowardstone/Epstein-research-data/raw/main/recovered_corrupted_pdfs/EFTA01220934/EFTA01220934_content.rtf) — Browser Extended Validation certificate help text (not case-relevant)

**Sector map (each character = 4096 bytes):**
```
P = PDF header, O = PDF object, J = JPEG, G = GIF, I = PNG, R = RTF, H = HTML
B = Apple PLIST, # = compressed data, ~ = medium entropy, - = low entropy
. = null, n = mostly null

P-#~#~--------------------G#####IJ#####---n..#n..#####nJJ-R-RR##
#####~###n##J##J##~~~~~##~~~~##~~###~~#~##~###--------~-#B-###n#
#####~#~~######################J##~####J###################---##
######H#--#####################H~#n~~I###.#--#..............n...
............nH--~~~~n--
```

**Recovery technique:**
1. Identified file as disk image via `file` command and absence of valid PDF structure
2. Scanned for file magic signatures: JPEG (FFD8FF), PNG (89504E47), GIF (47494638), RTF ({\\rtf), HTML (<html)
3. Carved each embedded file by following its format-specific structure
4. Also found: 3 XML assembly manifests, 1 bplist (Interface Builder), Apple codec tables

**Why the JPEGs are half-broken:**
JPEG files use sequential encoding. When a JPEG spans sectors 100, 101, 102 on disk but the
forensic image only captured sector 100 (plus sectors from other files at 101, 102), the JPEG
decoder renders the first N scan lines correctly, then produces garbage for the rest.

---

### [EFTA00597207](https://www.justice.gov/epstein/files/DataSet%209/EFTA00597207.pdf) — Apple Address Book + iPhone Photo (CONTACTS RECOVERED)

| Property | Value |
|----------|-------|
| Original size | 882,743 bytes |
| Corruption type | Linearized PDF with disk sectors overwritten by Apple Address Book data |
| What it is | PDF wrapper around a mix of: address book contacts, an iPhone photo, and compressed page data |
| Recovery method | PLIST parsing for contacts; base64 decoding for embedded JPEG |

**Content:** The PDF structure claims 10 pages but they are irrecoverable — the sectors that
contained the page cross-reference data were overwritten. Instead, 8 disk sectors (28KB-57KB) contain
**Apple macOS AddressBook.app binary property list records** — one contact per 4096-byte sector.

**8 Contacts Recovered:**
1. **[?] Sussman** — Phone: (713) 478-6444 (Houston, TX)
2. **Karim Wade** — Email: ME@micatti.gouv.sn (Senegalese government)
3. **Jacquie [?]** — Email: Jacquie@greenislandgardens.net
4. **Gwendolyn Beck** — Email: GBeck111@aol.com
5. **Jay Lefkowitz** — Phone: (917) 617-2278, (212) 446-4970 — Email: lefkowitz@kirkland.com (Kirkland & Ellis)
6. **Michael Wolff** — Email: michael@burnrate.com
7. **J. Robert Strang** — Email: RJS@investigativemanagement.com
8. **Jean-Luc [?]** — Phone: 1 (646) 961-8500 (NYC), +33 648 519 751 (France) — Email: 2jeanluc@gmail.com

Cross-references with persons registry: Gwendolyn Beck (known associate), Jay Lefkowitz (Epstein attorney),
Michael Wolff (journalist), Gerald Sussman.

**Also recovered:** 1 photograph taken with an **iPhone 5s on August 3, 2014, at 9:38:27 AM** (iOS 7.1.2).
Recovered as 640x480 thumbnail; original was 3264x2448.

**Recovered files:**
- [`contacts_extracted.txt`](https://github.com/rhowardstone/Epstein-research-data/raw/main/recovered_corrupted_pdfs/EFTA00597207/contacts_extracted.txt) — Full contact details with cross-references
- [`EFTA00597207_embedded_photo.jpg`](https://github.com/rhowardstone/Epstein-research-data/raw/main/recovered_corrupted_pdfs/EFTA00597207/EFTA00597207_embedded_photo.jpg) — iPhone 5s photo from Aug 3, 2014

**Byte-level structure:**
```
Offset 0-18KB:     PDF header + 13 small compressed objects (real PDF structure)
Offset 28KB-57KB:  8 Apple Address Book bplist records (4096 bytes each)
Offset 61KB-200KB: Base64-encoded JPEG (iPhone 5s photo, Aug 2014)
Offset 200KB-260KB: Null padding
Offset 260KB-882KB: Compressed data (original PDF page images, irrecoverable without xref)
```

**Recovery technique:**
1. Identified bplist00 signatures at 4096-byte aligned offsets
2. Extracted readable strings from each bplist sector (binary PLIST format)
3. Parsed contact fields: UID (UUID format), First, Last, Phone, Email
4. Found base64 JPEG at offset 61440 — decoded and extracted EXIF metadata
5. Verified no additional contacts or hidden data in remaining sectors

---

### [EFTA00593870](https://www.justice.gov/epstein/files/DataSet%209/EFTA00593870.pdf) — Null-Padded PDF Shell (MINIMAL CONTENT)

| Property | Value |
|----------|-------|
| Original size | 45,783 bytes |
| Corruption type | Linearized PDF header intact but page data sectors are all null bytes |
| What it is | PDF shell with %%EOF at byte 734; remaining 45KB is 64.3% null |
| Recovery method | Stripped null padding; only ~16KB of real data remains |

**Content:** *Jane Doe #1 and Jane Doe #2 v. United States* — Case No. 9:08-cv-80736-KAM
(Marra/Johnson). "Unopposed Motion of Jane Doe 1 and 2 to Exceed Page Limits in Their
Response to the Government's Motion for Summary Judgment." Document 412, entered on
FLSD Docket 08/11/2017. This is from the landmark Crime Victims' Rights Act case.

Page 1 of 4 was recovered from PDF content streams in the non-zeroed sectors. The motion
describes the complexity of the case (157 separate assertions of material fact) and the
Government's three responsive filings (DE 407, DE 402, and the 30-page cross-motion).

**Recovered files:**
- [`efta00593870_stripped.pdf`](carved_pdfs/efta00593870_stripped.pdf) — Null bytes removed, 16,384 bytes remaining
- [`EFTA00593870_cleaned_text.txt`](https://github.com/rhowardstone/Epstein-research-data/raw/main/recovered_corrupted_pdfs/EFTA00593870/EFTA00593870_cleaned_text.txt) — Cleaned, readable text from page 1

**Recovery technique:**
1. Identified %%EOF at byte 734 (linearization first part)
2. Mapped sector types: 4 real sectors, 8 null sectors
3. Found 8 FlateDecode streams in the non-null sectors; decompressed with zlib
4. Extracted text from PDF content stream operators (Tj/TJ)
5. Cleaned letter-spaced OCR text and reconstructed readable paragraphs
6. Pages 2-4 were in zeroed sectors and are irrecoverable

---

## Methodology

All five files were subjected to the same analysis pipeline:

1. **Header inspection** — Verify PDF signature, find %%EOF markers, count objects
2. **Sector mapping** — Classify every 4096-byte sector by content type (null, PDF, compressed, JPEG, PLIST, etc.)
3. **File signature scanning** — Search for embedded file magic bytes (JPEG FFD8FF, PNG 89504E47, bplist, RTF, HTML, ZIP, SQLite, etc.)
4. **Stream extraction** — For valid PDF objects, extract and attempt decompression of each stream
5. **CCITT fax decoding** — For scanner/fax images, extract raw CCITT data and wrap in TIFF headers for PIL decoding
6. **PLIST parsing** — For Apple binary plists, extract readable strings and parse contact field structure
7. **OCR** — Tesseract with page segmentation mode 3 or 6 on all recovered images
8. **Cross-referencing** — Check extracted names against persons_registry.json (1,536 persons)

## Tools Used

- Python 3 (struct, re, zlib, base64, plistlib)
- PIL/Pillow (image decoding)
- PyMuPDF/fitz (attempted PDF rendering)
- Ghostscript, pdftoppm (attempted PDF rendering)
- Tesseract OCR
- Custom TIFF header construction for CCITT fax data

## Key Finding

The most forensically significant recovery is **[EFTA00597207](https://www.justice.gov/epstein/files/DataSet%209/EFTA00597207.pdf)** — 8 Apple Address Book contacts
from a macOS computer, including known Epstein associates (Jay Lefkowitz, his attorney; Gwendolyn Beck;
Michael Wolff) plus a Senegalese government contact (Karim Wade) and an unidentified French contact.
The iPhone 5s photo from August 2014 was also recovered from the same file.

The "corrupted PDFs" are better understood as **forensic imaging artifacts** — fragments of hard drives
that were captured during evidence collection and assigned EFTA numbers regardless of their actual content.

---

## File Directory

### `github_release/` — Curated recoveries organized by EFTA number

| File | Description |
|------|-------------|
| [`EFTA00593870/EFTA00593870_cleaned_text.txt`](https://github.com/rhowardstone/Epstein-research-data/raw/main/recovered_corrupted_pdfs/EFTA00593870/EFTA00593870_cleaned_text.txt) | Cleaned OCR text — CVRA motion page 1 |
| [`EFTA00597207/contacts_extracted.txt`](https://github.com/rhowardstone/Epstein-research-data/raw/main/recovered_corrupted_pdfs/EFTA00597207/contacts_extracted.txt) | 8 Apple Address Book contacts with cross-references |
| [`EFTA00597207/EFTA00597207_embedded_photo.jpg`](https://github.com/rhowardstone/Epstein-research-data/raw/main/recovered_corrupted_pdfs/EFTA00597207/EFTA00597207_embedded_photo.jpg) | iPhone 5s photo, Aug 3, 2014 |
| [`EFTA00645624/EFTA00645624_decoded.png`](https://github.com/rhowardstone/Epstein-research-data/raw/main/recovered_corrupted_pdfs/EFTA00645624/EFTA00645624_decoded.png) | Legal memo — full-resolution fax image |
| [`EFTA00645624/EFTA00645624_ocr.txt`](https://github.com/rhowardstone/Epstein-research-data/raw/main/recovered_corrupted_pdfs/EFTA00645624/EFTA00645624_ocr.txt) | Full OCR text of legal memo |
| [`EFTA01175426/EFTA01175426_full_ocr.txt`](https://github.com/rhowardstone/Epstein-research-data/raw/main/recovered_corrupted_pdfs/EFTA01175426/EFTA01175426_full_ocr.txt) | Full OCR text — San Mateo probate order (10 pages) |
| [`EFTA01175426/EFTA01175426_page02.png`](https://github.com/rhowardstone/Epstein-research-data/raw/main/recovered_corrupted_pdfs/EFTA01175426/EFTA01175426_page02.png) ... [`_page20.png`](https://github.com/rhowardstone/Epstein-research-data/raw/main/recovered_corrupted_pdfs/EFTA01175426/EFTA01175426_page20.png) | 10 recovered page images |
| [`EFTA01220934/EFTA01220934_jpeg1.jpg`](https://github.com/rhowardstone/Epstein-research-data/raw/main/recovered_corrupted_pdfs/EFTA01220934/EFTA01220934_jpeg1.jpg) ... [`_jpeg9.jpg`](https://github.com/rhowardstone/Epstein-research-data/raw/main/recovered_corrupted_pdfs/EFTA01220934/EFTA01220934_jpeg9.jpg) | 9 JPEGs carved from disk image |
| [`EFTA01220934/EFTA01220934_gif1.gif`](https://github.com/rhowardstone/Epstein-research-data/raw/main/recovered_corrupted_pdfs/EFTA01220934/EFTA01220934_gif1.gif) | GIF carved from disk image |
| [`EFTA01220934/EFTA01220934_png1.png`](https://github.com/rhowardstone/Epstein-research-data/raw/main/recovered_corrupted_pdfs/EFTA01220934/EFTA01220934_png1.png), [`_png2.png`](https://github.com/rhowardstone/Epstein-research-data/raw/main/recovered_corrupted_pdfs/EFTA01220934/EFTA01220934_png2.png) | PNGs carved from disk image |
| [`EFTA01220934/EFTA01220934_content.html`](https://github.com/rhowardstone/Epstein-research-data/raw/main/recovered_corrupted_pdfs/EFTA01220934/EFTA01220934_content.html) | Dreamweaver tag library (not case-relevant) |
| [`EFTA01220934/EFTA01220934_content.rtf`](https://github.com/rhowardstone/Epstein-research-data/raw/main/recovered_corrupted_pdfs/EFTA01220934/EFTA01220934_content.rtf) | Browser EV cert help text (not case-relevant) |

### `carved_pdfs/` — Raw forensic carving output (all 44 files)

| File | Description |
|------|-------------|
| [`efta00593870_stripped.pdf`](carved_pdfs/efta00593870_stripped.pdf) | Null-stripped PDF shell (16KB) |
| [`EFTA00597207_embedded_photo.jpg`](carved_pdfs/EFTA00597207_embedded_photo.jpg) | iPhone 5s photo recovered from bplist data |
| [`EFTA00597207_pdftoppm-01.png`](carved_pdfs/EFTA00597207_pdftoppm-01.png) ... [`-10.png`](carved_pdfs/EFTA00597207_pdftoppm-10.png) | 10 pdftoppm render attempts (mostly blank — sectors overwritten) |
| [`EFTA00645624_ccitt.bin`](carved_pdfs/EFTA00645624_ccitt.bin), [`_ccitt_raw.bin`](carved_pdfs/EFTA00645624_ccitt_raw.bin) | Raw CCITT Group 4 fax bitstreams |
| [`EFTA00645624_decoded.png`](carved_pdfs/EFTA00645624_decoded.png) | Decoded fax page image |
| [`EFTA00645624.tiff`](carved_pdfs/EFTA00645624.tiff) | TIFF-wrapped CCITT data |
| [`EFTA01175426_full_ocr.txt`](carved_pdfs/EFTA01175426_full_ocr.txt) | Full OCR of 10 recovered pages |
| [`EFTA01175426_page02.png`](carved_pdfs/EFTA01175426_page02.png) ... [`_page20.png`](carved_pdfs/EFTA01175426_page20.png) | 10 recovered fax page images |
| [`EFTA01175426_repaired.pdf`](carved_pdfs/EFTA01175426_repaired.pdf) | Repaired PDF with recovered pages reinserted |
| [`EFTA01220934_content.html`](carved_pdfs/EFTA01220934_content.html) | Dreamweaver HTML carved from disk |
| [`EFTA01220934_content.rtf`](carved_pdfs/EFTA01220934_content.rtf) | RTF carved from disk |
| [`efta01220934_first_image.jpeg`](carved_pdfs/efta01220934_first_image.jpeg), [`_first_png.png`](carved_pdfs/efta01220934_first_png.png) | First image/PNG found in disk sectors |
| [`EFTA01220934_gif1.gif`](carved_pdfs/EFTA01220934_gif1.gif) | GIF carved from disk image |
| [`EFTA01220934_jpeg1.jpg`](carved_pdfs/EFTA01220934_jpeg1.jpg) ... [`_jpeg9.jpg`](carved_pdfs/EFTA01220934_jpeg9.jpg) | 9 JPEGs carved from disk (2 corrupted) |
| [`EFTA01220934_png1.png`](carved_pdfs/EFTA01220934_png1.png), [`_png2.png`](carved_pdfs/EFTA01220934_png2.png) | PNGs carved from disk image |
