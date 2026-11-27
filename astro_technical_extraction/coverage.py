"""Coverage ledger ensuring every parsed block receives a disposition."""
from __future__ import annotations

from collections import Counter
from typing import Iterable

from .classifier import Classification
from .document_ir import DocumentIR


def build_coverage_report(document: DocumentIR, classifications: Iterable[Classification]) -> dict:
    rows = list(classifications)
    by_id = {row.block_id: row for row in rows}
    missing = [
        block.locator.block_id for block in document.blocks
        if block.locator.block_id not in by_id
    ]
    counts = Counter(row.disposition.value for row in rows)
    return {
        "source_id": document.source_id,
        "content_sha256": document.content_sha256,
        "total_blocks": len(document.blocks),
        "classified_blocks": len(rows),
        "missing_block_ids": missing,
        "counts_by_disposition": dict(sorted(counts.items())),
        "coverage_complete": not missing and len(rows) == len(document.blocks),
        "completion_status": "COMPLETE_CLASSIFICATION" if not missing and len(rows) == len(document.blocks)
                             else "INCOMPLETE_CLASSIFICATION",
    }
