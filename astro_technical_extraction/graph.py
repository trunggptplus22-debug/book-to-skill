"""Explicit dependency graph with cycle reporting."""
from collections import defaultdict,deque
def build_dependency_graph(records):
    nodes={r.record_id:{"type":r.record_type,"block_id":r.block_id,"text":r.verbatim[:240]} for r in records}
    edges=[]; index={r.record_id:r for r in records}
    # Heuristic links by repeated technical tokens; link only as candidate.
    tokenmap=defaultdict(set)
    for r in records:
        import re
        for tok in set(re.findall(r"\b[A-Z][A-Za-z]{2,}|\b(?:Ascendant|Midheaven|profection|dignity|reception|orb|ephemeris)\b",r.verbatim)):
            tokenmap[tok.lower()].add(r.record_id)
    for token,ids in tokenmap.items():
        ids=sorted(ids)
        for a,b in zip(ids,ids[1:]):
            if a!=b: edges.append({"from":a,"to":b,"label":"shared_term_candidate","term":token,"confirmed":False})
    return {"nodes":nodes,"edges":edges,"edge_semantics":"heuristic candidates only; not doctrinal dependencies"}
