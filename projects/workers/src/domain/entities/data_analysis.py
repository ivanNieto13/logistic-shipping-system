from dataclasses import dataclass

@dataclass
class DataAnalysis:
    def __init__(
        self,
        total_shipments: int,
        delivered_shipments: int,
    ):
        self.total_shipments = total_shipments
        self.delivered_shipments = delivered_shipments
        
    def __repr__(self):
        return f"<DataAnalysis {self.total_shipments} {self.delivered_shipments}>"
    
    def to_dict(self):
        return {
            "total_shipments": self.total_shipments,
            "delivered_shipments": self.delivered_shipments,
        }
