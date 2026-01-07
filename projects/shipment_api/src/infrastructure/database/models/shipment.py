from uuid import UUID
from pydantic import BaseModel
        
class ShipmentModel(BaseModel):
    id: UUID
    origin_date: float
    total_amount: float