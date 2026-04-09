# create-rag-app

Python-first CLI for scaffolding practical RAG apps with one shared FastAPI backend and a selectable frontend shell.

## About

`create-rag-app` is built to scaffold readable, extensible RAG projects without forcing a heavy framework stack. The backend is the shared core in every generated app, and the frontend is an optional shell chosen during init.

The project is centered around:

- one clean FastAPI backend architecture across all generated variants
- opinionated defaults first, then additive `create-rag-app add ...` capabilities later
- machine-readable project metadata plus human-editable runtime config

## Progress

Current capabilities:

- `create-rag-app init <project-name>`
- frontend choice during init: `nextjs`, `streamlit`, or `backend-only`
- the same FastAPI backend scaffold generated for all three variants
- generated manifest: `create-rag-app.manifest.json`
- generated runtime config: `rag.toml`
- one narrow happy path for RAG:
  - local docs
  - recursive chunking
  - OpenAI embeddings
  - Chroma vector store
  - dense retrieval

- CLI scaffold flow for the three app shapes
- shared backend modules for ingestion, chunking, embeddings, vector store access, retrieval, and answer generation
- minimal Next.js chat shell over HTTP
- minimal Streamlit shell over HTTP
- backend-only mode for API-first usage

## Upcoming

Next steps:

- improve generated app polish and end-to-end setup experience
- add safe extension points for alternate chunkers, retrieval modes, and providers
- support future `create-rag-app add ...` commands using the manifest/config foundation
- expand testing beyond scaffold generation into stronger generated-project verification

## Development

```bash
pip install -e .[dev]
pytest
```
