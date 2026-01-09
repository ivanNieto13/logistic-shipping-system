from typing import List
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from .....domain.repositories.shipment_event_repository import ShipmentEventRepository
from .....domain.repositories.shipment_repository import ShipmentRepository
from .....application.services.notification_service import NotificationService
from .....application.usecases.shipment_event.create_many_shipment_event import CreateManyShipmentEventUseCase
from ....schemas.shipment_event import CreateShipmentEvent, CreateShipmentEventResponse
from ...dependencies import get_notification_service, get_shipment_event_repository_db, get_shipment_repository_db

router = APIRouter(prefix="/shipments-events", tags=["Publishers"])

@router.post("/", status_code=200, response_model=CreateShipmentEventResponse)
async def create_many_shipments_events(
    shipment_event: List[CreateShipmentEvent],
    service: NotificationService = Depends(get_notification_service),
    shipment_repo: ShipmentRepository = Depends(get_shipment_repository_db),
    shipment_event_repo: ShipmentEventRepository = Depends(get_shipment_event_repository_db)
):
    """Create many shipment events"""
    use_case = CreateManyShipmentEventUseCase(
        service=service, 
        shipment_repository=shipment_repo, 
        shipment_event_repository=shipment_event_repo,
    )
    acknowledge = await use_case.execute(shipment_event)
    
    return JSONResponse({"acknowledge": acknowledge })
    
