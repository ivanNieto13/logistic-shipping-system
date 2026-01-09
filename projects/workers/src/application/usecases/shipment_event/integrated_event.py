
from ....interfaces.schemas.shipment_event import ShipmentEventType
from ....domain.entities.shipment_event import ShipmentEvent
from ....interfaces.schemas.shipment_event import CreateShipmentEvent
from ....domain.repositories.shipment_repository import ShipmentRepository
from ....domain.repositories.shipment_event_repository import ShipmentEventRepository
from ....domain.entities.shipment import Shipment


class IntegratedEventUseCase:
    def __init__(
        self,
        shipment_repository: ShipmentRepository,
        shipment_event_repository: ShipmentEventRepository,
    ):
        self._shipment_repository = shipment_repository
        self._shipment_event_repository = shipment_event_repository
        
    def _map_event(event: ShipmentEventType) -> int:
        match event:
            case ShipmentEventType.INTEGRATED:
                return 1
            case ShipmentEventType.ON_ROUTE:
                return 2
            case ShipmentEventType.TRANSPORT_ARRIVAL:
                return 3
            case ShipmentEventType.COMPLETED | ShipmentEventType.REJECTED:
                return 4
            case _:
                pass
        
    
    async def execute(self, shipment_event: CreateShipmentEvent) -> None:
        found_existent_shipment: Shipment | None = await self._shipment_repository.find(
            Shipment(
                id=shipment_event.shipment_id,
            )
        )
        
        if not found_existent_shipment:
            print("not found_existent_shipment")
            return
        
        found_existent_shipment_event: ShipmentEvent | None = await self._shipment_event_repository.find(
            ShipmentEvent(
                shipment_id=shipment_event.shipment_id
            )
        )
        
        if not found_existent_shipment_event and shipment_event.event == ShipmentEventType.INTEGRATED:
            print("create new shipment event of integrated type")
            return await self._shipment_event_repository.save(
                ShipmentEvent(
                    shipment_id=shipment_event.shipment_id,
                    event=shipment_event.event,
                    origin_date=shipment_event.origin_date,
                    author=shipment_event.author,
                )
            )
        
        ponderated_existent_event = self._map_event(found_existent_shipment_event.event)
        ponderated_current_event = self._map_event(shipment_event.event)
        
        if ponderated_existent_event < ponderated_current_event:
            print("update existent event")
            return await self._shipment_event_repository.save(
                ShipmentEvent(
                    shipment_id=shipment_event.shipment_id,
                    event=shipment_event.event,
                    origin_date=shipment_event.origin_date,
                    author=shipment_event.author,
                )
            )
        
        
        