from uuid import UUID

class Shipment:
    def __init__(
        self,
        id: UUID | str,
        origin_date: float,
        total_amount: float,
    ):
        self.id = id
        self.origin_date = origin_date
        self.total_amount = total_amount
    
    def __repr__(self):
        return f"<Shipment {self.id} {self.origin_date} {self.total_amount}>"
