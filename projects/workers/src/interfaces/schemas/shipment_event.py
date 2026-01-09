import datetime
from enum import Enum
from uuid import UUID
from pydantic import BaseModel


class ShipmentEventType(str, Enum):
    INTEGRATED = "INTEGRATED"
    ON_ROUTE = "ON_ROUTE"
    TRANSPORT_ARRIVAL = "TRANSPORT_ARRIVAL"
    COMPLETED = "COMPLETED"
    REJECTED = "REJECTED"
    
class CreateShipmentEvent(BaseModel):
    shipment_id: UUID
    event: ShipmentEventType
    origin_date: datetime.datetime
    author: str