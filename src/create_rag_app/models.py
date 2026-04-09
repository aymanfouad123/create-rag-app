from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


FRONTENDS = ("nextjs", "streamlit", "backend-only")
DOC_SOURCE_TYPES = ("local-files",)
CHUNKING_STRATEGIES = ("recursive",)
EMBEDDING_PROVIDERS = ("openai",)
VECTOR_STORES = ("chroma",)
RETRIEVAL_MODES = ("dense",)


@dataclass(frozen=True)
class InitChoices:
    project_name: str
    target_dir: Path
    frontend: str
    document_source_type: str
    chunking_strategy: str
    embedding_provider: str
    vector_store: str
    retrieval_mode: str
    include_sample_assets: bool
