"""Strict block-level coverage reconciliation."""
from collections import Counter
from typing import Iterable
from .classifier import Classification
from .document_ir import DocumentIR

def build_coverage_report(document: DocumentIR, classifications: Iterable[Classification]) -> dict:
    rows=list(classifications); source_ids=[b.locator.block_id for b in document.blocks]; result_ids=[x.block_id for x in rows]
    duplicate_source_ids=sorted({x for x in source_ids if source_ids.count(x)>1})
    duplicate_result_ids=sorted({x for x in result_ids if result_ids.count(x)>1})
    missing=sorted(set(source_ids)-set(result_ids)); unexpected=sorted(set(result_ids)-set(source_ids))
    null_source_ids=[i for i,x in enumerate(source_ids) if not x]; null_result_ids=[i for i,x in enumerate(result_ids) if not x]
    counts=Counter(x.disposition.value for x in rows)
    integrity_ok=not (duplicate_source_ids or duplicate_result_ids or missing or unexpected or null_source_ids or null_result_ids)
    complete=integrity_ok and len(rows)==len(document.blocks)
    return {"source_id":document.source_id,"content_sha256":document.content_sha256,"manifest_sha256":document.manifest_sha256,
      "total_blocks":len(document.blocks),"classified_blocks":len(rows),"missing_block_ids":missing,"unexpected_block_ids":unexpected,
      "duplicate_source_block_ids":duplicate_source_ids,"duplicate_classification_block_ids":duplicate_result_ids,
      "null_source_id_indices":null_source_ids,"null_classification_id_indices":null_result_ids,
      "counts_by_disposition":dict(sorted(counts.items())),"integrity_ok":integrity_ok,"coverage_complete":complete,
      "completion_status":"COMPLETE_CLASSIFICATION" if complete else "INCOMPLETE_CLASSIFICATION"}
