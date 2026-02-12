# Audits

This directory contains systematic factual audits of the investigation reports in this repository.

## FACTUAL_ACCURACY_AUDIT.md

**Scope:** 133 issues identified and corrected across 23+ report files (ongoing)

**Methodology:**
1. Each report file is read in full and every claim, quote, and citation is catalogued
2. Key claims are verified against source EFTA documents using SQL queries against `full_text_corpus.db` (1.38M documents, 2.73M pages extracted from all 12 DOJ datasets)
3. Quotes attributed to specific EFTA documents are checked verbatim against the extracted text
4. Five error patterns are specifically targeted:
   - Interpretive leaps presented as fact
   - Cherry-picking (omitting contrary evidence)
   - Compaction-border misinterpretation (AI summary errors at context boundaries)
   - Overstatement/absolutes ("proves," "the most significant," "only explanation")
   - Conflation (mixing up people, databases, or attributing quotes to wrong sources)
5. Corrections are applied directly to the report files and logged with issue numbers
6. Legal conclusions (e.g., "money laundering") are reframed unless supported by an actual conviction or charge
7. CHS/NTOC tips are always noted as unverified
8. Victim privacy is maintained throughout

**Trigger:** A Reddit r/JeffreyEpstein moderator identified factual errors in the initial release of `FINAL_INVESTIGATION_REPORT.md`. Rather than patch individual errors, a comprehensive audit of all ~100 report files was initiated.

**Priority order:**
- Tier 1: Congressional-facing documents (highest exposure)
- Tier 2: Synthesis/overview reports
- Tier 3: Named individual investigations (defamation risk)
- Tier 4: Financial, evidence, and institutional reports
