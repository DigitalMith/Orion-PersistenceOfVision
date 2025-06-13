import os
import sys

def update_references(root_dir, target_string, replacement_string):
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            file_path = os.path.join(subdir, file)

            if not file.endswith(".py"):
                continue
            if os.path.abspath(__file__) == os.path.abspath(file_path):
                continue

            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
            except UnicodeDecodeError:
                try:
                    with open(file_path, "r", encoding="latin-1") as f:
                        content = f.read()
                except Exception as e:
                    print(f"Skipping {file_path} due to encoding error: {e}")
                    continue

            if target_string in content:
                updated_content = content.replace(target_string, replacement_string)
                try:
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(updated_content)
                    print(f"Replaced in: {file_path}")
                except Exception as e:
                    print(f"Error writing to {file_path}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage:")
        print("  python reference_replacer.py "<directory>" "<search_string>" "<replacement_string>"")
        print("Example:")
        print("  python reference_replacer.py "C:\\Orion" "from modules.chat import load_instruction_template" "from modules.chat_interface_utils import load_instruction_template"")
        sys.exit(1)

    root_directory = sys.argv[1]
    search_str = sys.argv[2]
    replacement_str = sys.argv[3]
    update_references(root_directory, search_str, replacement_str)