from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore"
    )
    
    # Application
    APP_NAME: str = "Aury"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True
    ENVIRONMENT: str = "development"
    LOG_LEVEL: str = "INFO"
    
    # Server
    HOST: str = "0.0.0.0"
    PORT: int = 8686
    
    # Database
    MONGODB_URL: str = "mongodb://localhost:27033"
    MONGODB_DB_NAME: str = "aury_db"
    
    # Telegram
    TELEGRAM_BOT_TOKEN: str = ""
    TELEGRAM_API_ID: int = 0
    TELEGRAM_API_HASH: str = ""


settings = Settings()
