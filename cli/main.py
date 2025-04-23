import os
import argparse
from goblin.analyzer import parse_java_file
from goblin.detector import detect_smells

def analyze_folder(folder_path: str):
    java_files = []

    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".java"):
                java_files.append(os.path.join(root, file))

    print(f"Found {len(java_files)} Java file(s).")

    for file_path in java_files:
        print(f"\n📂 Analyzing: {file_path}")
        try:
            result = parse_java_file(file_path)
            
            clean_count = 0
            smelly_count = 0

            for method in result.methods:
                print(f"\n   🧪 {method.method_name}")
                
                if method.smells:
                    smelly_count += 1
                    print("      👹 Smells:")
                    for smell in method.smells:
                        print(f"         - {smell.value}")
                else:
                    clean_count += 1
                    print(f"      ✅ Assertions: {method.assertion_count}")
                    print("      😇 No smells detected")

            # After all methods in a file
            print("\n🧾 Summary:")
            print(f"   • {len(result.methods)} test method(s)")
            print(f"   • {clean_count} clean")
            print(f"   • {smelly_count} suspicious")

        except Exception as e:
            print(f"⛔️ Failed to parse {file_path}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Goblin CLI – Test smell analyzer")
    subparsers = parser.add_subparsers(dest="command")

    analyze_parser = subparsers.add_parser("analyze", help="Analyze Java test files")
    analyze_parser.add_argument("path", help="Path to folder with .java files")

    args = parser.parse_args()

    if args.command == "analyze":
        analyze_folder(args.path)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()