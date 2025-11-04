import uvicorn
from core_context.interface.rest.controllers.heart_rate_controller import app


if __name__ == "__main__":
    print("""
    ╔════════════════════════════════════════════════════════════╗
    ║  Smart Band Edge Service - CQRS/DDD Architecture           ║
    ║  FastAPI Backend for ESP32 IoT Device                      ║
    ╚════════════════════════════════════════════════════════════╝

    Architecture Layers:
    ✓ Domain Layer: Entities, Value Objects, Domain Events
    ✓ Application Layer: Commands, Queries, Handlers (CQRS)
    ✓ Infrastructure Layer: Repositories, Event Bus
    ✓ API Layer: HTTP Controllers, DTOs

    Endpoints:
    • POST /api/v1/health-monitoring/data-records
    • GET  /api/v1/health-monitoring/data-records/{id}/history
    • GET  /api/v1/health-monitoring/data-records/{id}/statistics
    • GET  /health

    Starting server on http://localhost:8000
    Documentation: http://localhost:8000/docs
    """)

    uvicorn.run(app, host="0.0.0.0", port=8000)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
