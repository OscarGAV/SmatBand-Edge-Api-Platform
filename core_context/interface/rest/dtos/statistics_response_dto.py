from typing import Dict
from pydantic import BaseModel


class StatisticsResponseDTO(BaseModel):
    smart_band_id: int
    total_readings: int
    average_pulse: float
    min_pulse: int
    max_pulse: int
    abnormal_count: int
    status_distribution: Dict[str, int]