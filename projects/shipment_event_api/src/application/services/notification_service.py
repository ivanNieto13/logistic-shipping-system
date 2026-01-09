

from ...domain.entities.message_payload import MessagePayload
from ...domain.interfaces.publisher import MessagePublisher


class NotificationService:
    def __init__(self, publisher: MessagePublisher):
        self.publisher = publisher

    async def send_notification(self, channel: str, data: dict) -> None:
        payload = MessagePayload(channel=channel, content=data)
        await self.publisher.publish(payload)
