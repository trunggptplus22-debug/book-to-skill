---
name: astro-book-to-skill
description: "Extracts astrology books and primary sources into auditable, technically precise agent skills. Use for Hellenistic, Medieval, Renaissance, traditional, horary, natal, predictive, electional, mundane, fixed-star, astronomical, and other astrological source material when the goal is to preserve doctrine, calculation rules, chart procedures, delineation logic, timing methods, exceptions, and source provenance rather than produce a generic summary."
---

# Astro Book-to-Skill

## Mission

Convert astrology books, primary sources, translations, lecture notes, technical manuals, tables, and research corpora into a structured, source-auditable astrology skill. Extract operational knowledge, not generic summaries. Preserve the source's own terminology, historical framework, assumptions, procedures, tables, exceptions, and limits of applicability.

This is a domain specialization of the repository's original `book-to-skill` workflow. The original root `SKILL.md` remains the general-purpose converter. This skill adds astrology-specific analysis and output requirements; it does not replace or silently modify the original converter.

## Non-negotiable principles

1. **Source fidelity:** distinguish explicit source statements, faithful paraphrases, cross-source synthesis, and analyst inference. Label each where ambiguity is possible.
2. **No doctrinal blending:** do not merge Hellenistic, Medieval, Renaissance, Vedic, Chinese, modern psychological, or other systems into a synthetic rule unless the source explicitly does so or the user requests a comparative synthesis.
3. **No silent correction:** preserve the author's rule even if it conflicts with another authority or modern convention. Put possible errors, variants, and conflicts in an audit section.
4. **Technical completeness:** retain inputs, preconditions, sequence, calculation method, decision criteria, exceptions, and output. A named technique without its operational procedure is an incomplete extraction.
5. **No invented authority:** never attribute a rule, dignity, orb, house meaning, timing method, formula, or interpretive claim to a source unless the inspected source supports it.
6. **Provenance at claim level:** record book, author, edition/translation when known, chapter/section, and printed page or stable source locator. Distinguish printed page from PDF page.
7. **Uncertainty is data:** mark illegible, missing, ambiguous, disputed, or translator-dependent material. Do not repair it by guessing.
8. **Reproducibility:** convert procedures into explicit algorithms, decision tables, pseudocode, and test cases where the source provides enough information.
9. **Copyright discipline:** synthesize and paraphrase. Do not reproduce long passages, proprietary tables, or substantial copyrighted text. Short quotations only when necessary and within applicable limits.
10. **No chart calculation by inference:** if a procedure depends on astronomical positions, house cusps, lots, primary directions, fixed stars, or time/location data, require verified inputs or a validated calculation engine. Do not fabricate chart values.

## Modes

- **Full conversion (default):** inspect the corpus, extract all relevant astrological doctrine and procedures, build the complete skill package, run consistency and provenance audits.
- **Analyze only:** produce a source-grounded extraction inventory and technical gap report; do not write skill files.
- **Generate from prior analysis:** use supplied analysis only after checking that each extracted claim has source locators; mark unverified claims.
- **Update / fold-in:** integrate new sources into an existing skill without erasing earlier doctrine. Preserve source-specific variants and add conflict records rather than flattening disagreements.
- **Comparative synthesis:** compare named traditions, authors, editions, or schools in separate columns/layers. Do not collapse them into one rule set.

## Workflow

### Step 0 — Lock the task and domain

Identify:
- requested astrological domain and subdomain;
- tradition, school, period, author, and source type;
- intended use: reference, study, chart delineation, prediction, calculation, algorithm design, or comparative research;
- whether the output is one book skill or a multi-source corpus skill.

If the source tradition is not explicit, infer only from explicit bibliographic or textual evidence and label the identification provisional. Do not assume that all astrology books use the same zodiac, house system, rulership scheme, aspects, dignities, or predictive logic.

### Step 1 — Validate and inventory sources

Use the original converter's extraction pipeline and supported formats where available. Inventory every supplied source before analysis. Record:
- filename and format;
- title and author/editor/translator;
- edition, publication date, language;
- page count or section count;
- extraction method and known extraction warnings;
- whether the source is primary, translation, commentary, modern reconstruction, dataset, or secondary study.

Check that extracted text belongs to the intended source. For PDFs, preserve both printed page labels and PDF page indices where available. For scans, identify OCR uncertainty; do not treat OCR output as authoritative without visual verification of critical passages, symbols, tables, and formulas.

### Step 1.5 — Classify technical structure

Classify the source as one or more of:
- doctrinal / conceptual prose;
- procedural / method manual;
- astronomical or mathematical;
- ephemeris, tables, or reference data;
- case studies / chart delineations;
- historical / textual commentary;
- mixed.

