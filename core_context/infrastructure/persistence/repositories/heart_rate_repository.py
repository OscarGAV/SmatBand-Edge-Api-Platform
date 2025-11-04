from abc import abstractmethod, ABC
from typing import Optional, List
from uuid import UUID
from core_context.domain.model.aggregates.heart_rate_reading import HeartRateReading

# Repository Interface
class IHeartRateRepository(ABC):
    @abstractmethod
    async def save(self, reading: HeartRateReading) -> None:
        pass

    @abstractmethod
    async def find_by_id(self, heart_rate_id: UUID) -> Optional[HeartRateReading]:
        pass

    @abstractmethod
    async def find_by_smart_band_id(self, smart_band_id: int, limit: int) -> List[HeartRateReading]:
        pass