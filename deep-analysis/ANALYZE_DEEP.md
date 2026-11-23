---
name: book-to-skill-deep-analysis
description: "Exhaustive source-faithful analysis profile for Book-to-Skill. Extracts frameworks, atomic decision rules, complete tables and formulas, anti-patterns, terminology, procedures, exceptions, and cross-chapter dependencies without summarization or progressive compression. Use when completeness and source-level traceability are mandatory."
---

# Book-to-Skill — ANALYZE_DEEP Profile

## Purpose and relationship to the converter

This is an opt-in deep-analysis profile. It supplements the general Book-to-Skill converter without changing its default behavior or its existing output contract. Activate it only when the user requests `ANALYZE_DEEP`, exhaustive extraction, research-grade source analysis, or equivalent instructions.

The profile changes the analysis depth and completeness contract. It does not change source access limitations, platform permissions, copyright obligations, or the need to report unverified claims honestly.

## Operating contract

1. Analyze the complete accessible source corpus in its original sequence.
2. Do not produce a chapter summary as a substitute for structured extraction.
3. Do not invent, infer, reconcile, modernize, or supplement source rules. Mark missing information explicitly.
4. Preserve the source's terminology, categories, hierarchy, conditions, exceptions, examples, formulas, notation, and table structure.
5. Keep source-original content distinct from normalized AI-consumable representations.
6. Attach a stable source locator to every extracted item: source ID, chapter/section, printed page if available, PDF/page index if available, and table/figure/equation identifier where applicable.
7. Preserve disagreements and variants. Do not silently resolve contradictions.
8. Do not claim a source, page, chapter, table, or formula was inspected unless it was actually accessed.
9. Respect copyright. Create faithful structured notes and concise paraphrases; do not reproduce substantial copyrighted passages or proprietary tables verbatim. Preserve mathematical structure and factual relationships without copying protected expressive prose.
10. If the user specifies a language, use it consistently for explanations and metadata while preserving original technical terms where needed.

## Required extraction schema

For each chapter or independently numbered source unit, inspect and record all applicable categories below. A category can be marked complete with "NO APPLICABLE CONTENT IDENTIFIED" only after examining the relevant source unit.

### A. Core frameworks

For each framework capture:
- Stable framework ID and exact source name.
- Source definition and source locator.
- Purpose/function when explicitly stated.
- Components, variables, and their relationships.
- Preconditions and required inputs.
- Operational sequence, decision points, intermediate states, outputs, and termination conditions where specified.
- Exceptions, limitations, and boundary conditions.
- Source examples.
- Structured representation (hierarchy, flow, graph, state machine, procedure, etc.) only where supported by the source.
- Formalization status: explicit / faithful normalization / directly derivable / ambiguous / not specified.

Do not complete missing steps with model knowledge. Label them NOT SPECIFIED.

### B. Atomic decision rules

Create one record per independent rule. Never bundle independent rules to reduce count.

Mandatory representation:

`WHEN [Condition] -> DO [Action] -> BECAUSE [Source-stated reason] -> UNLESS [Source-stated exception]`

Fields:
- Rule ID.
- Faithful source statement or concise faithful paraphrase.
- WHEN.
- DO.
- BECAUSE; use NOT EXPLICITLY EXPLAINED when absent.
- UNLESS; use NO EXCEPTION SPECIFIED when absent.
- Preconditions.
- Dependencies.
- Output/consequence.
- Source locator.
- Formalization status.

Do not invent a rationale or exception. Preserve conflicting formulations as distinct rules.

### C. Tables, classifications, and matrices

- Inventory every table, classification, matrix, taxonomy, and decision table.
- Preserve original row/column relationships, hierarchy, order, labels, values, footnotes, qualifications, and merged-cell meaning where identifiable.
- Reconstruct in Markdown when lossless enough; otherwise use structured records plus a note explaining the representational limitation.
- Never replace a detailed table with a prose description.
- Mark illegible or unavailable cells individually where possible.
- Record table ID and source locator.

### D. Formulas and quantitative procedures

For each formula capture:
- Formula ID and original mathematical expression/LaTeX.
- Variable definitions exactly as supplied by the source.
- Units, constants, input requirements, preconditions, order of calculation, rounding and tolerances, if specified.
- Applicability conditions and exceptions.
- Source-provided worked examples and outputs.
- Source locator.
- Any apparent ambiguity or inconsistency, without silently correcting it.

