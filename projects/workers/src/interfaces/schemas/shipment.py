
from pydantic import BaseModel
import datetime
from uuid import UUID


class SaveShipment(BaseModel):
    id: UUID
    origin_date: datetime.datetime
    total_amount: float