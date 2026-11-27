"""Technical-only astrology extraction primitives."""
from .document_ir import DocumentBlock, DocumentIR, BlockType, SourceLocator
from .classifier import Classification, Disposition, RelevanceClass, RuleBasedClassifier

__all__ = ["BlockType","Classification","Disposition","DocumentBlock","DocumentIR","RelevanceClass","RuleBasedClassifier","SourceLocator"]
