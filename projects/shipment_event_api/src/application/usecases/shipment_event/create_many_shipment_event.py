import os
from typing import List

from ....domain.entities.shipment_event import ShipmentEvent
from ....interfaces.schemas.shipment_event import CreateShipmentEvent, ShipmentEventType
from ...services.notification_service import NotificationService

class CreateManyShipmentEventUseCase:
    def __init__(
        self,
        service: NotificationService
    ):
        self._service = service
        
    async def _send_notification(self, channel: str, shipment_event: CreateShipmentEvent):
        await self._service.send_notification(
            channel=channel, 
            data=ShipmentEvent(
                shipment_id=shipment_event.shipment_id, 
                event=shipment_event.event,
                origin_date=shipment_event.origin_date,
                author=shipment_event.author,
        ).to_dict())
     
    async def execute(self, shipment_events: List[CreateShipmentEvent]) -> bool:
        for shipment_event in shipment_events:
            shipment_event_channel = os.getenv("SHIPMENT_EVENT_CHANNEL", "shipment_event")
        
            await self._send_notification(shipment_event_channel, shipment_event)
            
            if shipment_event.event == ShipmentEventType.COMPLETED or shipment_event.event == ShipmentEventType.REJECTED:
                shipment_final_event = os.getenv("SHIPMENT_FINAL_EVENT_CHANNEL", "shipment_final_event")
                await self._send_notification(shipment_final_event, shipment_event)
        return True
