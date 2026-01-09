from uuid import UUID

from ...interfaces.schemas.shipment_event import ShipmentEventType

class ShipmentEvent:
    def __init__(
        self,
        shipment_id: UUID | str | None = None,
        event: ShipmentEventType | None = None,
        origin_date: float | None = None,
        author: str | None = None,
    ):
        self.shipment_id = shipment_id
        self.event = event
        self.origin_date = origin_date
        self.author = author
    
    def __repr__(self):
        return f"<Shipment Event {self.shipment_id} {self.event} {self.origin_date} {self.author}>"
    
    def to_dict(self):
        return {
            "shipment_id": self.shipment_id,
            "event": self.event,
            "origin_date": self.origin_date,
            "author": self.author,
        }
