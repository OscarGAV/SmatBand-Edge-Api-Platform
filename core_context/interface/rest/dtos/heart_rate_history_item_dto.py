from datetime import datetime
from uuid import UUID
from pydantic import BaseModel
from core_context.domain.model.value_objects.heart_rate_status import HeartRateStatus


class HeartRateHistoryItemDTO(BaseModel):
    id: UUID
    pulse: int
    status: HeartRateStatus
    timestamp: datetime