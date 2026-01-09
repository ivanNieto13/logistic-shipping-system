from dataclasses import dataclass
import datetime
from uuid import UUID

@dataclass
class Shipment:
    def __init__(
        self,
        id: UUID,
        origin_date: datetime.datetime | None = None,
        total_amount: float | None = None,
    ):
        self.id = id
        self.origin_date = origin_date
        self.total_amount = total_amount
    
    def __repr__(self):
        return f"<Shipment {self.id} {self.origin_date} {self.total_amount}>"
    
    def to_dict(self):
        return {"id": self.id, "origin_date": self.origin_date, "total_amount": self.total_amount}
