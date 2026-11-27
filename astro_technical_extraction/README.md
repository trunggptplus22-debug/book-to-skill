# Astrology technical extraction (prototype)

A staged, conservative, source-faithful extraction extension. **Candidate extraction is heuristic, not a doctrine engine.** Records remain review-required. The upstream Book-to-Skill parser is not modified.

## Pipeline
1. Document IR, source locators and hashes
2. Conservative relevance triage
3. Candidate technical-record extraction
4. Strict block coverage reconciliation
5. Record validation and quality gate
6. Candidate graph (shared-token edges are not authoritative)
7. JSON export bundle
8. Manual-label benchmark

## Run tests
`python -m unittest discover -s astro_technical_extraction/tests -v`

The adapter's current upstream integration exposes flattened text. It marks page/table/layout fidelity as unavailable; the extension does not fabricate page references. Table/formula semantics, accurate layout-preserving parsing, manual benchmarks, NotebookLM execution and real-source testing remain required before the PR can be considered complete.
