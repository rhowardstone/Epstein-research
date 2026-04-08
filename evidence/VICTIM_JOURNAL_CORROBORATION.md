# The Victim Journal: A Corroboration Analysis

**Date**: April 7, 2026
**Databases**: [`full_text_corpus.db`](https://github.com/rhowardstone/Epstein-research-data/releases) (6.3 GB, 1.42M documents, 2.91M pages), [`concordance_complete.db`](https://github.com/rhowardstone/Epstein-research-data/releases) (729 MB)
**Standard**: Every factual claim supported by EFTA document number with [justice.gov](https://www.justice.gov/epstein) URL, or external source URL. Proposed identifications are clearly labeled by confidence level. No identification is asserted as fact unless confirmed by multiple independent sources.
**Methodology**: Full-text search (FTS5 + LIKE) across 2,914,901 pages; cross-reference with persons_registry.json (1,538 persons); external source verification via web search
**Source reliability**: The journal is a first-person victim narrative submitted as a litigation exhibit. It is treated as Tier 3 evidence (personal account, unverified) unless independently corroborated by Tier 1 sources (court filings, FBI 302s, sworn testimony). Each name entry below states what the journal claims, what the corpus independently shows, and what remains unverified.

---

## Table of Contents

1. [What the Journal Is](#1-what-the-journal-is)
2. [How It Entered the Record](#2-how-it-entered-the-record)
3. [The Encoding Method](#3-the-encoding-method)
4. [Complete Name Inventory](#4-complete-name-inventory)
5. [Corroboration Analysis: Names with Independent Evidence](#5-corroboration-analysis-names-with-independent-evidence)
6. [Possible Public Matches for Washington-Area Names](#6-possible-public-matches-for-washington-area-names)
7. [Names Without Independent Corpus Evidence](#7-names-without-independent-corpus-evidence)
8. [What the Journal Does Not Prove](#8-what-the-journal-does-not-prove)
9. [Structural Findings](#9-structural-findings)
10. [Methodology](#10-methodology)

---

## 1. What the Journal Is

Four documents in the DOJ's EFTA production contain a coded handwritten journal and its typed translations, attributed in the record to a victim alleging abuse within Epstein's trafficking operation. The documents describe abuse occurring approximately 2001–2004, based on internal dating evidence (National Geographic clippings from September 2003 and June 2004; references to high school attendance; the victim turning 17 during the period described).

| Document | Pages | Type | Dataset |
|----------|-------|------|---------|
| [EFTA02731361](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731361.pdf) | 32 | Coded journal + typed translation, interleaved | DS12 |
| [EFTA02731393](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731393.pdf) | 17 | Coded journal + typed translation, interleaved | DS12 |
| [EFTA02731420](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731420.pdf) | 13 | Typed translation only | DS12 |
| [EFTA02731465](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731465.pdf) | 8 | Typed translation only | DS12 |

An earlier production copy of the translation exists at [EFTA00155037](https://www.justice.gov/epstein/files/DataSet%209/EFTA00155037.pdf) (DS9, 15 pages), confirming the document was in government possession prior to the DS12 release. All copies are marked "CONFIDENTIAL FOR ATTORNEY'S EYES ONLY / DO NOT COPY."

The journal describes forced pregnancies, forced abortions, trafficking to named individuals in Washington DC, New York, Palm Beach, the Bahamas, and New Mexico, and the removal of a newborn child approximately 15 minutes after birth. These descriptions are graphic and consistent across all four documents.

This analysis relies on the typed translations as produced in the EFTA record. Where coded originals are available, they can be checked against the translations, but for many key passages — including those naming specific individuals — the original coded pages are not publicly available. See [Section 9.1](#91-missing-coded-originals).

---

## 2. How It Entered the Record

The EFTA range surrounding the journal (EFTA02731473–02731490) contains correspondence between Wigdor LLP and the Southern District of New York. [EFTA02731490](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731490.pdf) states that the attorneys "shared the 2012 journal with you" and that "there are two PDFs (the entirety of the journal and a 'translation')."

[EFTA02731488](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731488.pdf) contains SDNY attorney notes from a May 26, 2023 phone call with Wigdor LLP partner Jeanne Christensen, recording allegations from Christensen's client. SDNY's response, documented in [EFTA02731478](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731478.pdf) (June 12, 2023 notes from a follow-up call with Christensen), indicates the office had "not opened an investigation" and would "get back to JC if our Office ends up moving forward."

The victim does not appear in the FBI serial system (the 3501.xxx numbering used to track Miami/SDNY case subjects). She entered the record through DANY (Manhattan District Attorney), not through the FBI.

---

## 3. The Encoding Method

The coded journal pages use a **rail fence cipher** — a transposition cipher where plaintext is written in alternating rows, then read row by row. The journal's method uses two rails: odd-positioned characters on the first line, even-positioned characters on the second.

Verification: interleaving rows from [EFTA02731362](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731361.pdf) (page 2) produces "Close your eyes close your eyes close your eyes," matching the typed translation on page 1.

The journal also employs:
- **Magazine cutout collages** — headlines and clippings arranged to convey messages
- **Annotated Sylvia Plath poems** — "Stillborn" (p. 6), "Edge" (p. 27, with "woman" crossed out and replaced with "girl"), and a 1961 poem about control and possession (p. 7 of EFTA02731393)
- **Underlined words in printed poems** — [EFTA02731428](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731420.pdf) (page 9) describes a page with Plath's "Stopped Dead" where the underlined words read: "birth, cry, fatso millionaire, it's violent, goddamn baby screaming, there's always a bloody baby, your seven chins, still as a ham" — adjacent to the name "Leon Black"

The interleaved documents (EFTA02731361 and EFTA02731393) contain both coded originals and typed translations. The standalone translations (EFTA02731420 and EFTA02731465) cover content whose coded originals are not present in the EFTA production. The Wigdor correspondence confirms the full coded journal was provided to SDNY, but only a portion was included in the public dataset.

---

## 4. Complete Name Inventory

Every name below is quoted directly from the typed translation pages. Page numbers refer to the Bates-stamped EFTA page within each document.

### From [EFTA02731420](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731420.pdf) (typed translation)

| Page | Name as Written | Context (quoted) |
|------|----------------|------------------|
| 1 | Mr. Glickman | "That my mom lied about Mr. Glickman all the time... Now he is dead" |
| 1 | British lady from Clearwater | "She lied about work trips about Michigan and about Clearwater" |
| 2 | Mr. Robert + wife Jill | "Went to a party at this huge house to meet this man named Mr. Robert and his pretty wife Jill" |
| 2 | British lady from Clearwater | "Same exact British lady from Clearwater was there! She talked to me all night" |
| 5 | Mr. Colgan | "Why did Mr. Colgan agree to this!" |
| 5 | Joe Gibbs | "Joe Gibbs is so nice" |
| 5 | Dan Snyder | "Dan Snyder is a pig! A red skin hoggett(sp?)!" |
| 6 | Mr. Dana | "For being a Rockefeller that plane Mr. Dana had me on was scary!" |
| 6 | Larry Summers | "Both he and Larry Summers are fucking disgusting!" |
| 6 | Andrew | "Andrew is like his brother in this way!" / "I guess it is a royal thing" |
| 7 | Mr. Mody | "Mr. Mody. Mr. Robert. Mr. Sant. Mr. Ludwig. Mr. Cecchi. Mr. Mora. Mr. Goodlatte. Mr. Atkins are not who they say! Run run run!" |
| 7 | Mr. Robert | Same passage |
| 7 | Mr. Sant | Same passage |
| 7 | Mr. Ludwig | Same passage |
| 7 | Mr. Cecchi | Same passage |
| 7 | Mr. Mora | Same passage |
| 7 | Mr. Goodlatte | Same passage |
| 7 | Mr. Atkins | Same passage |
| 8 | Mr. Black / Leon Black | "Walk down Madison Avenue to 71st St... Mr. Black is so important... that fat fuck bit me! He threw me on the floor and blood all over Jeffreys carpet" |
| 9 | Leon Black | Plath poem "Stopped Dead" annotated with "Leon Black" — underlined words: "fatso millionaire," "it's violent," "goddamn baby screaming" |
| 12 | Mr. Leonsis | "Whether its with Jeffrey, Mr. Leonsis, Mr. Case, Mr. Snyder, the Gregorys, Mr. Colgan..." |
| 12 | Mr. Case | Same "flights of horror" passage |
| 12 | Mr. Snyder | Same passage |
| 12 | The Gregorys | Same passage |
| 12 | Mr. Colgan | Same passage |
| 12 | George Mitchell | "even old senators like George Mitchell who you think would be good like a grandpa are bad" |
| 12 | Mr. Kimsey | "Mr. Kimsey is deranged" |

### From [EFTA02731465](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731465.pdf) (typed translation)

| Page | Name as Written | Context (quoted) |
|------|----------------|------------------|
| 2 | Ms. Vicki | "I will never be able to forgive myself for not being able to tell you what Ms. Vicki does and what really happens in FL and CA" |
| 2 | Weinstein | "I hope you dont ever meet fat pig Weinstein or the rest" |
| 3 | "the old president" | "Even the old president! They will get you. He should have been thinking of Chelsea!" |
| 3 | Allen Douschewitz | "Disgusting pigs like Allen Douschewitz and Mr. Caruthers and even Mr. Islam will hurt you especially if Ghislaine is busy or not with you!" |
| 3 | Mr. Caruthers | Same passage |
| 3 | Mr. Islam | Same passage |
| 5 | Mr. Krauss | "Mr. Sauerkraut krauss and martin minsky are gross" |
| 5 | Martin Minsky | Same passage |
| 5 | Mr. Novak | "but I felt sort of sorry for Mr. Novak. He was as uncomfortable as me" |
| 5 | Mr. Staley | "The disgusting Mr. staley if anyone ever calls me tinkerbell again I will lose my mind / He left bloody marks on my arms from his belt and thought he had had the right to call me that when he has ears as big as a dumbo" |
| 6 | Mr. Leonsis | "Why would they all allow Mr. Leonsis wait this long? Why would he bring a friend and make a video?" |
| 6 | Mr. Rails | "Mr. Rails and Mr. Ein [clipping: blood on their hands]" |
| 6 | Mr. Ein | Same passage |
| 6 | Mr. Jacobson | "but so does Jeffrey and Mr. Jacobson" |
| 6 | Mr. Conway | "Mr. Conway" |
| 6 | Mr. Vradenberg | "Mr. vradenberg and Bill s." |
| 6 | Bill s. | Same passage |
| 7 | Jeffrey + Ghislaine | "now he and Ghislaine are fighting because I am now over 20 weeks with a baby we are certain is his" |

### From [EFTA02731361](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731361.pdf) (interleaved journal)

| Page | Name as Written | Context (quoted) |
|------|----------------|------------------|
| 9 | Mr. Joe + Mrs. Anne | "Like Maralago and where I see Mr. Joe and Mrs. Anne" |
| 25 | Mr. M | "But only after maybe 15 minutes Mr. M came to take her" (referring to the newborn) |
| 28 | Jean Luc Brunel | "Jean Luc Brunel is a disgusting pig with bad breath" |

### From [EFTA02731393](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731393.pdf) (interleaved journal)

| Page | Name as Written | Context (quoted) |
|------|----------------|------------------|
| 11 | Leon | "The blood from Leon is no longer there" (referring to blood on carpet) |

---

## 5. Corroboration Analysis: Names with Independent Evidence

For each name below, the journal's claim is stated first, followed by what the EFTA corpus independently shows. "Independent" means evidence from a different victim, a different document type, or a different source — not another copy of the same journal.

### 5.1 Leon Black

**Journal claim** ([EFTA02731427](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731420.pdf), p. 8): Black bit the victim at a location on Madison Avenue near 71st Street. Blood on Epstein's carpet. "Who the fuck bites someone?"

**Independent source 1** — [EFTA02731488](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731488.pdf) (p. 1): SDNY attorney notes from a May 26, 2023 phone call with Wigdor LLP partner Jeanne Christensen, recording a **different** client's allegations. The notes state: "Black bites parts of her vagina, violence was arousing for him, very painful for her." The notes describe a separate victim abused by Black for "7 to 8 years." The same notes describe a **third** victim, a 16-year-old minor, who was "violently raped by Black" at Epstein's townhouse, involving sex toys and rectal bleeding.

**Independent source 2** — [EFTA02857849](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02857849.pdf) (pp. 4–5): An FD-302 (FBI interview, August 21, 2020, case NY-3027571) records a Brazilian-born woman's account of being trafficked by Epstein to meet Leon Black in 2004. She saw Black four times, all in New York. The 302 describes Black as "tall, heavy with a large stomach... gray hair, a big nose and a mole on his face." This 302 does not mention biting or physical violence in the Black-specific encounters, but independently confirms that Epstein arranged sexual access to Black for trafficking victims.

**External source** — Cheri Pierson filed a lawsuit against Leon Black under New York's Adult Survivors Act (Wigdor LLP, filed November 2022; case no. 952002/2022, N.Y. Sup. Ct.), alleging that Epstein arranged for her to give Black a massage in 2002 and that Black physically overwhelmed her. Black denied ever meeting Pierson. The case was dismissed with prejudice in February 2024 via stipulation of discontinuance ([Reuters, Feb. 20, 2024](https://www.reuters.com/legal/woman-ends-lawsuit-claiming-leon-black-raped-her-jeffrey-epsteins-mansion-2024-02-20/)). Dismissal with prejudice does not establish the truth or falsity of the allegations. A separate lawsuit by an anonymous plaintiff against Black remains pending. Black is pursuing a malicious prosecution claim against Wigdor LLP.

**What is corroborated**: The record contains multiple independent allegations of violent sexual conduct by Black from different victims transmitted through different channels. The strongest corroboration for biting comes from the journal and the SDNY attorney notes (EFTA02731488); the FBI 302 (EFTA02857849) independently corroborates trafficking to Black but not biting. The Pierson lawsuit alleges a separate assault but does not specifically describe biting. Note that EFTA02731488 records an attorney's account of her client's allegations — it is not sworn testimony or an FBI interview.

**What is not corroborated**: The specific location (Madison Avenue near 71st Street) and the carpet-blood detail are unique to the journal. No other corpus document confirms these specific details.

### 5.2 George Mitchell

**Journal claim** ([EFTA02731431](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731420.pdf), p. 12): "even old senators like George Mitchell who you think would be good like a grandpa are bad."

**Independent source** — [EFTA02857849](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02857849.pdf) (pp. 3–5): The same FD-302 cited above describes the Brazilian victim being trafficked to George Mitchell. She was flown to a presidential suite at the Beverly Hills Hotel where she "met a man named GEORGE MITCHELL" who was on the phone with Epstein. Mitchell was described as "slim and very old... gray hair but not much hair... He told [her] that he worked in politics." She was subsequently sent to the Four Seasons in Washington, DC, where "EPSTEIN sent her to DC."

**What is corroborated**: Two independent victims (the journal author and the Brazilian victim in EFTA02857849) describe Mitchell as elderly and involved in Epstein's trafficking operation. The journal's "like a grandpa" description is independently consistent with the 302's "very old... smiled... very nice."

**What is not corroborated**: The journal does not specify what Mitchell did. The 302 describes sexual encounters. They may describe different types of encounters or the same type.

### 5.3 Jim Atkins

**Journal claim** ([EFTA02731426](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731420.pdf), p. 7): Listed among men who "are not who they say! Run run run!"

**Independent source** — [EFTA02858481](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02858481.pdf) (Serial 252) and [EFTA02858491](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02858491.pdf) (Serial 264): FBI FD-302 interviews with a completely different victim (PROTECT SOURCE / Jane Doe 4) describe "JIM ATKINS (phonetic)" as an Epstein associate who sexually assaulted the witness on multiple occasions and participated in blackmailing her mother. Physical description: white male, gray hair, "big ears," associated with an Ohio university, in his 50s in the early 1980s. Separate research identified a 1986 newspaper listing "Jimmy L. Atkins of Ohio" as the owner of the real estate company described in the 302s (see [OHIO_NODE_INVESTIGATION.md](../individuals/OHIO_NODE_INVESTIGATION.md) for sourcing).

**What is corroborated**: Two independent victims, abused approximately 20 years apart (~1980s and ~2001–2004), name the same associate. "Atkins" appears in exactly four documents across 2.91 million pages: two PROTECT SOURCE FBI 302s, the journal, and one OCR misread.

**What is not corroborated**: Whether the journal's "Mr. Atkins" and the PROTECT SOURCE 302's "Jim Atkins" are the same individual. The name is not common in the corpus (4 total hits), and both appear in the context of Epstein's trafficking network, but positive identification cannot be made from surname alone.

### 5.4 Jes Staley

**Journal claim** ([EFTA02731469](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731465.pdf), p. 5): "The disgusting Mr. staley if anyone ever calls me tinkerbell again I will lose my mind / He left bloody marks on my arms from his belt and thought he had had the right to call me that when he has ears as big as a dumbo."

**Independent sources**: The EFTA corpus contains approximately 7,250 page references to Jes Staley. [EFTA00161693](https://www.justice.gov/epstein/files/DataSet%209/EFTA00161693.pdf) (DS9) reproduces a news item stating that "Staley exchanged more than 1,200 emails with Epstein and that these included photographs of young women sent by the convicted criminal." Multiple direct emails between Epstein and Staley appear in the corpus (EFTA00940747, EFTA00741744, EFTA01301012, among others).

**What is corroborated**: Staley's close, documented relationship with Epstein, including 1,200+ emails and photographs of young women. The UK Financial Conduct Authority investigated Staley over his Epstein relationship, and he resigned as Barclays CEO in 2021.

**What is not corroborated**: The belt marks, the "tinkerbell" nickname, and the physical description ("ears as big as a dumbo") are unique to the journal. No other corpus document describes physical abuse by Staley.

### 5.5 Marvin Minsky

**Journal claim** ([EFTA02731469](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731465.pdf), p. 5): "martin minsky are gross." The first name is misspelled (Martin for Marvin).

**Independent sources**: Direct emails between Minsky and Epstein appear at [EFTA00923827](https://www.justice.gov/epstein/files/DataSet%209/EFTA00923827.pdf) (conference planning) and [EFTA00988093](https://www.justice.gov/epstein/files/DataSet%209/EFTA00988093.pdf) (introduction). [EFTA00564935](https://www.justice.gov/epstein/files/DataSet%209/EFTA00564935.pdf) shows Epstein instructing staff to "coordinate with the Minskys, krause, marvin, church, novak" for a conference. The email is sent to Cecile de Jongh (then-First Lady of the US Virgin Islands), implying the conference was on or near Little Saint James, but the document does not explicitly state the location. The Maxwell deposition ([EFTA02846680](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02846680.pdf), pp. 102–103) confirms Maxwell knew Minsky as part of Epstein's circle.

**What is corroborated**: Minsky's documented relationship with Epstein, including island visits and conference co-planning.

**What is not corroborated**: The abuse allegation is unique to the journal within the EFTA corpus. Virginia Giuffre's 2015 declaration (publicly reported but not as a primary document in the EFTA production) contains a separate allegation about Minsky.

### 5.6 Lawrence Krauss

**Journal claim** ([EFTA02731469](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731465.pdf), p. 5): "Mr. Sauerkraut krauss... are gross."

**Independent sources**: [HOUSE_OVERSIGHT_018227](https://wikiepstein.com/) through HOUSE_OVERSIGHT_018229 (DS99) are Skype call logs between `jeevacation` (Epstein) and `lawkrauss` (Lawrence Krauss) showing direct video calls in July–August 2017. [EFTA00564935](https://www.justice.gov/epstein/files/DataSet%209/EFTA00564935.pdf) lists "krause" alongside "marvin" and "novak" for a conference coordinated through Cecile de Jongh (then-First Lady of the US Virgin Islands).

**What is corroborated**: Krauss's personal relationship with Epstein, including direct video calls and island conference attendance. Note that Krauss was separately investigated for sexual misconduct unrelated to Epstein ([BuzzFeed News, 2018](https://www.buzzfeednews.com/article/peteraldhous/lawrence-krauss-sexual-harassment-allegations)).

**What is not corroborated**: The abuse allegation in the journal is the only claim of Krauss involvement in Epstein's trafficking within the EFTA corpus.

### 5.7 Martin Nowak ("Mr. Novak")

**Journal claim** ([EFTA02731469](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731465.pdf), p. 5): "but I felt sort of sorry for Mr. Novak. He was as uncomfortable as me."

**Proposed identification**: Martin Nowak, director of Harvard's Program for Evolutionary Dynamics (PED). The Polish surname "Nowak" is pronounced with a "v" sound, making the journal's "Novak" a standard phonetic rendering.

**Independent sources**: Epstein donated $6.5 million to establish Nowak's PED at Harvard in 2003 — the exact period of the journal. Epstein maintained a personal office in Nowak's lab and used it over 40 times — all documented visits occurred after 2010, well after his 2008 conviction. Harvard sanctioned Nowak in 2021 and closed the PED; Nowak was placed on administrative leave again in February 2026 ([Harvard Magazine](https://www.harvardmagazine.com/2021/03/martin-nowak-sanctioned-for-jeffrey-epstein-involvement)). [EFTA00564935](https://www.justice.gov/epstein/files/DataSet%209/EFTA00564935.pdf) lists "novak" (same phonetic spelling) alongside Minsky and Krauss for a conference coordinated through Cecile de Jongh in the US Virgin Islands.

**What is corroborated**: Nowak's extensively documented financial and personal relationship with Epstein during the journal's timeframe, including island visits.

**What is not corroborated**: The journal describes Novak as "uncomfortable" — a characterization distinct from the other names, which are described as active participants. This detail neither confirms nor denies involvement; it records the victim's perception. No other corpus document describes Nowak in a trafficking context.

**Identification confidence**: Identity as Harvard's Martin Nowak: HIGHLY PROBABLE. Status as Epstein associate: CONFIRMED. Status as trafficking participant: uncorroborated in the corpus. The phonetic match, the timeline (2003), and the corpus co-listing with Minsky and Krauss — who appear in the same journal sentence — make this the strongest identification among proposed names.

### 5.8 Dan Snyder

**Journal claim** ([EFTA02731424](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731420.pdf), p. 5): "Joe Gibbs is so nice but Dan Snyder is a pig! A red skin hoggett(sp?)!" Also named in the "flights of horror" passage (p. 12).

**Independent source**: [EFTA01416472](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01416472.pdf) (DS10) is an art gallery event list that includes "Dan Snyder and Karl Schreiber — dinner and preview" alongside "Jeffrey Epstein — preview." This places Snyder and Epstein at the same art event, independent of the journal.

**What is corroborated**: Snyder and Epstein attended the same art event. The corpus does not contain further evidence of their relationship.

**What is not corroborated**: The abuse allegation and "flights of horror" are unique to the journal.

### 5.9 Steve Case

**Journal claim** ([EFTA02731431](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731420.pdf), p. 12): Named in the "flights of horror" passage alongside Leonsis, Snyder, the Gregorys, and Colgan.

**Independent sources**: [EFTA02548313](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02548313.pdf) (DS11) is a John Brockman mass email cc'ing Steve Case, Jeff Bezos, Paul Allen, and Jeffrey Epstein. [EFTA02673024](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02673024.pdf) shows a Twitter notification in Epstein's inbox that @SteveCase tweeted.

**What is corroborated**: Case appeared in Epstein's intellectual/social network via Brockman's Edge Foundation circle.

**What is not corroborated**: The abuse allegation and "flights of horror" are unique to the journal. Appearing on the same email list does not establish the type of relationship the journal describes.

### 5.10 Additional Confirmed Names

The following names are extensively documented in the EFTA corpus and require no detailed corroboration analysis here:

- **Alan Dershowitz** ("Allen Douschewitz"): Giuffre depositions, civil case, extensive corpus documentation
- **Bill Clinton** ("the old president... Chelsea"): Flight logs, extensive corpus
- **Prince Andrew** ("Andrew is like his brother in this way"): Civil settlement, sworn testimony
- **Jean-Luc Brunel** ("disgusting pig with bad breath"): Extensive corpus, died in custody February 2022
- **Larry Summers**: Documented Epstein associate, Vicky Ward article ([EFTA01334040](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01334040.pdf))
- **Harvey Weinstein** ("fat pig Weinstein"): Social circle co-occurrence only in corpus; no direct Epstein trafficking connection documented

### 5.11 Dana Chasin ("Mr. Dana")

**Journal claim** ([EFTA02731425](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731420.pdf), p. 6): "For being a Rockefeller that plane Mr. Dana had me on was scary! Both he and Larry Summers are fucking disgusting!"

**Proposed identification**: A Democratic political consultant with documented Rockefeller family ties through marriage and a Washington, DC base.

**Corpus evidence**: The name "Chasin" does not appear anywhere in the 2.91 million-page EFTA corpus. No independent document in the production connects Dana Chasin to Epstein.

**What supports the identification**: The journal describes a "Mr. Dana" who has a plane and a Rockefeller connection. The proposed match is the only publicly known individual named "Dana" with a documented Rockefeller family connection. The combination of first name + Rockefeller + private aircraft is distinctive.

**What is not corroborated**: The journal does not provide a surname. The identification rests entirely on the combination of "Dana" + "Rockefeller" + "plane" matching a single known individual's profile. No EFTA document mentions Chasin in any context. No independent victim, flight log, financial record, or email in the corpus connects Chasin to Epstein.

**Identification confidence**: SPECULATIVE. The combination of identifying details is suggestive, but without any independent corpus evidence, this identification cannot be elevated above speculative.

---

## 6. Possible Public Matches for Washington-Area Names

The journal names several individuals by surname only ("Mr. Rails," "Mr. Ein," etc.) who, if the proposed matches below are correct, correspond to figures in Washington, DC's social and institutional landscape from the early 2000s. This section states each proposed match, the basis for it, and the uncertainty.

**Important**: A proposed match means the named public figure is a possible or plausible candidate based on available evidence. It does not mean the match is confirmed. It does not constitute an allegation of wrongdoing. The journal is a single victim's personal account, and the assessments below are analytical exercises in identifying who the journal's "Mr." surnames may refer to, based on phonetic fit, public records, and — where available — corpus evidence. Social-network coherence among proposed matches is noted where it exists, but network fit alone does not verify an identification or imply participation in abuse.

### 6.1 "Mr. Rails" → Mitchell Rales

**Basis**: Mitchell Rales co-founded Danaher Corporation and is based in the Washington, DC area. He was president of the National Gallery of Art (2019–2024) and co-founded Glenstone museum. He joined the [Washington Commanders ownership group](https://www.commanders.com/team/front-office-roster/ownership-group) alongside Mark Ein (another proposed journal name). House Oversight documents ([HOUSE_OVERSIGHT_005548](https://wikiepstein.com/)) contain a handwritten entry "DEMO flight MITCHEL RALES" on N908GM ("Air Ghislaine") dated July 17, 2008 — 17 days after Epstein's Florida sex crime conviction. [First reported by Kait Justice](https://kaitjustice.substack.com/p/billionaire-mitchell-rales-in-flight).

**Uncertainty**: The journal uses only "Mr. Rails." Mitchell Rales has a brother, Steven Rales, who is also based in the DC area. The surname "Rails" as a phonetic rendering of "Rales" is plausible but not confirmed. The flight log entry establishes Mitchell Rales on an Epstein aircraft in 2008, but the journal describes events from 2001–2004. No corpus document places either Rales brother in a trafficking context.

**Confidence**: PLAUSIBLE for Mitchell Rales based on the documented flight log entry. SPECULATIVE for Steven Rales.

### 6.2 "Mr. Ein" → Mark Ein

**Basis**: Mark Ein is a Washington, DC-based venture capitalist. He appears in the journal alongside "Mr. Rails" in the passage "Mr. Rails and Mr. Ein [clipping: blood on their hands]." Ein and Mitchell Rales are both part of the Washington Commanders ownership group, establishing a documented social connection between the two proposed identifications. The EFTA corpus contains emails forwarding NYJTL (New York Junior Tennis & Learning) event invitations to Epstein's jeevacation@gmail.com that reference Mark Ein as an honorary chair — though these are from 2016, post-journal.

**Uncertainty**: "Ein" is an uncommon but not unique surname. The corpus emails are from 2016 and do not establish a 2001–2004 connection. No corpus document places Ein in a trafficking context.

**Confidence**: PLAUSIBLE.

### 6.3 "Mr. Vradenberg" → George Vradenburg

**Basis**: George Vradenburg (note: the public figure spells it "Vradenburg"; the journal writes "vradenberg") was Executive Vice President for Global and Strategic Policy at AOL Time Warner from January 2001 through late 2003 — precisely the journal's timeframe. He chaired the Phillips Collection for 14 years (2002–2016) and is a member of the Council on Foreign Relations and the Economic Club of Washington. He appears in the journal alongside "Mr. Rails" and "Mr. Ein."

**Uncertainty**: The spelling differs slightly ("berg" vs "burg"). No corpus document mentions Vradenburg outside the journal. No public record connects him to Epstein.

**Confidence**: POSSIBLE, based on the near-exact phonetic match and the AOL/DC milieu. No independent evidence connects Vradenburg to Epstein.

### 6.4 "Mr. Kimsey" → James V. Kimsey

**Basis**: James V. Kimsey (1939–2016) was the co-founder and first CEO of America Online (AOL). He was a major Washington, DC philanthropist and social figure. The journal states "Mr. Kimsey is deranged." He appears in the same "flights of horror" passage as Mr. Case (Steve Case was AOL's co-founder and succeeded Kimsey as CEO) and Mr. Leonsis (Ted Leonsis was an AOL executive).

**Uncertainty**: No corpus document outside the journal connects Kimsey to Epstein. Kimsey died in 2016. No public record of an Epstein connection exists.

**Confidence**: POSSIBLE, based on the AOL milieu coherence. No independent evidence connects Kimsey to Epstein.

### 6.5 "Mr. Leonsis" → Ted Leonsis

**Basis**: Ted Leonsis was an AOL executive and is the owner of the Washington Capitals and Washington Wizards. The journal names him three times: in the "flights of horror" passage (p. 12 of EFTA02731420), and twice in EFTA02731465 — "Why would they all allow Mr. Leonsis wait this long? Why would he bring a friend and make a video?" and the procedure/blood passage.

**Uncertainty**: No corpus document outside the journal connects Leonsis to Epstein's trafficking. Leonsis appears in incidental financial news in the corpus but not in any Epstein contact record, email, or flight log.

**Confidence**: The identification of "Mr. Leonsis" as Ted Leonsis is straightforward (the surname is uncommon). Whether the person named in the journal is the same Ted Leonsis who is the public sports team owner is unverified by independent corpus evidence.

### 6.6 "Mr. Sant" → Roger Sant (Proposed)

**Basis**: Roger Sant (born 1931) co-founded AES Corporation and was the Smithsonian Institution's first Board Chair (2001–2013). He is a central figure in Washington, DC philanthropy. His wife, Victoria Sant, served on the National Gallery of Art board (where Mitchell Rales is president) and the Phillips Collection board (where George Vradenburg served as chair).

**Uncertainty**: No corpus document mentions Roger Sant in any Epstein context. No public record connects him to Epstein. His age (~70 during the journal period) is noted. The identification rests entirely on the surname match and the DC institutional cluster coherence.

**Confidence**: SPECULATIVE. The institutional overlaps with other proposed identifications are notable but circumstantial.

### 6.7 "Ms. Vicki" → Unresolved

**Journal claim** (EFTA02731465, p. 2): "I will never be able to forgive myself for not being able to tell you what Ms. Vicki does and what really happens in FL and CA."

This describes a facilitator or handler with operations in Florida and California. No candidate has been identified with sufficient evidence to propose a public match. The name is listed here for completeness but no identification is offered.

### 6.8 The Cluster as a Whole

Several proposed matches above fit a real early-2000s Washington social and institutional milieu: AOL executives (Case, Kimsey, Leonsis, Vradenburg), DC-area billionaires (Rales), DC investors (Ein), a Virginia congressman (Goodlatte), Washington NFL figures (Snyder, Gibbs), and DC philanthropists (Sant). These individuals are documented in public records as moving in overlapping social, institutional, and philanthropic circles.

That coherence suggests the author may have had knowledge of an authentic network, but it does not independently verify that each proposed match is correct or that each person participated in abuse. The journal's "Joe Gibbs is so nice" demonstrates the author differentiated between people she perceived as benign and people she described as abusers — the names cluster socially, but the allegations do not apply uniformly.

---

## 7. Names Without Independent Corpus Evidence

The following names appear only in the journal. No independent EFTA document confirms their identity or connection to Epstein.

| Name | Journal Context | Corpus Status |
|------|----------------|---------------|
| Mr. Colgan | "Why did Mr. Colgan agree to this!" / "flights of horror" list | 0 relevant independent hits |
| The Gregorys | "flights of horror" list (plural — a couple) | 0 relevant hits |
| Mr. Cecchi | "not who they say" list | 0 hits outside journal |
| Mr. Mora | "not who they say" list | 0 hits outside journal (all OCR noise) |
| Mr. Mody | "not who they say" list | 0 hits outside journal (all Moody's rating agency) |
| Mr. Caruthers | "will hurt you especially if Ghislaine is busy" | 0 relevant hits |
| Mr. Islam | Same passage as Caruthers | Mike Islam (Core Club restaurant manager) appears in Epstein staff emails ([EFTA01746728](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01746728.pdf)); same person unconfirmed |
| Mr. Robert + wife Jill | Recruited victim at a party | 0 relevant hits (no surname given) |
| Mr. Joe + Mrs. Anne | Seen at "Maralago" | 0 relevant hits (no surname given) |
| Mr. M | Took the baby 15 minutes after birth | 0 relevant hits |
| Bill s. | Named with Vradenberg | 0 relevant hits |
| Ms. Vicki | Facilitator in FL and CA | See Section 6.7 |
| Mr. Ludwig | "not who they say" list | Dr. Robert L. Ludwig (Epstein's radiologist, [EFTA01735277](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01735277.pdf)) exists in corpus; same person unconfirmed |
| Joe Gibbs | "so nice" (contrast with Snyder) | Joe Gibbs Racing aircraft waiver in Epstein files ([EFTA00521006](https://www.justice.gov/epstein/files/DataSet%209/EFTA00521006.pdf)); context unclear |
| Tracy | "Hope no relation to Tracy!" (re: Summers) | 0 relevant hits |

---

## 8. What the Journal Does Not Prove

This section exists because responsible analysis requires stating limitations.

1. **The journal is a single victim's personal account.** It was not created under oath or in a law enforcement interview. It is a coded diary written by a teenager during or shortly after the events described. Memory, trauma, and the passage of time may affect accuracy.

2. **Appearing in the journal is not the same as appearing in the corpus.** The journal is one document (in multiple copies). When it is the only source for a name, that name has not been independently corroborated.

3. **A proposed identification is not a confirmed identification.** Where this report proposes that "Mr. Rails" may refer to Mitchell Rales, this is an analytical assessment based on available evidence — not a statement of fact. The journal does not provide first names for most individuals.

4. **Network coherence is suggestive, not conclusive.** Several proposed matches fit a real DC social network, which suggests the author knew real people in that milieu. It does not mean every individual named was involved in trafficking, nor does it verify that every proposed match is correct.

5. **Absence from the corpus is not absence from the record.** The EFTA corpus contains 2.91 million pages, but it does not contain everything. Flight logs from Epstein's aircraft are not in the full-text corpus as searchable documents. Financial records may exist under entity names not searched. Sealed court documents are not included.

6. **The journal describes events from approximately 2001–2004.** Epstein's Gmail correspondence in the corpus begins in May 2009. Many names in the journal predate the email evidence entirely.

---

## 9. Structural Findings

### 9.1 Missing Coded Originals

The typed translations in EFTA02731420 and EFTA02731465 cover journal content — including all named perpetrators — whose coded originals are not present in the EFTA production. The Wigdor correspondence confirms "the entirety of the journal" was provided to SDNY, but only a portion of the coded pages were included in the public dataset. The coded originals for the pages naming Leon Black, George Mitchell, the DC cluster, Minsky, Krauss, Staley, and other perpetrators are not publicly available.

### 9.2 SDNY Declined to Investigate

The documents show that as of June 2023, SDNY had "not opened an investigation" based on the allegations presented through counsel ([EFTA02731478](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731478.pdf)). The victim was never assigned an FBI serial number. The public record released in the EFTA production does not show further investigative steps by that office. The journal — which names dozens of individuals, describes forced pregnancies and an infant removal, and is independently corroborated on its strongest claims — was received by federal prosecutors, and no investigation resulted from it in the public record.

### 9.3 The Journal Predates Most Corpus Evidence

The journal describes events from 2001–2004. Epstein's Gmail corpus begins in 2009. Most financial records in the production cover 2004–2019. The Brockman/Edge Foundation emails are from 2011–2015. This means the journal describes a period for which the corpus has relatively little documentation — and many of the names that appear "only in the journal" may simply predate the available evidence.

---

## 10. Methodology

1. **Page-level visual reading**: All 69 pages across four journal documents were read from 400 DPI renders extracted via PyMuPDF from the original DOJ PDFs
2. **Text extraction**: PyMuPDF text layer extraction from all four documents; typed pages yielded clean text, coded pages yielded noise
3. **Cipher verification**: Rail fence decode confirmed by interleaving rows from EFTA02731362 against typed translation on EFTA02731361 page 1
4. **Corpus search**: FTS5 and LIKE queries across 2,914,901 pages in `full_text_corpus.db` for every name in the inventory
5. **Registry cross-reference**: All names checked against `persons_registry.json` (1,538 persons)
6. **External verification**: Web search for proposed identifications, public records, and prior reporting
7. **Source attribution**: Every factual claim linked to specific EFTA page or external URL

### Tools
- Python 3.x, PyMuPDF, PIL/Pillow
- SQLite3 (full_text_corpus.db, 6.3 GB)
- Tesseract OCR (attempted; results poor on spaced handwritten characters)
- Web search for external verification

### Prior Reporting

This journal has been reported on by multiple outlets including [Scripps News](https://www.scrippsnews.com/), [Hyperallergic](https://hyperallergic.com/), [Narativ](https://narativ.org/), and independent researcher [Ellie Leonard](https://ellieleonard.substack.com/). The present analysis focuses specifically on corpus corroboration — matching journal claims against 2.91 million pages of independently produced documents — which has not been systematically attempted in prior reporting.
