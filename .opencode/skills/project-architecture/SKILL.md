---
name: project-architecture
description: Explica la arquitectura, estructura de carpetas y convenciones del proyecto. Usar cuando el usuario pregunte sobre organización, estructura, arquitectura o antes de crear/mover archivos.
---

# Arquitectura del proyecto

Arquitectura limpia (Clean Architecture) con separación de capas y principios SOLID. La lógica de negocio permanece independiente de frameworks e infraestructura.

## Convenciones

Para reglas de nomenclatura y organización, consulta [conventions.md](conventions.md).

## Estructura de carpetas

```
server/src/app/
├── main.py                 # entry point
├── domain/                 # business logic (no external deps)
│   ├── entities/
│   ├── value_objects/
│   └── exceptions/
├── application/            # use cases orchestrate business
│   ├── use_cases/
│   ├── interfaces/         # contracts implemented by infrastructure
│   │   ├── repositories/
│   │   └── services/
│   └── dto/
├── infrastructure/         # concrete implementations
│   ├── database/
│   │   ├── models/         # SQLAlchemy models
│   │   └── repositories/   # implements application interfaces
│   ├── external_services/
│   └── security/
├── presentation/           # HTTP layer (FastAPI)
│   ├── api/routes/
│   ├── schemas/            # Pydantic request/response
│   ├── dependencies/       # FastAPI Depends()
│   └── error_handlers.py
├── core/                   # cross-cutting config
│   ├── config.py           # settings (env vars)
│   ├── container.py        # DI container
│   └── logging.py
└── workers/                # background tasks
```

## Al revisar código existente

Verifica que el archivo esté en la carpeta correcta y cumpla las convenciones. Revisa que respete separación de responsabilidades, inyección de dependencias y uso de interfaces entre capas.
