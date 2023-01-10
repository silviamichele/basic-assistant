from pydantic import BaseSettings


class AssistantConfig(BaseSettings):
    OPEN_API_KEY: str

    class Config:
        env_file = ".env"
        env_prefix = "ASS_"


def create_config():
    return AssistantConfig()


settings = create_config()
