# Investigation Methodology

How the reports in this repository are researched, written, and fact-checked. If you're using AI to investigate these files, treat this document as your operating manual.

---

## Investigation Pipeline

Every investigation follows five phases. Do not skip phases or reorder them.

### Phase 1a: Cursory Corpus Search

Search `full_text_corpus.db` using FTS5 and LIKE queries. Cast a wide net: name variants, known aliases, associated entities. Create a **scratchpad file** immediately to capture raw findings. The scratchpad is the single source of truth for the investigation.

### Phase 1b: Parallel Deep Reads + External Research

Run up to three parallel workstreams:

1. **Deep-read**: Pull key EFTA documents in full. Read complete pages, not snippets. Scan neighboring EFTA ranges (documents near a hit are often related).
2. **Cross-reference**: Check concordance metadata (email headers, folder paths, custodians) for context. Query the prosecutorial query graph for subpoena and gap connections.
3. **External research**: Search for existing public reporting on the topic. Record URLs. This is **mandatory**, not optional. You must know what's already been reported before claiming anything is new.

Update the scratchpad as each workstream completes. Never re-do work that's already captured.

### Phase 2: Cross-Reference and Pattern Analysis

Connect findings across databases. Check for:
- Co-occurrence (two names in the same document)
- Temporal patterns (clusters of activity around specific dates)
- Financial flows (shell entities, wire transfers, trust drawdowns)
- Production anomalies (redactions, missing serials, altered documents)

### Phase 3: Write with Citations

Write the report. Every factual claim must cite either an EFTA number or an external source URL. No exceptions. One clear claim per paragraph. See [WRITING_GUIDE.md](WRITING_GUIDE.md) for style rules.

### Phase 4: Fact-Check Every Claim

Audit every sentence that contains a factual claim:
- Does it have a citation (EFTA number or external URL)?
- Can a reader follow that citation and confirm the claim?
- Is the claim accurately stated (correct dates, titles, amounts)?
- If biographical, has it been verified against a current external source?

If a claim fails any of these checks, fix or remove it.

### Phase 5: Novelty Verification

Before publishing, web search every major finding to determine whether it has been previously reported. If it has, cite the prior reporting. Do not claim something is "unreported" or "previously unknown" without search evidence backing that claim.

---

## External Article Fact-Check Protocol

When fact-checking an external article (journalist, Substack, researcher), use a five-table reconciliation structure. This catches errors that a claim-by-claim review misses — conflated addresses, reversed transactions, sourcing gaps.

### Step 1: Extract Every Factual Claim

Read the article and extract every assertion of fact: names, dates, amounts, quotes, relationships, events. Use exact wording. Do not summarize.

### Step 2: Corpus Search + External Verification

For each claim, run three checks:

1. **Corpus search**: FTS5 + LIKE queries on `full_text_corpus.db`. Record EFTA numbers and page numbers.
2. **External verification**: Web search for independent reporting, court filings, public records. Record URLs.
3. **Cross-reference**: Check if corpus and external sources agree, and whether the article's characterization matches the underlying evidence.

### Step 3: Build the Five Reconciliation Tables

| Table | Contents | Purpose |
|-------|----------|---------|
| **Table 1: CONFIRMED** | Claims that are correct; our EFTA cite or external source | Shows what's solid ground |
| **Table 2: ERRORS** | Claims that are factually wrong, with the correct facts and source | Identifies what must be fixed |
| **Table 3: UNVERIFIED** | Claims we can't confirm or deny from available evidence | Shows sourcing limits |
| **Table 4: THINGS WE HAVE THAT THE ARTICLE DOESN'T** | Corpus findings the article missed | Identifies what a proper report would add |
| **Table 5: SOURCE DEEP DIVE** | Detailed inventory of source documents, what exists vs. what's missing | Shows methodological completeness |

Each row should include: claim text, verdict, EFTA source (if any), external source (if any), and notes on nuance.

### Step 4: Reconcile Contested Claims

For each UNVERIFIED or INCORRECT claim, write a reconciliation section explaining:

- What the article claims (exact wording)
- What the corpus shows
- What external sources show
- Possible explanations for the discrepancy
- What additional evidence would resolve it

### Step 5: Viability Assessment

Summarize: Could we write a properly-cited version of this article? Break it into:

