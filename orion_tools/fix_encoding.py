from pathlib import Path

# --- Configuration ---
# Set the path to the file with the encoding issue
problem_file_path = Path("C:/Orion/text-generation-webui/extensions/long_term_memory/script.py")

# --- Main Script ---
print(f"Attempting to fix encoding for: {problem_file_path}")

try:
    # Read the file's content using 'utf-8-sig', which automatically detects and handles the BOM
    content = problem_file_path.read_text(encoding='utf-8-sig')
    
    # Write the content back using standard 'utf-8', which does not add a BOM
    problem_file_path.write_text(content, encoding='utf-8')
    
    print(f"\nSuccess! The file has been re-saved with the correct UTF-8 encoding (no BOM).")

except FileNotFoundError:
    print(f"\nError: Could not find the file at the specified path.")
except Exception as e:
    print(f"\nAn unexpected error occurred: {e}")