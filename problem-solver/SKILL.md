---
name: thesis-driven-problem-solver
description: Solve unfamiliar problems by first describing the real-world/domain-specific phenomenon in precise academic and operational detail; characterize the objects, vocabulary, source ecology, data quality, knowledge form, rule explicitness, validation limits and failure modes; then formulate researchable theses, identify exact professional or academic expertise, discover authorities and source material, build evidence-grounded skills, and verify the solution. Use especially when the problem is vague, interdisciplinary, historically layered, based on weakly structured sources, or cannot yet be framed as a conventional thesis.
---

# Thesis-Driven Problem Solver

## Mission

Resolve the user's actual problem. Do not start with generic problem definitions, tool recommendations or an assumed thesis structure. First discover what the problem consists of in its native context, describe the observable facts and source/data conditions, and identify the methods required to characterize it. Only then formulate a researchable thesis and build missing capabilities.

## Core sequence

1. Observe the actual problem in domain-native detail.
2. Characterize the domain, objects, data, source ecology, uncertainty and failure morphology.
3. Separate directly observed facts from interpretations and assumptions.
4. Identify which aspects are researchable and which are not yet testable.
5. Formulate one or more precise theses only after characterization.
6. Decompose each thesis into work packages and exact specialist methods.
7. Find the strongest relevant practitioners first; use academic authority discovery when practitioners cannot be established or foundational theory is required.
8. Find the actual methods, textbooks, authors, official syllabi, standards and primary research.
9. Locate existing skills/tools that perform the needed method; do not invent a skill category before searching.
10. Build or adapt only the missing skills using the best-fit skill engineering workflow.
11. Apply, test, falsify and independently review the solution.
12. Report what is established, provisional, disputed and unknown.

Do not jump from a vague input directly to thesis, expert, textbook or skill creator.

## Stage 1 — Detailed problem observation

Describe:
- the real setting and operating context;
- actors, objects, artifacts, processes and decisions involved;
- concrete examples, excerpts, records or observed outputs;
- current workflow and where it breaks;
- frequency, magnitude and consequences where available;
- successful, failed, ambiguous and boundary cases;
- available evidence and missing evidence;
- competing explanations;
- cost of false conclusions and reversibility.

Use `templates/problem-observation.md`. Do not replace a concrete problem with an abstract label such as "knowledge management", "AI optimization" or "astrology analysis".

## Stage 2 — Domain characterization (mandatory when domain is unfamiliar, vague or source-dependent)

Read `DOMAIN_CHARACTERIZATION.md` and produce `00-domain-characterization.md` using `templates/domain-dossier.md`.

Inspect the domain's actual properties:
- ontology: what kinds of objects, events, records, symbols, calculations, procedures and claims exist;
- vocabulary: native terms, polysemy, historical shifts, school-specific meanings, translation choices and implicit context;
- source ecology: primary texts, editions, manuscripts, commentaries, textbooks, oral teaching, cases, databases, websites, code and software;
- transmission: variant versions, authorship attribution, quotations, editorial layers, translation, paraphrase and OCR/transcription issues;
- knowledge form: declarative, procedural, interpretive, numerical, tacit, case-based, normative or diagrammatic;
- explicitness: stated rules, compressed formulae, missing preconditions, hidden intermediate steps and exceptions;
- evidence: historical, textual, observational, experimental, statistical, testimonial, anecdotal or unsupported;
- reproducibility: whether independent trained analysts obtain the same output from the same input;
- validation: what can be checked and with what independent data;
- contradictions: differences in school, era, definition, edition, context, assumptions or genuine incompatibility;
- data defects: missingness, selection bias, survivorship, duplicated/copying sources, retrospective fitting and absent negative cases;
- technical needs: annotation, controlled vocabulary, ontology, knowledge graph, rule engine, calculation engine, statistical validation or human review.

Do not assume each defect exists in every corpus. Verify it against the material in scope. Separate characterization from endorsement: the presence of a doctrine in a book proves that the book records the doctrine, not that its prediction is empirically true.

## Stage 3 — Thesis formation after characterization

The thesis must be shaped by the type of problem actually found. Use a conventional empirical thesis only when outcomes and a defensible validation design exist.

Possible thesis families include:
- textual: establish the provenance, edition history, variant readings or attribution of a passage;
- semantic: distinguish meanings of a technical term across sources, schools and periods;
- doctrinal: compare the rules and assumptions of specific traditions;
- operational: formalize an incomplete or tacit method into reproducible steps;
- computational: specify and validate a calculation, data model or deterministic engine;
- empirical: test a defined claim against independent outcome data;
- methodological: design a data collection, annotation or validation framework;
- engineering: build a system that preserves provenance, uncertainty, conflicts and traceability.

A thesis must name the specific object, claim or procedure, method of inquiry, scope, evidence needed and conditions under which the conclusion would be revised. Do not impose measurable prediction accuracy when the available material only supports textual or doctrinal research.

## Stage 4 — Specialist decomposition

For every observed defect or thesis question, identify the exact method required, then the specialist who practices that method. Do not select a prestigious expert first and retrofit the problem to their expertise.

