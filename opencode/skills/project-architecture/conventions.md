# Convenciones del proyecto

Este documento define las convenciones de organización y nomenclatura que deben seguirse al crear o modificar archivos del proyecto. Su propósito es mantener la estructura consistente, facilitar el mantenimiento del código y alinearse con la arquitectura establecida.

## Convenciones de nombres de archivos
- Los archivos que contienen definiciones de rutas o endpoints deben nombrarse con el sufijo `routes.py`.
- En este proyecto, los archivos de ruta deben seguir el patrón `nombre_routes.py`.
- Los nombres deben escribirse en minúsculas y, cuando sea necesario, separar palabras con guiones bajos.
- El nombre del archivo debe reflejar de forma clara la responsabilidad que cumple dentro del módulo.

## Convenciones de nomenclatura general
- Todos los nombres del proyecto deben escribirse en inglés, incluyendo archivos, carpetas, variables, constantes, funciones, clases, métodos, enums, interfaces y demás símbolos.
- Se debe preferir nomenclatura descriptiva y clara, evitando abreviaturas poco intuitivas.
- Para nombres compuestos, se recomienda usar `snake_case` para funciones, variables y archivos; `PascalCase` para clases, enums y tipos; y `UPPER_SNAKE_CASE` para constantes.
- Evitar nombres en español, acrónimos ambiguos o mezclas de idiomas.

## Relación con la SKILL
- Esta guía complementa la SKILL de arquitectura del proyecto en [SKILL.md](SKILL.md).
- Antes de crear, mover o renombrar archivos, revisa esta guía junto con la estructura definida en la SKILL.