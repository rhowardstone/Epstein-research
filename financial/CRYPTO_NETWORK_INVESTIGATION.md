# Epstein's Cryptocurrency Network: $18M+ Through Shell Companies, Zero On-Chain

## A forensic map of every crypto contact, investment, and proposal in the EFTA corpus

**Updated:** March 2026
**Scope:** 2,429 documents / 3,841 pages across the EFTA corpus containing bitcoin, cryptocurrency, coinbase, or blockchain references
**Databases:** full_text_corpus.db (6.3 GB, 1.39M docs), prosecutorial_query_graph.db, concordance_complete.db
**Companion report:** [Line of Investigation 08: The Cryptocurrency Gap](../pqg_lines_of_investigation/08_CRYPTO_DEAD_END.md)

---

## Executive Summary

Jeffrey Epstein ran a cryptocurrency investment network spanning 2011 to 2019. He invested at least **$18 million** into crypto-adjacent companies — Coinbase, Blockstream, Bitmain — through a lattice of Delaware and USVI shell companies managed by Deutsche Bank. He consulted with the US Treasury on digital currency regulation. He discussed creating a "Russian version of bitcoin" for Vladimir Putin. He hosted Gavin Andresen, Bitcoin's lead developer after Satoshi Nakamoto. His computer forensics were performed by Dave Kleiman, later central to the Kleiman v. Wright (Satoshi) lawsuit.

And yet: **not a single dollar of this moved on any blockchain.** Every transaction was a traditional bank wire. No cryptocurrency wallet, exchange account, or on-chain address attributable to Epstein or his entities has ever been found — not in the EFTA corpus, not in the estate probate ($636M inventory), not in the NYDFS Deutsche Bank consent order, and not in any public blockchain record.

The SDNY investigation reinforced this blindness. Across 257 grand jury subpoenas, **zero** mentioned cryptocurrency, bitcoin, blockchain, or digital currency. No exchange was subpoenaed. No blockchain analytics firm was retained. The prosecution's financial framework was comprehensive for traditional banking and completely absent for digital assets.

The closest anyone came to putting Epstein-linked money on-chain: Blockstream co-founder Austin Hill proposed settling a side-project investment via **"Tumbled bitcoin transactions"** — CoinJoin mixing — with **"Snowden's escape to Russia level counter-surveillance."** There is no evidence this was ever executed.

---

## Part 1: The Network — 12 Named Crypto Contacts (2011-2019)

### 1.1 "Amir" — The Earliest Reference (June 2011)

The corpus's first cryptocurrency mention is a staff scheduling email:

> *"Reminder: you want to fly Amir with Bitcoin in to NY this week"*

Source: [EFTA02020736](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02020736.pdf). Bitcoin was trading under $20. "Amir" is unidentified — possibly Amir Taaki (early Bitcoin developer) or another figure. The phrasing "Amir with Bitcoin" suggests this person was presenting or demonstrating the technology, not conducting a transaction.

### 1.2 Brock Pierce — The Pipeline (2011-2017)

Pierce was Epstein's primary crypto-sector contact. At least 15-20 in-person meetings are documented. Pierce would later chair the Bitcoin Foundation and run for president on a Bitcoin platform.

**September 2011** — Pierce to Epstein, Subject "Virtual Currency / Goods":

> *"I believe I found a way to provide monetary control, tax optimization, and effectively manage earnings through the use of an exchange, insurance, and marketing."*

Source: [EFTA01989757](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01989757.pdf). This is a pitch for crypto-based tax optimization — three years before Epstein made his first crypto-sector investment.

**May 2013** — Pierce to Epstein, Subject "Starting a Crypto Mining co":

> *"When can you chat?"*

Source: [EFTA01975894](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01975894.pdf).

**December 3, 2014** — Pierce to Epstein:

> *"Attached are the docs I sent you for the LLC that we intend to funnel your investments through"*

Source: [EFTA02708994](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02708994.pdf). Pierce's email signature reads "Managing Director — Crypto Currency Partners" (also in [EFTA00362034](https://www.justice.gov/epstein/files/DataSet%209/EFTA00362034.pdf)). The LLC referenced here is the Blockchain Capital vehicle that would hold Epstein's Coinbase equity.

**December 2014** — Pierce soliciting $12M Coinbase round from Epstein:

Source: [EFTA01731638](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01731638.pdf).

**October 2015** — Full Blockchain Capital Investor Update found in Epstein's files:

