# Technical-only Astrology Extraction for Notebook

This is a notebook-first extension for extracting only the technical content of astrology books. It complements `astro-book-to-skill/SKILL.md` and does not modify the original Book-to-Skill extractor.

## Governing distinction

- **Source truth:** the inspected book and its exact locators.
- **Technical source blocks:** the technical material as it appears in the book.
- **Normalized technical records:** a separate representation produced after preserving the source form.
- **Semantic interpretation:** excluded from the technical-only deliverable unless required to identify or explain the operation of a technical rule. When included, it is limited to the minimum explanation needed to understand the operation and remains separately labelled.

This notebook is not a general astrology summarizer. It does not extract biography, broad history, metaphysical exposition, spiritual advice, or psychological commentary as standalone output. Such material is retained only as brief context where it establishes the scope, provenance, convention, or precondition of a technical method.

## Technical-only inclusion taxonomy

Include these classes when present in the inspected source:

1. **Conventions and system parameters:** zodiac, epoch, coordinate frame, house system, planetary set, rulership scheme, dignities, sect, aspects, orbs, bounds/terms, faces, triplicities, lots, reception conventions.
2. **Astronomical calculation:** time and place inputs, time zones, daylight saving, coordinates, ephemeris assumptions, longitude/latitude, RA/declination, obliquity, angles, cusps, lots, directions, returns, fixed-star positions and related calculations.
3. **Tables and reference data:** essential dignities, bounds, triplicities, faces, rulerships, orb tables, time-lord tables, star catalogues, planetary speeds and other source-provided technical data.
4. **Procedures and algorithms:** inputs, preconditions, ordered operations, branch conditions, intermediate results, output, termination and exceptions.
5. **Delineation and judgment rules:** significator selection, houses, rulers, receptions, aspects, testimonies, conditions, priorities, event judgments and source-defined timing criteria.
6. **Predictive methods:** profections, time-lord sequences, solar/lunar returns, primary directions, transits, eclipses, ingress, fixed-star methods, electional and horary timing, only when the source contains them.
7. **Technical examples:** chart inputs, source-provided positions, worked calculations, decision sequences and author's conclusions, separated from model-generated examples.
8. **Technical terminology:** terms required to understand or execute a technical method, calculation, table or rule.

Classify each source block as `TECHNICAL_CORE`, `TECHNICAL_CONTEXT`, `EXAMPLE_CASE`, `HISTORICAL_CONTEXT`, `PHILOSOPHICAL_CONTEXT`, `BIOGRAPHICAL`, `GENERAL_COMMENTARY`, or `UNCERTAIN`. Only the first three normally enter the technical output. Context can be retained in a separate context note where necessary. Every block receives a disposition: `INCLUDE`, `CONTEXT_ONLY`, `EXCLUDE`, `REVIEW`, or `UNREADABLE`.

## Required extraction order

| Stage | Exact task | Primary result | Completion gate |
|---|---|---|---|
| 0 | Lock scope and source identity | Domain/source manifest | Tradition, author, work/edition and technical scope recorded or UNKNOWN |
| 1 | Build document/source representation | Document blocks with locators | Source units accounted for; extraction limitations recorded |
| 2 | Classify technical relevance | Technical inclusion ledger | Every inspected block classified or marked for review |
| 3A | Extract technical procedures and rules | Atomic technical rule records | Conditions, inputs, operation, outputs, exceptions and locators captured |
| 3B | Extract computational structures | Formula, variable, unit, algorithm records | Original notation preserved; gaps explicitly marked |
| 3C | Extract tables and chart/reference data | Structured tables/data records | Row/column order, labels, footnotes and missing cells audited |
| 4 | Align rules with tables/formulas/procedures | Evidence links | Every link has a supporting source locator or remains UNVERIFIED |
| 5 | Validate technical structure | Validation and gap report | No silent repairs; unverified units, symbols, cells and conventions listed |
| 6 | Map cross-chapter dependencies and variants | Technical dependency graph | Source-specific variants preserved |
| 7 | Export technical-only corpus | Markdown/JSONL/CSV outputs | All exported records retain source IDs and locators |
| 8 | Audit coverage | Final coverage ledger | No unprocessed source units represented as complete |

Stages 3A, 3B and 3C are separate extraction passes over the same source blocks. They are not interchangeable. Each can be processed chapter by chapter.

## Canonical schemas

### Source locator

```json
{
  "source_id": "SRC001",
  "file_name": "book.pdf",
  "work_title": "UNKNOWN",
  "author": "UNKNOWN",
  "edition": "UNKNOWN",
  "chapter_id": "CH04",
  "section_path": ["Chapter 4", "The Ascendant"],
  "printed_page": "UNKNOWN",
  "pdf_page_index": 63,
  "table_id": null,
  "figure_id": null,
  "equation_id": null,
  "block_id": "SRC001-CH04-BLK0063"
}
```

Printed page and PDF page index must never be conflated.

### Technical rule

```json
{
  "rule_id": "SRC001-CH04-RULE0001",
  "rule_name_source": "UNKNOWN",
  "rule_class": "CALCULATION | SELECTION | DELINEATION | TIMING | CONDITION | OTHER",
  "tradition_scope": "SOURCE_STATED_OR_UNKNOWN",
  "inputs": [],
  "preconditions": [],
  "ordered_operations": [],
  "decision_conditions": [],
  "priority_rules": [],
  "exceptions": [],
  "outputs": [],
  "source_status": "EXPLICIT | FAITHFUL_NORMALIZATION | DIRECTLY_DERIVABLE | AMBIGUOUS",
  "source_locators": [],
  "review_status": "UNREVIEWED"
}
```

