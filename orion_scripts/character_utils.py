from pathlib import Path
import json
import modules.shared as shared

def force_load_character(name="Orion"):
    char_path = Path(f"user_data/characters/{name}.json")
    if char_path.exists():
        with open(char_path, "r", encoding="utf-8") as f:
            character_data = json.load(f)
        shared.character = character_data
        shared.character_name = character_data.get("char_name", name)
        print(f"[INFO] Forced character load: {shared.character_name}")
    else:
        print(f"[WARN] Character file not found at {char_path}")
