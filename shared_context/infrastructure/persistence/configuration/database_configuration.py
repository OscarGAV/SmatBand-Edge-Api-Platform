from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from typing import AsyncGenerator

# Supabase Connection
DATABASE_URL = "postgresql+psycopg://postgres.mpdqijbgwifdmceojbok:smart_band_db@aws-1-us-east-1.pooler.supabase.com:6543/postgres"

# Create async engine with connection pooling for Supabase
engine = create_async_engine(
    DATABASE_URL,
    echo=False,  # Set to True for SQL query logging
    pool_size=10,
    max_overflow=20,
    pool_pre_ping=True,  # Verify connections before using
    pool_recycle=3600,  # Recycle connections after 1 hour
)

# Create async session factory
async_session_maker = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    """Dependency for getting database session"""
    async with async_session_maker() as session:
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()


async def init_db():
    """Initialize database tables (creates if not exist)"""
    from shared_context.domain.model.heart_rate_reading_model import Base

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        print("✓ Database tables created successfully")


async def close_db():
    """Close database connections"""
    await engine.dispose()
    print("✓ Database connections closed")