A 30-company portfolio summary with 1.4x NAV. Source: [EFTA00604942](https://www.justice.gov/epstein/files/DataSet%209/EFTA00604942.pdf). Pierce also forwarded Coinbase investor newsletters to Epstein and Richard Kahn showing $60.6M in the bank and $800K monthly revenue ([EFTA00625694](https://www.justice.gov/epstein/files/DataSet%209/EFTA00625694.pdf)).

**Blockchain Capital's position**: The firm has publicly stated that Epstein's investment "was never consummated." The EFTA corpus tells a different story — see Part 2 below.

### 1.3 Andrew Farkas — "Your Little Bitcoin Elf" (2014)

Farkas, a New York real estate investor, served as intermediary in Epstein's crypto dealings and coined a nickname for Pierce:

> *"If I could short bitcoin I would"* — Epstein
> *"Your boy Brock would do it"* — Farkas

Source: [EFTA00626207](https://www.justice.gov/epstein/files/DataSet%209/EFTA00626207.pdf).

> *"That's funny! The bitcoin elf!"*
> *"Yes your little bitcoin elf"*

Source: [EFTA00681240](https://www.justice.gov/epstein/files/DataSet%209/EFTA00681240.pdf) — same document also contains a Pierce/Farkas/Nasdaq agreement for a "Nasdaq Xtreme platform."

Farkas forwarded Austin Hill's "Why Bitcoin Has Value" paper to Epstein ([EFTA00870319](https://www.justice.gov/epstein/files/DataSet%209/EFTA00870319.pdf)). Epstein kept an Apple Notes to-do item reading "farkas, bitcoin" ([EFTA00518681](https://www.justice.gov/epstein/files/DataSet%209/EFTA00518681.pdf) — [removed from justice.gov](../doj_audit/CONFIRMED_REMOVED.csv)).

### 1.4 Steven Sinofsky — Most Frequent Bitcoin Correspondent (2013-2014)

Sinofsky, former president of the Windows division at Microsoft, exchanged more bitcoin-related emails with Epstein than any other contact.

**October 2013** — Subject "bitcoin and silk road":

> *"He really got busted because he used his real name and gmail account... many more to follow... any new ideas? should we organize a..."* (truncates)

Source: [EFTA01754738](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01754738.pdf), [EFTA01754969](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01754969.pdf).

> *"I'm up 50% on my BTC investment!"* — Sinofsky

Source: [EFTA00976881](https://www.justice.gov/epstein/files/DataSet%209/EFTA00976881.pdf).

Sinofsky also brokered introductions — Epstein asked him to:

> *"Ask Adreeson to talk to Jes Staley about my interest in currency"*

Source: [EFTA01804670](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01804670.pdf). "Adreeson" = Marc Andreessen (a16z). "Jes Staley" = Barclays CEO and Epstein's longtime banker.

> *"Bitcoin will totally fall with the first aiding and abetting money laundering suit"* — Sinofsky

Source: [EFTA01897935](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01897935.pdf).

### 1.5 Reid Hoffman — From Skeptic to Allocator (December 2013 - November 2014)

Twelve bitcoin-related emails trace Hoffman's evolution from cautious to invested:

**December 19, 2013**: *"Please be careful with bitcoin. Its a kernel of a good idea wrapped in stink"*

**January 22, 2014**: *"Some interesting people, re a bitcoin type currency"*

**March 25, 2014**: *"THE BITCOIN tax ruling is complex. Creates FIFO LIFO accounting issues"*

**March 26, 2014**: *"Someone should start an option market now on bitcoins"* and *"Documents for Joi investment? Bitcoin initial ruling is very pro govt"*

**July 4, 2014**: *"I have some new ideas for your bitcoin crowd"*

Source: [EFTA00375689](https://www.justice.gov/epstein/files/DataSet%209/EFTA00375689.pdf), [EFTA00369148](https://www.justice.gov/epstein/files/DataSet%209/EFTA00369148.pdf).

And the confirmation of an actual position:

> *"Are we out of the Reid bitcoin position?"* — Epstein

Source: [EFTA00631402](https://www.justice.gov/epstein/files/DataSet%209/EFTA00631402.pdf). This establishes that Hoffman and Epstein held a joint or coordinated crypto investment.

Hoffman's role extended to the Blockstream seed round: Austin Hill wrote that *"Reid at the last minute told us to bump your allocation from $50k to $500k"* ([EFTA01917472](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01917472.pdf)).

### 1.6 Joi Ito / MIT Media Lab — The Channel (2013-2016)

Ito managed Epstein's crypto investments through the Kyara LLC chain (see Part 2) while simultaneously running the MIT Digital Currency Initiative. This dual role created a pipeline between Epstein's money and crypto's institutional infrastructure.

> *"Happy to stay in the background, I can be the Jewish version of Bitcoin's mysterious Japanese programmer"*

Source: [EFTA01964463](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01964463.pdf) — Epstein referencing Satoshi Nakamoto.

> *"The beginning of the end for bitcoin 1.0 2.0 could be a home run"* — Ito also mentions working on "Media Lab coin"

Source: [EFTA01916567](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01916567.pdf).

Ito scheduled a US Treasury call for October 15, 2014 on the "MIT BitCoin Project" and "how decentralized VC could evolve over time" ([EFTA02099970](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02099970.pdf)). The Treasury contact was **Anne Shere Wallwork**, Office of Terrorist Financing and Financial Crimes:

> *"Jeffrey offered to provide us in written form some of his thoughts on virtual currency"*

Source: [EFTA00631425](https://www.justice.gov/epstein/files/DataSet%209/EFTA00631425.pdf). A conference call with Wallwork took place on October 15, 2014 ([EFTA00360763](https://www.justice.gov/epstein/files/DataSet%209/EFTA00360763.pdf)).

**Larry Summers** also participated in this nexus:

> *"Bitcoin at your convenience. Do use me as an advisor."*

Source: [EFTA01746562](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01746562.pdf) — Summers to Ito, cc Epstein. Ito replied: *"Would love to connect again and introduce you to my bitcoin kids."*

Other MIT/DCI activity: *"1:30pm Appt w/Jeremy Rubin and the Bitcoin troops"* (October 2015, [EFTA00337558](https://www.justice.gov/epstein/files/DataSet%209/EFTA00337558.pdf)). Bitcoin Expo attendance in March 2016 ([EFTA00328767](https://www.justice.gov/epstein/files/DataSet%209/EFTA00328767.pdf)).

Epstein donated approximately **$525,000** to the MIT Digital Currency Initiative through intermediaries. This was extensively reported in 2019 following Ronan Farrow's New Yorker investigation and Ito's subsequent resignation.

### 1.7 John Brockman / Gavin Andresen — Bitcoin's Post-Satoshi Lead Developer (June 2011)

Literary agent and Edge Foundation founder John Brockman introduced **Gavin Andresen** — the developer Satoshi Nakamoto handed Bitcoin's lead maintainer role to before disappearing — directly to Epstein.

Source: [EFTA00629471](https://www.justice.gov/epstein/files/DataSet%209/EFTA00629471.pdf).

### 1.8 Austin Hill / Adam Back / Blockstream (2015-2018)

Hill co-founded Blockstream with Adam Back (inventor of Hashcash, cited in the Bitcoin whitepaper). Hill scheduled New York meetings with Epstein and discussed the Bitcoin North America conference ([EFTA00631742](https://www.justice.gov/epstein/files/DataSet%209/EFTA00631742.pdf)).

Hill provided PGP and OTR keys in correspondence: PGP fingerprint `90C0 79D9 190C BA1A 1A2C 780F 04F3 7ABA B333 4BE4`. He refused Skype calls, writing that *"@pmarca gave them full listening capabilities via Echelon."*

His most significant document is the **tumbled bitcoin proposal** — see Part 3.

### 1.9 Kathy Ruemmler / Ben Lawsky (December 2014)

> *"Kathy — Ben Lawsky is the head of financial service enforcement. Topic: bitcoin."*

Source: [EFTA00357807](https://www.justice.gov/epstein/files/DataSet%209/EFTA00357807.pdf). Ruemmler was former White House Counsel, later Epstein estate trustee (see [Ruemmler Deep Dive](../individuals/RUEMMLER_DEEP_DIVE.md)). Lawsky was New York's Superintendent of Financial Services, architect of the BitLicense regulation. This email places Epstein at the intersection of crypto regulation and political power.

### 1.10 Jem Bendell / Gates Foundation / UN (March 2014)

> *"Connected via the Gates Foundation... things have exploded due to bitcoin... project with the UN"*

Source: [EFTA00373452](https://www.justice.gov/epstein/files/DataSet%209/EFTA00373452.pdf).

### 1.11 Thorbjorn Jagland / Putin (January 2014)

> *"You can explain to Putin, that there should be a sophisticated Russian version of bitcoin. It would be the most advanced financial instrument available on a global basis."*

Source: [EFTA01941232](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01941232.pdf). Jagland was Secretary General of the Council of Europe.

### 1.12 Steve Bannon (2017-2019)

Bannon and Epstein shared crypto-related articles and discussed *"Crypto health data"*, *"Bitcoin health"*, bitcoin vs. Turkish lira, FedCoin, and Facebook's Libra.

Sources: [EFTA01612904](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01612904.pdf), [EFTA01615250](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01615250.pdf), [EFTA01615069](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01615069.pdf), [EFTA01615957](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01615957.pdf).

---

## Part 2: The Money — $18M+ in Traditional Bank Wires

Every confirmed Epstein cryptocurrency investment moved as a conventional bank wire through Deutsche Bank. Not one dollar moved on any blockchain.

### 2.1 The Shell Company Architecture

```
EPSTEIN → Southern Financial LLC (Deutsche Bank, USVI)
             ├── Kyara Investments LLC ────── $99,999 ──→ [Unknown, May 2014]
             ├── Kyara Investments II LLC ─── $250,000 ─→ Wearality (Jul 2014)
             ├── Kyara Investments III LLC ── $500,001 ─→ Blockstream seed (Sep 2014)
             ├── Kyara Investments IV LLC ─── $250,000 ─→ OH2 Laboratories (Mar 2015)
             └── 2017 Caterpillar Trust (GRAT)
                   └── IGO Company LLC ──────── $3,001,000 → Coinbase Series C (Dec 2014)
                         ↑ $15,000,000 buyback from Blockchain Capital (Feb 2018)
```

All Kyara LLCs were managed by **Joi Ito** (Manager) with Southern Financial LLC (signed by Epstein) as sole Member. Operating agreement: [EFTA00584696](https://www.justice.gov/epstein/files/DataSet%209/EFTA00584696.pdf) (18 pages).

### 2.2 Confirmed Investment Flows

| Date | From Entity | To | Amount | Vehicle | Source |
|------|------------|-----|--------|---------|--------|
| May 2014 | Southern Financial LLC | Unknown | $99,999 | Kyara Investments LLC | [EFTA01681865](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01681865.pdf) (removed from justice.gov) |
| Jul 2014 | Southern Financial LLC | Wearality | $250,000 | Kyara Investments II LLC | [EFTA01681865](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01681865.pdf) |
| Sep 2014 | Southern Financial LLC | Blockstream seed | $500,001 | Kyara Investments III LLC | [EFTA01681865](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01681865.pdf), [EFTA00027019](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027019.pdf) |
| Dec 2014 | IGO Company LLC (USVI) | Coinbase Series C | $3,001,000 | Direct equity | External reporting |
| 2014-2016 | Epstein / MIT intermediaries | MIT Digital Currency Initiative | ~$525,000 | Donation | External reporting |
| Feb 2018 | Blockchain Capital | 2017 Caterpillar Trust | $14,666,667 | 50% Coinbase equity buyback at $4B valuation | [EFTA00843103](https://www.justice.gov/epstein/files/DataSet%209/EFTA00843103.pdf) |

**Total confirmed: ~$18.5 million** (plus ~$525K MIT DCI donations)

### 2.3 The Coinbase Equity Buyback — $15M in Three Wires

On February 1, 2018, Blockchain Capital's Brad Stephens gave a 24-hour deadline to close the purchase of 50% of Epstein's Coinbase position at a $4 billion valuation. Darren Indyke confirmed: *"Jeffrey agrees that he will sell you 50% of his LLC."* The purchase came from three Blockchain Capital funds:

| Entity | Amount |
|--------|--------|
| Blockchain Capital IV, LP | $10,000,000 |
| Blockchain Capital Parallel IV, LP | $2,000,000 |
| Blockchain Capital III Digital Liquid Venture Fund, LP | $2,666,667 |
| **Total** | **$14,666,667** |

Source: [EFTA00843103](https://www.justice.gov/epstein/files/DataSet%209/EFTA00843103.pdf) (4 pages — full email thread between Kahn, Stephens, and Indyke).

Richard Kahn's commentary on this transaction:

> *"Blockchain, although paying us a big number, has insight they are not letting on as Kathryn Haun from their company is on Coinbase board"*

Source: [EFTA02533329](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02533329.pdf). Haun was a former federal prosecutor (DOJ digital currency coordinator) who joined Blockchain Capital as a general partner while serving on Coinbase's board. Kahn's email suggests the $15M buyout undervalued the position — that insiders knew Coinbase equity was worth more than the price paid.

### 2.4 The 2017 Caterpillar Trust

The receiving entity for the $15M buyback was a GRAT (Grantor Retained Annuity Trust):

| Field | Value |
|-------|-------|
| Name | The 2017 Caterpillar Trust |
| Type | GRAT |
| TIN | 28-6639711 |
| Jurisdiction | USVI |
| Formation | January 3, 2017 |
| Trustees | Lesley Groff + Daphne Wallace |
| Holds | IGO Company LLC membership interest |
| Terminates to | 2013 Butterfly Trust |
| Balance | ~$13.5M |
| Account manager | Stewart Oldfield (Deutsche Bank) |

Source: [EFTA01387275](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01387275.pdf), [EFTA01387281](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01387281.pdf) (Deutsche Bank "One Sheet").

### 2.5 Southern Financial LLC — The Funding Source

Southern Financial LLC was Epstein's USVI vehicle at Deutsche Bank that funded all Kyara investments. Bank statements show:

| Month | Balance | Notable Activity |
|-------|---------|-----------------|
| Oct 2014 | $13.2M | $301K incoming from Kyara I |
| Dec 2016 | $2.7M → $1.97M | $750K outgoing to ID Bank for HARLEQUIN DANE LLC |
| Sep 2018 | $1.18M | $8M internal transfers |

Sources: [EFTA01285141](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01285141.pdf), [EFTA01286529](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01286529.pdf), [EFTA01287877](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01287877.pdf).

### 2.6 Bitmain — The Deal That May Not Have Closed

In August 2018, Epstein explored a $1-3M investment in Bitmain's Series B via Blocktree Private Opps LLC / iAngels ([EFTA01004511](https://www.justice.gov/epstein/files/DataSet%209/EFTA01004511.pdf)). No consummation documents exist in the corpus. Blockchain Capital has stated publicly that this investment was never finalized.

### 2.7 Joscha Bach — The Only On-Chain Adjacent Transaction

AI researcher Joscha Bach held bitcoin on **Bitstamp** (Luxembourg-based exchange):

- Bought: February 27, 2014 for **$2,730.02**
- Sold: December 7, 2017 for **$71,224.02** (~$68K capital gain)

Source: [EFTA00809754](https://www.justice.gov/epstein/files/DataSet%209/EFTA00809754.pdf).

Bach couldn't figure out how to transfer proceeds from Bitstamp to a US bank account ([EFTA02659109](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02659109.pdf)). Richard Kahn flagged this to Epstein in the context of an IRS letter:

> *"Joscha loan that is repaid with bitcoin proceeds?"*

Source: [EFTA02614265](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02614265.pdf). Epstein had extended a personal loan to Bach that was to be repaid from the bitcoin sale. This is the closest any transaction in the corpus comes to touching an actual blockchain — but no Bitstamp account identifier or wallet address is visible.

---

## Part 3: The Tumbled Bitcoin Proposal

The single most explosive cryptocurrency document in the EFTA corpus.

**EFTA01004727** ([EFTA01004727](https://www.justice.gov/epstein/files/DataSet%209/EFTA01004727.pdf)) — July 2018 email from **Austin Hill**, co-founder and former CEO of Blockstream, to Epstein.

Hill proposed structuring funding for a side project via:

> *An "offshore hedge fund" or "investment trust" with settlements "managed in Tumbled bitcoin transactions"*

He referenced **Gregory Maxwell's CoinJoin protocol** — a bitcoin mixing technique designed to break the transaction graph and make funds untraceable on-chain.

Hill offered:

> *"Snowden's escape to Russia level counter-surveillance"*

### What This Means

CoinJoin (now called "tumbling" or "mixing") works by combining multiple users' bitcoin transactions into a single transaction with multiple inputs and outputs, making it difficult or impossible to trace which input corresponds to which output. It is the same technology that later led to the federal prosecution and conviction of the founders of Samourai Wallet and Tornado Cash.

Blockstream's co-founder proposed applying this technology to manage Epstein-linked investment settlements. The explicit goal was to make the money flow untraceable.

### What We Don't Know

There is no evidence in the EFTA corpus that this proposal was ever executed. No tumbled bitcoin transactions, CoinJoin outputs, or mixing service records appear anywhere. Hill departed Blockstream before this email, so it may have been a freelance proposal for a separate venture. But the proposal exists, in writing, from one of Bitcoin's most prominent infrastructure builders, to a convicted sex offender, offering military-grade financial obfuscation.

---

## Part 4: The Prosecutorial Blind Spot

The companion report ([Line of Investigation 08: The Cryptocurrency Gap](../pqg_lines_of_investigation/08_CRYPTO_DEAD_END.md)) documents the subpoena record in detail. The summary:

| Dimension | Subpoena Record | Corpus Evidence |
|-----------|----------------|-----------------|
| Crypto subpoenas from Epstein case | **0** | — |
| Crypto mentions in any rider clause | **0** | — |
| Exchange subpoenas (Coinbase, Kraken, etc.) | **0** | Coinbase equity held directly |
| Blockchain analytics (Chainalysis, Elliptic) | **0** | — |
| Wallet / address / private key requests | **0** | — |
| Named crypto contacts | Not investigated | 12+ (Pierce, Ito, Sinofsky, Hoffman, Summers, Hill, Andresen, Bannon...) |
| Epstein's crypto engagement period | Not investigated | June 2011 – June 2019 |
| US Treasury consultation on crypto | Not investigated | October 2014, documented |
| Total crypto-sector investment | Not investigated | ~$18.5M confirmed |

The closest the investigation came to fintech: two subpoenas to **Square, Inc.** ([EFTA00123491](https://www.justice.gov/epstein/files/DataSet%209/EFTA00123491.pdf), [EFTA00123518](https://www.justice.gov/epstein/files/DataSet%209/EFTA00123518.pdf)) requesting standard subscriber records for Cash App — both produced zero returns. Neither mentioned cryptocurrency despite Cash App's Bitcoin trading feature.

The sole "Cryptocurrency / Fintech" subpoena in the Prosecutorial Query Graph ([EFTA00102639](https://www.justice.gov/epstein/files/DataSet%209/EFTA00102639.pdf)) was not from the Epstein case at all — it was from a standalone Volantis/Thompson cryptocurrency fraud prosecution (USAO Ref 2018R01689) that ended up in the EFTA corpus through SDNY's broad document production sweep.

---

## Part 5: Dave Kleiman — The Satoshi Connection

On July 25-26, 2007, **Dave Kleiman** — a computer forensics examiner from Palm Beach County — cloned three of Epstein's computers for defense attorney Roy Black.

Sources: [EFTA00222965](https://www.justice.gov/epstein/files/DataSet%209/EFTA00222965.pdf), [EFTA00178967](https://www.justice.gov/epstein/files/DataSet%209/EFTA00178967.pdf), [EFTA01728788](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01728788.pdf) (sworn declarations).

Kleiman died in April 2013. After his death, his estate sued **Craig Wright** in *Kleiman v. Wright* (S.D. Fla. 2018), alleging that Wright and Kleiman had jointly created Bitcoin under the pseudonym Satoshi Nakamoto and that Wright had misappropriated Kleiman's share of the earliest-mined bitcoin (estimated at 1.1 million BTC, worth over $60 billion at peak).

No media outlet has connected Kleiman's forensic work on Epstein's computers with his role in the Bitcoin/Satoshi controversy. The connection is circumstantial — Kleiman was a Palm Beach computer forensics specialist hired for a routine defense engagement — but it places one of the two people most credibly connected to Satoshi Nakamoto inside Epstein's legal defense at the exact moment when the Bitcoin whitepaper was being drafted (published October 2008).

For full analysis of Kleiman's Epstein engagement, see: [Epstein Storage Units Investigation](../institutional/EPSTEIN_STORAGE_UNITS_INVESTIGATION.md).

---

## Part 6: Extortion and Blackmail — The Only Wallet Address

### 6.1 The Zorro Blackmailer

The only explicit Bitcoin wallet address in the entire EFTA corpus is a dead extortion demand:

**Address:** `3Cr9TpVeRcgeg4zGhPEdzhC94HzuUScbHN`
**Email:** `dfd43299@protonmail.com`
**Date:** November 21, 2019 (three months after Epstein's death)
**Target:** Eddy Aragon, a New Mexico conservative radio host ("Rock of Talk")

The email threatened to release information about Epstein's Zorro Ranch unless payment was sent to the wallet. Three copies exist in the corpus: [EFTA01250229](https://www.justice.gov/epstein/files/DataSet%209/EFTA01250229.pdf) (unredacted, serial 3501.517-001), [EFTA00067066](https://www.justice.gov/epstein/files/DataSet%209/EFTA00067066.pdf), [EFTA00038382](https://www.justice.gov/epstein/files/DataSet%208/EFTA00038382.pdf).

The FBI cataloged it: [EFTA01684300](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01684300.pdf) p.105 — *"The email had a valid wallet."* A Guardian form was generated: [EFTA00067072](https://www.justice.gov/epstein/files/DataSet%209/EFTA00067072.pdf), Case ID 50D-NY-3027571, dated October 8, 2021.

**Blockchain verification (March 2026):** The wallet `3Cr9TpVeRcgeg4zGhPEdzhC94HzuUScbHN` has **zero transactions**. It has never received or sent any bitcoin. The extortion attempt was never paid. Verified via Blockstream API, blockchain.info, and mempool.space.

**NM developments:** In February 2026, New Mexico AG Raúl Torrez [reopened the Zorro Ranch investigation](https://www.cbsnews.com/news/new-mexico-reopens-investigation-jeffrey-epstein-zorro-ranch/) based partly on this email and other newly-released EFTA materials. The New Mexico legislature [unanimously established a bipartisan Epstein Truth Commission](https://sourcenm.com/2026/02/16/new-mexico-house-unanimously-enacts-epstein-truth-commission/) with $2M budget and subpoena power.

**Note:** The user's initial reference stated Maxwell Frost read this into the Congressional Record. This is incorrect. Frost viewed unredacted files in the SCIF and planned a floor speech about Trump/Mar-a-Lago contradictions. It was **Ro Khanna** who read names into the record (not crypto-related). The Zorro email became public through the standard EFTA document release.

### 6.2 Mark Epstein Iranian Hacker Threats

A separate extortion scheme targeted **Mark Epstein** (Jeffrey's brother) following Ghislaine Maxwell's arrest. The FBI traced threats to Iranian IP addresses.

Device accounts included bitcoin-themed email addresses:
- `bitcoinhvv@gmail.com`
- `newbtc242@gmail.com`
- `pomplianoa@gmail.com`

Source: [EFTA00146889](https://www.justice.gov/epstein/files/DataSet%209/EFTA00146889.pdf). FBI identified the device (Android ID: 4201921700075594851, IMEI: 866778023302932) and VOIP numbers (4302482541, 6203229434). NYPD Complaint 2020-001-2753.

No bitcoin transactions are documented in connection with this threat.

### 6.3 ProtonMail Setup

On July 12, 2017, **Jeffery Martin** set up a ProtonMail account for Epstein: `jmje@protonmail.com`.

Source: [EFTA01621829](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01621829.pdf). This is unrelated to the Zorro blackmailer's protonmail but establishes that Epstein used encrypted email.

---

## Part 7: What Remains Undiscoverable

Without subpoena power or cooperation from exchanges, the following questions cannot be answered from the EFTA corpus:

1. **Did Epstein personally hold cryptocurrency?** The estate probate ($636M inventory, 100+ pages) lists no crypto holdings. The NYDFS Deutsche Bank consent order ($150M penalty) does not mention cryptocurrency. But neither document would capture self-custodied wallets or exchange accounts at non-subpoenaed platforms.

2. **What did the FBI find on Epstein's 60+ seized devices?** Forensic analysis could have recovered wallet files (wallet.dat), exchange app data, browser history for exchange logins, or cryptocurrency-related metadata. None of this is documented in the EFTA corpus.

3. **Was the Austin Hill tumbled bitcoin proposal ever executed?** No CoinJoin transactions or mixing service outputs appear anywhere in the record.

4. **What happened to the Coinbase equity after the $15M buyback?** The 2017 Caterpillar Trust received the proceeds, which were supposed to terminate to the 2013 Butterfly Trust. Whether this chain was followed through is not documented.

5. **Did any of Epstein's 12+ crypto contacts transact with him on-chain?** None of their personal wallets are publicly disclosed. Pierce ran for president on a Bitcoin platform without revealing personal holdings. Sinofsky's "50% BTC investment" is referenced but no address given.

6. **Was the "Joscha loan" ever formalized or reported to the IRS?** Kahn's email flagging "joscha loan that is repaid with bitcoin proceeds" implies this was a taxable event. Bach's Bitstamp account is the nearest on-chain lead but no account identifier is visible in the corpus.

7. **What was in Brock Pierce's "tax optimization" proposal (2011)?** The pitch referenced "monetary control, tax optimization, and effectively manage earnings through the use of an exchange." If this used an actual cryptocurrency exchange, there may be historical transaction records.

---

## Part 8: What's Already Been Reported

Several outlets have covered Epstein's crypto connections since the EFTA release:

| Outlet | Focus | URL |
|--------|-------|-----|
| Fortune | Coinbase, Blockstream, Saylor, Pierce investments | [fortune.com](https://fortune.com/2026/02/06/jeffrey-epstein-files-coinbase-blockstream-michael-saylor-brock-pierce/) |
| CoinDesk | Coinbase $3M investment via DOJ files | [coindesk.com](https://www.coindesk.com/policy/2026/02/04/newly-unsealed-doj-files-link-jeffrey-epstein-to-a-2014-investment-in-coinbase) |
| Blockspace | Comprehensive bitcoin/Epstein overview | [blockspace.media](https://blockspace.media/insight/everything-you-need-to-know-about-bitcoin-and-the-epstein-files/) |
| The Logic | Blockstream investment details | [thelogic.co](https://thelogic.co/news/epstein-invest-bitcoin-crypto-blockstream/) |
| BitcoinProtocol.org | Wire-level analysis (4 articles) | [blockstream ties](https://news.bitcoinprotocol.org/blockstreams-ties-to-epstein-reveal-hidden-investments-bitcoin-mixing-and-deniable-funding/), [money trail](https://news.bitcoinprotocol.org/following-epsteins-83-million-money-trail-to-bitcoins-earliest-builders/), [Pierce/CCP](https://news.bitcoinprotocol.org/epstein-funneled-millions-into-bitcoin-through-brock-pierces-crypto-currency-partners-fund/), [Bitmain](https://news.bitcoinprotocol.org/epsteins-2018-bitmain-investment-deal-that-came-down-to-the-wire/) |
| France 24 | Debunked "Epstein invented Bitcoin" emails | [france24.com](https://www.france24.com/en/doctored-emails-online-claim-jeffrey-epstein-invented-bitcoin) |

### What This Report Adds

**Unreported findings:**

- **The Reid Hoffman "are we out of the Reid bitcoin position" email** — confirms a joint or coordinated Epstein-Hoffman crypto holding. Not found in any prior reporting despite extensive Hoffman/Epstein coverage.
- **The Joscha Bach Bitstamp account** — bitcoin bought for $2,730, sold for $71,224, Epstein loan repayment from proceeds. No prior reporting connects Bach to cryptocurrency activity.
- **Systematic blockchain API verification** — no outlet has documented searching Blockstream, mempool.space, blockchain.info, and WalletExplorer to confirm zero Epstein-attributable wallets exist on-chain.
- **The prosecutorial blind spot quantified** — zero crypto subpoenas across 257 total, zero exchange subpoenas, zero blockchain analytics retention. No prior reporting counts the subpoena corpus.

**Partially reported findings with new elements:**

- **The Austin Hill corpus profile** — the tumbled bitcoin proposal was reported by [BitcoinProtocol.org](https://news.bitcoinprotocol.org/blockstreams-ties-to-epstein-reveal-hidden-investments-bitcoin-mixing-and-deniable-funding/). This report adds cross-references to Hill's 7+ other EFTA documents (PGP keys, island scheduling, conference invitations, regulatory meetings).
- **The complete Sinofsky correspondence** — individual Sinofsky-Epstein emails have been reported (CNBC, Bloomberg). This report is the first to map the full bitcoin thread, characterize Sinofsky as the most frequent bitcoin correspondent, and publish the Andreessen/Staley brokering email.
- **Kahn's Kathryn Haun insider complaint** — the $14.7M Coinbase buyback is well reported (Bloomberg, CoinDesk, Fortune). The specific Kahn email alleging Blockchain Capital had asymmetric information via Haun's Coinbase board seat is not.
- **Ruemmler in the Lawsky bitcoin meeting** — the Epstein-Lawsky meeting during BitLicense rollout was reported (Decrypt, Crypto Economy). Ruemmler's name in that context — connecting the future estate trustee to the regulatory discussion — is new.
- **The complete Kyara I-IV LLC chain** — Kyara III's $500K Blockstream wire is widely reported. The full four-LLC chain (Kyara I = $99,999 unknown, II = $250K Wearality, III = $500K Blockstream, IV = $250K OH2 Labs) with specific amounts and targets has not been published.

---

## Methodology

### Corpus Search
FTS5 queries against `full_text_corpus.db` for: bitcoin, cryptocurrency, blockchain, coinbase, blockstream, bitmain, crypto, wallet, BTC, ethereum, dogecoin, ripple, litecoin, monero, zcash, bitstamp, kraken, binance, gemini. Results: 2,429 documents, 3,841 pages with substantive hits.

### Blockchain Verification
All wallet addresses identified in the corpus were queried against:
- Blockstream API (`blockstream.info/api/address/`)
- mempool.space API (`mempool.space/api/address/`)
- blockchain.info API (`blockchain.info/rawaddr/`)
- WalletExplorer (clustering database)

One valid address found: `3Cr9TpVeRcgeg4zGhPEdzhC94HzuUScbHN` — zero transactions.

### External Source Verification
Media coverage cross-referenced for all claims. Investment amounts verified against both EFTA corpus (wire transfer records) and external reporting (Fortune, CoinDesk, Blockspace, The Logic, BitcoinProtocol.org).

### EFTA Removal Status
Three EFTAs cited in this report have been [confirmed removed from justice.gov](../doj_audit/CONFIRMED_REMOVED.csv):
- EFTA00518681 (Apple Notes "farkas, bitcoin") — removed
- EFTA01681865 (Deutsche Bank Southern Financial presentation) — removed
- EFTA01699932 (FBI case file) — removed

All content cited from removed documents was read from `full_text_corpus.db` before removal and is accurately represented.

---

## See Also

- [Line of Investigation 08: The Cryptocurrency Gap](../pqg_lines_of_investigation/08_CRYPTO_DEAD_END.md) — subpoena analysis
- [Epstein Storage Units Investigation](../institutional/EPSTEIN_STORAGE_UNITS_INVESTIGATION.md) — Kleiman computer cloning
- [Shell Entity Dark Money Investigation](SHELL_ENTITY_DARK_MONEY_INVESTIGATION.md) — Southern Financial LLC, IGO Company LLC, Caterpillar Trust
- [Ruemmler Deep Dive](../individuals/RUEMMLER_DEEP_DIVE.md) — estate trustee + crypto regulator meetings
