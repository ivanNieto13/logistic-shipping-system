
from pydantic import BaseModel, Field
import datetime
from uuid import UUID

class CreateShipment(BaseModel):
    id: UUID | str = Field(default=UUID, description="Shipment unique id. Must be UUID format.")
    origin_date: datetime.datetime | str = Field(default=datetime.datetime, description="Shipment origin date. Must be ISO 8601 format.")
    total_amount: float = Field(gt=0, description="Shipment total amount. Must be greater than zero.")
    

class CreateShipmentResponse(BaseModel):
    acknowledge: bool = Field()
    