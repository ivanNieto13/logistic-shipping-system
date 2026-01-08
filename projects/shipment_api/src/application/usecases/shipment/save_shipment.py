from typing import List
from uuid import UUID

from ....domain.repositories.shipment_repository import ShipmentRepository
from ....domain.entities.shipment import Shipment
from ....interfaces.schemas.shipment import SaveShipment

class SaveShipmentUseCase:
    def __init__(
        self,
        repository: ShipmentRepository,
    ):
        self._repository = repository
    
    def execute(self, shipment: SaveShipment) -> List[Shipment]:
        return self._repository.save(
            Shipment(
                id=shipment.id,
                origin_date=shipment.origin_date,
                total_amount=shipment.total_amount,
            )
        )
