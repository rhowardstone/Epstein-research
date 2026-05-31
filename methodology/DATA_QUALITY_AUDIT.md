# DATA QUALITY AUDIT: "bad_overlay" Redaction Records

**Database:** the primary document text database (v2 redaction database, 1.8M records)
**Date:** 2026-02-10 | **Updated:** 2026-02-12
**Auditor:** Systematic analysis of document text records
**Purpose:** Determine what fraction of "bad_overlay" records contain genuinely recoverable hidden text vs. OCR noise from degraded scans.

**Scope Note (added 2026-02-12):** This audit was conducted against the v2 redaction database only. The subsequently completed full_text_corpus.db (1,380,937 documents, 2,731,796 pages across all 12 datasets) provides a parallel, more reliable text extraction method (PyMuPDF). The audit's conclusions about bad_overlay noise are confirmed by subsequent analysis: the "bad_overlay" label reflects garbled OCR of baked-in JPEG redaction bars, not actual hidden text beneath annotation-type redactions. Per REDACTION_TEXT_LAYER_ANALYSIS.md, DS10's PDFs use invisible OCR text layers (Text Rendering Mode 3 at 96 DPI), and the black boxes are baked JPEG pixels, not PDF annotation overlays. Zero annotation-type (Method 1) redactions were found across the entire corpus.

---

## Executive Summary

**The honest verdict: The vast majority of "bad_overlay" records are NOT hidden text behind removable redactions. They are OCR artifacts -- fragments of characters, partial words, and scan noise that the detection algorithm misclassified as "text under a bad overlay."**

Of 616,233 bad_overlay records:
- ~20% (122,922) are single characters or 2-3 character fragments -- pure noise
- ~18% (108,709) are 4-10 character fragments without spaces -- mostly truncated word edges
- ~17% (103,722) are short fragments with spaces -- partial OCR captures
- ~43% (264,575) are 11-50 characters -- mixed quality, mostly garbled
- **~2.6% (16,305) are 51+ characters -- the only tier with potentially substantive content**

Even within that 2.6%, many records contain garbled OCR rather than coherent text. A realistic estimate is that **fewer than 1% of bad_overlay records contain genuinely readable, coherent English text.**

However, the small number that ARE real include some extraordinarily significant content (FBI hotline tips, legal documents, email headers with names).

---

## 1. Confidence Bucket Distribution

| Confidence Range | Count   | Avg Text Length | Min Len | Max Len |
|-----------------|---------|-----------------|---------|---------|
| 0.95 - 1.00    | 49,102  | 52.9 chars      | 1       | 3,938   |
| 0.90 - 0.95    | 22,132  | 30.3 chars      | 1       | 48      |
| 0.85 - 0.90    | 53,301  | 25.0 chars      | 1       | 38      |
| 0.80 - 0.85    | 99,252  | 18.2 chars      | 1       | 29      |
| 0.75 - 0.80    | 185,526 | 9.9 chars       | 1       | 19      |
| 0.70 - 0.75    | 206,920 | 3.7 chars       | 1       | 9       |

**Key observation:** Confidence correlates strongly with text length but NOT with text quality. The 0.70-0.75 bucket (206,920 records) has an average text length of 3.7 characters -- these are overwhelmingly single characters and short fragments. Even the highest confidence bucket (0.95-1.00) averages only 52.9 characters, and includes single-character records.

The max text length of 3,938 in the top bucket is a significant outlier -- this is one of the FBI hotline tip compilations (see Section 8).

---

## 2. High-Confidence (>0.95) Sample -- 20 Random Records

Sample of actual hidden_text values from records with confidence > 0.95:

