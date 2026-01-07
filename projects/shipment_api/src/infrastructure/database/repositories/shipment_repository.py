from typing import List

from ....domain.entities.shipment import Shipment
from ....infrastructure.database.models.shipment import ShipmentModel
from ....domain.repositories.shipment_repository import IShipmentRepository

class ShipmentRepository(IShipmentRepository):
    def __init__(self, ):
        pass
    
    def _to_entity(self, model: ShipmentModel) -> Shipment:
        return Shipment(
            id=model.id,
            name=model.name,
            price=model.price,
            stock=model.stock,
            is_active=model.is_active,
            description=model.description,
            created_at=model.created_at
        )
    
    async def create(self, entities: List[Shipment]) -> Shipment:
        models: List[ShipmentModel] = []
        for entity in entities:
            models.append(ShipmentModel(
            id=entity.id,
            origin_date=entity.origin_date,
            total_amount=entity.total_amount,
        ))
        
        return self._to_entity(models)
    
    