Use layout-aware extraction for tables, diagrams, glyphs, mathematical expressions, chart figures, and tabular data. Flag extraction loss explicitly. Do not normalize unusual notation until the original form has been preserved.

### Step 2 — Build the source map

Read the title page, contents, preface/introduction, chapter headings, appendices, glossary, bibliography, and index when available. Build a complete chapter map before extracting detailed rules.

For large works, use targeted retrieval by chapter, heading, index term, or page range. Do not rely on a small opening excerpt to characterize an entire book. Record sections that were not accessible or not yet inspected.

### Step 3 — Extract the doctrinal model

For each major concept or technique, capture:

| Field | Required content |
|---|---|
| Concept / technique | Exact source term; preserve original-language form where useful |
| Definition | What the source says it is |
| Function | What problem or astrological question it addresses |
| Tradition / scope | School, period, chart type, and conditions of use |
| Inputs | Required chart factors, astronomical data, dates, places, tables |
| Preconditions | Sect, house system, zodiac, planetary condition, data validity, etc. |
| Procedure | Ordered steps, not a loose description |
| Decision rules | If/then criteria, thresholds, rulerships, receptions, configurations |
| Exceptions | Exclusions, overrides, qualifications, edge cases |
| Output | What conclusion or event judgment the procedure yields |
| Provenance | Source locator(s) |
| Confidence | Direct / strongly supported paraphrase / uncertain / disputed |

Keep separate records for definitions, interpretive claims, computational rules, historical statements, and examples. A statement that a planet signifies something is not automatically a complete predictive rule.

### Step 4 — Extract technical astrology modules

Create only modules supported by the inspected sources. Possible modules include:

**A. Foundational conventions**
- tropical or sidereal zodiac and epoch assumptions;
- whole-sign, quadrant, equal, or other house systems;
- planetary set, nodes, lots, dignities, triplicities, terms/bounds, faces/decanates;
- sect, planetary joys, essential and accidental dignity;
- aspect doctrine, application/separation, orbs, configuration rules;
- rulership, dispositorship, reception, antiscia, contra-antiscia;
- day/night chart conditions and other chart preconditions.

**B. Chart construction and astronomical calculation**
- required birth/event data and time-zone handling;
- coordinate system, ecliptic/equatorial conventions, geocentric/topocentric assumptions;
- planetary longitudes, latitudes, right ascension, declination, obliquity;
- angles, house cusps, lots, fixed-star positions, precession and epoch;
- rounding, units, tolerances, and validation checks.

Do not assume the book supplies a complete calculation algorithm. Separate source-defined rules from externally supplied astronomical standards or engine behavior.

**C. Natal delineation**
- significator selection;
- house and topic assignment;
- lord condition and placement;
- essential/accidental dignity;
- sect, reception, aspects, configuration, and testimony;
- synthesis and priority rules;
- explicit limits and contrary testimony.

**D. Predictive techniques**
- profections, directions, distributions, solar returns, transits, progressions, time-lords, or other methods only when present in the source;
- significator/promissor selection;
- arc or time conversion;
- activation conditions;
- timing windows and uncertainty;
- event manifestation criteria;
- corroboration and contradiction rules.

**E. Horary / electional / mundane / fixed stars**
Extract the relevant question or event protocol, significators, radicality or validity checks, perfection/denial, timing, electional constraints, mundane scope, stellar conjunction/paran/heliacal conditions, and all stated exceptions only where the source addresses them.

### Step 5 — Formalize rules without changing them

Represent each rule in three coordinated forms where possible:

1. **Readable rule:** concise natural-language statement faithful to the source.
2. **Decision structure:** conditions, branches, exceptions, and priority.
3. **Executable specification:** pseudocode, JSON/YAML rule record, or testable function when the source gives deterministic criteria.

Recommended rule record:

```yaml
rule_id: AUTHOR-CHAPTER-NNN
name: "Source's rule name"
source:
  author: ""
  work: ""
  edition: ""
  chapter: ""
  printed_page: ""
  pdf_page: ""
tradition: ""
domain: ""
inputs: []
preconditions: []
procedure: []
conditions: []
exceptions: []
outputs: []
source_claim_type: direct | paraphrase | synthesis | inference
confidence: high | medium | low
unresolved_questions: []
```

Do not convert qualitative language into numeric thresholds unless the source defines those thresholds. Do not invent weights, scoring, or precedence. If algorithmization requires an assumption, isolate it as a proposed engineering hypothesis and never present it as the author's doctrine.

