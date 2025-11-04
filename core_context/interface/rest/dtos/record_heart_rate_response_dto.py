from datetime import datetime
from uuid import UUID
from pydantic import BaseModel
from core_context.domain.model.value_objects.heart_rate_status import HeartRateStatus


class RecordHeartRateResponseDTO(BaseModel):
    id: UUID
    smart_band_id: int
    pulse: int
    status: HeartRateStatus
    timestamp: datetime
    message: str