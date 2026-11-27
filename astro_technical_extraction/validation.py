"""Validation gates for extraction records; flags, never silently rewrites."""
from collections import Counter
def validate_records(document,records,classification,strict=True):
    block_ids={b.locator.block_id for b in document.blocks}; rec_ids=[r.record_id for r in records]; src=[r.block_id for r in records]
    issues=[]
    if len(rec_ids)!=len(set(rec_ids)): issues.append("duplicate_record_ids")
    if any(x not in block_ids for x in src): issues.append("record_source_block_missing")
    if any(not r.verbatim.strip() for r in records): issues.append("empty_verbatim_record")
    if any(r.confidence<0 or r.confidence>1 for r in records): issues.append("confidence_out_of_range")
    if any(not r.locator for r in records): issues.append("missing_locator")
    cov=classification.get("coverage_complete",False)
    if not cov: issues.append("classification_coverage_incomplete")
    byblock=Counter(src)
    return {"valid":not issues,"issues":issues,"record_count":len(records),"source_block_count":len(block_ids),
      "coverage_complete":cov,"duplicate_source_record_blocks":[k for k,v in byblock.items() if v>1],
      "strict_gate_pass":not issues if strict else True}
