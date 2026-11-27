# Astrology Technical Extraction Notebook — Design Specification

**Status:** Design proposal / notebook-first implementation plan  
**Target repository:** `trunggptplus22-debug/book-to-skill`  
**Base branch:** `master`  
**Feature branch:** `feature/astrology-technical-extraction-notebook`

## 1. Objective

Build a notebook-driven extraction pipeline for astrology books that identifies, separates, validates, and exports **technical astrological material only**.

The notebook is not a generic summarizer and does not attempt to interpret every paragraph. Its primary task is to detect technical units in the source, preserve their exact provenance, extract them into typed records, validate technical structures, and export a source-faithful technical corpus.

The target output is suitable for later conversion into an astrology skill, research corpus, calculation specification, or executable implementation plan.

## 2. Scope lock: what counts as technical astrology content

Include content that defines or operationalizes astrological systems, techniques, calculations, or judgments:

1. **System conventions and parameters**
   - Zodiac type, epoch, coordinate conventions, house systems, planetary set, rulership schemes, dignities, sect, aspects, orbs, lots, bounds/terms, faces, triplicities.
   - Include only where the source actually specifies them.

2. **Astronomical and chart calculation**
   - Date/time/place inputs, time zones, daylight-saving assumptions, coordinates, ephemeris data, planetary longitudes/latitudes, right ascension, declination, obliquity, ascendant, MC, house cusps, lots, directions, returns, profections, transits, heliacal events, parans, fixed stars.
   - Preserve formulas, units, coordinate frames, epochs, rounding and tolerances.

3. **Dignity and condition tables**
   - Essential/accidental dignity, domicile, exaltation, triplicity, terms/bounds, face, detriment, fall, sect, joy, speed, visibility, solar proximity, station, retrogradation, combustion, cazimi, reception.
   - Reconstruct tables with original row/column structure, footnotes, variants and gaps.

4. **Technical procedures and algorithms**
   - Ordered steps, preconditions, branch rules, decision criteria, intermediate values, outputs, termination, exceptions.
   - Distinguish descriptive explanations from executable procedures.

5. **Delineation and judgment rules**
   - House significators, rulers, receptions, aspects, configurations, testimony, strength/weakness, event judgment, timing rules.
   - Extract as atomic rules with conditions, action/judgment, rationale only if source-stated, exception, scope and provenance.

6. **Predictive timing methods**
   - Profections, annual/monthly/daily time lords, solar/lunar returns, primary directions, secondary progressions when source-based, transits, eclipses, ingress, fixed-star timing, electional timing, horary timing.
   - Do not mix methods from different traditions or authors.

7. **Technical examples and worked charts**
   - Chart data, tables, calculation sequences, rule applications and source conclusions.
   - Separate source-provided chart values from values recomputed by a separate calculation engine.

8. **Technical terminology**
   - Terms that are required to understand a calculation, procedure, dignity, configuration, rule, or chart judgment.
   - Preserve original-language term and source definition.

## 3. Exclusion policy

Exclude from the technical corpus by default:

- Author biography and personal anecdotes unrelated to a method.
- General historical narrative, cultural background, and philosophical discussion that does not define a technical premise or procedure.
- Inspirational, devotional, spiritual, or promotional prose.
- Broad personality descriptions and modern psychological commentary that do not express an operational astrological rule.
- Repetitive rhetorical explanation.
- Unsupported claims added by the model.

**Important:** Do not delete excluded material from source files. The notebook creates a *technical-only derivative*. Keep a source coverage ledger recording every inspected source unit and its disposition: INCLUDED, CONTEXT_ONLY, EXCLUDED, or UNREADABLE. A historical or philosophical passage must be retained as CONTEXT_ONLY when required to understand a technical rule, but it must not silently become a technical rule.

## 4. Non-negotiable fidelity rules

