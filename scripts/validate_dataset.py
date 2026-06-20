# scripts/validate_dataset.py

import json

from converters.devanagari_brahmi import chars

SUPPORTED = {row[0] for row in chars}

SUPPORTED.update([
    " ", "\n", "\t",
    ",", ".", ";", ":",
    "!", "?", "-", "—",
    "(", ")", "[", "]",
    "'", '"'
])

def find_unknown(text):
    return sorted({
        ch for ch in str(text)
        if ch not in SUPPORTED
    })


def validate_json(json_file):
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    all_unknown = set()

    for item in data:

        text = item.get("prakrit", "")

        bad = find_unknown(text)

        if bad:
            print(
                f"Verse {item.get('verse_number')} -> {' '.join(bad)}"
            )

            all_unknown.update(bad)

    print("\n====================")

    if all_unknown:
        print("Missing mappings:")
        print(" ".join(sorted(all_unknown)))
    else:
        print("Dataset is clean ✓")


if __name__ == "__main__":
    validate_json(
        "data/sattsai_dataset.json"
    )