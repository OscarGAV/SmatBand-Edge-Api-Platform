from typing import List
from pydantic import BaseModel
from core_context.interface.rest.dtos.heart_rate_history_item_dto import HeartRateHistoryItemDTO


class HeartRateHistoryResponseDTO(BaseModel):
    smart_band_id: int
    readings: List[HeartRateHistoryItemDTO]
    total: int