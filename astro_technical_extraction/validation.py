"""Validation gates for extraction records; flags, never silently rewrites."""
from collections import Counter

def validate_records(document,records,coverage,strict=True):
    source={b.locator.block_id:b for b in document.blocks}
    record_ids=[r.record_id for r in records]
    issues=[]
    if len(record_ids)!=len(set(record_ids)): issues.append("duplicate_record_ids")
    for r in records:
        b=source.get(r.block_id)
        if b is None: issues.append(f"record_source_block_missing:{r.record_id}"); continue
        if r.source_id!=document.source_id or r.source_id!=b.locator.source_id: issues.append(f"source_id_mismatch:{r.record_id}")
        if r.verbatim!=b.raw_text: issues.append(f"verbatim_source_mismatch:{r.record_id}")
        if not r.verbatim.strip(): issues.append(f"empty_verbatim_record:{r.record_id}")
        if not 0<=r.confidence<=1: issues.append(f"confidence_out_of_range:{r.record_id}")
        if not r.locator: issues.append(f"missing_locator:{r.record_id}")
        elif r.locator.get("block_id")!=r.block_id or r.locator.get("source_id")!=r.source_id: issues.append(f"locator_mismatch:{r.record_id}")
    cov=coverage.get("coverage_complete",False) and coverage.get("integrity_ok",False)
    if not cov: issues.append("classification_coverage_incomplete_or_integrity_failed")
    counts=Counter(r.block_id for r in records)
    return {"valid":not issues,"issues":issues,"record_count":len(records),"source_block_count":len(source),
      "coverage_complete":cov,"duplicate_source_record_blocks":[k for k,n in counts.items() if n>1],
      "strict_gate_pass":not issues if strict else True}
