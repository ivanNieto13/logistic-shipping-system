
import os
from motor.core import AgnosticDatabase
from ....domain.entities.shipment import Shipment
from ....infrastructure.database.models.shipment import ShipmentModel
from ....domain.repositories.shipment_repository import ShipmentRepository

class ShipmentRepository(ShipmentRepository):
    def __init__(self, db: AgnosticDatabase):
        self._db = db[os.getenv("SHIPMENTS_COLLECTION_NAME", "shipments_db")]
    
    def _to_entity(self, model: ShipmentModel) -> Shipment:
        return Shipment(
            id=model.id,
            origin_date=model.origin_date,
            total_amount=model.total_amount,
        )
    
    async def save(self, entity: Shipment) -> Shipment:
        model = ShipmentModel(
            id=entity.id,
            origin_date=entity.origin_date,
            total_amount=entity.total_amount,
        )
        
        await self._db.update_one(
            {"id": entity.id}, 
            {"$set": model.model_dump()}, 
            upsert=True
        )
        
        return entity
    
    
