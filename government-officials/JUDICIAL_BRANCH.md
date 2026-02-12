# Judicial Branch: Federal Judges and Prosecutors in the Epstein Corpus

## Data Source
The Federal Judicial Center (FJC) maintains the authoritative Biographical Directory of all Article III federal judges appointed since 1789. We downloaded the complete database (4,055 judges) and filtered to all currently-serving judges (active + senior status):

| Category | Searched | With Hits |
|----------|----------|-----------|
| Supreme Court (current + retired, alive) | 11 | 11 |
| Circuit Court of Appeals — Active | 179 | 38 |
| Circuit Court of Appeals — Senior Status | 122 | 26 |
| District Court — Active (key courts) | 102 | 53 |
| District Court — Senior Status (key courts) | 89 | 46 |
| **TOTAL** | **503** | **174** |

**Key courts searched**: SDNY, SDFL, DDC, DNM, DVI, EDNY, NDNY, D.Conn., D.Mass. — the districts most connected to Epstein litigation.

**Search method**: FTS5 full-text search of `full_text_corpus.db` (1,380,937 documents, 2,731,796 pages across all 12 DOJ datasets) using exact phrase matching on each judge's first and last name.

---

## EXECUTIVE SUMMARY

**No sitting or former Supreme Court justice has any direct personal connection to Jeffrey Epstein in this corpus.**

The most notable finding is Justice **Elena Kagan** (58 documents), whose name appears because Epstein funded a Harvard poetry project she participated in, and because his lawyer Kathryn Ruemmler suggested her as a social contact for Epstein's associates. However, there is no evidence Kagan communicated with Epstein directly or knew of his involvement in the project.

