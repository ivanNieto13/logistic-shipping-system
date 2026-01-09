from typing import List
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from .....application.services.notification_service import NotificationService
from .....application.usecases.shipment.create_many_shipment import CreateManyShipmentUseCase
from ....schemas.shipment import CreateShipment, CreateShipmentResponse
from ...dependencies import get_notification_service

router = APIRouter(prefix="/shipments", tags=["Publishers"])

@router.post("/", status_code=200, response_model=CreateShipmentResponse)
async def create_many_shipments(
    shipments: List[CreateShipment],
    service: NotificationService = Depends(get_notification_service),
):
    """Create many shipments"""
    use_case = CreateManyShipmentUseCase(service=service)
    acknowledge = await use_case.execute(shipments)
    
    return JSONResponse({"acknowledge": acknowledge })
    
