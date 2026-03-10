# Writing Guide

Style rules for investigation reports in this repository. These exist because AI-generated text has recognizable patterns that undermine credibility. The goal is writing that reads like it was produced by a careful human researcher.

---

## AI Writing Avoidance

### Hard Rules (never do these)

- **No em-dashes in prose.** This is the single most-flagged AI writing marker. Use commas, periods, parentheses, or restructure the sentence. Em-dashes are acceptable only in quoted source material or citation formatting.
- **No banned words:** "delve," "tapestry," "nuanced," "multifaceted," "pivotal," "underscores," "landscape"
- **No generic transitions:** "Moreover," "Furthermore," "In conclusion," "What this means," "It is worth noting that"
- **No colon-then-explanation patterns** (except in citations and data tables)
- **No symmetric rhetorical templates:** "It's not X. It's Y." Once is fine. Twice in a report is a tell.
- **No repetitive phrasing / low lexical variation.** If you used a word in the last paragraph, find a different one.
- **No hedging in every paragraph.** Hedge only where genuinely uncertain. If the document says it, state it.

### What Works

- **Bold emphasis** on key names, concepts, and findings
- Words like **"notably"** and **"crucially"** are fine and part of the author's voice
- Short, punchy sentences. Vary paragraph length. Three sentences followed by one. Then five. Break the rhythm.
- Concrete evidence over abstractions. Quote the document. Give the number. State the fact.
- One clear claim per paragraph. Don't stack three findings into a single block.

---

## Analytical Neutrality

- **Corpus absence ≠ non-existence.** A missing document may be under seal, in a separate case, or outside the EFTA production scope. State what's absent without assuming why.
- **Minimal production is standard legal practice.** Defense attorneys produce what's specifically demanded and nothing more. This is normal, not evidence of a cover-up.
- **Present data, not conclusions.** "The subpoena demanded X. The return contained Y. Z categories received no responsive documents." Let the reader see the gap.
- **Legal precision on document types and certainty levels.** A grand jury subpoena is not a search warrant. An FD-302 is not a transcript. A draft is not a final filing.

---

## Victim Privacy

**Never include real victim names, pseudonym-to-name mappings, or identifying details in any report.** This is non-negotiable.

- Use pseudonyms: Jane Doe, JD#1, Katlyn Doe
- Use EFTA references: "the victim described in EFTA01245817"
- Describe patterns, not individuals: "multiple victims reported being recruited at age 14-16"
- When discussing victim counts or demographics, aggregate. Never single out an identifiable person.

---

## Citation Standards

Every factual claim requires a citation. No exceptions.

### EFTA Citations

Format: `EFTA00074206` or `EFTA00074206 p.3` for a specific page.

To link to the source PDF:
```
https://www.justice.gov/epstein/files/DataSet%20{N}/EFTA{NUMBER}.pdf
```
Look up the dataset number from `full_text_corpus.db` before constructing URLs. Do not guess from the EFTA number.

### External Citations

Link directly to the source. Prefer primary sources (court filings, SEC records, government databases) over secondary reporting. When citing news articles, include the publication name and date.

### What Requires a Citation

- Biographical facts (birth year, education, career, net worth)
- Dates and timelines
- Entity relationships and corporate structures
- Property values, transaction amounts
- Government positions and titles
- Any claim about what a document says

### What Doesn't

- General background widely available in multiple sources ("Epstein was arrested in July 2019")
- Logical inferences clearly derived from cited evidence in the same section
- Methodological descriptions (how you searched, not what you found)

---

## Report Structure

Reports don't need to follow a rigid template, but they should:

1. **Open with what matters.** Lead with the finding, not the methodology.
2. **Organize by topic, not chronology.** Group related evidence together.
3. **Use headers liberally.** A reader should be able to scan headers and know what the report covers.
4. **End with what's missing.** Unanswered questions, promising leads, documents that should exist but weren't found.

---

## References

- Linguistic patterns in AI text: https://arxiv.org/abs/2510.05136
- Human accuracy at detecting AI writing: https://arxiv.org/abs/2206.07271
- AP standards on generative AI: https://www.ap.org/standards-around-generative-ai
