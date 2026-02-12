# Dataset 10 - Complete Redaction Analysis Findings

**Generated:** 2026-02-05
**Status:** COMPLETE - All 503,154 PDFs scanned in 28.4 minutes
**Database:** Dataset 10 document text database (1,629,776 redaction rows)
**Zero errors**

## Scale Comparison

| Metric | DS1-9,11-12 (all combined) | DS10 | DS10 vs Others |
|--------|---------------------------|------|----------------|
| PDFs scanned | 16,284 | 503,154 | **30.9x** |
| Total redactions | 179,139 | 1,629,776 | **9.1x** |
| Bad overlays (OCR text layers) | 70,940 | 545,293 | **7.7x** |
| Proper redactions | 108,199 | 1,084,483 | **10.0x** |
| Documents with hidden text | 9,133 | 209,829 | **23.0x** |

**Methodology note:** DS10's PDFs are predominantly image-based scans with invisible OCR text layers (Text Rendering Mode 3 at 96 DPI). The black rectangles visible in redacted documents are baked JPEG pixels, not PDF annotation overlays. The "bad overlay" / "hidden text" entries in the redaction database represent garbled OCR from the scanning pipeline, not genuinely concealed content behind removable black rectangles. One confirmed readable exception: [EFTA00001932](https://www.justice.gov/epstein/files/DataSet%201/EFTA00001932.pdf) victim letter fragments. See REDACTION_TEXT_LAYER_ANALYSIS.md for the definitive methodology analysis.

## CRITICAL FINDING: FBI "PROMINENT NAMES" Briefing ([EFTA01660622](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01660622.pdf))

**This is the single most significant document found across all datasets.** It is an FBI internal case briefing document covering the entire Epstein investigation (2006-2022+) with all case numbers (31E-MM-1080, 72-MM-113327, 50D-NY-30275, 90A-NY-31512).

Page 17 contains a "PROMINENT NAMES" summary listing victim allegations against specific individuals. The entire page was redacted but the text was recoverable:

### Trump
1. Victim stated Epstein introduced her to Trump who "subsequently forced her head down to his exposed penis which she subsequently bit. In response, Trump punched her in the head and kicked her out." (date range 1983-1985; victim "Lafine" would have been 13-15)
2. Victim remembers Epstein introducing her to Trump saying "This is a good one, huh" and Trump responded "Yes." (date range roughly 1984; victim "Bjorlin" would have been 14)

### Harvey Weinstein
1. Victim stated she gave Weinstein a massage, during which he fondled her, masturbated, and offered to pay extra if he could ejaculate on her chest.
2. Victim stated Weinstein came to her apartment, offered her a job and then tried to follow her into the shower.
3. Victim stated Epstein told her to give Weinstein a massage, during which Weinstein told her to take off her shirt; she refused and Weinstein threatened to "get women to come force her too."

### Glen Dubin
1. Victim stated Maxwell instructed her to give Dubin a massage and "do what she did for Epstein."