The vast majority of judicial hits (174 of 503 judges) fall into predictable categories:
- **Case judges** appearing in court filings they presided over
- **Prosecutors** appearing on documents they signed
- **News mentions** in FBI daily briefings collected in the corpus
- **Common name collisions** (e.g., "Jeffrey Howard" matching Epstein's legal name)

One significant finding outside the judiciary itself: **Stephanie Dawn Thacker** (now 4th Circuit judge, 40 documents) was formerly a CEOS deputy who wrote a critical response about the handling of the original Epstein prosecution — the only case of its kind she had seen CEOS take on.

---

## I. SUPREME COURT OF THE UNITED STATES

### Current Justices

| Justice | Appointed By | Docs | Pages | Category |
|---------|-------------|------|-------|----------|
| Elena Kagan | Obama (2010) | 58 | 77 | MIXED |
| Brett Kavanaugh | Trump (2018) | 53 | 62 | NEWS |
| John Roberts | G.W. Bush (2005) | 45 | 52 | NEWS |
| Clarence Thomas | G.H.W. Bush (1991) | 29 | 35 | NEWS |
| Samuel Alito | G.W. Bush (2006) | 25 | 30 | NEWS |
| Sonia Sotomayor | Obama (2009) | 21 | 26 | NEWS |
| Neil Gorsuch | Trump (2017) | 18 | 21 | NEWS |
| Amy Coney Barrett | Trump (2020) | 1 | 1 | NEWS |
| Ketanji Brown Jackson | Biden (2022) | 1 | 1 | NEWS |

### Recent Former Justices (alive, retired/senior)

| Justice | Status | Docs | Category |
|---------|--------|------|----------|
| Anthony Kennedy | Retired 2018 | 17 | NEWS |
| Stephen Breyer | Retired 2022 | 15 | NEWS |

### Deceased Former Justices (searched for completeness)

| Justice | Status | Docs | Category |
|---------|--------|------|----------|
| Ruth Bader Ginsburg | Died 2020 | 46 | NEWS |
| Antonin Scalia | Died 2016 | 30 | NEWS |
| Sandra Day O'Connor | Died 2023 | 3 | NEWS |
| John Paul Stevens | Died 2019 | 2 | NEWS |
| David Souter | Retired 2009 | 1 | NEWS |

### Detailed Analysis: Elena Kagan (58 documents)

Justice Kagan's elevated document count traces to three distinct threads:

**1. Harvard "Poetry in America" Project (majority of hits)**
Epstein funded a Harvard poetry project called "Verse Video Education" / "Poetry in America" through his Gratitude America foundation ($110,000 grant). The project was run by Professor Elisa New (who is Larry Summers' wife). Kagan was one of dozens of prominent participants who taped poetry readings — alongside NBA players, architects, hip-hop artists, and other public figures.

Key documents:
- [EFTA00970475](https://www.justice.gov/epstein/files/DataSet%209/EFTA00970475.pdf): Lisa New to Epstein: *"We had Justice Elena Kagan last week and it was fantastic"*
- [EFTA00678464](https://www.justice.gov/epstein/files/DataSet%209/EFTA00678464.pdf): Kagan *"agreed to tape a reading in September"* — listed alongside Henry Louis Gates and Samantha Power
- [EFTA02703149](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02703149.pdf): Full email chain showing Epstein funding the project via Gratitude America ($110K), Richard Kahn handling grant logistics

**2. Ruemmler Social Suggestion**
- [EFTA02392995](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02392995.pdf): Kathryn Ruemmler (Obama's former White House Counsel, by then Epstein's lawyer at Latham & Watkins) replied *"Elena Kagan?"* when Epstein emailed about a DC trip with Woody Allen, asking *"anyone fun?"* in May 2015. This appears to be about the poetry project connection rather than a personal social relationship.

**3. News clips and legal coverage**
Standard mentions of Kagan in SCOTUS opinions, confirmation hearings, and judicial news.

**Assessment**: Kagan participated in a Harvard educational project that Epstein funded behind the scenes. There is no evidence she communicated with Epstein directly, was aware of his funding role, or had any personal or social relationship with him. Ruemmler's suggestion of Kagan appears to reference the existing poetry project connection. Multiple copies of project-related emails inflate the document count.

### Detailed Analysis: Brett Kavanaugh (53 documents)

All Kavanaugh mentions fall into two categories:

**1. News coverage (majority)**: FBI daily briefings about Kavanaugh's SCOTUS confirmation battle, #MeToo era coverage, and subsequent opinions.

**2. Two notable documents**:
- [EFTA02563087](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02563087.pdf): Someone in Epstein's email traffic wrote *"Brett Kavanaugh Is the best. Very courageous — returned to the Clinton investigation during Lewinsky"* — this is political commentary about Kavanaugh's role on the Ken Starr team, not evidence of any personal connection.
- [EFTA02605329](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02605329.pdf): Email discussing Ken Starr and Kavanaugh sent to Epstein — again political commentary, not personal contact.

**Assessment**: Pure news context. No evidence of any personal connection between Kavanaugh and Epstein. Epstein's social circle discussed Kavanaugh as a political figure, not as a personal contact.

### All Other SCOTUS Justices: NEWS Only

Roberts, Thomas, Alito, Sotomayor, Gorsuch, Barrett, Jackson, Kennedy, Breyer, Ginsburg, Scalia, O'Connor, Stevens, and Souter all appear exclusively in news coverage, FBI daily briefings, SCOTUS opinion summaries, and legal commentary. Zero evidence of any personal connection to Epstein for any of them.

---

## II. JUDGES WHO HANDLED EPSTEIN/MAXWELL CASES

These judges appear in the corpus strictly in their judicial capacity:

| Judge | Court | Role in Epstein Cases | Docs |
|-------|-------|----------------------|------|
| **Kenneth Marra** | S.D. Florida | CVRA ruling — found NPA violated victims' rights | 221 |
| **Alison Nathan** | S.D. New York / 2nd Circuit | Presided over Maxwell trial and conviction | 63 |
| **Colleen McMahon** | S.D. New York (Chief Judge) | Received BOP communications re Epstein at MCC; administrative oversight | 57 |
| **Richard Berman** | S.D. New York | Denied Epstein bail in 2019 case; death occurred during his case | 53 |
| **Jed Rakoff** | S.D. New York | Signed "Order regarding Review of Videomaterials" — led to 2023 CSAM discovery | 31 |
| **Analisa Torres** | S.D. New York | Handled MCC guard deferred prosecution agreement (USA v. Michael Thomas) | 26 |
| **Ronnie Abrams** | S.D. New York | Presided over "Katie Johnson" v. Trump & Epstein civil lawsuit (dismissed on technical grounds) | 23 |
| **Loretta Preska** | S.D. New York | Ordered unsealing of Maxwell deposition documents in Giuffre v. Maxwell | 20 |
| **Robert Sweet** | S.D. New York (died 2019) | Original Giuffre v. Maxwell judge; also sentenced Hoffenberg (Epstein's co-conspirator in Towers Financial fraud) | 17 |
| **Denise Cote** | S.D. New York | Related proceedings | 3 |

### Notable: Judge Jed Rakoff and the 2023 CSAM Discovery
Rakoff signed the order governing the post-mortem review of video materials from Epstein's estate. During this review in 2023, lawyers from Hughes Hubbard discovered a video that appeared to contain child pornography — material that had been missed during the initial 2019-2021 FBI evidence processing. This is documented in [EFTA00039019](https://www.justice.gov/epstein/files/DataSet%208/EFTA00039019.pdf).

### Notable: Judge Denny Chin — 1996 Civil Case
Chin (now 2nd Circuit, 7 documents) presided over a 1996 civil case: *USA v. Epstein et al.* (Case 1:96-cv-08307-DC) — a rent/lease/ejectment matter filed by the United States against Jeffrey E. Epstein and Ivan Fisher, predating the sex trafficking investigation by a decade. Documented in [EFTA00187391](https://www.justice.gov/epstein/files/DataSet%209/EFTA00187391.pdf).

---

## III. KEY PROSECUTORS AND LEGAL OFFICIALS

| Official | Role | Docs | Context |
|----------|------|------|---------|
| **Alan Dershowitz** | Epstein defense attorney; Harvard Law | 1,360 | DIRECT — negotiated NPA whose co-conspirator immunity clause later shielded him; accused of sexual abuse by victims |
| **Audrey Strauss** | Acting U.S. Attorney, SDNY | 606 | INVESTIGATION — charged Maxwell; name on hundreds of filings |
| **Barry Krischer** | Palm Beach County State Attorney | 214 | INVESTIGATION — original prosecutor accused of leniency; Police Chief Reiter feuded with him publicly |
| **Geoffrey Berman** | U.S. Attorney, SDNY | 208 | INVESTIGATION — brought 2019 charges; visited MCC after death; later fired by AG Barr |
| **Damian Williams** | U.S. Attorney, SDNY | 134 | INVESTIGATION — oversaw Maxwell trial to guilty verdict |
| **Maurene Comey** | AUSA, SDNY (daughter of James Comey) | 52 | INVESTIGATION — lead prosecutor; signed grand jury subpoenas, search warrant protocols |
| **Jack Smith** | Special Counsel (Trump cases) | 77 | MIXED — 85% news coverage of Trump prosecution. **15% is a DIFFERENT Jack Smith**: a New Mexico historian who wanted to visit Epstein's Zorro Ranch to research "Popes Well." Epstein personally called him back. Completely unrelated to the Special Counsel. |
| **James Boasberg** | Chief Judge, FISA Court / D.D.C. | 8 | NEWS only — FBI daily briefings about FISA rulings, unrelated cases |

### Dershowitz: Unique Position
Alan Dershowitz holds a unique position as both Epstein's defense attorney AND an accused individual. His 1,360 documents include:
- **Defense work**: Negotiated the 2007 NPA that included an unprecedented clause granting immunity to "potential co-conspirators" — which he himself was named as in victim testimony
- **Accusations**: Named by Virginia Giuffre as having sexually abused her on Epstein's island; Dershowitz has vigorously denied all allegations
- **Dual role**: Dershowitz was part of the defense team that negotiated the NPA, which included a co-conspirator immunity clause from which he personally benefited when later accused — a potential conflict of interest noted in subsequent litigation

### Krischer: The Prosecution That Wasn't
Barry Krischer drew extensive criticism in the corpus. Police Chief Michael Reiter was *"so angry with State Attorney Barry Krischer's handling of the case that he wrote a memo suggesting he disqualify himself."* One document states: *"Unfortunately, the local prosecutor in this case was... named Barry Krischer. When Krischer found out the target was Epstein, a big Democratic donor, he refused to prosecute."* The grand jury under Krischer returned only a single count of solicitation of prostitution, despite police presenting evidence of dozens of underage victims.

---

## IV. FEDERAL CIRCUIT COURTS OF APPEALS (301 judges searched)

Of 301 circuit court judges searched (179 active + 122 senior status), 64 had hits. The vast majority are common name collisions, news mentions, or incidental references. Noteworthy entries:

### Judges with 10+ Documents

| Judge | Circuit | Status | Docs | Assessment |
|-------|---------|--------|------|------------|
| **Alison Nathan** | 2nd Circuit | Active | 63 | INVESTIGATION — Maxwell trial judge (elevated from SDNY) |
| **Stephanie Thacker** | 4th Circuit | Active | 40 | MIXED — see detailed analysis below |
| **Stephanie Seymour** | 10th Circuit | Senior | 36 | FALSE POSITIVE — matches supermodel Stephanie Seymour (Peter Brant's wife), NOT the judge |
| **Chad Readler** | 6th Circuit | Active | 31 | NTOC TIPS — conspiracy theory material alleging cover-up, no substance |
| **Jeffrey Howard** | 1st Circuit | Senior | 19 | FALSE POSITIVE — sentence-boundary crossings ("Jeffrey,\nHoward German from Sikorsky"), a background check DB listing "Jeffrey Howard" as middle name (correct: Jeffrey **Edward** Epstein), and 1 actual judge reference (Harvard admissions case) |
| **John Rogers** | 6th Circuit | Senior | 15 | Likely common name collision |
| **David Barron** | 1st Circuit | Active | 13 | FALSE POSITIVE — name on Dialog retreat invite list forwarded to Epstein by Lisa Randall |
| **W. Eugene Davis** | 5th Circuit | Senior | 13 | Likely common name collision |
| **John Zihun Lee** | 7th Circuit | Active | 11 | Likely common name collision ("John Lee") |
| **David Hamilton** | 7th Circuit | Senior | 10 | Likely common name collision |

### Detailed Analysis: Stephanie Dawn Thacker (40 documents)

Stephanie Thacker is now a 4th Circuit judge (appointed by Obama, 2012), but BEFORE her judicial appointment, she was a **deputy in the Child Exploitation and Obscenity Section (CEOS)** of the DOJ — the very section that was supposed to prosecute Epstein federally.

Her 40 documents include:
- A critical letter she wrote responding to CEOS's assessment of the Epstein case, submitted as part of the CVRA proceedings before Judge Marra
- She stated she *"knew of no other case like this being prosecuted by CEOS"* — highlighting the extraordinary nature of the plea deal
- Her response was filed alongside the "Principal Submission" and "Summary of Misconduct" documents

This is significant: a former CEOS insider — now a federal appellate judge — formally criticized the section's handling of the Epstein prosecution, and her critique became part of the judicial record.

Key documents:
- [EFTA00013783](https://www.justice.gov/epstein/files/DataSet%208/EFTA00013783.pdf): Email transmitting Thacker's CEOS response letter
- [EFTA00209832](https://www.justice.gov/epstein/files/DataSet%209/EFTA00209832.pdf): *"Stephanie Thacker, a former deputy to CEOS Chief Drew Oosterbaan, has stated that she knew of no other case like this being prosecuted by CEOS."*
- [EFTA01615855](https://www.justice.gov/epstein/files/DataSet%209/EFTA01615855.pdf): Internal DOJ discussion referencing Thacker's role

### Chad Readler (31 documents) — NTOC Tips
The Readler mentions come from NTOC (National Threat Operations Center) tip submissions. Tipsters alleged that Readler, while an acting Assistant Attorney General in Trump's DOJ, handled certain cases leniently and was subsequently appointed to the 6th Circuit by Trump as a reward. The tips use language like *"The 'prosecutor' on the case was Chad Readler. Now: JUDGE Chad Readler. Made so by Trump."* These are unverified public tips — conspiracy allegations, not established facts.

---

## V. KEY DISTRICT COURT JUDGES (191 judges searched)

Of 191 key-district judges searched (102 active + 89 senior), 99 had hits. Most are routine case references. Notable entries beyond those already covered in Section II:

### SDNY Judges with 5+ Documents (not already covered)

| Judge | Status | Docs | Context |
|-------|--------|------|---------|
| John Koeltl | Active | 15 | Court filings, related cases |
| Lewis Kaplan | Senior | 11 | Presided over Giuffre v. Prince Andrew; E. Jean Carroll v. Trump |
| Paul Gardephe | Senior | 7 | Related SDNY proceedings |
| Victor Marrero | Senior | 7 | Related SDNY proceedings |
| Jesse Furman | Active | 8 | Related SDNY proceedings |
| Kenneth Karas | Active | 5 | Related proceedings |
| Paul Engelmayer | Active | 4 | Related proceedings |

### SDFL Judges with 5+ Documents

| Judge | Status | Docs | Context |
|-------|--------|------|---------|
| **Kenneth Marra** | Senior | 221 | CVRA ruling (covered in Section II) |
| Rodney Smith | Active | 9 | Likely case-related |
| James Cohn | Senior | 8 | SDFL proceedings |
| Donald Middlebrooks | Active | 6 | SDFL proceedings |
| James Lawrence King | Senior | 6 | SDFL proceedings |
| Donald Graham | Senior | 5 | SDFL proceedings |

### D.C. District Judges with 5+ Documents

| Judge | Status | Docs | Context |
|-------|--------|------|---------|
| Emmet Sullivan | Senior | 17 | Primarily news (Flynn case), some Epstein-related DOJ oversight |
| Richard Leon | Senior | 14 | News coverage, DOJ-related proceedings |
| John Bates | Senior | 13 | FISA matters, DOJ oversight |
| Amit Mehta | Active | 12 | Google antitrust trial, DOJ news |
| Royce Lamberth | Senior | 11 | Primarily news coverage |
| Reggie Walton | Senior | 11 | Primarily news coverage |
| Tanya Chutkan | Active | 10 | Trump Jan. 6 case news coverage |
| James Boasberg | Active | 8 | FISA court, news coverage |

Note: Many D.C. district judge hits come from FBI daily briefings collected in the corpus, not from Epstein-specific documents.

---

## VI. COMPLETE SEARCH RESULTS

### False Positives Identified

| Name | Claimed Match | Actual Match | Docs |
|------|--------------|--------------|------|
| Stephanie Seymour | 10th Circuit Senior Judge | Supermodel (Peter Brant's wife) — socialite in Epstein's orbit | 36 |
| Jeffrey Howard | 1st Circuit Senior Judge | Sentence-boundary crossings ("Jeffrey,\nHoward German..."), a background check DB error listing "Jeffrey Howard" as middle name (correct: Jeffrey Edward Epstein), and 1 actual judge reference | 19 |
| David Barron | 1st Circuit Chief Judge | Name on Dialog retreat invite forwarded to Epstein | 13 |
| John Lee | 7th Circuit Active Judge | Common name collision | 11 |
| David Hamilton | 7th Circuit Senior Judge | Common name collision | 10 |
| Brian Murphy | D.D.C. Active Judge | Common name collision (12 docs) | 12 |
| Rodney Smith | S.D. Fla. Active Judge | Possibly common name | 9 |

### Summary by Category

| Category | Count | Description |
|----------|-------|-------------|
| INVESTIGATION | ~25 | Judges/prosecutors who handled Epstein/Maxwell cases in their professional capacity |
| NEWS | ~120 | Names appearing in FBI daily briefings, legal news clips, or political coverage |
| FALSE POSITIVE | ~7 | Common name collisions or incidental mentions |
| MIXED | 3 | Elena Kagan (indirect project connection), Denny Chin (1996 civil case), Stephanie Thacker (CEOS criticism) |
| DIRECT | 1 | Alan Dershowitz (defense attorney AND accused individual) |
| NONE | ~329 | Zero documents found |

---

## VII. KEY FINDINGS

1. **No SCOTUS justice has a direct connection to Epstein.** Elena Kagan's 58-document count is explained by Epstein funding a Harvard educational project she participated in. There is no evidence she was aware of his involvement.

2. **Stephanie Thacker's CEOS criticism** is the most significant judicial-branch finding. A federal appellate judge (before her appointment) formally criticized the DOJ section that handled the original Epstein prosecution, stating it was unprecedented — and her critique became part of the CVRA court record.

3. **The "Jack Smith" in Epstein's emails is a historian**, not the Special Counsel. He wanted access to Epstein's New Mexico ranch to research a historic well called "Popes Well."

4. **Supermodel Stephanie Seymour** (NOT the judge) appears in Epstein's social emails — she was part of the art world/socialite scene connected to Epstein through Peter Brant and Jean Pigozzi.

5. **Barry Krischer** drew the harshest criticism of any legal official, with police alleging political favoritism in his handling of the original prosecution.

6. **Jed Rakoff's video review order** led to the 2023 discovery of CSAM that was missed during the initial 2019-2021 evidence processing — years after Epstein's death.

7. **503 federal judges comprehensively searched.** This includes every active and senior-status Article III judge on the Supreme Court, all 13 Courts of Appeals, and the key district courts involved in Epstein litigation. Data sourced from the Federal Judicial Center's official biographical directory.

---

## Methodology Notes

- **Source**: Federal Judicial Center Biographical Directory of Article III Federal Judges (downloaded February 2026, updated nightly)
- **Corpus**: `full_text_corpus.db` — 1,380,937 documents, 2,731,796 pages across all 12 DOJ Epstein datasets
- **Search**: FTS5 exact phrase matching on "First Last" name pairs
- **Context analysis**: Deep-read of all documents for judges with 5+ hits and all SCOTUS justices
- **Limitations**: Exact phrase search means some name variants may be missed (e.g., "J. Roberts" would not match "John Roberts"). Conversely, common names produce false positives that required manual review.
