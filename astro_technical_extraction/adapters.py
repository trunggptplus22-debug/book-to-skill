"""Thin adapter boundary around the existing Book-to-Skill extractor."""
from pathlib import Path
from .document_ir import DocumentIR

def from_extracted_text(source_id:str,path:str|Path,extracted_text:str)->DocumentIR:
    return DocumentIR.from_text(source_id,Path(path).name,extracted_text)

def extract_with_existing_pipeline(source_id:str,path:str|Path)->DocumentIR:
    """Call the existing parser dispatch, leaving parser behavior untouched."""
    from book_to_skill.utils import extract_file
    p=Path(path)
    extracted=extract_file(str(p))
    if not isinstance(extracted,str):
        raise TypeError("Expected existing extractor to return text; inspect this adapter for the repository version.")
    return from_extracted_text(source_id,p,extracted)
