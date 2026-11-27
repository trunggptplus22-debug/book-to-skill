"""Explainable conservative technical relevance triage."""
from __future__ import annotations
from dataclasses import asdict,dataclass
from enum import Enum
import re
from typing import Iterable
from .document_ir import BlockType,DocumentBlock

class RelevanceClass(str,Enum):
    TECHNICAL_CORE="TECHNICAL_CORE"; TECHNICAL_CONTEXT="TECHNICAL_CONTEXT"
    EXAMPLE_CASE="EXAMPLE_CASE"; HISTORICAL_CONTEXT="HISTORICAL_CONTEXT"
    PHILOSOPHICAL_CONTEXT="PHILOSOPHICAL_CONTEXT"; BIOGRAPHICAL="BIOGRAPHICAL"
    GENERAL_COMMENTARY="GENERAL_COMMENTARY"; UNCERTAIN="UNCERTAIN"
class Disposition(str,Enum):
    INCLUDE="INCLUDE"; CONTEXT_ONLY="CONTEXT_ONLY"; EXCLUDE="EXCLUDE"
    REVIEW="REVIEW"; UNREADABLE="UNREADABLE"

@dataclass(frozen=True)
class Classification:
    block_id: str|None
    relevance_class: RelevanceClass
    disposition: Disposition
    reason: str
    confidence: float
    evidence: tuple[str,...]=()
    classifier_version: str="rule-based-0.1"
    def to_dict(self):
        d=asdict(self); d["relevance_class"]=self.relevance_class.value
        d["disposition"]=self.disposition.value; return d

class RuleBasedClassifier:
    """Triage only: keywords alone cannot automatically include a block."""
    TECH=re.compile(r"\b(ascendant|midheaven|house cusp|house system|domicile|exaltation|triplicity|terms|bounds|face|decan|sect|reception|dispositor|profection|primary direction|solar return|lunar return|ephemeris|right ascension|declination|obliquity|longitude|latitude|orb|combust|cazimi|retrograde|fixed star|lot of fortune|significator|applying aspect|separating aspect|dignity|essential dignity|accidental dignity)\b",re.I)
    PROCEDURE=re.compile(r"\b(if|when|unless|provided that|calculate|computed|subtract|add|divide|multiply|measure|convert|determine|select|judge|consider|apply|procedure|method|rule|steps?)\b",re.I)
    EXAMPLE=re.compile(r"\b(worked example|example chart|nativit\w+|horary chart|case study|for example|in this figure)\b",re.I)
    HISTORY=re.compile(r"\b(was born|born in|died in|century|historian|historical|manuscript tradition|published in|edition of)\b",re.I)
    BIO=re.compile(r"\b(he was born|she was born|his life|her life|biography)\b",re.I)
    PHIL=re.compile(r"\b(universe|cosmos|divine|soul|metaphysical|spiritual nature|cosmic order)\b",re.I)
    COMMENT=re.compile(r"\b(in my opinion|it is interesting|generally speaking|as mentioned above|needless to say)\b",re.I)
    FORMULA=re.compile(r"(=|≤|≥|\b(arctan|sin|cos|tan|sqrt)\b|\b\w+\s*\*\s*\w+)")
    def classify(self,b:DocumentBlock)->Classification:
        t=b.raw_text.strip(); bid=b.locator.block_id
        if not t:
            return Classification(bid,RelevanceClass.UNCERTAIN,Disposition.UNREADABLE,"Empty source block.",1.0)
        if self.BIO.search(t):
            return Classification(bid,RelevanceClass.BIOGRAPHICAL,Disposition.EXCLUDE,"Biographical cue.",.91,("biographical_phrase",))
        if self.EXAMPLE.search(t):
            return Classification(bid,RelevanceClass.EXAMPLE_CASE,Disposition.INCLUDE,
                "Worked-example cue; keep distinct from general rules.",.78,("worked_example_phrase",))
        terms=self.TECH.findall(t); steps=self.PROCEDURE.findall(t)
        formula=bool(self.FORMULA.search(t))
        structure=b.block_type in {BlockType.TABLE,BlockType.EQUATION,BlockType.CODE}
        if terms and (steps or formula or structure):
            evidence=tuple(x for x,yes in (("technical_term",bool(terms)),("procedural_language",bool(steps)),("formula_syntax",formula),("structured_block",structure)) if yes)
            return Classification(bid,RelevanceClass.TECHNICAL_CORE,Disposition.INCLUDE,
                "Technical terminology co-occurs with an operational or structured cue.",.84,evidence)
        if terms:
            return Classification(bid,RelevanceClass.TECHNICAL_CONTEXT,Disposition.CONTEXT_ONLY,
                "Technical terminology without sufficient operational evidence.",.68,("technical_term_only",))
        if self.HISTORY.search(t):
            return Classification(bid,RelevanceClass.HISTORICAL_CONTEXT,Disposition.CONTEXT_ONLY,"Historical/provenance cue.",.85,("historical_phrase",))
        if self.PHIL.search(t):
            return Classification(bid,RelevanceClass.PHILOSOPHICAL_CONTEXT,Disposition.EXCLUDE,"Philosophical cue without detected technical operation.",.72,("philosophical_phrase",))
        if self.COMMENT.search(t):
            return Classification(bid,RelevanceClass.GENERAL_COMMENTARY,Disposition.EXCLUDE,"General commentary cue.",.72,("commentary_phrase",))
        if b.block_type==BlockType.HEADING:
            return Classification(bid,RelevanceClass.UNCERTAIN,Disposition.REVIEW,"Heading requires section context.",.55,("heading_context_required",))
        return Classification(bid,RelevanceClass.UNCERTAIN,Disposition.REVIEW,"No reliable deterministic evidence; retain for review.",.40,("insufficient_evidence",))
    def classify_many(self,blocks:Iterable[DocumentBlock])->list[Classification]:
        return [self.classify(b) for b in blocks]
