from converters.prakrit_brahmi import (
    PrakritBrahmiConverter
)


samples = [
    "बुद्ध",
    "धम्म",
    "संघ",
    "अमिअं",
    "पसुवइणो",
    "श्रीकांत"
]

for text in samples:

    print(text)

    print(
        PrakritBrahmiConverter.convert(
            text
        )
    )

    print("-" * 50)