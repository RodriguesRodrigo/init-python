from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str
    SECRET_KEY: str
    DEBUG: str

    ALLOWED_HOSTS: list[str] = ["http://localhost", "http://127.0.0.1"]
    DOCS_URL: str | None = None
    OPENAPI_URL: str | None = None
    REDOC_URL: str | None = None

    class Config:
        env_file: str = ".env"
        env_file_encoding: str = "utf-8"


settings = Settings()
