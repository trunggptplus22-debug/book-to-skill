# Notebook-first Technical Astrology Extraction

This folder contains a proposed notebook-first solution for isolating technical astrology content from source books.

Read [NOTEBOOK_SOLUTION.md](NOTEBOOK_SOLUTION.md) for scope, pipeline, schemas, notebook stages, validation rules, output structure and acceptance criteria.

This proposal does not change the original Book-to-Skill extractor. Python execution, layout-sensitive parsing, hashing and deterministic validation must run in an external Python notebook/runtime; NotebookLM is used for source-grounded inspection and semantic analysis, not as a Python runtime.
