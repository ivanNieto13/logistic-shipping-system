from abc import ABC, abstractmethod

from ..entities.data_analysis import DataAnalysis

class DataAnalysisRepository(ABC):   
    @abstractmethod
    def increase(self, entity: DataAnalysis) -> DataAnalysis:
        pass
    
