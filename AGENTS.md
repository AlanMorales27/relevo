# CODENAME: RELEVEO APP

- If you need more information about the project structure and architecture you can go for `project-architecture` skill
- Never add or modify code related to `config.py` or `.env`
- Never create branches or commits unless explicitly requested.


Dependencies flow inward: presentation → application → domain. Infrastructure depends on domain. Never import upward.

## Run

Requires a `.env` file in `server/` or env vars set. Default DB connection: `postgresql://postgres:dev12345@localhost:5432/relevo_app_db`.

```bash
cd server
pip install -r requirements.txt
uvicorn src.app.main:app --reload
```

## Key facts

- `requirements.txt` is a frozen pip export — add new deps with `pip install <pkg> && pip freeze > requirements.txt`
- No test framework or linting config exists yet. `scripts/` and `test/` are empty.
- No CI/CD pipelines. No Dockerfile. No `pyproject.toml`.
- Auth routes (`auth_routes.py`) are stubs — not implemented.
- `pydantic-settings` loads config from env vars (see `core/config.py`). `DATA_SOURCE` and `DEBUG` are the only settings.
- Schemas are re-exported from `presentation/schemas/__init__.py` — import from the package, not from individual files.

## Conventions

- New routes go in `presentation/api/routes/` and get registered in `presentation/api/router.py`.
- New schemas go in `presentation/schemas/` and get re-exported in `__init__.py`.
- Use relative imports within `src/app` (e.g., `from ...core.config import settings`).
- The project uses Spanish in a few places (`get_data_base`, error messages) — keep naming consistent with existing code.
