import argparse
import json
import os
from dataclasses import asdict

from goblin.analyzer import parse_java_file
from goblin.ascii_logo import GOBLIN_LOGO


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
                print(f"\n📂❌ Failed to parse {r['file']} due to {r['error'] if r['error'] else 'unknown reason'}")
                continue
            
            print(f"\n📂 Analyzing: {r['file']}")
            clean = 0
            smelly = 0
            for method in r["methods"]:
                print(f"\n   🧪 {method['method_name']}")
                if method["smells"]:
                    smelly += 1
                    print("      👹 Smells:")
                    for smell in method["smells"]:
                        print(f"         - {smell.value}")
                else:
                    clean += 1
                    print(f"      ✅ Assertions: {method['assertion_count']}")
                    print("      😇 No smells detected")
            print("\n🧾 Summary:")
            print(f"   • {len(r['methods'])} test method(s)")
            print(f"   • {clean} clean")
            print(f"   • {smelly} suspicious")

def main():
    print(GOBLIN_LOGO)
    parser = argparse.ArgumentParser(description="Goblin CLI – Test smell analyzer")
    subparsers = parser.add_subparsers(dest="command")

    analyze_parser = subparsers.add_parser("analyze", help="Analyze Java test files")
    analyze_parser.add_argument("path", help="Path to folder with .java files")
    analyze_parser.add_argument("--json", action="store_true", help="Output results as JSON")

    args = parser.parse_args()

    if args.command == "analyze":
        analyze_folder(args.path, json_output=args.json)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()