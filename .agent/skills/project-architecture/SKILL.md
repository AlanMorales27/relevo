---
name: project-architecture
description: Explica la arquitectura, estructura de carpetas y convenciones del proyecto.
Usar cuando el usuario pregunte "cómo está organizado el proyecto", "dónde va este archivo",
"cuál es la arquitectura", "cómo se conectan estos módulos", antes de crear/mover archivos, o
al revisar código existente para asegurar que respeten la estructura existente.
---

# Arquitectura del proyecto        
Arquitectura limpia (Clean Architecture) con separación de capas y principios SOLID. La idea es mantener la lógica de negocio independiente de frameworks, librerías o detalles de infraestructura, permitiendo que la aplicación sea más mantenible, testeable y escalable.          

## Estructura de carpetas
relevo/server/
├── src/
│   └── app/
│       ├── main.py                      # punto de entrada, arma la app

│       ├── domain/                      # lógica de negocio pura, sin dependencias externas
│       │   ├── entities/                # entidades del dominio
│       │   ├── value_objects/           # enums y tipos de datos específicos del dominio
│       │   └── exceptions/
│       │
│       ├── application/                 
│       │   ├── use_cases/               # casos de uso (orquestan el negocio)
│       │   ├── interfaces/              # contratos (puertos) que implementa infraestructura
│       │   │   ├── repositories/
│       │   │   └── services/
│       │   └── dto/                     # objetos de transferencia entre capas
│       │
│       ├── infrastructure/              # implementaciones concretas
│       │   ├── database/                
│       │   │   ├── models/              # modelos SQLAlchemy
│       │   │   ├── repositories/        # implementación de los contratos de la capa de aplicación
│       │   ├── external_services/
│       │   └── security/
│       │
│       ├── presentation/                # capa HTTP (FastAPI)
│       │   ├── api/
│       │   │   ├── routes/
│       │   │   ├── router.py            # agrupa todos los routers
│       │   ├── schemas/                 # Pydantic (request/response)
│       │   ├── dependencies/            # Depends() de FastAPI (auth, DB session, etc.)
│       │   └── error_handlers.py
│       │
│       ├── core/                        # configuración transversal
│       │   ├── config.py                # settings (env vars)
│       │   ├── container.py             # inyección de dependencias (DI container)
│       │   └── logging.py
│       │
│       └── workers/                     # tareas en background
│
├── tests/
│   ├── unit/                            # tests de domain + application (sin infraestructura real)
│   ├── integration/                     # tests con DB/servicios reales o mockeados
│                  
├── alembic/                             # migraciones de base de datos
└── scripts/      

## Al revisar código existente
Verifica que el archivo esté en la carpeta correcta y si cumple con las convenciones según estas reglas.
Adicionalmente, revisa que el código cumpla con los principios de arquitectura limpia, como separación de responsabilidades, inyección de dependencias y uso de interfaces para desacoplar las capas.