import json
from orion_ltm import add_memory
from uuid import uuid4

with open("long_term_memory.json", "r", encoding="utf-8") as f:
    memories = json.load(f)

print(f"Loaded {len(memories)} entries from long_term_memory.json")

def clean_metadata(raw):
    allowed_types = (str, int, float, bool, type(None))
    return {
        k: v for k, v in raw.items()
        if isinstance(v, allowed_types)
    }
    
for entry in memories:
    content = entry.get("content", "").strip()
    if not content:
        continue

    raw_meta = {
        "role": entry.get("role"),
        "source": entry.get("source"),
        "tags": entry.get("tags"),           # <- these are lists
        "timestamp": entry.get("source_time"),
        "emotions": entry.get("emotions"),   # <- also lists
    }
    
    # Flatten metadata (remove list values)
    meta = clean_metadata(raw_meta)
    uid = entry.get("id") or str(uuid4())
    add_memory(content, metadata=meta, uid=uid)

print("✅ Orion's long-term memory seeded into ChromaDB.")
