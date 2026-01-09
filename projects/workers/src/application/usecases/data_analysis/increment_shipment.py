
from ....domain.entities.data_analysis import DataAnalysis
from ....interfaces.schemas.shipment_event import CreateShipmentEvent, ShipmentEventType
from ....domain.repositories.data_analysis_repository import DataAnalysisRepository


class IncrementShipmentUseCase:
    def __init__(
        self,
        data_analysis_repository: DataAnalysisRepository,
    ):
        self._data_analysis_repository = data_analysis_repository

    async def execute(self, shipment_event: CreateShipmentEvent) -> None:
        delivered_shipments = 0
        
        if shipment_event.event == ShipmentEventType.COMPLETED:
            delivered_shipments = 1
        
        return await self._data_analysis_repository.increase(
                DataAnalysis(
                    total_shipments=1,
                    delivered_shipments=delivered_shipments,
                )
            )
        
        
        