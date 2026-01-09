import datetime
from uuid import UUID
from pydantic import BaseModel
        
class ShipmentModel(BaseModel):
    id: UUID | None
    origin_date: datetime.datetime | None
    total_amount: float | None