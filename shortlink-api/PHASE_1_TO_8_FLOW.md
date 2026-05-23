# Start Here: Phases 1 → 8 Flow

If you want to quickly understand the setup before starting Phase 9, review files in this order:

1. `app/main.py`  
   Entry point of the API, app creation, middleware, router registration, startup logs, and DB connectivity check.

2. `app/routes/root.py`  
   Existing public endpoints (`/`, `/health`) and current routing style.

3. `app/config.py`  
   Centralized settings loading from `.env` with defaults used by app and migrations.

4. `shortlink-api/.env.example`  
   Environment variables you need locally (database and auth-related defaults).

5. `app/database.py`  
   SQLAlchemy engine/session setup and FastAPI `get_db()` dependency.

6. `app/models/user.py` and `app/models/__init__.py`  
   First ORM model (`users` table) introduced in Phase 6.

7. `alembic.ini` and `alembic/env.py`  
   Migration system wiring and metadata discovery.

8. `alembic/versions/20260523_01_create_users_table.py`  
   First migration that creates the `users` table (Phase 8 output).

## Quick local run checklist (before Phase 9)

1. From `shortlink-api/`, copy env file:
   - `cp .env.example .env`
2. Start PostgreSQL:
   - `docker compose up -d db`
3. Install deps from repo root:
   - `python -m pip install -r requirements.txt`
4. Run migration from `shortlink-api/`:
   - `alembic upgrade head`
5. Start API from `shortlink-api/`:
   - `uvicorn app.main:app --reload`

After this, Phase 9 (`/register`) can be built directly on top.
