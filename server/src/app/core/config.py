
from pydantic import model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="../.env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    DEBUG: bool = False
    LOCAL_DB_PASSWORD: str = ""
    DATA_SOURCE: str = ""
    
    @model_validator(mode="after")
    def get_data_source(self):
        if not self.DATA_SOURCE:
            self.DATA_SOURCE = f"postgresql://postgres:{self.LOCAL_DB_PASSWORD}@localhost:5432/relevo_app_db"
        return self

settings = Settings()