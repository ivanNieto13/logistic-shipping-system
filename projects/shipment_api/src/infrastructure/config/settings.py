"""Application Settings"""
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "shipment_api"
    DEBUG: bool = True
    API_VERSION: str = "v1"
    DATABASE_URL: str = "mongodb://user:password@localhost:27017/app_db"
    
    class Config:
        env_file = ".env"

settings = Settings()
