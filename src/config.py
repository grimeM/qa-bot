from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr


class Config(BaseSettings):
    model_config = SettingsConfigDict(secrets_dir="/secrets")

    production: bool = False
    run_dir: Path = Path("/run")

    telegram_api_token: SecretStr

    questions_file: Path = Path("/data/qa.json")
    answer_threshold: float = 60