### Step 6 — Preserve variants and resolve conflicts transparently

When sources disagree:
- retain each rule under its own source and tradition;
- identify whether the disagreement is terminological, translational, computational, doctrinal, or interpretive;
- compare preconditions before declaring a contradiction;
- record the exact scope in which each rule applies;
- do not select a winner unless the user asks for adjudication and the evidence supports it.

Create `conflicts.md` with fields: issue, source A rule, source B rule, precondition differences, evidence, unresolved points, and resolution status.

### Step 7 — Build chapter references

Create one chapter or section reference file per substantive unit. Use a consistent template:

```markdown
# Chapter N — Exact Source Heading

## Source locator
- Work / author / edition:
- Printed pages:
- PDF pages:
- Extraction quality:

## Chapter thesis
## Astrological concepts and definitions
## Rules and techniques
## Required inputs and preconditions
## Procedure
## Decision tables
## Worked examples from the source
## Exceptions and limitations
## Cross-references
## Unresolved or ambiguous passages
## Evidence ledger
```

Worked examples must distinguish the author's actual example from a newly constructed illustration. Never silently substitute a modern chart or calculation for the source's example.

### Step 8 — Generate the skill index and reference files

The top-level `SKILL.md` must remain a concise operating manual and index, not a copy of the whole book. Generate only relevant files from this list:

- `chapters/` — source-mapped chapter references;
- `rules/` — atomic doctrine and procedural rule records;
- `tables/` — extracted and normalized tables with source locators;
- `algorithms/` — pseudocode and formal specifications;
- `examples/` — source examples and independently labelled test examples;
- `glossary.md` — technical terms with original spelling, transliteration, definition, and source;
- `conflicts.md` — variants and unresolved contradictions;
- `calculation-spec.md` — astronomical and chart-calculation conventions;
- `source-manifest.json` — source metadata and coverage;
- `evidence-ledger.csv` or `evidence-ledger.json` — claim-to-source mapping;
- `tests/` — rule-level fixtures and expected outcomes.

Do not create empty modules merely to satisfy a template. Mark unavailable modules as not covered in the source manifest.

### Step 9 — Quality assurance and adversarial audit

Run the following checks before declaring completion:

**Coverage**
- Every chapter/section in the source map is marked processed, intentionally excluded, or inaccessible.
- Every extracted rule has at least one locator.
- Every table, formula, diagram, and example identified as technically material is either captured or explicitly flagged as missing.

**Fidelity**
- No unsupported doctrine, invented thresholds, or merged traditions.
- Terminology and original notation are preserved.
- Paraphrases do not reverse conditions or omit exceptions.
- Translation uncertainty and OCR ambiguity are visible.

**Operational completeness**
- Each procedure specifies inputs, preconditions, ordered steps, branches, exceptions, and outputs where the source provides them.
- Each algorithmic rule can be traced to source evidence.
- Missing astronomical inputs or unverified calculations are not silently filled.

**Contradiction tests**
- Test rules against contrary testimony and stated exceptions.
- Check whether two apparent conflicts actually use different chart types, house systems, sect conditions, time periods, or traditions.
- Identify circular definitions, missing variables, and under-specified procedures.

**Regression tests**
- Create minimal test cases from source examples where enough data is present.
- Expected outputs must be source-derived, not invented to make the test pass.
- Label synthetic fixtures clearly.
- Do not claim numerical parity unless independently computed and verified.

Report passed, failed, blocked, and not-applicable checks separately.

### Step 10 — Final delivery report

Report:
- sources inspected and source coverage;
- skill files created;
- traditions and technical domains covered;
- extraction limitations and OCR/table issues;
- unresolved conflicts and ambiguities;
- rules formalized versus still descriptive;
- tests executed and results;
- claims or modules that require a verified ephemeris/calculation engine.

Do not claim that a skill is complete if source sections remain unread, critical tables were lost, or required chart calculations were not validated.

## Output architecture

A typical generated astrology skill:

```text
<skill-slug>/
├── SKILL.md
├── source-manifest.json
├── evidence-ledger.json
├── glossary.md
├── conflicts.md
├── calculation-spec.md
├── chapters/
├── rules/
├── tables/
├── algorithms/
├── examples/
└── tests/
```

Use progressive disclosure: keep the main `SKILL.md` small enough to route tasks, and load chapter/rule references only when relevant.

## Invocation

Use this skill when asked to turn an astrology book, collection of books, primary source, translation, technical table, or research corpus into a reusable, auditable skill. For general non-astrological books, use the repository's original `book-to-skill` skill instead.
