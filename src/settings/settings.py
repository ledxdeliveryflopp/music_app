from functools import lru_cache

from pydantic_settings import BaseSettings


class ApiSettings(BaseSettings):

    api_url: str = "http://localhost:7000/"


class Settings(BaseSettings):

    api_settings: ApiSettings


@lru_cache
def init_settings() -> Settings:
    return Settings(api_settings=ApiSettings())


settings = init_settings()
