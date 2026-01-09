
import os
import uuid
from motor.core import AgnosticDatabase

from ....infrastructure.database.models.shipment_event import ShipmentEventModel
from ....domain.entities.shipment_event import ShipmentEvent
from ....domain.repositories.shipment_event_repository import ShipmentEventRepository


class ShipmentEventRepository(ShipmentEventRepository):
    def __init__(self, db: AgnosticDatabase):
        self._db = db[os.getenv("SHIPMENTS_EVENTS_COLLECTION_NAME", "shipment_events")]
    
    def _to_entity(self, model: ShipmentEventModel) -> ShipmentEvent:
        return ShipmentEvent(
            shipment_id=model.shipment_id,
            event=model.event,
            origin_date=model.origin_date,
            author=model.author,
        )
    
    async def save(self, entity: ShipmentEvent) -> ShipmentEvent:
        model = ShipmentEventModel(
            shipment_id=entity.shipment_id,
            event=entity.event,
            origin_date=entity.origin_date,
            author=entity.author,
        )
        
        await self._db.insert_one(model.model_dump())
        
        return entity
    
    async def find(self, entity: ShipmentEvent) -> ShipmentEvent | None:
        document = await self._db.find_one(
            {"shipment_id": uuid.UUID(entity.shipment_id)},
            sort=[('_id', -1)]
        )
        
        if document:
            return self._to_entity(ShipmentEventModel(**document))
        return None
    
    