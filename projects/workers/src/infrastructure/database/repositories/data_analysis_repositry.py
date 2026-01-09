
import os
from motor.core import AgnosticDatabase

from ....domain.entities.data_analysis import DataAnalysis
from ....infrastructure.database.models.data_analysis import DataAnalysisModel
from ....domain.repositories.data_analysis_repository import DataAnalysisRepository

class DataAnalysisRepository(DataAnalysisRepository):
    def __init__(self, db: AgnosticDatabase):
        self._db = db[os.getenv("DATA_ANALYSIS_COLLECTION_NAME", "data_analysis")]
    
    def _to_entity(self, model: DataAnalysisModel) -> DataAnalysis:
        return DataAnalysis(
            delivered_shipments=model.delivered_shipments,
            total_shipments=model.total_shipments,
        )
    
    async def increase(self, entity: DataAnalysis) -> DataAnalysis:
        model = DataAnalysisModel(
            delivered_shipments=entity.delivered_shipments,
            total_shipments=entity.total_shipments,
        )
        
        await self._db.update_one(
            {},
            {"$inc": {
                "total_shipments": model.total_shipments, 
                "delivered_shipments": model.delivered_shipments,
            }},
            upsert=True
        )
        
        return entity
    