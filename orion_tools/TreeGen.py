import argparse
import json
import os
from pathlib import Path

CONFIG_PATH = Path.home() / '.config' / 'treegen'
PROFILE_FILE = CONFIG_PATH / 'profiles.json'


def load_profiles():
    if not PROFILE_FILE.exists():
        return {}
    try:
        return json.loads(PROFILE_FILE.read_text())
    except json.JSONDecodeError:
        return {}


def save_profiles(profiles):
    CONFIG_PATH.mkdir(parents=True, exist_ok=True)
    PROFILE_FILE.write_text(json.dumps(profiles, indent=2))


def main():
    parser = argparse.ArgumentParser(
        description="TreeGen: directory tree visualizer with profile support"
    )
    # core options
    parser.add_argument('-o', '--output', help='Output file')
    parser.add_argument('--md', action='store_true', help='Markdown format')
    parser.add_argument('--gitignore', action='store_true', help='Use .gitignore rules')
    parser.add_argument('-i', '--ignore', nargs='+', default=[], help='Ignore patterns')
    parser.add_argument('root', nargs='?', help='Root folder to scan')

    # profile commands
    parser.add_argument('--profile-save', metavar='NAME', help='Save current args as a named profile and exit')
    parser.add_argument('--profile-load', metavar='NAME', help='Load args from named profile and run')
    parser.add_argument('--profile-list', action='store_true', help='List all saved profile names and exit')
    parser.add_argument('--profile-del', metavar='NAME', help='Delete a named profile and exit')

    args = parser.parse_args()
    profiles = load_profiles()

    # Handle list
    if args.profile_list:
        if profiles:
            print("Available profiles:")
            for name in profiles:
                print(f"  - {name}")
        else:
            print("No profiles saved.")
        return

    # Handle delete
    if args.profile_del:
        name = args.profile_del
        if name in profiles:
            del profiles[name]
            save_profiles(profiles)
            print(f'Profile "{name}" deleted.')
        else:
            print(f'Profile "{name}" not found.')
        return

    # Handle load
    if args.profile_load:
        name = args.profile_load
        if name not in profiles:
            parser.error(f'Profile "{name}" not found. Available: {list(profiles.keys())}')
        prof = profiles[name]
        # merge profile into args
        for key, val in prof.items():
            # only override if CLI did not supply
            current = getattr(args, key, None)
            if current in (None, [], False):
                setattr(args, key, val)

    # Handle save
    if args.profile_save:
        name = args.profile_save
        prof = {
            'output': args.output,
            'md': args.md,
            'gitignore': args.gitignore,
            'ignore': args.ignore,
            'root': args.root
        }
        profiles[name] = prof
        save_profiles(profiles)
        print(f'Profile "{name}" saved.')
        return

    # Ensure root is provided
    if not args.root:
        parser.error('No root directory specified.')

    # Your existing tree generation logic goes here, e.g.:
    # tree = generate_tree(args.root, ignore=args.ignore, gitignore=args.gitignore)
    # output = format_tree(tree, markdown=args.md)
    # if args.output:
    #     Path(args.output).write_text(output)
    # else:
    #     print(output)

    print(f"Running TreeGen on {args.root} with ignore={args.ignore} md={args.md} gitignore={args.gitignore}")


if __name__ == '__main__':
    main()
