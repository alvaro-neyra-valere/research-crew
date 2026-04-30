"""
Import a Generic Agent Format (GAF) text into the CrewAI project.

Usage:
    python import_from_gaf.py <path_to_gaf_file>

The script reads the GAF file, calls the LLM parser, and overwrites
agents.yaml and tasks.yaml in the crew config directory.
"""

import sys
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

REPO_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(REPO_ROOT))

from src.parser import parse_to_crewai  # noqa: E402

CONFIG_DIR = Path(__file__).parent / "src" / "research_crew" / "config"


def import_gaf(gaf_path: Path) -> None:
    text = gaf_path.read_text(encoding="utf-8")
    print(f"Parsing GAF from: {gaf_path}")

    result = parse_to_crewai(text)

    agents_path = CONFIG_DIR / "agents.yaml"
    tasks_path = CONFIG_DIR / "tasks.yaml"

    agents_path.write_text(result["agents_yaml"], encoding="utf-8")
    tasks_path.write_text(result["tasks_yaml"], encoding="utf-8")

    print(f"agents.yaml written to: {agents_path}")
    print(f"tasks.yaml  written to: {tasks_path}")
    print(f"Agent key: {result['agent_key']}")
    print("\n--- agents.yaml ---")
    print(result["agents_yaml"])
    print("--- tasks.yaml ---")
    print(result["tasks_yaml"])


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python import_from_gaf.py <path_to_gaf_file>")
        sys.exit(1)

    gaf_file = Path(sys.argv[1])
    if not gaf_file.exists():
        print(f"Error: file not found: {gaf_file}")
        sys.exit(1)

    import_gaf(gaf_file)
