from __future__ import annotations

from pathlib import Path

import typer

from . import __version__
from .prompts import collect_init_choices
from .scaffolder import scaffold_project

app = typer.Typer(add_completion=False, no_args_is_help=True)


def _validate_project_name(name: str) -> None:
    valid = all(char.isalnum() or char in {"-", "_"} for char in name)
    if not name or not valid:
        raise typer.BadParameter(
            "Project name must contain only letters, numbers, hyphens, or underscores."
        )


@app.command()
def init(project_name: str) -> None:
    """Create a new RAG application scaffold."""
    _validate_project_name(project_name)

    target_dir = Path.cwd() / project_name
    if target_dir.exists():
        raise typer.BadParameter(f"Target directory already exists: {target_dir}")

    choices = collect_init_choices(project_name=project_name, target_dir=target_dir)
    scaffold_project(choices)

    typer.secho(f"Created {project_name} at {target_dir}", fg=typer.colors.GREEN)
    typer.echo("")
    typer.echo("Next steps:")
    typer.echo(f"  cd {project_name}")
    typer.echo("  cp .env.example .env")
    typer.echo("  Set OPENAI_API_KEY")
    typer.echo("  See README.md for backend and frontend run commands")


@app.command("list-templates")
def list_templates() -> None:
    """List supported scaffold variants."""
    typer.echo("Frontends: nextjs, streamlit, backend-only")
    typer.echo("Backend defaults: local-files, recursive, openai, chroma, dense")


@app.callback(invoke_without_command=False)
def main(version: bool = typer.Option(False, "--version", help="Print the CLI version.")) -> None:
    if version:
        typer.echo(__version__)
        raise typer.Exit()


if __name__ == "__main__":
    app()
