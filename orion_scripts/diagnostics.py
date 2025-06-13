import os
import sys
from pathlib import Path

# Constants
ROOT = Path("C:/Orion/text-generation-webui")
MODELS_DIR = ROOT / "models"
REQUIRED_FILES = [
    ROOT / "orion_server.py",
    ROOT / "modules" / "shared.py",
    ROOT / "modules" / "models.py"
]
REQUIRED_DIRS = [
    ROOT / ".venv",
    ROOT / "modules",
    MODELS_DIR
]
DEFAULTS = {
    "batch_size": 512,
    "gpu_layers": 0,
    "ctx_size": 2048
}

def check_directories():
    print("[CHECK] Validating required directories...")
    for d in REQUIRED_DIRS:
        print(f" - {d}:", "OK" if d.exists() else "Missing")

def check_files():
    print("[CHECK] Validating key runtime files...")
    for f in REQUIRED_FILES:
        print(f" - {f.name}:", "Found" if f.exists() else "Missing")

def check_model():
    print("[CHECK] Validating model file existence...")
    for model_path in MODELS_DIR.rglob("*.gguf"):
        print(f" - Found model: {model_path}")
        return
    print(" - ERROR: No .gguf model found under models/")

def check_args_safety():
    print("[CHECK] Simulating shared.args integrity...")
    class ArgsSim:
        pass
    args = ArgsSim()
    for k, v in DEFAULTS.items():
        if not hasattr(args, k):
            setattr(args, k, v)
            print(f" - {k} was missing, set to {v}")
        else:
            print(f" - {k} exists with value {getattr(args, k)}")

def main():
    print("[DIAGNOSTICS] Running Orion integrity pre-check...")
    check_directories()
    check_files()
    check_model()
    check_args_safety()
    print("[DIAGNOSTICS] Done.")

if __name__ == "__main__":
    main()
