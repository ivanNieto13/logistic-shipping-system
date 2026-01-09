from pydantic import BaseModel
        
class DataAnalysisModel(BaseModel):
    total_shipments: int
    delivered_shipments: int