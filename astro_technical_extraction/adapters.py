"""Adapter to the existing Book-to-Skill extraction API."""
from pathlib import Path
from .document_ir import DocumentIR, blocks_from_records

def from_extracted_text(source_id: str, path: str | Path, extracted_text: str) -> DocumentIR:
    """Fallback adapter for flattened text; records the loss of physical layout."""
    return DocumentIR.from_text(source_id, Path(path).name, extracted_text)

def extract_with_existing_pipeline(source_id: str, path: str | Path,
                                    extraction_mode: str = "technical",
                                    install_mode: str = "ask") -> DocumentIR:
    """Reuse extract_single_file(); do not duplicate format-specific parser logic.

    The original parser returns text and metadata. Since it does not expose
    page-level blocks through this API, paragraph locators are used and the
    Document IR flags missing printed-page/layout fidelity.
    """
    from book_to_skill.utils import extract_single_file
    source = Path(path)
    result = extract_single_file(source, extraction_mode, install_mode)
    text = result.get("text")
    if not isinstance(text, str) or not text.strip():
        raise ValueError("The existing extractor returned no usable text.")
    document = from_extracted_text(source_id, source, text)
    document.metadata.update({
        "filename": result.get("filename", source.name),
        "format": result.get("format"),
        "extraction_method": result.get("extraction_method"),
        "fallback_reason": result.get("fallback_reason"),
        "source_sha256": result.get("sha256"),
        "pages": result.get("pages"),
        "pages_label": result.get("pages_label"),
        "chapters_detected": result.get("chapters_detected"),
        "chapters_method": result.get("chapters_method"),
        "layout_fidelity": "FLATTENED_TEXT_ONLY",
    })
    return document
