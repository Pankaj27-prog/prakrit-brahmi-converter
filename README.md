# Prakrit → Brahmi Converter

A Python-based tool for converting **Prakrit text written in Devanagari** into the **Brahmi script**. The project supports both standalone Prakrit datasets and parallel Prakrit–English datasets, and can batch process entire directory structures while preserving folder hierarchy.

---

## Features

- Convert Prakrit (Devanagari) to Brahmi
- Batch conversion of multiple JSON datasets
- Supports both:
  - Prakrit-only datasets
  - Prakrit–English parallel datasets
- Automatically traverses all subdirectories
- Preserves the original folder structure
- Generates output files with the suffix `-output.json`
- Dataset validation
- Flask web interface
- Unicode-safe JSON processing

---

## Installation

### Clone the repository

```bash
git clone https://github.com/Pankaj27-prog/prakrit-brahmi-converter.git
cd prakrit-brahmi-converter
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Dataset Structure

The converter expects datasets inside the `data` directory.

```
data/
├── Prakrit_English/
│   ├── input.json
│   ├── sattsai_dataset.json
│   └── ...
│
└── Prakrit_Text/
    ├── Chappannaya/
    ├── Dhanapala/
    ├── Dhanēśvara/
    ├── Haribhadra/
    ├── Hāla/
    ├── Jayavallabha/
    ├── Jinēśvara/
    ├── Kautūhala/
    ├── Pravarasēna/
    ├── Prākr̥tapaiṅgalam/
    ├── Vararuci/
    ├── Vākpatirāja/
    └── Śvētāmbarāgama/
```

The converter recursively processes every JSON file inside `data/`.

---

## Supported Input Formats

### 1. Prakrit-only Dataset

```json
[
    {
        "verse_number": 1,
        "Prakrit": "..."
    }
]
```

### 2. Prakrit–English Dataset

```json
[
    {
        "verse_number": 1,
        "Prakrit": "...",
        "English": "..."
    }
]
```

Lowercase keys (`prakrit`, `english`) are also supported.

---

## Dataset Conversion

Run:

```bash
python -m scripts.convert_dataset
```

The script will:

- Traverse every JSON file under `data/`
- Convert the Prakrit text into Brahmi
- Preserve the original directory hierarchy
- Store the converted datasets inside `data_output/`

Example:

```
data/
└── Prakrit_Text/
    └── Dhanēśvara/
        └── SurSuCa.json
```

↓

```
data_output/
└── Prakrit_Text/
    └── Dhanēśvara/
        └── SurSuCa-output.json
```

Likewise,

```
data/
└── Prakrit_English/
    └── sattsai_dataset.json
```

↓

```
data_output/
└── Prakrit_English/
    └── sattsai_dataset-output.json
```

---

## Output Format

For Prakrit-only datasets:

```json
[
    {
        "verse_number": 1,
        "Prakrit": "...",
        "brahmi": "..."
    }
]
```

For Prakrit–English datasets:

```json
[
    {
        "verse_number": 1,
        "Prakrit": "...",
        "English": "...",
        "brahmi": "..."
    }
]
```

---

## Dataset Validation

Validate the generated datasets:

```bash
python -m scripts.validate_dataset
```

Expected output:

```text
====================
Dataset is clean ✓
```

---

## Project Structure

```text
prakrit-brahmi-converter/
├── app.py
├── converters/
│   ├── prakrit_brahmi.py
│   └── ...
│
├── scripts/
│   ├── convert_dataset.py
│   └── validate_dataset.py
│
├── data/
│   ├── Prakrit_Text/
│   └── Prakrit_English/
│
├── data_output/
│   ├── Prakrit_Text/
│   └── Prakrit_English/
│
├── templates/
├── static/
├── tests/
├── requirements.txt
└── README.md
```

---

## Author

**Pankaj Sarwa**

GitHub: https://github.com/Pankaj27-prog
