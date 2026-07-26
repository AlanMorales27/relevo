
from fastapi import FastAPI
from .presentation.api.router import api_router
from .core.database import init_db


def create_app() -> FastAPI:
    app = FastAPI(title="Relevo API")
    app.include_router(api_router)

    init_db()

    return app


app = create_app()
