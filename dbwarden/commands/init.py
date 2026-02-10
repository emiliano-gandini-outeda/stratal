from pathlib import Path

from dbwarden.constants import MIGRATIONS_DIR, TOML_FILE
from dbwarden.logging import get_logger


def init_cmd() -> None:
    """
    Initialize DBWarden in current directory.

    Creates the migrations directory and a warden.toml config file.
    """
    logger = get_logger()
    current_dir = Path.cwd()

    migrations_dir = current_dir / MIGRATIONS_DIR
    migrations_dir.mkdir(parents=True, exist_ok=True)

    toml_path = current_dir / TOML_FILE
    if not toml_path.exists():
        toml_content = """# DBWarden Configuration
sqlalchemy_url = "sqlite:///./mydb.db"

# Enable async mode (set to false for sync connections)
async = false

# Optional: PostgreSQL schema to use
# postgres_schema = "public"

# Optional: Paths to SQLAlchemy model files for automatic migration generation
# model_paths = ["models/"]
"""
        toml_path.write_text(toml_content)
        logger.info(f"Created DBWarden configuration file: {toml_path}")
        print(f"Created configuration file: {toml_path}")

    logger.info(
        f"Initialized DBWarden migrations directory: {migrations_dir.absolute()}"
    )
    print(f"DBWarden migrations directory created: {migrations_dir.absolute()}")
    print("\nNext steps:")
    print("  1. Edit warden.toml with your database connection URL")
    print("  2. Run 'dbwarden make-migrations' to generate migrations from your models")
