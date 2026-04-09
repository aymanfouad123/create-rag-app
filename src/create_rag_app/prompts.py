from __future__ import annotations

import click
import typer

from .models import (
    CHUNKING_STRATEGIES,
    DOC_SOURCE_TYPES,
    EMBEDDING_PROVIDERS,
    FRONTENDS,
    RETRIEVAL_MODES,
    VECTOR_STORES,
    InitChoices,
)


def _choice(values: tuple[str, ...]) -> click.Choice:
    return click.Choice(list(values), case_sensitive=False)


def collect_init_choices(project_name: str, target_dir) -> InitChoices:
    frontend = typer.prompt(
        "Frontend shell",
        type=_choice(FRONTENDS),
        default="nextjs",
        show_choices=True,
    )
    document_source_type = typer.prompt(
        "Document source type",
        type=_choice(DOC_SOURCE_TYPES),
        default="local-files",
        show_choices=True,
    )
    chunking_strategy = typer.prompt(
        "Chunking strategy",
        type=_choice(CHUNKING_STRATEGIES),
        default="recursive",
        show_choices=True,
    )
    vector_store = typer.prompt(
        "Vector database",
        type=_choice(VECTOR_STORES),
        default="chroma",
        show_choices=True,
    )
    embedding_provider = typer.prompt(
        "Embedding provider",
        type=_choice(EMBEDDING_PROVIDERS),
        default="openai",
        show_choices=True,
    )
    retrieval_mode = typer.prompt(
        "Retrieval mode",
        type=_choice(RETRIEVAL_MODES),
        default="dense",
        show_choices=True,
    )
    include_sample_assets = typer.confirm("Include sample docs and env file?", default=True)

    return InitChoices(
        project_name=project_name,
        target_dir=target_dir,
        frontend=frontend,
        document_source_type=document_source_type,
        chunking_strategy=chunking_strategy,
        embedding_provider=embedding_provider,
        vector_store=vector_store,
        retrieval_mode=retrieval_mode,
        include_sample_assets=include_sample_assets,
    )
