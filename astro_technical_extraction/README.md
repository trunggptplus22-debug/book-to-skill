# Astrology Technical Extraction — Executable Foundation

Isolated technical-only extension for the existing Book-to-Skill repository.

## Implemented
- Typed Document IR with source locators, stable block IDs, JSONL and content hash.
- Conservative explainable technical relevance classifier.
- Block-level coverage accounting.
- Thin adapter boundary to the original extractor.
- Runtime capability probe for the active Python environment.
- Two starter notebooks and focused tests.

## Not implemented
Semantic rule extraction, formula/table reconstruction, alignment, dependency graph, production export and benchmark on real astrology texts remain future stages.

## Run tests
The repository's test suite uses pytest. With pytest installed:
```bash
python -m pytest astro_technical_extraction/tests -q
```

## Run a smoke test
```python
from astro_technical_extraction.document_ir import DocumentIR
from astro_technical_extraction.classifier import RuleBasedClassifier
ir = DocumentIR.from_text("SRC001", "source.txt", "Calculate the Ascendant from local sidereal time.")
print(RuleBasedClassifier().classify_many(ir.blocks)[0].to_dict())
```

The default adapter is paragraph-level when only flattened text is available. It does not reconstruct printed page numbers, table cells, formulas or layout that were lost upstream. The classifier is a first-pass triage tool; uncertain material is sent to REVIEW. Benchmarking is required before production use.

Run notebook `00_runtime_and_source.ipynb` in the actual NotebookLM code environment to test Python, libraries and filesystem behavior. That probe does not prove uploaded-source persistence, external network or GitHub access.
