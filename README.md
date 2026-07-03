# Prakrit → Brahmi Converter

A Python-based tool for converting Prakrit text written in Devanagari into Brahmi script.

## Features

- Convert Prakrit text to Brahmi
- Batch dataset conversion
- Dataset validation
- Flask web interface
- CSV dataset support

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

## Dataset Conversion

Convert the source dataset:

```bash
python -m scripts.convert_dataset
```

---

## Dataset Validation

Validate the converted dataset:

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
├── scripts/
│   ├── convert_dataset.py
│   └── validate_dataset.py
├── data/
├── templates/
├── static/
├── requirements.txt
└── README.md
```

---

## Author

Pankaj Sarwa
