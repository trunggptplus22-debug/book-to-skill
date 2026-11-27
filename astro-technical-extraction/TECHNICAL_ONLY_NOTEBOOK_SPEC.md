# Technical-only Astrology Extraction — Execution Specification

The executable foundation is implemented in the sibling package `astro_technical_extraction/`. Existing technical taxonomy, canonical schemas, provenance rules and source-fidelity constraints remain governing requirements.

## Execution workflow
1. Probe active runtime and source access.
2. Extract with the existing Book-to-Skill parser.
3. Convert extracted content to typed Document IR.
4. Classify every block; preserve ambiguous blocks for review.
5. Export classification and coverage ledgers.
6. Continue with separate semantic, formula, table, alignment, validation and export modules.

## Current prototype limits
- Text adapter is paragraph-level when fed flattened text.
- Printed page labels and PDF page indices are retained only when parser records supply them.
- Formula/table reconstruction is not implemented.
- Classifier is baseline triage, not production accuracy.
- NotebookLM file access, persistence and installed packages are capability-probed, not assumed.
