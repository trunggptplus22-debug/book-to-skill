# Master Plan — Domain-Characterization-First Problem Solver

## 1. Objective

Create an agent that can enter a poorly specified or unfamiliar field and describe it accurately enough to discover the actual research problem, relevant methods, experts, source materials and missing capabilities. It must not flatten all problems into a generic thesis template.

The system begins with **detailed empirical/operational observation and domain characterization**. The thesis is a later artifact, produced only when the ontology, terminology, source ecology, evidence conditions and validation possibilities are sufficiently understood.

## 2. Why the previous generic sequence is insufficient

A problem such as "make an AI understand Bát Tự" is not yet a research thesis. It conceals several distinct problems:
- classical passages may have incomplete or uncertain provenance;
- quoted rules may lack verified edition/page references;
- one term may have different meanings across schools, periods and authors;
- a mnemonic sentence may omit the prerequisites and intermediate reasoning needed to apply it;
- a rule may be interpretive rather than algorithmic;
- commentaries may disagree with the base text or with each other;
- modern internet explanations may paraphrase one another without independent source chains;
- case collections may contain only successful retrospective examples;
- chart inputs may depend on hidden calendrical or calculation conventions;
- a software implementation may faithfully encode one school's interpretation without validating the interpretation itself.

These are distinct technical and scholarly problems. Each requires different evidence and expertise. A generic "find an expert and textbook" process will often choose the wrong specialist and build an unjustified skill.

The agent must first discover which of these, if any, are present in the corpus. Do not presume the diagnosis from the domain label.

## 3. Operating principles

1. Concrete observations before abstract labels.
2. Domain characterization before thesis.
3. Describe the domain in its native terminology and operating context.
4. Diagnose actual data defects instead of applying generic data-quality checklists mechanically.
5. Keep text history, doctrine, operational practice, computation and empirical outcomes separate.
6. Match each observed problem to a specialist method before identifying a person.
7. Practitioner-first for tacit and operational knowledge; academic specialists for philology, historiography, statistics and formal methods.
8. Ivy League is a fallback search lane, not a proxy for relevance or quality.
9. Search existing skills and tools by method before creating new ones.
10. Convert source-supported capabilities, not chapters or broad topics, into skills.
11. Preserve disagreements, variant readings, uncertainty and negative evidence.
12. Test skill behavior and the solution separately.
13. Never represent source authority as empirical truth.
14. Never claim a method was executed when only a plan or extracted summary exists.

## 4. System architecture

### 4.1 Problem Observer
Collects concrete events, examples, artifacts, workflow observations, failures, boundary cases and consequences. Uses native domain language, not premature abstraction.

### 4.2 Domain Characterizer
Builds an object inventory, terminology map, source ecology, knowledge-form classification, rule-explicitness assessment, data/evidence-quality profile, contradiction map and validation-capability assessment.

### 4.3 Source Critic
Inspects textual provenance, edition history, attribution, translations, commentaries, quotations, transcription/OCR quality, source dependencies and variant readings. Only invoke the philological/textual-criticism methods when the corpus warrants them.

### 4.4 Research Designer
Chooses the correct thesis family: textual, semantic, doctrinal, operational, computational, empirical, methodological or engineering. It must not force predictive or quantitative validation when such evidence is absent.

### 4.5 Method-to-Expert Mapper
Maps observed defects and research questions to specific specialist methods and then to exact practitioner/academic profiles.

### 4.6 Authority & Curriculum Researcher
Finds practitioners and verifies their actual work. When academic expertise is needed, traces official university programs, courses, instructors, syllabi, textbooks, authors and relevant chapters.

### 4.7 Skill/Tool Scout
Searches GitHub, existing skill libraries, professional repositories, research software and agent skill registries for tools that perform the required specialist methods. Produces a feature-fit comparison rather than recommending by name alone.

### 4.8 Source Analyst
Creates source register, claim ledger, evidence map, contradiction register and inspection ledger.

### 4.9 Skill Architect / Builder
Chooses between reusing, adapting or creating. Generates minimal but complete atomic skills, combo workflows, router and references. Maintains explicit traceability from operational instruction back to inspected evidence.

### 4.10 Evaluator
Tests extraction fidelity, source grounding, semantic behavior, reproducibility, calculations and original-problem acceptance criteria independently.

### 4.11 Integrator / Independent Reviewer
Applies the capabilities to the user's original problem, checks interdependencies, attempts to falsify findings and produces the final solution with calibrated claims.

## 5. Workflow and stage gates

