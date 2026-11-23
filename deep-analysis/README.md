# ANALYZE_DEEP Profile

This directory contains the opt-in exhaustive extraction profile for Book-to-Skill.

## Activation

Use this profile when the user explicitly requests `ANALYZE_DEEP`, exhaustive extraction, no-summary analysis, or source-level traceability.

The root `SKILL.md` routes such requests here. Domain-specific skills (including `astro-book-to-skill`) remain additive: apply their specialist requirements together with the general deep-analysis contract.

## Execution requirements

1. Inventory the complete accessible source corpus.
2. Build a chapter/section map and master coverage ledger.
3. Extract each chapter independently using every applicable category in `ANALYZE_DEEP.md`.
4. Preserve source locators and distinguish source statements from normalized representations.
5. Maintain an execution checkpoint and verify saved artifacts before resuming.
6. Perform cross-chapter synthesis only after individual chapter audits.
7. Do not compress later chapters, merge independent units, or claim completion without a full audit.

The profile deliberately does not change standard conversion behavior for requests that do not activate deep analysis.
