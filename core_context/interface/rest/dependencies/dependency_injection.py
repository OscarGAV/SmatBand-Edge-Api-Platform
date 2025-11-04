from typing import Optional
from core_context.application.internal.commandservices.record_heart_rate_command_handler import \
    RecordHeartRateCommandHandler
from core_context.application.internal.queryservices.heart_rate_query_handler import HeartRateQueryHandler
from core_context.infrastructure.event_bus import IEventBus
from core_context.infrastructure.in_memory_event_bus import InMemoryEventBus
from core_context.infrastructure.persistence.repositories.heart_rate_repository import IHeartRateRepository
from core_context.infrastructure.persistence.repositories.in_memory_heart_rate_repository import \
    InMemoryHeartRateRepository


class Dependencies:
    _repository: Optional[IHeartRateRepository] = None
    _event_bus: Optional[IEventBus] = None

    @classmethod
    def get_repository(cls) -> IHeartRateRepository:
        if cls._repository is None:
            cls._repository = InMemoryHeartRateRepository()
        return cls._repository

    @classmethod
    def get_event_bus(cls) -> IEventBus:
        if cls._event_bus is None:
            cls._event_bus = InMemoryEventBus()
        return cls._event_bus


def get_command_handler() -> RecordHeartRateCommandHandler:
    return RecordHeartRateCommandHandler(
        repository=Dependencies.get_repository(),
        event_bus=Dependencies.get_event_bus()
    )


def get_query_handler() -> HeartRateQueryHandler:
    return HeartRateQueryHandler(
        repository=Dependencies.get_repository()
    )
