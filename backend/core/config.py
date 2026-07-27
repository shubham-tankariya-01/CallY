from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    PROJECT_NAME: str = "Meet"
    VERSION: str = "1.0.0"
    DATABASE_URL: str = "sqlite:///./app.db"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_ignore_empty=True,
        extra="ignore",
    )


settings = AppSettings()