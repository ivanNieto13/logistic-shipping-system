import os
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