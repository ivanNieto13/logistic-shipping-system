import datetime
from uuid import UUID
from pydantic import BaseModel
        
class ShipmentModel(BaseModel):
    id: UUID
    origin_date: datetime.datetime
    total_amount: float