# Operational Workflow

This document is the execution runbook for one problem instance.

## 0. Create a problem workspace

Assign a stable problem ID. Create a workspace separate from the agent repository. Record user-provided source locations and the exact scope authorized for inspection. Do not assume access to adjacent folders, accounts or private systems.

## 1. Intake and thesis

Produce `00-problem-brief.md` and `01-thesis.json`.

Required thesis test:
- Is the object or system identified?
- Is the current problem observable?
- Is the mechanism, decision or intervention stated?
- Is the outcome measurable?
- Is the scope bounded?
- Is there a baseline or comparator?
- Is there a way to disconfirm the claim?
- Are constraints and failure costs stated?

If any critical item is missing, ask one blocking question or explicitly record a bounded assumption. Do not start expert search from an unbounded topic label.

## 2. Decompose expertise

Create `02-expertise-map.md` with one row per work package:

| WP | Thesis question | Required discipline | Practitioner role | Academic discipline | Method needed | Deliverable | Dependency |
|---|---|---|---|---|---|---|---|

Split work packages when the underlying methods or professional responsibilities differ. Identify integration points where one expert's output becomes another's input.

## 3. Search and verify authorities

For each work package:
1. Search for people who perform the exact professional function.
2. Search professional bodies, award/project records, portfolios, case studies, standards contributions and technical publications.
3. Verify candidate claims using primary sources and independent corroboration.
4. Record why the candidate is relevant to this thesis, not merely to the general field.
5. If practitioner search produces no credible candidate, document the search boundary and switch to academic fallback.
6. Search Ivy League official department and course pages.
7. Verify the course is genuinely relevant from its description and syllabus.
8. Verify instructor identity from the official faculty/course page.
9. Verify textbook title, edition, author/editor and publisher from syllabus, publisher or library catalog.
10. If the Ivy route yields no suitable source, expand to other research universities or professional institutions and state why.

Do not invent a ranking. Report candidate evidence and gaps. Use `templates/expert-dossier.md`.

## 4. Build the source register

For every source record:
- stable source ID;
- title;
- author/editor/institution;
- source type;
- edition/version/date;
- publisher/official URL/DOI where available;
- authority route (practitioner / academic / standard / primary research);
- thesis questions supported;
- chapters/pages inspected;
- access status;
- license/copyright constraints;
- extraction quality and gaps;
- contradictions and corroborating sources.

Inspect sources rather than relying on search snippets. For books, record which chapters were actually read and which remain uninspected.

## 5. Select the skill engineering route

Apply this decision logic:

- Need a multi-skill pack with explicit capability planning, provenance, conflict tracking, routing and validation → Book Skills Creator.
- Need broad multi-format book/document conversion or chapter-on-demand access, including configured MCP search → Book-to-Skill.
- Need to create or refine an individual SKILL.md and its activation metadata → Meta Skill Creator.
- Need both document conversion and modular pack architecture → Book-to-Skill may ingest/structure the corpus; feed the selected, authorized source set into Book Skills Creator for the canonical capability plan and pack.

Do not process the same source twice without a reason. Verify repository state, release, license and host compatibility before installation.

## 6. Build capability plan

Use `templates/skill-spec.md` to define each candidate capability. Categorize:
- Atomic: one reusable operation.
- Combo: a sequence of existing atomic/combo capabilities.
- Router: selects the smallest appropriate capability and handles ambiguity.
- Reference: concepts, definitions, evidence, taxonomies and examples not requiring a procedure.
- Rejected: weakly supported, redundant or non-operational candidates with reason.

For Book Skills Creator, preserve its canonical workflow:
```bash
python scripts/book_skills.py preflight
python scripts/book_skills.py inspect <explicit-source-paths> --json
python scripts/book_skills.py extract <explicit-source-paths> --output .book_skills_work --json
python scripts/book_skills.py plan .book_skills_work/sources.json <pack-name> --output .book_skills_work/plan.json
# Agent completes and reviews the draft plan; set status=ready only after architecture review.
python scripts/book_skills.py build .book_skills_work/plan.json --output ./<pack-directory>
python scripts/book_skills.py validate ./<pack-directory> --extraction .book_skills_work/sources.json --json
```
These commands are specific to Book Skills Creator. Confirm the checked-out version's CLI and schema before running. Never treat a draft plan as ready.

## 7. Quality review

Run:
- structural validator;
- evidence-to-instruction trace review;
- source conflict and extraction-gap review;
- duplicate capability review;
- trigger/route review;
- positive and negative routing cases;
- ambiguity and unsupported request cases;
- combo dependency tests;
- adversarial source-injection test;
- deterministic script unit tests;
- original-problem acceptance tests.

Record failures. A structural PASS does not imply factual or semantic correctness.

## 8. Apply to the problem

For each thesis question:
1. identify required skill(s);
2. read the relevant skill and referenced source sections;
3. list verified inputs;
4. execute method or procedure;
5. record outputs and intermediate evidence;
6. compare alternatives;
7. test assumptions and edge cases;
8. independently verify critical calculations or claims;
9. integrate work packages;
10. assess against thesis acceptance criteria.

## 9. Final review and handoff

The independent reviewer must attempt to falsify the main conclusion, inspect the weakest evidence link, and identify what new evidence would change the recommendation.

The final report must distinguish:
- verified facts;
- source-reported claims;
- agent inferences;
- hypotheses;
- test observations;
- unresolved uncertainties.

Do not report success if the required outcome was not measured or the acceptance criterion was not met.
