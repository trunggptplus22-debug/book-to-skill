# Operational Workflow — Observe, Characterize, Research, Build, Solve

## 0. Problem evidence intake

Create `00-problem-observation.md` using the supplied template. Capture the concrete setting, original terminology, examples, artifacts, failure modes, boundary cases and consequences. Mark every statement as observed, user-reported, source-reported, inferred or unknown.

Do not convert the input into a thesis yet.

## 1. Domain reconnaissance

Read `DOMAIN_CHARACTERIZATION.md`. Inventory the actual objects, terms, source types, knowledge forms, rules and evidence conditions. Inspect representative primary material rather than relying on a description of the field. For historical corpora, verify available editions and transmission evidence; for operational systems, inspect logs, workflows and real outputs; for scientific datasets, inspect schema, labels and collection protocol.

Create `00-domain-characterization.md`. Record the defects actually observed and their consequences. Use one row per defect in the form:

`observed defect → evidence → why it matters → specialist method → required deliverable`.

Do not fill this dossier with generic data-quality terms without examples or evidence.

## 2. Select a research design and thesis family

Decide whether the actual problem is textual, semantic, doctrinal, operational, computational, empirical, methodological or engineering. A mixed problem may require multiple linked theses. Determine the maximum claim level that the available sources can support. Then draft the research questions, hypotheses where meaningful, scope, method, evidence requirements, success criteria and disconfirmation/revision conditions.

If empirical outcomes are unavailable, a textual, semantic, doctrinal, reproducibility or validation-design thesis may be more rigorous than inventing a predictive-accuracy study.

## 3. Map issue to method to expert

For every diagnosed issue:
1. name the exact method that could investigate or solve it;
2. define what the specialist would actually do;
3. identify the precise profession/discipline;
4. define the evidence or output expected from that expert;
5. only then search for named people.

Build a matrix:

| Observation | Research question | Method | Professional role | Academic discipline | Deliverable | Dependency |
|---|---|---|---|---|---|---|

Examples: variant passages require collation; historical term shifts require historical semantics; incomplete procedures require practitioner elicitation plus formalization; weak prediction claims require research design and independent outcome data. Verify each mapping for the actual case.

## 4. Find authorities

### Practitioner-first
Search for the best practitioner who performs the exact task. Validate actual projects, methods, published material, outcomes and recognition. Distinguish:
- active practitioner;
- teacher/trainer;
- author/commentator;
- historian / philologist;
- statistician / methodologist;
- engineer / tool author;
- regulator / standards body.

More than one profile may be needed. Do not score a textual critic by business outcomes or an astrologer by unrelated academic credentials; use role-appropriate criteria.

### Academic route when needed
If no practitioner authority can be evidenced, or the work requires specialist scholarship, search:
1. relevant Ivy League institution and official department;
2. official course catalog / course page;
3. instructor and faculty profile;
4. official syllabus and reading list;
5. required textbook, edition, publisher and author/editor;
6. relevant chapters, papers and method.

If Ivy sources lack a direct fit, widen to specialist centers and other research universities. Preserve the reason for widening. No institution is automatically authoritative outside its actual discipline.

## 5. Source inspection and claim ledger

Create source register, claim ledger and inspection ledger. For each source:
- inspect title page, edition, author/editor, publication details and table of contents;
- inspect the specific passages relevant to the problem;
- record original language and translation where applicable;
- record the exact location and source identifier;
- distinguish quotation from paraphrase and later commentary;
- check whether the source cites an earlier authority;
- identify parallel passages and contradictions;
- record what has not been inspected.

For historical Chinese sources, add witness/edition identifiers and variant readings when available. Preserve source wording separately from the agent's gloss. Do not normalize away meaningful variants.

## 6. Skill and tool search

Search for existing tools by method, not only by the desired outcome:
- GitHub repositories and source code;
- existing agent skills and skill registries;
- academic digital-humanities projects;
- language corpora and dictionaries;
- research software, standards and workflow tools;
- professional association methods and public datasets.

For each candidate, test fit against: inputs, output, method fidelity, provenance, uncertainty handling, reproducibility, dependencies, maintenance, license and runtime. Search should include both a direct tool and methods/resources that could be adapted.

### Select skill builder only after this review
- Book Skills Creator for source-grounded modular packs with explicit planning, evidence mapping, conflict tracking and validation.
- Book-to-Skill for multi-format ingestion, chapter-aware extraction and on-demand source references.
- Meta Skill Creator / skill-architect for individual skill design, evaluation strategy and maintainability.
- Domain-specific tools for actual collation, corpus annotation, semantic analysis, knowledge graphs, statistical work or calculation verification.

Do not treat Book-to-Skill as an expert in textual criticism. It is an ingestion/conversion mechanism unless an independently verified component provides the scholarly method.

## 7. Build a capability plan

For each proposed skill document:
- one concrete operation or decision;
- trigger conditions and non-trigger conditions;
- input schema and prerequisites;
- exact procedure and decision rules;
- exception handling;
- outputs and evidence pointers;
- limits and uncertainty representation;
- dependencies and skill boundaries;
- positive, negative, ambiguous and unsupported tests.

Classify source-supported knowledge as:
- operational procedure;
- doctrinal/reference content;
- terminology/reference;
- source criticism procedure;
- annotation/data model;
- calculation/verification routine;
- empirical research protocol;
- unresolved candidate / rejected candidate.

Do not convert every chapter into a skill or every paragraph into a rule.

## 8. Build and validate

For Book Skills Creator, preserve the repository's current inspect → extract → plan → review draft → build → validate → semantic behavior test → install procedure. Verify the installed version's CLI and schema before commands. Keep plan status draft until the architecture and evidence map are reviewed.

For Book-to-Skill, inspect conversion mode, extraction quality and chapter segmentation. Verify that the generated material retains source references and does not silently flatten conflicting editions.

For all tools:
- keep private sources local unless sharing is authorized;
- preserve license constraints;
- verify generated files and routing metadata;
- run positive/negative/edge tests;
- independently review domain semantics and claims.

## 9. Apply and verify

Use the new/reused skills against the original task. Compare output with original source passages or raw data. For symbolic or traditional systems, separate:
1. exact text extraction;
2. textual interpretation;
3. doctrinal rule selection;
4. operational application;
5. deterministic calculation;
6. empirical outcome validation.

Do not use correctness at one level as proof of correctness at another.

## 10. Report

Return the concrete problem description, domain dossier, selected thesis, method/expert map, source register, existing tool/skill search, build decision, skill pack and tests, actual solution, confidence by claim class, unresolved conflicts and next evidence needed.