Keep original notation separate from normalized notation. Never invent constants, thresholds, weights, or derived formulas.

### E. Anti-patterns and failure conditions

For each source-supported anti-pattern:
- ID and source name/description.
- Source warning or faithful paraphrase.
- Observable indicators.
- Incorrect operation.
- Cause stated by the source.
- Consequences stated by the source.
- Prevention/corrective method stated by the source.
- Exceptions or qualifications.
- Source locator.

Do not turn general model advice into authorial anti-patterns. Label inferred observations as inference, or omit them if unsupported.

### F. Glossary

For each technical term:
- Term ID.
- Original term and spelling.
- Original/source definition.
- Meaning within the source's system.
- Ordinary meaning only when reliably distinguishable and useful.
- Difference from ordinary usage.
- Related terms and source-defined relationships.
- Context and usage conditions.
- Source locator.

Keep multiple contextual definitions separate. Never assume near-synonyms are interchangeable.

### G. Procedures and workflows

Capture:
- Procedure ID and original name.
- Objective.
- Inputs and preconditions.
- Ordered steps and branches.
- Decision points and dependencies.
- Intermediate results and final output.
- Stop/termination conditions.
- Exceptions and source examples.
- Source locator.

Do not reorder steps or transform descriptive prose into a mandatory procedure unless the source does so.

### H. Cross-chapter dependencies and contradictions

After individual chapter extraction, record:
- Explicit references and dependencies.
- Concepts defined earlier and applied later.
- Repeated terms and contextual variations.
- Framework/rule dependencies.
- Source contradictions and apparent contradictions.
- Preconditions that explain apparent differences.

Each relationship requires both source locators and an evidence statement. Distinguish explicit relationships from inferred ones. Keep source-specific variants intact.

## STRICT QUALITY PRESERVATION — NO COMPRESSION / NO MERGING

This section overrides any default tendency toward concise chapter summaries, token budgets, density optimization, or equalized output length. It does not override platform safety, copyright, or actual capability limits.

### 1. No progressive quality degradation

Maintain the same extraction schema, depth, granularity, verification standard, and source traceability from the first source unit to the last. Later chapters must not become shorter, less detailed, or less rigorously audited because the task is long or the remaining context/output budget is smaller.

### 2. No unauthorized merging

Never merge chapters, sections, frameworks, independent rules, tables, formulas, procedures, or anti-patterns to reduce effort. Each chapter remains independently auditable. Cross-chapter synthesis is permitted only after component-level extraction is complete and must not replace it.

### 3. No summary substitution

A chapter recap, overview, or list of highlights is not an acceptable substitute for any applicable extraction category. Do not use phrases such as "key points" to silently omit source detail. Every category must be fully processed or explicitly marked as blocked/unavailable/not applicable after inspection.

### 4. Capacity constraints require more segments, not less quality

When context, output, time, or tool limits prevent completion:
- Stop at a logical source boundary.
- Preserve all completed outputs.
- Record exact completed and pending units in the checkpoint.
- Continue in a subsequent segment/session from the first incomplete item.
- Retain the complete schema and quality bar.
- Never shorten later units, merge them, or silently skip them to fit one response.

### 5. Continuation and state recovery

Maintain persistent artifacts where the execution environment supports file writing:
- `00_SOURCE_MANIFEST.md`
- `01_MASTER_COVERAGE_LEDGER.md`
- `02_EXECUTION_CHECKPOINT.md`
- One independent file per chapter/source unit.
- Master indexes for frameworks, rules, tables, formulas, anti-patterns, glossary, procedures, relationships, and conflicts.

Before resuming after a context reset or new session:
1. Read the source manifest and checkpoint.
2. Read the coverage ledger.
3. Read the last completed unit and the next pending unit.
4. Verify that completed artifacts exist and are not truncated.
5. Resume at the first incomplete item only.

Never assume persistence. Verify that the files exist and can be read. If persistent file storage is unavailable, emit a complete checkpoint in the response so the user can preserve it. Do not claim that a file was saved when it was not.

### 6. No false completion

