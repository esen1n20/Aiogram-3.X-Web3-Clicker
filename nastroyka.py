from pydantic import SecretStr, BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    bot_token: SecretStr
    model_config: SettingsConfigDict = SettingsConfigDict(

        env_file = '.env',
        env_file_encoding = 'utf-8'
    )

config = Settings()