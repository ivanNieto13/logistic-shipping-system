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
     
    async def execute(self, shipment_events: List[CreateShipmentEvent]) -> bool:
        for event in shipment_events:
            channel: str
            match event.event:
                case ShipmentEventType.INTEGRATED:
                    channel = os.getenv("SHIPMENT_INTEGRATED_EVENT_CHANNEL", "shipment_integrated_event")
                case ShipmentEventType.ON_ROUTE:
                    channel = os.getenv("SHIPMENT_ON_ROUTE_EVENT_CHANNEL", "shipment_on_route_event")
                case ShipmentEventType.TRANSPORT_ARRIVAL:
                    channel = os.getenv("SHIPMENT_TRANSPORT_ARRIVAL_EVENT_CHANNEL", "shipment_transport_arrival_event")
                case ShipmentEventType.COMPLETED | ShipmentEventType.REJECTED:
                    channel = os.getenv("SHIPMENT_FINAL_EVENT_CHANNEL", "shipment_final_event")
                case _:
                    pass
            
            await self._service.send_notification(
                channel=channel, 
                data=ShipmentEvent(
                    shipment_id=event.shipment_id, 
                    event=event.event,
                    origin_date=event.origin_date,
                    author=event.author,
                ).to_dict())
        return True