| Text Sample | Assessment |
|------------|------------|
| `EFT` | EFTA number fragment bleeding through -- noise |
| `JEGE INC Primary Account:` | Partial business name + header -- edge OCR capture |
| `Number` | Single word -- could be anything |
| `"USAHUB-USAJournal111" < IMINE>` | Garbled email header with HTML -- noise |
| `ATIVE K t i JFK i D lt #2240` | Heavily garbled -- noise |
| `EFTA` | Stamp fragment -- noise |
| `E` | Single character -- noise |
| `EFTA01639` | Bates number fragment -- noise |
| `rum I` | Fragment -- noise |
| `g y ve C/P 33172 Y inactive Holterbosch NY 10152 Y P P Y Y Y Y Y Y Y` | Looks like a fragmented database/form record -- partially coherent |
| `SDNY_GM_02756555 SUBJECT TO PROTECTIVE ORDER PARAGRAPHS 7 8 9 10 15 and 17` | Bates stamp + standard protective order boilerplate -- real text but boilerplate |
| `From: Jay Gunz ent: pm` | Truncated email header -- real but fragmentary |
| `t Numbs telephone number ather), was !!!!!!!!!lWderal invest` | Heavily garbled -- noise |
| `bject: Fwd: FW: VI Daily News: AG says Epstein` | Truncated email subject line -- real content |
| `ou es ey give me t e correct contact person .` | Missing characters throughout -- garbled OCR |
| `N 243105 (P) Airframe Battery. #1--Capacity Check 6 ',I OS` | Aircraft maintenance record -- partially readable |
| `Subject: Re: Victim assistance` | Clean email header -- real content |
| `(USANYS) bject: RE: [EXTERNAL]` | Truncated email header -- real but fragmentary |

**Verdict for this tier:** Even at >0.95 confidence, roughly 60-70% of records are noise, fragments, or boilerplate. About 20-30% contain partially readable real text. About 10% contain clearly coherent text.

---

## 3. Long + High-Confidence Records (>50 chars, >0.9 confidence)

This is the subset most likely to contain real content. A sample of 20 records shows:

**Clearly coherent/real content (~45% of this subset):**
- `"SOUTHERN TRUST COMPANY, INC. 1,000,000.00 MONEY TRANSFER"` -- financial transaction record
- `"SDNY_GM_02757248 SUBJECT TO PROTECTIVE ORDER PARAGRAPHS 7 8 9 10 15 and 17"` -- bates/boilerplate
- `"THIS CHECK HAS A COLORED BACKGROUND AND CONTAINS MULTIPLE SECURITY FEATURES"` -- check boilerplate
- `"Daniel Siad < yTo: ;'Jean Luc Brunell< >bieCommition de mes 2 filles Chez toi"` -- email about Jean-Luc Brunel (notable name)
- `"Subject: Fw: Formal appeal for preliminary denial covered action 2015-016"` -- email subject
- `"Name. GHISLAINE N MAXWELL Application RESIDENCE PREMISES Type: Application 2/21/2006"` -- real structured data

**Partially readable / garbled (~30%):**
- `"o: Andrew King c: Nathaniel Morgan MMIPIPcoverage and Glendow"` -- garbled email
- `"Warwick Wicksman _ <*eevacation mail. m> gary RE: LSJ"` -- garbled email header
- `"suoject: soutnern rinanclal LU. - KYI. ana cream a crea1L aerlvatives/convert1DLe"` -- severely garbled
- `"lues*ay, ay !,?rirMl i :* 41. I t tan lson, Justin D"` -- heavily garbled

**Pure noise / financial data (~25%):**
- SPX options data strings (2000+ chars of numbers)
- `"Sep 2013 Dec Mar 2O14 Jun 6.1604 O. J.DVU 0-6.1000 P-6.0500"` -- garbled chart data
- `"l O d the rubel deeost o over erase downers sauce of folds or source"` -- pure OCR garbage

---

## 4. English Word Analysis

How many bad_overlay records contain common English words:

