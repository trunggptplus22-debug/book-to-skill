"""Source-faithful technical record extraction helpers (heuristic, reviewable)."""
from __future__ import annotations
import re
from dataclasses import dataclass,asdict
from typing import Any
from .classifier import Classification,Disposition
from .document_ir import DocumentIR

@dataclass
class TechnicalRecord:
    record_id:str
    block_id:str
    source_id:str
    locator:dict[str,Any]
    record_type:str
    verbatim:str
    normalized:str|None
    confidence:float
    evidence:list[str]
    review_required:bool=True
    fields:dict[str,Any]|None=None

FORMULA=re.compile(r"(?:[=<>≤≥]|\b(?:sin|cos|tan|arctan|sqrt)\b|\b\w+\s*[*/]\s*\w+)",re.I)
TABLE_HINT=re.compile(r"\b(table|tabular|column|row|reference|orb|degree|terms|bounds|triplicity|dignit)",re.I)
RULE_HINT=re.compile(r"\b(if|when|unless|provided|must|should|select|calculate|apply|judge|consider|determine|condition|rule|procedure)\b",re.I)
def extract_records(document:DocumentIR, classifications:list[Classification])->list[TechnicalRecord]:
    byid={c.block_id:c for c in classifications}; out=[]
    for b in document.blocks:
        c=byid.get(b.locator.block_id)
        if not c or c.disposition not in (Disposition.INCLUDE,Disposition.CONTEXT_ONLY,Disposition.REVIEW): continue
        t=b.raw_text.strip()
        if not t: continue
        typ="RULE" if RULE_HINT.search(t) else "FORMULA" if FORMULA.search(t) else "TABLE_REFERENCE" if b.block_type.value=="TABLE" or TABLE_HINT.search(t) else "TECHNICAL_NOTE"
        fields={}
        if typ=="FORMULA": fields["formula_candidates"]=FORMULA.findall(t)
        if typ=="RULE": fields["rule_cue_candidates"]=RULE_HINT.findall(t)
        out.append(TechnicalRecord(f"{document.source_id}-R{len(out)+1:06d}",b.locator.block_id,document.source_id,asdict(b.locator),typ,t,None,c.confidence,list(c.evidence),True,fields or None))
    return out
