# Convenciones del proyecto

Este documento define las convenciones de organización y nomenclatura que deben seguirse al crear o modificar archivos del proyecto. Su propósito es mantener la estructura consistente, facilitar el mantenimiento del código y alinearse con la arquitectura establecida.

## Convenciones de nombres de archivos
- Los nombres deben escribirse en minúsculas y, cuando sea necesario, separar palabras con guiones bajos.
- El nombre del archivo debe reflejar de forma clara la responsabilidad que cumple dentro del módulo.

### Sufijos por tipo de archivo
- **Rutas**: `*_routes.py` (ej: `auth_routes.py`, `health_routes.py`)
- **Modelos de BD**: `*_model.py` (ej: `user_model.py`, `product_model.py`)
- **Schemas Pydantic**: `*_schemas.py` (ej: `auth_schemas.py`, `user_schemas.py`)
- **Entidades de dominio**: sin sufijo (ej: `user.py`, `product.py`)
- **Excepciones de dominio**: `*_error.py` (ej: `user_not_found_error.py`)
- **Interfaces**: prefijo `i_` (ej: `i_password_hasher.py`, `i_user_repository.py`)

## Convenciones de nomenclatura general
- Todos los nombres del proyecto deben escribirse en inglés, incluyendo archivos, carpetas, variables, constantes, funciones, clases, métodos, enums, interfaces y demás símbolos.
- Se debe preferir nomenclatura descriptiva y clara, evitando abreviaturas poco intuitivas.
- Para nombres compuestos, se recomienda usar `snake_case` para funciones, variables y archivos; `PascalCase` para clases, enums y tipos; y `UPPER_SNAKE_CASE` para constantes.
- Las interfaces (clases abstractas) deben usar prefijo `I` en el nombre de la clase (ej: `IPasswordHasher`, `IUserRepository`).
- Evitar nombres en español, acrónimos ambiguos o mezclas de idiomas.

## Relación con la SKILL
- Esta guía complementa la SKILL de arquitectura del proyecto en [SKILL.md](SKILL.md).
- Antes de crear, mover o renombrar archivos, revisa esta guía junto con la estructura definida en la SKILL.