1. The book is the ground truth for what the author says.
2. Do not blend Hellenistic, Medieval, Renaissance, Vedic, Chinese, modern, or other systems unless the user explicitly requests comparison. Maintain separate tradition/author/edition scopes.
3. Do not silently modernize, correct, harmonize, or supplement a source rule.
4. Keep original notation and normalized notation in separate fields.
5. Every extracted item must carry a source locator. Distinguish printed page from PDF page index.
6. A missing condition, formula, threshold, unit, exception or rationale must be marked NOT SPECIFIED, not invented.
7. Preserve conflicting source formulations as separate records; create a conflict record rather than resolving them.
8. Copyright: produce structured notes and concise paraphrases; do not reproduce substantial copyrighted prose or proprietary tables verbatim. Preserve mathematical relations and factual structures without copying protected expression.
9. This pipeline extracts a source's technical doctrine; it does not certify that the doctrine is astronomically or historically correct.
10. If a calculation is independently recomputed, label it COMPUTED and record engine/version/inputs; never present it as a source quotation.

## 5. Notebook pipeline

### Stage 0 — Initialize run and source manifest

Inputs:
- One or more astrology books/source documents.
- Optional user scope: tradition, author, period, technical subdomain, intended use.
- Optional source metadata: edition, translator, publication year.

Actions:
- Assign stable Source IDs.
- Record filename, format, file hash if available, title, author/editor/translator, edition, language, publication data.
- Record primary/secondary/translation/commentary status if identifiable.
- Determine accessible page count / section count.
- Record extraction limitations and OCR warnings.

Outputs:
- `00_SOURCE_MANIFEST.json`
- `00_SOURCE_MANIFEST.md`

Gate:
- Do not start extraction until source identity and available access are recorded.
- Uncertain bibliographic fields remain UNKNOWN.

### Stage 1 — Document and technical-layout parsing

Purpose: preserve layout and source evidence before semantic interpretation.

Extract typed blocks:
- HEADING
- PARAGRAPH
- LIST
- TABLE
- TABLE_CELL
- EQUATION
- SYMBOL/GLYPH
- FIGURE/CAPTION
- CODE
- FOOTNOTE
- PAGE_HEADER/FOOTER
- REFERENCES
- UNKNOWN

For each block record:
- block_id, source_id, sequence_index
- printed_page, pdf_page_index
- section_path, heading_id
- block_type
- raw_text or structured payload
- table_id / equation_id / figure_id when applicable
- extraction_method
- extraction_confidence
- OCR/layout warnings

Notebook operations:
- Upload original book as a source.
- Use NotebookLM source-grounded extraction to inspect the original source.
- For tables, mathematical notation, charts, glyphs, and scanned pages, use a layout-aware external extraction path when NotebookLM source rendering does not preserve structure.
- Do not treat flattened text as an adequate table or formula representation.

Outputs:
- `01_DOCUMENT_IR.jsonl`
- `01_DOCUMENT_IR.md`
- `01_LAYOUT_WARNINGS.json`

Gate:
- Every page/section must be represented as processed, inaccessible, or unreadable.
- Critical formula/table/chart regions must be visually checked when OCR/layout loss is suspected.

### Stage 2 — Technical relevance classifier

Classify each Document IR block as one of:

- TECHNICAL_CORE: operational rule, calculation, formula, table, method, algorithm, chart factor, technical definition.
- TECHNICAL_CONTEXT: background necessary to interpret a technical item.
- HISTORICAL_CONTEXT: historical information, dates, authorship, transmission, textual history.
- PHILOSOPHICAL_CONTEXT: conceptual/metaphysical discussion not itself an operational rule.
- BIOGRAPHICAL: biography or anecdote.
- GENERAL_COMMENTARY: non-operational prose.
- EXAMPLE_CASE: worked chart or illustrative application.
- UNCERTAIN: cannot confidently classify.

Required classifier output:
- block_id
- class
- reason
- inclusion_decision: INCLUDE / CONTEXT_ONLY / EXCLUDE / REVIEW
- linked_technical_item_ids (initially empty)
- confidence
- human_review_required

