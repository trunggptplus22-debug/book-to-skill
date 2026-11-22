# Domain Characterization Before Thesis Formation

## Purpose

This stage prevents a general-purpose problem-solving agent from prematurely translating an unfamiliar subject into generic research language. Before drafting a thesis, the agent must describe the domain as it actually exists: what its objects are, how practitioners use it, how knowledge is transmitted, what data exists, how reliable those data are, what remains disputed, and what kinds of claims can realistically be checked.

The initial output is a **domain dossier**, not a thesis. A thesis is written only after the dossier reveals which questions are answerable, what evidence could support them, and which research designs are feasible.

## Required characterization dimensions

For every new domain, inspect the following dimensions and fill them with concrete observations. Do not treat this list as a substitute for domain-specific analysis; derive additional dimensions from the subject itself.

1. **Object ontology:** What are the real objects practitioners manipulate or discuss? Distinguish observed entities, calculated entities, symbolic constructs, classifications, textual categories, and modern analytical abstractions.
2. **Vocabulary and semantics:** Which terms are technical? Which have multiple meanings across authors, periods, schools or contexts? Which words are metaphorical, compressed, borrowed, obsolete or used differently by modern interpreters?
3. **Source ecology:** What source types exist (primary text, received edition, manuscript, commentary, oral teaching, modern textbook, case record, software implementation, internet post)? Who produced each, when, for whom and for what purpose?
4. **Transmission history:** Are there variant editions, missing passages, interpolations, editorial reconstruction, paraphrase chains, translations, OCR corruption or unattributed quotations?
5. **Knowledge form:** Is the material declarative, procedural, interpretive, numerical, diagrammatic, oral, tacit, case-based, normative or polemical? One source can mix several forms.
6. **Rule explicitness:** Are rules stated completely, implied through examples, encoded in mnemonic formulae, dependent on omitted prerequisites, or recoverable only from practice?
7. **Evidence quality:** What supports each claim: direct observation, documented case, measurement, experiment, historical artifact, philological argument, expert testimony, repeated anecdote, lineage assertion or unsupported internet claim?
8. **Operational reproducibility:** Can two trained analysts apply the same rule to the same input and obtain the same output? Identify discretionary judgement, hidden conventions, parameter ambiguity and inter-school variation.
9. **Validation availability:** Can claims be checked against independent outcomes, archival evidence, controlled comparisons, established standards, reproducible calculations or only internal consistency?
10. **Contradiction structure:** Do sources disagree because of different definitions, schools, editions, historical layers, use cases, assumptions, or actual incompatible claims?
11. **Data availability and bias:** What cases exist, how were they selected, are negative cases available, are outcomes recorded prospectively, and is there survivorship/publication/selection bias?
12. **Boundary and applicability:** Where does the method claim to apply? What input conditions, populations, periods, contexts or exceptions invalidate transfer?
13. **Ethical and social context:** Could outputs affect health, finances, legal outcomes, identity, reputation or consequential life decisions? What safeguards and claim calibration are required?
14. **Technical affordances:** Which parts should be encoded as controlled vocabularies, tables, formulas, ontologies, rule engines, knowledge graphs, probabilistic models, annotation tools or human-review workflows?

For each dimension, record: concrete observation; supporting sources; uncertainty; consequences for analysis; and the specialist method required to investigate it.

## Mandatory distinction between description and endorsement

Characterizing a system does not validate its truth claims. For a traditional or symbolic system, the agent must distinguish at least:
- historical claim: what a text or lineage says;
- textual claim: what a particular edition actually contains;
- doctrinal claim: what a school teaches;
- operational claim: how a practitioner applies the rule;
- empirical claim: what observable outcomes support;
- computational claim: what an implementation calculates;
- interpretive claim: what an analyst infers in a case.

Never allow evidence for one category to be presented as evidence for another. A text may prove that a doctrine was recorded in an edition; it does not by itself prove that the doctrine predicts real-world outcomes.

## Illustrative characterization: classical Chinese fate-analysis material

The following is a domain-specific hypothesis map to guide inspection, not a claim that every Bát Tự, Tử Vi or other mệnh lý corpus has all these defects.

A corpus of Bát Tự / Tử Vi / traditional fate-analysis material may contain:
- classical Chinese prose, later commentaries, modern Vietnamese translations and teaching notes interleaved;
- terms whose meanings vary between schools, books and historical periods;
- compressed khẩu quyết (mnemonic formulae) omitting preconditions, exceptions or intermediate inference steps;
- rules described by example rather than formal procedure;
- parallel passages that are similar but not textually identical;
- attributions to famous authors or classics that may not be verified against an edition;
- modern claims repeated across websites without a traceable primary citation;
- interpretive case examples selected because they appear successful, with few systematically documented failures;
- retrospective fitting of events to symbolic configurations;
- unresolved disagreement between schools presented as if there were one universal rule;
- hidden dependencies on chart construction, calendrical conversion, house/star mapping or other calculation conventions;
- prose that shifts between metaphorical image, categorical rule, causal explanation and prediction without marking the transition.

The agent must verify which of these are actually present in the selected corpus. It must not assume them merely because the subject is mệnh lý.

## Research methods implied by this domain

Depending on observed problems, expert discovery may need to include:
- sinology / classical Chinese philology for language, genre, historical semantics and textual interpretation;
- textual criticism / collation / bibliographic studies for editions, variants, transmission and attribution;
- intellectual history / history of science / history of divination for changing conceptual systems and social context;
- corpus linguistics / digital humanities / Chinese NLP for corpus preparation, segmentation, annotation and terminology tracking;
- knowledge representation / ontology engineering for controlled concepts, relations, provenance and versioned definitions;
- knowledge graph engineering for source-to-claim-to-rule-to-case traceability;
- epistemology and philosophy of science for claim types, testability, falsification and evidential limits;
- statistics / causal inference / research design for case selection, outcome definition, baseline comparison and retrospective bias;
- software verification / rule-engine engineering for determinism, test coverage, rule conflicts and calculation validation;
- domain practitioners from the relevant school for tacit procedural knowledge and operational interpretation.

Do not automatically choose every discipline. Map each observed defect to the specialist method that can actually investigate it.

## When the thesis may be drafted

Only after the domain dossier identifies:
- the specific object or corpus under study;
- the type of problem (textual, semantic, doctrinal, operational, computational, empirical or mixed);
- the source/data that can be inspected;
- the claim class being investigated;
- the feasible method of inquiry;
- what can and cannot be concluded.

If empirical outcome data do not exist, do not manufacture an empirical thesis. A valid thesis may instead concern source attribution, doctrinal comparison, rule formalization, calculation reproducibility, corpus completeness or the feasibility of a validation study.

## Required output

Create `00-domain-characterization.md` with:
1. Domain and subdomain boundaries.
2. Concrete object inventory and terminology map.
3. Source ecology and transmission observations.
4. Data quality / evidence quality assessment.
5. Rule explicitness and reproducibility assessment.
6. Contradiction and school-variation map.
7. Validation availability and limits.
8. Risks of overclaiming.
9. Specialist methods required, each tied to an observed issue.
10. Candidate researchable problems, ranked by tractability and significance.
11. What must be inspected next.
12. Explicit unknowns that must not be filled by inference.
