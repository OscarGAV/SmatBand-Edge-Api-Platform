from typing import Dict, Optional, List
from uuid import UUID
from core_context.domain.model.aggregates.heart_rate_reading import HeartRateReading
from core_context.infrastructure.persistence.repositories.heart_rate_repository import IHeartRateRepository

# In-Memory Repository Implementation (Adapter)
class InMemoryHeartRateRepository(IHeartRateRepository):
    def __init__(self):
        self._storage: Dict[UUID, HeartRateReading] = {}

    async def save(self, reading: HeartRateReading) -> None:
        self._storage[reading.id] = reading

    async def find_by_id(self, heart_rate_id: UUID) -> Optional[HeartRateReading]:
        return self._storage.get(heart_rate_id)

    async def find_by_smart_band_id(self, smart_band_id: int, limit: int) -> List[HeartRateReading]:
        readings = [
            r for r in self._storage.values()
            if r.smart_band_id == smart_band_id
        ]
        readings.sort(key=lambda x: x.timestamp, reverse=True)
        return readings[:limit]