| Gate | Required work | Artifact | Pass condition |
|---|---|---|---|
| G0 | Observe the concrete situation | `00-problem-observation.md` | Actual objects, failures, examples and consequences recorded |
| G1 | Characterize the domain | `00-domain-characterization.md` | Source ecology, terminology, knowledge form, evidence and validation limits understood sufficiently |
| G2 | Select researchable question | `01-research-design.md` | Thesis family and feasible inquiry method justified |
| G3 | Decompose specialist methods | `02-method-expertise-map.md` | Each observed issue maps to a specific method and deliverable |
| G4 | Identify authorities | `03-authority-dossiers/` | Practitioner search or academic fallback evidenced |
| G5 | Acquire and inspect sources | `04-source-register.csv`, claim ledger | Editions/authors/sections verified; gaps visible |
| G6 | Scout existing tools/skills | `05-tool-skill-fit.md` | Existing options tested/compared; create-versus-reuse decision reasoned |
| G7 | Plan skill architecture | `06-capability-plan.json` | Nonredundant atomic/combo/router/reference architecture linked to evidence |
| G8 | Build and validate skills | `07-skill-pack/`, `08-validation-report.md` | Structural and semantic tests completed |
| G9 | Apply to original problem | `09-solution-analysis.md` | Methods applied; criteria assessed |
| G10 | Independent review | `10-independent-review.md` | Counterevidence, uncertainty and weakest evidence chain reviewed |
| G11 | Delivery | `11-final-report.md` | Answer addresses the initial concrete problem, not merely the research process |

A failed gate returns to the earliest stage that can resolve it. Work packages may proceed in parallel only after G1 has supplied a stable domain map and dependencies are explicit.

## 6. Domain characterization specification

Before thesis writing, characterize:

- **Ontology:** objects, events, symbolic constructs, calculated variables, records, procedures and actors.
- **Vocabulary:** native terms, definitions by author/school/period, polysemy, metaphors and translation choices.
- **Source ecology:** primary texts, editions, manuscripts, commentaries, textbooks, oral teachings, cases, websites, datasets and software.
- **Transmission:** interpolation, variant readings, citation chains, attribution issues, translation, paraphrase and OCR errors.
- **Knowledge form:** declarative, procedural, tacit, interpretive, numerical, diagrammatic, case-based or normative.
- **Rule completeness:** explicit prerequisites, omitted steps, exceptions, mnemonic compression and hidden dependencies.
- **Evidence type:** textual, historical, observational, experimental, computational, testimonial, anecdotal or absent.
- **Reproducibility:** inter-annotator agreement, independent application, operational ambiguity and deterministic behavior.
- **Validation ceiling:** highest claim class supportable by available evidence.
- **Contradictions:** school, version, period, definition, context or real incompatibility.
- **Data quality:** missingness, source dependence, selection bias, survivorship, retrospective fitting and lack of negative cases.
- **Technical requirements:** cataloging, collation, annotation, ontology, graph, rule engine, calculation engine, statistical design and auditability.

The output must tie every diagnosed defect to evidence and a method. A generic checklist with empty boxes is not a diagnosis.

## 7. Example: Bát Tự / Tử Vi / traditional mệnh lý corpus

This example demonstrates the expected depth. It is a set of issues to investigate, not a presumption that every source has every defect.

### 7.1 Corpus composition

A real working corpus may include classical Chinese source works, modern annotated editions, Vietnamese translations, teacher notes, oral explanations, internet articles, case books, chart screenshots, manually calculated charts, software outputs and modern synthesis. These materials are not equivalent. The system must preserve author, edition, language, translation, school, date, source location and provenance chain for each item.

### 7.2 Semantic problems

A concept such as `用神` (Dụng thần), `格局` (Cách cục), `旺衰` (Vượng suy), `化氣` (Hóa khí) or `四化` (Tứ Hóa) may have definitions that differ by source, school and methodology. Record the exact wording, local context, source-specific reading and operational consequences. Do not merge terms into one canonical definition until the evidence demonstrates equivalence.

### 7.3 Textual problems

A passage may be quoted without its exact chapter/page; attribution may be conventional rather than independently authenticated; a modern translation may silently interpret ambiguous Classical Chinese; commentarial material may be mixed into the base text; two editions may contain different wording. These require bibliographic work, textual criticism, collation, classical Chinese philology and translation review, not merely LLM summarization.

### 7.4 Rule-formalization problems

A khẩu quyết may compress several conditions into a short statement. The omitted components may include required chart state, priority order, exceptions, timing, school-specific convention or a dependency on another rule. Formalization must preserve the original statement, enumerate interpretations, mark missing preconditions, and obtain practitioner review before treating the result as an executable rule.

### 7.5 Case/evidence problems

A retrospective reading may select memorable matches, reinterpret ambiguous events, omit unsuccessful cases or use vague event categories. The corpus may lack birth-time verification, event dates, independent labels, control cases and pre-registered criteria. Therefore, doctrinal fidelity, interpretive consistency and empirical predictive performance must be measured separately. A large quantity of anecdotes does not automatically create a valid dataset.

### 7.6 Computation problems

A doctrinal conclusion can be contaminated by incorrect calendar conversion, time zone, solar-term boundary, stem-branch derivation, house placement, star mapping, transformation mapping or rounding convention. Separate input-data verification, astronomical/calendar calculations, symbolic-rule execution and final interpretation. Unit tests and parity tests can establish computational consistency, not doctrinal truth.

### 7.7 Potential research packages

