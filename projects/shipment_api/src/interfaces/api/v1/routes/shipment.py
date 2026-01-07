from typing import List
from fastapi import APIRouter
from ....schemas.shipment import CreateShipment

router = APIRouter(tags=["Shipments"])

@router.post("/shipments")
async def create_many_shipments(
    shipments: List[CreateShipment]
):
    """Create many shipments"""
    return shipments
