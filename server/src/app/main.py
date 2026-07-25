
from fastapi import FastAPI

from server.src.app.presentation.api.router import api_router


def create_app() -> FastAPI:
    app = FastAPI(title="Relevo API")
    app.include_router(api_router)
    return app


app = create_app()
