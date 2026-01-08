from typing import List
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from .....application.services.notification_service import NotificationService
from .....application.usecases.shipment_event.create_many_shipment_event import CreateManyShipmentEventUseCase
from ....schemas.shipment_event import CreateShipmentEvent, CreateShipmentEventResponse
from ...dependencies import get_notification_service

router = APIRouter(prefix="/shipments-events", tags=["Shipment events"])

@router.post("/", status_code=200, response_model=CreateShipmentEventResponse)
async def create_many_shipments_events(
    shipment_event: List[CreateShipmentEvent],
    service: NotificationService = Depends(get_notification_service),
):
    """Create many shipment events"""
    use_case = CreateManyShipmentEventUseCase(service=service)
    acknowledge = await use_case.execute(shipment_event)
    
    return JSONResponse({"acknowledge": acknowledge })
    
