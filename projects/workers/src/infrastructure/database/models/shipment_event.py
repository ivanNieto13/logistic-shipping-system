import datetime
from uuid import UUID
from pydantic import BaseModel

from ....interfaces.schemas.shipment_event import ShipmentEventType
        
class ShipmentEventModel(BaseModel):
    shipment_id: UUID
    event: ShipmentEventType
    origin_date: datetime.datetime
    author: str