Classification rules:
- A sentence is not technical merely because it contains an astrological word.
- A definition can be technical if it defines a term used in a method/system.
- History is CONTEXT_ONLY when it establishes the provenance, date, school, edition or scope of a technical rule.
- Philosophical premises are CONTEXT_ONLY only when a technical procedure explicitly depends on them.
- Never discard UNCERTAIN records; add to review queue.

Outputs:
- `02_RELEVANCE_CLASSIFICATION.jsonl`
- `02_EXCLUSION_REVIEW.md`

Gate:
- All pages/blocks have a disposition or are marked inaccessible.
- Low-confidence / UNCERTAIN blocks are preserved for human review.

### Stage 3 — Technical extraction into separate typed tracks

#### Track A: Semantic astrology data

Extract:
- Concepts and source definitions.
- Astrological propositions and doctrinal statements.
- Atomic delineation/judgment rules.
- Preconditions and applicability scope.
- Procedure steps and decision branches.
- Mechanisms/rationales explicitly stated by the source.
- Exceptions, limitations and source-specific variants.
- Cross-chapter references and dependencies.
- Worked-example interpretations, distinguished from general rules.

Atomic rule schema:
```json
{
  "rule_id": "RULE-SRC01-CH04-0001",
  "source_id": "SRC01",
  "tradition": "SOURCE_STATED_OR_UNKNOWN",
  "author_scope": "AUTHOR_OR_UNKNOWN",
  "term_original": "source wording",
  "rule_type": "DELINEATION | CONFIGURATION | TIMING | HORARY | ELECTIONAL | OTHER",
  "when": [],
  "required_inputs": [],
  "operation_or_judgment": "faithful concise paraphrase",
  "rationale": "SOURCE_STATED | NOT_EXPLICITLY_EXPLAINED",
  "exceptions": [],
  "scope_conditions": [],
  "output": "source-stated result",
  "formalization_status": "EXPLICIT | FAITHFUL_NORMALIZATION | DIRECTLY_DERIVABLE | AMBIGUOUS",
  "source_locators": [],
  "review_status": "UNREVIEWED"
}
```

#### Track B: Technical/structured astrology data

Extract:
- Equations and formulas.
- Variable definitions, units, constants and calculation order.
- Tables: dignities, bounds/terms, triplicities, faces, rulerships, planetary data, orb tables, time-lord tables, star catalogues.
- Coordinate systems, epochs, time conventions and astronomical parameters.
- Chart structures and positions as represented in source.
- Algorithms, pseudocode, ordered calculation steps, decision trees.
- Code snippets and machine-readable data when present.
- Worked calculation inputs and expected outputs.

Technical record schema:
```json
{
  "technical_id": "TECH-SRC01-CH04-0001",
  "source_id": "SRC01",
  "technical_type": "FORMULA | TABLE | VARIABLE | CONSTANT | UNIT | ALGORITHM | POSITION_DATA | COORDINATE_CONVENTION | CODE | OTHER",
  "name": "source label",
  "original_representation": "exact mathematical/table/code notation where permitted",
  "normalized_representation": null,
  "variables": [],
  "units": [],
  "preconditions": [],
  "calculation_steps": [],
  "rounding_or_tolerance": "NOT_SPECIFIED",
  "limitations": [],
  "source_locators": [],
  "extraction_status": "UNREVIEWED"
}
```

Rules:
- Never merge source values with independently computed values.
- Preserve original table ordering and labels.
- Record missing or illegible cells individually.
- Never invent an orb, dignity, threshold, conversion, formula or astronomical constant.

Outputs:
- `03A_SEMANTIC_ASTROLOGY.jsonl`
- `03B_TECHNICAL_ASTROLOGY.jsonl`
- `03C_TECHNICAL_TABLES.md`
- `03D_FORMULAS_AND_ALGORITHMS.md`

### Stage 4 — Semantic–technical alignment

Link semantic items to technical evidence only when the source supports the link.

