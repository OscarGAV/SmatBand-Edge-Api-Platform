from datetime import UTC
from typing import Optional, List
from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from core_context.domain.model.aggregates.heart_rate_reading import HeartRateReading
from core_context.domain.model.value_objects.heart_rate_status import HeartRateStatus
from core_context.infrastructure.persistence.repositories.heart_rate_repository import IHeartRateRepository
from shared_context.domain.model.heart_rate_reading_model import HeartRateReadingModel


class PostgreSQLHeartRateRepository(IHeartRateRepository):
    """PostgreSQL implementation of HeartRateRepository using SQLAlchemy"""

    def __init__(self, session: AsyncSession):
        self.session = session

    async def save(self, reading: HeartRateReading) -> None:
        """Save heart rate reading to PostgreSQL"""
        model = self._to_orm(reading)
        self.session.add(model)
        await self.session.commit()
        await self.session.refresh(model)

    async def find_by_id(self, heart_rate_id: UUID) -> Optional[HeartRateReading]:
        """Find reading by ID"""
        result = await self.session.execute(
            select(HeartRateReadingModel).where(HeartRateReadingModel.id == heart_rate_id)
        )
        model = result.scalar_one_or_none()
        return self._from_orm(model) if model else None

    async def find_by_smart_band_id(self, smart_band_id: int, limit: int) -> List[HeartRateReading]:
        """Find readings by smart band ID, ordered by timestamp DESC"""
        result = await self.session.execute(
            select(HeartRateReadingModel)
            .where(HeartRateReadingModel.smart_band_id == smart_band_id)
            .order_by(HeartRateReadingModel.timestamp.desc())
            .limit(limit)
        )
        models = result.scalars().all()
        return [self._from_orm(model) for model in models]

    @staticmethod
    def _from_orm(model: HeartRateReadingModel) -> HeartRateReading:
        """Convert SQLAlchemy model to Domain entity"""
        return HeartRateReading(
            heart_rate_id=model.id,
            smart_band_id=model.smart_band_id,
            pulse=model.pulse,
            timestamp=model.timestamp,
            status=HeartRateStatus(model.status)
        )

    @staticmethod
    def _to_orm(reading: HeartRateReading) -> HeartRateReadingModel:
        """Convert Domain entity to SQLAlchemy model"""
        from datetime import datetime
        return HeartRateReadingModel(
            id=reading.id,
            smart_band_id=reading.smart_band_id,
            pulse=reading.pulse,
            status=reading.status.value,
            timestamp=reading.timestamp,
            created_at=datetime.now(UTC)
        )