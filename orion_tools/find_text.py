import os

search_root = "C:/Orion"
target_phrase = "Orion wasn't given"

for root, dirs, files in os.walk(search_root):
    for file in files:
        if file.endswith(".py") or file.endswith(".txt"):
            filepath = os.path.join(root, file)
            try:
                with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                    for i, line in enumerate(f, 1):
                        if target_phrase in line:
                            print(f"{filepath} (line {i}): {line.strip()}")
            except Exception as e:
                print(f"[SKIP] {filepath}: {e}")
