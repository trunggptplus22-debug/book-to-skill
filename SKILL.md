---
name: book-to-skill
description: "Converts books and documents into structured agent skills. Includes an opt-in ANALYZE_DEEP profile for exhaustive, source-faithful extraction without summarization or progressive compression."
---

# Book-to-Skill

Use the original general-purpose converter for standard conversions. For user requests that explicitly require exhaustive analysis, full extraction, source-level traceability, or ANALYZE_DEEP, you MUST load and follow the deep-analysis profile at [deep-analysis/ANALYZE_DEEP.md](deep-analysis/ANALYZE_DEEP.md).

## Mode selection

- Standard Book-to-Skill conversion: follow this skill's existing default workflow and output contract.
- ANALYZE_DEEP: follow the complete extraction schema, chapter workflow, quality-preservation rules, checkpoint protocol, and final audit in deep-analysis/ANALYZE_DEEP.md.
- Domain-specific specialization: use the relevant specialist skill (for example astro-book-to-skill/SKILL.md) in addition to the selected mode. Domain-specific requirements supplement, not replace, the deep-analysis profile.

## Deep-analysis non-negotiables

When ANALYZE_DEEP is active:
1. Do not substitute summaries for extraction.
2. Extract all applicable frameworks, atomic decision rules, tables/matrices, formulas, anti-patterns, glossary terms, procedures, exceptions, and cross-chapter dependencies.
3. Preserve each source chapter as an independently auditable unit.
4. Preserve original terminology, structure, qualifications, formulas, and source locators.
5. Do not invent or silently supplement source knowledge.
6. Keep original source content distinct from normalized AI-consumable structures.
7. Maintain a coverage ledger and execution checkpoint.
8. Do not merge independent units or progressively reduce depth in later chapters.
9. Under capacity limits, create more execution segments and resume from the first incomplete unit.
10. Never claim completion without a full source-coverage audit.

The deep-analysis profile is opt-in and does not alter the standard converter behavior for users who do not request it.
