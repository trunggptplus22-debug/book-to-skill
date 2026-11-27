import json
import pytest
from astro_technical_extraction.classifier import Disposition,RelevanceClass,RuleBasedClassifier
from astro_technical_extraction.coverage import build_coverage_report
from astro_technical_extraction.document_ir import BlockType,DocumentBlock,DocumentIR,SourceLocator

def block(text,kind=BlockType.PARAGRAPH,block_id="SRC-B1"):
    return DocumentBlock(SourceLocator("SRC","fixture.txt",block_id=block_id),kind,text,0)

def test_ir_jsonl_and_hash():
    ir=DocumentIR.from_text("SRC","fixture.txt","First line.\nSecond line.")
    rows=[json.loads(line) for line in ir.to_jsonl().splitlines()]
    assert len(rows)==2 and rows[1]["locator"]["block_id"]=="SRC-B000002"
    assert len(ir.content_sha256)==64

@pytest.mark.parametrize("text",["The Ascendant is significant in this chart.","Mars has domicile in Aries."])
def test_technical_term_alone_is_context(text):
    result=RuleBasedClassifier().classify(block(text))
    assert result.relevance_class==RelevanceClass.TECHNICAL_CONTEXT
    assert result.disposition==Disposition.CONTEXT_ONLY

def test_procedure_plus_term_is_core():
    result=RuleBasedClassifier().classify(block("Calculate the Ascendant from local sidereal time."))
    assert result.disposition==Disposition.INCLUDE
    assert result.relevance_class==RelevanceClass.TECHNICAL_CORE

def test_blank_is_unreadable():
    assert RuleBasedClassifier().classify(block(" ")).disposition==Disposition.UNREADABLE

def test_heading_requires_review():
    assert RuleBasedClassifier().classify(block("The Dignities",BlockType.HEADING)).disposition==Disposition.REVIEW

def test_coverage_detects_missing_blocks():
    ir=DocumentIR.from_text("SRC","fixture.txt","A\nB")
    report=build_coverage_report(ir,RuleBasedClassifier().classify_many(ir.blocks[:1]))
    assert not report["coverage_complete"]
    assert report["missing_block_ids"]==["SRC-B000002"]

def test_rejects_mixed_sources():
    with pytest.raises(ValueError):
        DocumentIR("OTHER",[block("wrong source")])
