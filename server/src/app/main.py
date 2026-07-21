
from fastapi import FastAPI

def create_app() -> FastAPI:
    return FastAPI( title = "Relevo API")

app = create_app()
