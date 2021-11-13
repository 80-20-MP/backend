from pydantic import BaseSettings

__all__ = ("Settings", "settings")


class Settings(BaseSettings):
    max_workers: int = 10


settings = Settings()
