from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

from src.domain.constants import TEXT_ENCODING


class Settings(BaseSettings):
    FILE_REPORT_DIR: str = Field(default="./data/report")

    # 2 ГБ
    MAX_UPLOAD_SIZE: int = Field(default=2 * 1024 * 1024 * 1024)
    LOG_LEVEL: str = Field(default="INFO")
    DEBUG: bool = Field(default=True)

    APP_HOST: str = "127.0.0.1"
    APP_PORT: int = 8000

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding=TEXT_ENCODING,
        extra="ignore"
    )

settings = Settings()