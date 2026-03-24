# Corrupted PDF Forensic Recovery — Dataset 9

## Summary

Five files in DOJ Epstein Files Dataset 9 were flagged as corrupted PDFs (0 pages extracted
by standard tools). Byte-level forensic analysis revealed they are **not simply corrupted** —
they are forensic disk image fragments, truncated scans, and files with non-PDF data saved
with `.pdf` extensions during the evidence imaging process.

**Key finding:** One file (**[EFTA00597207](https://www.justice.gov/epstein/files/DataSet%209/EFTA00597207.pdf)**) contains **8 Apple macOS Address Book contacts**
recovered from raw disk sectors, plus an **iPhone 5s photograph taken on Little Saint James
island on August 3, 2014**. The contacts include Epstein's attorney Jay Lefkowitz, known
associate Gwendolyn Beck, journalist Michael Wolff, and international contacts including
the son of the President of Senegal.

No other public reporting has identified this data. Standard PDF processing pipelines
(including bulk OCR, PyMuPDF, Ghostscript, Poppler) all report "0 pages" for this file.

## Why These Files Were Missed

| Tool | Result on [EFTA00597207](https://www.justice.gov/epstein/files/DataSet%209/EFTA00597207.pdf) |
|------|----------------------|
| PyMuPDF | `page_count = 0` |
| Ghostscript | `Error: Couldn't initialise file` |
| pdftoppm | 10 blank 90-byte PNGs |
| Our [`full_text_corpus.db`](https://github.com/rhowardstone/Epstein-research-data/releases) | `total_pages: 0` |
| Our `extract_full_corpus.py` | Skipped (no text layer) |

Every bulk processing pipeline skips files with 0 extractable pages. With 2.6 million files
in the corpus, nobody manually investigates each one. These five files required reading raw
bytes and understanding disk-level forensic imaging artifacts.

## The Five Files

### [EFTA00597207](https://www.justice.gov/epstein/files/DataSet%209/EFTA00597207.pdf) — Apple Address Book + iPhone 5s Photo

**Source:** [[EFTA00597207](https://www.justice.gov/epstein/files/DataSet%209/EFTA00597207.pdf).pdf](https://www.justice.gov/epstein/files/DataSet%209/EFTA00597207.pdf) (882,743 bytes)

**What it actually is:** A forensic disk image fragment containing interleaved data from
three sources: a linearized PDF skeleton, Apple macOS AddressBook.app binary property lists,
and a base64-encoded JPEG photograph.

**Structure (byte-level):**
```
Offset 0-18KB:      PDF header + 13 compressed objects (real PDF structure, no pages)
Offset 28KB-57KB:   8 Apple Address Book bplist records (4096 bytes each)
Offset 61KB-200KB:  Base64-encoded JPEG photograph
Offset 200KB-260KB: Null padding
Offset 260KB-882KB: Compressed data (original PDF page images, irrecoverable)
```

**8 Contacts Recovered:**

| # | Name | Affiliation | Registry Match |
|---|------|-------------|----------------|
| 1 | [?] Sussman | Houston, TX | Gerald Sussman |
| 2 | Karim Wade | Senegalese government (.gouv.sn) | — |
| 3 | Jacquie [?] | Green Island Gardens | — |
| 4 | Gwendolyn Beck | — | Known Epstein associate |
| 5 | Jay Lefkowitz | Kirkland & Ellis LLP | **Epstein attorney** |
| 6 | Michael Wolff | Journalist | Michael Wolff (author) |
| 7 | J. Robert Strang | Investigative Management Group | — |
| 8 | Jean-Luc [?] | NYC + France phone numbers | — |

**Photograph recovered:**
- **Device:** Apple iPhone 5s running iOS 7.1.2
- **Date:** August 3, 2014, 9:38:27 AM
- **Original resolution:** 3264x2448 (recovered as 640x480 thumbnail)
- **Conditions:** Bright daylight (ISO 40, 1/2740s exposure)
- **Content:** Outdoor location on or near Little Saint James island

**Key questions:**
1. Whose device was forensically imaged to produce this file?
2. Why does an address book containing Epstein's attorney, a known associate, a journalist,
   a private investigations firm, and the son of a foreign head of state exist on the same device?
3. J. Robert Strang runs Investigative Management Group — was this firm retained by Epstein's
   legal team? In what capacity?
4. The Karim Wade + Jean-Luc (France) connection suggests international reach beyond the
   known Epstein network

**Recovery method:**
1. Identified `bplist00` signatures at 4096-byte aligned offsets within the "PDF"
2. Recognized these as macOS AddressBook.app binary property list records (one contact per sector)
3. Extracted readable strings from each bplist: UUID, First, Last, Phone, Email fields
4. Found base64-encoded JPEG at offset 61440 — decoded to recover iPhone 5s photograph with full EXIF
5. Cross-referenced all names against persons_registry.json (1,536 persons)

---

### [EFTA00645624](https://www.justice.gov/epstein/files/DataSet%209/EFTA00645624.pdf) — Legal Memorandum (Fully Recovered)

**Source:** [[EFTA00645624](https://www.justice.gov/epstein/files/DataSet%209/EFTA00645624.pdf).pdf](https://www.justice.gov/epstein/files/DataSet%209/EFTA00645624.pdf) (35,153 bytes)

**What it actually is:** Single-page CCITT Group 4 fax scan from a Sharp MX-M363N scanner.
The PDF is truncated (missing xref table, trailer, and %%EOF marker) but the image data
is complete.

**Content:** Memorandum dated April 22, 2015, from W. Chester Brewer Jr. to Jeffrey Epstein,
Darren Indyke, Jack Goldberger, Tonja Haddad Coleman, and Fred Haddad. RE: *Jeffrey Epstein
vs. Scott Rothstein, Bradley J. Edwards, et al.* — 15th Judicial Circuit Case No.
502009CA040800XXXXMB. Concerns a UMC hearing about Epstein's motion for fees/costs.

**Recovery method:** Extracted 31,992 bytes of raw CCITT Group 4 fax data from PDF object 6,
constructed a TIFF header (1704x2196, 1-bit, CCITT G4), decoded with PIL, OCR'd with Tesseract.

---

### [EFTA01175426](https://www.justice.gov/epstein/files/DataSet%209/EFTA01175426.pdf) — Faxed Court Order (10 of 11 Pages Recovered)

**Source:** [[EFTA01175426](https://www.justice.gov/epstein/files/DataSet%209/EFTA01175426.pdf).pdf](https://www.justice.gov/epstein/files/DataSet%209/EFTA01175426.pdf) (826,803 bytes)

**What it actually is:** 11-page linearized PDF truncated by ~10,735 bytes, missing the
main xref table and Pages tree object.

**Content:** San Mateo County Superior Court probate order — "Order Approving Modification
of Trust" for the Elisa Zaffaroni irrevocable trust (dated April 15, 1989). Involves trustee
succession, J.P. Morgan Trust Company as corporate co-trustee, a $4.1M principal distribution
for a Tiburon, CA residence. References David Packard (Hewlett-Packard) and the Zaffaroni
family. Faxed from "Academic Affairs" at UT Dallas (972-883-6764), March 2012/2014.

**Recovery method:** All PDF tools failed on the truncated xref. Regex-scanned the raw file
for `/Subtype/Image` objects with CCITTFaxDecode parameters (W=1728, H=2203, K=0, Group 3).
Found 10 image objects, extracted each stream, built TIFF headers, decoded with PIL.

---

### [EFTA01220934](https://www.justice.gov/epstein/files/DataSet%209/EFTA01220934.pdf) — Forensic Disk Image Fragment (Not a PDF)

**Source:** [[EFTA01220934](https://www.justice.gov/epstein/files/DataSet%209/EFTA01220934.pdf).pdf](https://www.justice.gov/epstein/files/DataSet%209/EFTA01220934.pdf) (1,138,878 bytes)

**What it actually is:** Raw disk image sectors (~279 sectors of 4096 bytes) from a Windows
PC hard drive, saved as `.pdf` during forensic imaging. Contains cached web content,
application files, and fragmented photographs.

**Carved content:**
- 9 JPEG files (7 viewable, 2 corrupted) — cached web images showing classic sector
  fragmentation: top half renders correctly, bottom half is garbage from unrelated sectors
- 1 GIF (application icons)
- 2 PNGs (tiny UI elements)
- 1 HTML file (Macromedia Dreamweaver tag library dialog)
- 1 RTF file (browser Extended Validation certificate help text)
- 3 XML Windows assembly manifests (IE compatibility, MSAuditEvtLog)
- 1 Apple Interface Builder plist (music application UI)
- 1 Adobe license agreement fragment (in Czech)

**None of this content is case-relevant.** It is miscellaneous cached/installed software
data from whatever computer was forensically imaged.

**Why the JPEGs are half-broken:** JPEG uses sequential encoding. When a JPEG file spans
disk sectors 100-102 but only sector 100 was captured contiguously (101-102 contain data from
other files), the decoder renders the first N scan lines, then produces noise.

---

### [EFTA00593870](https://www.justice.gov/epstein/files/DataSet%209/EFTA00593870.pdf) — Court Filing (Page 1 of 4 Recovered)

**Source:** [[EFTA00593870](https://www.justice.gov/epstein/files/DataSet%209/EFTA00593870.pdf).pdf](https://www.justice.gov/epstein/files/DataSet%209/EFTA00593870.pdf) (45,783 bytes)

**What it actually is:** Linearized PDF with 64.3% null bytes — the file header and first
four disk sectors contain real data, but the remaining eight sectors are zeroed out.

**Content:** *Jane Doe #1 and Jane Doe #2 v. United States* — Case No. 9:08-cv-80736-KAM
(Marra/Johnson). "Unopposed Motion of Jane Doe 1 and 2 to Exceed Page Limits in Their
Response to the Government's Motion for Summary Judgment." Document 412, entered on FLSD
Docket 08/11/2017. From the landmark Crime Victims' Rights Act case.

**Recovery method:** Decompressed 8 FlateDecode streams from the 4 non-null sectors using
zlib. Extracted text from PDF content stream Tj/TJ operators. Reconstructed readable text
from letter-spaced OCR encoding.

---

## Methodology

All five files were subjected to the same byte-level analysis pipeline:

1. **Header inspection** — Verify PDF signature, locate all %%EOF markers, enumerate objects
2. **Sector mapping** — Classify every 4096-byte sector by content type and entropy level
3. **File signature scanning** — Search for embedded magic bytes (JPEG FFD8FF, PNG 89504E47,
   bplist, GIF, RTF, HTML, ZIP, SQLite, XML, OLE, email headers)
4. **Stream extraction** — For valid PDF objects, extract and attempt FlateDecode decompression
5. **CCITT fax decoding** — Extract raw CCITT data, construct TIFF headers with correct
   parameters (Group 3 vs Group 4, dimensions, EndOfBlock), decode with PIL
6. **PLIST parsing** — For Apple binary plists, extract readable strings and identify
   AddressBook.app contact field structures (UID, First, Last, Phone, Email)
7. **Base64 decoding** — Identify and decode base64-encoded content within raw sectors
8. **EXIF extraction** — For recovered photographs, extract camera model, date, GPS, settings
9. **OCR** — Tesseract with appropriate page segmentation modes on all recovered images
10. **Cross-referencing** — Check extracted names against persons_registry.json (1,536 persons)

## Tools

- Python 3.x (struct, re, zlib, base64, plistlib, io)
- PIL/Pillow (image decoding, TIFF construction)
- Tesseract OCR
- PyMuPDF, Ghostscript, pdftoppm (attempted standard recovery — all failed)

## Reproducing These Results

Every source file is publicly available from the DOJ Epstein Files release:
- Dataset 9: https://www.justice.gov/epstein/dataset-9
- Archive.org mirror: https://archive.org/download/Epstein-Dataset-9-2026-01-30/

The analysis requires only standard Python libraries and Tesseract. No specialized forensic
tools are needed — just the willingness to read bytes that PDF viewers refuse to open.
