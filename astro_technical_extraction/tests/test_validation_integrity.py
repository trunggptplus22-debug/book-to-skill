import unittest
from ..document_ir import DocumentIR
from ..classifier import RuleBasedClassifier
from ..coverage import build_coverage_report
from ..extraction import extract_records
from ..validation import validate_records

class ValidationTests(unittest.TestCase):
 def setUp(self):
  self.doc=DocumentIR.from_text("S","fixture.txt","Calculate the Ascendant.")
  self.cl=RuleBasedClassifier().classify_many(self.doc.blocks)
  self.coverage=build_coverage_report(self.doc,self.cl)
  self.records=extract_records(self.doc,self.cl)
 def test_verbatim_and_source_pass(self):
  self.assertTrue(validate_records(self.doc,self.records,self.coverage)["valid"])
 def test_verbatim_mutation_detected(self):
  r=self.records[0]; r.verbatim+=" changed"
  self.assertIn("verbatim_source_mismatch:"+r.record_id,validate_records(self.doc,self.records,self.coverage)["issues"])
 def test_source_id_mutation_detected(self):
  r=self.records[0]; r.source_id="OTHER"
  self.assertIn("source_id_mismatch:"+r.record_id,validate_records(self.doc,self.records,self.coverage)["issues"])
 def test_locator_mismatch_detected(self):
  r=self.records[0]; r.locator["block_id"]="OTHER"
  self.assertIn("locator_mismatch:"+r.record_id,validate_records(self.doc,self.records,self.coverage)["issues"])
