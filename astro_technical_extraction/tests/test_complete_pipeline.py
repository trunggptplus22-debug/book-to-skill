import unittest
from ..document_ir import DocumentIR,BlockType
from ..classifier import RuleBasedClassifier,Disposition
from ..coverage import build_coverage_report
from ..extraction import extract_records
from ..validation import validate_records
from ..graph import build_dependency_graph
from ..exporter import export_bundle,export_json
from ..benchmark import evaluate

class PipelineTests(unittest.TestCase):
 def doc(self):
  return DocumentIR.from_text("fixture","fixture.txt","# Procedure\nCalculate the Ascendant using longitude and latitude.\nFormula: x = sin(a) + cos(b).\nA worked example chart.")
 def test_hash_and_coverage(self):
  d=self.doc(); c=RuleBasedClassifier().classify_many(d.blocks); report=build_coverage_report(d,c)
  self.assertTrue(report["coverage_complete"]); self.assertEqual(len(d.content_sha256),64); self.assertEqual(len(d.manifest_sha256),64)
 def test_extraction_validation_export(self):
  d=self.doc(); c=RuleBasedClassifier().classify_many(d.blocks); cov=build_coverage_report(d,c)
  r=extract_records(d,c); v=validate_records(d,r,cov); g=build_dependency_graph(r)
  self.assertEqual(v["record_count"],len(r)); self.assertIn("technical_records",export_bundle(d,c,r,cov,v,g)); self.assertIn("manifest_sha256",export_json(export_bundle(d,c,r,cov,v,g)))
 def test_benchmark(self):
  m=evaluate({"a":"INCLUDE","b":"EXCLUDE"},{"a":"INCLUDE","b":"REVIEW"})
  self.assertEqual(m["include_precision"],1); self.assertEqual(m["include_recall"],1); self.assertEqual(m["label_exact_accuracy"],.5)
 def test_duplicate_classification_rejected_by_coverage(self):
  d=self.doc(); c=RuleBasedClassifier().classify_many(d.blocks); report=build_coverage_report(d,c+[c[0]])
  self.assertFalse(report["integrity_ok"])
if __name__=="__main__": unittest.main()