| Pattern | Count | % of 616,233 |
|---------|-------|---------------|
| Contains " the " | 4,888 | 0.79% |
| Contains " and " | 4,661 | 0.76% |
| Contains " was " | 745 | 0.12% |
| Contains " for " | 3,903 | 0.63% |
| Contains " that " | 1,059 | 0.17% |
| Contains " with " | 1,539 | 0.25% |
| Contains " from " | 1,998 | 0.32% |
| **Contains 2+ common words** | **2,840** | **0.46%** |

**Only 2,840 records (0.46%) contain two or more common English words.** This is the strongest signal we have for "actually readable text." The overwhelming majority of bad_overlay records do not contain recognizable English.

---

## 5. Documents with ONLY bad_overlay Records

**62,009 distinct EFTA documents** have only bad_overlay records (no proper_redaction records).

These documents likely have NO actual redactions -- the "bad_overlay" detections are entirely from OCR noise on degraded scans. These documents should be considered **zero-signal for hidden text recovery**.

---

## 6. Documents with BOTH bad_overlay AND proper_redaction Records

**156,951 distinct EFTA documents** have both types.

This is the more interesting set. In these documents, proper_redaction records mark genuine redaction rectangles (which almost never have recoverable text -- only 32,357 of 1,192,682 proper_redaction records have any hidden_text at all, a 2.7% rate). The bad_overlay records in the same documents are likely picking up edge artifacts around the real redactions or OCR noise in degraded areas of the scan.

**Total distinct EFTA documents with bad_overlay:** 218,960
**Total distinct EFTA documents with proper_redaction:** 314,550
**Total distinct EFTA documents overall:** 376,571

---

## 7. Side-by-Side Comparison: Same Document, Both Types

Example from [EFTA01342644](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01342644.pdf) (a document with both types):

**bad_overlay records (18 of them on page 0):**
- `"author"` (conf 0.732)
- `"know"` (conf 0.721)
- `"ompany"` (conf 0.732)
- `"ITN Case ID XXXXXX"` (conf 0.846)
- `"Mobile Number"` (conf 0.786)
- `"Longitude Latitude"` (conf 0.856)
- `"Radius"` (conf 0.735)
- `"you m"`, `"accur"`, `"igative"`, `"as loc"`, `"source"`, `"atabas"`, `"which"`, `"ct"`, `"nce in"`, `"w th"`, `"an indic"` (all conf 0.71-0.74)

**proper_redaction records (5 on same page):**
- All have NULL/empty hidden_text, confidence 0.50-0.51

**Interpretation:** This is a textbook example of the OCR noise problem. The document has a form layout with field labels ("Mobile Number", "Longitude", "Latitude"). The bad_overlay detector is picking up text fragments around or near the actual redaction boxes. The words `"ompany"`, `"atabas"`, `"w th"`, `"igative"` are clearly truncated edge captures of "Company", "database", "with", "investigative". These are NOT text hidden behind removable overlays -- they are visible text fragments that the OCR captured near redaction boundaries.

---

## 8. PLIST/XML Forensic Records

**51 records** contain PLIST, XML, DOCTYPE, or CFBundle references.

These are real and significant. They represent Apple property list metadata that was embedded in email attachments and captured by the redaction scanner. Examples:

| EFTA | Sample |
|------|--------|
| [EFTA02554189](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02554189.pdf) | `<?xml version="1.0" encoding IDOCTYPE li PUBLIC //A` |
| [EFTA01766832](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01766832.pdf) | `li t PUBLIC " //A l //DTD PLIST 1 0//EN" "htt //` |
| [EFTA01781767](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01781767.pdf) | `Sent from my iPhone <?xml version "1 0" encoding "UTF 8"?> <!DOCTYPE plist PUBLIC " //Apple//DTD PLIST 1 0//EN"` |
| [EFTA02114558](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02114558.pdf) | `<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.co` |
| [EFTA01769469](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01769469.pdf) | `<?xml version "1 0" encoding "UTF 8"?>` |

**Assessment:** These are genuinely interesting forensic artifacts. They confirm that email source code / MIME structure was present in the PDF layers. The "Sent from my iPhone" + plist combination confirms these are iOS email metadata blobs. However, these are metadata artifacts, not redacted content -- they were never intentionally hidden, they just happened to be in a PDF layer that the scanner detected.