A source unit is complete only after extraction and its completeness audit. The entire task is complete only when every accessible source unit and every applicable category is audited.

Use statuses:
- NOT STARTED
- IN PROGRESS
- PARTIALLY EXTRACTED
- EXTRACTED — PENDING AUDIT
- AUDITED — COMPLETE
- BLOCKED — SOURCE ACCESS
- BLOCKED — UNREADABLE CONTENT

Do not report COMPLETE when any accessible chapter, category, table, or critical passage remains unexamined.

### 7. Checkpoint format

At the end of every execution segment record:

```text
EXPORT STATUS: IN PROGRESS
SOURCE CORPUS:
LAST COMPLETED SOURCE UNIT:
LAST COMPLETED SECTION:
NEXT SOURCE UNIT:
NEXT SECTION:
COMPLETED EXTRACTION CATEGORIES:
PENDING EXTRACTION CATEGORIES:
BLOCKED ITEMS:
ARTIFACTS VERIFIED:
KNOWN SOURCE/EXTRACTION LIMITATIONS:
```

Resume without duplicating completed work, but re-check completed artifacts for corruption or truncation before relying on them.

## Execution workflow

### Phase 0 — Source inventory
Identify all supplied files and their metadata. Establish the authoritative corpus and detect missing volumes, pages, appendices, or companion files.

### Phase 1 — Structural mapping
Inspect title page, contents, preface, chapter/section headings, appendices, glossary, bibliography, index, tables, figures, and page ranges. Build the complete source map before detailed extraction.

### Phase 2 — Chapter-by-chapter analysis
Process each unit sequentially. For every unit:
1. Confirm its boundaries and accessible page range.
2. Inspect the complete unit, including notes, tables, figures, and examples.
3. Extract all applicable categories A–G.
4. Attach source locators to every record.
5. Record ambiguity, illegibility, and extraction losses.
6. Run the chapter completeness audit.
7. Write/verify the independent chapter artifact.
8. Update the coverage ledger and checkpoint.

Do not begin cross-chapter synthesis while individual units remain incomplete, except to record an explicit source cross-reference needed for traceability.

### Phase 3 — Corpus synthesis
Only after all accessible units have been individually audited:
- Build master indexes.
- Map cross-chapter dependencies.
- Record contradictions and variants.
- Deduplicate only exact duplicate records while preserving every source locator and version.
- Never collapse materially different rules or definitions.

### Phase 4 — Final audit
Compare the source map against the coverage ledger. Verify every chapter, section, table, figure, formula, and example identified as relevant. Distinguish complete, blocked, unreadable, ambiguous, and not-applicable records. Report exact limitations.

## Recommended output structure

```text
book_knowledge_base/
├── 00_SOURCE_MANIFEST.md
├── 01_MASTER_COVERAGE_LEDGER.md
├── 02_EXECUTION_CHECKPOINT.md
├── 03_MASTER_FRAMEWORK_INDEX.md
├── 04_MASTER_RULE_INDEX.md
├── 05_MASTER_TABLE_INDEX.md
├── 06_MASTER_FORMULA_INDEX.md
├── 07_MASTER_ANTIPATTERN_INDEX.md
├── 08_MASTER_GLOSSARY.md
├── 09_MASTER_PROCEDURE_INDEX.md
├── 10_CROSS_CHAPTER_RELATIONSHIPS.md
├── 11_CONTRADICTIONS_AND_AMBIGUITIES.md
├── 12_FINAL_COMPLETENESS_AUDIT.md
└── chapters/
    ├── chapter_001.md
    ├── chapter_002.md
    └── ...
```

Adapt file names to actual source structure, but retain one independently auditable artifact per source unit. If the platform cannot create files, output file-delimited Markdown sections without claiming persistence.

## Final report

Report:
- Total source units and pages identified.
- Units/pages actually inspected.
- Units fully extracted and audited.
- Extraction counts by category.
- Tables/formulas/figures identified, extracted, and blocked.
- Files/artifacts actually created and verified.
- Conflicts, ambiguities, OCR/layout limitations.
- Remaining work and exact continuation point.
- Final status: COMPLETE or PARTIAL.

Accuracy and completeness take priority over brevity. When the task is too large, expand the number of execution segments; do not reduce the depth of any segment.