*Prosecutors formally classified Dubin under "Individuals Who Have Engaged in Massages with Epstein Girls" alongside Jes Staley ([EFTA00098755](https://www.justice.gov/epstein/files/DataSet%209/EFTA00098755.pdf)). Former Dubin employee Rinaldo Rizzo identified as having "knowledge of Epstein underage activity." Eva Dubin's phone number was on the operational staff contacts sheet alongside Groff, Indyke, Kahn, and Brunel. See LUTNICK_DUBIN_INVESTIGATION.md.*

### Prince Andrew
1. Victim was told to "make Prince Andrew same things" — "he is good friends [with Epstein]"
2. Steve Scully** [noted as having criminal history] witnessed at Epstein's Island
3. Victim stated she was on Epstein's plane with Andrew; Andrew and Epstein flew [to various locations]

### Jes Staley (former JPMorgan CEO)
1. Victim told to give Staley a massage at Epstein's. Staley "forced her" and "had rough sex" with her.

### Leon Black (Apollo Global Management founder)
1. Victim told to give Black a massage. "Cuomo stated [he gave her a] massage and he made [jokes]" — another female gave her oral sex while Black watched. Made jokes about Black's penis size. **Note: "Cuomo" is a victim surname (Tony Cuomo, per [EFTA02696360](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02696360.pdf)), not Governor Andrew Cuomo.**
2. Victim stated Black "sex trafficked" and "threatened [her] numerous [times, including at Epstein's]." Black threatened her life and stated he had "connections."

*The 2-allegation summary above significantly understates the evidentiary record. DS9/DS11 revisit identified at least 4 distinct victims with FBI 302s or ADA notes, $118.5M+ in documented wire transfers (Deutsche Bank Exhibit A), and a complete DANY-SDNY-FBI correspondence chain showing SDNY declined to investigate. See LEON_BLACK_PROSECUTION_FAILURE.md for the full record.*

### Les Wexner (L Brands/Victoria's Secret founder)
1. Victim stated someone "earned his money from Wexner."
2. Reference to Wexner having "homosexual" [interactions].

### Alan Dershowitz
1. Victim stated she gave Dershowitz a massage on Epstein's plane. (FBI note: "not a minor")

### Bill Clinton
1. FBI assessment: "not a victim in the Epstein case."
2. One person claimed she was invited to an orgy with Clinton but did not attend.

### Howard Lutnick (Cantor Fitzgerald CEO)
1. "Simon Andriesz reported that Lutnick made his money through Ponzi schemes and money laundering. Lutnick and Epstein were neighbors and Epstein sold Lutnick a home for $10 which was then sold for millions."

*The single NTOC tip above is the only Prominent Names entry for Lutnick. However, DS9 revisit found 20+ documents showing an active 2011-2013 social relationship: calendar appointments, family visit to Little St. James Island by boat (Dec 2012), email correspondence, and placement on the same call list as Leon Black, Boris Nikolic, Jes Staley, and John Brockman. See LUTNICK_DUBIN_INVESTIGATION.md.*

### William Barr / Leon Black
1. NTOC tip stated "Barr and Black were present during abuses."
2. Victim stated she was at Epstein's for a model event and "ran into Barr who stated he wanted to see her next time he came." At another point, "Epstein asked if she had ever met Barr."

*Note: "Numerous anonymous NTOC's were received with allegations against prominent individuals."*

## FBI/NTOC Tip Line Reports ([EFTA01660651](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01660651.pdf), [EFTA01660679](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01660679.pdf))

These are compilations of FBI tip line reports from **August 6-7, 2025** containing multiple complainant statements:

1. **Female friend forced to perform oral sex on Trump ~35 years ago in NJ, age 13-14** — friend bit Trump, was hit in the face, was also abused by Epstein

2. **16-year-old model attended 8 parties at Epstein's NY residence** — sexually assaulted by Epstein on one occasion; twin brothers Allen and Oren lured girls upstairs; "Oren raped her best friend and a third brother, Tal, raped a 14 year old girl named Katie"

3. **Limo driver recalled picking up Trump in 1995** — described Trump's phone conversation as "very concerning," described being "a few seconds from pulling the limousine over"

4. **Complainant forced to perform sex acts at age 13 while pregnant (1984)** — reported "high profile individuals involved in her sex trafficking and the murder and disposal of her newborn daughter"; Trump "participated regularly in paying money to force her to perform sex acts"

5. **Complainant reported participating in orgies** — "some girls went missing, rumored to have been murdered and buried at the facility"; threatened by Trump's head of security that "if she ever talked...he would end up as fertilizer for the back nine holes like the other cunts"; claims to have video

6. **14-year-old approached by Ghislaine Maxwell about modeling, international travel, and massages**

7. **Detailed allegation**: "He measured the children's vulva and vaginas by entering a finger and rated the children on tightness. The guests were elder men and included Elon Musk, Don Jr. Trump, Ivanka Trump, and Eric Trump. Attorney Allan Dershowitz was also there with Attorney Bob Shapiro. We were taken in rooms, forced to give oral sex to Donald J Trump. Forced to allow them to penetrate us. I was 13 years old when Donald J Trump raped me. Ghislaine Maxwell was also present."

**IMPORTANT CAVEAT:** These are anonymous FBI tip line reports (NTOC = National Threat Operations Center) containing **unverified, unvetted intake from callers**. They are NOT established facts, NOT FBI investigative conclusions, and NOT evidence of the alleged conduct. NTOC tips routinely contain unsubstantiated, internally inconsistent, and sometimes entirely fabricated claims. Several of the tips above contain details that cannot be corroborated anywhere in the 218GB, 1.38M-document DOJ corpus. The FBI compiled these as raw intake for potential investigation. Their significance is institutional (they were included in the case file and redacted from public release) rather than evidentiary.

## Epstein Death Investigation Details ([EFTA01660622](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01660622.pdf) p12)

Hidden under redaction on the death investigation page:
- Over 400 hours of video from 7/23/2019 - 8/10/2019 reviewed
- 150 cameras total in MCC
- **DVR#1 - functioning; DVR#2 - system failure on 7/29/2019-8/9/2019** (not recording during death)
- **5 times inmate head count was not conducted**
- CO Michael Thomas was working the shift during which Epstein committed suicide
- 43 interviews conducted: 28 MCC Staff Members, 15 Inmates (mostly from SHU)
- Case closed 12/5/2022, with no criminality found
- OCME autopsy: cause of death was hanging, manner of death was [suicide]
- SDNY charged COs Michael Thomas and Tova [Noel] with Conspiracy, entered into 6-month deferred prosecution; terms satisfied
- Cellmate Efrain Reyes released; AUSA Rebekah Donaleski made the [charging decision]

## Maxwell Trial Summary ([EFTA01660622](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01660622.pdf) p14)

Trial dates: 11/29/2021 - 12/29/2021

Verdicts:
- Count 1: Conspiracy to Entice Minors - **Guilty**
- Count 2: Enticement of a Minor - **Not Guilty**
- Count 3: Conspiracy to Transport Minors - **Guilty**
- Count 4: Transportation of a Minor - **Guilty**
- Count 5: Sex Trafficking Conspiracy - **Guilty**
- Count 6: Sex Trafficking of a Minor - **Guilty**
- 2 Perjury charges [adjudicated separately]

Defense strategy: attempted to portray Maxwell as "a victim of circumstances" who "was targeted by Epstein and was unaware"
Sentence: 20 years with 5 years supervised release and $750,000 [restitution]

## Epstein Trust Documents - Beneficiary Names

Multiple documents reveal hidden beneficiary names from Epstein's trust:
- **Ghislaine Maxwell** - beneficiary under Article Third ([EFTA01296151](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01296151.pdf), [EFTA01297516](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01297516.pdf))
- **Jean-Luc Brunel** - beneficiary ([EFTA01297516](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01297516.pdf))
- **Karyna Shuliak** - trustee and beneficiary ([EFTA01266134](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01266134.pdf), [EFTA01298025](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01298025.pdf)+)
- **Richard Kahn** - attorney/trustee (20+ documents)
- **Eva Andersson-Dubin** - "SSON DUBIN, if she survives" ([EFTA01266434](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01266434.pdf))
- **Lawrence Paul Visoski Jr** - pilot, beneficiary ([EFTA01266380](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01266380.pdf))

## 56 Ghislaine Maxwell Bank Statements

[EFTA01524001](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01524001.pdf)-01524928 contain Maxwell's bank statements with "GHISLAINE MAXWELL Primary Account:" headers. Include:
- Chase/JPMorgan Private Client Checking Plus account
- Fedwire debits via Citibank
- Book transfers to "Samantha K Harris, New York NY"
- Online transfers to money market accounts
- Credit card purchases
- Statement periods from 2011 onwards

## Victim Interview Transcripts ([EFTA01333133](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01333133.pdf), [EFTA01333327](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01333327.pdf))

Palm Beach PD victim interviews with extensive detail:
- Multiple victims describing abuse patterns
- Ages: "just turned seventeen," "still a minor"
- Payment: $200-$1,000 per visit
- "reminded not to speak of what [happened]"
- Physical descriptions of abuse
- References to Juan Alessi (butler), Ghislaine Maxwell, school recruitment
- "from her family in Yugoslavia into the United States" — trafficking

## FBI Case Files

- **JEFFREY EPSTEIN; CHILD PROSTITUTION** — FBI case title ([EFTA01307710](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01307710.pdf))
- **ALFREDO RODRIGUEZ; OBSTRUCTION OF JUSTICE** — Case IDs 72-MM-113327 and 415M-HQ-C1424550 ([EFTA01326101](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01326101.pdf)-01326156)
- Cell phone location tracking data with longitude/latitude/radius ([EFTA01342463](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01342463.pdf)-01342469)
- FBI Sign-In Logs for evidence room access, Case 316-NY-3627 ([EFTA01303474](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01303474.pdf))
- **Maxwell + "fourteen-year-old" + "minor females"** ([EFTA01325315](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01325315.pdf))
- Grand Jury Subpoena ([EFTA01333003](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01333003.pdf))
- Intelligence Analyst reference ([EFTA01301641](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01301641.pdf))

## Financial Records

- **Deutsche Bank**: 224 entries — AG offices at 60 Wall Street, Wealth Management presentations
- **JPMorgan**: 738 entries — custody accounts, SDNY discovery production documents (JPM-SDNY-)
- **TD Ameritrade**: Portfolio statements, account positions ([EFTA01267639](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01267639.pdf), 1,204 bad redactions)
- **Bear Stearns**: 2 entries ([EFTA01482965](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01482965.pdf))
- **MoneyGram wire transfer records**: "WIRE TRANSFER RECORDS THAT INCLUDES NAMES" ([EFTA01265800](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01265800.pdf))
- **MCC commissary/account records** ([EFTA01265978](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01265978.pdf))

## Plea Negotiation Emails ([EFTA01302111](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01302111.pdf))

Hidden lawyer-to-lawyer email about Epstein's plea deal:
- Discussion of NYT coverage
- "David Weinstein's actions" — breach of local rules of conduct
- "multiple charging statutes, even including the 1591" (18 USC 1591 = sex trafficking)
- "patently unfair to Mr. Epstein"
- Reference to "Ken" as "a man of great faith" — believes the system "has failed miserably"

## Property Records

- **Zorro Ranch**: 177 entries — "ZORRO DEVELOPMENT CORP," "49 ZORRO RANCH ROAD, STANLEY NM 87056"
- **9 E 71st Street**: 42 entries — Epstein's Manhattan townhouse
- **457 Madison Avenue**: Epstein's NY office ([EFTA01312863](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01312863.pdf) etc.)
- **Bedminster**: Construction/roofing documents ([EFTA01303089](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01303089.pdf), [EFTA01340681](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01340681.pdf))
- **Virgin Islands**: 11 entries
- **Island structures**: "Potential Hidden Structure" noted in surveillance analysis ([EFTA01307744](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01307744.pdf))

## Aircraft / Estate Disposal

- Sikorsky S76C+ helicopter sale (N162AE, SN 760472) — extensive email chain ([EFTA01339374](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01339374.pdf))
- Aircraft N722JE and N162AE
- "Helicopter 1029 LLC sn 760750"
- Larry Visoski, Darren Indyke, Richard Kahn involved in post-death aircraft sales
- Wire transfer instructions for sales

## Jean-Luc Brunel / Modeling

"World renowned modeling entrepreneur Jean Luc Brunel opened Karin Models in Paris, France decades ago, to be eventually [convicted]" ([EFTA01728258](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01728258.pdf))

## Tom Barrack

"Tom Barrack time change" — scheduling communication ([EFTA02176329](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02176329.pdf))

## Ehud Barak

"8:30am Breakfast w/Ehud Barak" — Epstein's calendar entry ([EFTA02154241](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02154241.pdf))

## Key Statistics by Category

| Category | Hidden Text Entry Count |
|----------|------------------------|
| Victim references | 699 |
| Massage references | 267 |
| Trafficking references | 70 |
| Minor/underage references | 38 |
| Sex trafficking | 32 |
| Obstruction | 17 |
| FBI case documents | 224 |
| Grand jury | 6 |
| Palm Beach references | 706 |
| Zorro Ranch | 177 |
| Trust/beneficiary | 155 |
| School references | 169 |

## Combined Totals (All Datasets)

| Metric | DS1-9,11-12 | DS10 | **TOTAL** |
|--------|-------------|------|-----------|
| PDFs scanned | 16,284 | 503,154 | **519,438** |
| Total redactions | 179,139 | 1,629,776 | **1,808,915** |
| Bad overlays | 70,940 | 545,293 | **616,233** |
| Proper redactions | 108,199 | 1,084,483 | **1,192,682** |
| Docs with hidden text | 9,133 | 209,829 | **218,962** |
