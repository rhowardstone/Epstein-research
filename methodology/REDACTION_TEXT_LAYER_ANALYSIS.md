# Redaction Text Layer Forensic Analysis
## [EFTA00000476](https://www.justice.gov/epstein/files/DataSet%201/EFTA00000476.pdf).pdf and [EFTA00001932](https://www.justice.gov/epstein/files/DataSet%201/EFTA00001932.pdf).pdf - December 2025 vs. Re-Release Versions

**Date:** 2026-02-08
**Analyst:** Forensic PDF structure investigation
**Subject:** Determining whether "exposed text" from poorly-redacted PDFs represents hidden readable text behind black rectangles, garbled OCR, encoding corruption, or missed text layers

---

## EXECUTIVE SUMMARY

**The "exposed text" is garbled OCR of low-resolution scanned images. There is NO hidden readable text behind black rectangle overlays in these PDFs.**

Both [EFTA00000476](https://www.justice.gov/epstein/files/DataSet%201/EFTA00000476.pdf).pdf and [EFTA00001932](https://www.justice.gov/epstein/files/DataSet%201/EFTA00001932.pdf).pdf are **image-based scanned documents** with invisible OCR text layers. The OCR text layer uses PDF Text Rendering Mode 3 (invisible) and is positioned BEHIND the scanned image in the rendering order. The text appears garbled because OCR software attempted to read:
- A photograph of a financial ledger on a manila envelope ([EFTA00000476](https://www.justice.gov/epstein/files/DataSet%201/EFTA00000476.pdf)) at only 96 DPI
- A handwritten letter in cursive blue ink on decorative paper ([EFTA00001932](https://www.justice.gov/epstein/files/DataSet%201/EFTA00001932.pdf)) at only 96 DPI

Neither document contains text-based PDF content with black rectangle overlays hiding selectable text underneath. The viral claim of "poorly redacted" documents exposing hidden text behind copy-paste-removable black bars is **not supported** by the PDF structure of these specific files.

---

## METHODOLOGY

### Files Analyzed

| File | Version | Path | Size |
|------|---------|------|------|
| [EFTA00000476](https://www.justice.gov/epstein/files/DataSet%201/EFTA00000476.pdf).pdf | Original (Dec 19) | local analysis file `originals/december_2025/VOL00001/IMAGES/0001/EFTA00000476.pdf` | 365,781 bytes |
| [EFTA00000476](https://www.justice.gov/epstein/files/DataSet%201/EFTA00000476.pdf).pdf | Current (re-release) | DOJ dataset file `dataset1/DataSet` 1/DataSet 1/VOL00001/IMAGES/0001/[EFTA00000476](https://www.justice.gov/epstein/files/DataSet%201/EFTA00000476.pdf).pdf` | 362,263 bytes |
| [EFTA00001932](https://www.justice.gov/epstein/files/DataSet%201/EFTA00001932.pdf).pdf | Original (Dec 19) | local analysis file `originals/december_2025/VOL00001/IMAGES/0002/EFTA00001932.pdf` | 573,379 bytes |
| [EFTA00001932](https://www.justice.gov/epstein/files/DataSet%201/EFTA00001932.pdf).pdf | Current (re-release) | DOJ dataset file `dataset1/DataSet` 1/DataSet 1/VOL00001/IMAGES/0002/[EFTA00001932](https://www.justice.gov/epstein/files/DataSet%201/EFTA00001932.pdf).pdf` | 572,881 bytes |

### Tools Used
- PDF analysis tools for PDF structure analysis
- pdftotext for text extraction
- pdfimages for image listing
- PIL/numpy/scipy for pixel-level image comparison
- Direct content stream parsing for rendering order verification

---

## FINDING 1: PDF RENDERING PIPELINE

All four PDFs (both versions of both files) share an identical 5-layer rendering structure:

```
Layer 1: Graphics state save (q)
Layer 2: INVISIBLE OCR TEXT LAYER (Text Rendering Mode 3)
Layer 3: SCANNED IMAGE (/Im0 Do) - rendered ON TOP of text layer
Layer 4: WHITE RECTANGLE (clip mask) + BLACK EFTA LABEL at bottom
Layer 5: End
```

### Evidence from content streams:

**[EFTA00000476](https://www.justice.gov/epstein/files/DataSet%201/EFTA00000476.pdf) Original** - Content streams [23, 6, 7, 24, 25]:
- Stream 23 (1 byte): `q` - graphics state save
- Stream 6 (24,617 bytes): OCR text with `3 Tr` (invisible mode), 410 unique Tz values
- Stream 7 (34 bytes): `q / 864 0 0 576.75 0 0 cm / /Im0 Do / Q` - image rendering
- Stream 24 (171 bytes): White rectangle fill + hex-encoded "[EFTA00000476](https://www.justice.gov/epstein/files/DataSet%201/EFTA00000476.pdf)" label
- Stream 25: End

**[EFTA00001932](https://www.justice.gov/epstein/files/DataSet%201/EFTA00001932.pdf) Original** - Content streams [29, 22, 4, 30, 31]:
- Stream 29 (1 byte): `q` - graphics state save
- Stream 22 (15,993 bytes): OCR text with `3 Tr` (invisible mode), 279 unique Tz values
- Stream 4 (34 bytes): Image rendering
- Stream 30 (142 bytes): White rectangle fill + hex-encoded "[EFTA00001932](https://www.justice.gov/epstein/files/DataSet%201/EFTA00001932.pdf)" label
- Stream 31: End

### Critical Detail: Text Rendering Mode 3

From the raw content streams:
```
3 Tr
```

PDF Text Rendering Mode 3 means the text is **neither filled nor stroked** - it is completely invisible. This is the standard method used by OCR software (such as ABBYY FineReader, Adobe Acrobat's OCR, or OmniPage) to create a "searchable" text layer behind a scanned image. The text exists only for search/copy functionality, not for visual display.

---

## FINDING 2: OCR SIGNATURE PROOF

The text layers exhibit unmistakable OCR signatures:

### Wildly Varying Font Sizes
| Document | Version | Unique Font Sizes |
|----------|---------|-------------------|
| [EFTA00000476](https://www.justice.gov/epstein/files/DataSet%201/EFTA00000476.pdf) | Original | 197 |
| [EFTA00000476](https://www.justice.gov/epstein/files/DataSet%201/EFTA00000476.pdf) | Current | Different OCR run |
| [EFTA00001932](https://www.justice.gov/epstein/files/DataSet%201/EFTA00001932.pdf) | Original | 266 |
| [EFTA00001932](https://www.justice.gov/epstein/files/DataSet%201/EFTA00001932.pdf) | Current | Different OCR run |

Real PDF text typically uses 2-10 font sizes. Having 197-266 unique sizes means OCR software is assigning different sizes to each word to match the spatial dimensions detected in the scan.

### Wildly Varying Horizontal Scaling (Tz)
| Document | Unique Tz Values |
|----------|-----------------|
| [EFTA00000476](https://www.justice.gov/epstein/files/DataSet%201/EFTA00000476.pdf) Original | 410 |
| [EFTA00000476](https://www.justice.gov/epstein/files/DataSet%201/EFTA00000476.pdf) Current | 272 |
| [EFTA00001932](https://www.justice.gov/epstein/files/DataSet%201/EFTA00001932.pdf) Original | 279 |
| [EFTA00001932](https://www.justice.gov/epstein/files/DataSet%201/EFTA00001932.pdf) Current | 248 |

The `Tz` operator sets horizontal text scaling. OCR software varies this per-word to fit each recognized word into the exact pixel width of the original. Real text documents have Tz=100 (or a handful of values). 272-410 unique values is absolute proof of OCR generation.

### Standard OCR Font Names
All four PDFs use identical non-embedded standard fonts:
- `Courier` (OPBaseFont0)
- `Helvetica` (OPBaseFont1)
- `Helvetica-Bold` (OPBaseFont2)
- `Times-Roman` (OPBaseFont3)
- `ArialMT` (OPExtFont0)

These are the default substitute fonts used by OCR engines when the actual font is unknown. The `OPBaseFont` naming convention is specific to OmniPage OCR software.

---

## FINDING 3: IMAGE ANALYSIS

### Both PDFs contain a single embedded image per page

| Document | Image Size | Color | Resolution | Coverage |
|----------|-----------|-------|------------|----------|
| [EFTA00000476](https://www.justice.gov/epstein/files/DataSet%201/EFTA00000476.pdf) | 1152x769 | Indexed (1-bit/8bpc) | 96 DPI | Full page |
| [EFTA00001932](https://www.justice.gov/epstein/files/DataSet%201/EFTA00001932.pdf) | 1152x769 | Indexed (1-bit/8bpc) | 96 DPI | Full page |

96 DPI is extremely low for OCR purposes (typical OCR requires 300+ DPI for good accuracy). This explains the garbled text output.

### Images are DIFFERENT between versions

Pixel-level comparison shows the images were re-scanned or re-processed:

| Document | Changed Pixels | Percentage |
|----------|---------------|------------|
| [EFTA00000476](https://www.justice.gov/epstein/files/DataSet%201/EFTA00000476.pdf) | 716,787 / 885,888 | 80.91% |
| [EFTA00001932](https://www.justice.gov/epstein/files/DataSet%201/EFTA00001932.pdf) | 808,168 / 885,888 | 91.23% |

Despite the massive pixel-level difference, the images look visually similar to the human eye - this indicates re-scanning from the same physical document (or re-processing with different settings).

### [EFTA00001932](https://www.justice.gov/epstein/files/DataSet%201/EFTA00001932.pdf) has an ADDITIONAL redaction in the current version

Visual comparison reveals the current (re-released) version of [EFTA00001932](https://www.justice.gov/epstein/files/DataSet%201/EFTA00001932.pdf) has a new black rectangle that does not exist in the December 19 original:

- **Original**: 1 black rectangle at image coordinates (73,105)-(165,222) - top-left area (likely covering the greeting/name)
- **Current**: 2 black rectangles - the original one PLUS a new one at approximately (370,524)-(403,676) - middle area of the letter

This new redaction is **baked into the scanned image itself**, not a PDF annotation overlay. It was applied by re-scanning or re-processing the physical document with an additional physical or digital redaction.

---

## FINDING 4: WHAT IS THE "EXPOSED TEXT"?

### [EFTA00000476](https://www.justice.gov/epstein/files/DataSet%201/EFTA00000476.pdf) (Financial Ledger)

The document is a **photograph of a financial ledger** lying on a manila envelope. The image shows:
- A spreadsheet/table with columns for dates, descriptions, and dollar amounts
- Black marker redactions covering certain cells in the physical document
- The document was photographed (not flatbed scanned) at low resolution

The "213 lines of exposed text" are OCR's attempt to read this low-resolution photograph:
```
04044 so 4,10y yentaYI ory a 4
Afaoutt W a Paso pew teoi 016.4
L290 /39 51 92100'0I
```

This is not "exposed hidden text" - it is garbled OCR of the visible printed content in the photograph, mangled by:
1. Low resolution (96 DPI)
2. Angle distortion (it's a photograph, not a scan)
3. Complex table layout confusing the OCR engine
4. Black marker redactions creating partial character occlusion

### [EFTA00001932](https://www.justice.gov/epstein/files/DataSet%201/EFTA00001932.pdf) (Handwritten Victim Letter)

The document is a **handwritten letter in blue cursive ink** on decorative stationery paper with a cartoon owl design. The "47 lines of exposed text" are OCR's attempt to read cursive handwriting:

```
ear e.i-freA;
1- i.O,,-_)c ot( hac.i. a wonderi-iti 110ii-
dali SeaSO11.
```

Manual reconstruction suggests this reads approximately:
```
Dear [name],
I hope [you] had a wonderful holiday
season.
```

The letter is a **victim thank-you letter** to Epstein, expressing gratitude for:
- Holiday/Christmas celebrations
- Trips to Palm Beach, Las Vegas, Mexico, and an island
- Flying her sister out to visit
- Use of a Manhattan apartment
- Help seeing her mother
- "Pushing me to be at my best"

This is consistent with the well-documented grooming pattern where victims were conditioned to express gratitude for material benefits.

---

## FINDING 5: NO BLACK RECTANGLE OVERLAY HIDING TEXT

### Annotation Check
| Document | Version | PDF Annotations | Redaction Annotations |
|----------|---------|----------------|----------------------|
| [EFTA00000476](https://www.justice.gov/epstein/files/DataSet%201/EFTA00000476.pdf) | Original | 0 | 0 |
| [EFTA00000476](https://www.justice.gov/epstein/files/DataSet%201/EFTA00000476.pdf) | Current | 0 | 0 |
| [EFTA00001932](https://www.justice.gov/epstein/files/DataSet%201/EFTA00001932.pdf) | Original | 0 | 0 |
| [EFTA00001932](https://www.justice.gov/epstein/files/DataSet%201/EFTA00001932.pdf) | Current | 0 | 0 |

**Zero PDF redaction annotations exist in any version.** There are no "overlay" black rectangles in the PDF structure.

### Drawing Object Check
| Document | Version | Drawings | Black-Filled | Description |
|----------|---------|----------|-------------|-------------|
| [EFTA00000476](https://www.justice.gov/epstein/files/DataSet%201/EFTA00000476.pdf) | Original | 1 | 0 | White page border only |
| [EFTA00001932](https://www.justice.gov/epstein/files/DataSet%201/EFTA00001932.pdf) | Original | 1 | 0 | White page border only |

The only drawing objects are white-filled page borders. **No black rectangles exist as PDF drawing objects.**

### Where are the black rectangles?

The black rectangles visible in these documents are **baked into the scanned images themselves**. They are part of the pixel data of the embedded raster image. This means:

1. The physical documents were redacted (with black tape, marker, or digital masking) BEFORE scanning
2. The scanner captured the already-redacted document
3. No text exists "behind" the black rectangles because the text was physically obscured before the scan

For [EFTA00000476](https://www.justice.gov/epstein/files/DataSet%201/EFTA00000476.pdf) (financial ledger):
- 143,650 near-black pixels in the image (17.1% of image area)
- Largest black region: 998x561 pixels (the table area with multiple column redactions)
- These are physical marker/tape redactions on the printed document, captured in the photograph

For [EFTA00001932](https://www.justice.gov/epstein/files/DataSet%201/EFTA00001932.pdf) (victim letter):
- Original: 1 black region at (73,105)-(165,222) = 92x117 pixels
- Current: Same region PLUS new region at (370,524)-(403,676) = 33x152 pixels
- The additional redaction in the re-release was applied to the image (re-scanned or digitally added to the raster)

---

## FINDING 6: ORIGINAL vs. CURRENT COMPARISON

### Text Layer Differences
| Document | Original Text Length | Current Text Length | Identical? |
|----------|---------------------|--------------------| -----------|
| [EFTA00000476](https://www.justice.gov/epstein/files/DataSet%201/EFTA00000476.pdf) | 2,853 chars | 2,392 chars | No |
| [EFTA00001932](https://www.justice.gov/epstein/files/DataSet%201/EFTA00001932.pdf) | 1,409 chars | 1,240 chars | No |

The text layers differ because **different OCR runs produce different results** from different scans of the same physical document. The current versions were re-scanned and re-OCR'd, producing slightly different (but equally garbled) text.

Key differences for [EFTA00001932](https://www.justice.gov/epstein/files/DataSet%201/EFTA00001932.pdf):
- Original OCR produces 257 words; Current OCR produces 229 words
- The original has "Mexico", "Vegas", "Friends"; the current has "Arizona", "Christmas", "circus"
- Both are equally garbled attempts at reading the same handwriting
- The current version lost some text near the new redaction area

### File Size Differences
| Document | Original Size | Current Size | Difference |
|----------|--------------|-------------|------------|
| [EFTA00000476](https://www.justice.gov/epstein/files/DataSet%201/EFTA00000476.pdf) | 365,781 | 362,263 | -3,518 bytes |
| [EFTA00001932](https://www.justice.gov/epstein/files/DataSet%201/EFTA00001932.pdf) | 573,379 | 572,881 | -498 bytes |

The slight size differences are consistent with different compression of the re-scanned images and different OCR text content.

---

## CONCLUSION

### Answer to the Key Question

**Do the original December 19 PDFs have actual selectable text behind black visual rectangles (text-based PDFs with overlay redactions)?**

**NO.** The evidence conclusively shows:

1. **These are image-based scanned documents**, not text-based PDFs
2. **The text layer is invisible OCR** (Text Rendering Mode 3), placed behind the image
3. **The OCR is garbled** because of 96 DPI resolution, cursive handwriting, and photographic distortion
4. **The black rectangles are in the images**, not PDF overlays - they represent physical redactions applied before scanning
5. **No PDF annotations or drawing objects** create the visible redactions
6. **The "exposed text" is garbled OCR artifacts**, not hidden text behind removable black bars

### Assessment of the Viral "Poorly Redacted" Claim for These Specific Files

For [EFTA00000476](https://www.justice.gov/epstein/files/DataSet%201/EFTA00000476.pdf) and [EFTA00001932](https://www.justice.gov/epstein/files/DataSet%201/EFTA00001932.pdf) specifically, the claim that redacted text can be "exposed" by copying/pasting from behind black rectangles is **overstated**. The "exposed text" is the OCR engine's garbled attempt at reading visible (non-redacted) content from a low-resolution scan. It does not reveal information hidden by the redactions.

However, it is worth noting:
- [EFTA00001932](https://www.justice.gov/epstein/files/DataSet%201/EFTA00001932.pdf) did receive an **additional physical redaction** in the re-release, covering what appears to be a signature or name area. This confirms that DOJ recognized at least some content needed additional redaction.
- The OCR text, while garbled, does provide fragmentary readable content from the non-redacted portions (e.g., recognizable words like "Christmas," "Manhattan," "Mexico," "friends," "wonderful")
- Other documents in the collection may have different redaction methods - this analysis applies only to these two specific files

### Root Cause of Garbled "Exposed Text"

The text appears garbled because:
1. **96 DPI scan resolution** - far below the 300 DPI minimum recommended for OCR
2. **Handwriting recognition failure** ([EFTA00001932](https://www.justice.gov/epstein/files/DataSet%201/EFTA00001932.pdf)) - cursive blue ink is extremely difficult for OCR
3. **Photographic distortion** ([EFTA00000476](https://www.justice.gov/epstein/files/DataSet%201/EFTA00000476.pdf)) - the document was photographed, not flatbed scanned
4. **OmniPage OCR limitations** - the `OPBaseFont` naming in the fonts confirms OmniPage was used, which has limited handwriting recognition
5. **Indexed color space** - both images use 1-bit indexed color (essentially black and white), losing any gray-scale information that could help character recognition

---

## APPENDIX: Technical Evidence

### Content Stream: [EFTA00000476](https://www.justice.gov/epstein/files/DataSet%201/EFTA00000476.pdf) Original - OCR Layer (first 500 bytes)
```
%WB0AiUxr
q
1 0.06 -0.06 1 17.43 -26.32 cm
BT
0 0 0 rg
0 0 0 RG
1 0 0 1 252.8 489 Tm
77.33 Tz
3 Tr/OPBaseFont0 8.33 Tf(\)1 )Tj
1 0 0 1 246.23 475.12 Tm
65.18 Tz/OPBaseFont0 15.62 Tf(4 )Tj
```

Key operators:
- `3 Tr` = Text Rendering Mode 3 (invisible)
- `77.33 Tz` / `65.18 Tz` = per-word horizontal scaling (OCR signature)
- `/OPBaseFont0` = OmniPage default font substitute

### Content Stream: Image Rendering Layer
```
q
864 0 0 576.75 0 0 cm
/Im0 Do
Q
```
This renders the image at full page size, ON TOP of the invisible text layer.

### Font Inventory ([EFTA00000476](https://www.justice.gov/epstein/files/DataSet%201/EFTA00000476.pdf) Original)
```
(9,  'n/a', 'Type1', 'Courier',        'OPBaseFont0', 'WinAnsiEncoding')
(10, 'n/a', 'Type1', 'Helvetica',      'OPBaseFont1', 'WinAnsiEncoding')
(11, 'n/a', 'Type1', 'Helvetica-Bold', 'OPBaseFont2', 'WinAnsiEncoding')
(12, 'n/a', 'Type1', 'Times-Roman',    'OPBaseFont3', 'WinAnsiEncoding')
(13, 'n/a', 'Type1', 'ArialMT',        'OPExtFont0',  'WinAnsiEncoding')
```

All fonts are non-embedded standard Type1 fonts with OmniPage naming.
