# Crash Course in the Files

**A Complete Guide to the Epstein Document Production**
**For Journalists, Producers, and Investigators Starting From Zero**

*Last updated: March 12, 2026*

---

## How to Use This Document

Every factual claim in this document links to a source: either an EFTA-numbered document from the DOJ's production (linked via `epstein-data.com/EFTA{NUMBER}`, which renders the original PDF with full-text search; if the DOJ has removed the document, the OCR text copy is preserved) or an external news report with URL. The "What This Does NOT Show" sections at the end of each chapter are as important as the findings themselves.

---

# SECTION 0: COLD OPEN

## What 2.73 Million Pages Actually Show

On January 30, 2026, the Department of Justice released the largest single document production in American legal history. The [Epstein Files Transparency Act](https://www.congress.gov/bill/119th-congress/house-bill/4405) (Public Law 119-38) had ordered the Attorney General to publish all unclassified records related to Jeffrey Epstein within 30 days. What came out was 2.73 million pages across 12 datasets, encompassing FBI investigations, federal grand jury materials, banking records, prison files, victim interviews, and a decade of Epstein's personal email.

The files tell a story that no single news outlet has fully reported. Not because the documents are hard to find, but because there are too many of them for any newsroom to read. Here are five findings that illustrate the scale of what is in these pages:

**1. The money was ten times larger than reported.** Financial records extracted from Deutsche Bank and JPMorgan productions reveal at least 95 shell entities controlled by Epstein, with cumulative documented flows exceeding $755 million. The most-cited figure before the release was $85 million, which turned out to be a single point-in-time balance snapshot. ([EFTA00027019](https://epstein-data.com/EFTA00027019) — Deutsche Bank master transaction tables)

**2. The DOJ released the files, then quietly removed 64,000 of them.** Between the January 30 release and mid-February, approximately 64,259 documents were silently pulled from justice.gov. No Federal Register notice. No congressional notification. Among the removed files: the FBI's 476-page death investigation, the Bureau of Prisons logs from the unit where Epstein died, and the complete psychological reconstruction of his final weeks. The EFTA requires written justification for any withholding. None has been published. The removal pattern was first reported by [Roger Sollenberger](https://sollenbergerrc.substack.com/p/doj-removed-record-of-multiple-fbi) and independently verified by [NPR](https://www.npr.org/2026/02/24/nx-s1-5723968/epstein-files-trump-accusation-maxwell).

**3. 1.46 million additional pages were reviewed but never released.** Hidden secondary Bates stamps on the released pages reveal two parallel numbering systems (the FBI's "R1" device extraction sequence and SDNY's production sequence) that together show 2.48 million pages were reviewed and stamped. Only 1.04 million made it into the public production. The withholding rate for SDNY's investigative files was 74.9%. NPR's Stephen Fowler [confirmed the 53-page gap](https://www.npr.org/2026/02/24/nx-s1-5723968/epstein-files-trump-accusation-maxwell) that first demonstrated this pattern; the broader analysis covers the full 2.48 million page universe.

**4. The FBI ran a parallel intelligence investigation that has never been reported.** The corpus reveals at least nine FBI case numbers across four criminal investigations, multiple intelligence sub-files, and a standalone foreign intelligence case (813B-NY-2928278) opened in December 2017, eighteen months before the public SDNY criminal case. The intelligence track ran through at least seven field offices, produced 12 Tactical Intelligence Reports at SECRET//NOFORN classification, and included a 2020 election influence assessment. No outlet has mapped this architecture. ([EFTA01683874](https://epstein-data.com/EFTA01683874) — the 813B FD-1023)

**5. The DOJ altered 42,782 documents after publication.** A forensic comparison of archived originals against currently-hosted versions found 152,312 individual changes. Only 2.6% were defensible victim privacy redactions. The DOJ removed 16 times more non-PII content than victim-protective content, including: 150+ FinCEN Suspicious Activity Reports gutted of banking intelligence, the entire searchable text layer of Epstein's prison psychological file, and 1.4 million characters degraded from Ghislaine Maxwell's credit card statements, which had already been public trial exhibits. AG Bondi stated [no records were withheld for "embarrassment, reputational harm, or political sensitivity"](https://www.npr.org/2026/02/24/nx-s1-5723968/epstein-files-trump-accusation-maxwell); the alteration evidence complicates that claim.

These are not conspiracy theories. They are the documents themselves, released by the government, analyzed page by page. The rest of this briefing walks through what they contain.

---

# SECTION 1: THE DATASET

## What the DOJ Released and What It Didn't

### 1.1 The Epstein Files Transparency Act

The EFTA ([Public Law 119-38](https://www.congress.gov/bill/119th-congress/house-bill/4405), H.R. 4405) became law on November 19, 2025. It ordered the Attorney General to release, within 30 days, all unclassified DOJ records related to Jeffrey Epstein across nine specific categories:

1. All investigations, prosecutions, or custodial matters involving Epstein
2. All records relating to Ghislaine Maxwell
3. All flight logs, travel records, manifests, and customs documentation
4. All references to individuals named in connection with criminal activities, settlements, or investigations
5. All references to entities with ties to trafficking or financial networks
6. All immunity deals, plea bargains, and sealed settlements
7. All internal DOJ communications about decisions to charge, not charge, investigate, or decline
8. All records concerning destruction, deletion, alteration, or concealment of evidence
9. All documentation of Epstein's detention and death

The statute prohibits withholding based on "embarrassment, reputational harm, or political sensitivity, including to any government official, public figure, or foreign dignitary." Five narrow exceptions exist: victim PII, CSAM, active investigations (narrowly tailored and temporary), images of death or abuse, and classified national security material. Every redaction requires written justification in the Federal Register. As of this writing, no such justification has been published.

### 1.2 The 12 Datasets

The DOJ organized its production into 12 datasets, released on justice.gov as individual PDFs. Each document is assigned an EFTA number (e.g., EFTA00074206).

| Dataset | EFTA Range | Documents | Primary Contents |
|---------|-----------|-----------|-----------------|
| 1 | 00000001–00003158 | 3,158 | Initial document production |
| 2 | 00003159–00003857 | 574 | Supplemental documents |
| 3 | 00003858–00005586 | 67 | Legal filings and motions |
| 4 | 00005705–00008320 | 152 | Court records |
| 5 | 00008409–00008528 | 120 | Additional court records |
| 6 | 00008529–00008998 | 13 | Short supplemental filings |
| 7 | 00009016–00009664 | 17 | Additional legal records |
| **8** | **00009676–00039023** | **10,595** | **Deutsche Bank/JPMorgan records, court exhibits, NPA documents** |
| **9** | **00039025–01262781** | **531,284** | **FBI investigative files, Bureau of Prisons records, grand jury materials, victim interviews, 302s** |
| **10** | **01262782–02205654** | **503,154** | **FBI device extractions (email, iMessage), banking records (JPM-SDNY, DB-SDNY), financial forensics** |
| **11** | **02205655–02730264** | **331,655** | **FBI device extractions continued (97% email/iMessage from R1 review)** |
| 12 | 02730265–02858497 | 3,475 | DS12 originally contained 152 documents. Expanded silently on ~March 5, 2026 to include 23 additional documents (1,046 pages) containing Operation Leap Year prosecution memos, grand jury transcripts, and a 582-page FBI case file |

**The bulk of the production is in Datasets 9, 10, and 11**, which together contain 1.37 million documents and 2.5+ million pages. DS9 holds the investigative backbone: FBI 302 witness interviews, grand jury subpoenas, BOP custody records, and prosecution files. DS10 and DS11 hold Epstein's personal communications extracted from seized electronic devices.

EFTA numbers are assigned per page, not per document. A 10-page document starting at EFTA00000001 occupies numbers 00000001 through 00000010.

### 1.3 Three Numbering Systems

The production uses three independent Bates numbering systems, which can cause confusion:

| System | Format | Source | Where It Appears |
|--------|--------|--------|-----------------|
| **EFTA** | `EFTA00074206` (8 digits) | DOJ production | All 12 datasets. The primary citation system. |
| **DOJ-OGR** | `DOJ-OGR-00000001` | Concordance/OGR production | Cross-reference system used in production metadata. |
| **HOUSE_OVERSIGHT** | `HOUSE_OVERSIGHT_010477` | House Oversight Committee | A separate production from congressional records, not hosted on justice.gov. |

### 1.4 What's Missing

Four categories of missing material have been identified:

**Removed documents (~64,259).** Documents that were published on January 30 and subsequently pulled from justice.gov. Concentrated overwhelmingly in Dataset 9, the FBI investigative files. First reported by [Sollenberger](https://sollenbergerrc.substack.com/p/doj-removed-record-of-multiple-fbi) and confirmed by [NPR](https://www.npr.org/2026/02/24/nx-s1-5723968/epstein-files-trump-accusation-maxwell). An authenticated scan of all 1.38 million document URLs, followed by statistical sampling (n=500, 94.8% true positive rate), produced the full-corpus estimate.

**Withheld pages (~1.46 million).** Secondary Bates stamps on the released documents reveal that 2.48 million pages were reviewed and numbered during production. Only 1.04 million made it into the public release. The FBI's "R1" device extraction stream withheld 57% of reviewed pages. SDNY's investigative file stream withheld 74.9%. The gap analysis is based on sequential numbering: missing numbers in the sequence represent pages that were reviewed, stamped, and then excluded. NPR used this same methodology to identify the [53-page PROTECT SOURCE gap](https://www.npr.org/2026/02/24/nx-s1-5723968/epstein-files-trump-accusation-maxwell).

**Altered documents (42,782).** Documents that remain on justice.gov but have been modified since the original publication. Changes range from defensible victim PII redaction (2.6% of changes) to wholesale content removal (46.9%), text-layer degradation (27,026 pages rendered unsearchable), and FinCEN SAR gutting.

**Never-collected evidence.** Material that the FBI had legal authority or opportunity to collect but did not:
- A 2005 computer forensic image from Palm Beach (16 DVDs, never searched — no legal authority obtained after the NPA)
- Zorro Ranch in New Mexico (never searched; SDNY ordered NM to halt its investigation in July 2019; ranch not searched until March 2026)
- 86 audio recordings listed in FBI indices but not present in the production
- 7 discs of "consensually monitored phone calls" referenced in evidence logs ([EFTA02730741](https://epstein-data.com/EFTA02730741))

### 1.5 The DS12 Expansion

On approximately March 5, 2026, the DOJ quietly added 23 new documents (1,046 pages) to Dataset 12 without public announcement. The EFTA range for DS12 expanded from EFTA02730265-02731783 to EFTA02730265-02858497. The new documents include:

- **Operation Leap Year prosecution memos** — 60-count indictment drafts from the original Palm Beach investigation that was derailed by the 2007 Non-Prosecution Agreement ([EFTA02857524](https://epstein-data.com/EFTA02857524), [EFTA02857810](https://epstein-data.com/EFTA02857810))
- **Grand jury transcripts** — testimony from the 2006-2007 MCC grand jury proceedings
- **A 582-page FBI case file** (31E-MM-108062) — the complete serial index for the original Miami investigation ([EFTA02857863](https://epstein-data.com/EFTA02857863))
- **PROTECT SOURCE interviews** — four FBI FD-302s with a woman who accused both Epstein and Donald Trump of sexual assault when she was between 13 and 15 years old. The FBI designated her PROTECT SOURCE, indicating assessed risk to her safety. Three of the four interviews were new in the expansion; Interview #1 had been in DS9. ([EFTA02858481](https://epstein-data.com/EFTA02858481), [EFTA02858491](https://epstein-data.com/EFTA02858491))

The timing of the expansion is notable: [NPR reported](https://www.npr.org/2026/03/05/nx-s1-5737562/justice-department-missing-epstein-files-trump) on the release the same day. The House Oversight Committee had [voted to subpoena AG Bondi](https://www.pbs.org/newshour/politics/house-committee-votes-to-subpoena-bondi-to-answer-questions-over-epstein-files) the day before.

Further reading: [DS12 Expansion Analysis](https://epstein-data.com/reports/institutional/DS12_EXPANSION_ANALYSIS.html)

---

# SECTION 2: THE YEAR IN EPSTEIN NEWS

## Top Stories: January 2025 Through March 2026

*Chronological. Each entry: what was reported, where, and what the EFTA corpus adds.*

### 2025: The Road to Disclosure

**April 25, 2025: Virginia Giuffre Dies**
The most prominent Epstein survivor dies at age 41 at her home in Western Australia. Giuffre had been the named plaintiff in the civil case that forced the unsealing of Maxwell deposition materials and the public face of the survivor advocacy movement. Her death is confirmed as suicide. ([NPR](https://www.npr.org/2025/04/26/g-s1-62856/virginia-giuffre-has-died))

*Segment potential: HIGH. Giuffre's story is the narrative spine of the entire public Epstein case. Her death before the files were released is itself significant.*

**July 15, 2025: Epstein Files Transparency Act Introduced**
Representatives Ro Khanna and Thomas Massie introduce H.R. 4405 with bipartisan co-sponsors. The bill requires DOJ disclosure of all Epstein investigative records within 30 days of enactment. ([Congress.gov](https://www.congress.gov/bill/119th-congress/house-bill/4405))

**July 17, 2025: Trump Letter in Epstein's Birthday Album**
The Wall Street Journal reports on a sexually suggestive letter bearing Trump's name found in Epstein's 50th birthday album (2003). Trump denies authorship and sues the newspaper. The corpus contains the album as a scanned document.

**July 24-25, 2025: DAG Blanche Interviews Maxwell**
Deputy Attorney General Todd Blanche interviews Maxwell at FCI Tallahassee. Maxwell denies wrongdoing and says she never saw Trump in "inappropriate situations." She is subsequently transferred to a minimum-security camp in Texas.

**August-September 2025: House Oversight Subpoenas**
Chairman Comer issues subpoenas for Epstein estate records. The committee releases 33,295 pages on September 2. Separately, Bloomberg obtains 18,000 Epstein emails from his Yahoo account spanning 2005-2008, revealing how elite contacts rallied to his defense as investigators closed in. ([Bloomberg, Sep 25](https://www.bloomberg.com/features/2025-jeffrey-epstein-emails-the-network/))

**September 26, 2025: House Democrats Release Meeting Records**
Six pages showing Epstein had meetings with Peter Thiel, Elon Musk, and Steve Bannon.

**October 6, 2025: Supreme Court Declines Maxwell Appeal**
Maxwell's certiorari petition denied. All direct appellate options exhausted. ([SCOTUSblog](https://www.scotusblog.com/2025/10/supreme-court-declines-to-hear-ghislaine-maxwells-appeal/))

**October 2025: Prince Andrew Stripped of All Titles**
The Duke of York title, prince title, and all remaining honors removed. ([PBS](https://www.pbs.org/newshour/world/andrew-windsor-officially-no-longer-a-prince-after-king-formally-strips-title-for-epstein-ties))

**October 16, 2025: Banks Sued by Epstein Victims**
Bank of America and BNY Mellon sued for allegedly facilitating Epstein's trafficking through financial services. Leon Black's $170M in transfers flagged. ([CNBC](https://www.cnbc.com/2025/10/16/bank-of-america-bny-sued-over-alleged-financial-ties-to-jeffrey-epstein.html))

**November 19, 2025: EFTA Signed Into Law**
Passes both chambers unanimously. Trump signs immediately. 30-day clock starts. ([Pub. L. 119-38](https://www.congress.gov/bill/119th-congress/house-bill/4405))

**December 19, 2025: First DOJ Release — Bipartisan Fury**
Small initial batch draws immediate criticism. Extensive redactions. The Wall Street Journal finds 43 of 47 victim names left unredacted. A copy-paste bypass is discovered allowing the public to read blacked-out text. Documents disappear from DOJ site hours after posting. ([NPR](https://www.npr.org/2025/12/20/nx-s1-5650758/epstein-files-doj-trump-photo), [Bloomberg](https://www.bloomberg.com/news/articles/2025-12-19/epstein-files-released-after-years-of-political-legal-acrimony))

### January-February 2026: The Flood

**January 30, 2026: The Full Release — 3.5 Million Pages**
The DOJ publishes what it calls the "final" release: approximately 3.5 million pages including 2,000+ videos and 180,000 images across 12 datasets. Every major outlet covers the event. The sheer volume (over 1.3 million individual PDF files) makes comprehensive analysis impossible in a news cycle. ([CNN](https://www.cnn.com/politics/live-news/epstein-files-release-doj-01-30-26), [DOJ](https://www.justice.gov/opa/pr/department-justice-publishes-35-million-responsive-pages-compliance-epstein-files))

**January 21 - February 3, 2026: Clinton Contempt and Depositions**
Both Clintons defy House subpoenas (Bill no-show Jan 13, Hillary no-show Jan 14). Bipartisan contempt vote January 21 (9 Democrats voting yes). The Clintons capitulate February 3. Hillary deposed February 26; Bill deposed February 27 — under oath before the House Oversight Committee. ([NPR](https://www.npr.org/2026/02/03/nx-s1-5697831/clintons-agree-testify-house-epstein-investigation-contempt-congress-vote))

*Segment potential: HIGH. Congressional contempt of a former president is rare. The depositions themselves are the story.*

**January 29, 2026: BofA Case Survives Dismissal**
Judge Rakoff allows two claims against Bank of America to proceed (knowing beneficiary + obstruction). Dismisses BNY entirely. Trial set for May 11, 2026. Leon Black's deposition ordered.

**February 9-10, 2026: Maxwell Declines, Seeks Clemency**
Maxwell invokes the Fifth Amendment before House Oversight. Offers to testify that Trump and Clinton "did nothing wrong" in exchange for clemency. White House says pardon "not on his radar." In her pro se habeas petition, Maxwell names 4 unindicted co-conspirators and alleges the DOJ reached "secret settlements" with 25 men. ([NPR](https://www.npr.org/2026/02/10/g-s1-109413/maxwell-appeals-for-clemency))

**February 10, 2026: Khanna Reads Six Redacted Names on House Floor**
After viewing unredacted files with Rep. Massie, Rep. Khanna names: Sultan Ahmed bin Sulayem, Leslie Wexner, Salvatore Nuara, Zurab Mikeladze, Leonic Leonov, Nicola Caputo. The DOJ responds that some of the named individuals had "no Epstein ties." ([New Republic](https://newrepublic.com/post/206411/ro-khanna-reads-redacted-names-epstein-files-house-floor))

**February 10-11, 2026: Lutnick Admits Island Visit**
Commerce Secretary Howard Lutnick admits visiting Epstein's island in 2012 with family and nannies, contradicting earlier claims of cutting contact years before. Volunteers to testify before House Oversight. ([NPR](https://www.npr.org/2026/02/11/nx-s1-5708943/commerce-secretary-howard-lutnick-testifies-about-visiting-jeffrey-epsteins-island))

**February 13, 2026: Bloomberg — "The Leon Black Files"**
Bloomberg publishes the definitive deep dive on the Black-Epstein relationship, documenting Epstein as a "fixer" for Black's personal secrets and the $158M+ financial relationship. The corpus adds the "HT Subject Referral" and the DA's "do not doubt" statement ([EFTA02731737](https://epstein-data.com/EFTA02731737)). ([Bloomberg](https://www.bloomberg.com/news/features/2026-02-13/the-leon-black-files-epstein-was-a-fixer-for-billionaire-s-deepest-secrets))

*Segment potential: HIGH. The gap between "do not doubt" and "no charges" is the central tension.*

**February 15-24, 2026: Sollenberger Breaks the Document Removal Story**
Roger Sollenberger (The Daily Beast / independent Substack) discovers the FBI interviewed an underage Trump accuser at least 4 times, and that the DOJ removed the records from the public database. A 53-page gap is confirmed via serial number analysis. NPR independently verifies the findings. The story triggers a bipartisan congressional investigation within 24 hours. ([Sollenberger Substack](https://sollenbergerrc.substack.com/p/fbi-interviewed-trump-accuser-epstein), [NPR](https://www.npr.org/2026/02/24/nx-s1-5723968/epstein-files-trump-accusation-maxwell))

*What the corpus adds: The serial number methodology Sollenberger used parallels the broader secondary Bates stamp analysis. The 53 missing pages are a subset of the 1.46 million withheld pages identified through R1 and EFTA_ gap analysis.*

**February 18, 2026: Wexner Deposed**
Les Wexner sits for a five-hour deposition at his New Albany, Ohio mansion before the House Oversight Committee. Calls Epstein a "con man." Denies friendship. Democrats accuse him of facilitating trafficking. Video released by the committee. ([CNBC](https://www.cnbc.com/2026/02/18/jeffrey-epstein-les-wexner-deposition.html))

**February 19, 2026: Prince Andrew Arrested**
Arrested on his 66th birthday on suspicion of misconduct in public office: sharing confidential trade envoy reports (Hong Kong, Vietnam, Singapore) with Epstein. Released under investigation. First senior British royal arrested in approximately 400 years. Maximum sentence if convicted: life imprisonment. ([NBC](https://www.nbcnews.com/world/united-kingdom/former-prince-andrew-arrested-epstein-files-revelations-rcna259691))

*Segment potential: HIGHEST. A royal arrest based on documents in the EFTA corpus.*

**February 19-20, 2026: NYT — CBP Corruption**
The New York Times names David Routch and additional CBP officers (Heil, Samuel, Richards, Montgomery, Martinez) who facilitated Epstein's customs bypass in the USVI. The corpus contains the full FBI referral chain.

**February 23, 2026: Peter Mandelson Arrested**
Former UK Ambassador to the U.S. arrested for misconduct in public office. Accused of passing market-sensitive government information to Epstein during his tenure as UK Business Secretary (2008-2010). Released on bail. ([CNN](https://www.cnn.com/2026/02/23/uk/peter-mandelson-arrested-gbr-intl))

**February 26-27, 2026: Clinton Depositions**
Hillary Clinton deposed February 26; Bill Clinton deposed February 27. Both under oath before the House Oversight Committee. Content of depositions not yet fully public.

### March 2026: The Second Wave

**March 4-11, 2026: Congressional Escalation**
Bipartisan Senate group (Durbin, Murkowski, Lujan, Merkley) requests GAO review of DOJ EFTA compliance. House Oversight subpoenas AG Bondi. Richard Kahn deposed for 7 hours (March 11), denies knowledge of crimes. Leon Black ordered deposed in BofA civil suit (scheduled March 26). UN human rights experts demand accountability. ([Washington Post](https://www.washingtonpost.com/politics/2026/03/11/senators-investigation-epstein-files/), [CBS](https://www.cbsnews.com/news/richard-kahn-jeffrey-epstein-house-oversight-testimony/))

**~March 5, 2026: Silent DS12 Expansion**
Without public announcement, the DOJ adds 23 new documents to Dataset 12, including Operation Leap Year prosecution memos and grand jury transcripts. The 582-page FBI case file provides the first complete serial index for the original Miami investigation.

**March 10, 2026: Zorro Ranch Finally Searched**
NM Attorney General Raúl Torrez executes a search warrant at Zorro Ranch. First search of the property, nearly seven years after Epstein's death and despite the corpus documenting that SDNY ordered NM to halt its investigation in July 2019. ([EFTA00019183](https://epstein-data.com/EFTA00019183))

### Coming: Key Upcoming Dates

| Date | Event |
|------|-------|
| **March 19, 2026** | Darren Indyke House Oversight deposition (scheduled) |
| **March 26, 2026** | Leon Black deposition in BofA civil suit (Judge Rakoff) |
| **May 11, 2026** | Bank of America trial begins (SDNY, Judge Rakoff) |
| **May 13, 2026** | Leon Black voluntary House Oversight appearance |
| **June 3, 2026** | Sarah Kellen House Oversight testimony (requested) |

### The Reporting Landscape

The Epstein files story has been covered unevenly. Most outlets focused on celebrity names in the first weeks. The structural findings (financial architecture, document removals, the intelligence track) have received less attention. Here is the landscape as of March 2026:

**Roger Sollenberger** (The Daily Beast / [Substack](https://sollenbergerrc.substack.com/)) — Senior political reporter. Broke the serial-number-based document removal story. Eight Epstein-focused Substack pieces since Feb 15, 2026, plus Daily Beast reporting. Key focus: DOJ removal of Trump-related documents, FBI interviews with underage accuser, serial number gap analysis. His methodology was independently verified by NPR. Contact: roger.sollenberger@protonmail.com

**Stephen Fowler / NPR** — Institutional story: DOJ removal pattern, DS12 expansion, congressional investigation. Verified Sollenberger's 53-page finding independently. Feb-Mar 2026 reporting.

**Ellie Leonard** ([Substack: The Panicked Writer](https://ellieleonard.substack.com/)) — Independent citizen journalist. New Jersey mother of four who read every published Epstein email in the corpus. Profiled by the AP/Washington Times (Feb 23, 2026) as a leading citizen journalist on the files. 35+ Epstein-focused articles and live episodes since September 2025, including the "Epstein Files Breakdown" volume-by-volume series, "Decoding an Unknown Survivor's Journal" (3 parts), the complete "Epstein Birthday Book" transcription, and the Bannon email deep dives. Regular collaborators: Wajahat Ali (The Left Hook), Jim Acosta, Glenn Kirschner, Gen. Mark Hertling, Narativ. ([AP/WashTimes profile](https://www.washingtontimes.com/news/2026/feb/23/epstein-files-tackled-citizen-sleuths-citizen-journalists-help/))

**Bloomberg** — The Leon Black deep dive ("The Leon Black Files," Feb 13, 2026) and the pre-release 18,000-email investigation (Sep 2025). Also covering the BofA trial.

**New York Times** — CBP corruption series (Routch and additional officers, Feb 19-20). Institutional failure angle.

**CNN** — Bannon-Epstein relationship, Italian connections, arrest coverage (Andrew, Mandelson).

**Reuters** — Deutsche Bank team identification (Stewart Oldfield, Feb 2026).

**International press:**
- *Italian*: Fanpage, Open.online, Il Foglio (Teodorani-Fabbri, Elkann, Berlusconi)
- *French*: Mediapart, France 24, Art Newspaper (Prytanee/Binant/Jack Lang — active criminal investigation)
- *UK*: Guardian, Telegraph, BBC (Prince Andrew arrest, Mandelson arrest)
- *Al Jazeera*: Comprehensive arrest and resignation tracking

**What nobody has covered yet** (as of March 12, 2026):
1. The parallel FBI intelligence architecture (9+ case numbers, SECRET//NOFORN)
2. The full shell entity financial map ($755M through 95+ entities)
3. HBRK Associates ($84.5M managed, 35,919 documents)
4. helpfulexperts.com (first SDNY grand jury subpoena, July 2017)
5. The 853 deleted phone record pages
6. The 47 missing victim FD-302 interviews (29.4% of known interviews)
7. Dr. Steven Victor / "Dr. Evil" identification and the free treatment pipeline
8. The "MacGyver" correction (multiple outlets identified as Trump; corpus points to Brafman)
9. The full alteration scale (42,782 documents, only 2.6% for victim privacy)
10. The deference dynamic: SDNY controlling all parallel investigations from 2019 forward

---

# SECTION 3: THE MONEY

## Follow the Money: $755 Million Through 95 Shell Entities

### 3.1 Deutsche Bank: RM CODE 82289

Deutsche Bank was Epstein's primary banking relationship from 2013 through his 2019 death, succeeding JPMorgan Chase (which dropped Epstein in 2013 after internal compliance pressure). The bank [paid $150 million in 2020](https://www.cnbc.com/2020/07/07/jeffrey-epstein-case-deutsche-bank-fined-150-million-penalty-for-relationship.html) to settle New York State charges of compliance failures related to Epstein accounts.

The EFTA corpus reveals the internal mechanics:

**The team.** At least 13 named Deutsche Bank employees handled Epstein's accounts, organized under Relationship Manager Code 82289. Key figures include Natalie Barak (primary relationship manager), Stewart Oldfield, Bradley Gillin, and Tazia Smith. The full team is documented in internal correspondence. ([EFTA00027019](https://epstein-data.com/EFTA00027019) — master transaction tables)

**"KYC is not happening."** Know Your Customer due diligence, the regulatory requirement that banks verify the source of their clients' wealth, was repeatedly flagged as incomplete or bypassed. Internal emails show compliance officers raising concerns that were not acted upon. Deutsche Bank opened currency option positions worth €30 million while KYC remained incomplete.

**The Wanek connection.** Under RM82289, the corpus identifies 14 separate Wanek family trusts, GRATs, and LLCs with combined balances at Deutsche Bank. The Wanek family (founders of Ashley Furniture) represent the largest identified non-Epstein client cluster under the same relationship manager code.

### 3.2 The Shell Entity Map

At least 95 shell entities controlled by or associated with Epstein have been identified in the corpus. The major ones, with documented balances from Deutsche Bank transaction tables:

| Entity | Documented Balance | Purpose |
|--------|-------------------|---------|
| Southern Trust Company | $45,151,615 | Primary custodial vehicle |
| Gratitude America, Ltd. | $2,025,366 | Charitable entity |
| The Haze Trust | $2,503,668 | Art purchases, financial flows |
| Southern Financial LLC | $1,187,707 | Pass-through entity (Tudor $13.5M, Valar/Thiel $28.8M) |
| Butterfly Trust | $734,175 | Deutsche Bank linked |
| Hyperion Air, LLC | $789,558 | Aviation operations |
| Plan D, LLC | $347,675 | Unknown purpose |
| Neptune, LLC | $366,478 | Unknown purpose |
| JEGE, LLC | $299,328 | JE initials entity |
| HBRK Associates | $84,500,000+ | Post-prison operational hub (managed accounts) |
| Zorro Management, LLC | $464,683 | New Mexico operations |
| Jeepers, Inc. | — | Linked to Glen Dubin |

Source: [EFTA00027019](https://epstein-data.com/EFTA00027019) (Exhibits A-E) for Deutsche Bank figures. HBRK figure from forensic analysis of managed account statements across DS10/DS11.

### 3.3 Leon Black: $158 Million+

Leon Black, co-founder of Apollo Global Management, [paid Epstein at least $158 million](https://www.bloomberg.com/news/articles/2021-01-26/what-leon-black-got-for-paying-jeffrey-epstein-158-million) between 2012 and 2017, according to financial records and the Dechert LLP investigation commissioned by Apollo's board. Black has the highest connection weight (816) of any individual in the knowledge graph, more than double the next person.

The corpus adds:
- An "HT Subject Referral" (Human Trafficking) in federal records ([EFTA02731473](https://epstein-data.com/EFTA02731473)–02731783, ~50 documents)
- The Manhattan DA stating: "DANY do not doubt her allegations against JE and LB" while also noting "They have not found any independent corroboration" ([EFTA02731737](https://epstein-data.com/EFTA02731737))
- A victim's recovered text message: "Leon. You sexually harassed me, sex trafficked me, raped me, and eventually blacklisted me."
- Epstein's codename for Black: "Mr. Big" — confirmed by Bloomberg, CBS, and The Daily Beast
- The complete Dechert LLP investigation file that formed the basis of Apollo's board review

**What this does NOT show:** The corpus does not contain direct documentary evidence of Black committing sexual abuse. The victim text message and DA statement are the strongest evidence. The DA simultaneously noted a lack of independent corroboration. No charges were filed.

### 3.4 The Art Pipeline

Epstein used art purchases as a financial pipeline. Documented transactions through Sotheby's and Christie's totaled at least $30.5 million, flowing into The Haze Trust ($2.5M documented balance). The pipeline worked through a layered structure:

1. Art purchased at auction under shell entity names
2. Proceeds and art routed through The Haze Trust
3. Art stored at UOVO climate-controlled facilities (also connected to the storage unit investigation)

Art broker and consultant relationships are documented in DS10/DS11 correspondence. Some art purchases appear to be financial transactions disguised as acquisitions, with pricing inconsistencies between purchase and insurance valuations. The transaction chain runs: cash → auction house → shell entity → trust → storage. Each step adds a layer of opacity.

### 3.5 The Post-Death Estate

Epstein's estate was valued at approximately $600 million at the time of his death. Analysis of the known asset inventory against the estate accounting reveals an approximately $228 million gap between documented assets and accounted funds.

**Known major assets:**
- East 71st Street mansion, NYC (valued at ~$56M)
- The Herbert Straus mansion, East 71st Street (reportedly purchased for $51M)
- Little St. James Island, USVI
- Great St. James Island, USVI
- Zorro Ranch, Stanley, NM
- Boeing 727 (N908JE, offered for sale at $1.5M in 2016)
- Gulfstream IV and other aircraft
- Art collection (value unknown)
- Financial accounts across 95+ entities

The $228M gap between documented assets and the estate valuation has not been publicly explained. The Victims' Compensation Program [distributed approximately $121 million to about 150 claimants](https://abcnews.go.com/US/jeffrey-epstein-victims-program-shutting-121-million-paid/story?id=79344412) before shutting down in August 2021.

### 3.6 The Key Operators

Three individuals managed the operational mechanics of Epstein's financial empire:

**Richard Kahn** — Trustee and self-described "Project Manager." Managed HBRK Associates, which controlled $84.5 million in managed accounts and generated 35,919 documents in the corpus. Kahn's trajectory through the Epstein organization is documented from his early role as Epstein's CPA through his elevation to co-executor of the estate. His trust agreement (Section 2.5) contained a lock-in clause making termination extraordinarily difficult. Kahn is currently under House Oversight subpoena (issued Feb 25, 2026). (Further reading: [witness brief](https://epstein-data.com/reports/congressional/WITNESS_BRIEF_KAHN.html))

**Darren Indyke** — Co-executor of the estate and Epstein's longtime personal attorney. Operated through Darren K. Indyke PLLC ($259,740 documented balance). Filed the DHS/FOIA complaint that attempted to block document releases. 70+ EFTA citations across the corpus. (Further reading: [witness brief](https://epstein-data.com/reports/congressional/WITNESS_BRIEF_INDYKE.html))

**Jean-Michel Barrett** — Accountant who prepared financial reports on the shell entity network.

### 3.7 The German Network

The Deutsche Bank relationship was not simply a banking account. It was a 13-person team managing a complex financial architecture:

**Key personnel documented in the corpus:**
- **Natalie Barak** — Primary relationship manager
- **Stewart Oldfield** — Account officer (named by Reuters, Feb 2026)
- **Bradley Gillin** — Account officer
- **Tazia Smith** — Account officer (named only in Handelsblatt)
- Plus 9 additional named employees

**Sal. Oppenheim Bank Rescue Play.** Jes Staley leaked JPMorgan intelligence to Epstein about the Sal. Oppenheim bank rescue, which Epstein attempted to exploit. This documents a sitting JPMorgan executive providing inside information to a convicted sex offender for financial gain.

**€30 Million Currency Options.** Deutsche Bank opened currency option positions worth €30 million while KYC (Know Your Customer) compliance remained incomplete. Internal emails document compliance officers raising concerns that were not acted upon.

**€150 Million Scholz Steel Financing.** Epstein pitched a €150 million financing deal for Scholz AG (German steel recycling), documented in correspondence. This places Epstein as an active deal-broker in German industrial finance well after his Florida conviction.

**Nobel Laureate Connection.** Bert Sakmann, Nobel Prize in Medicine (1991), was invited to lunch with Epstein through the Deutsche Bank network. The science-finance overlap documented in the German correspondence parallels the broader pattern of Epstein using financial relationships to access academic and scientific networks.

### 3.8 The Phone Records Window

A production inconsistency between Datasets 9 and 10 left **46 AT&T cell phone bills completely unredacted** in DS9, while the same records in DS10 were redacted. This gap exposes 25 months of Epstein's itemized call records (May 2004 through July 2006), covering the entire Palm Beach investigation, FBI involvement, and NPA negotiation period.

From the unredacted bills: **1,179 unique phone numbers** and **8,173 total call records** were extracted. Approximately 20 numbers were identified by cross-referencing the corpus alone (no external lookup services used).

A separate 2,153-page document ([EFTA01242527](https://epstein-data.com/EFTA01242527)) contains Epstein's office landline records (212-750-1176) with zero redactions. This includes calls to the Trump Organization (5 calls) and the Clinton Foundation (10 calls) across three Epstein phone lines.

The FBI explicitly deleted **853 pages** of phone records under FOIA exemptions b6, b7C, and b7D, documented in "Deleted Page Information Sheets" within the production.

### 3.9 What the Money Does NOT Show

The financial records in the corpus are extensive but incomplete. Several important limitations:

- No single document contains a complete accounting of all Epstein's assets or income sources
- The "source of wealth" question (how Epstein originally accumulated his fortune) is not answered by the production. Deutsche Bank's own KYC files acknowledge this gap
- The $755 million figure is cumulative documented flows, not a net worth estimate
- Many shell entities have minimal documentation; their true purpose and scale may be larger than what the banking records reveal
- JPMorgan's internal records (the JPM-SDNY stamp series) are present but mostly consist of account statements, not internal deliberations about why the bank maintained the relationship

Further reading: [Shell Entity Map](https://epstein-data.com/reports/financial/SHELL_ENTITY_MAP.html), [Phone Records Investigation](https://epstein-data.com/reports/evidence/PHONE_RECORDS_INVESTIGATION.html)

---

# SECTION 4: THE VICTIMS

## 60 to 200+: What the Files Show About Scale

*This section discusses the system of exploitation documented in the files. No victim names, pseudonym-to-name mappings, or identifying details are included. The goal is to expose the system and the perpetrators, never to retraumatize or identify victims.*

### 4.1 The Numbers

The number of Epstein's victims has been stated differently by different authorities at different times:

- **28 victims** identified in the original 2005-2007 Palm Beach investigation
- **36+ victims** named in the 2019 SDNY indictment
- **60-80 victims** identified across the full EFTA production through FBI interview records and victim indices
- **"Hundreds"** alleged in the USVI Attorney General's civil complaint
- **23 victims** documented in the FBI's internal victim tracking matrix ([EFTA00184128](https://epstein-data.com/EFTA00184128) — 40-page FBI matrix with Jane Doe designations)
- **19 Jane Does** listed in the Operation Leap Year prosecution memos from DS12

The numbers vary because they reflect different counting methods, jurisdictions, and evidentiary standards. The FBI matrix tracks victims with sufficient evidence for prosecution; the broader figure includes reports, tips, and civil complaints.

### 4.2 The Recruitment System

The documents reveal a structured recruitment operation, not opportunistic abuse:

**The masseuse pipeline.** Victims were recruited through the pretense of providing massage services. Epstein's staff (principally Sarah Kellen, Nadia Marcinkova, and Lesley Groff) maintained scheduling lists and contact information. The scheduling emails in DS10/DS11 show a systematic operation with daily appointments.

**Peer recruitment.** Multiple victims described being recruited by other victims — a pyramid structure in which existing victims brought friends and classmates in exchange for payment. This is documented in FBI 302 interviews across DS9.

**MC2 Model Management.** Jean-Luc Brunel's modeling agency served as a recruitment pipeline. Maxwell and Brunel are documented working together to source young women through the modeling industry. Brunel was found dead in his Paris jail cell in February 2022 while awaiting trial.

**Geographic nodes.** The recruitment operation centered on four primary locations, each with distinct victim pools and methods:

- **Palm Beach, Florida** — The original investigation site. Victims recruited from local high schools (Royal Palm Beach High School, Jupiter Farms, Wellington). The recruitment was concentrated in working-class neighborhoods. FBI 302s document a peer-to-peer referral network where victims brought classmates to 358 El Brillo Way for "massage" appointments at $200-300 per visit. The Palm Beach operation is the most thoroughly documented in the corpus because it was investigated first.

- **New York City** — The East 71st Street mansion (9 East 71st, transferred from Wexner). Scheduling emails show daily appointment blocks. The NYC operation overlapped with the MC2 modeling pipeline and featured a grooming infrastructure that included cosmetic treatments (Dr. Victor), salon visits (Fekkai), and apartment housing (301 East 66th Street, the same building as MC2's offices).

- **New Mexico** — Zorro Ranch, 49 Zorro Ranch Road, Stanley. The FBI documented victim testimony placing abuse at the ranch. SDNY ordered the NM AG to halt its investigation in July 2019. The ranch was not searched until March 2026.

- **U.S. Virgin Islands** — Little St. James Island and Great St. James Island. The USVI operation benefited from CBP officer complicity (the Routch pipeline documented by NYT). The USVI AG's civil complaint alleged "hundreds" of victims.

**International extensions** documented in travel records, scheduling emails, and phone records: Paris (MC2 operations, Brunel pipeline), London (Prince Andrew correspondence, Dr. Victor travels), and various locations through commercial airline and private jet records.

### 4.3 The Missing Interviews

Of 160 FBI FD-302 interview records identified through the corpus's serial numbering system (the 3501.xxx series), **47 are absent from the production**, a 29.4% missing rate. Additionally:

- 86 audio recordings listed in FBI indices have zero corresponding documents in the production
- 149 serial numbers in the FBI's case file index have zero published documents
- The FBI's own Sentinel Serial Report lists 33 entries categorized as "CHILD VICTIM INFO" — exceeding the 26 victims referenced in prosecution memos

### 4.4 The Jane Doe System

A critical finding for anyone reporting on specific victims: the Jane Doe numbering system is unstable across proceedings. At least three different numbering schemes (the FBI victim matrix, the prosecution worksheets, and civil litigation) assign different JD numbers to the same individuals. A victim called "JD#9" in one document may be "JD#10" in another, or may not have a JD number at all.

For this reason, the serial number (e.g., 3501.045) and victim characteristics (school, DOB, geographic location) are more reliable identifiers than JD numbers.

### 4.5 What the Files Do NOT Show

The victim section requires particular care about what is and is not in the documents:

**Regarding Donald Trump:** The DS12 expansion (March 2026) contains four FBI FD-302 interviews with a woman designated PROTECT SOURCE who alleges Trump sexually assaulted her when she was between 13 and 15. In Interview #2 ([EFTA02858481](https://epstein-data.com/EFTA02858481)), she describes Trump forcing oral sex and striking her. In Interview #3 ([EFTA02858491](https://epstein-data.com/EFTA02858491)), she clarifies that he "pulled her hair and punched her on the side of her head." These are FBI-recorded witness statements (Tier 1 source reliability), not anonymous tips. They are a single witness's account, uncorroborated by physical evidence or other witness testimony in the available corpus. Trump also appears separately in FBI 302 summaries as an interview subject discussing his knowledge of Epstein, and in scheduling records showing social contact. A separate witness ([EFTA02857857](https://epstein-data.com/EFTA02857857)) describes Trump on speakerphone during her visit to Epstein. A massage therapist ([EFTA02857860](https://epstein-data.com/EFTA02857860)) says she massaged "Donald Trump's feet" on a plane.

**Regarding Bill Clinton:** No document in the corpus contains an allegation by an identified victim that Clinton committed sexual abuse. Clinton appears in scheduling and travel records documenting a multi-year social relationship, including documented flights on Epstein's aircraft. Third-party statements describe the relationship as social/political.

**Regarding victim credibility:** Memory inconsistencies in victim testimony are expected and documented in trauma research literature. Inconsistencies in dates, sequences, or details across multiple interviews conducted years apart do not discredit the underlying allegations. The FBI's own assessments treated inconsistencies as expected rather than disqualifying.

**Regarding the total number:** The true number of victims is unknown. The numbers cited above represent documented, identified individuals. Many victims never reported to law enforcement.

Further reading: [FBI 302 Missing Serials Dossier](https://epstein-data.com/reports/institutional/FBI_302_MISSING_SERIALS_DOSSIER.html)

---

# SECTION 5: THE PLAYERS

## A Producer's Guide to the Cast of Characters

*Organized by role. Each entry includes: name, role in the Epstein network, evidence weight (approximate document count in corpus), key documents with viewer links, current status, and segment potential for investigative journalism.*

---

### TIER A: THE INNER CIRCLE

These are the people who made the operation run day to day.

---

#### Ghislaine Maxwell — Co-Conspirator, Convicted

**Role:** Epstein's longtime partner, described as the chief recruiter and manager of the trafficking operation. [Convicted in December 2021](https://www.npr.org/2021/12/29/1066219689/ghislaine-maxwell-verdict-trial-jeffrey-epstein) on five of six counts including sex trafficking of a minor.

**Evidence weight:** 387 (travel connections) + 182 (association). Tens of thousands of documents across DS10/DS11 contain Maxwell's email correspondence. Her American Express Centurion card statements document travel and spending across multiple continents.

**Key documents:**
- [EFTA02335012](https://epstein-data.com/EFTA02335012) — Maxwell to Prince Andrew ("The Invisible Man"): "Some sight seeing some 2 legged sight seeing (read intelligent pretty fun and from good families)"
- [EFTA00011437](https://epstein-data.com/EFTA00011437) — Prince Andrew to Maxwell from Balmoral: "Have you found me some new inappro[priate friends]..."
- Maxwell trial transcripts and depositions across DS8, DS9

**Current status:** Serving 20-year sentence at FPC Bryan, Texas (transferred from Tallahassee July 2025 after Blanche interview). All appeals exhausted (Second Circuit denied 2024, SCOTUS cert denied October 2025, habeas denied January 2026). Declined House Oversight testimony February 9, 2026, invoking the Fifth Amendment. Seeking clemency from Trump, offering to testify that Trump and Clinton "did nothing wrong" in exchange. In her pro se habeas petition, named 4 unindicted co-conspirators and alleged the DOJ reached "secret settlements" with 25 men. Earliest possible release with good-time credit: ~2037.

**Segment potential:** HIGH — but the story is her network, not her conviction. The clemency play and the "25 men" allegation are both producible.

---

#### Sarah Kellen (now Sarah Kellen Vickers) — Scheduler/Assistant

**Role:** Epstein's personal assistant who managed the scheduling of "massage" appointments. Named as a co-conspirator in the 2007 Non-Prosecution Agreement but never charged. The NPA's immunity clause, expanded by prosecutors beyond what the original agreement specified, shielded Kellen and others from federal prosecution.

**Evidence weight:** 171 (travel). Thousands of scheduling emails in DS10/DS11.

**Current status:** Divorced from NASCAR driver Brian Vickers (finalized December 2025). Works in interior design, owns luxury properties in Miami and New York. House Oversight has requested her testimony for a transcribed interview on June 3, 2026. Not charged. Protected by NPA immunity.

**Segment potential:** MEDIUM — her scheduling emails are the operational backbone of the trafficking evidence. The upcoming House Oversight testimony request could change her status significantly.

---

#### Nadia Marcinkova (now Nadia Marcinko) — Victim Turned Associate

**Role:** Brought to the U.S. from Eastern Europe as a teenager. Described in victim testimony as both a victim and a participant in abuse. Later became a licensed pilot and aviation businesswoman.

**Evidence weight:** 124 (travel). Documented in victim 302s, flight records, and scheduling emails.

**Current status:** Disappeared from public view in early January 2024 after the final Epstein document unsealing. OSINT investigation found digital activity through November 2025 tied to Zen Studies Society (Buddhist community) in the New York area. Assessed as alive and in NY region as of early 2026. Never charged. Protected by NPA immunity.

**Segment potential:** MEDIUM — her dual status as victim and named co-conspirator is a complex narrative. Her disappearance from public life is itself a story.

---

#### Lesley Groff — Executive Assistant

**Role:** Epstein's chief executive assistant for over 20 years. Managed the office, arranged travel, coordinated schedules. Her scheduling emails in the corpus are the most granular record of Epstein's daily activities.

**Evidence weight:** Appears in thousands of scheduling documents across DS10/DS11.

**Key documents:**
- [EFTA00339454](https://epstein-data.com/EFTA00339454) — Scheduling email covering September-October 2015, showing daily contact management with public figures, medical appointments, travel coordination

**Current status:** Not charged. Protected by NPA immunity.

---

#### Jean-Luc Brunel — MC2 Models

**Role:** Founded MC2 Model Management with financial backing from Epstein. The modeling agency served as a recruitment pipeline for young women. Maxwell and Brunel are documented coordinating the sourcing of women through the modeling industry.

**Evidence weight:** 16 (travel) plus extensive references in victim testimony and financial records.

**Current status:** [Found dead in his Paris jail cell](https://www.npr.org/2022/02/19/1081961087/jeffrey-epstein-jean-luc-brunel-dead) on February 19, 2022, while awaiting trial on rape and sex trafficking charges. French authorities ruled suicide.

**Segment potential:** HIGH — his death while in custody mirrors Epstein's, and the French investigation into the modeling pipeline continues.

---

#### "Ross" — Unidentified Inner Circle

**Evidence weight:** 286 (association) — the third-highest connection weight in the entire corpus, behind only Leon Black (816) and Maxwell (387). Despite this extraordinary connection weight, "Ross" has not been definitively identified. The name appears in travel records and association data.

**Current status:** Unknown.

**Segment potential:** HIGH — the third most-connected person in Epstein's orbit, and nobody knows who they are.

---

### TIER B: THE MONEY

The financial operators, bankers, and billionaires who sustained the operation.

---

#### Darren Indyke — Personal Attorney / Co-Executor

**Role:** Epstein's longtime personal attorney who became co-executor of the estate. Filed the DHS/FOIA complaint attempting to block EFTA document releases. Operated through Darren K. Indyke PLLC.

**Evidence weight:** 70+ EFTA citations. Financial records show $259,740 in his firm's Deutsche Bank account.

**Key documents:**
- DHS/FOIA complaint filing
- Estate administration records
- Deutsche Bank correspondence

**Current status:** Under House Oversight subpoena (letters sent Feb 2026). Active attorney in New York.

**Segment potential:** HIGH — the gatekeeper of Epstein's legal and financial architecture, now under congressional scrutiny.

---

#### Richard Kahn — Trustee / "Project Manager"

**Role:** Epstein's CPA who rose to become the manager of HBRK Associates, the operational hub controlling $84.5 million in managed accounts. Generated 35,919 documents in the corpus. Kahn's trust agreement contained a Section 2.5 lock-in clause making his removal nearly impossible without cause.

**Evidence weight:** 38+ EFTA citations in dedicated witness brief. 35,919 documents through HBRK.

**Key documents:**
- HBRK managed account statements
- Trust agreement with Section 2.5 lock-in
- Deutsche Bank RM82289 correspondence

**Current status:** Under House Oversight subpoena (issued Feb 25, 2026). Appeared at deposition.

**Segment potential:** HIGH — Kahn knows where every dollar went, and Congress is asking him.

---

#### Leon Black — Apollo Global Management

**Role:** Co-founder of Apollo Global Management. Paid Epstein $158M+ between 2012-2017. Codename: "Mr. Big." Subject of an "HT Subject Referral" in federal records that produced no charges. Named in a DS12 FBI FD-302 where a victim describes being sent by Epstein to service him.

**Evidence weight:** 816 (highest in corpus).

**Key documents:**
- [EFTA02857849](https://epstein-data.com/EFTA02857849) — DS12 FD-302: Brazilian victim describes being sent to Black four times in New York in 2004; describes him as "tall, heavy, large stomach, gray hair, big nose, mole on face"
- [EFTA02731737](https://epstein-data.com/EFTA02731737) — DA stating "do not doubt her allegations"
- [EFTA02731473](https://epstein-data.com/EFTA02731473)–02731783 — HT investigation file (~50 docs)
- [EFTA00025507](https://epstein-data.com/EFTA00025507) — Apollo Board review reference

**Current status:** Stepped down as Apollo CEO in 2021. **Deposition ordered** in victims' BofA lawsuit (Judge Rakoff, March 11, 2026; scheduled March 26). BofA trial set for May 11, 2026. Voluntary House Oversight appearance scheduled May 13, 2026. Senator Wyden [released Black's $62 million USVI settlement](https://www.finance.senate.gov/ranking-members-news/wyden-releases-new-information-on-financing-of-jeffrey-epsteins-operations-by-billionaire-leon-black-seeks-documents-from-trump-administration), which gave Black immunity from criminal prosecution in the Virgin Islands. Bloomberg reported extensively on the relationship in February 2026.

**Segment potential:** HIGH — the largest documented financial relationship, an unresolved HT referral, a DA statement on record, an upcoming deposition, and a trial.

---

#### Les Wexner — L Brands / Victoria's Secret

**Role:** Founder of L Brands (Victoria's Secret, Bath & Body Works). Epstein's first major benefactor. Granted Epstein extraordinary power of attorney over his personal finances in the late 1980s. Transferred the East 71st Street Manhattan mansion to Epstein. The connection between Victoria's Secret and Epstein's access to young women has been alleged but not conclusively documented in the corpus.

**Evidence weight:** 41 (association).

**Key documents:**
- Power of attorney documents
- [EFTA01682081](https://epstein-data.com/EFTA01682081) — reference to decision "not to sue Wexner"
- Wexner deposition (video released; official transcript pending)

**Current status:** Retired from L Brands. Deposed by House Oversight on February 18, 2026 at his New Albany, Ohio mansion for five hours. Called Epstein a "con man" and denied friendship. Video released by the committee. Democrats accused him of facilitating trafficking. ([CNBC](https://www.cnbc.com/2026/02/18/jeffrey-epstein-les-wexner-deposition.html))

**Segment potential:** MEDIUM — the origin story of Epstein's wealth and access. The deposition adds new material but Wexner has been extensively covered.

---

#### Jes Staley — JPMorgan / Barclays

**Role:** Senior JPMorgan executive who managed Epstein's banking relationship. Later became Barclays CEO before being forced out over Epstein ties. Named as a sexual abuser in victim statements within the corpus.

**Evidence weight:** 72 (association).

**Key documents:**
- Internal JPMorgan correspondence about the Epstein relationship
- Victim statements naming Staley
- Communications showing Staley leaked JPMorgan intelligence to Epstein regarding the Sal. Oppenheim bank rescue

**Current status:** Resigned from Barclays in 2021. Subject of UK FCA investigation. JPMorgan [settled Epstein-related lawsuits for $290M](https://www.npr.org/2023/06/12/1181675580/epstein-jane-doe-1-290-million-settlement-jpmorgan-chase) in 2023.

**Segment potential:** HIGH — a sitting bank CEO brought down by the Epstein connection, with victim statements in the record.

---

#### Deutsche Bank Team — The Institutional Enabler

**Role:** At least 13 named employees managed Epstein's accounts under RM CODE 82289, enabling financial flows while KYC compliance remained incomplete. The bank [paid $150M](https://www.cnbc.com/2020/07/07/jeffrey-epstein-case-deutsche-bank-fined-150-million-penalty-for-relationship.html) to settle compliance failure charges in 2020.

**Key figures:** Natalie Barak (RM), Stewart Oldfield, Bradley Gillin, Tazia Smith

**Key documents:**
- [EFTA00027019](https://epstein-data.com/EFTA00027019) — master transaction tables
- Internal compliance emails
- €30M currency options documentation

**Current status:** Deutsche Bank settled. Individual bankers not charged. Oldfield named by Reuters (Feb 2026).

**Segment potential:** HIGH — the institutional enabler story, with named individuals and internal documents showing they knew.

---

### TIER C: THE POLITICAL

Public figures with documented connections. Each entry states what the documents show AND what they do not show.

---

#### Bill Clinton — 42nd President

**Role:** Social/political associate documented in scheduling records, flight manifests, and correspondence.

**Evidence weight:** 45 (association).

**Key documents:**
- Flight records showing travel on N908JE (Epstein's Boeing 727)
- Secret Service logistics correspondence
- 2002 Africa trip documentation
- Scheduling emails placing Clinton at Epstein events

**What the files show:** A multi-year social relationship with documented flights, event attendance, and coordinated scheduling through Epstein's staff.

**What the files do NOT show:** No document contains a victim allegation of sexual misconduct by Clinton. No document places Clinton at a location during an instance of documented abuse.

**Current status:** Living. Not charged. Not under known active investigation.

**Segment potential:** MEDIUM — the name drives interest but the documents show a social relationship, not criminal conduct.

---

#### Donald Trump — 47th President

**Role:** Social acquaintance of Epstein documented in scheduling records, FBI interview summaries, and third-party statements. Subject of a PROTECT SOURCE witness's allegations of sexual assault when she was a minor.

**Evidence weight:** 33 (association). 4 PROTECT SOURCE FD-302 interviews, ~20 additional FD-302 interview summaries, ~15 NTOC tips.

**Key documents:**
- [EFTA02858481](https://epstein-data.com/EFTA02858481) — PROTECT SOURCE Interview #2 (10 pages): witness describes Trump forcing oral sex when she was 13-15, Trump struck her, said "Let me teach you how little girls are supposed to be"
- [EFTA02858491](https://epstein-data.com/EFTA02858491) — PROTECT SOURCE Interview #3 (4 pages): witness clarifies Trump "pulled her hair and punched her on the side of her head"
- [EFTA02857857](https://epstein-data.com/EFTA02857857) — Chilean witness: Trump on speakerphone during her visit to Epstein
- [EFTA02857860](https://epstein-data.com/EFTA02857860) — Massage therapist: massaged "Donald Trump's feet" on a plane
- [EFTA02858497](https://epstein-data.com/EFTA02858497) — Original NTOC tip (July 8, 2019) that initiated the PROTECT SOURCE investigation

**What the files show:** Four FBI interviews (DS12 expansion, March 2026) record a woman designated PROTECT SOURCE alleging that Trump sexually assaulted her when she was between 13 and 15. She told agents Trump forced oral sex, struck her, and said words to the effect of "get this little bitch the hell out of here." She stated Trump and Epstein used terms like "fresh meat" and "untainted" when referring to girls. She said she was "confident TRUMP knew EPSTEIN blackmailed people." In a separate interview, a Chilean witness describes Trump on a speakerphone call with Epstein during her visit. A massage therapist describes massaging Trump's feet on Epstein's plane. Scheduling records document social contact in the late 1990s and 2000s. Trump made a public statement in 2002 that Epstein "likes beautiful women as much as I do, and many of them are on the younger side."

**What the files do NOT show:** The PROTECT SOURCE allegations are a single witness's account. No second witness corroborates the specific assault allegations. No physical evidence in the corpus links Trump to the described incidents. The witness's account has not been tested through cross-examination. Separately, the ~15 NTOC tips referencing Trump are unverified caller reports (Tier 3 reliability). No document places Trump at Little Saint James, Zorro Ranch, or any Epstein property during a documented instance of abuse of a different victim. Roger Sollenberger reported that the DOJ removed and then partially restored these documents; NPR independently verified the removal pattern.

**Current status:** 47th President of the United States. DOJ removed the PROTECT SOURCE interview documents from justice.gov in February 2026 and partially restored them in the DS12 expansion in March 2026. 37 pages of FBI agent notes from the interviews remain withheld.

**Segment potential:** HIGH. The PROTECT SOURCE interviews, the DOJ's removal and partial restoration of the documents, and the 37 still-withheld pages of agent notes are all producible. Sollenberger and NPR have both reported on the removal pattern. The witness's request for protection ("Throughout my life his people have found me... have kept tabs on me") and the FBI's PROTECT SOURCE designation add context.

---

#### Prince Andrew, Duke of York — "The Invisible Man"

**Role:** Long-term social associate documented extensively in email correspondence with Maxwell. Identified through seven independent proofs as "The Invisible Man" in coded emails.

**Evidence weight:** 181 (association).

**Key documents:**
- [EFTA00011437](https://epstein-data.com/EFTA00011437) — Andrew from Balmoral: "Have you found me some new inappro[priate friends]..."
- [EFTA02335012](https://epstein-data.com/EFTA02335012) — Maxwell: "2 legged sight seeing (read intelligent pretty fun and from good families)"
- [EFTA02332233](https://epstein-data.com/EFTA02332233) — "Andrew sweet heart"
- Email aliases: `abx17@dial.pipex.com`, `aace@dial.pipex.com` (both targeted in FBI search warrant)

**What the files show:** Extensive personal correspondence with Maxwell spanning 2001-2002, including requests for Maxwell to procure female companions described in sexually suggestive language. The Balmoral email's truncated "inappro..." and Maxwell's "2 legged sight seeing" language speak for themselves.

**What the files do NOT show:** The corpus does not contain direct evidence of sexual abuse by Prince Andrew. The [Virginia Giuffre civil settlement](https://www.npr.org/2022/02/15/1080828750/prince-andrew-settlement-virginia-giuffre) (reported as £12M, 2022) resolved allegations outside the EFTA production.

**Current status:** Stripped of all titles and honors (October 2025). **Arrested February 19, 2026** on his 66th birthday on suspicion of misconduct in public office: sharing confidential trade envoy reports with Epstein. First senior British royal arrested in approximately 400 years. Released under investigation. Not yet charged. Maximum sentence if convicted: life imprisonment. Previously [settled the Giuffre civil lawsuit](https://www.npr.org/2022/02/15/1080828750/prince-andrew-settlement-virginia-giuffre) in 2022 for a reported £12M.

**Segment potential:** HIGHEST — the coded emails are the most quotable documents in the entire corpus, the seven-proof identification chain is airtight, and the arrest makes it a live story.

---

#### Alan Dershowitz — Attorney / Associate

**Role:** Harvard Law professor who served as Epstein's defense attorney and has been accused by Virginia Giuffre of sexual abuse (allegations he has consistently and vigorously denied).

**Evidence weight:** 43 (association) + 9 (travel).

**Key documents:**
- Legal filings and correspondence as Epstein's attorney
- [EFTA00601154](https://epstein-data.com/EFTA00601154) — Dershowitz naming Benjamin Brafman as volunteer attorney: "Ben Brafman is one of the leading criminal lawyers... He has volunteered to help me"
- Travel records

**Current status:** Living. Continues to deny all allegations. Active in media commentary.

---

#### William Barr — Attorney General (2019)

**Role:** Served as U.S. Attorney General during Epstein's arrest, detention, and death. Recused himself from the Epstein case due to his former law firm's (Kirkland & Ellis) representation of Epstein, then reportedly un-recused himself. His father, Donald Barr, hired a young Epstein to teach at the Dalton School in 1973.

**Evidence weight:** 234 (association — reflects AG role, not personal involvement).

**Key documents:**
- NTOC tip handling records during his tenure
- Recusal/un-recusal documentation
- AG correspondence regarding Epstein case

**What the files do NOT show:** No document suggests Barr personally intervened to protect Epstein or influence the prosecution. The high association weight reflects his institutional role as AG, not a personal relationship.

**Current status:** No longer AG.

**Segment potential:** MEDIUM — the recusal question and the Dalton School connection are real but largely reported.

---

#### Ehud Barak — Former Israeli Prime Minister

**Role:** Long-term associate documented in 3,756+ corpus records spanning 2013 through February 2019. The relationship included a week-long island stay, an apartment at 301 East 66th Street (the same building as MC2 and documented trafficking victims), and investment in Carbyne (50+ documents) and Reporty (324+ documents) — surveillance technology companies.

**Evidence weight:** 14 (association) in knowledge graph, but 3,756+ documents in full corpus search.

**Key documents:**
- [EFTA00090314](https://epstein-data.com/EFTA00090314) — FBI CHS FD-1023 containing an *unverified* claim that "Epstein belonged to both U.S. and allied intelligence services" and "trained as a spy under" Barak. **Note: CHS reports are raw intelligence, not established facts.**
- Carbyne/Reporty investment documentation
- Calendar records showing meeting frequency
- Email: Epstein to Barak: "you should make clear that i dont work for mossad :)" / "unfortunately, not" — Barak: "You or I?" ([EFTA01013272](https://www.justice.gov/epstein/files/DataSet%209/EFTA01013272.pdf))

**What the files do NOT show:** No document establishes that Barak participated in or was aware of sexual abuse. The CHS intelligence claim about Epstein's spy training is unverified and comes from a single confidential source.

**Current status:** Living in Israel. Not charged. Confirmed apartment use.

**Segment potential:** HIGH — the intelligence thread alone is producible, and the "i dont work for mossad" email exchange is a remarkable document.

---

#### Senator George Mitchell

**Role:** Former Senate Majority Leader. Named in a DS12 FBI FD-302 where a victim describes being dispatched by Epstein to service Mitchell at two hotels.

**Evidence weight:** Referenced in DS12 302 interviews and scheduling correspondence.

**Key documents:**
- [EFTA02857849](https://epstein-data.com/EFTA02857849) — DS12 FD-302: Brazilian victim describes being sent to Mitchell at the Beverly Hills Hotel in Los Angeles, where Mitchell was on the phone with Epstein when she arrived and said "She's here." Epstein later sent her to Mitchell again at the Four Seasons in Washington, D.C. This is the first FBI FD-302 in the public record where a witness describes being dispatched by Epstein to service a named individual under an FBI case number.

**Current status:** Retired from public life. Mitchell has denied inappropriate conduct. ([Maine Campus](https://mainecampus.com/category/news/2026/02/george-mitchell-found-in-epstein-files-umaine-to-consider-changing-program-names/))

---

#### Alexander Acosta — U.S. Attorney (2007 NPA)

**Role:** As U.S. Attorney for the Southern District of Florida, Acosta approved the 2007 Non-Prosecution Agreement that gave Epstein and named co-conspirators extraordinary blanket immunity. Later served as Secretary of Labor under Trump before resigning in 2019 after the NPA became public.

**Key fact:** Acosta reportedly told the Trump transition team during his cabinet vetting that he was told to leave Epstein alone because "he belonged to intelligence." This claim was [reported by Vicky Ward in The Daily Beast](https://www.thedailybeast.com/jeffrey-epsteins-sick-story-played-out-for-years-in-plain-sight/) in 2019, citing an anonymous source. Acosta has not confirmed it.

**Key documents:**
- The NPA itself and negotiation correspondence (2007)
- [EFTA01688067](https://epstein-data.com/EFTA01688067) — **NOTE: This is the "Nassar letter" which the DOJ has declared FAKE. Do not cite as evidence.**
- Kenneth Starr's 36-page lobbying fax to Acosta on Epstein's behalf

**Current status:** Nominated to serve again as Secretary of Labor in 2025. Previously resigned in 2019 after the NPA terms became public.

---

### TIER D: THE INSTITUTIONAL PLAYERS

The prosecutors, guards, and handlers who shaped the investigation and its failures.

---

#### Kathryn Ruemmler — Former Obama White House Counsel

**Role:** Became Epstein's personal attorney after leaving the White House. Extensive email correspondence with Epstein in DS11 spanning 2015-2018, including discussions of legal strategy, social commentary, and the "MacGyver" codename (see below).

**Evidence weight:** Hundreds of emails in DS11.

**Key documents:**
- Ruemmler-Epstein correspondence throughout DS11
- "MacGyver" discussion chain (see Pseudonym Registry)
- Legal strategy communications

**Current status:** Partner at Goldman Sachs. Previously general counsel at Goldman.

**Segment potential:** HIGH — a former White House Counsel serving as personal attorney to a convicted sex offender, with extensive candid correspondence in the record.

---

#### MCC Guards — Tova Noel & Michael Thomas

**Role:** The two correctional officers assigned to Epstein's Special Housing Unit on the night of August 9-10, 2019. Both falsified records claiming they had conducted inmate rounds when they had not.

**Key documents:**
- [EFTA00010968](https://epstein-data.com/EFTA00010968) — Indictment
- TRUINTEL operational logs (removed from justice.gov)
- FBI 302 interviews with BOP officers (removed from justice.gov)

**Current status:** Indicted November 2019. Entered [deferred prosecution agreements](https://www.npr.org/2021/05/22/999441586/jeffrey-epstein-guards-would-avoid-serving-jail-time-in-a-new-deal-with-prosecut) requiring 100 hours of community service. [Charges dismissed January 2022](https://edition.cnn.com/2022/01/03/us/jeffrey-epstein-officers-dismissed-charges-judge).

**Segment potential:** MEDIUM — the lenient resolution is itself a story.

---

#### The SDNY Prosecution Team

**Key figures:** Maurene Comey (AUSA, daughter of former FBI Director James Comey), Alison Moe (AUSA), and their supervisors.

**Role:** Managed the 2019 federal prosecution of Epstein and the subsequent Maxwell case. Also orchestrated the halt of New Mexico's independent investigation and maintained control over all parallel Epstein investigations through at least May 2021.

**Key documents:**
- [EFTA00019183](https://epstein-data.com/EFTA00019183) — The SDNY-DNM email chain documenting the NM investigation halt
- Prosecution memos from DS12

---

#### FBI CART Lab — The One-Day-Per-Week Examiner

**Role:** The FBI's Computer Analysis and Response Team processed all seized digital evidence. A single CART examiner was assigned to the Epstein case. During COVID, that examiner was reduced to one day per week, stretching processing timelines by "a factor of 5." Evidence review was still ongoing in April 2025, six years after seizure.

**Key documents:**
- [EFTA00038465](https://epstein-data.com/EFTA00038465) — CART evidence log (complete device inventory)
- Internal processing timeline emails

**Segment potential:** MEDIUM — institutional failure story, not a character piece. But illustrative of systemic dysfunction.

---

#### Kenneth Starr — Epstein's Lobbyist

**Role:** The former independent counsel who investigated President Clinton sent a 36-page lobbying fax to U.S. Attorney Acosta on Epstein's behalf during the NPA negotiations. Starr, along with Dershowitz and Jay Lefkowitz (a Kirkland & Ellis partner), formed what Acosta described as "an army of legal superstars" deployed to prevent federal prosecution.

**Key documents:**
- The 36-page lobbying fax
- [EFTA00009116](https://epstein-data.com/EFTA00009116) — Acosta OPR interview: "an army of legal superstars"

**Current status:** Deceased (September 2022).

---

#### Steve Bannon — Political Advisor

**Role:** Exchanged iMessages with Epstein in 2018-2019 (DS10), documented in the corpus. Discussions included Harvey Weinstein's legal defense, Italian political contacts (Salvini, Grillo, Five Star Movement), and War Powers lobbying through "Mr. Evil" (Shaher Abdulhak). Bannon's role appears to be that of a political consultant, with Epstein serving as a real-time advisor during Bannon's 2018 Italy tour.

**Key documents:**
- [EFTA01615580](https://epstein-data.com/EFTA01615580) — Bannon-Epstein iMessage: Weinstein defense, "Ben" (Brafman)
- Italian connections correspondence

**Current status:** Previously convicted of contempt of Congress (pardoned). Active in political consulting.

**Segment potential:** MEDIUM — the Bannon-Epstein relationship has been reported by CNN. The specific Italian connections and Weinstein legal strategy discussions add depth.

---

#### Howard Lutnick — Cantor Fitzgerald

**Role:** CEO of Cantor Fitzgerald, documented in 13 association records. The corpus shows social contact with Epstein. Lutnick was nominated as Secretary of Commerce in 2025.

**Evidence weight:** 13 (association).

**Current status:** Serving as Secretary of Commerce.

**What the files do NOT show:** The corpus documents social contact but does not contain allegations of criminal conduct by Lutnick.

---

#### Glenn and Eva Dubin — Highbridge Capital

**Role:** Glen Dubin (Highbridge Capital Management) has 65 association records and 18 travel records with Epstein. Eva Dubin exchanged personal health information through Epstein's email system. "Jeepers Glen Dubin" links the Jeepers Inc. shell company directly to Glen Dubin. Named in the "Prominent Names" document. 34+ documented flights on Epstein aircraft.

**Evidence weight:** 65 (association) + 18 (travel).

**Segment potential:** HIGH — extensive flight records, a named shell company, and health communications through Epstein's systems.

---

#### Robert Trivers — Evolutionary Biologist

**Role:** Rutgers University professor whose decade-long financial dependency on Epstein is documented across 78 EFTAs. The funding pipeline ran through COUQ → ELF → HBRK shell entities. Epstein controlled Trivers' research direction: blocked an honor killings study, steered him toward transgender biology. Trivers was expelled from Chapman University for flashing a staff member and made a private confession of "a bit more than massages." A 2023 FBI FinCEN deconfliction request indicates financial investigation.

**Key documents:**
- Funding pipeline documentation
- Chapman University expulsion records
- FinCEN deconfliction request

**Current status:** Retired from Rutgers.

**Segment potential:** MEDIUM — illustrates the science funding model (control through dependency) but Trivers is not a household name.

---

#### David Mitchell / Cascade Investment — Bill Gates

**Role:** Mitchell, of Cascade Investment (Bill Gates' investment vehicle), coordinated between Gates and Epstein. The corpus documents scheduling and financial discussions. A Gates Foundation internal email found in Epstein's files had an entire page blacked out in the DOJ's post-publication alterations.

**Evidence weight:** Documented in scheduling correspondence, financial records.

**Current status:** Active at Cascade.

---

### TIER E: THE UNRESOLVED

People and entities that appear prominently in the corpus but whose roles are not fully understood.

---

#### The Alexander Brothers — Allen, Oren, and Tal

**Role:** Three brothers described in FBI tips as present at Epstein's New York parties. A victim reported: "Oren raped her best friend and a third brother, Tal, raped a 14 year old girl named Katie."

**Key documents:**
- [EFTA01660651](https://epstein-data.com/EFTA01660651) — FBI tip
- [EFTA01660679](https://epstein-data.com/EFTA01660679) — FBI tip

**Current status:** Currently on trial at SDNY (since January 2026) for sex trafficking of 60+ women. Their mistrial motion after the Epstein files release was denied by Judge Caproni. The FBI had annotated the original tip as "possibly identifiable as Alexander brothers" but delayed action for years.

**Segment potential:** HIGH — active trial, clear documentary trail from Epstein tip to current prosecution.

---

#### Frederic Fekkai — Celebrity Hairstylist

**Role:** 3,534 pages across 3,067 documents. Deposition testimony: "Fekkai is in Hawaii. Can we find some girls for him?" Virginia Roberts was sent to Fekkai's salon as part of her grooming. Fekkai lived in an Epstein-controlled apartment (301 E 66th St), exchanged emails with Epstein over a decade, and appears on Epstein's "girls list" email.

**Key documents:**
- Deposition testimony about "finding girls" for Fekkai
- Scheduling emails documenting salon visits as part of victim grooming
- "Girls list" email
- St. Barths 2010 guest list

**Current status:** Active celebrity hairstylist. Not charged. Not publicly reported in connection with Epstein corpus evidence.

**Segment potential:** HIGH — completely unreported, extensive corpus presence, direct solicitation language in testimony.

---

#### "MacGyver" / Benjamin Brafman — Defense Attorney (HIGH CONFIDENCE)

The codename "MacGyver" (also spelled "Macgiver") appears in Epstein-Ruemmler emails from 2015-2018. External reporting (Defector, American Prospect, CNN) identified MacGyver as Trump, based on an email comparing Trump's mannerisms to MacGyver's. Corpus analysis strongly suggests MacGyver is actually defense attorney **Benjamin Brafman**:

- "Was asked and passed" to represent Eric Schneiderman (you ask a *lawyer* to take your case)
- "Macgiver loves representing misogynists — he empathizes with and relates to them" (describes a defense practice)
- "Even more fitting would be macgiver defending" (legal defense context)
- The Bannon iMessage clincher: Epstein and Bannon discuss Weinstein's defense, referring to "Ben" who had just separated from Weinstein as counsel in January 2019 — Benjamin Brafman ([EFTA01615580](https://epstein-data.com/EFTA01615580))
- The email comparing Trump to MacGyver says "similar mannerisms" — comparing two different people, not identifying them as the same person
- Brafman and "MacGyver" never co-occur in the same document

The full evidence chain includes 15 emails and the Bannon iMessage. (Further reading: [Pseudonym Registry](https://epstein-data.com/reports/individuals/PSEUDONYM_CODENAME_REGISTRY.html))

---

#### "Dr. Evil" / Dr. Steven Victor — NYC Dermatologist (CONFIRMED)

Epstein's codename for Dr. Steven A. Victor, a cosmetic dermatologist. The identification is confirmed by a smoking gun email where the same appointment is referred to as "dr evil" in the morning and "victor" in the evening reply ([EFTA01991050](https://epstein-data.com/EFTA01991050)). Victor provided $20,000+ in free cosmetic treatments to young women in Epstein's circle in exchange for Epstein "bailing him out" of financial trouble ([EFTA01779967](https://epstein-data.com/EFTA01779967): "the last time I bailed you out we agreed I would never see another bill for my friends"). Completely original finding, not previously reported.

---

#### HBRK Associates — The Operational Hub

35,919 documents. $84.5 million in managed accounts. The single largest cluster of documents associated with any entity other than Epstein himself. HBRK was Epstein's post-prison financial management operation, run by Richard Kahn, with Emad Hanna as a key operator. No outlet has reported on the operational architecture: the trust lock-in, construction operations, or the 39+ entities managed through HBRK. (Further reading: [HBRK investigation](https://epstein-data.com/reports/individuals/EMAD_HANNA_HBRK_INVESTIGATION.html))

---

#### Emmy Tayler — Maxwell's Assistant

**Evidence weight:** 185 (travel). Maxwell's personal assistant, documented in extensive travel and scheduling records. Tayler's travel records place her at nearly every Epstein property and event during the 2000s-2010s period.

**Current status:** Not publicly charged. Investigation status unknown.

---

#### Eduardo Teodorani-Fabbri — The "Master" Correspondent

SVP at CNH Industrial (Agnelli/Elkann dynasty), Teodorani-Fabbri addressed Epstein as "Master" in emails spanning 2012-2019. The correspondence reveals a subservient relationship: "Hi master. How are you I am in USA" ([EFTA01873297](https://epstein-data.com/EFTA01873297)), "Master the airport is Ciampino" ([EFTA01619031](https://epstein-data.com/EFTA01619031)), "master can you lend me your plane." The corpus documents efforts to connect Epstein to the Elkann family ("new target"), the Borghese family, and Italian political figures.

**Segment potential:** MEDIUM — the "Master" language is striking but Teodorani is not widely known.

---

#### Peggy Siegal — Celebrity Event Planner

**Role:** NYC event planner who organized social gatherings attended by Epstein. Documented in scheduling emails and correspondence.

**Current status:** Publicly ostracized after the Epstein connection became known. Career significantly damaged.

---

#### Bobby Kotick — Activision CEO

**Role:** Former CEO of Activision Blizzard. Documented in Epstein scheduling emails and correspondence.

**Current status:** Left Activision after Microsoft acquisition. Connection to Epstein widely reported.

---

#### Noam Chomsky — MIT Linguist

**Role:** Met with Epstein multiple times, documented in scheduling emails. Phone number listed in Groff scheduling records ([EFTA00339454](https://epstein-data.com/EFTA00339454)). Chomsky acknowledged meeting Epstein to discuss political topics.

**Current status:** Retired professor. Health issues reported.

**What the files do NOT show:** No document connects Chomsky to illegal activity. The documents show social meetings and phone contact.

---

#### Larry Summers — Harvard / Treasury

**Evidence weight:** 26 (association). Former Harvard president and Treasury Secretary. Documented in scheduling records and correspondence. A central node in the science/academic network.

**Current status:** Active academic and public commentator.

---

#### Boris Nikolic — Bill Gates Advisor

**Role:** Science advisor to Bill Gates. Named as a backup executor in Epstein's will, signed the day before Epstein's death. Nikolic said he was "shocked" to learn of the designation. Facilitated introductions between Epstein and the science network, including Larry Summers and Christine Lagarde.

**Key documents:**
- Will signing records
- Correspondence facilitating Epstein-Gates network introductions
- Lagarde currency exchange suggestion email

---

#### CBP Officers — The USVI Customs Pipeline

**Role:** Multiple Customs and Border Protection officers facilitated Epstein's travel through the U.S. Virgin Islands, allowing his entourage to bypass standard customs inspections. Key figure: David Routch. Additional officers named in NYT reporting (February 2026): Heil, Samuel, Richards, Montgomery, Martinez.

**Key documents:**
- FBI internal referral documents
- DHS/FOIA complaint (filed by Indyke)
- CBP correspondence

**Current status:** NYT reported extensively (Feb 19-20, 2026). Routch status unknown.

**Segment potential:** LOW (already reported by NYT in detail).

---

#### Shaher Abdulhak / "Mr. Evil" — Yemeni Billionaire Heir

**Role:** Identified through 5 independent proofs as "Mr. Evil" (distinct from "Dr. Evil" / Steven Victor). Yemeni billionaire heir connected to a War Powers lobbying pipeline through Steve Bannon. 57 documents in the corpus. Abdulhak's camp sought to influence U.S. policy on the Yemen war through Epstein's political connections, with a Pompeo team pitch documented.

**Key documents:**
- [Full investigation report](https://epstein-data.com/reports/individuals/SHAHER_ABDULHAK_MR_EVIL_INVESTIGATION.html)

**Current status:** Al Bawaba and Yahoo News have mentioned the name; the codename + lobbying pipeline is unreported.

**Segment potential:** HIGH — war-powers lobbying through a convicted sex trafficker is a producible story.

---

#### Jean Pigozzi — Billionaire Photographer

**Role:** Heir to the Simca automobile fortune. Attended Epstein events, documented in guest lists and scheduling emails. Connected to the science network through Edge Foundation dinners.

**Current status:** Living. Active art collector.

---

#### The Reuben Brothers — UK Billionaires

**Role:** Sir David and Sir Simon Reuben. Documented in Epstein's social network through the Siren luxury yacht connection and Chernoy/Cherney business relationships.

**Current status:** Active businessmen. Net worth >$20B.

---

#### David Geffen — Entertainment Mogul

**Role:** DreamWorks co-founder documented in Epstein scheduling and correspondence records.

**Current status:** Retired from active business. Living on yacht Rising Sun.

---

# SECTION 6: THE DEATH

## August 10, 2019

### 6.1 Three Investigations, One Conclusion

Three separate federal investigations examined Jeffrey Epstein's death at the Metropolitan Correctional Center:

1. **FBI Death Investigation** (Case 90A-NY-3151227) — Epstein classified as the victim, subject listed as "UNSUB(S)" (unknown subjects). The New York City Office of the Chief Medical Examiner ruled death by suicide by hanging.
2. **DOJ Office of Inspector General** — Four-year investigation (2019-2023) finding "numerous and serious failures" by MCC staff. 127-page public report. ([OIG report](https://oig.justice.gov/reports/investigation-and-review-federal-bureau-prisons-custody-care-and-supervision-jeffrey))
3. **SDNY Criminal Prosecution** — Guards Tova Noel and Michael Thomas indicted for falsifying records. [Deferred prosecution agreements](https://www.npr.org/2021/05/22/999441586/jeffrey-epstein-guards-would-avoid-serving-jail-time-in-a-new-deal-with-prosecut) (100 hours community service). [Charges dismissed January 2022](https://edition.cnn.com/2022/01/03/us/jeffrey-epstein-officers-dismissed-charges-judge).

### 6.2 The DVR Timeline

The surveillance camera system at MCC was in a state of documented failure leading up to Epstein's death:

- **147 cameras** total at MCC, capturing **8.08 TB** of data ([EFTA00164855](https://epstein-data.com/EFTA00164855))
- **July 29, 2019:** DVR2 suffered a "system failure" and "was not recording"
- **August 8, 2019:** Two hard drives in DVR2 failed — two days before the death
- **The cameras in the Special Housing Unit, where Epstein was located, were not active at the time** of his death
- Inmate head count was not conducted 5 times during the relevant period

### 6.3 The Night Before: The Phone Call

On August 9, Epstein's cellmate Efrain Reyes was transferred for a court hearing and did not return. Despite BOP policy requiring a cellmate at all times, no replacement was assigned. Staff were informed at 1:50 PM that the cellmate would not return. The handoff was "spread by word of mouth" — no emails or documentation.

That evening, Epstein terminated a legal visit early to make a phone call. The BOP Psychological Reconstruction records:

> "Since Mr. Epstein reportedly did not have his PAC or PIN number, which is required to use the inmate telephone system, the Unit Manager placed the call, dialing a number that reportedly began with area code 347. Mr. Epstein told Mr. Bullock he was calling his mother who, according to public records, has been deceased since 2004."

([EFTA00041963](https://epstein-data.com/EFTA00041963), p. 14)

A congressional OIG interview provides more: when the Unit Manager dialed the 347 number, "a man answered." The Unit Manager handed the phone to Epstein and left for the day, instructing no one to monitor the call. ([EFTA00061927](https://epstein-data.com/EFTA00061927), pp. 62-64)

Public reporting has identified the call recipient as Karyna Shuliak, described as Epstein's girlfriend and primary estate beneficiary.

The same documents reveal: "a review of financial transactions associated with Mr. Epstein's prison account revealed one of his attorneys was depositing funds into his cellmate's (inmate Reyes) commissary account for unknown reasons."

### 6.4 The Discovery

At approximately 6:33 AM on August 10, officers found Epstein unresponsive in cell #220 on L Tier. Clinical Nurse J. Ono recorded: "Inmate was Cold, with circumferential Bruising around the neck and posterior mottling, Pupils Fixed and dilated, No Palpable pulses were felt." An AED showed asystole (flat line). Three rounds of epinephrine administered. Pronounced dead at 7:36 AM.

Inmate Johnny Contreras told the FBI that "EPSTEIN did not have any marks around his neck and he didn't see a rope around EPSTEIN's neck" and that his cellmate "made a comment that EPSTEIN didn't hang himself because he didn't have the typical injuries." ([EFTA00132208](https://epstein-data.com/EFTA00132208), p. 173)

The nurse's report and the inmate's observation describe different things at different moments. The nurse arrived to find "circumferential Bruising around the neck." The inmate observed from a distance through cell bars in the immediate aftermath. Both are documented. Both are cited. The reader can weigh them.

### 6.5 The Removed Documents

Sixteen death investigation documents totaling approximately 1,987 pages have been removed from justice.gov. Among them:

- The FBI FD-302 death investigation serial (476 pages, at least 11 witness interviews)
- BOP TRUINTEL operational logs from the SHU (1,395 pages across two documents)
- Four copies of the BOP Form 583 incident report (88 pages total)
- The OIG evidence disposition memo documenting 18 hard drives seized from MCC's camera system
- The FBI's one-page death investigation timeline

Two documents were restored on February 24, 2026: the BOP Psychological Reconstruction (1,000 pages) and the July 23 first incident documentation. The remaining 16 are still offline.

None of these documents contain victim PII, CSAM, or classified national security material — the [EFTA's five permitted bases for withholding](https://www.congress.gov/bill/119th-congress/house-bill/4405).

### 6.6 The BOP Psychological Reconstruction

The restored 1,000-page BOP document ([EFTA00041963](https://epstein-data.com/EFTA00041963)) is the most detailed account of Epstein's final weeks. Key findings:

- Every BOP psychology assessment rated chronic suicide risk as **"Absent"**
- Acute risk was stepped up to "Moderate" on July 23 (after the first incident) then returned to "Low" on July 24, where it remained through August 1
- No psychological assessment was conducted after bail denial (July 18), despite BOP policy requiring it
- Epstein told psychologists he was "a coward" who "does not like pain"
- The July 23 incident report coding was **expunged** by August 15 — "it is unclear why it had been expunged"
- The document notes: "It is unclear at this time if Mr. Epstein had placed the string around his own neck" regarding the July 23 incident

### 6.7 What the Files Do NOT Show

**The OCME ruling stands.** The New York City Office of the Chief Medical Examiner ruled Epstein's death a suicide by hanging. No document in the corpus contradicts this ruling with contrary forensic evidence. The inmate observation, camera failures, and missed rounds describe institutional failures, not proof of foul play.

**The questions are procedural, not forensic.** The unresolved issues are: Why was the cellmate not replaced? Why was the phone call unmonitored? Who answered the 347 number? Why were the DVR failures not repaired? Why were 16 death investigation documents removed? These are questions about institutional failure and transparency, not murder evidence.

**The conspiracy theories outrun the documents.** Multiple conspiracy theories circulate about Epstein's death. The available documents describe a cascade of institutional failures at a facility with known systemic problems. The [OIG investigation](https://oig.justice.gov/reports/investigation-and-review-federal-bureau-prisons-custody-care-and-supervision-jeffrey) found "numerous and serious failures" but did not conclude foul play. ([CBS](https://www.cbsnews.com/news/jeffrey-epsteins-suicide-justice-dept-watchdog-report-finds/), [NPR](https://www.npr.org/2023/06/27/1184380805/jeffrey-epstein-suicide-department))

Further reading: [Death Investigation Document Removal](https://epstein-data.com/reports/institutional/DEATH_INVESTIGATION_DOCUMENT_REMOVAL.html)

---

# SECTION 7: THE COVER-UP QUESTION

## What's Missing and Why It Matters

This section documents the structural pattern of non-investigation. Not a conspiracy. Not a theory. A documented pattern of decisions, at every level, that resulted in less accountability rather than more. These decisions may reflect bureaucratic dysfunction, resource constraints, institutional inertia, or something worse. The documents present the pattern. The reader decides what explains it.

### 7.1 The 2007 Non-Prosecution Agreement

The NPA, negotiated between Epstein's defense team and U.S. Attorney Alexander Acosta's office, is one of the most extraordinary plea agreements in federal criminal history. The Miami Herald's [2018 "Perversion of Justice" series](https://www.miamiherald.com/news/local/article220097825.html) by Julie K. Brown first brought widespread public attention to the NPA's terms.

**The deal:**
- Epstein pleaded guilty to two state prostitution charges (not federal trafficking charges)
- Served 13 months in a private wing of the Palm Beach County jail with daily work-release privileges (12 hours per day, 6 days per week outside the jail)
- **Named co-conspirators** (Kellen, Marcinkova, Groff, and others) received blanket immunity from federal prosecution
- Victims were not notified of the agreement, violating their rights under the [Crime Victims' Rights Act](https://www.law.cornell.edu/uscode/text/18/3771)
- The immunity clause was later expanded by prosecutors beyond its original scope

**How it happened.** Epstein assembled what Acosta himself described as "an army of legal superstars" — Harvard professor Dershowitz, former Whitewater independent counsel Kenneth Starr, Kirkland & Ellis partner Jay Lefkowitz, and several former prosecutors. ([EFTA00009116](https://epstein-data.com/EFTA00009116), p. 396)

Kirkland & Ellis argued "there is insufficient evidence that Mr. Epstein targeted minors" and that victims "lied to Mr. Epstein about their ages." ([EFTA00013811](https://epstein-data.com/EFTA00013811)) Dershowitz personally threatened Acosta: "I might be personally embarrassed by pursuing this matter, because I would be the subject of a chapter in a book on prosecutorial overreach." ([EFTA00009116](https://epstein-data.com/EFTA00009116), p. 391)

**The co-conspirator immunity clause was not in the original draft.** It was proposed by Epstein's defense and gradually expanded. Acosta testified he did not "recall focusing on the coconspirator provision" and speculated that "whether some of his employees go to jail, or other, lesser involved, is not the focus of this." ([EFTA00009016](https://epstein-data.com/EFTA00009016), pp. 285, 289-290)

The 11th Circuit Court of Appeals later found it "highly unusual — never seen before — that the government would extend federal immunity to Epstein's co-conspirators" who "had not cooperated or assisted the government." "The sole consideration for their federal immunity was that Epstein plead to two state charges." ([EFTA00073493](https://epstein-data.com/EFTA00073493) — [*In re Wild*, 955 F.3d 1196](https://media.ca11.uscourts.gov/opinions/pub/files/201913843.enb.pdf))

**The concealment.** After the NPA was signed, prosecutors and Epstein's lawyers negotiated whether to tell the victims — itself "a deviation from the Government's standard practice." On January 10, 2008, victims received letters stating the case was "currently under investigation" and requesting "continued patience" — despite the NPA already being signed. Judge Marra found: "the Government chose to conceal the existence of the NPA from the victims" and "spent untold hours negotiating the terms and implications of the NPA with Epstein's attorneys" while "scant information was shared with victims." ([EFTA00010507](https://epstein-data.com/EFTA00010507), pp. 9, 16, 28)

**The Main Justice appeal.** The defense team appealed directly to the Deputy Attorney General's office, creating a parallel review that stalled prosecution. After months of delay, the DAG wrote: "We do not believe such intervention is warranted here. Even if we were to substitute our judgment for that of the U.S. Attorney, we believe that federal prosecution of this case is appropriate." ([EFTA00013555](https://epstein-data.com/EFTA00013555)) Even Main Justice said to prosecute. It didn't matter.

**The OPR finding.** The DOJ Office of Professional Responsibility concluded Acosta exercised "poor judgment" but did not commit "professional misconduct." OPR found "no evidence that Acosta's decision was based on corruption or other impermissible considerations, such as Epstein's wealth, status, or associations" while finding the victims "were not treated with the forthrightness and sensitivity expected by the Department." ([EFTA00095558](https://epstein-data.com/EFTA00095558))

**The state plea.** During the state plea hearing, Epstein's counsel stated on the record: "there is a nonprosecution agreement with the United States Attorney's office that triggers as a result of this plea agreement." SDNY prosecutors later flagged this: "Check out pages 38-39 of his state plea." ([EFTA00027590](https://epstein-data.com/EFTA00027590), pp. 38-39)

The NPA is the foundational document. Everything that follows — the unsearched computer, the unprocessed devices, the halted state investigations — flows from a system in which federal prosecution was traded for a county jail sentence with work release.

Further reading: [Prosecution Failures Analysis](https://epstein-data.com/reports/institutional/PROSECUTION_FAILURES_ANALYSIS.html), [Grand Jury Subpoena Analysis](https://epstein-data.com/reports/pqg_lines_of_investigation/INDEX.html)

### 7.2 The 2005 Computer: Never Searched

When Palm Beach Police executed a search warrant at 358 El Brillo Way in October 2005, they seized computers. Investigator Dave Kleiman created forensic images on 16 DVDs. Those DVDs were subpoenaed by the grand jury (subpoenas OLY-63 and OLY-64). The grand jury never received them. After the NPA, no legal authority existed to search the 2005 computer forensic images. They remain unexamined.

Additionally, three computers were physically removed from the El Brillo Way residence 13 days before the search warrant was executed — October 7, 2005.

### 7.3 The Device Processing Catastrophe

After Epstein's 2019 arrest, the FBI seized over 70 digital devices from his New York mansion and USVI properties, including:
- 40+ storage devices (hard drives, USBs, SD cards)
- 60+ CDs
- 25+ devices from Little St. James Island (including servers and server racks)
- The critical Epstein iPhone (1B71, IMEI 357201093322785)

The processing was catastrophic:
- 17+ months of delays between seizure and usable production to prosecutors
- 71,000+ zero-byte (empty) files in initial productions
- The FBI CART examiner was reduced to **1 day per week** during COVID, stretching timelines by "a factor of 5"
- Server hard drives physically failed, requiring FBI HQ data recovery specialists
- Prosecutors could not match folders to devices — no standardized tracking system existed
- Evidence review was still ongoing as of April 2025, six years after seizure

Over 1 million images and videos were extracted from the devices. Of these, approximately 34,000 were marked responsive (85 GB). 15-20 images were identified as CSAM (commercial, not self-produced). Approximately 90% was adult pornography/erotica. No videos of sexual abuse were identified "at any point in the investigation" ([EFTA00164742](https://epstein-data.com/EFTA00164742)).

### 7.4 The Intelligence Thread

The FBI's Epstein investigation was not one case. It was at least nine case numbers across two parallel tracks:

**Criminal track (well-known):**

| Case | Type | Opened |
|------|------|--------|
| 31E-MM-108062 | Child sex trafficking, Miami | July 2006 |
| 72-MM-113327 | Obstruction of justice | October 2009 |
| 50D-NY-3027571 | Sex trafficking, SDNY | December 2018 |
| 90A-NY-3151227 | Death investigation | August 2019 |

**Intelligence track (unreported):**

| Case | Type | Field Office | First Seen |
|------|------|-------------|-----------|
| 813B-NY-2928278 | Foreign intelligence program | New York | December 2017 |
| 804I-LA-3315657-INTELPRODS | Election influence assessment | Los Angeles | October 2020 |
| 804I-DL-5089795 | VCAC assessment | Dallas | August 2019 |
| 804I-NY-304798-INTELPRODS | Human trafficking intelligence | New York | October 2019 |
| 804I-SJ-3371215 | TOC assessment | San Juan | July 2021 |

Plus: a fully redacted case initiated September 8, 2020, and INTELPRODS sub-files under both the Miami and New York criminal cases producing 12 Tactical Intelligence Reports at SECRET//NOFORN classification.

The 813B case was filed 18 months before the public SDNY criminal investigation opened. Classification 813 designates the FBI's Foreign Intelligence Program. The handling unit was Intelligence Division Squad ID 25, not a criminal squad. The declassification date is 2042. No outlet has reported on this architecture.

Further reading: [FBI Intelligence Investigations](https://epstein-data.com/reports/intelligence/FBI_INTELLIGENCE_INVESTIGATIONS.html)

### 7.5 Document Removal: 64,259 Pages

Approximately 64,259 documents were removed from justice.gov after the initial January 30, 2026 publication. The removals are concentrated in Dataset 9, which contains the FBI's investigative files. No Federal Register notice has been published. No congressional notification has been made. The removal pattern was first reported by [Sollenberger](https://sollenbergerrc.substack.com/p/doj-removed-record-of-multiple-fbi) and confirmed by [NPR](https://www.npr.org/2026/02/24/nx-s1-5723968/epstein-files-trump-accusation-maxwell).

Among the removed documents:
- The FBI's complete death investigation file (476 pages)
- BOP operational logs from Epstein's unit (1,395 pages)
- The BOP Psychological Reconstruction (since restored)
- FBI financial records for Epstein-linked shell entities
- Grand jury materials

The DOJ's stated explanation accounts for victim PII removals and Maxwell protective order material — roughly 16,500 documents. The remaining ~48,000 removals have no published justification.

Further reading: [Document Removal Audit](https://epstein-data.com/reports/institutional/DOJ_DOCUMENT_REMOVAL_AUDIT.html)

### 7.6 Document Alteration: 42,782 Files Modified

After publication, the DOJ re-processed 42,782 documents, making 152,312 classified changes:
- **2.6%** were defensible victim PII redactions
- **46.9%** were content removal (substantive text removed with no PII basis)
- **27,026 pages** had their searchable text layer degraded (content visible on page but invisible to keyword search)
- **150+ FinCEN Suspicious Activity Reports** were gutted of banking intelligence
- **1,452,264 characters** were degraded from Maxwell's American Express statements — already public trial exhibits

The DOJ's Attorney Review Protocol reveals the mechanism: a dual-track system where Track 1 covers victim PII (as authorized by the EFTA) and Track 2 invokes the Privacy Act to strip telephone numbers, government employee names, and other PII from all persons — an authority not enumerated in the [EFTA's five permitted exceptions](https://www.congress.gov/bill/119th-congress/house-bill/4405).

Further reading: [Alteration Forensics](https://epstein-data.com/reports/institutional/DOJ_DOCUMENT_ALTERATION_FORENSICS.html)

### 7.7 The 1.46 Million Withheld Pages

Secondary Bates stamps on the released pages reveal that 2.48 million pages were reviewed and numbered before the production was finalized. Only 1.04 million were released. The FBI's device extraction stream withheld 57% of reviewed pages. SDNY's investigative file stream withheld 74.9%.

240,799 gaps exist in the R1 numbering sequence alone. The majority are 1-5 pages (consistent with individual emails or short threads removed during review), but 18 gaps exceed 2,000 consecutive pages each, and the largest single gap is 19,937 consecutive pages. The withholding rate is uniform across the entire R1 corpus.

Possible explanations include attorney-client privilege, grand jury secrecy (Rule 6(e)), deduplication, material outside production scope, protective order restrictions, and law enforcement sensitivity. No explanation has been published.

Further reading: [Secondary Bates Stamp Analysis](https://epstein-data.com/reports/institutional/SECONDARY_BATES_STAMP_ANALYSIS.html)

### 7.8 Zorro Ranch: SDNY Ordered New Mexico to Halt

In July 2019, SDNY instructed the New Mexico Attorney General's office to "cease any investigation into sex trafficking" at Epstein's Zorro Ranch. The agreement, documented in a 10-page email chain ([EFTA00019183](https://epstein-data.com/EFTA00019183)), required New Mexico to hand over all materials and defer to federal prosecutors.

One month later, Epstein was dead. The federal case died with him.

SDNY never returned any information to New Mexico as promised. As of May 2021, the NM U.S. Attorney's office was still seeking SDNY's permission before making public statements about Epstein matters in their own jurisdiction.

No search warrant was executed at Zorro Ranch until March 10, 2026 — nearly seven years after Epstein's death — when NM Attorney General Raúl Torrez finally conducted a search. ([NBC News](https://www.nbcnews.com/politics/politics-news/jeffrey-epstein-new-mexico-ranch-state-investigation-rcna262724), [Albuquerque Journal](https://www.abqjournal.com/news/feds-asked-new-mexico-to-halt-its-epstein-probe/2990694))

Further reading: [Zorro Ranch Investigation Halt](https://epstein-data.com/reports/institutional/ZORRO_RANCH_INVESTIGATION_HALT.html)

### 7.9 What This Does NOT Prove

The pattern documented above is real and documented: the NPA immunity, the unsearched computer, the device processing failure, the parallel intelligence track, the document removals, the alterations, the withheld pages, the halted state investigation. Every claim is sourced to specific EFTA numbers or external reporting.

What this pattern does not prove is conspiracy. Each individual failure has a plausible bureaucratic explanation:

- The NPA was aggressive defense lawyering meeting a willing prosecutor
- The 2005 computer was not searched because legal authority expired with the NPA
- Device processing was slow because of COVID and understaffing
- Document removals may reflect a genuine (if overbroad) attempt to protect victim privacy
- The intelligence track may be standard practice for cases with foreign connections
- The Zorro Ranch halt may reflect legitimate concerns about parallel investigations contaminating witness testimony

The question is whether the cumulative weight of these failures, all running in the same direction, all resulting in less accountability rather than more, can be adequately explained by coincidence and bureaucracy. That is a question for Congress, not for this document.

---

# SECTION 8: THE REPORTING LANDSCAPE

## Who's Covering This and What They've Found

The Epstein files story is being reported in three distinct layers: **mainstream outlets** (names and politics), **beat reporters** (document analysis), and **citizen journalists** (reading everything). The gaps between these layers are where the unreported stories live.

### 8.1 Roger Sollenberger — The Daily Beast / Substack

**Roger C. Sollenberger** is a senior political reporter at The Daily Beast who launched an independent Substack (sollenbergerrc.substack.com) focused on EFTA analysis in February 2026. His serial-number-based methodology for identifying removed documents was independently verified by NPR and triggered a bipartisan congressional investigation within 24 hours.

**Key pieces:**

| Date | Title | Outlet |
|------|-------|--------|
| Feb 15 | FBI Interviewed Trump Accuser, Epstein Files Show | [Substack](https://sollenbergerrc.substack.com/p/fbi-interviewed-trump-accuser-epstein) |
| Feb 18 | DOJ Removed Record of Multiple FBI Interviews with Underage Trump Accuser | [Substack](https://sollenbergerrc.substack.com/p/doj-removed-record-of-multiple-fbi) |
| Feb 20 | DOJ Deleted Record Revealing That Maxwell Holds Potential Blackmail Over Trump | [Substack](https://sollenbergerrc.substack.com/p/doj-deleted-record-revealing-that) |
| Feb 24 | DOJ Exposed Name of Trump Underage Accuser After She "Refused To Cooperate" | [Substack](https://sollenbergerrc.substack.com/p/doj-exposed-name-of-trump-underage) |
| Mar 11 | On Trump Accuser Files, DOJ Establishes Pattern of Obstruction | [Substack](https://substack.com/@sollenbergerrc/note/p-190677003) |
| Feb 2026 | Bombshell Epstein File Reveals FBI Interviewed Underage Trump Accuser | [Daily Beast](https://www.thedailybeast.com/fbi-interviewed-underage-trump-accuser-bombshell-epstein-file-reveals/) |
| Feb 2026 | DOJ Cornered on Epstein Files' Missing Donald Trump Bombshells | [Daily Beast](https://www.thedailybeast.com/doj-cornered-on-epstein-files-missing-donald-trump-bombshells/) |

Sollenberger's focus is primarily political: the Trump-related document removals, the underage accuser FBI interviews, and the DOJ's selective withholding pattern. His serial-number methodology is sound and parallels the broader secondary Bates stamp analysis, though his scope is narrower (focused on specific individuals rather than the structural production gaps).

### 8.2 Stephen Fowler — NPR

NPR's reporting has focused on the institutional story: DOJ compliance with the statute, the removal pattern, and congressional responses. Fowler independently verified Sollenberger's 53-page gap and connected it to the broader pattern of DOJ non-compliance. NPR's February 24, 2026 piece ([link](https://www.npr.org/2026/02/24/nx-s1-5723968/epstein-files-trump-accusation-maxwell)) was among the most thorough on the removal story.

### 8.3 Ellie Leonard — Citizen Journalist

**Ellie Leonard** runs "The Panicked Writer" on Substack (ellieleonard.substack.com). A New Jersey mother of four with a background in classics and transcription, Leonard has read every published Epstein email in the EFTA corpus. The AP/Washington Times profiled her as one of the leading citizen journalists on the files ([Feb 23, 2026](https://www.washingtontimes.com/news/2026/feb/23/epstein-files-tackled-citizen-sleuths-citizen-journalists-help/)).

Leonard publishes frequently (sometimes multiple posts daily), mixing written analysis, live video, and podcast episodes. She has produced 35+ Epstein-focused pieces since September 2025, including:

- **"Epstein Files Breakdown"** — Volume-by-volume walkthroughs of each dataset release
- **"Decoding an Unknown Survivor's Journal"** (3 parts, Feb 2026) — Close reading of a victim document
- **"The Epstein Birthday Book (Transcribed)"** (5+ parts) — Full transcription of Epstein's birthday album
- **"The Epstein-Bannon Emails"** (3 parts, 2018 + 2019) — Deep read of the Bannon correspondence
- **"SPECIAL REPORT: What Everyone Is Missing About The Epstein Files"** (Jan 29, 2026) — Structural analysis
- **"The Missing FBI Interviews"** (Mar 6, 2026, with Wajahat Ali) — Covers the 302 gap

Regular collaborators: Wajahat Ali (The Left Hook), Jim Acosta, Glenn Kirschner, Gen. Mark Hertling, Narativ. ([Left Hook feature: "Ellie Leonard Read EVERY Epstein Email"](https://thelefthook.substack.com/p/ellie-leonard-read-every-epstein))

### 8.4 Major Outlets

**Bloomberg** — Two landmark pieces: the pre-release 18,000-email investigation ([Sep 2025](https://www.bloomberg.com/features/2025-jeffrey-epstein-emails-the-network/)) and "The Leon Black Files" ([Feb 13, 2026](https://www.bloomberg.com/news/features/2026-02-13/the-leon-black-files-epstein-was-a-fixer-for-billionaire-s-deepest-secrets)). Also covering the BofA trial (Bloomberg Law).

**New York Times** — CBP corruption series (Routch and additional officers, Feb 19-20). Institutional failure angle. Thorough enough that further CBP reporting has limited value-add.

**CNN** — Bannon-Epstein relationship, Italian connections, arrest coverage (Andrew, Mandelson). Live coverage of major depositions.

**Reuters** — Deutsche Bank team identification (Stewart Oldfield, Feb 2026).

**CNBC / CBS / NBC** — Congressional deposition coverage (Wexner, Kahn, Clintons), legal proceedings, arrest coverage.

### 8.5 International Press

**UK:** The Prince Andrew arrest (Feb 19) and Peter Mandelson arrest (Feb 23) generated massive coverage across the Guardian, Telegraph, BBC, Sky News, and tabloids. The UK angle is the most active international investigation, with Thames Valley Police and the Metropolitan Police both conducting misconduct-in-public-office inquiries.

**France:** Mediapart, France 24, and the Art Newspaper are covering the active criminal investigation into Jean-Luc Brunel's associates — specifically the Prytanee gallery network, David Binant, and former Culture Minister Jack Lang.

**Italy:** Fanpage, Open.online, and Il Foglio reported on the Teodorani-Fabbri/Elkann connections. The "Master" correspondence and the "new target" language about the Elkann family received significant Italian press attention.

**Al Jazeera:** Comprehensive tracker of arrests, resignations, and legal proceedings across all jurisdictions.

### 8.6 The Gaps

The gap between what has been reported and what the corpus contains is enormous. The celebrity-name stories get covered. The structural findings do not. Ten significant corpus findings that have received zero or minimal media attention:

1. **The parallel FBI intelligence architecture** (9+ case numbers, SECRET//NOFORN, seven field offices, 12 TIRs)
2. **HBRK Associates** ($84.5M, 35,919 documents, operational hub)
3. **helpfulexperts.com** (first grand jury subpoena July 2017, 17 months before public investigation)
4. **47 missing victim 302 interviews** (29.4% of known FBI interviews absent)
5. **853 deleted phone record pages**
6. **Dr. Steven Victor / "Dr. Evil"** (free cosmetic treatment pipeline for young women)
7. **The "MacGyver" correction** (Brafman, not Trump — 15 emails + Bannon iMessage)
8. **The full alteration scale** (42,782 documents, only 2.6% for victim privacy)
9. **The deference dynamic** (SDNY controlling all parallel investigations 2019-2021)
10. **The 2005 computer** (forensic images on 16 DVDs, grand jury subpoenas, never searched)

---

# SECTION 9: OPEN THREADS

## Eleven Threads Nobody Has Pulled Yet

Each thread below includes: what the evidence shows, which documents contain it, who the characters are, why it hasn't been reported, and what it would take to produce.

---

### Thread 1: HBRK Associates — $84.5 Million, 35,919 Documents

**The evidence:** HBRK Associates, Inc., managed by Richard Kahn, controlled $84.5 million in managed accounts and generated more documents than any entity other than Epstein himself. The entity served as the operational hub for Epstein's post-prison financial architecture, managing 39+ sub-entities, construction operations, and trust administration. The trust agreement's Section 2.5 contained a lock-in clause making Kahn's termination nearly impossible.

**The characters:** Richard Kahn (manager), Emad Hanna (key operator), Darren Indyke (co-executor)

**Why unreported:** The name "Kahn" and "HBRK" have been mentioned in passing (Daily Beast 2021, Business Insider Nov 2025), but no outlet has reported on the $84.5M figure, the trust lock-in, the construction operations, or the full operational architecture.

**What it would take:** Subpoena Kahn's financial records through House Oversight. He's already under subpoena.

---

### Thread 2: helpfulexperts.com — The First Grand Jury Subpoena

**The evidence:** The SDNY grand jury issued subpoena Case 2017R00550 in July 2017 — a wire fraud investigation — 17 months before the publicly reported December 2018 opening of the trafficking case. The subpoena targeted helpfulexperts.com, a domain that has been registered for 19 years with zero internet footprint. No website, no social media, no press mention — ever. The domain was still maintained as recently as December 2025.

**Why unreported:** Zero media coverage. The document is in the corpus but buried among hundreds of thousands of legal filings.

**What it would take:** WHOIS history, domain registrar subpoena, interview with the domain registrant.

---

### Thread 3: The Parallel Intelligence Architecture

**The evidence:** See Section 7.4 above. Nine case numbers, two tracks, seven field offices, 12 TIRs, a 2020 election influence assessment, SECRET//NOFORN classification.

**Why unreported:** Individual CHS claims (Israeli spy allegations, Italian hacker) have been widely reported. The architecture itself — the case numbers, the INTELPRODS sub-files, the 804I cases across field offices — has not been mapped by any outlet.

**What it would take:** Congressional request for classified briefing. Senate Intelligence Committee has jurisdiction.

---

### Thread 4: The 47 Missing Victim Interviews

**The evidence:** 160 FBI FD-302 interview records identified through serial numbering. 47 absent from production (29.4%). 86 audio recordings listed in FBI indices not present. 149 serials with zero published documents.

**Why unreported:** Requires cross-referencing FBI serial indices against the production — a technical exercise that no newsroom has done.

**What it would take:** FOIA request for the 47 identified missing serial numbers. Congressional demand for complete serial-level inventory.

---

### Thread 5: The Wanek Family — 14 Entities Under RM82289

**The evidence:** 14 separate Wanek family trusts, GRATs, and LLCs managed under the same Deutsche Bank relationship manager code as Epstein. The Wanek family founded Ashley Furniture Industries.

**Why unreported:** Partially covered in existing reporting on the RM82289 code, but the 14-entity cluster and combined balances have not been reported.

**What it would take:** Deutsche Bank subpoena through Senate Banking Committee.

---

### Thread 6: Frederic Fekkai — The Grooming Pipeline

**The evidence:** 3,534 pages, 3,067 documents. "Can we find some girls for him?" Roberts sent to his salon. Lived in Epstein apartment. Decade of email correspondence.

**Why unreported:** Fekkai's name appeared in Maxwell deposition excerpts but the depth of corpus evidence (direct solicitation language, salon visits as grooming, apartment dependency) has not been reported.

**What it would take:** Full corpus read of 3,067 documents, interview with Fekkai.

---

### Thread 7: The 853 Deleted Phone Record Pages

**The evidence:** DS9 and DS10 contain 853 "Deleted Page" sheets where phone records should be. DS12's 582-page case file lists every carrier subpoenaed: Cingular, T-Mobile, Sprint, BellSouth, MetroPCS, Verizon, AT&T.

**Why unreported:** Requires matching carrier subpoenas to deleted page sheets — a database exercise.

**What it would take:** FOIA for the deleted phone records. Congressional demand under EFTA authority.

---

### Thread 8: Maxwell Post-2019 Finances

**The evidence:** After Epstein's death and before her arrest, Maxwell purchased a New Hampshire property ("Tuckedaway") through Scott Borgerson (former CEO of CargoMetrics). The EFTA corpus documents the period before; the post-2019 financial picture — how Maxwell funded herself — is a gap.

**Why unreported:** Falls outside the EFTA production's timeframe.

**What it would take:** Financial records subpoena, Borgerson/CargoMetrics investigation, real estate transaction analysis.

---

### Thread 9: The Surveillance Tapes — "ITEM WAS NOT SCANNED"

**The evidence:** Evidence logs in the corpus reference surveillance tapes, DVRs, and recording equipment seized from Epstein's properties. Multiple items are marked "ITEM WAS NOT SCANNED." The FBI confirmed no sexual abuse videos were found "at any point in the investigation," but 2,100 nude/partially nude images were found, and the processing of evidence was ongoing as of April 2025.

**Why unreported:** The "no sexual abuse videos" finding was widely reported. The "ITEM WAS NOT SCANNED" notations and the 6-year processing timeline have not been.

**What it would take:** FOIA for complete evidence processing logs. Congressional demand for device-by-device accounting.

---

### Thread 10: The Storage Units

**The evidence:** Seven commercial storage facilities across FL/NY/NJ. Three computers removed from 358 El Brillo Way 13 days before the search warrant. Forensic images created by Dave Kleiman (known in cryptocurrency circles as a candidate for the Satoshi Nakamoto identity). Maxwell maintained 3+ units at Extra Space Storage in River Edge, NJ (~$1,200/month). UOVO climate-controlled art storage. A court preservation order explicitly covered "any evidence stored in Defendant's storage unit."

**Why unreported:** Telegraph, ABC News, and Palm Beach Post broke the basic story (Feb 2026). The Maxwell NJ units, specific addresses, Kleiman connection, preservation order, and UOVO art storage remain unreported.

**What it would take:** Storage facility subpoenas. Florida lien law creates urgency — unpaid units may have been liquidated.

---

### Thread 11: The 2005 Computer

**The evidence:** Palm Beach PD created forensic images on 16 DVDs during the 2005 investigation. Grand jury subpoenas OLY-63 and OLY-64 demanded the images. The grand jury never received them. The NPA extinguished the legal authority to search them. They remain unexamined 20+ years later.

**Why unreported:** The existence of the 2005 computer evidence has been mentioned in passing, but the specific chain — forensic image, subpoena, non-delivery, NPA destruction of authority — has not been fully reported.

**What it would take:** Congressional authorization for examination. The DVDs may still be in FBI evidence custody.

---

# APPENDIX A: 50 KEY DOCUMENTS

## A Producer's Hit List

*Each entry: EFTA number, direct link, one-line description, which section covers it.*

| # | EFTA | Description | Section |
|---|------|-------------|---------|
| 1 | [EFTA00027019](https://epstein-data.com/EFTA00027019) | Deutsche Bank master transaction tables (Exhibits A-E) | 3.1, 3.2 |
| 2 | [EFTA02731737](https://epstein-data.com/EFTA02731737) | Manhattan DA: "do not doubt her allegations against JE and LB" | 3.3 |
| 3 | [EFTA00011437](https://epstein-data.com/EFTA00011437) | Prince Andrew from Balmoral: "new inappro[priate friends]" | 5, Prince Andrew |
| 4 | [EFTA02335012](https://epstein-data.com/EFTA02335012) | Maxwell: "2 legged sight seeing" to "The Invisible Man" | 5, Prince Andrew |
| 5 | [EFTA00041963](https://epstein-data.com/EFTA00041963) | BOP Psychological Reconstruction (1,000 pages) — Epstein's final weeks | 6.3, 6.6 |
| 6 | [EFTA00132208](https://epstein-data.com/EFTA00132208) | FBI death investigation 302s — witness interviews | 6.4 |
| 7 | [EFTA00164742](https://epstein-data.com/EFTA00164742) | FBI to Director Patel: "no videos of any sexual abuse identified at any point" | 7.3 |
| 8 | [EFTA00164855](https://epstein-data.com/EFTA00164855) | MCC: 147 cameras, 8.08 TB, SHU cameras not active | 6.2 |
| 9 | [EFTA00019183](https://epstein-data.com/EFTA00019183) | SDNY-DNM email chain: "they agreed to cease any investigation" | 7.8 |
| 10 | [EFTA01683874](https://epstein-data.com/EFTA01683874) | 813B-NY-2928278: FBI foreign intelligence FD-1023 (December 2017) | 7.4 |
| 11 | [EFTA00090314](https://epstein-data.com/EFTA00090314) | CHS FD-1023: "belonged to both U.S. and allied intelligence services" (UNVERIFIED) | 5, Barak |
| 12 | [EFTA00038465](https://epstein-data.com/EFTA00038465) | CART evidence log — complete seized device inventory | 7.3 |
| 13 | [EFTA00339454](https://epstein-data.com/EFTA00339454) | Groff scheduling email — the smoking gun alteration example | 7.6 |
| 14 | [EFTA01779967](https://epstein-data.com/EFTA01779967) | Dr. Victor: "$20k on your group of friends" free treatment arrangement | 5, Dr. Evil |
| 15 | [EFTA01991050](https://epstein-data.com/EFTA01991050) | "Dr. Evil" = "Victor" same-day identification | 5, Dr. Evil |
| 16 | [EFTA01615580](https://epstein-data.com/EFTA01615580) | Bannon iMessage: "Ben" / Brafman discussed re Weinstein | 5, MacGyver |
| 17 | [EFTA02446582](https://epstein-data.com/EFTA02446582) | "Macgiver loves representing misogynists" | 5, MacGyver |
| 18 | [EFTA01660651](https://epstein-data.com/EFTA01660651) | FBI tip: Alexander brothers, rape at Epstein parties | 5, Alexander Brothers |
| 19 | [EFTA00184128](https://epstein-data.com/EFTA00184128) | FBI victim tracking matrix — 23 victims, 40 pages | 4.1 |
| 20 | [EFTA02857524](https://epstein-data.com/EFTA02857524) | Operation Leap Year prosecution memo (DS12 expansion) | 1.5 |
| 21 | [EFTA02857863](https://epstein-data.com/EFTA02857863) | 582-page FBI case file — complete serial index | 1.5 |
| 22 | [EFTA00061927](https://epstein-data.com/EFTA00061927) | Congressional OIG interview: "a man answered" the phone call | 6.3 |
| 23 | [EFTA00115642](https://epstein-data.com/EFTA00115642) | OIG witness: "It could have potentially led to the incident" | 6.3 |
| 24 | [EFTA00109863](https://epstein-data.com/EFTA00109863) | BOP incident report — discovery of body, medical response | 6.4 |
| 25 | [EFTA00120887](https://epstein-data.com/EFTA00120887) | TRUINTEL operational logs — SHU daily operations | 6.2 |
| 26 | [EFTA01656152](https://epstein-data.com/EFTA01656152) | "Prominent Names" document — Trump, Weinstein, Staley, Black, Andrew | 3.3 |
| 27 | [EFTA02731082](https://epstein-data.com/EFTA02731082) | 60+ page victim interview: "lent out," Weinstein connection | 4 |
| 28 | [EFTA02730741](https://epstein-data.com/EFTA02730741) | Reference to 7 discs of "consensually monitored phone calls" | 1.4 |
| 29 | [EFTA00164939](https://epstein-data.com/EFTA00164939) | FBI briefing deck showing all four criminal case numbers | 7.4 |
| 30 | [EFTA00101065](https://epstein-data.com/EFTA00101065) | FBI device search warrant — email target list (Prince Andrew aliases) | 5, Prince Andrew |
| 31 | [EFTA01266403](https://epstein-data.com/EFTA01266403) | Epstein's will — loan forgiveness for Victor, Shuliak | 5 |
| 32 | [EFTA02332233](https://epstein-data.com/EFTA02332233) | "Andrew sweet heart" — Maxwell to Prince Andrew | 5 |
| 33 | [EFTA00010968](https://epstein-data.com/EFTA00010968) | Guard indictment — Noel and Thomas | 6.1 |
| 34 | [EFTA00095558](https://epstein-data.com/EFTA00095558) | OPR Executive Summary — internal DOJ review | 7 |
| 35 | [EFTA01649074](https://epstein-data.com/EFTA01649074) | Sentinel File Review — CHS landscape map | 7.4 |
| 36 | [EFTA01659529](https://epstein-data.com/EFTA01659529) | FBI Albuquerque daily headlines — NM halt corroboration | 7.8 |
| 37 | [EFTA00157526](https://epstein-data.com/EFTA00157526) | Palm Beach PD burglary report — camera-in-clock practice (2003) | 7.3 |
| 38 | [EFTA01884983](https://epstein-data.com/EFTA01884983) | "dr steven victor. 57 st." — direct naming of Dr. Evil | 5 |
| 39 | [EFTA02664944](https://epstein-data.com/EFTA02664944) | "Similar mannerisms between Trump and McGyver" — the comparison email | 5 |
| 40 | [EFTA01620096](https://epstein-data.com/EFTA01620096) | "mr evil asked karyna whr ws the blonde girl" | 5 |
| 41 | [EFTA00025507](https://epstein-data.com/EFTA00025507) | Apollo Board review of Black-Epstein relationship | 3.3 |
| 42 | [EFTA00038690](https://epstein-data.com/EFTA00038690) | JPMorgan account ending in 5001 | 3.1 |
| 43 | [EFTA01682081](https://epstein-data.com/EFTA01682081) | Decision "not to sue Wexner" | 5, Wexner |
| 44 | [EFTA00174673](https://epstein-data.com/EFTA00174673) | FBI 266N — Black Book on extremist Telegram channels | 7.4 |
| 45 | [EFTA01310387](https://epstein-data.com/EFTA01310387) | Most comprehensively redacted document (7,988 redactions) | 1.4 |
| 46 | [EFTA02731473](https://epstein-data.com/EFTA02731473) | Leon Black HT investigation file (start of ~50 doc series) | 3.3 |
| 47 | [EFTA00601154](https://epstein-data.com/EFTA00601154) | Dershowitz: "Ben Brafman... volunteered to help me" | 5, MacGyver |
| 48 | [EFTA01873297](https://epstein-data.com/EFTA01873297) | Teodorani: "Hi master" — the "Master" codename | 5 |
| 49 | [EFTA01619031](https://epstein-data.com/EFTA01619031) | Teodorani iMessage: "Master the airport is Ciampino" + Prince Borghese | 5 |
| 50 | [EFTA00163686](https://epstein-data.com/EFTA00163686) | FBI one-page death investigation timeline (removed from justice.gov) | 6.5 |

---

# APPENDIX B: TIMELINE

## 1987–2026: From Wexner to the Files

| Date | Event | Source |
|------|-------|--------|
| **1987** | Les Wexner grants Epstein power of attorney over personal finances | Public reporting; corpus docs |
| **~1989** | Wexner transfers East 71st Street mansion to Epstein | Property records |
| **1991** | Ghislaine Maxwell begins relationship with Epstein | Trial testimony |
| **1996** | Jean-Luc Brunel founds MC2 Model Management with Epstein backing | Court filings |
| **1999** | First documented victim contact (per FBI timeline reconstructions) | DS9 302s |
| **Aug 2001** | Prince Andrew emails Maxwell from Balmoral: "Have you found me some new inappro..." | [EFTA00011437](https://epstein-data.com/EFTA00011437) |
| **2002** | Bill Clinton Africa trip on Epstein aircraft | Flight records, scheduling docs |
| **2003** | Palm Beach PD burglary report documents camera-in-clock in Epstein home | [EFTA00157526](https://epstein-data.com/EFTA00157526) |
| **Mar 2005** | Palm Beach Police Department opens investigation after victim report | Police records |
| **Oct 7, 2005** | Three computers removed from 358 El Brillo Way — 13 days before search warrant | Storage units report |
| **Oct 20, 2005** | PBPD executes search warrant; seizes computers; Dave Kleiman creates forensic images | DS12 case file |
| **Jul 24, 2006** | FBI opens Miami investigation (31E-MM-108062) | [EFTA00164939](https://epstein-data.com/EFTA00164939#page=3) |
| **2006-2007** | Federal grand jury convened; Operation Leap Year prosecution memos drafted | [EFTA02857524](https://epstein-data.com/EFTA02857524) |
| **Sep 2007** | Non-Prosecution Agreement signed; blanket immunity for co-conspirators | [Miami Herald](https://www.miamiherald.com/news/local/article220097825.html) |
| **2008-2009** | Epstein serves 13 months in Palm Beach County jail with work release | [Miami Herald](https://www.miamiherald.com/news/local/article220097825.html) |
| **May 2009** | Earliest Epstein personal email in corpus (jeevacation@gmail.com) | DS10/DS11 |
| **Oct 2009** | FBI opens obstruction case (72-MM-113327) | [EFTA00164939](https://epstein-data.com/EFTA00164939#page=4) |
| **2012-2017** | Leon Black pays Epstein $158M+ | Financial records, Bloomberg |
| **2013** | JPMorgan drops Epstein; Deutsche Bank becomes primary bank | Banking records |
| **Aug 2013** | Deutsche Bank opens Epstein accounts under RM CODE 82289 | [EFTA00027019](https://epstein-data.com/EFTA00027019) |
| **2015-2018** | Epstein-Ruemmler correspondence ("MacGyver" exchanges) | DS11 emails |
| **Dec 13, 2017** | FBI foreign intelligence FD-1023 filed under 813B-NY-2928278 | [EFTA01683874](https://epstein-data.com/EFTA01683874) |
| **Jul 2017** | First SDNY grand jury subpoena (Case 2017R00550, wire fraud, helpfulexperts.com) | Grand jury records |
| **Dec 6, 2018** | FBI opens SDNY sex trafficking case (50D-NY-3027571) | [EFTA00164939](https://epstein-data.com/EFTA00164939#page=5) |
| **Jan 2019** | Bannon-Epstein iMessage: "Ben" (Brafman) discussed re Weinstein | [EFTA01615580](https://epstein-data.com/EFTA01615580) |
| **Jul 6, 2019** | Epstein arrested at Teterboro Airport; enters MCC at 9:24 PM | [EFTA00041963](https://epstein-data.com/EFTA00041963) |
| **Jul 18, 2019** | Bail denied; no psychological assessment conducted afterward | BOP records |
| **Jul 2019** | SDNY orders NM AG to halt Zorro Ranch investigation | [EFTA00019183](https://epstein-data.com/EFTA00019183) |
| **Jul 23, 2019** | First incident — "handmade orange rope" found around Epstein's neck; 31 hours on suicide watch | [EFTA00120887](https://epstein-data.com/EFTA00120887) |
| **Jul 29, 2019** | DVR2 system failure — "was not recording" | Death investigation docs |
| **Aug 8, 2019** | Two hard drives in DVR2 fail | Death investigation docs |
| **Aug 9, 2019** | Giuffre v. Maxwell documents unsealed; cellmate transferred, not replaced; unmonitored phone call (347 area code, "a man answered") | [EFTA00061927](https://epstein-data.com/EFTA00061927) |
| **Aug 10, 2019** | Epstein found dead at 6:33 AM; pronounced at 7:36 AM; OCME rules suicide | [EFTA00109863](https://epstein-data.com/EFTA00109863) |
| **Aug 12, 2019** | FBI opens death investigation (90A-NY-3151227) | [EFTA00164939](https://epstein-data.com/EFTA00164939#page=12) |
| **Nov 2019** | Guards Noel and Thomas indicted | [EFTA00010968](https://epstein-data.com/EFTA00010968) |
| **Jul 2020** | Maxwell arrested in New Hampshire | [NPR](https://www.npr.org/2020/07/02/886537383/fbi-arrests-ghislaine-maxwell-in-connection-to-jeffrey-epstein-case) |
| **Oct 2020** | FBI 804I-LA election influence assessment opened | [EFTA00090314](https://epstein-data.com/EFTA00090314) |
| **May 2021** | Guard deferred prosecution agreements | [NPR](https://www.npr.org/2021/05/22/999441586/jeffrey-epstein-guards-would-avoid-serving-jail-time-in-a-new-deal-with-prosecut) |
| **Dec 2021** | Maxwell convicted on 5 of 6 counts | [NPR](https://www.npr.org/2021/12/29/1066219689/ghislaine-maxwell-verdict-trial-jeffrey-epstein) |
| **Jan 2022** | Guard charges dismissed | [CNN](https://edition.cnn.com/2022/01/03/us/jeffrey-epstein-officers-dismissed-charges-judge) |
| **Feb 2022** | Jean-Luc Brunel found dead in Paris jail cell | [NPR](https://www.npr.org/2022/02/19/1081961087/jeffrey-epstein-jean-luc-brunel-dead) |
| **Jun 2022** | Maxwell sentenced to 20 years | [NPR](https://www.npr.org/2022/06/28/1107899156/ghislaine-maxwell-is-sentenced-to-20-years-in-prison) |
| **Jun 2023** | DOJ OIG publishes 127-page death investigation report | [OIG report](https://oig.justice.gov/reports/investigation-and-review-federal-bureau-prisons-custody-care-and-supervision-jeffrey) |
| **Apr 25, 2025** | Virginia Giuffre dies at 41 in Western Australia | [NPR](https://www.npr.org/2025/04/26/g-s1-62856/virginia-giuffre-has-died) |
| **Jul 15, 2025** | Epstein Files Transparency Act introduced (Khanna-Massie) | [Congress.gov](https://www.congress.gov/bill/119th-congress/house-bill/4405) |
| **Jul 24-25, 2025** | DAG Blanche interviews Maxwell at FCI Tallahassee | Public reporting |
| **Sep 2, 2025** | House Oversight releases 33,295 pages of Epstein estate records | House Oversight |
| **Sep 25, 2025** | Bloomberg obtains 18,000 Epstein emails (2005-2008) | [Bloomberg](https://www.bloomberg.com/features/2025-jeffrey-epstein-emails-the-network/) |
| **Oct 6, 2025** | Supreme Court declines Maxwell appeal — all options exhausted | [SCOTUSblog](https://www.scotusblog.com/2025/10/supreme-court-declines-to-hear-ghislaine-maxwells-appeal/) |
| **Oct 2025** | Prince Andrew stripped of all titles and honors | [PBS](https://www.pbs.org/newshour/world/andrew-windsor-officially-no-longer-a-prince-after-king-formally-strips-title-for-epstein-ties) |
| **Oct 16, 2025** | Bank of America and BNY sued by Epstein victims | [CNBC](https://www.cnbc.com/2025/10/16/bank-of-america-bny-sued-over-alleged-financial-ties-to-jeffrey-epstein.html) |
| **Nov 19, 2025** | Epstein Files Transparency Act signed into law | [Pub. L. 119-38](https://www.congress.gov/bill/119th-congress/house-bill/4405) |
| **Dec 19, 2025** | First DOJ release — bipartisan fury over redactions, victim names exposed | [NPR](https://www.npr.org/2025/12/20/nx-s1-5650758/epstein-files-doj-trump-photo), [Bloomberg](https://www.bloomberg.com/news/articles/2025-12-19/epstein-files-released-after-years-of-political-legal-acrimony) |
| **Jan 30, 2026** | Full DOJ release: ~3.5 million pages across 12 datasets | [DOJ](https://www.justice.gov/opa/pr/department-justice-publishes-35-million-responsive-pages-compliance-epstein-files) |
| **Jan 21, 2026** | Bipartisan contempt vote for Bill Clinton (9 Democrats vote yes) | [NPR](https://www.npr.org/2026/02/03/nx-s1-5697831/clintons-agree-testify-house-epstein-investigation-contempt-congress-vote) |
| **Feb 3, 2026** | Clintons capitulate, agree to testify under oath | [NPR](https://www.npr.org/2026/02/03/nx-s1-5697831/clintons-agree-testify-house-epstein-investigation-contempt-congress-vote) |
| **Feb 2026** | ~64,259 documents removed from justice.gov; 42,782 altered | Audit reports |
| **Feb 9-10, 2026** | Maxwell invokes Fifth before House Oversight; seeks Trump clemency | [NPR](https://www.npr.org/2026/02/10/g-s1-109413/maxwell-appeals-for-clemency) |
| **Feb 10, 2026** | Rep. Khanna reads six redacted names on House floor | [New Republic](https://newrepublic.com/post/206411/ro-khanna-reads-redacted-names-epstein-files-house-floor) |
| **Feb 10-11, 2026** | Commerce Secretary Lutnick admits 2012 island visit | [NPR](https://www.npr.org/2026/02/11/nx-s1-5708943/commerce-secretary-howard-lutnick-testifies-about-visiting-jeffrey-epsteins-island) |
| **Feb 13, 2026** | Bloomberg: "The Leon Black Files" | [Bloomberg](https://www.bloomberg.com/news/features/2026-02-13/the-leon-black-files-epstein-was-a-fixer-for-billionaire-s-deepest-secrets) |
| **Feb 15, 2026** | Sollenberger breaks underage Trump accuser / DOJ removal story | [Substack](https://sollenbergerrc.substack.com/p/fbi-interviewed-trump-accuser-epstein) |
| **Feb 18, 2026** | Wexner deposed by House Oversight (5 hours, New Albany OH) | [CNBC](https://www.cnbc.com/2026/02/18/jeffrey-epstein-les-wexner-deposition.html) |
| **Feb 19, 2026** | Prince Andrew arrested on his 66th birthday — misconduct in public office | [NBC](https://www.nbcnews.com/world/united-kingdom/former-prince-andrew-arrested-epstein-files-revelations-rcna259691) |
| **Feb 19-20, 2026** | NYT: CBP corruption — Routch and others | New York Times (paywall) |
| **Feb 23, 2026** | Peter Mandelson arrested — misconduct in public office | [CNN](https://www.cnn.com/2026/02/23/uk/peter-mandelson-arrested-gbr-intl) |
| **Feb 24, 2026** | NPR independently verifies 53-page gap; bipartisan congressional probe launched | [NPR](https://www.npr.org/2026/02/24/nx-s1-5723968/epstein-files-trump-accusation-maxwell) |
| **Feb 25, 2026** | House Oversight issues subpoenas to Kahn, Indyke | Congressional records |
| **Feb 26-27, 2026** | Hillary Clinton deposed (26th); Bill Clinton deposed (27th) — under oath | [NPR](https://www.npr.org/2026/02/03/nx-s1-5697831/clintons-agree-testify-house-epstein-investigation-contempt-congress-vote) |
| **~Mar 5, 2026** | DOJ silently expands DS12: 23 new documents, 1,046 pages | DOJ production |
| **Mar 10, 2026** | NM AG Torrez searches Zorro Ranch — first search, nearly 7 years after death | [CNN](https://www.cnn.com/2026/03/10/politics/epstein-zorro-ranch-search-new-mexico) |
| **Mar 11, 2026** | Richard Kahn deposed by House Oversight (7 hours), denies knowledge of crimes | [CBS](https://www.cbsnews.com/news/richard-kahn-jeffrey-epstein-house-oversight-testimony/) |
| **Mar 11, 2026** | Bipartisan Senate group requests GAO review of DOJ EFTA compliance | [Washington Post](https://www.washingtonpost.com/politics/2026/03/11/senators-investigation-epstein-files/) |

---

*This document was compiled from the Epstein Files Transparency Act production (2.73 million pages, 12 datasets), cross-referenced against published reporting, court filings, and public records. Every factual claim links to a source document. Sections labeled "What This Does NOT Show" are as important as the findings — read them.*

*For the complete report library: [epstein-data.com/reports](https://epstein-data.com/reports)*

---

*Analysis by epstein-data.com. Claude Code (Opus 4.6) assisted with database queries, cross-referencing, and document synthesis. All findings were verified against source documents. The underlying databases, CSVs, and analysis code are published at [github.com/rhowardstone/Epstein-research-data](https://github.com/rhowardstone/Epstein-research-data).*
