# The Epstein Legal Universe: Every Lawyer, Every Case

## A comprehensive index of legal actors and litigation in the EFTA corpus

Updated: March 2026
Scope: 1.42M documents, 2.91M pages across 12 DOJ datasets + DS98 (FBI Vault) + DS99 (House Oversight)
Databases: full_text_corpus.db, prosecutorial_query_graph.db, concordance_complete.db, persons_registry.json

**Machine-readable data**: [LEGAL_ACTORS.csv](https://github.com/rhowardstone/Epstein-research/blob/main/institutional/LEGAL_ACTORS.csv) (129 entries, 12 columns) | [LITIGATION_MATTERS.csv](https://github.com/rhowardstone/Epstein-research/blob/main/institutional/LITIGATION_MATTERS.csv) (37 cases, 15 columns)

---

## EXECUTIVE SUMMARY

The DOJ's EFTA production is, at its core, a legal archive. Over 35% of the corpus — more than 490,000 of 1.39 million documents — references attorneys or legal counsel. Attorney-client privilege is invoked on 548,831 pages. Privilege logs account for 2,636 pages. Motions to quash total 811.

This report indexes every lawyer, law firm, judge, prosecutor, and litigation matter identifiable in the corpus. The numbers:

- **120+ individual legal actors** identified by name with verifiable corpus presence
- **50+ law firms** with document counts
- **30+ distinct cases** (criminal, civil, regulatory, administrative)
- **25+ judges** across federal, state, and international jurisdictions
- **15+ prosecutors** (federal and state)
- **257 grand jury subpoenas** (from prosecutorial_query_graph.db)
- **548,831 pages** invoking attorney-client privilege

### The "Army of Legal Superstars"

Former U.S. Attorney Alexander Acosta himself used this phrase to describe Epstein's defense team during his OPR interview ([EFTA00009116](https://www.justice.gov/epstein/files/DataSet%207/EFTA00009116.pdf), p. 396):

> "Mr. Epstein hired an army of legal superstars: Harvard Professor Dershowitz, former judge and then Pepperdine [Dean] Ken Starr, former deputy assistant to the president then Kirkland & Ellis law partner Jay Lefkowitz, and several others, including prosecutors that formerly worked in the U.S. Attorney's Office, the child exploitation section of the Department of Justice."

The corpus confirms at least 120 named legal actors across the Epstein legal universe. Media reports have cited a figure of "75+ lawyers" though the original source for that number has not been definitively located. The actual count depends on how you draw boundaries: does it include Maxwell's defense team (7 lawyers)? The victim attorneys (12+)? Government counsel pursuing Epstein (15+)? By our corpus count, the Epstein-side total alone exceeds 52 named attorneys — and that is a floor.

### Key Structural Finding: Criminal Defense Lawyers for Everything

Nearly every member of Epstein's NPA-era defense team (2006-2008) was a criminal defense specialist: Dershowitz (criminal appellate), Starr (former judge/solicitor general), Lefkowitz (White House policy), Lefcourt (criminal defense), Goldberger (FL criminal defense), Roy Black (FL criminal defense), Guy Lewis (former USAO chief). This team was assembled to fight a federal sex trafficking investigation but was simultaneously deployed for civil CVRA litigation, counter-suits against victim attorneys, and NPA negotiation — a pattern consistent with treating all legal threats as criminal-defense problems requiring aggressive advocacy rather than civil-matter resolution.

### Cross-References to Existing Reports

This index complements:
- [Prosecution Failures Analysis](./PROSECUTION_FAILURES_ANALYSIS.md) — detailed NPA narrative, named individuals who escaped prosecution
- [Ruemmler Deep Dive](../individuals/RUEMMLER_DEEP_DIVE.md) — Kathryn Ruemmler's White House → Epstein → Goldman trajectory
- [Grand Jury Subpoena Analysis (PQG Index)](../pqg_lines_of_investigation/00_INDEX.md) — 257 subpoenas, 779 investigative gaps
- [FBI 302 Missing Serials Dossier](./FBI_302_MISSING_SERIALS_DOSSIER.md) — gaps in the investigative record
- [Death Investigation Document Removal](./DEATH_INVESTIGATION_DOCUMENT_REMOVAL.md) — MCC death investigation records

---

## HOW TO USE THIS INDEX

- **Looking for every lawyer who touched the NPA?** See §2.2 (NPA Defense Army) for Epstein's team, §1.2 for the NPA itself, §2.5 (SDFL prosecutors) for the government side, and §2.4 for victim counsel in the subsequent CVRA challenge.
- **Looking for all matters with privilege log activity?** See §3.3 (The Privilege Architecture). Privilege logs are in 2,636 pages; start with [EFTA01325051](https://www.justice.gov/epstein/files/DataSet%209/EFTA01325051.pdf).
- **Looking for a specific lawyer?** Use Ctrl+F / Cmd+F. Every lawyer with 10+ docs appears at least once in this index.
- **Looking for all litigation involving a specific bank?** See §1.8 (Deutsche Bank), §1.9 (JPMorgan). For subpoenaed banks, see §1.13 (PQG Summary) and the [PQG Index](../pqg_lines_of_investigation/00_INDEX.md).
- **Looking for co-conspirators / cooperators?** See §2.10.
- **Want to verify a doc count?** All counts are `COUNT(DISTINCT efta_number)` queries against [`full_text_corpus.db`](https://github.com/rhowardstone/Epstein-research-data/releases) — see Methodology for disambiguation rules.

---

## PART 1: THE CASES

### 1.1 Criminal Proceedings

#### USA v. Jeffrey Epstein — SDNY (19-cr-490-RMB)

| Field | Content |
|-------|---------|
| Court | U.S. District Court, Southern District of New York |
| Judge | Hon. Richard M. Berman (49 docs) |
| Filed | July 8, 2019 |
| Resolved | August 10, 2019 — defendant died pre-trial (suicide ruling) |
| Charges | 18 U.S.C. §§ 371, 1591 (sex trafficking conspiracy, sex trafficking) |
| Epstein's counsel | Reid Weingarten (Steptoe & Johnson, 2,393 docs), Martin Weinberg (solo P.C., 1,933 docs), Marc Fernich (91 docs), Bruce Barket (Barket Epstein Kearon, 162 docs), Joseph Nascimento (Ross Amsel Raben, 95 docs) |
| Prosecutors | Geoffrey Berman (U.S. Attorney), Maurene Comey (AUSA), Alison Moe (AUSA), Alexander Rossmiller (AUSA) |
| Magistrates | Barbara Moses (arrest warrant, 95 docs), Henry Pitman (search warrant), Kevin Fox (device warrants), Ruth Miller (USVI warrant) |
| DOJ case number | 2018R01618 |
| Corpus presence | 1,404 pages |
| Key EFTAs | [EFTA01659328](https://www.justice.gov/epstein/files/DataSet%209/EFTA01659328.pdf) (bail order), [EFTA01301551](https://www.justice.gov/epstein/files/DataSet%209/EFTA01301551.pdf) (search warrant), [EFTA01625916](https://www.justice.gov/epstein/files/DataSet%209/EFTA01625916.pdf) (warrant affidavit), [EFTA01649305](https://www.justice.gov/epstein/files/DataSet%209/EFTA01649305.pdf) (VNS notification) |

#### USA v. Ghislaine Maxwell — SDNY (20-cr-330-AJN)

| Field | Content |
|-------|---------|
| Court | U.S. District Court, Southern District of New York |
| Judge | Hon. Alison J. Nathan (61 docs) |
| Filed | July 2, 2020 |
| Resolved | Convicted December 29, 2021 (5 of 6 counts); sentenced June 28, 2022 — 20 years, $750,030 fine. [2d Circuit affirmed September 17, 2024](https://law.justia.com/cases/federal/appellate-courts/ca2/22-1426/22-1426-2024-09-17.html). [Supreme Court cert denied October 6, 2025](https://www.nbcnews.com/politics/supreme-court/supreme-court-rejects-epstein-associate-ghislaine-maxwells-appeal-crim-rcna233281). |
| Charges | Sex trafficking conspiracy, sex trafficking of a minor, enticing a minor to travel to engage in illegal sex acts, transporting a minor to engage in illegal sex acts, conspiracy to commit sex trafficking, perjury |
| Maxwell's counsel | Laura Menninger & Jeffrey Pagliuca (Haddon Morgan Foreman, 1,447 docs combined firm), Mark Cohen & Christian Everdell (Cohen & Gresser, 1,495 docs), Bobby Sternheim (804 docs), David Bruck (sentencing, 210 docs) |
| Prosecutors | Audrey Strauss (Acting U.S. Attorney, 706 docs), Maurene Comey (380 docs), Alison Moe (423 docs), Alexander Rossmiller (108 docs), Nicolas Roos (46 docs), Rebekah Donaleski (31 docs) |
| DOJ case number | 2020R00719 |
| Corpus presence | 17,848 pages — the single largest litigation matter in the corpus |
| Appeals | 21-770, 20-3061, 22-1426, 21-58 (2d Cir.) |
| Key EFTAs | [EFTA01659412](https://www.justice.gov/epstein/files/DataSet%209/EFTA01659412.pdf) (detention memo), [EFTA01684225](https://www.justice.gov/epstein/files/DataSet%209/EFTA01684225.pdf) (sentencing — 20 years), [EFTA01655191](https://www.justice.gov/epstein/files/DataSet%209/EFTA01655191.pdf) (juror ruling) |

#### USA v. Tova Noel & Michael Thomas — SDNY (19-cr-830-AT)

| Field | Content |
|-------|---------|
| Court | SDNY |
| Charges | Conspiracy, making false records (MCC guard duty logs, night of Epstein's death) |
| Corpus presence | 108 docs |
| Key EFTAs | [EFTA00009786](https://www.justice.gov/epstein/files/DataSet%208/EFTA00009786.pdf), [EFTA00022186](https://www.justice.gov/epstein/files/DataSet%208/EFTA00022186.pdf) |
| Note | Guards entered deferred prosecution agreements in [May 2021](https://www.cnbc.com/2021/05/25/judge-approves-deferred-prosecution-deal-for-epstein-jail-guards.html); government moved to dismiss charges [late December 2021](https://www.cnn.com/2021/12/30/us/jeffrey-epstein-officers-dismissed-charges) after DPA completion |

#### State of Florida v. Epstein — 15th Judicial Circuit (CF 09454)

| Field | Content |
|-------|---------|
| Court | Circuit Court, Palm Beach County, Florida |
| Judge | Hon. Deborah Dale Pucillo (76 docs) |
| Filed | 2006 |
| Resolved | Guilty plea June 30, 2008 — 18 months county jail, lifetime sex offender registration |
| Charges | Felony solicitation of prostitution (1 count), procuring (1 count) |
| Epstein's counsel | Jack Goldberger (Atterbury Goldberger Weiss, 4,560 docs), Joseph Ackerman (Fowler White Burnett, 1,107 docs), Lilly Ann Sanchez (1,006 docs) |
| State Attorney | Barry Krischer (368 docs); reassigned by executive order to Bruce Colton (4 docs) |
| Other judges | Sandra McSorley (probation/work release, 36 docs), Jeffrey Colbath (NPA unsealing, 64 docs), David Crow (settlement matters, 65 docs) |
| Corpus presence | 510 pages |
| Key EFTAs | [EFTA00010496](https://www.justice.gov/epstein/files/DataSet%208/EFTA00010496.pdf), [EFTA00027590](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027590.pdf) (plea transcript — pp. 38-39 reveal NPA trigger), [EFTA01625438](https://www.justice.gov/epstein/files/DataSet%209/EFTA01625438.pdf) (booking/probation records) |

#### Rodriguez Obstruction — SDFL (10-80015-CR-MARRA)

| Field | Content |
|-------|---------|
| Court | SDFL |
| Judge | Kenneth Marra |
| Defendant | Alfredo Rodriguez (Epstein household manager) |
| Resolved | Convicted — attempted to sell Epstein's "black book" for $50,000 after testifying he didn't possess it |
| Corpus presence | 11 docs |
| Key EFTAs | [EFTA00608045](https://www.justice.gov/epstein/files/DataSet%209/EFTA00608045.pdf) (FBI CW meeting), [EFTA00728180](https://www.justice.gov/epstein/files/DataSet%209/EFTA00728180.pdf) (document sale attempt) |

### 1.2 The Non-Prosecution Agreement (NPA) — SDFL (08-80736)

Not a filed case, but the most consequential legal instrument in the corpus:

| Field | Content |
|-------|---------|
| Negotiated | 2006-2008 |
| Parties | USAO-SDFL (Acosta/Villafana) and Epstein defense team |
| Immunity scope | Epstein + 4 named co-conspirators (redacted) + Lesley Groff + "any potential co-conspirators" |
| Condition | Epstein plead guilty to state charges |
| Victim notification | Deliberately concealed for 9 months in violation of CVRA |
| OPR finding | "Poor judgment" but not "professional misconduct" ([EFTA00095558](https://www.justice.gov/epstein/files/DataSet%209/EFTA00095558.pdf)) |
| Key EFTAs | [EFTA00010507](https://www.justice.gov/epstein/files/DataSet%208/EFTA00010507.pdf) (Judge Marra's order), [EFTA01659896](https://www.justice.gov/epstein/files/DataSet%209/EFTA01659896.pdf) (Acosta letter to Starr), [EFTA00009116](https://www.justice.gov/epstein/files/DataSet%207/EFTA00009116.pdf) (Acosta OPR interview), [EFTA01656152](https://www.justice.gov/epstein/files/DataSet%209/EFTA01656152.pdf) (NPA immunity coverage) |

### 1.3 CVRA / Victim Rights Litigation

#### Jane Doe #1 & #2 v. United States — SDFL (08-80736-CIV-MARRA)

| Field | Content |
|-------|---------|
| Court | SDFL |
| Judge | Kenneth Marra (228 docs), Magistrate Linnea Johnson (119 docs) |
| Filed | 2008 |
| Nature | CVRA enforcement — victims challenged the NPA's concealment |
| Victim counsel | Paul Cassell (2,895 docs), Brad Edwards (3,317 docs) |
| Government | Marie Villafana (846 docs), Dexter Lee (376 docs) |
| Epstein defense | Jack Goldberger, Roy Black, Martin Weinberg, Jay Lefkowitz |
| Corpus presence | 1,397 distinct docs; 7,605 pages including related dockets |
| Appellate | In re Wild — 11th Circuit: 955 F.3d 1196 (2020), 994 F.3d 1244 (2021) |
| Key EFTAs | [EFTA01657752](https://www.justice.gov/epstein/files/DataSet%209/EFTA01657752.pdf) (51-page privilege ruling), [EFTA01325051](https://www.justice.gov/epstein/files/DataSet%209/EFTA01325051.pdf) (privilege log), EFTA00073493 (removed from justice.gov) / [EFTA00074599](https://www.justice.gov/epstein/files/DataSet%209/EFTA00074599.pdf) (11th Circuit opinions) |

### 1.4 Civil — Giuffre Cases

#### Giuffre v. Maxwell — SDNY (15-cv-7433)

| Field | Content |
|-------|---------|
| Court | SDNY |
| Judges | Robert Sweet (17 docs, deceased), then Loretta Preska (21 docs) |
| Filed | 2015 |
| Nature | Defamation — Maxwell called Giuffre a liar |
| Plaintiff counsel | Sigrid McCawley (Boies Schiller, 736 docs), David Boies (370 docs) |
| Defense counsel | Laura Menninger, Jeffrey Pagliuca (Haddon Morgan) |
| Resolved | Settled 2017; unsealing proceedings continued through 2024 |
| Corpus presence | 1,655 pages |
| Key EFTAs | [EFTA01282143](https://www.justice.gov/epstein/files/DataSet%209/EFTA01282143.pdf) (Deutsche Bank KYC referencing case), [EFTA01340452](https://www.justice.gov/epstein/files/DataSet%209/EFTA01340452.pdf), [EFTA01357027](https://www.justice.gov/epstein/files/DataSet%209/EFTA01357027.pdf) |

### 1.5 Civil — SDFL Victim Suits

The SDFL docket contains at least 11 related victim civil suits, all before Judge Marra/Johnson:

| Case Number | Description | Doc Count |
|-------------|-------------|-----------|
| 08-cv-80119-KAM | Jane Doe v. Epstein (lead case) | 634 |
| 08-cv-80232-KAM | Jane Doe No. 3 v. Epstein | 190 |
| 08-cv-80380-KAM | Related victim suit | 181 |
| 08-cv-80381-KAM | Related victim suit | 149 |
| 08-cv-80811-CIV-MARRA | Victim suit | 130 |
| 08-cv-80893-KAM | Victim suit | 357 |
| 08-cv-80993-KAM | Victim suit | 95 |
| 08-cv-80994-KAM | Jane Doe No. 6 | 102 |
| 08-cv-90693-CIV-MARRA | Subpoena enforcement | Small |
| 09-cv-80469-KAM | Kellen intervention / Jane Doe II | 301 |
| 09-cv-80591-KAM | Jane Doe No. 101 | 334 |
| 09-cv-80656-KAM | Related victim suit | 331 |

Combined corpus presence of civil victim suits: ~2,900+ docs.

Defense counsel across these suits: Jack Goldberger (Atterbury Goldberger Weiss), Joseph Ackerman (Fowler White Burnett), Robert Critton (Burman Critton, 2,037 docs).
Victim counsel: Brad Edwards, Jack Scarola (Searcy Denney, 1,817 docs firm), Paul Cassell.

### 1.6 Counter-Litigation & SLAPP

#### Epstein v. Edwards, Rothstein, L.M. — Palm Beach (50 2009CA040800XXXXMB AG)

| Field | Content |
|-------|---------|
| Court | Circuit Court, 15th Judicial Circuit, Palm Beach County |
| Nature | Epstein counter-sued victim attorney Brad Edwards, Ponzi schemer Scott Rothstein, and a Jane Doe (L.M.) |
| Epstein's counsel | Joseph Ackerman (Fowler White Burnett) |
| Edwards' counsel | Gary Farmer Jr. (Farmer Jaffe Weissing Edwards Fistos & Lehrman) |
| Rothstein's counsel | Marc Nurik (928 docs across corpus) |
| Key EFTAs | [EFTA01112732](https://www.justice.gov/epstein/files/DataSet%209/EFTA01112732.pdf) (deposition notice for Rothstein), [EFTA01099387](https://www.justice.gov/epstein/files/DataSet%209/EFTA01099387.pdf) (interrogatories to Edwards) |
| Resolved | Settled December 4, 2018, on the eve of jury selection. Epstein issued a written apology: "The lawsuit I filed was my unreasonable attempt to damage [Edwards'] business reputation and cause Mr. Edwards to stop pursuing cases against me." Financial terms confidential. |
| Note | Scott Rothstein separately pleaded guilty to Ponzi scheme crimes (2010), sentenced to 50 years. His firm (Rothstein Rosenfeldt Adler) appears in 1,665 docs. |

### 1.7 Financial/Corporate Litigation

#### Gerber & Koenig v. Financial Trust Company / Epstein — SDNY (18-cv-07580)

| Field | Content |
|-------|---------|
| Nature | Towers Financial Corporation / Hoffenberg class action |
| Epstein's role | Named as "uncharged co-conspirator" of Steven Hoffenberg in TFC's $450M Ponzi scheme |
| Corpus presence | 45 docs |
| Related | In re Towers Financial Corporation (93-B41558), Hoffenberg v. Epstein (16-03989) |
| Key EFTAs | [EFTA01298858](https://www.justice.gov/epstein/files/DataSet%209/EFTA01298858.pdf) (voluntary dismissal), [EFTA01386750](https://www.justice.gov/epstein/files/DataSet%209/EFTA01386750.pdf) (TFC complaint naming Epstein), [EFTA01334040](https://www.justice.gov/epstein/files/DataSet%209/EFTA01334040.pdf) (Hoffenberg told grand jury Epstein was "technical" person) |

#### Citibank v. Epstein — SDNY (02-CV-5332-SHS)

$10M loan dispute. Referenced in [EFTA01386058](https://www.justice.gov/epstein/files/DataSet%209/EFTA01386058.pdf).

#### NASD v. Epstein — NASD (02-03451)

Referenced in [EFTA01387836](https://www.justice.gov/epstein/files/DataSet%209/EFTA01387836.pdf).

### 1.8 Deutsche Bank Regulatory

| Field | Content |
|-------|---------|
| Regulator | NYDFS (New York Department of Financial Services) |
| Result | $150 million fine (July 2020) for compliance failures related to Epstein relationship |
| Corpus presence | 9,122 pages matching Deutsche Bank + regulatory terms |
| Internal AML cases | Case Nos. 146215, 142716, 147864, 144434, 01946825 |
| Key EFTAs | [EFTA01355597](https://www.justice.gov/epstein/files/DataSet%209/EFTA01355597.pdf) (DBSI settlement with SEC/NASD/NYSE/NY AG), [EFTA01415338](https://www.justice.gov/epstein/files/DataSet%209/EFTA01415338.pdf)–[EFTA01427000](https://www.justice.gov/epstein/files/DataSet%209/EFTA01427000.pdf) range (massive AML/KYC documentation) |

### 1.9 JPMorgan Chase

| Field | Content |
|-------|---------|
| Regulatory/Civil | USVI AG suit; private victim class action |
| Result | $290 million to Epstein survivors (class action, approved November 9, 2023) + $75 million to USVI (September 2023) = $365 million total |
| Corpus presence | 7,742 pages matching JPMorgan + litigation terms |
| Key EFTAs | [EFTA01581722](https://www.justice.gov/epstein/files/DataSet%209/EFTA01581722.pdf) (Highbridge objection to Epstein subpoena), [EFTA01583334](https://www.justice.gov/epstein/files/DataSet%209/EFTA01583334.pdf) (account applications) |

### 1.10 USVI v. Epstein Estate

| Field | Content |
|-------|---------|
| Filed by | Denise George (USVI Attorney General, 47 docs) |
| Filed | January 15, 2020 |
| Nature | Civil enforcement under USVI anti-criminal enterprise, sex trafficking, child exploitation, and fraud laws. Initially sought $577M in punitive damages. |
| Settlement | $105 million in cash plus 50% of proceeds from sale of Little St. James island, plus $450K for environmental remediation, plus return of $80M+ in tax benefits. Settled November 29, 2022 — largest settlement in USVI history. |
| Outcome | AG George was fired December 31, 2022, by Governor Albert Bryan Jr. — days after she filed a separate suit against JPMorgan Chase (December 27, 2022) without informing the Governor. |
| Corpus presence | 508 pages matching "Virgin Islands" AND "Attorney General" |
| Key EFTAs | [EFTA01651272](https://www.justice.gov/epstein/files/DataSet%209/EFTA01651272.pdf), [EFTA01654937](https://www.justice.gov/epstein/files/DataSet%209/EFTA01654937.pdf) |

### 1.11 Government Investigations (Non-Criminal)

| Investigation | Entity | Corpus Presence | Key EFTAs |
|---------------|--------|----------------|-----------|
| OPR (NPA handling) | DOJ Office of Professional Responsibility | Substantial | [EFTA01659527](https://www.justice.gov/epstein/files/DataSet%209/EFTA01659527.pdf), [EFTA00095558](https://www.justice.gov/epstein/files/DataSet%209/EFTA00095558.pdf) (exec summary) |
| OIG (MCC death) | DOJ Office of Inspector General | Multiple | [EFTA01659612](https://www.justice.gov/epstein/files/DataSet%209/EFTA01659612.pdf) (guard falsification), [EFTA01659557](https://www.justice.gov/epstein/files/DataSet%209/EFTA01659557.pdf) |
| MLAT — UK (Prince Andrew) | OIA / UK Central Authority | 52 docs | [EFTA00022062](https://www.justice.gov/epstein/files/DataSet%208/EFTA00022062.pdf) (MLAT request, April 2020) |
| MLAT — France (Maxwell) | OIA / French authorities | Referenced | [EFTA00023110](https://www.justice.gov/epstein/files/DataSet%208/EFTA00023110.pdf) (December 2020) |
| MLAT — Sweden | OIA / Swedish National Police | 1 doc | [EFTA01684085](https://www.justice.gov/epstein/files/DataSet%209/EFTA01684085.pdf) (January 2020) |
| FCA/PRA (Jes Staley) | UK Financial Conduct Authority | 30+ docs | [EFTA00022164](https://www.justice.gov/epstein/files/DataSet%208/EFTA00022164.pdf) (SDNY-FCA coordination) |
| Congressional — House Judiciary | U.S. House of Representatives | 50+ docs | [EFTA01655861](https://www.justice.gov/epstein/files/DataSet%209/EFTA01655861.pdf) |
| Congressional — House Oversight | U.S. House of Representatives | Multiple | [EFTA01655625](https://www.justice.gov/epstein/files/DataSet%209/EFTA01655625.pdf) (Kash Patel FBI director letter, Feb 2025) |

### 1.12 Sealed Miscellaneous Matters — SDNY

| Case Number | Nature | Corpus Presence |
|-------------|--------|----------------|
| 19-mc-149 | Sealed (related to Epstein/Maxwell) | 13 docs — "All materials under this docket number... will be kept under seal" |
| 19-mc-179 | Sealed (related to Epstein/Maxwell) | Referenced |

### 1.13 Prosecutorial Query Graph Summary

From [`prosecutorial_query_graph.db`](https://github.com/rhowardstone/Epstein-research-data/releases):

| Metric | Value |
|--------|-------|
| Grand jury subpoenas analyzed | 257 |
| Individual demand clauses | 2,018 |
| Subpoenas matched to returns | 133 (51.8%) |
| Subpoenas with no identifiable return | 124 (48.2%) |
| Investigative gaps | 779 (all UNFULFILLED_DEMAND) |
| Subpoena targets include | Financial institutions (FirstBank PR, Wells Fargo, TD Bank, Capital One, UBS), Tech companies (Facebook, Google, Amazon, Lyft), Airlines, MCC, U.S. State Dept, Named individuals (Indyke, Kahn) |

For detailed subpoena analysis, see [PQG Index](../pqg_lines_of_investigation/00_INDEX.md).

---

## PART 2: THE LAWYERS

### 2.1 Epstein's Personal Legal Team (Inner Circle)

These attorneys managed Epstein's day-to-day legal affairs, estate, and business operations.

| Name | Firm | Doc Count | Role | Key EFTAs |
|------|------|-----------|------|-----------|
| **Darren Indyke** | Indyke (solo) | 25,719 | General counsel, co-executor of estate, trustee of 1953 Trust. Most-mentioned lawyer in the corpus by a wide margin. | Privilege log emails ([EFTA02171955](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02171955.pdf)), estate administration |
| **Richard Kahn** | — | 53,083 | Co-executor, trustee, financial administration. The most-mentioned individual in the corpus after Epstein himself. | Financial records, wire authorizations, estate docs |
| **Kathryn Ruemmler** | Latham & Watkins → Goldman Sachs | 9,164 | Listed as backup executor in early 2019 version of Epstein's will (removed before death). Former White House Counsel (2011-2014); Latham & Watkins partner (2014-2020); Goldman Sachs GC (2021-2026, [announced departure Feb 2026](https://www.npr.org/2026/02/13/nx-s1-5713309/goldman-sachs-epstein-ties-resignation) following EFTA email revelations, effective June 30, 2026). | See [Ruemmler Deep Dive](../individuals/RUEMMLER_DEEP_DIVE.md) |
| **Erika Kellerhals** | Solo (USVI tax law) | 4,809 | USVI immigration/tax attorney. Received $23M+ in documented payments. | USVI residency, tax planning, Southern Trust |
| **Robert Glassman** | — | 634 | Personal/business counsel | Referenced across business documents |
| **Alan Grubman** | Grubman Shire | 205 | Entertainment/media lawyer; personal relationship | Referenced in emails |
| **Dlugash** (full name varies) | — | 1,251 | Estate planning, tax | Settlement agreements, trust documents |

### 2.2 The NPA Defense Army (2006-2008)

Assembled to fight the SDFL federal investigation. Acosta called them "an army of legal superstars." Nearly all were criminal defense specialists — a fact the corpus makes explicit.

| Name | Firm | Doc Count | Specialty | Notes |
|------|------|-----------|-----------|-------|
| **Alan Dershowitz** | Kirkland & Ellis → solo | 2,212 | Criminal appellate, constitutional law | Harvard Law professor. Threatened Acosta: "I would be the subject of a chapter in a book on prosecutorial overreach" ([EFTA00009116](https://www.justice.gov/epstein/files/DataSet%207/EFTA00009116.pdf), p. 391). Later named as abuser by Virginia Giuffre; denied allegations. |
| **Kenneth Starr** | Kirkland & Ellis | 1,395 | Former Solicitor General, former independent counsel (Whitewater) | Argued against federal prosecution in letters to SDFL ([EFTA01659896](https://www.justice.gov/epstein/files/DataSet%209/EFTA01659896.pdf)). Died September 2022. |
| **Jay Lefkowitz** | Kirkland & Ellis | 1,652 | Former deputy assistant to the President | Negotiated NPA drafts with AUSA Villafana. Argued "insufficient evidence" Epstein targeted minors ([EFTA00013811](https://www.justice.gov/epstein/files/DataSet%208/EFTA00013811.pdf)). |
| **Gerald Lefcourt** | Lefcourt (solo) | 670 | Criminal defense | NY criminal defense attorney |
| **Jack Goldberger** | Atterbury Goldberger Weiss, P.A. | 4,560 | FL criminal defense | Primary FL defense counsel. NPA implementation correspondence ([EFTA01659770](https://www.justice.gov/epstein/files/DataSet%209/EFTA01659770.pdf)–01659773). Firm appears in 1,877 docs. |
| **Roy Black** | Black Srebnick Kornspan & Stumpf, P.A. | 1,546 | FL criminal defense | "Miami's best criminal defense lawyer." Firm appears in 994 docs. Listed on CVRA Certificates of Service. |
| **Lilly Ann Sanchez** | Fowler White Burnett, P.A. | 1,006 | FL defense | Managed privilege logs per email reminders ([EFTA02171955](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02171955.pdf)). |
| **Guy Lewis** | Lewis Tein, P.L. | 169 | Former USAO chief (SDFL) | "Prosecutors that formerly worked in the U.S. Attorney's Office" (Acosta, [EFTA00009116](https://www.justice.gov/epstein/files/DataSet%207/EFTA00009116.pdf)) |
| **Joseph Ackerman** | Fowler White Burnett, P.A. | 1,107 | FL defense | Signed Certificates of Service in victim civil suits ([EFTA00592983](https://www.justice.gov/epstein/files/DataSet%209/EFTA00592983.pdf)). Firm total: 2,116 docs. |

**The Kirkland & Ellis nexus**: 3,824 pages reference Kirkland & Ellis. The firm provided three of Epstein's most prominent defenders (Dershowitz, Starr, Lefkowitz). William Barr, who served as Attorney General when Epstein died in custody (August 2019), was formerly of counsel to Kirkland & Ellis.

### 2.3 Maxwell Defense Team

| Name | Firm | Doc Count | Role |
|------|------|-----------|------|
| **Laura Menninger** | Haddon Morgan Foreman | 1,156 | Lead trial counsel |
| **Jeffrey Pagliuca** | Haddon Morgan Foreman | 1,098 | Co-counsel |
| **Christian Everdell** | Cohen & Gresser | 1,058 | Co-counsel |
| **Mark Cohen** | Cohen & Gresser | 166 (by full name) | Lead counsel (pre-trial) |
| **Bobby Sternheim** | Sternheim & Sternheim | 804 | Co-counsel |
| **David Bruck** | — | 210 | Sentencing specialist |

Firm totals: Haddon Morgan Foreman — 1,447 docs. Cohen & Gresser — 1,495 docs.

### 2.4 Victim Attorneys

| Name | Firm | Doc Count | Clients/Role | Notes |
|------|------|-----------|--------------|-------|
| **Brad Edwards** | Edwards & Pottinger (later Edwards Henderson) | 3,317 | Lead victim attorney, CVRA pioneer | Counter-sued by Epstein (see §1.6). Firm: 555 docs. |
| **Paul Cassell** | University of Utah (pro bono) | 2,895 | CVRA specialist | Filed original CVRA challenge to NPA. Constitutional law scholar. |
| **Jack Scarola** | Searcy Denney Scarola Barnhart & Shipley | 1,972 | Victim civil suits | Told Judge Crow "all lawsuits were settled for very substantial sums" ([EFTA01480957](https://www.justice.gov/epstein/files/DataSet%209/EFTA01480957.pdf)). Firm: 1,817 docs. |
| **Sigrid McCawley** | Boies Schiller Flexner | 736 | Giuffre v. Maxwell | Lead counsel for Virginia Giuffre in defamation suit |
| **David Boies** | Boies Schiller Flexner | 370 | Giuffre v. Maxwell | Chairman of BSF. Became embroiled in the "Patrick Kessler" affair (2019): a man claiming to possess Epstein sex tapes approached Boies and Pottinger; Boies reported the contact to the FBI. No criminal charges resulted but ethics questions were raised. Firm: 1,423 docs. |
| **Stan Pottinger** | Edwards & Pottinger | 633 | Victim attorney | Also involved in the "Kessler" affair. Discussed using promised videos in litigation; "Kessler" turned out to be a fraud who never produced tapes. No criminal charges filed. Pottinger later died (age 84). |
| **Gloria Allred** | Allred Maroko & Goldberg | 285 | Victim representation | |
| **Jeanne Christensen** | Wigdor LLP | 41 | Leon Black victims | Emailed SDNY: "outrageous that criminal charges have not been brought against [Black]" ([EFTA02731473](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731473.pdf)). Firm: 84 docs. |
| **Spencer Kuvin** | Leopold Kuvin (formerly Ricci Leopold) | 565 | Victim representation | FL victim civil suits |
| **Theodore Leopold** | Ricci Leopold, P.A. (now Leopold Kuvin) | 533 | Victim representation | |
| **Stuart Mermelstein** | Mermelstein & Horowitz, P.A. | 670 | Victim representation | Firm: 362 docs |
| **Adam Horowitz** | Mermelstein & Horowitz, P.A. | 529 | Victim representation | |
| **Jeffrey Herman** | Herman Law | 226 | Victim representation | |
| **Jay Howell** | Jay Howell & Associates | 282 | Victim representation | |
| **Kara Rockenbach** | Link & Rockenbach / Burlington & Rockenbach | 457 | Appellate counsel | |
| **Scott Link** | Link & Rockenbach | 474 | Epstein defense (appellate) | |
| **Brittany Henderson** | Edwards Pottinger LLC | 246 | Victim representation | |
| **David Vitale** | Searcy Denney Scarola | 212 | Victim representation | |
| **Gary Farmer Jr.** | Farmer Jaffe Weissing Edwards Fistos & Lehrman | 250 | Edwards' defense (Epstein v. Edwards) | |
| **Kevin Boyle** | Panish Shea & Boyle | 19 | Maxwell victim representation | |
| **Motley Rice LLC** | — | 19 | USVI victim claims | |

### 2.5 Prosecutors & Government Lawyers

#### SDNY — Epstein/Maxwell Prosecution Team

| Name | Title | Doc Count |
|------|-------|-----------|
| **Geoffrey S. Berman** | U.S. Attorney, SDNY (2018-2020) | 461 |
| **Audrey Strauss** | Acting U.S. Attorney (2020-2021) | 756 |
| **Maurene Comey** | AUSA, lead trial prosecutor | 394 |
| **Alison Moe** | AUSA, co-prosecutor | 423 |
| **Alexander Rossmiller** | AUSA, co-prosecutor | 173 |
| **Nicolas Roos** | AUSA, BOP interviews | 46 |
| **Rebekah Donaleski** | AUSA, MCC interviews | 31 |
| **Damian Williams** | U.S. Attorney (2021-2025) | 310 |
| **Jason Swergold** | AUSA, MCC conditions/FOIA | 13 |
| **Lara Pomerantz** | AUSA | 315 |
| **Andrew Rohrbach** | AUSA | 327 |

#### SDFL — NPA Negotiation Team

| Name | Title | Doc Count |
|------|-------|-----------|
| **R. Alexander Acosta** | U.S. Attorney, SDFL | 2,290 |
| **A. Marie Villafana** | AUSA, lead investigator | 826 |
| **Andrew Lourie** | AUSA | 51 |
| **Dexter Lee** | AUSA | 376 |

Note: Acosta resigned as Secretary of Labor in July 2019 over NPA controversy. Villafana's name is frequently OCR-garbled as "Villafalia" or "Villafaila."

#### The Bruce Reinhart Trajectory

Bruce Reinhart (323 docs) appears in the corpus in two capacities: first as an AUSA in SDFL (1996-2008), then as a private attorney who resigned from the USAO on January 1, 2008, and was retained by Epstein the very next day to represent Sarah Kellen and other Epstein employees/co-conspirators who received NPA immunity. He was later appointed U.S. Magistrate Judge for the SDFL (sworn in March 14, 2018). The OPR investigated his "possible involvement in the Epstein matter" ([EFTA01657803](https://www.justice.gov/epstein/files/DataSet%209/EFTA01657803.pdf)).

#### State/Territory Prosecutors

| Name | Title | Doc Count |
|------|-------|-----------|
| **Barry Krischer** | State Attorney, Palm Beach County | 368 |
| **Denise George** | Attorney General, USVI | 47 |
| **David Aronberg** | State Attorney, 15th Judicial Circuit FL | 7 |
| **Bruce Colton** | State Attorney, 19th Judicial Circuit FL (DeSantis appointee) | 4 |
| **Cy Vance** | Manhattan DA | 83 |

### 2.6 Judges

#### Federal — District

| Judge | Court | Doc Count | Primary Role |
|-------|-------|-----------|--------------|
| **Kenneth A. Marra** | SDFL | 6,451 (name) / 228 (full reference) | CVRA enforcement, victim civil suits. Most-referenced Epstein-case judge. |
| **Alison J. Nathan** | SDNY | 1,265 | Maxwell trial. Ruled on victim anonymity. |
| **Richard M. Berman** | SDNY | 264 | Epstein bail hearing, death aftermath. |
| **Colleen McMahon** | SDNY (Chief) | 71 | Ex parte proceedings — government obtained Giuffre deposition. Maxwell defense alleged government "misled" McMahon. |
| **Loretta Preska** | SDNY | 135 | Giuffre v. Maxwell unsealing after Judge Sweet's death. |
| **Robert W. Sweet** | SDNY | 17 | Original Giuffre v. Maxwell judge (deceased). |
| **Paul Engelmayer** | SDNY | 4 | Grand jury records unsealing. |
| **Linnea R. Johnson** | SDFL (Magistrate) | 119 | Marra case referrals. |

#### Federal — Magistrate (Search/Arrest Warrants)

| Judge | Court | Doc Count | Role |
|-------|-------|-----------|------|
| **Barbara Moses** | SDNY | 95 | Signed Epstein arrest warrant (July 6, 2019), first search warrant for 9 East 71st St. |
| **Henry B. Pitman** | SDNY | 59 | Authorized additional NYC residence search (July 11, 2019). |
| **Kevin Nathaniel Fox** | SDNY | 19 | Electronic device search warrants (July 14, 2019). |
| **Ruth Miller** | SDNY | 27 | Little Saint James (USVI) search warrant. |
| **Sarah Netburn** | SDNY | 29 | Sealed proceedings, unsealing rulings. |
| **James L. Cott** | SDNY | 8 | Warrants, Dennis cyberstalker complaint. |
| **Debra Freeman** | SDNY | 18 | Maxwell civil stays. |

#### Florida State

| Judge | Court | Doc Count | Role |
|-------|-------|-----------|------|
| **Deborah Dale Pucillo** | 15th Judicial Circuit | 178 | Accepted Epstein's FL guilty plea. "After Circuit Judge Pucillo accepted the plea, he was fingerprinted... then handcuffed." |
| **Jeffrey Colbath** | 15th Judicial Circuit | 64 | Unsealed NPA/federal deal documents. |
| **David Crow** | 15th Judicial Circuit | 65 | Heard settlement matters. |
| **Sandra K. McSorley** | 15th Judicial Circuit | 36 | Probation/work release orders. |
| **Bill Berger** | 15th Judicial Circuit (former) | 42 | Former judge turned victim advocate: "Everybody was in on this deal except the victims and the public." |
| **Luis Delgado** | FL Circuit | Referenced | Unsealed NPA-era documents (2024-2025). |

### 2.7 Estate & Trust Lawyers

| Name/Firm | Doc Count | Role | Notes |
|-----------|-----------|------|-------|
| **Brad Karp / Paul, Weiss, Rifkind, Wharton & Garrison** | 1,898 (Karp) / 2,805 (firm) | Estate litigation defense, personal advisor | Chairman of Paul Weiss. Also retained by Leon Black for fee disputes with Epstein. |
| **Alan Halperin** | 2,039 | Paul Weiss — estate/GRAT valuations | |
| **Matthew Menchel / Kobre & Kim** | 937 (Menchel) / 970 (firm) | International asset recovery/offshore | |
| **Deborah Pechet Quinan** | 558 | Riemer & Braunstein (RIW) — Trusts & Estates | |
| **Carlyn McCaffrey** | 533 | McDermott Will & Emery — Trusts & Estates | |
| **Dlugash** | 1,251 | Estate planning, tax trusts | Settlement agreement from 2000 ([EFTA01917842](https://www.justice.gov/epstein/files/DataSet%209/EFTA01917842.pdf)) |
| **Robert Josefsberg** | 1,004 | Podhurst Orseck, P.A. — served as Special Master (NPA) | |
| **Weil Gotshal & Manges** | 78 | Estate-related | |
| **Cooley LLP** | 115 | Estate-related | |

### 2.8 Third-Party & Peripheral Counsel

| Name/Firm | Doc Count | Role/Context | Notes |
|-----------|-----------|--------------|-------|
| **Gary Bloxsome / Blackfords LLP** | 45 / 57 | Prince Andrew's UK counsel | Systematic obstruction of SDNY interview requests. "The DOJ's dealings with the Duke of York have not been designed to seek his assistance" ([EFTA00019885](https://www.justice.gov/epstein/files/DataSet%208/EFTA00019885.pdf)). |
| **Peter Mandelson / Global Counsel LLP** | 5,530 / 833 | Political consulting/legal advisory | Former UK First Secretary of State. 833 docs reference "Global Counsel" — the nature of legal work for Epstein remains undetermined. |
| **Aileen Josephs** | 18 | Immigration attorney | USVI immigration matters |
| **Arda Beskardes** | 738 | Immigration lawyer (NY-based) | |
| **Marc Nurik** | 928 | Defense counsel (Rothstein) | Represented Scott Rothstein in Epstein v. Edwards/Rothstein |
| **Sullivan & Cromwell** | 425 | Role undetermined | |
| **Akin Gump** | 433 | Role undetermined | |
| **Skadden Arps** | 194 | Role undetermined | |
| **Davis Polk** | 172 | Role undetermined | |
| **Dechert LLP** | 77 | Apollo independent report | |
| **Martin O'Connor** | 311 | O'Connor, Morss & O'Connor, P.C. — NJ estate/property matters | |
| **Erica Dubno** | 505 | Appellate counsel | |
| **Thomas Scott / Steven Safra** | 127 / 75 | Cole, Scott & Kissane, P.A. — Dershowitz defense counsel (Giuffre v. Dershowitz) | |
| **Benito Romano** | 253 | Former U.S. Attorney SDNY | |
| **Lanna Belohlavek** | 340 | Assistant State Attorney, Palm Beach County | |
| **Jeffrey Sloman** | 134 | U.S. Attorney, SDFL (successor to Acosta) | |
| **Michael Genovese** | 53 | Referenced in legal filings | |

### 2.9 Under-Investigated Firms

These firms have substantial corpus presence but their role in the Epstein legal universe has not been fully attributed:

| Firm | Doc Count | Known Context |
|------|-----------|---------------|
| **Burman Critton Luttier & Coleman** | 1,663 | Robert Critton (2,037 docs) and Michael Pike (991 docs) appear on Certificates of Service as Epstein FL defense counsel in victim civil suits |
| **Rothstein Rosenfeldt Adler** | 1,665 | Scott Rothstein's disbarred Ponzi scheme firm; Epstein counter-suit defendant. Brad Edwards was initially at this firm before its 2009 collapse. |
| **Tonja Haddad, P.A. / Fred Haddad, P.A.** | 1,184 / 1,599 | Tonja Haddad Coleman and Fred Haddad appear in defense and victim civil dockets |
| **Sullivan & Cromwell** | 425 | Role undetermined — likely financial institution counsel |
| **Akin Gump** | 433 | Role undetermined |

Note: **Steptoe & Johnson** (802 docs) — previously listed as "role undetermined" — is now attributed: it is Reid Weingarten's firm, Epstein's lead criminal defense counsel for the SDNY 2019 case.

### 2.10 Co-Conspirators, Cooperators, and Immunity Recipients

**Named co-conspirators in the NPA**:
Per [EFTA01656152](https://www.justice.gov/epstein/files/DataSet%209/EFTA01656152.pdf): "Non Prosecution Agreement covering Epstein, 4 co-conspirators ([names redacted]) and Lesley Groff and any potential co-conspirators."

Public-record named accomplices (not victims — these are perpetrators identified in court filings):
- **Ghislaine Maxwell** — convicted 2021, sentenced to 20 years
- **Sarah Kellen** — "named accomplice in Epstein's 2008 plea deal, which shielded her from prosecution" ([EFTA01654937](https://www.justice.gov/epstein/files/DataSet%209/EFTA01654937.pdf)). Participated in two proffer sessions (November-December 2019, [EFTA01625916](https://www.justice.gov/epstein/files/DataSet%209/EFTA01625916.pdf)).
- **Nadia Marcinkova** — named in NPA immunity provision
- **Lesley Groff** — explicitly named in NPA text
- **Adriana Ross** — named in NPA immunity provision

**Cooperating witness — Alfredo Rodriguez**:
Epstein household manager who attempted to sell Epstein's "black book" for $50,000 to a cooperating witness after testifying under oath he didn't possess it. Convicted of obstruction (10-80015-CR-MARRA). Rodriguez also reported "lists of hundreds of additional victims" ([EFTA00207048](https://www.justice.gov/epstein/files/DataSet%209/EFTA00207048.pdf)). Died of cancer while serving sentence.

**Steven Hoffenberg** — named Epstein as "uncharged co-conspirator" in Towers Financial Corporation fraud ([EFTA01386750](https://www.justice.gov/epstein/files/DataSet%209/EFTA01386750.pdf)). Told grand jury Epstein was the "technical" person ([EFTA01334040](https://www.justice.gov/epstein/files/DataSet%209/EFTA01334040.pdf)). Hoffenberg served 18 years for fraud. Died August 2022.

---

## PART 3: CROSS-CUTTING ANALYSIS

### 3.1 Criminal Lawyers for Civil Cases

The corpus confirms this pattern unambiguously. In the CVRA case (08-80736-CIV-MARRA) — a *civil* proceeding under the Crime Victims' Rights Act — the Certificate of Service literally labels Epstein's attorneys as **"Criminal Defense Counsel for Jeffrey Epstein"** ([EFTA01099482](https://www.justice.gov/epstein/files/DataSet%209/EFTA01099482.pdf), p. 19; see also [EFTA01098253](https://www.justice.gov/epstein/files/DataSet%209/EFTA01098253.pdf), p. 10):

- Roy Black, Esq. (Black Srebnick Kornspan & Stumpf — *criminal defense firm*)
- Jay P. Lefkowitz (Kirkland & Ellis — *policy/appellate*)
- Martin G. Weinberg, P.C. — *criminal defense*

That caption is not interpretive. The documents themselves label criminal defense lawyers as such on civil filings. The same team appeared in the Epstein v. Edwards/Rothstein counter-suit (a civil case), in victim civil suits, and in NPA negotiations. The Fowler White Burnett team (Ackerman, Sanchez) bridged both dockets, filing motions in victim suits while managing criminal-case privilege logs ([EFTA02171955](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02171955.pdf)).

### 3.2 Conflicts of Interest Map

The Epstein legal universe contains an unusual density of role-crossing, boundary-blurring, and outright conflicts:

**Dershowitz**: NPA defense team negotiator → named by Virginia Giuffre as abuser → defamation defendant → victim-plaintiff who settled with Giuffre (2024). Denied all allegations.

**David Boies / Stan Pottinger**: Victim attorneys (Boies Schiller represented Giuffre) → embroiled in the "Patrick Kessler" affair where a fraudster claimed to possess Epstein sex tapes; ethics questions raised but no criminal charges resulted.

**Bruce Reinhart**: AUSA in SDFL (1996-2008) → resigned January 1, 2008, retained by Epstein the next day to represent Kellen and other employees/co-conspirators who received NPA immunity → appointed U.S. Magistrate Judge, SDFL (March 2018). OPR investigated his "possible involvement in the Epstein matter" ([EFTA01657803](https://www.justice.gov/epstein/files/DataSet%209/EFTA01657803.pdf)).

**Kathryn Ruemmler**: White House Counsel under Obama (2011-2014) → Latham & Watkins partner (during which period she was listed as backup executor in early 2019 Epstein will, removed before his death) → Goldman Sachs GC (2021-2026, announced departure Feb 2026 after EFTA revelations, effective June 30, 2026). See [Ruemmler Deep Dive](../individuals/RUEMMLER_DEEP_DIVE.md).

**Kirkland & Ellis / William Barr**: Kirkland provided three of Epstein's NPA defense lawyers (Dershowitz, Starr, Lefkowitz). William Barr was formerly of counsel to Kirkland & Ellis. Barr served as Attorney General when Epstein died in MCC custody (August 2019). (238 docs reference "William Barr".)

**Brad Karp / Paul Weiss**: Retained by Leon Black to handle fee disputes with Epstein. (Note: this is Brad *Karp*, not victim attorney Brad *Edwards*; the two are sometimes confused in reporting.)

### 3.3 The Privilege Architecture

The corpus reveals the scale of attorney-client privilege deployment:

| Category | Page Count |
|----------|------------|
| Pages invoking attorney-client privilege | 548,831 |
| Privilege log pages | 2,636 |
| Motions to quash | 811 |
| "CERTIFICATE OF SERVICE" pages | 2,385 |
| "Esq" / "Esquire" pages | 18,515 |

**548,831 pages** — roughly 20% of the entire 2.91M-page corpus — invoke attorney-client privilege. This extraordinary volume reflects the dual reality of the Epstein archive: it is simultaneously a criminal investigation file and a record of the legal apparatus built to resist that investigation.

Privilege log management was an active, ongoing process. Emails show Darren Indyke receiving calendar reminders: "remind D: Privilege log re attorney's bills, Lilly to advise" ([EFTA02171955](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02171955.pdf)) — referencing Lilly Ann Sanchez's role in managing privilege assertions.

### 3.4 Attorney Payment Flows

Documented legal fees identifiable in the corpus:

| Lawyer/Firm | Amount | Source |
|-------------|--------|--------|
| **Erika Kellerhals** | $23M+ (plus $75K additional) | USVI tax/immigration work — see financial investigations |
| **$526,000 attorney representative payment** | $526,000 | NPA compliance — "paid to attorney representative" ([EFTA01657823](https://www.justice.gov/epstein/files/DataSet%209/EFTA01657823.pdf)) |
| **Victim attorney fees (NPA condition)** | Undisclosed | NPA required Epstein to pay victim attorney fees preceding litigation |

The full scope of Epstein's legal spending is not determinable from this corpus alone. Wire transfers to law firms in the Deutsche Bank records (DS8) would require systematic extraction to quantify — a task better suited to the financial investigation workbench.

### 3.5 The Lawyer Count

Acosta described Epstein's team as "an army of legal superstars." Media reports have cited a figure of "no fewer than 75 lawyers," though the original source for that specific number has not been definitively traced. It may derive from a reporter's count of counsel of record across all proceedings.

From corpus evidence alone, this report identifies:

| Category | Count |
|----------|-------|
| Epstein personal/business counsel | 7 |
| NPA defense team (2006-2008) | 9 |
| SDNY 2019 defense team additions | 3 |
| Additional FL defense counsel | 6+ |
| Maxwell defense team | 6 |
| Estate/trust lawyers | 9+ |
| Third-party/peripheral counsel | 12+ |
| **Total Epstein-side lawyers** | **52+** |
| Victim attorneys | 20+ |
| Federal prosecutors (SDNY + SDFL) | 17+ |
| State/territory prosecutors | 6+ |
| Judges | 25+ |
| **Grand total named legal actors** | **120+** |

The 52+ Epstein-side lawyers identified here are a floor, not a ceiling. Many attorneys appear only in redacted or abbreviated form in the corpus. Under-investigated firms (Sullivan & Cromwell at 425 docs, Akin Gump at 433) may contain additional lawyers acting on Epstein's behalf whose names have not yet been extracted.

---

## METHODOLOGY

### Data Sources

1. **full_text_corpus.db** (6.3 GB): All page-level text from the DOJ EFTA production. 1,416,711 documents, 2,914,901 pages. FTS5 full-text search index.
2. **prosecutorial_query_graph.db** (2.5 MB): 257 subpoenas, 2,018 demand clauses, 779 investigative gaps.
3. **concordance_complete.db** (729 MB): Cross-reference metadata including author/custodian fields.
4. **persons_registry.json**: 1,536 persons, 42 in "legal" category.
5. **Existing reports**: PROSECUTION_FAILURES_ANALYSIS.md, RUEMMLER_DEEP_DIVE.md, PQG Index.

### Counting Convention

**"Doc Count"** throughout this report means: the number of distinct EFTA documents in [`full_text_corpus.db`](https://github.com/rhowardstone/Epstein-research-data/releases) that contain at least one match to the entity's search string. Computed as `COUNT(DISTINCT efta_number) FROM pages WHERE text_content LIKE '%SearchTerm%'`. **"Pages"** means page-level matches (a single multi-page document may contribute multiple page hits). Unless otherwise noted, all figures are doc counts, not page counts.

### Disambiguation Rules

High-collision surnames are flagged where they affect reported counts. The following entities require context-aware resolution:

| Entity | Collision risk | Resolution used | Impact |
|--------|---------------|-----------------|--------|
| **Richard Kahn** | "Kahn" appears in financial records (bank names, other individuals) | Searched `"Richard Kahn"` or `"Kahn, Richard"` where possible; raw `"Kahn"` count (53,083) is noted as inflated | Kahn doc count likely overstated by 2-5x |
| **Roy Black** | Overlaps with Leon Black, generic "black" | Searched `"Roy Black"` or `"Black, Roy"` | Count (1,546) is reasonably clean |
| **Mark Cohen** | Extremely common name | Searched `"Mark Cohen"` — low-confidence count (166) | Likely includes false positives; firm count (Cohen & Gresser, 1,495) is more reliable |
| **Paul Morris** | Common name | Excluded — raw count (12,450) is almost entirely false positives | Not reported as a lawyer |
| **David Boies** | Unique enough | `"David Boies"` | Clean (370) |

For all other names, the search string is the full name or distinctive surname. Where a firm name is available, the firm-level count is the more reliable metric.

### Extraction Methods

- **Lawyer names**: "Esq" / "Esquire" pattern extraction (18,515 pages), "Bar No" / "admitted to practice" searches (3,323 pages), Certificate of Service extraction (2,385 pages), persons_registry.json seed list (42 "legal" entries), concordance author/custodian fields (found to be sparse and not useful — mostly software metadata).
- **Law firms**: Pattern matching on "LLP", "P.A.", "P.C.", "& Associates", "Law Offices of" (firm-by-firm verification with doc counts).
- **Cases**: Case number extraction (`-cv-`, `-cr-`, `-mc-`, `Case No`, `CF`), caption extraction (`v.` patterns on page 1), PQG database records.
- **Judges**: "Honorable", "Judge", "Magistrate" pattern extraction with context windows.
- **Prosecutors**: "AUSA", "Assistant United States Attorney", "State Attorney", "Attorney General" pattern extraction.

### Limitations

- Doc counts are approximate and subject to the disambiguation rules above. For entities with common names, prefer firm-level counts.
- Redacted names in NPA co-conspirator provisions cannot be attributed.
- 27 fully-redacted subpoena targets in the PQG remain unidentified.
- Concordance author/custodian fields were sampled and found mostly empty (software usernames, not substantive attributions).
- Under-investigated firms (§2.9) require additional deep-reading to determine Epstein-relationship.

### Document URL Format

All EFTA citations link to the DOJ's public release:
```
https://www.justice.gov/epstein/files/DataSet%20{N}/EFTA{NUMBER}.pdf
```
Dataset numbers were verified against [`full_text_corpus.db`](https://github.com/rhowardstone/Epstein-research-data/releases) for every cited document. Documents confirmed removed from justice.gov (per CONFIRMED_REMOVED.csv) are not linked.

---

## SEE ALSO

- [Prosecution Failures Analysis](./PROSECUTION_FAILURES_ANALYSIS.md) — detailed NPA history, named individuals who escaped prosecution
- [Ruemmler Deep Dive](../individuals/RUEMMLER_DEEP_DIVE.md) — White House → Epstein → Goldman Sachs
- [Grand Jury Subpoena Analysis](../pqg_lines_of_investigation/00_INDEX.md) — 257 subpoenas, 779 investigative gaps
- [FBI 302 Missing Serials Dossier](./FBI_302_MISSING_SERIALS_DOSSIER.md) — gaps in the FBI investigative record
- [Death Investigation Document Removal](./DEATH_INVESTIGATION_DOCUMENT_REMOVAL.md) — MCC death investigation records
- [DOJ Document Removal Audit](./DOJ_DOCUMENT_REMOVAL_AUDIT.md) — 64,259 documents removed from justice.gov
- [CBP Corruption Investigation](./CBP_CORRUPTION_INVESTIGATION.md) — customs/immigration angle
- [STT Aviation Infrastructure](./STT_AVIATION_INFRASTRUCTURE_CONTROL.md) — USVI aviation/travel records
