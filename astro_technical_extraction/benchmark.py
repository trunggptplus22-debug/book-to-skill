"""Benchmark metrics for manually labelled blocks."""
def evaluate(gold,pred):
    # gold/pred map block ID -> INCLUDE/CONTEXT_ONLY/EXCLUDE/REVIEW/UNREADABLE
    ids=set(gold)|set(pred); missing=set(gold)-set(pred); extra=set(pred)-set(gold)
    tp=sum(gold.get(i)=="INCLUDE" and pred.get(i)=="INCLUDE" for i in ids)
    fp=sum(pred.get(i)=="INCLUDE" and gold.get(i)!="INCLUDE" for i in ids)
    fn=sum(gold.get(i)=="INCLUDE" and pred.get(i)!="INCLUDE" for i in ids)
    precision=tp/(tp+fp) if tp+fp else None; recall=tp/(tp+fn) if tp+fn else None
    return {"block_ids":len(ids),"missing_labels":sorted(missing),"unexpected_predictions":sorted(extra),
      "include_precision":precision,"include_recall":recall,"tp":tp,"fp":fp,"fn":fn,
      "label_exact_accuracy":sum(gold.get(i)==pred.get(i) for i in ids)/len(ids) if ids else None}
