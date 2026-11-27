"""Typed, provenance-preserving intermediate representation for source blocks."""
from __future__ import annotations

from dataclasses import asdict, dataclass, field
from enum import Enum
import hashlib
import json
from typing import Any, Iterable, Optional


class BlockType(str, Enum):
    HEADING = "HEADING"
    PARAGRAPH = "PARAGRAPH"
    LIST = "LIST"
    TABLE = "TABLE"
    EQUATION = "EQUATION"
    SYMBOL = "SYMBOL"
    FIGURE = "FIGURE"
    FOOTNOTE = "FOOTNOTE"
    CODE = "CODE"
    UNKNOWN = "UNKNOWN"


@dataclass(frozen=True)
class SourceLocator:
    source_id: str
    file_name: str
    printed_page: Optional[str] = None
    pdf_page_index: Optional[int] = None
    chapter_id: Optional[str] = None
    section_path: tuple[str, ...] = ()
    block_id: Optional[str] = None

    def __post_init__(self) -> None:
        if not self.source_id.strip():
            raise ValueError("source_id must be non-empty")
        if self.pdf_page_index is not None and self.pdf_page_index < 0:
            raise ValueError("pdf_page_index must be zero-based and non-negative")


@dataclass(frozen=True)
class DocumentBlock:
    locator: SourceLocator
    block_type: BlockType
    raw_text: str
    sequence_index: int
    extraction_method: str = "provided_text"
    extraction_confidence: Optional[float] = None
    warnings: tuple[str, ...] = ()
    payload: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if self.sequence_index < 0:
            raise ValueError("sequence_index must be non-negative")
        if self.extraction_confidence is not None and not 0.0 <= self.extraction_confidence <= 1.0:
            raise ValueError("extraction_confidence must be between 0 and 1")


@dataclass
class DocumentIR:
    source_id: str
    blocks: list[DocumentBlock]
    metadata: dict[str, Any] = field(default_factory=dict)
    schema_version: str = "1.0"

    def __post_init__(self) -> None:
        if not self.source_id.strip():
            raise ValueError("source_id must be non-empty")
        if any(block.locator.source_id != self.source_id for block in self.blocks):
            raise ValueError("all blocks must belong to DocumentIR.source_id")
        ids = [b.locator.block_id for b in self.blocks if b.locator.block_id]
        if len(ids) != len(set(ids)):
            raise ValueError("block_id values must be unique within a document")

    @property
    def content_sha256(self) -> str:
        canonical = "\n".join(
            f"{b.sequence_index}:{b.block_type.value}:{b.raw_text}" for b in self.blocks
        )
        return hashlib.sha256(canonical.encode("utf-8")).hexdigest()

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": self.schema_version,
            "source_id": self.source_id,
            "content_sha256": self.content_sha256,
            "metadata": self.metadata,
            "blocks": [
                {
                    **asdict(block),
                    "block_type": block.block_type.value,
                    "locator": asdict(block.locator),
                }
                for block in self.blocks
            ],
        }

    def to_jsonl(self) -> str:
        return "\n".join(
            json.dumps(
                {
                    **asdict(block),
                    "block_type": block.block_type.value,
                    "locator": asdict(block.locator),
                },
                ensure_ascii=False,
                sort_keys=True,
            )
            for block in self.blocks
        )

    @classmethod
    def from_text(
        cls,
        source_id: str,
        file_name: str,
        text: str,
        *,
        chapter_id: Optional[str] = None,
    ) -> "DocumentIR":
        """Create a conservative paragraph-level IR from already extracted text.

        This adapter intentionally does not claim PDF page/table fidelity. Use
        richer parser output when physical layout metadata is available.
        """
        blocks: list[DocumentBlock] = []
        for index, paragraph in enumerate(p for p in text.splitlines() if p.strip()):
            block_id = f"{source_id}-B{index + 1:06d}"
            locator = SourceLocator(
                source_id=source_id,
                file_name=file_name,
                chapter_id=chapter_id,
                block_id=block_id,
            )
            stripped = paragraph.strip()
            block_type = BlockType.HEADING if (
                stripped.startswith("#") or (len(stripped) < 100 and stripped.isupper())
            ) else BlockType.PARAGRAPH
            blocks.append(
                DocumentBlock(
                    locator=locator,
                    block_type=block_type,
                    raw_text=stripped,
                    sequence_index=index,
                    extraction_method="plain_text_adapter",
                    warnings=("layout_and_printed_page_not_preserved",),
                )
            )
        return cls(source_id=source_id, blocks=blocks)


def blocks_from_records(
    source_id: str,
    file_name: str,
    records: Iterable[dict[str, Any]],
) -> DocumentIR:
    """Adapt page/block dictionaries from existing parsers into the common IR."""
    blocks: list[DocumentBlock] = []
    for index, record in enumerate(records):
        text = str(record.get("text", record.get("content", "")))
        page_index = record.get("pdf_page_index", record.get("page_index"))
        locator = SourceLocator(
            source_id=source_id,
            file_name=file_name,
            printed_page=record.get("printed_page"),
            pdf_page_index=page_index if isinstance(page_index, int) else None,
            chapter_id=record.get("chapter_id"),
            section_path=tuple(record.get("section_path", ())),
            block_id=str(record.get("block_id") or f"{source_id}-B{index + 1:06d}"),
        )
        raw_type = str(record.get("block_type", "PARAGRAPH")).upper()
        try:
            block_type = BlockType(raw_type)
        except ValueError:
            block_type = BlockType.UNKNOWN
        blocks.append(
            DocumentBlock(
                locator=locator,
                block_type=block_type,
                raw_text=text,
                sequence_index=index,
                extraction_method=str(record.get("extraction_method", "existing_parser")),
                extraction_confidence=record.get("extraction_confidence"),
                warnings=tuple(record.get("warnings", ())),
                payload={k: v for k, v in record.items() if k not in {
                    "text", "content", "printed_page", "pdf_page_index", "page_index",
                    "chapter_id", "section_path", "block_id", "block_type",
                    "extraction_method", "extraction_confidence", "warnings"
                }},
            )
        )
    return DocumentIR(source_id=source_id, blocks=blocks)