- bibliographic and edition provenance;
- Classical Chinese terminology and semantic variation;
- passage alignment and textual collation;
- doctrinal comparison by school and author;
- extraction of implicit procedures and exception rules;
- knowledge ontology and claim-evidence graph;
- deterministic calculation verification;
- case schema and prospective validation methodology;
- inter-annotator consistency and disagreement analysis.

Do not instantiate all packages automatically. Select those supported by the actual objective and corpus audit.

## 8. Method → expert → source → skill matching

| Observed issue | Candidate method | Expert profile to find | Source types to locate | Potential skill |
|---|---|---|---|---|
| Classical text attribution unclear | Textual history, bibliographic criticism, authentication studies | Sinologist / bibliographer / textual critic | Catalogs, editions, bibliographies, authentication studies | Classical Text Provenance |
| Variant passages | Collation, manuscript/edition comparison | Philologist / textual critic | Scans, witnesses, critical editions | Text Variant Collation |
| Ambiguous Classical Chinese expression | Philology, historical semantics, translation criticism | Classical Chinese scholar / translator | Dictionaries, commentaries, parallel usage | Classical Chinese Semantic Analysis |
| Different school definitions | Comparative intellectual history / doctrinal analysis | Historian of ideas + practitioners of each school | Primary manuals, school-specific commentaries, teaching texts | School-Specific Doctrine Comparison |
| Implicit mnemonic rule | Knowledge elicitation, protocol analysis, formal specification | Domain practitioner + knowledge engineer | Demonstrations, cases, manuals, interviews | Tacit Rule Elicitation |
| Text facts not traceable to source | Information provenance, claim extraction | Information scientist / knowledge engineer | Citation graph, source corpus | Claim-Evidence Provenance |
| Narrative case records vague | Qualitative coding / data schema design | Qualitative methodologist + domain researcher | Case records, interview protocols | Case Record Structuring |
| No predictive validation | Study design, measurement, statistics, causal inference as appropriate | Statistician / research methodologist | Prospective data, protocols, outcome labels | Predictive Claim Validation Design |
| Calculation disagreement | Formal methods, numerical verification, software testing | Computational scientist / verification engineer | Algorithms, ephemerides, test vectors | Deterministic Calculation Audit |
| Rules depend on each other | Ontology, knowledge graph, rule engine design | Ontologist / knowledge graph engineer | Taxonomies, rule bases, schemas | Mệnh Lý Knowledge Graph |

This table is a discovery map, not a final expert list. The agent must locate actual people and sources for each selected work package.

## 9. Skill/tool discovery requirements

Search more than repositories named "skill creator". Search for actual method implementations and reference frameworks. Required search lanes may include:
- textual criticism, manuscript collation, critical apparatus and bibliographic databases;
- Chinese Classical language corpora, dictionaries, segmentation and annotation;
- digital humanities and corpus annotation workflows;
- document parsing, OCR quality review, citation extraction and entity linking;
- knowledge graph / ontology engineering and provenance tracking;
- qualitative coding and data annotation;
- statistical design, preregistration and validation;
- rule engines, formal specification, property-based tests and calculation audit;
- agent-skill creation, evaluation, routing and lifecycle management.

Evaluate the tool's real ability against the observed task. A search result, repository name, star count or README claim is not proof it performs the needed method.

## 10. Skill creator selection

- Book Skills Creator: modular source-grounded skill pack architecture, candidate tracking, evidence IDs, routes, conflict register, validation. Best for corpus-to-capability design.
- Book-to-Skill: multi-format document ingestion and chapter-oriented knowledge references. Best as ingestion / extraction support. It does not by itself authenticate ancient texts or validate domain truth claims.
- Meta Skill Creator / skill architect: design and refine SKILL.md, activation metadata, progressive disclosure and evaluation. Best for skill authoring quality.
- Domain-specific research tools: use where they implement actual philological, annotation, knowledge graph, statistics or verification techniques.

A proper toolchain may combine these components. Do not assume one repository is sufficient.

## 11. Runtime artifacts

```text
problem-work/<problem-id>/
├── 00-problem-observation.md
├── 00-domain-characterization.md
├── 01-research-design.md
├── 02-method-expertise-map.md
├── 03-authority-dossiers/
├── 04-source-register.csv
├── 04-claim-ledger.jsonl
├── 04-text-variant-register.csv
├── 04-inspection-ledger.md
├── 05-tool-skill-fit.md
├── 06-capability-plan.json
├── 07-skill-pack/
├── 08-validation-report.md
├── 09-solution-analysis.md
├── 10-independent-review.md
└── 11-final-report.md
```

Do not create irrelevant artifacts when the domain does not require them. Keep source material and copyrighted books outside public skill repositories.

## 12. Definition of done

- actual situation described in domain-native detail;
- domain characterized using inspectable evidence;
- thesis family chosen for the actual evidence conditions;
- methods mapped to concrete specialists;
- authorities and sources individually verified;
- existing skills/tools searched by method;
- create-versus-reuse decision documented;
- resulting skills have provenance, limits and behavioral tests;
- solution applied and checked against the original practical objective;
- independent review performed;
- empirical claims calibrated to the actual validation available.

A generic thesis, a list of famous experts, a converted textbook or a passing structural validator is not sufficient.
