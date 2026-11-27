# Astrology Technical Extraction — Executable Foundation

Isolated technical-only extension for the existing Book-to-Skill repository.

## Implemented
- Typed Document IR with source locators, stable block IDs, JSONL and content hash.
- Conservative explainable relevance classifier.
- Block-level coverage accounting.
- Thin adapter boundary to the original extractor.
- Runtime capability probe.
- Two starter notebooks and focused tests.

## Not implemented
Semantic rule extraction, formula/table reconstruction, alignment, dependency graph, production export and real-book benchmark remain future stages.

## Run tests
With pytest installed:
```bash
python -m pytest astro_technical_extraction/tests -q
```

The default adapter is paragraph-level if only flattened text is available. It cannot reconstruct lost printed page numbers, table cells, equations or layout. The classifier is baseline triage; ambiguous material is REVIEW. Benchmarking is required before production use.

Run `00_runtime_and_source.ipynb` in the actual NotebookLM code environment to inspect Python and filesystem capabilities. A successful runtime probe does not prove uploaded-source persistence, network or GitHub access.
