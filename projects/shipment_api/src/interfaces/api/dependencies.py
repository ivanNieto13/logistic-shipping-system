import os
from ...infrastructure.adapters.redis_adapter import RedisPublisherAdapter
from ...application.services.notification_service import NotificationService

_redis_adapter: RedisPublisherAdapter = None

def get_redis_adapter() -> RedisPublisherAdapter:
    global _redis_adapter
    if _redis_adapter is None:
        _redis_adapter = RedisPublisherAdapter(os.getenv("REDIS_URL", "redis://localhost:6379"))
    return _redis_adapter

def get_notification_service() -> NotificationService:
    adapter = get_redis_adapter()
    return NotificationService(publisher=adapter)