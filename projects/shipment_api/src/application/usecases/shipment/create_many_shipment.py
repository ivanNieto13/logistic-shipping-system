from typing import List

from ....interfaces.schemas.shipment import CreateShipment
from ....domain.entities.shipment import Shipment
from ....domain.repositories.shipment_repository import IShipmentRepository

class CreateManyShipmentUseCase:
    def __init__(self, repository: IShipmentRepository):
        self._repository = repository
    
    async def execute(self, shipments: List[CreateShipment], ) -> bool:
        entities: List[Shipment] = []
        for shipment in shipments:
            entities.append(Shipment(id=shipment.id, origin_date=shipment.origin_date, total_amount=shipment.total_amount))        
        await self._repository.create_many(self, entity=entities)
        return True
