# Smart Band Edge API Platform

Edge API Platform para dispositivo IoT ESP32 Smart Band con el objetivo de conformar un sistema de monitoreo de la frecuencia cardiaca en tiempo real

## Arquitectura

- DDD (Domain-Driven Design)
- CQRS (Command Query Responsibility Segregation)
- Arquitectura Hexagonal

### Estructura del Proyecto

```
SmatBand-Edge-Api-Platform/
├── core_context/
│   ├── domain/              # Entidades y lógica de dominio
│   ├── application/         # Casos de uso (Commands/Queries)
│   ├── infrastructure/      # Repositorios e implementaciones
│   └── interface/           # Controllers y DTOs
├── shared_context/
│   └── infrastructure/      # Configuración de BD
├── main.py                  # Punto de entrada
└── requirements.txt         # Dependencias
```

## Tecnologías

- FastAPI - Framework web asíncrono
- SQLAlchemy 2.0 - ORM con soporte async
- PostgreSQL - Base de datos (Supabase)
- Psycopg - Driver PostgreSQL async
- Pydantic - Validación de datos

## Requisitos

- Python 3.13
- PostgreSQL (Supabase)

## Instalación

```bash
# Clonar repositorio
git clone https://github.com/tu-usuario/SmatBand-Edge-Api-Platform.git
cd SmatBand-Edge-Api-Platform

# Instalar dependencias
pip install -r requirements.txt
```

## Ejecución Local

```bash
python main.py
```

La API estará disponible en:
- API: http://localhost:8000
- Documentación: http://localhost:8000/docs
- Health Check: http://localhost:8000/health

## Endpoints

### Health Monitoring

#### Registrar frecuencia cardíaca
```http
POST /api/v1/health-monitoring/data-records
Content-Type: application/json

{
  "smartBandId": 1,
  "pulse": 75
}
```

#### Obtener historial
```http
GET /api/v1/health-monitoring/data-records/{smart_band_id}/history?limit=10
```

#### Obtener estadísticas
```http
GET /api/v1/health-monitoring/data-records/{smart_band_id}/statistics
```

## Deployment en Azure

La api está desplegada en Azure App Service:

```
https://smart-band-edge-api-platform-grupo-uno.azurewebsites.net/docs
```

## Base de Datos

### Tabla: heart_rate_readings

| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | UUID | Identificador único |
| smart_band_id | INT | ID del dispositivo |
| pulse | INT | Frecuencia cardíaca |
| status | VARCHAR | Estado (NORMAL, LOW, HIGH, CRITICAL) |
| timestamp | TIMESTAMP | Fecha y hora del registro |
| created_at | TIMESTAMP | Fecha de creación |

## Lógica de Negocio

El sistema clasifica la frecuencia cardíaca automáticamente:

- LOW: menor a 60 bpm
- NORMAL: 60-100 bpm
- HIGH: 101-120 bpm
- CRITICAL: mayor a 120 bpm