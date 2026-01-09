
from ....domain.entities.shipment_event import ShipmentEvent
from ....interfaces.schemas.shipment_event import CreateShipmentEvent
from ....domain.repositories.shipment_event_repository import ShipmentEventRepository


class IntegratedEventUseCase:
    def __init__(
        self,
        shipment_event_repository: ShipmentEventRepository,
    ):
        self._shipment_event_repository = shipment_event_repository

    async def execute(self, shipment_event: CreateShipmentEvent) -> None:
        return await self._shipment_event_repository.save(
                ShipmentEvent(
                    shipment_id=shipment_event.shipment_id,
                    event=shipment_event.event,
                    origin_date=shipment_event.origin_date,
                    author=shipment_event.author,
                )
            )
        
        
        