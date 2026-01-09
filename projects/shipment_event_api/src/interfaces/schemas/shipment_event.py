import datetime
from enum import Enum
from pydantic import BaseModel, Field
from uuid import UUID

class ShipmentEventType(str, Enum):
    INTEGRATED = "INTEGRATED"
    ON_ROUTE = "ON_ROUTE"
    TRANSPORT_ARRIVAL = "TRANSPORT_ARRIVAL"
    COMPLETED = "COMPLETED"
    REJECTED = "REJECTED"

class CreateShipmentEvent(BaseModel):
    shipment_id: UUID | str = Field(description="Shipment unique id. Must be UUID format.")
    event: ShipmentEventType | str = Field(examples=[ShipmentEventType.INTEGRATED], description="Shipment event.")
    origin_date: datetime.datetime | str = Field(default=datetime.datetime, description="Shipment origin date. Must be ISO 8601 format.")
    author: str = Field(min_length=1, max_length=50, description="Shipment event author.")
    

class CreateShipmentEventResponse(BaseModel):
    acknowledge: bool = Field()
    