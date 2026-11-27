# Astrology Technical Extraction — Prototype

An isolated technical-only extraction extension for the original Book-to-Skill repository.

## Status

Prototype implementation of the foundational layers:
- typed Document IR with source locators and deterministic content hash;
- conservative, explainable rule-based relevance classifier;
- block-level coverage report;
- adapters and NotebookLM runtime capability probe;
- two starter notebooks and focused tests.

Not implemented yet: semantic rule extraction, formula/table reconstruction, alignment, graph generation, production export, and benchmark on real astrology books.

## Architecture

The original parser remains authoritative for input extraction. This package consumes its extracted text/records and converts them to a typed intermediate representation. It does not rewrite or replace the original parser.

The current text adapter is paragraph-level. It cannot reconstruct printed page numbers, table cells, figure coordinates, or mathematical layout when those were lost upstream. Such units must remain flagged for visual or layout-aware inspection.

## Install and test

From the repository root:

```bash
python -m pip install -e ".[test]"
python -m pytest astro_technical_extraction/tests -q
```

The repository currently does not declare a `test` extra; use the existing development/CI setup with `pytest` installed. No new runtime dependency is required.

Run the starter notebook from the repository root, or run a smoke test:

```python
from astro_technical_extraction.document_ir import DocumentIR
from astro_technical_extraction.classifier import RuleBasedClassifier

ir = DocumentIR.from_text("SRC001", "book.txt", "Calculate the Ascendant from local sidereal time.")
print(RuleBasedClassifier().classify_many(ir.blocks)[0].to_dict())
```

## NotebookLM runtime verification

Run `00_runtime_and_source.ipynb` in the actual NotebookLM-supported code environment. This probe reports the current Python runtime and installed libraries; it does not assume file access, persistence, network access, or GitHub access.

## Classifier policy

A technical word alone is not enough for TECHNICAL_CORE. The baseline combines astrological terms with procedural, formula, table, or structured-block evidence. Unclear material is routed to REVIEW. The classifier is a triage aid and requires evaluation against manually labelled source blocks before production use.
