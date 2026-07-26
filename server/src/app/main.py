
from fastapi import FastAPI
from .presentation.api.router import api_router


def create_app() -> FastAPI:
    app = FastAPI(title="Relevo API")
    app.include_router(api_router)
    return app


app = create_app()
