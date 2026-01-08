from abc import ABC, abstractmethod

from ...domain.entities.new_shipment_event import MessagePayload

class MessagePublisher(ABC):
    @abstractmethod
    async def publish(self, message: MessagePayload) -> None:
        pass