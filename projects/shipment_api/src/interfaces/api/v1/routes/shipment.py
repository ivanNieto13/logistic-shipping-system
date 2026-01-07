from typing import List
from fastapi import APIRouter
from fastapi.responses import JSONResponse

from .....infrastructure.database.repositories.shipment_repository import ShipmentRepository
from .....application.usecases.shipment.create_many_shipment import CreateManyShipmentUseCase
from ....schemas.shipment import CreateShipment, CreateShipmentResponse

router = APIRouter(prefix="/shipments", tags=["Shipments"])

@router.post("/", status_code=200, response_model=CreateShipmentResponse)
async def create_many_shipments(
    shipments: List[CreateShipment],
):
    """Create many shipments"""
    use_case = CreateManyShipmentUseCase(repository=ShipmentRepository)
    acknowledge = await use_case.execute(shipments)
    
    return JSONResponse({"acknowledge": acknowledge })
    
