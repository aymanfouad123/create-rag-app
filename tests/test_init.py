from __future__ import annotations

import json

from typer.testing import CliRunner

from create_rag_app.cli import app


runner = CliRunner()


def test_init_generates_nextjs_project(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    result = runner.invoke(app, ["init", "demo-rag"], input="\n\n\n\n\n\ny\n")

    assert result.exit_code == 0, result.output
    project_dir = tmp_path / "demo-rag"
    assert (project_dir / "backend" / "app" / "main.py").exists()
    assert (project_dir / "frontend" / "app" / "page.tsx").exists()
    assert (project_dir / "frontend" / "lib" / "api.ts").exists()
    assert not (project_dir / "frontend" / "app" / "api.ts").exists()
    assert not (project_dir / "frontend" / "components" / "ui" / "card.tsx").exists()
    assert (project_dir / "rag.toml").exists()
    assert (project_dir / "create-rag-app.manifest.json").exists()

    manifest = json.loads((project_dir / "create-rag-app.manifest.json").read_text())
    assert manifest["project"]["frontend"] == "nextjs"
    assert manifest["backend"]["rag_profile"]["embedding_provider"] == "openai"

    config = (project_dir / "rag.toml").read_text()
    assert 'frontend = "nextjs"' in config
    assert 'provider = "chroma"' in config
    readme = (project_dir / "README.md").read_text()
    assert "## Project Layout" in readme
    assert "        ## Project Layout" not in readme
    assert (project_dir / ".env.example").read_text() == "OPENAI_API_KEY=\n"


def test_init_generates_streamlit_project(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    result = runner.invoke(
        app,
        ["init", "streamlit-rag"],
        input="streamlit\n\n\n\n\n\ny\n",
    )

    assert result.exit_code == 0, result.output
    project_dir = tmp_path / "streamlit-rag"
    assert (project_dir / "frontend" / "app.py").exists()
    assert not (project_dir / "frontend" / "app" / "page.tsx").exists()
    assert 'frontend = "streamlit"' in (project_dir / "rag.toml").read_text()


def test_init_generates_backend_only_project(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    result = runner.invoke(
        app,
        ["init", "backend-rag"],
        input="backend-only\n\n\n\n\n\ny\n",
    )

    assert result.exit_code == 0, result.output
    project_dir = tmp_path / "backend-rag"
    assert (project_dir / "backend" / "app" / "api" / "routes" / "chat.py").exists()
    assert not (project_dir / "frontend").exists()

    manifest = json.loads((project_dir / "create-rag-app.manifest.json").read_text())
    assert manifest["paths"]["frontend_dir"] is None
    assert manifest["capabilities"]["frontend_shell"] is False


def test_init_rejects_invalid_name():
    result = runner.invoke(app, ["init", "bad/name"])
    assert result.exit_code != 0
    assert "Project name must contain only letters" in result.output


def test_init_rejects_existing_directory(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    (tmp_path / "existing-app").mkdir()
    result = runner.invoke(app, ["init", "existing-app"])

    assert result.exit_code != 0
    assert "Target directory already exists" in result.output


def test_list_templates():
    result = runner.invoke(app, ["list-templates"])
    assert result.exit_code == 0
    assert "Frontends: nextjs, streamlit, backend-only" in result.output
