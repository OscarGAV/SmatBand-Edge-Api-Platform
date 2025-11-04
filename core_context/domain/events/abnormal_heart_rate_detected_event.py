from uuid import UUID
from core_context.domain.events.domain_event import DomainEvent
from core_context.domain.model.value_objects.heart_rate_status import HeartRateStatus


class AbnormalHeartRateDetectedEvent(DomainEvent):
    def __init__(self, reading_id: UUID, smart_band_id: int, pulse: int,
                 status: HeartRateStatus):
        super().__init__()
        self.reading_id = reading_id
        self.smart_band_id = smart_band_id
        self.pulse = pulse
        self.status = status