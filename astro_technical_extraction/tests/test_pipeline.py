import json

import pytest

from astro_technical_extraction.classifier import (
    Disposition, RelevanceClass, RuleBasedClassifier,
)
from astro_technical_extraction.coverage import build_coverage_report
from astro_technical_extraction.document_ir import (
    BlockType, DocumentBlock, DocumentIR, SourceLocator,
)


def make_block(text, block_type=BlockType.PARAGRAPH, block_id="SRC-B1"):
    return DocumentBlock(
        locator=SourceLocator("SRC", "fixture.txt", block_id=block_id),
        block_type=block_type,
        raw_text=text,
        sequence_index=0,
    )


def test_ir_jsonl_preserves_source_and_block():
    ir = DocumentIR.from_text("SRC", "fixture.txt", "First line.\nSecond line.")
    rows = [json.loads(line) for line in ir.to_jsonl().splitlines()]
    assert len(rows) == 2
    assert rows[0]["locator"]["source_id"] == "SRC"
    assert rows[1]["locator"]["block_id"] == "SRC-B000002"
    assert len(ir.content_sha256) == 64


@pytest.mark.parametrize("text", [
    "The Ascendant is a significant factor in the chart.",
    "Mars has domicile in Aries.",
])
def test_technical_term_alone_is_context_not_rule(text):
    result = RuleBasedClassifier().classify(make_block(text))
    assert result.relevance_class == RelevanceClass.TECHNICAL_CONTEXT
    assert result.disposition == Disposition.CONTEXT_ONLY


def test_procedure_with_technical_term_is_core():
    result = RuleBasedClassifier().classify(
        make_block("Calculate the Ascendant from local sidereal time.")
    )
    assert result.relevance_class == RelevanceClass.TECHNICAL_CORE
    assert result.disposition == Disposition.INCLUDE


def test_empty_block_is_unreadable():
    result = RuleBasedClassifier().classify(make_block("   "))
    assert result.disposition == Disposition.UNREADABLE


def test_heading_is_sent_to_review():
    result = RuleBasedClassifier().classify(make_block("The Dignities", BlockType.HEADING))
    assert result.disposition == Disposition.REVIEW


def test_coverage_flags_missing_classification():
    ir = DocumentIR.from_text("SRC", "fixture.txt", "A\nB")
    classified = RuleBasedClassifier().classify_many(ir.blocks[:1])
    report = build_coverage_report(ir, classified)
    assert not report["coverage_complete"]
    assert report["missing_block_ids"] == ["SRC-B000002"]


def test_document_rejects_cross_source_blocks():
    block = make_block("Text")
    with pytest.raises(ValueError):
        DocumentIR("OTHER", [block])
