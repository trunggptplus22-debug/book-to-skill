"""Block-level coverage ledger."""
from collections import Counter
from typing import Iterable
from .classifier import Classification
from .document_ir import DocumentIR

def build_coverage_report(document:DocumentIR,classifications:Iterable[Classification])->dict:
    rows=list(classifications); by_id={x.block_id:x for x in rows}
    missing=[b.locator.block_id for b in document.blocks if b.locator.block_id not in by_id]
    counts=Counter(x.disposition.value for x in rows)
    complete=not missing and len(rows)==len(document.blocks)
    return {"source_id":document.source_id,"content_sha256":document.content_sha256,
      "total_blocks":len(document.blocks),"classified_blocks":len(rows),
      "missing_block_ids":missing,"counts_by_disposition":dict(sorted(counts.items())),
      "coverage_complete":complete,
      "completion_status":"COMPLETE_CLASSIFICATION" if complete else "INCOMPLETE_CLASSIFICATION"}