Allowed relation types:
- RULE_SUPPORTED_BY_TABLE
- RULE_USES_FORMULA
- CONCEPT_REPRESENTED_BY_VARIABLE
- PROCEDURE_USES_ALGORITHM
- TECHNIQUE_REQUIRES_PARAMETER
- EXAMPLE_INSTANTIATES_RULE
- RULE_QUALIFIED_BY_EXCEPTION
- ITEM_LOCATED_AT_SOURCE

Each link:
- alignment_id
- semantic_item_id
- technical_item_id
- relation_type
- evidence_statement
- source_locators
- alignment_status: EXPLICIT / DIRECTLY_DERIVABLE / AMBIGUOUS / UNVERIFIED
- reviewer_note

Do not use a generic semantic similarity score as proof of equivalence. Similarity may propose candidates; source evidence must establish the final link.

Outputs:
- `04_ALIGNMENT_LINKS.jsonl`
- `04_ALIGNMENT_UNRESOLVED.md`

### Stage 5 — Technical validation

Run validation by type:

**Formula validation**
- Syntax parse where possible.
- Symbol inventory complete or missing variables explicitly recorded.
- Unit dimensional checks only where units are specified.
- Check equation consistency without silently correcting source notation.

**Table validation**
- Row/column counts.
- Duplicate or missing cells.
- Domain coverage where the source defines a complete domain.
- Preserve exceptions and footnotes.
- Distinguish illegible from empty cells.

**Algorithm validation**
- Inputs, preconditions, ordered steps, branches, outputs and termination.
- Mark underspecified steps.
- Do not turn prose into executable code unless semantics are complete and the user requests implementation.

**Astrology-specific validation**
- Confirm zodiac, epoch, house system, planetary set, sect convention, dignity scheme, aspect doctrine, orbs and time conventions are known or explicitly UNKNOWN.
- Do not assume different authors use identical conventions.
- Validate technical chart values only with a separately identified ephemeris/calculation engine and recorded settings.

Outputs:
- `05_TECHNICAL_VALIDATION.json`
- `05_TECHNICAL_GAPS.md`

### Stage 6 — Cross-chapter structure and knowledge graph

Build typed nodes:
- SOURCE, CHAPTER, SECTION, TECHNICAL_BLOCK
- CONCEPT, DEFINITION, RULE, PROCEDURE, EXCEPTION
- FORMULA, VARIABLE, CONSTANT, UNIT, TABLE, TABLE_CELL, ALGORITHM
- EXAMPLE, TRADITION, AUTHOR, EDITION

Build typed edges:
- DEFINES, USES, REQUIRES, APPLIES_TO, EXCEPTS
- SUPPORTED_BY, IMPLEMENTED_BY, DERIVED_FROM
- PRECEDES, DEPENDS_ON, CONTRADICTS, VARIANT_OF
- LOCATED_AT, EXAMPLE_OF

All nodes and edges must retain provenance. Store explicit and inferred edges separately.

Outputs:
- `06_ASTRO_KNOWLEDGE_GRAPH.json`
- `06_CROSS_CHAPTER_DEPENDENCIES.md`
- `06_CONFLICTS_AND_VARIANTS.md`

### Stage 7 — Technical-only skill package generation

Generate skill materials from validated records, not directly from unstructured book text.

Suggested output:
- `SKILL.md`: concise entry point, system scope, source map, module index.
- `chapters/`: one technical extraction file per source chapter.
- `techniques/`: one procedure per technique.
- `rules/`: atomic rule registry.
- `tables/`: reconstructed technical tables.
- `formulas/`: formulas and variable dictionaries.
- `algorithms/`: pseudocode and decision trees.
- `glossary.md`: technical terms only.
- `source_register.md`: source provenance and edition details.
- `coverage_ledger.md`: inspected/included/context-only/excluded/unreadable coverage.
- `conflicts.md`: preserved differences and unresolved contradictions.

The generated technical skill must not silently include general historical, philosophical, biographical or psychological content as doctrine.

### Stage 8 — Coverage audit and final report

