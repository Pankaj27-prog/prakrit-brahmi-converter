import json

from converters.prakrit_brahmi import (
    PrakritBrahmiConverter
)


INPUT_FILE = "data/sattsai_dataset.json"
OUTPUT_FILE = "data/sattsai_brahmi.json"


def convert_dataset():

    with open(
        INPUT_FILE,
        "r",
        encoding="utf-8"
    ) as f:

        verses = json.load(f)

    output = []

    for verse in verses:

        prakrit = verse["prakrit"]

        brahmi = (
            PrakritBrahmiConverter.convert(
                prakrit
            )
        )

        output.append(
            {
                "verse_number":
                    verse["verse_number"],

                "prakrit":
                    prakrit,

                "english":
                    verse["english"],

                "brahmi":
                    brahmi
            }
        )

    with open(
        OUTPUT_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            output,
            f,
            ensure_ascii=False,
            indent=4
        )

    print(
        f"Converted {len(output)} verses"
    )


if __name__ == "__main__":
    convert_dataset()