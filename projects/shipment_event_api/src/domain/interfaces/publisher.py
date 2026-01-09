from abc import ABC, abstractmethod

from ..entities.message_payload import MessagePayload

class MessagePublisher(ABC):
    @abstractmethod
    async def publish(self, message: MessagePayload) -> None:
        pass