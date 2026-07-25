
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DEBUG: bool = False
    DATA_SOURCE: str = "postgresql://postgres:dev12345@localhost:5432/relevo_app_db"


settings = Settings()