from datetime import datetime, UTC
from uuid import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Integer, DateTime, Index
from sqlalchemy.dialects.postgresql import UUID as SQL_UUID


class Base(DeclarativeBase):
    """Base class for all ORM models"""
    pass


class HeartRateReadingModel(Base):
    """SQLAlchemy ORM Model for heart_rate_readings table"""
    __tablename__ = "heart_rate_readings"

    id: Mapped[UUID] = mapped_column(
        SQL_UUID(as_uuid=True),
        primary_key=True
    )

    smart_band_id: Mapped[int] = mapped_column(Integer, nullable=False, index=True)

    pulse: Mapped[int] = mapped_column(Integer, nullable=False)

    status: Mapped[str] = mapped_column(String(20), nullable=False, index=True)

    timestamp: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        index=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        default=datetime.now(UTC)
    )

    # Composite indexes for query optimization
    __table_args__ = (
        Index('idx_smart_band_timestamp', 'smart_band_id', 'timestamp'),
        Index('idx_status_timestamp', 'status', 'timestamp'),
    )