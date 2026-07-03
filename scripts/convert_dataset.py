import json
from pathlib import Path

from converters.prakrit_brahmi import PrakritBrahmiConverter


# Project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent

INPUT_ROOT = PROJECT_ROOT / "data"
OUTPUT_ROOT = PROJECT_ROOT / "data_output"


def convert_file(input_path: Path, output_path: Path):
    """Convert one JSON dataset."""

    with open(input_path, "r", encoding="utf-8") as f:
        verses = json.load(f)

    # Only process datasets that are lists
    if not isinstance(verses, list):
        print(f"Skipping (not a verse list): {input_path}")
        return

    output = []

    for verse in verses:

        if not isinstance(verse, dict):
            continue

        prakrit = verse.get("Prakrit") or verse.get("prakrit")

        if not prakrit:
            continue

        brahmi = PrakritBrahmiConverter.convert(prakrit)

        record = {
            "verse_number": verse.get("verse_number"),
            "Prakrit": prakrit,
            "brahmi": brahmi,
        }

        # Preserve English if present
        if "English" in verse:
            record["English"] = verse["English"]

        if "english" in verse:
            record["english"] = verse["english"]

        output.append(record)

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(
            output,
            f,
            ensure_ascii=False,
            indent=4
        )

    print(f"✓ {input_path.relative_to(INPUT_ROOT)}")


def convert_dataset():

    total = 0

    for input_file in INPUT_ROOT.rglob("*.json"):

        # Skip already-converted files
        if input_file.stem.endswith("-output"):
            continue

        # Skip existing Brahmi datasets if desired
        if "brahmi" in input_file.stem.lower():
            print(f"Skipping existing Brahmi file: {input_file.name}")
            continue

        relative = input_file.relative_to(INPUT_ROOT)

        output_dir = OUTPUT_ROOT / relative.parent

        output_file = output_dir / f"{input_file.stem}-output.json"

        convert_file(input_file, output_file)

        total += 1

    print("\n===================================")
    print(f"Converted {total} JSON files.")
    print(f"Output saved in: {OUTPUT_ROOT}")
    print("===================================")


if __name__ == "__main__":
    convert_dataset()