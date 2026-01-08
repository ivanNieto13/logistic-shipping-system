import json
import redis.asyncio as redis
from ...domain.interfaces.publisher import MessagePublisher
from ...domain.entities.message_payload import MessagePayload

class RedisPublisherAdapter(MessagePublisher):
    def __init__(self, redis_url: str):
        self.redis_client = redis.from_url(redis_url, decode_responses=True)

    async def publish(self, message: MessagePayload) -> None:
        message_str = json.dumps(message.content)
        
        await self.redis_client.publish(message.channel, message_str)

    async def close(self):
        await self.redis_client.close()