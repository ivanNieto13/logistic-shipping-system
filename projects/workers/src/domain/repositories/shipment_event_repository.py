from abc import ABC, abstractmethod

from ...domain.entities.shipment_event import ShipmentEvent

class ShipmentEventRepository(ABC):   
    @abstractmethod
    def save(self, entity: ShipmentEvent) -> ShipmentEvent:
        pass
    
    @abstractmethod
    def find(self, entity: ShipmentEvent) -> ShipmentEvent:
        pass