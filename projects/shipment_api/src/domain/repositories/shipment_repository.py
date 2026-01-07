from abc import ABC, abstractmethod
from typing import List

from ..entities.shipment import Shipment

class IShipmentRepository(ABC):   
    @abstractmethod
    async def create_many(self, entity: List[Shipment]) -> List[Shipment]:
        pass