---

## 9. FBI Prominent Names Document ([EFTA00004800](https://www.justice.gov/epstein/files/DataSet%203/EFTA00004800.pdf))

[EFTA00004800](https://www.justice.gov/epstein/files/DataSet%203/EFTA00004800.pdf) contains 30 records across pages 0-5:
- **5 proper_redaction records on page 0** (conf 0.50-0.57, no hidden text)
- **8 bad_overlay records on pages 1-2** with text like:
  - `"dn"` (conf 0.845)
  - `"0 R"` (conf 0.879)
  - `"$.jpg"` (conf 0.859)
  - `"5.jog"` (conf 0.867)
  - `"1"` (conf 0.724)
  - `"1 6 jpg"` (conf 0.890)
  - `"98iP0"` (conf 0.907)
  - `"5909"` (conf 0.902)
- More proper_redaction records on pages 2-5

**Assessment:** The bad_overlay records for this document are pure garbage -- `.jpg` fragments, random digits, garbled characters. These are OCR artifacts from what appears to be a scanned document with images (the `.jpg` references suggest image file name fragments bleeding through). There is NO recoverable meaningful text in the bad_overlay records for this document.

---

## 10. Overall Coherence Assessment

### Text Length Distribution

| Category | Count | % of Total |
|----------|-------|------------|
| 1 character | 56,617 | 9.19% |
| 2-3 characters | 66,305 | 10.76% |
| 4-10 characters | 212,431 | 34.47% |
| 11-30 characters | 224,167 | 36.38% |
| 31-50 characters | 40,408 | 6.56% |
| 51-100 characters | 12,247 | 1.99% |
| 101-200 characters | 2,941 | 0.48% |
| 200+ characters | 1,117 | 0.18% |

### Content Pattern Analysis

| Pattern | Count | Notes |
|---------|-------|-------|
| Multi-word (2+ spaces) | 250,169 | Having spaces does not mean coherent |
| Sentence-like (3+ spaces) | 165,725 | Many are line-broken fragments |
| Paragraph-like (6+ spaces) | 39,731 | Mostly multiline fragments with newlines |
| Single digit only | 4,582 | Pure numeric noise |
| Contains "EFTA" | 3,035 | Bates number bleedthrough |
| Contains "SDNY_GM" | 689 | Discovery stamp boilerplate |
| Contains "PROTECTIVE ORDER" | 970 | Legal boilerplate text |
| Contains Subject: header | 16,625 | Email subject line fragments |
| Contains From: header | 1,365 | Email sender fragments |

### Character Class Breakdown

| Starts With | Count | % |
|------------|-------|---|
| Letter (A-Z, a-z) | 502,654 | 81.6% |
| Special character | 58,313 | 9.5% |
| Digit | 6,991 | 1.1% |

### What the 1-Character Records Actually Are

The top single characters detected as "hidden text":
`i` (6,776), `a` (4,451), `>` (3,269), `I` (2,758), `l` (2,485), `n` (2,247), `e` (1,799), `t` (1,575), `d` (1,512), `1` (1,452), `M` (1,397), a bullet `*` (1,371)

These are overwhelmingly OCR artifacts -- single-pixel character captures at the edges of redaction boxes.

### Dataset Source Breakdown

| Source | bad_overlay Count |
|--------|-------------------|
| ds1-9_11-12 | 70,940 (11.5%) |
| ds10 | 545,293 (88.5%) |

The ds10 dataset contributes 88.5% of all bad_overlay records, suggesting this dataset may have lower scan quality or the scanner was run with more aggressive settings.

---

## The Genuinely Interesting Records

Despite the noise, there ARE records of genuine significance. The longest records (200+ chars) include:

1. **FBI Hotline Tips ([EFTA01660651](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01660651.pdf), [EFTA01660679](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01660679.pdf)):** 3,000-3,900 character records containing detailed FBI hotline tip summaries. These include complainant reports about sex trafficking, named individuals, and specific allegations. These are clearly real text that was captured from an underlying PDF layer.

2. **Ghislaine Maxwell Records ([EFTA01653379](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01653379.pdf)):** Residence application data, including birth country, height, application dates.

3. **Jean-Luc Brunel Email ([EFTA01986452](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01986452.pdf)):** `"Daniel Siad < yTo: ;'Jean Luc Brunell< >bieCommition de mes 2 filles Chez toi"` -- French-language email reference.

4. **Legal Documents:** Protective order references, subpoena subjects, victim assistance communications.

5. **Financial Records:** Southern Trust Company transfers, account values, options trading data.

6. **Aircraft Maintenance Records ([EFTA02110383](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02110383.pdf), [EFTA02110465](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02110465.pdf)):** Airframe service records with serial numbers.

---

## Final Honest Assessment

### What You Can Trust

- **Records >200 chars with confidence >0.95:** ~1,117 records. About 40-50% of these contain genuinely readable content. Manual review is worthwhile for this small set.
- **Records 51-200 chars with confidence >0.95:** ~15,188 records. About 20-30% contain useful partial content (email headers, names, subject lines). Worth sampling but expect heavy noise.
- **PLIST/XML records (51 total):** Real forensic metadata artifacts. Not "hidden" content, but genuine technical data.
- **Records containing "Subject:" or "From:" headers (~18,000):** Many of these are real email header fragments showing through scan layers. Partially readable.

### What You Cannot Trust

- **Everything with text length < 10 characters (335,353 records, 54.4%):** This is noise. Single characters, truncated word edges, digits. Zero informational value.
- **Records with confidence < 0.85 but no common English words (the vast majority of the 545,000 low-confidence records):** OCR artifacts.
- **The "62,009 documents with only bad_overlay" set:** These documents almost certainly have no actual redactions. The scanner detected OCR noise.

### The Numbers

| Category | Est. Count | % of 616,233 | Trust Level |
|----------|-----------|---------------|-------------|
| Pure noise (1-3 chars, garbled) | ~335,000 | ~54% | ZERO -- discard |
| Word fragments (4-10 chars, no coherent sentences) | ~210,000 | ~34% | NEAR-ZERO -- mostly OCR edge captures |
| Partially readable (11-50 chars, some English) | ~55,000 | ~9% | LOW -- fragments of headers/labels |
| Potentially readable (51+ chars, some coherence) | ~12,000 | ~2% | MEDIUM -- worth sampling |
| Clearly substantive (200+ chars, coherent English) | ~500 | ~0.08% | HIGH -- manual review recommended |

### Bottom Line

**~0.08% of bad_overlay records (roughly 500 out of 616,233) contain clearly substantive, readable text.** Another ~2% contain partially useful fragments. The remaining ~98% is OCR noise that should not be treated as "recovered hidden text."

The detection algorithm appears to have been run with very aggressive sensitivity, causing it to flag any OCR artifact near a dark region as a "bad overlay with hidden text." This produced a 98% false positive rate.

**Recommendation:** Create a curated subset of bad_overlay records where `LENGTH(hidden_text) > 100 AND confidence > 0.95` (approximately 3,500 records) and manually review those. Everything else should be considered noise unless specifically investigated.

**Update (2026-02-12):** This curation recommendation was implemented via HIDDEN_TEXT_COMPLETE_REVIEW.md (report #95). However, the full_text_corpus.db now provides a more reliable text extraction path for most documents -- PyMuPDF captures the same invisible OCR text layer without the false positive problem. The curation recommendation was sound for its time but is now secondary to full corpus search via full_text_corpus.db.

---

*This audit was generated from direct systematic searches against the primary document text database. All numbers are exact counts from the database. Quality assessments of text samples are based on human-readable inspection of random samples.*
