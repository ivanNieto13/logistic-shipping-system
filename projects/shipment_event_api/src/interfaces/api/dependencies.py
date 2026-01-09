import os
from motor.motor_asyncio import AsyncIOMotorClient

from ...infrastructure.database.repositories.shipment_event_repository import ShipmentEventRepository
from ...infrastructure.database.repositories.shipment_repository import ShipmentRepository
from ...infrastructure.adapters.redis_adapter import RedisPublisherAdapter
from ...application.services.notification_service import NotificationService
from ...infrastructure.config.settings import settings

_redis_adapter: RedisPublisherAdapter = None

def get_redis_adapter() -> RedisPublisherAdapter:
    global _redis_adapter
    if _redis_adapter is None:
        _redis_adapter = RedisPublisherAdapter(os.getenv("REDIS_URL", settings.REDIS_URL))
    return _redis_adapter

def get_notification_service() -> NotificationService:
    adapter = get_redis_adapter()
    return NotificationService(publisher=adapter)

def get_shipment_repository_db() -> ShipmentRepository:
    client = AsyncIOMotorClient(os.getenv("DATABASE_URL", "mongodb://root:example@db:27017"), uuidRepresentation="standard")
    db = client[os.getenv("DATABASE_NAME", "app_db")]
    return ShipmentRepository(db)

def get_shipment_event_repository_db() -> ShipmentEventRepository:
    client = AsyncIOMotorClient(os.getenv("DATABASE_URL", "mongodb://root:example@db:27017"), uuidRepresentation="standard")
    db = client[os.getenv("DATABASE_NAME", "app_db")]
    return ShipmentEventRepository(db)