# DBWarden - Python Database Migrations

**DBWarden** es un sistema de migraciones de base de datos profesional para proyectos Python/SQLAlchemy.

## Instalación

```bash
pip install dbwarden
```

## Configuración

Crear `.env` en tu proyecto:

```env
STRATA_SQLALCHEMY_URL=postgresql://user:pass@localhost/db
STRATA_ASYNC=false  # o true para modo async
```

## Comandos Básicos

| Comando | Descripción |
|---------|-------------|
| `dbwarden init` | Inicializa el directorio de migraciones |
| `dbwarden make-migrations "nombre"` | Genera SQL desde modelos SQLAlchemy |
| `dbwarden migrate` | Aplica migraciones pendientes |
| `dbwarden migrate --verbose` | Aplica con logging detallado |
| `dbwarden rollback` | Revierte la última migración |
| `dbwarden history` | Muestra historial de migraciones |
| `dbwarden status` | Muestra estado actual |
| `dbwarden mode` | Muestra modo sync/async |
| `dbwarden check-db` | Inspecciona el schema de la DB |
| `dbwarden diff` | Muestra diferencias modelos vs DB |

## Modelos SQLAlchemy

DBWarden detecta automáticamente modelos en `models/`:

```python
# models/user.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(255), unique=True)
```

## Ejemplo Completo

```bash
# 1. Inicializar
dbwarden init

# 2. Crear modelos en models/

# 3. Generar migración desde modelos
dbwarden make-migrations "create users table"

# 4. Aplicar
dbwarden migrate --verbose

# 5. Ver historial
dbwarden history
```

## Variables de Entorno

| Variable | Descripción |
|----------|-------------|
| `STRATA_SQLALCHEMY_URL` | URL de conexión a la DB |
| `STRATA_ASYNC` | Modo async (`true`/`false`) |
| `STRATA_MODEL_PATHS` | Paths a modelos SQLAlchemy |

## Bases de Datos Soportadas

- PostgreSQL (sync + async)
- SQLite (sync + async)
- MySQL (sync)

## Licencia

MIT
