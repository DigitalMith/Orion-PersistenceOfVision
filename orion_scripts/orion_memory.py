import json
import os
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any, Optional
import uuid

# --- Configuration: The single source of truth for all memory files ---
ORION_DATA_PATH = Path(__file__).parent.parent / 'orion_data'
EPISODIC_MEMORY_PATH = ORION_DATA_PATH / "memory" / "long_term_memory.json"
CORE_MEMORY_PATH = ORION_DATA_PATH / "memory" / "orion_ltm_memory.json" # <-- New path

class OrionMemoryManager:
    """Manages Orion's dual-component memory system."""

    def __init__(self):
        """Initializes the memory manager and loads both memory types."""
        self.episodic_memories: List[Dict[str, Any]] = self._load_json(EPISODIC_MEMORY_PATH)
        self.core_memories: List[Dict[str, Any]] = self._load_json(CORE_MEMORY_PATH)
        print(f"Loaded {len(self.episodic_memories)} episodic memories and {len(self.core_memories)} core memories.")

    def _load_json(self, file_path: Path) -> List[Dict[str, Any]]:
        """Loads a JSON file, creating it if it doesn't exist."""
        if not file_path.exists():
            file_path.parent.mkdir(parents=True, exist_ok=True)
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump([], f)
            return []
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def save_episodic_memory(self):
        """Saves the current episodic memory list back to its JSON file."""
        with open(EPISODIC_MEMORY_PATH, "w", encoding="utf-8") as f:
            json.dump(self.episodic_memories, f, indent=2, ensure_ascii=False)
        print("Episodic memory saved.")

    def add_episodic_memory(self, role: str, content: str, tags: Optional[List[str]] = None, importance: float = 0.5):
        """Adds a new memory to the chronological, episodic log."""
        entry = {
            "id": str(uuid.uuid4()),
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "source": "conversation_log",
            "tags": tags or [],
            "importance": importance,
            "role": role,
            "content": content,
            "summary": "" 
        }
        self.episodic_memories.append(entry)
        self.save_episodic_memory()
        print(f"Added new episodic memory: {entry['id']}")

    def get_context_for_prompt(self, recent_limit: int = 5, core_limit: int = 3) -> str:
        """Constructs a memory block for the LLM prompt."""
        
        # Get the most important core memories
        sorted_core = sorted(self.core_memories, key=lambda m: m.get("weight", 0), reverse=True)
        selected_core = sorted_core[:core_limit]

        # Get the most recent episodic memories
        sorted_episodic = sorted(self.episodic_memories, key=lambda m: m.get("timestamp", ""), reverse=True)
        selected_episodic = sorted_episodic[:recent_limit]

        # Assemble the prompt block
        memory_block = ["# Core Memories (What I know about myself):"]
        for mem in selected_core:
            memory_block.append(f"- {mem['text']}")

        memory_block.append("\n# Recent Events (What has happened recently):")
        for mem in selected_episodic:
            display_role = mem['role']
            if display_role == 'user':
                display_role = 'John'
            elif display_role == 'assistant':
                display_role = 'Orion'
            memory_block.append(f"- At {mem['timestamp']}, {display_role} said: {mem['content']}")
        return "\n".join(memory_block)


# This part allows the script to be run directly for testing
if __name__ == '__main__':
    print("Initializing Orion Memory Manager for a test run...")
    memory_manager = OrionMemoryManager()

    print("\n--- Generating sample context for prompt ---")
    context_string = memory_manager.get_context_for_prompt()
    print(context_string)
    
    print("\nTest run complete.")