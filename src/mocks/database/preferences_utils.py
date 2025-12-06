import json
from pathlib import Path
from typing import Any, cast

REPO_ROOT = Path(__file__).resolve().parents[2]
DB_DIR = REPO_ROOT / "mocks" / "database"
DB_FILE = DB_DIR / "preferences.json"


def get_db_path() -> Path:
    if not DB_DIR.exists():
        DB_DIR.mkdir(parents=True, exist_ok=True)
    return DB_FILE


def load_preferences() -> dict[str, Any]:
    db_path = get_db_path()
    if not db_path.exists():
        # Initialize with empty dict
        defaults: dict[str, Any] = {}
        save_preferences(defaults)
        return defaults
    try:
        with open(db_path, "r") as f:
            data = json.load(f)
            return cast(dict[str, Any], data)
    except json.JSONDecodeError:
        return {}


def save_preferences(prefs: dict[str, Any]) -> None:
    db_path = get_db_path()
    with open(db_path, "w") as f:
        json.dump(prefs, f, indent=2)
