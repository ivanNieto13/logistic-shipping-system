"""Application Settings"""
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "shipment_api"
    DEBUG: bool = True
    API_VERSION: str = "v1"
    DATABASE_URL: str = "mongodb://user:password@localhost:27017/app_db"
    DATABASE_NAME: str = "shipments_db"
    SHIPMENTS_COLLECTION_NAME: str = "shipments"
    REDIS_URL: str = "redis://localhost:6379"
    CREATE_SHIPMENT_CHANNEL: str = "shipment"
    
    class Config:
        env_file = ".env"

settings = Settings()