- **Strong ground**: Claims backed by corpus primary sources (EFTA documents)
- **Solid ground**: Claims backed by external reporting but not in corpus
- **Weak ground**: Claims that would need to be hedged, softened, or dropped
- **New findings**: Evidence we have that the original article missed

This structure makes it clear whether a topic merits a full investigation report, and exactly where the sourcing work is already done vs. still needed.

---

## Witness/Person Briefing Algorithm

For deep-dive reports on specific individuals:

1. **Search all existing reports** for every mention of the person's name
2. **Read full context** around each mention. Pull all EFTA citations, findings, cross-references
3. **Run corpus database searches**: FTS5 + LIKE queries on name, known aliases, associated entities
4. **Cross-link everything**: each finding links to (a) the source report and (b) the source EFTA document on justice.gov
5. **Verify with external reporting**: web search for news coverage, court filings, current status. Include URLs
6. **Write the report** in standard format: Who They Are, Evidence Inventory (organized by topic), key questions, counter-strategies
7. **Fact-check within the same working session as the write.** If the investigation is too large to hold in context at once, work incrementally: read a batch of sources, write that section, read more, write more. Never write an entire report from summarized memory alone
8. **Update the master index**: after fact-checking each brief, go back to the relevant index document and enrich that person's section with highlights from the deep dive

---

## Compaction Safety

AI context windows compact older messages into summaries. These summaries can contain errors, conflations, and fabrications that look plausible but are wrong.

**Core rule: Never write factual claims from compacted memory.** If you cannot see the source document in your current context, re-read it before writing.

### Error Types Caught in Audit

These are real errors that originated from trusting compacted context:

| Error Type | Example |
|-----------|---------|
| **Wrong nationality/origin** | "British-Iraqi" for subjects who were actually Mumbai-born, Baghdadi Jewish heritage |
| **Wrong identification** | A helicopter pilot misidentified as a named attorney |
| **Wrong legal citation** | A BVI architectural contract case cited as an unrelated high-profile lawsuit |
| **Duplicate sources presented as independent** | The same letter sent to four recipients counted as four separate pieces of evidence |
| **Wrong professional title** | "Vice Chairman" used for a date when the person actually held "President/COO" (promoted three years later) |
| **Wrong duration** | "Two weeks" instead of ten days |
| **Wrong measurement** | 242ft instead of 243ft |

### Prevention Rules

1. After compaction, re-verify everything: every quote, EFTA number, biographical claim, date, title, and measurement
2. Biographical facts about real people must be verified against web search or the corpus. Never trust your own memory for nationality, birth city, professional title at a specific date, family relationships, company roles, ages, or dates
3. Cross-check internal consistency. If two sections give different numbers for the same fact, one is wrong. The corpus is the authority
4. When multiple documents say the same thing, check if they're copies. The same complaint sent four times is one source, not four
5. Legal citations require reading the actual document. A 27-page filing may mention a case in one paragraph on page 17
6. Professional titles change over time. Always check the title as of the date being discussed

---

## Reader-Verifiability

**All claims must tie back to source material that a reader can independently check.**

Sources that count:
- **EFTA number**: links to a PDF on justice.gov (or OCR on epstein-data.com if the DOJ has removed it)
- **External articles**: newspaper URLs, court records, SEC filings, public databases
- **Public records**: FAA registrations, property records, corporate filings

If a claim cannot be verified by a reader following the citation, it must be removed or rewritten with a proper citation.

---

## Scratchpad Discipline

Create a scratchpad file at the start of every investigation. Write findings to it immediately, before they can be lost to context compaction. The scratchpad is the single source of truth. Never re-launch searches for information already captured in the scratchpad.

Delete scratchpads only after the final report is published and fact-checked.

---

## Analytical Neutrality

- **Corpus absence ≠ non-existence.** A document not appearing in the EFTA production may be under seal, filed in a different case, or outside the scope of the DOJ release. Do not assume non-compliance from a gap.
- **Minimal production is standard legal practice.** Defense attorneys routinely produce only what is specifically demanded. Don't treat normal defense behavior as suspicious.
- **Present data, not conclusions.** Show what the documents contain. Let readers draw their own inferences.
- **Hedge only where genuinely uncertain.** Don't hedge in every paragraph as a defensive reflex.

---

## Victim Privacy

**Never include real victim names, pseudonym-to-name mappings, or identifying details in any output.** Use pseudonyms (Jane Doe, JD#1) or EFTA references only. The goal is exposing the system and the perpetrators, never retraumatizing or identifying victims.
