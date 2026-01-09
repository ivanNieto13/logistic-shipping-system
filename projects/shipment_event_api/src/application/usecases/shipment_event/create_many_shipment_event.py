import os
from typing import List
from ....interfaces.schemas.shipment_event import ShipmentEventType
from ....domain.entities.shipment_event import ShipmentEvent
from ....interfaces.schemas.shipment_event import CreateShipmentEvent
from ....domain.repositories.shipment_repository import ShipmentRepository
from ....domain.repositories.shipment_event_repository import ShipmentEventRepository
from ....domain.entities.shipment import Shipment
from ...services.notification_service import NotificationService

class CreateManyShipmentEventUseCase:
    def __init__(
        self,
        shipment_repository: ShipmentRepository,
        shipment_event_repository: ShipmentEventRepository,
        service: NotificationService,
    ):
        self._shipment_repository = shipment_repository
        self._shipment_event_repository = shipment_event_repository
        self._service = service
        self._final_event = 4
        
    def _map_event(self, event: ShipmentEventType) -> int:
        match event:
            case ShipmentEventType.INTEGRATED:
                return 1
            case ShipmentEventType.ON_ROUTE:
                return 2
            case ShipmentEventType.TRANSPORT_ARRIVAL:
                return 3
            case ShipmentEventType.COMPLETED | ShipmentEventType.REJECTED:
                return self._final_event
            case _:
                pass
    
    async def _send_notification(self, channel: str, shipment_event: CreateShipmentEvent):
        await self._service.send_notification(
            channel=channel, 
            data=ShipmentEvent(
                shipment_id=shipment_event.shipment_id, 
                event=shipment_event.event,
                origin_date=shipment_event.origin_date,
                author=shipment_event.author,
        ).to_dict())
        
    
    async def execute(self, shipment_events: List[CreateShipmentEvent]) -> None:
        for shipment_event in shipment_events:
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
                    shipment_id=shipment_event.shipment_id,
                )
            )
            
            shipment_event_channel = os.getenv("SHIPMENT_EVENT_CHANNEL", "shipment_event")
        
            if not found_existent_shipment_event and shipment_event.event == ShipmentEventType.INTEGRATED:
                print("create new shipment event of integrated type")
                await self._send_notification(shipment_event_channel, shipment_event)

                return
            
            ponderated_existent_event = self._map_event(found_existent_shipment_event.event)
            ponderated_current_event = self._map_event(shipment_event.event)
            
            allowed_update = ponderated_existent_event < ponderated_current_event
            print(f"allowed_update: {allowed_update}")
            
            if allowed_update:
                print(f"update existent event from {found_existent_shipment_event.event} to {shipment_event.event}")
                await self._send_notification(shipment_event_channel, shipment_event)

                if ponderated_current_event == self._final_event:
                    shipment_final_event = os.getenv("SHIPMENT_FINAL_EVENT_CHANNEL", "shipment_final_event")
                    await self._send_notification(shipment_final_event, shipment_event)

                return
        
        
        