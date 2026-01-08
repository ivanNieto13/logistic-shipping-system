
from ....domain.entities.shipment import Shipment
from ....infrastructure.database.models.shipment import ShipmentModel
from ....domain.repositories.shipment_repository import ShipmentRepository

class ShipmentRepository(ShipmentRepository):
    def __init__(self, ):
        pass
    
    def _to_entity(self, model: ShipmentModel) -> Shipment:
        return Shipment(
            id=model.id,
            origin_date=model.origin_date,
            total_amount=model.total_amount,
        )
    
    def save(self, entity: Shipment) -> Shipment:
        model = ShipmentModel(
            id=entity.id,
            origin_date=entity.origin_date,
            total_amount=entity.total_amount,
        )
    
        return self._to_entity(model)
    
    