Examples:
- variant classical Chinese passages → classical philology / textual criticism / collation;
- ambiguous historical terminology → historical semantics / sinology / intellectual history;
- tacit rule reconstruction → domain practitioner + knowledge acquisition / process modeling;
- source-to-claim traceability → information science / knowledge representation / provenance engineering;
- inconsistent deterministic calculation → mathematical specification / software verification;
- missing independent outcome records → research design / statistics / causal inference;
- interpretive inter-school conflict → history of ideas + practitioners from each school;
- unstructured corpora → digital humanities / corpus linguistics / document engineering.

These are candidate mappings. Establish the actual method from the problem evidence and source inspection.

## Stage 5 — Authority discovery

### Practitioner route first

Find people who actually perform the required work, not merely general commentators. Verify relevance through documented projects, outputs, methods, publications, standards contributions, case work, peer recognition and evidence of results. Distinguish master practitioner, teacher, historian, philologist, statistician, engineer and software implementer; these are not interchangeable expert roles.

### Academic fallback

When a suitable practitioner is not identifiable, or the required method is academic/foundational, follow this trace:
Ivy League institution → relevant department/program → course → instructor → official syllabus → textbook/required readings → author/editor → relevant chapters and methods.

Verify every link through official or primary sources. If no direct match exists among Ivy League institutions, expand to other leading research universities, specialist institutes and professional associations. Do not select an unrelated Ivy course simply to preserve prestige.

### Multiple authorities

A single domain may need several experts. For classical mệnh lý texts, for example, a domain practitioner may explain how a rule is used; a classical Chinese philologist may analyze the wording; a textual critic may compare editions; a knowledge engineer may formalize the rule; a statistician may design an external validation study. No one role can substitute for the others.

## Stage 6 — Source and claim analysis

Build a source register and claim ledger. For every material claim record:
- exact source and edition/version;
- author/editor/translator/attribution and attribution confidence;
- exact location (chapter, page, section, line or evidence ID);
- source type and transmission route;
- what the source directly states;
- agent interpretation, kept separate;
- corroborating and conflicting evidence;
- what the source can establish and what it cannot;
- whether the relevant material was actually inspected.

Never claim complete reading from metadata, preview snippets or secondary summaries. Preserve variant wording and uncertainty. Do not silently fill missing steps in a method.

## Stage 7 — Skill and tool discovery BEFORE skill creation

Search for existing skills, libraries, repositories and tools that implement the needed method. Search by the actual specialist methods discovered in stages 2–5, not only by generic "skill creator" keywords.

For every candidate, inspect:
- exact functionality and supported inputs;
- output artifacts and data model;
- methodology and evidence handling;
- dependencies, runtime and supported hosts;
- maintenance, tests, license and known limitations;
- overlap with existing tools and skills;
- whether it can be adapted or should only be used as a reference.

Prefer an existing tool when it performs the required task reliably. Build a new skill only for a missing capability or a justified integration layer.

## Stage 8 — Skill engineering

Select the tool based on the actual source and capability architecture:
- **Book Skills Creator**: preferred when a source corpus needs capability decomposition into atomic skills, combo workflows, a router and references with evidence IDs, conflict tracking and deterministic validation.
- **Book-to-Skill**: use for broad document ingestion, multi-format book processing, chapter-aware reference generation or configured remote book search; it is not itself a substitute for source criticism or empirical validation.
- **Meta Skill Creator / skill-architect tools**: use for individual skill design, trigger quality, boundaries, progressive disclosure, eval strategy and maintainability.
- **Domain-specific skills**: search and reuse specialist skills for textual criticism, research methods, corpus annotation, statistics, ontology engineering, knowledge graphs, provenance, software verification or other methods actually needed.

Treat these components as complementary. A converter extracts and organizes; a domain method interprets; a pack architect decomposes capabilities; a skill creator shapes runnable instructions; an evaluator tests behavior. Do not expect one tool to perform all five jobs.

Every skill must identify inputs, preconditions, steps, decision rules, exceptions, outputs, provenance, limitations and tests. Keep source text separate from synthesized procedural knowledge. Preserve unresolved disagreement rather than forcing consensus.

## Stage 9 — Validation and solution

Validate the skill pack structurally and semantically. Then apply it to the original problem. Distinguish:
- source fidelity;
- rule extraction correctness;
- interpretation consistency;
- calculation correctness;
- empirical validity;
- usefulness for the user's goal.

A skill may pass source fidelity while its underlying doctrine remains empirically unvalidated. A calculation engine may be numerically correct while the source rule it implements is disputed. Report these dimensions separately.

## Stage 10 — Final report

Deliver:
1. detailed problem observation;
2. domain characterization dossier;
3. candidate thesis/theses and why selected;
4. map from observed problem to required disciplines and methods;
5. expert dossiers with evidence;
6. textbook/source register with author, edition and inspected sections;
7. existing skills/tools discovered and selection rationale;
8. new/updated skill pack and validation report;
9. applied solution and evidence;
10. limitations, unresolved conflicts and next data required.

## Stop and uncertainty rules

Ask one focused question only when a missing user-controlled fact changes the object of analysis, source scope, safety, jurisdiction or acceptance criteria. Continue on bounded assumptions where safe.

Stop or mark a work package blocked when evidence is inaccessible, attribution is unverified, the text is too corrupt to interpret, the procedure lacks essential steps, the methods conflict, or the required external test cannot be performed. Do not invent a source, expert, rule, citation, case result or validation result.
