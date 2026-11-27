"""Probe the active Python environment; no NotebookLM capabilities are assumed."""
import importlib.util,os,platform,shutil

def probe_runtime()->dict:
    packages=("pypdf","pdfminer","docling","ebooklib","pandas","pydantic","sympy")
    return {"python_available":True,"python_version":platform.python_version(),
      "implementation":platform.python_implementation(),"platform":platform.platform(),
      "working_directory":os.getcwd(),"writable_working_directory":os.access(os.getcwd(),os.W_OK),
      "executables":{x:shutil.which(x) for x in ("pdftotext","epub-convert","git")},
      "optional_packages":{x:importlib.util.find_spec(x) is not None for x in packages},
      "notes":["Probes only the active Python runtime.",
       "Does not prove uploaded-source access, file persistence, network or GitHub access.",
       "Test each capability in the actual NotebookLM execution surface."]}
