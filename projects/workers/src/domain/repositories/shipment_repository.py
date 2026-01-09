from abc import ABC, abstractmethod

from ..entities.shipment import Shipment

class ShipmentRepository(ABC):   
    @abstractmethod
    def save(self, entity: Shipment) -> Shipment:
        pass