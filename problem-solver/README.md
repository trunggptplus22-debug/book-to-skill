# Thesis-Driven Problem Solver Agent

A reusable workflow for solving unfamiliar, domain-specific problems by first formalizing the problem as a research thesis, then identifying the right authorities, acquiring their methods, engineering verified skills, and applying those skills to the original problem.

## Core operating rule

**Problem → Thesis → Required expertise → Authority discovery → Textbook/source selection → Skill engineering → Execution → Verification.**

Do not begin by guessing which tool or skill is needed. Determine the problem's actual knowledge requirements first.

## Components

- [SKILL.md](SKILL.md): agent operating instructions and routing contract.
- [MASTER_PLAN.md](MASTER_PLAN.md): complete system design, roles, stages, gates, artifacts, and acceptance criteria.
- [WORKFLOW.md](WORKFLOW.md): detailed execution procedure and decision rules.
- [schemas/thesis.schema.json](schemas/thesis.schema.json): machine-readable thesis record.
- [templates/expert-dossier.md](templates/expert-dossier.md): expert and academic authority research record.
- [templates/skill-spec.md](templates/skill-spec.md): source-grounded skill specification.
- [evaluation/acceptance-tests.md](evaluation/acceptance-tests.md): end-to-end behavioral tests.

## Skill engineering toolchain

1. **Primary pack architect:** [Tire-C/book-skills-creator](https://github.com/Tire-C/book-skills-creator). Use its explicit-source, evidence-linked atomic/combo/router/reference architecture and deterministic validation.
2. **Document ingestion / alternative converter:** [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill). Use for supported local documents, multi-source ingestion, chapter-aware references, and remote MCP book search where configured.
3. **Skill quality layer:** [sentient-agi/meta-skill-creator](https://github.com/sentient-agi/meta-skill-creator). Use to review trigger descriptions, progressive disclosure, skill boundaries, and maintainability.

These are complementary tools, not interchangeable authorities. Verify each tool's current compatibility, release, dependencies, license, and host support before installation or execution.

## Quick start

Give the agent a concrete problem. It should return a thesis and an evidence-based expert/source plan before it creates any domain skill. Once source selection is authorized, it can build the skill pack, test it, and apply it to the original thesis.

No domain-specific expert, university, textbook, or solution is hard-coded here. Those are discovered anew for each thesis.
