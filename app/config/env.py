from enum import Enum
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Environment(str, Enum):
    LOCAL    = 'local'
    DEV      = 'dev'
    PROD     = 'prod'
    TEST_E2E = 'test_e2e'

class Environments(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True
    )

    app_name: str = "Payment Gateway"
    environment: Environment = Field(default=Environment.DEV, description="Environment of Application")
    DB_USER: str = Field(..., validation_alias="DB_USER", description="Root user of Database")
    DB_HOST: str = Field(..., validation_alias="DB_HOST", description="Database Host")
    DB_PASSWORD: str = Field(..., validation_alias="DB_PASSWORD", description="Database Password")
    DB_NAME: str = Field(..., validation_alias="DB_NAME", description="Database name")
    DB_DIALECT: str = Field(default="postgresql+psycopg2", validation_alias="DB_DIALECT", description="Database Dialect")
    DB_PORT: int = Field(default=5432, validation_alias="DB_PORT", description="Database Port")

env = Environments()