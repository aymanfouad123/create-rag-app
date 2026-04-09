from __future__ import annotations

import json
from pathlib import Path

from . import __version__
from .models import InitChoices
from .templates import build_files


def scaffold_project(choices: InitChoices) -> None:
    files = build_files(choices, cli_version=__version__)
    choices.target_dir.mkdir(parents=True, exist_ok=False)

    for relative_path, content in files.items():
        destination = choices.target_dir / relative_path
        destination.parent.mkdir(parents=True, exist_ok=True)

        if isinstance(content, dict):
            destination.write_text(json.dumps(content, indent=2) + "\n", encoding="utf-8")
        else:
            destination.write_text(content, encoding="utf-8")
