"""Adapters around Book-to-Skill's existing text extraction functions.

The original extractor remains the owner of file-format parsing. These
adapters convert its text output to a conservative paragraph-level IR.
For table/layout fidelity, pass richer page/block records to blocks_from_records.
"""
from __future__ import annotations

from pathlib import Path

from .document_ir import DocumentIR


def from_extracted_text(source_id: str, path: str | Path, extracted_text: str) -> DocumentIR:
    return DocumentIR.from_text(source_id, Path(path).name, extracted_text)


def extract_with_existing_pipeline(source_id: str, path: str | Path) -> DocumentIR:
    """Use existing Book-to-Skill parser dispatch without copying parser logic."""
    from book_to_skill.utils import extract_file  # local import avoids import-time coupling

    file_path = Path(path)
    extracted = extract_file(str(file_path))
    if not isinstance(extracted, str):
        raise TypeError("Existing extract_file() must return text; inspect adapter for this repository version.")
    return from_extracted_text(source_id, file_path, extracted)