### Formula / variable / unit record

```json
{
  "technical_id": "SRC001-CH04-FORMULA0001",
  "kind": "FORMULA",
  "original_notation": "SOURCE FORMULA",
  "normalized_notation": null,
  "variables": [
    {
      "symbol": "X",
      "definition_source": "NOT SPECIFIED",
      "unit": "NOT SPECIFIED",
      "domain": "NOT SPECIFIED"
    }
  ],
  "constants": [],
  "calculation_order": [],
  "rounding": "NOT SPECIFIED",
  "tolerances": "NOT SPECIFIED",
  "applicability": [],
  "exceptions": [],
  "source_locators": [],
  "validation_status": "UNVALIDATED"
}
```

### Table record

```json
{
  "technical_id": "SRC001-APP-TABLE0001",
  "kind": "TABLE",
  "source_title": "SOURCE TABLE TITLE",
  "row_labels": [],
  "column_labels": [],
  "cells": [],
  "footnotes": [],
  "missing_or_illegible_cells": [],
  "normalization_notes": [],
  "source_locators": [],
  "validation_status": "UNVALIDATED"
}
```

### Provenance and classification record

Every extraction record includes:
- `record_id`
- `source_id`
- `source_locator`
- `block_ids`
- `extraction_method`
- `source_claim_type`: `DIRECT`, `FAITHFUL_PARAPHRASE`, `NORMALIZED`, `DERIVED`, `INFERENCE`
- `confidence`: `HIGH`, `MEDIUM`, `LOW`, or `UNKNOWN`
- `review_status`
- `limitations`

Do not use confidence as a substitute for evidence. Semantic similarity may suggest a match, but it cannot establish technical equivalence.

## NotebookLM operating instructions

1. Add the original book as a source. Add this specification as a separate source.
2. Start by locking the book's tradition, author, edition, intended subdomain and technical-only scope. Unknown values remain UNKNOWN.
3. Process one chapter or bounded source unit at a time.
4. For each unit, classify blocks before extracting technical records.
5. Run separate passes for rules/procedures, formulas/variables, and tables/reference data.
6. Attach source locators to every record. If NotebookLM cannot verify a printed page, table cell, equation symbol or glyph, mark it UNKNOWN/UNREADABLE and request external visual inspection.
7. Do not invent values, fill missing cells, infer unspecified orbs, silently correct formulas, or complete absent algorithm steps.
8. Preserve variant techniques and conflicting conventions separately.
9. After each unit, update the progress ledger and continue only from the first incomplete unit.
10. Generate technical-only outputs after the chapter extraction passes are complete.

NotebookLM can perform source-grounded reading, classification, structured extraction and synthesis. It does not execute the repository's Python scripts, run local ephemeris calculations, guarantee layout-perfect table OCR, write files to arbitrary local paths, or call GitHub directly. Use a Python notebook/runtime for deterministic parsing, PDF page images, data validation, hashing, conversion and export. Distinguish NotebookLM-produced records from Python-computed records.

## Notebook prompts

### START
```text
START TECHNICAL ASTROLOGY EXTRACTION.
Read the technical-only specification and identify the source identity, tradition, author, edition, language, and intended technical scope. Do not extract detailed rules yet. Build the source manifest and report unknown fields. Then wait for confirmation of the source scope.
```

### PROCESS CURRENT CHAPTER
```text
PROCESS THE NEXT UNCOMPLETED CHAPTER ONLY.
First list its sections and source units. Classify every unit using the defined taxonomy. Then perform separate passes for (A) technical rules/procedures, (B) formulas/variables/units/algorithms, and (C) tables/reference data. Preserve source-specific terminology and original notation. Attach source locators to every output. Mark omissions, uncertainty, illegibility and missing data explicitly. Do not summarize excluded content. Update the coverage ledger and stop at the chapter boundary.
```

### TECHNICAL ONLY
```text
For the current source unit, extract only technical astrology content defined in the specification. Do not produce biography, general history, philosophy, spiritual advice, psychological interpretation or general prose summaries. Retain only the minimum context necessary to identify a technical convention, provenance, precondition or method scope. Classify uncertain material for review rather than guessing.
```

### AUDIT
```text
AUDIT THE CURRENT EXTRACTION. Check source coverage, every record's source locator, table row/column preservation, formula notation, variable definitions, units, procedure order, exceptions, and convention scope. Identify unsupported inferences, missing material, conflicting source variants and unverified values. Do not repair the source. Return a gap list and status.
```

## Deliverables

Recommended output package:

- `00_source_manifest.md`
- `01_source_coverage.jsonl`
- `02_technical_classification.jsonl`
- `03_rules_and_procedures.jsonl`
- `04_formulas_variables_units.jsonl`
- `05_technical_tables.jsonl`
- `06_algorithms_and_decision_trees.md`
- `07_alignment_and_dependencies.jsonl`
- `08_conflicts_and_variants.md`
- `09_technical_validation_report.md`
- `10_technical_only_index.md`

## Acceptance criteria

A run is complete only when:
1. Every accessible chapter/section/page unit has a coverage disposition.
2. Every technical record has a valid source ID and locator or is explicitly marked locator-unavailable.
3. Rules, formulas, tables and algorithms have been extracted as distinct record types.
4. Original notation is kept separate from normalized notation.
5. Missing inputs, units, thresholds, exception conditions and unreadable cells remain explicit.
6. Tradition, author, edition and technical conventions are not blended.
7. Technical-only filtering is auditable; excluded/context-only units are counted and retrievable in the ledger.
8. No external calculations are attributed to the book.
9. No completion claim is made while material sections remain unprocessed or materially unreadable.
