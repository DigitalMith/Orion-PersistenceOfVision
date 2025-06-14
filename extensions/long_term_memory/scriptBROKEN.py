import gradio as gr
import sys
from pathlib import Path

# --- Path Correction: Allow this script to find our 'orion_memory.py' ---
# This adds the 'C:\Orion\tools' directory to Python's search path so we can import our manager.
try:
    # This navigates up from this script's location to the C:\Orion folder, then down into 'tools'
tools_path = Path(__file__).resolve().parent.parent.parent / 'orion_scripts'
    if str(tools_path) not in sys.path:
        sys.path.insert(0, str(tools_path))
    
    from orion_memory import OrionMemoryManager
    
    # Initialize our memory manager once when the script loads
    memory_manager = OrionMemoryManager()
    print("Orion LTM Extension: Successfully initialized OrionMemoryManager.")

except ImportError as e:
    print(f"FATAL: Orion LTM Extension could not import OrionMemoryManager. Is orion_memory.py in the C:\\Orion\\text-generation-webui\\orion_scripts folder? Details: {e}")
    print(f"FATAL: Orion LTM Extension encountered an unexpected error during initialization: {e}")
    memory_manager = None

# --- Oobabooga Extension Functions ---

def input_modifier(string: str, state: dict) -> str:
    """
    This function is called by the WebUI for every prompt.
    It modifies the user's input string to include Orion's memories.
    """
    if memory_manager:
        print("Orion LTM Extension: Injecting memories into prompt...")
        memory_block = memory_manager.get_context_for_prompt()
        
        # Combine the memory block with the original user input
        # This places the memories at the top of the context for the AI
        new_string = f"{memory_block}\n\n{string}"
        return new_string
    else:
        print("Orion LTM Extension: Memory manager not available. Passing through original string.")
        return string

def ui():
    """
    This function can add custom UI elements to the Gradio interface.
    We will use this later to add buttons for manually saving memories.
    For now, it does nothing.
    """
    pass