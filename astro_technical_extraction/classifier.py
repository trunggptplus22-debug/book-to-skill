"""Explainable first-pass technical relevance classifier.

This classifier is a deterministic triage layer, not a doctrinal authority.
It combines structural cues and phrase patterns; keyword presence alone never
causes automatic inclusion. Ambiguous blocks are sent to REVIEW.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
from enum import Enum
import re
from typing import Iterable

from .document_ir import BlockType, DocumentBlock


class RelevanceClass(str, Enum):
    TECHNICAL_CORE = "TECHNICAL_CORE"
    TECHNICAL_CONTEXT = "TECHNICAL_CONTEXT"
    EXAMPLE_CASE = "EXAMPLE_CASE"
    HISTORICAL_CONTEXT = "HISTORICAL_CONTEXT"
    PHILOSOPHICAL_CONTEXT = "PHILOSOPHICAL_CONTEXT"
    BIOGRAPHICAL = "BIOGRAPHICAL"
    GENERAL_COMMENTARY = "GENERAL_COMMENTARY"
    UNCERTAIN = "UNCERTAIN"


class Disposition(str, Enum):
    INCLUDE = "INCLUDE"
    CONTEXT_ONLY = "CONTEXT_ONLY"
    EXCLUDE = "EXCLUDE"
    REVIEW = "REVIEW"
    UNREADABLE = "UNREADABLE"


@dataclass(frozen=True)
class Classification:
    block_id: str | None
    relevance_class: RelevanceClass
    disposition: Disposition
    reason: str
    confidence: float
    evidence: tuple[str, ...] = ()
    classifier_version: str = "rule-based-0.1"

    def to_dict(self) -> dict:
        result = asdict(self)
        result["relevance_class"] = self.relevance_class.value
        result["disposition"] = self.disposition.value
        return result


class RuleBasedClassifier:
    """Small conservative classifier suitable for human-in-the-loop review."""

    _EXAMPLE = re.compile(
        r"\b(worked example|example chart|nativit\w+|horary chart|case study|"
        r"for example|in this figure|the nativity)\b", re.I
    )
    _PROCEDURE = re.compile(
        r"\b(if|when|unless|provided that|calculate|computed|subtract|add|"
        r"divide|multiply|measure|convert|determine|select|judge|consider|"
        r"apply|apply(?:ing)?|procedure|method|rule|steps?)\b", re.I
    )
    _TECHNICAL_NOUNS = re.compile(
        r"\b(ascendant|midheaven|house cusp|house system|domicile|exaltation|"
        r"triplicity|terms|bounds|face|decan|sect|reception|dispositor|"
        r"profection|primary direction|solar return|lunar return|ephemeris|"
        r"right ascension|declination|obliquity|longitude|latitude|orb|"
        r"combust|cazimi|retrograde|fixed star|lot of fortune|significator|"
        r"applying aspect|separating aspect|dignity|essential dignity|"
        r"accidental dignity)\b", re.I
    )
    _FORMULA = re.compile(r"(=|≤|≥|\b(arctan|sin|cos|tan|sqrt)\b|\b\w+\s*\*\s*\w+)")
    _TABLE_CUES = re.compile(r"\b(table|column|row|degrees?\s+of|terms?\s+of)\b", re.I)
    _HISTORY = re.compile(
        r"\b(was born|born in|died in|century|historian|historical|"
        r"manuscript tradition|published in|edition of)\b", re.I
    )
    _BIO = re.compile(r"\b(he was born|she was born|his life|her life|biography)\b", re.I)
    _PHILOSOPHY = re.compile(r"\b(universe|cosmos|divine|soul|metaphysical|"
                             r"spiritual nature|cosmic order)\b", re.I)
    _COMMENTARY = re.compile(r"\b(in my opinion|it is interesting|generally speaking|"
                             r"as mentioned above|needless to say)\b", re.I)

    def classify(self, block: DocumentBlock) -> Classification:
        text = block.raw_text.strip()
        block_id = block.locator.block_id

        if not text or block.block_type == BlockType.UNKNOWN and not text:
            return Classification(
                block_id, RelevanceClass.UNCERTAIN, Disposition.UNREADABLE,
                "Empty or unreadable source block.", 1.0
            )

        if self._BIO.search(text):
            return Classification(block_id, RelevanceClass.BIOGRAPHICAL,
                                  Disposition.EXCLUDE, "Biographical pattern detected.",
                                  0.91, ("biographical_phrase",))

        if self._EXAMPLE.search(text):
            return Classification(block_id, RelevanceClass.EXAMPLE_CASE,
                                  Disposition.INCLUDE, "Worked-example cue detected; keep separate from general rules.",
                                  0.78, ("worked_example_phrase",))

        technical_hits = self._TECHNICAL_NOUNS.findall(text)
        procedure_hits = self._PROCEDURE.findall(text)
        formula_hit = bool(self._FORMULA.search(text))
        table_hit = block.block_type == BlockType.TABLE or bool(self._TABLE_CUES.search(text))
        structural_hit = block.block_type in {BlockType.EQUATION, BlockType.TABLE, BlockType.CODE}

        # A technical term by itself is insufficient. Require a procedural,
        # mathematical, table-structural, or source-defined technical statement.
        if technical_hits and (procedure_hits or formula_hit or structural_hit):
            evidence = tuple(sorted(set(
                (["technical_term"] if technical_hits else [])
                + (["procedural_language"] if procedure_hits else [])
                + (["formula_syntax"] if formula_hit else [])
                + (["technical_structure"] if structural_hit else [])
            )))
            return Classification(block_id, RelevanceClass.TECHNICAL_CORE,
                                  Disposition.INCLUDE,
                                  "Technical terminology co-occurs with an operational or structured cue.",
                                  0.84, evidence)

        if table_hit and technical_hits:
            return Classification(block_id, RelevanceClass.TECHNICAL_CORE,
                                  Disposition.INCLUDE, "Astrological table structure detected.",
                                  0.82, ("technical_term", "table_structure"))

        if technical_hits:
            return Classification(block_id, RelevanceClass.TECHNICAL_CONTEXT,
                                  Disposition.CONTEXT_ONLY,
                                  "Technical terminology found without sufficient operational evidence.",
                                  0.68, ("technical_term_only",))

        if self._HISTORY.search(text):
            return Classification(block_id, RelevanceClass.HISTORICAL_CONTEXT,
                                  Disposition.CONTEXT_ONLY,
                                  "Historical/provenance cue detected.", 0.85,
                                  ("historical_phrase",))

        if self._PHILOSOPHY.search(text):
            return Classification(block_id, RelevanceClass.PHILOSOPHICAL_CONTEXT,
                                  Disposition.EXCLUDE,
                                  "Philosophical cue without a detected technical operation.",
                                  0.72, ("philosophical_phrase",))

        if self._COMMENTARY.search(text):
            return Classification(block_id, RelevanceClass.GENERAL_COMMENTARY,
                                  Disposition.EXCLUDE,
                                  "General commentary cue detected.", 0.72,
                                  ("commentary_phrase",))

        if block.block_type == BlockType.HEADING:
            return Classification(block_id, RelevanceClass.UNCERTAIN,
                                  Disposition.REVIEW,
                                  "Heading requires section-level context.", 0.55,
                                  ("heading_context_required",))

        return Classification(block_id, RelevanceClass.UNCERTAIN,
                              Disposition.REVIEW,
                              "No reliable deterministic evidence; do not infer exclusion.",
                              0.40, ("insufficient_evidence",))

    def classify_many(self, blocks: Iterable[DocumentBlock]) -> list[Classification]:
        return [self.classify(block) for block in blocks]
