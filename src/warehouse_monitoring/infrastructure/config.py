from typing import Optional

from pydantic_settings import BaseSettings

import dotenv


class Environment(BaseSettings):
    postgres_password: str
    postgres_user: str
    postgres_db: str
    postgres_host: str = "0.0.0.0"
    postgres_port: int = 5432
    redis_port: int = 6379
    redis_host: str = "0.0.0.0"
    application_protocol: str = None
    allowed_origin: Optional[str] = None
    application_ssl_keyfile: Optional[str] = None
    application_ssl_certfile: Optional[str] = None
    allow_testing: bool = False
    jwt_secret: str
    jwt_expire_minutes: int
    telegram_bot_token: str
    website_base_url: str


def load_env(filename: str) -> Environment:
    dotenv.load_dotenv(filename)

    return Environment()


environment = load_env('.env')
