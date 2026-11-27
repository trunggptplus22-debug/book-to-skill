"""Technical-only astrology extraction primitives.

This package is an isolated extension. It does not alter the original
Book-to-Skill extraction pipeline.
"""
from .document_ir import DocumentBlock, DocumentIR, BlockType, SourceLocator
from .classifier import Classification, Disposition, RelevanceClass, RuleBasedClassifier

__all__ = [
    "BlockType", "Classification", "Disposition", "DocumentBlock",
    "DocumentIR", "RelevanceClass", "RuleBasedClassifier", "SourceLocator",
]
