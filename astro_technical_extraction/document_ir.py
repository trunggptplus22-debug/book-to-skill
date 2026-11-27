"""Typed, provenance-preserving intermediate representation."""
from __future__ import annotations
from dataclasses import asdict, dataclass, field
from enum import Enum
import hashlib, json
from typing import Any, Iterable, Optional

class BlockType(str, Enum):
    HEADING="HEADING"; PARAGRAPH="PARAGRAPH"; LIST="LIST"; TABLE="TABLE"
    EQUATION="EQUATION"; SYMBOL="SYMBOL"; FIGURE="FIGURE"; FOOTNOTE="FOOTNOTE"
    CODE="CODE"; UNKNOWN="UNKNOWN"

@dataclass(frozen=True)
class SourceLocator:
    source_id: str
    file_name: str
    printed_page: Optional[str]=None
    pdf_page_index: Optional[int]=None
    chapter_id: Optional[str]=None
    section_path: tuple[str,...]=()
    block_id: Optional[str]=None
    def __post_init__(self):
        if not self.source_id.strip(): raise ValueError("source_id must be non-empty")
        if self.pdf_page_index is not None and self.pdf_page_index < 0:
            raise ValueError("pdf_page_index must be zero-based and non-negative")

@dataclass(frozen=True)
class DocumentBlock:
    locator: SourceLocator
    block_type: BlockType
    raw_text: str
    sequence_index: int
    extraction_method: str="provided_text"
    extraction_confidence: Optional[float]=None
    warnings: tuple[str,...]=()
    payload: dict[str,Any]=field(default_factory=dict)
    def __post_init__(self):
        if self.sequence_index < 0: raise ValueError("sequence_index must be non-negative")
        if self.extraction_confidence is not None and not 0 <= self.extraction_confidence <= 1:
            raise ValueError("extraction_confidence must be between 0 and 1")

@dataclass
class DocumentIR:
    source_id: str
    blocks: list[DocumentBlock]
    metadata: dict[str,Any]=field(default_factory=dict)
    schema_version: str="1.0"
    def __post_init__(self):
        if not self.source_id.strip(): raise ValueError("source_id must be non-empty")
        if any(b.locator.source_id != self.source_id for b in self.blocks):
            raise ValueError("all blocks must belong to DocumentIR.source_id")
        ids=[b.locator.block_id for b in self.blocks if b.locator.block_id]
        if len(ids) != len(set(ids)): raise ValueError("block_id values must be unique")
    @property
    def content_sha256(self):
        canonical="\n".join(f"{b.sequence_index}:{b.block_type.value}:{b.raw_text}" for b in self.blocks)
        return hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    def to_dict(self):
        return {"schema_version":self.schema_version,"source_id":self.source_id,
                "content_sha256":self.content_sha256,"metadata":self.metadata,
                "blocks":[{**asdict(b),"block_type":b.block_type.value,
                           "locator":asdict(b.locator)} for b in self.blocks]}
    def to_jsonl(self):
        return "\n".join(json.dumps({**asdict(b),"block_type":b.block_type.value,
            "locator":asdict(b.locator)},ensure_ascii=False,sort_keys=True) for b in self.blocks)
    @classmethod
    def from_text(cls, source_id: str, file_name: str, text: str, *, chapter_id=None):
        """Conservative paragraph adapter; does not claim page/table fidelity."""
        blocks=[]
        for i,line in enumerate(p for p in text.splitlines() if p.strip()):
            value=line.strip()
            locator=SourceLocator(source_id,file_name,chapter_id=chapter_id,
                                  block_id=f"{source_id}-B{i+1:06d}")
            kind=BlockType.HEADING if value.startswith("#") or (len(value)<100 and value.isupper()) else BlockType.PARAGRAPH
            blocks.append(DocumentBlock(locator,kind,value,i,"plain_text_adapter",
                warnings=("layout_and_printed_page_not_preserved",)))
        return cls(source_id,blocks)

def blocks_from_records(source_id: str, file_name: str, records: Iterable[dict[str,Any]]) -> DocumentIR:
    """Adapt richer parser records while keeping page labels and indices distinct."""
    blocks=[]
    for i,r in enumerate(records):
        page=r.get("pdf_page_index",r.get("page_index"))
        locator=SourceLocator(source_id,file_name,r.get("printed_page"),
          page if isinstance(page,int) else None,r.get("chapter_id"),
          tuple(r.get("section_path",())),str(r.get("block_id") or f"{source_id}-B{i+1:06d}"))
        try: kind=BlockType(str(r.get("block_type","PARAGRAPH")).upper())
        except ValueError: kind=BlockType.UNKNOWN
        blocks.append(DocumentBlock(locator,kind,str(r.get("text",r.get("content",""))),i,
          str(r.get("extraction_method","existing_parser")),r.get("extraction_confidence"),
          tuple(r.get("warnings",())),{k:v for k,v in r.items() if k not in {
          "text","content","printed_page","pdf_page_index","page_index","chapter_id",
          "section_path","block_id","block_type","extraction_method","extraction_confidence","warnings"}}))
    return DocumentIR(source_id,blocks)
