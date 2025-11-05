import asyncio
import sys
import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI
from shared_context.infrastructure.persistence.configuration.database_configuration import init_db, close_db

# Fix for Windows + psycopg async mode
if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifecycle: startup and shutdown"""
    # Startup
    print("\n" + "=" * 60)
    print("Starting Smart Band Edge Service")
    print("=" * 60)
    await init_db()
    print("Connected to PostgreSQL (Supabase)")
    print("Server ready to accept connections")
    print("=" * 60 + "\n")

    yield

    # Shutdown
    print("\n" + "=" * 60)
    print("Shutting down Smart Band Edge Service")
    await close_db()
    print("=" * 60 + "\n")


# Import after event loop policy is set
from core_context.interface.rest.controllers.heart_rate_controller import create_app

# Create app with lifespan
app = create_app(lifespan)

if __name__ == "__main__":
    print("""
    ═══════════════════════════════════════════════════════════════════════
    Smart Band Edge Service - Hexagonal Architecture with DDD and CQRS       
    FastAPI Backend for ESP32 IoT Device                      
    ═══════════════════════════════════════════════════════════════════════

    Architecture Layers:
    ✓ Domain Layer: Entities, Value Objects, Domain Events
    ✓ Application Layer: Commands, Queries, Handlers
    ✓ Infrastructure Layer: PostgreSQL + SQLAlchemy
    ✓ API Layer: HTTP Controllers, DTOs

    Database:
    • PostgreSQL (Supabase)
    • SQLAlchemy 2.0 ORM
    • Connection Pooling: 10-30 connections

    Endpoints:
    • POST /api/v1/health-monitoring/data-records
    • GET  /api/v1/health-monitoring/data-records/{id}/history
    • GET  /api/v1/health-monitoring/data-records/{id}/statistics
    • GET  /health

    Starting server on http://localhost:8000
    Documentation: http://localhost:8000/docs
    """)

    uvicorn.run(app, host="0.0.0.0", port=8000)