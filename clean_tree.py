import os
import sys
import shutil
import argparse
import fnmatch

def load_tree_file(file_path):
    # Try UTF-16 then fallback to UTF-8
    for encoding in ('utf-16', 'utf-8'):
        try:
            with open(file_path, 'r', encoding=encoding) as f:
                return [line.strip() for line in f if line.strip()]
        except Exception:
            continue
    raise RuntimeError(f"Failed to read {file_path} with supported encodings")

def matches_pattern(path, patterns):
    for pat in patterns:
        # Support glob patterns
        if fnmatch.fnmatch(path, pat):
            return True
        # Support directory prefix matches
        if path.startswith(pat.rstrip(os.sep) + os.sep):
            return True
    return False

def clean_paths(tree_lines, patterns, dry_run=True):
    to_remove = []
    for line in tree_lines:
        norm = line
        if matches_pattern(norm, patterns):
            to_remove.append(norm)
    for path in to_remove:
        if dry_run:
            print(f"[DRY RUN] Would remove: {path}")
        else:
            if os.path.isdir(path):
                shutil.rmtree(path)
                print(f"Removed directory: {path}")
            elif os.path.isfile(path):
                os.remove(path)
                print(f"Removed file: {path}")
            else:
                print(f"Path not found (skipped): {path}")

def main():
    parser = argparse.ArgumentParser(
        description="Clean unneeded files/directories based on a tree listing"
    )
    parser.add_argument(
        "treefile",
        help="Path to the tree listing file (txt)"
    )
    parser.add_argument(
        "-p", "--pattern",
        nargs='+',
        required=True,
        help="Patterns or literal paths to remove (e.g. .git *.tmp)"
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Actually delete files, otherwise dry run"
    )
    args = parser.parse_args()

    lines = load_tree_file(args.treefile)
    clean_paths(lines, args.pattern, dry_run=not args.apply)

if __name__ == "__main__":
    main()
