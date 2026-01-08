import os
from typing import List

from ....domain.entities.shipment import Shipment
from ....application.services.notification_service import NotificationService
from ....interfaces.schemas.shipment import CreateShipment

class CreateManyShipmentUseCase:
    def __init__(
        self,
        service: NotificationService
    ):
        self._service = service
    
    async def execute(self, shipments: List[CreateShipment]) -> bool:
        for shipment in shipments:
            await self._service.send_notification(
                channel=os.getenv("CREATE_SHIPMENT_CHANNEL", "shipment"), 
                data=Shipment(
                    id=shipment.id, 
                    origin_date=shipment.origin_date, 
                    total_amount=shipment.total_amount
                ).to_dict())
        return True
