from typing import Optional
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core_context.application.internal.commandservices.record_heart_rate_command_handler import \
    RecordHeartRateCommandHandler
from core_context.application.internal.queryservices.heart_rate_query_handler import HeartRateQueryHandler
from core_context.infrastructure.event_bus import IEventBus
from core_context.infrastructure.in_memory_event_bus import InMemoryEventBus
from core_context.infrastructure.persistence.repositories.heart_rate_repository import IHeartRateRepository
from shared_context.infrastructure.persistence.repositories.postgresql_heart_rate_repository import \
    PostgreSQLHeartRateRepository
from shared_context.infrastructure.persistence.configuration.database_configuration import get_db_session


class Dependencies:
    """Dependency container for managing singleton instances"""
    _event_bus: Optional[IEventBus] = None
    _repository: Optional[IHeartRateRepository] = None

    @classmethod
    def get_event_bus(cls) -> IEventBus:
        if cls._event_bus is None:
            cls._event_bus = InMemoryEventBus()
        return cls._event_bus

    @classmethod
    def get_repository(cls) -> IHeartRateRepository:
        """Get the current repository instance (for backwards compatibility)"""
        return cls._repository


def get_repository(session: AsyncSession = Depends(get_db_session)) -> PostgreSQLHeartRateRepository:
    """Get PostgreSQL repository instance with injected session"""
    repo = PostgreSQLHeartRateRepository(session)
    Dependencies._repository = repo  # Store for later access
    return repo


def get_command_handler(
        repository: PostgreSQLHeartRateRepository = Depends(get_repository)
) -> RecordHeartRateCommandHandler:
    """Get command handler with injected dependencies"""
    return RecordHeartRateCommandHandler(
        repository=repository,
        event_bus=Dependencies.get_event_bus()
    )


def get_query_handler(
        repository: PostgreSQLHeartRateRepository = Depends(get_repository)
) -> HeartRateQueryHandler:
    """Get query handler with injected dependencies"""
    return HeartRateQueryHandler(repository=repository)