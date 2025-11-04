from typing import List, Dict, Any
from core_context.domain.model.aggregates.heart_rate_reading import HeartRateReading
from core_context.domain.model.queries.get_heart_rate_history_query import GetHeartRateHistoryQuery
from core_context.domain.model.queries.get_heart_rate_statistics_query import GetHeartRateStatisticsQuery
from core_context.domain.model.value_objects.heart_rate_status import HeartRateStatus


class HeartRateQueryHandler:
    """Handler for heart rate queries"""

    def __init__(self, repository: 'IHeartRateRepository'):
        self.repository = repository

    async def get_history(self, query: GetHeartRateHistoryQuery) -> List[HeartRateReading]:
        return await self.repository.find_by_smart_band_id(
            query.smart_band_id,
            query.limit
        )

    async def get_statistics(self, query: GetHeartRateStatisticsQuery) -> Dict[str, Any]:
        readings = await self.repository.find_by_smart_band_id(
            query.smart_band_id,
            limit=100
        )

        if not readings:
            return {
                "smart_band_id": query.smart_band_id,
                "total_readings": 0,
                "average_pulse": 0,
                "min_pulse": 0,
                "max_pulse": 0,
                "abnormal_count": 0
            }

        pulses = [r.pulse for r in readings]
        abnormal_count = sum(1 for r in readings if r.status != HeartRateStatus.NORMAL)

        return {
            "smart_band_id": query.smart_band_id,
            "total_readings": len(readings),
            "average_pulse": sum(pulses) / len(pulses),
            "min_pulse": min(pulses),
            "max_pulse": max(pulses),
            "abnormal_count": abnormal_count,
            "status_distribution": {
                status.value: sum(1 for r in readings if r.status == status)
                for status in HeartRateStatus
            }
        }