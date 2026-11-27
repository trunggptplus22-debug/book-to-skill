# Astrology Technical Extraction Notebook — Updated Implementation Plan

**Status:** Design plus executable foundation prototype  
**Repository:** `trunggptplus22-debug/book-to-skill`  
**Feature branch:** `feature/astrology-technical-extraction-notebook`

## Objective
Build a technical-only astrology extraction extension while reusing the original Book-to-Skill parser and leaving its behavior unchanged.

## Runtime principle
Do not hard-code assumptions about NotebookLM execution capabilities. Probe its actual code-execution surface. Test Python, working-directory writes, uploaded-source access, persistence, package installation, external network, GitHub access and artifact export independently. Enable a capability only after its live test succeeds. The same deterministic package remains portable to Jupyter/Colab as a fallback.

## Implemented foundation
Typed Document IR, provenance locators, JSONL/hash export, conservative classifier, block-level coverage, parser adapter boundary, runtime capability probe, two starter notebooks and focused tests.

## Next stages
1. Preserve page/table/equation structures where original parsers expose them.
2. Add source manifest/hash exporter and section-context propagation.
3. Benchmark classifier against manually labelled astrology passages; improve using layout and section context.
4. Implement semantic rules, formulas/variables/units and technical table extraction as separate tracks.
5. Add alignment, validation, dependency graph, exporters and final coverage audit.
6. Benchmark at least one public-domain traditional astrology source and one table/formula-heavy source.

## Quality gates
No changes to original parser behavior; preserve source locators or mark them unavailable; term presence alone does not cause automatic inclusion; ambiguity remains reviewable; every block receives a disposition; no unsupported doctrine or astronomical values are invented.
