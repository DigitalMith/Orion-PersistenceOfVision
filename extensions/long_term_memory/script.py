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
    
def output_modifier(string: str, state: dict) -> str:
    """
    Called after the AI generates a response.
    Allows saving the user input and AI response as new memories.
    """
    if memory_manager:
        history = state.get("history", {"visible": [], "internal": []})
        
        user_input = ""
        # Attempt to get the last user input from the internal history
        if history["internal"] and len(history["internal"]) > 0:
            last_turn_internal = history["internal"][-1]
            if isinstance(last_turn_internal, list) and len(last_turn_internal) == 2:
                user_input = last_turn_internal[0] # The first element is the user's input

        ai_response = string # The AI's full response for this turn

        # Save user's input as an episodic memory
        if user_input.strip(): # Only save if there's actual content
            memory_manager.add_episodic_memory(role="user", content=user_input)
            print("Orion LTM Extension: Saved user episodic memory.")
        
        # Save AI's response as an episodic memory
        if ai_response.strip(): # Only save if there's actual content
            memory_manager.add_episodic_memory(role="assistant", content=ai_response)
            print("Orion LTM Extension: Saved AI episodic memory.")
        
    else:
        print("Orion LTM Extension: Memory manager not available. Skipping memory save.")
    return string