Report:
- Total sources, pages/sections and blocks.
- Included technical blocks.
- Context-only blocks.
- Excluded blocks.
- Uncertain/review blocks.
- Unreadable/inaccessible blocks.
- Count of concepts, rules, formulas, tables, algorithms and procedures.
- Missing variables, cells, units, preconditions and exceptions.
- Alignment links verified vs unresolved.
- Conflicts and source variants.
- Validation failures and warnings.
- Exact list of files generated.

Completion cannot be claimed if source units remain unprocessed, or if technical tables/formulas have unresolved extraction problems that materially affect the intended use.

## 6. Notebook execution contract

Use one source unit or one bounded chapter segment per extraction pass. Maintain a checkpoint after every pass.

Commands:
- `START`: initialize manifest and classify the selected source.
- `NEXT CHAPTER`: process the next uncompleted source unit only.
- `EXTRACT TECHNICAL ONLY`: run the technical-relevance filter and extraction for the current source unit.
- `REVIEW UNCERTAIN`: show uncertain blocks and request a decision.
- `STATUS`: report coverage and checkpoint without new extraction.
- `EXPORT`: assemble current validated records into deliverable files where the runtime permits.
- `STOP`: stop and record exact state.

NotebookLM is the source-grounded research and analysis surface. It must not claim to execute Python, create files, calculate charts, or write to GitHub unless an external connected execution service actually performs and verifies that operation. Large tables, scanned pages, formula recognition, file hashing and deterministic validation should use an external Python notebook/runtime when available.

## 7. Suggested implementation architecture

Keep the existing Book-to-Skill extractor unchanged. Add a separate specialist package:

```text
astro_technical_extraction/
  schemas/
    document_block.schema.json
    semantic_item.schema.json
    technical_item.schema.json
    alignment_link.schema.json
  notebook/
    00_source_manifest.ipynb
    01_document_ir.ipynb
    02_relevance_classifier.ipynb
    03A_semantic_extraction.ipynb
    03B_technical_extraction.ipynb
    04_semantic_technical_alignment.ipynb
    05_validation.ipynb
    06_knowledge_graph.ipynb
    07_export.ipynb
    08_coverage_audit.ipynb
  src/
    document_parser.py
    relevance_classifier.py
    semantic_extractor.py
    technical_extractor.py
    astrology_schema.py
    alignment_engine.py
    table_validator.py
    formula_validator.py
    provenance.py
    coverage.py
    graph_builder.py
    exporter.py
  tests/
    fixtures/
    test_document_ir.py
    test_relevance_classifier.py
    test_table_reconstruction.py
    test_formula_provenance.py
    test_alignment.py
    test_coverage.py
```

This is a proposed extension, not a claim that these files already exist. It should be implemented as a separate package/branch and integrated only after tests and a benchmark against a manually annotated astrology chapter.

## 8. Acceptance criteria

A pilot notebook passes only if:

1. Every source page/section has an explicit coverage status.
2. Every extracted technical item has a valid source locator.
3. Technical tables preserve row/column relationships and identify missing cells.
4. Formula records preserve original notation separately from normalized notation.
5. Semantic rules and technical records remain separate until alignment.
6. Every cross-layer link has evidence and a verification status.
7. Uncertain passages remain visible in a review queue.
8. No unsupported tradition, dignity, orb, threshold, timing rule, formula or chart value is invented.
9. Historical/philosophical/biographical prose is excluded from the technical output unless explicitly retained as technical context.
10. Output files can be regenerated from the same source and settings, with extraction version and run manifest recorded.
11. No claim of full completion is made while any required source segment remains unreadable, unprocessed or materially unresolved.

## 9. Non-goals

- Replacing or modifying the original Book-to-Skill extractor.
- Rewriting the astrology source into a generic summary.
- Blending different astrology traditions.
- Automatically correcting historical authors.
- Performing natal chart calculations unless a separate validated calculation engine and full input settings are explicitly supplied.
- Treating LLM confidence or semantic similarity as proof.
