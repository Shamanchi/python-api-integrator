from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    api_base_url: str = 'https://api.example.com'
    api_key: Optional[str] = None
    api_timeout: int = 30
    retry_attempts: int = 3
    retry_backoff: float = 1.5
    database_url: str = 'sqlite:///./integrations.db'
    log_level: str = 'INFO'

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        extra = 'ignore'


settings = Settings()