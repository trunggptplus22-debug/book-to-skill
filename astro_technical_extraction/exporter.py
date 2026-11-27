"""Machine-readable export plus human audit bundle."""
import json
from dataclasses import asdict
def export_bundle(document,classifications,records,coverage,validation,graph):
    return {"manifest":document.to_dict(),"classifications":[c.to_dict() for c in classifications],
      "technical_records":[asdict(r) for r in records],"coverage":coverage,"validation":validation,"dependency_graph":graph,
      "export_notice":"Normalized interpretations are absent unless explicitly populated; records are heuristic and review-required."}
def export_json(bundle): return json.dumps(bundle,ensure_ascii=False,indent=2,sort_keys=True)
