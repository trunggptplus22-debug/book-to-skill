"""Runtime capability probe; no assumptions about NotebookLM execution features."""
from __future__ import annotations

import importlib.util
import os
import platform
import shutil
import sys


def probe_runtime() -> dict:
    candidates = ("pypdf", "pdfminer", "docling", "ebooklib", "pandas", "pydantic", "sympy")
    available = {name: importlib.util.find_spec(name) is not None for name in candidates}
    return {
        "python_available": True,
        "python_version": platform.python_version(),
        "implementation": platform.python_implementation(),
        "platform": platform.platform(),
        "working_directory": os.getcwd(),
        "writable_working_directory": os.access(os.getcwd(), os.W_OK),
        "executables": {name: shutil.which(name) for name in ("pdftotext", "epub-convert", "git")},
        "optional_packages": available,
        "can_write_files": os.access(os.getcwd(), os.W_OK),
        "notes": [
            "This probes the current Python runtime only.",
            "It does not prove NotebookLM can persist files, access uploaded source bytes, or call external services.",
            "Record results from the actual NotebookLM execution surface before enabling those features.",
        ],
    }
