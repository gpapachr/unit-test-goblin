import argparse
import json
import os
import sys
from dataclasses import asdict
import toml

from goblin.analyzer import parse_java_file
from goblin.ascii_logo import GOBLIN_LOGO

from rich.console import Console
from rich.text import Text
from rich.panel import Panel

from goblin.shame_o_meter import shame_insult

console = Console()

def analyze_folder(folder_path: str, json_output=False):
    java_files = []
    results = []

    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".java"):
                java_files.append(os.path.join(root, file))
                file_path = os.path.join(root, file)
                try:
                    test_class = parse_java_file(file_path)
                    results.append({
                        "file": file_path,
                        "class": test_class.class_name,
                        "methods": [asdict(m) for m in test_class.methods]
                    })
                except Exception as e:
                    results.append({
                        "file": file_path,
                        "error": str(e)
                    })

    print(f"Found {len(java_files)} Java file(s).")

    if json_output:
        print(json.dumps(results, indent=2))
    else:
        for r in results:
            if "error" in r:
                print(f"\n📂❌ Failed to parse {r['file']} due to {r['error'] if r['error'] else 'Java syntax issues'}")
                continue
            
            console.print(f"📂 [bold cyan]Analyzing:[/] {r['file']}")
            clean = 0
            smelly = 0
            for method in r["methods"]:
                if method["smells"]:
                    smelly += 1
                    console.print(f"   🧪 [bold]{method['method_name']}[/]", style="yellow")
                    console.print("      👹 [bold red]Smells detected![/]")
                    for smell in method["smells"]:
                        print(f"         - {smell.value}")
                else:
                    clean += 1
                    console.print(f"   🧪 [green]{method['method_name']}[/] – [bold green]Clean![/]")
            console.print(Panel.fit(
                f"[bold white]🧾 Summary:[/]\n"
                f"• Total methods: {len(r['methods'])}\n"
                f"• ✅ Clean: {clean}\n"
                f"• 👹 Smelly: {smelly}",
                title="Analysis Result",
                subtitle="Goblin Summary",
                border_style="magenta"
            ))
            console.print(f"\n[italic red]{shame_insult(smelly, len(r['methods']))}[/]")

def get_version():
    pyproject_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "pyproject.toml"))
    try:
        data = toml.load(pyproject_path)
        return data["tool"]["poetry"]["version"]
    except Exception as e:
        raise RuntimeError(f"Could not read version from pyproject.toml: {e}")

def main():
    print(GOBLIN_LOGO)
    parser = argparse.ArgumentParser(
        prog="goblin",
        description="Goblin: A simple unit test runner for Python projects.",
        epilog="Examples:\n  goblin analyze ./examples\n  goblin --version\n  goblin --help",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--version", action="store_true", help="Show Goblin CLI version")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    analyze_parser = subparsers.add_parser("analyze", help="Analyze Java test files")
    analyze_parser.add_argument("path", help="Path to folder with .java files")
    analyze_parser.add_argument("--json", action="store_true", help="Output results as JSON")

    args = parser.parse_args()

    if args.version:
        try:
            version = get_version()
            print(f"Goblin CLI version: {version}")
            sys.exit(0)
        except RuntimeError as e:
            print(e)
            sys.exit(1)
    elif args.command == "analyze":
        analyze_folder(args.path, json_output=args.json)
        sys.exit(0)
    elif args.command is None:
        print("Error: No subcommand provided. Use '--help' to see available commands.")
        parser.print_help()
        sys.exit(1)
    else:
        parser.print_help()
if __name__ == "__main__":
    main()