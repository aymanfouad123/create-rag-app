# create-rag-app

Python-first CLI for scaffolding opinionated RAG applications with a shared FastAPI backend.

Milestone 1 supports:
- `create-rag-app init <project-name>`
- frontend selection: `nextjs`, `streamlit`, `backend-only`
- shared FastAPI backend in every generated project
- one default RAG stack: local docs, recursive chunking, OpenAI embeddings, Chroma, dense retrieval

## Development

```bash
pip install -e .[dev]
pytest
```
