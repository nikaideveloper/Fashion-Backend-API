from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    MAIL_USERNAME: str
    MAIL_PASSWORD: str
    MAIL_FROM: str

    MAIL_SERVER: str = "smtp.gmail.com"
    MAIL_PORT: int = 587

    FRONTEND_URL: str = "http://localhost:3000"


    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    DATABASE_URL : str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )


settings = Settings()