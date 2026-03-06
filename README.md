# Armageddon Treats — Document Generator

A Python toolkit for generating the Armageddon Treats business plan documents and financial projections.

## Project Structure

```
armageddon_treats/
├── styles/
│   └── doc_styles.py        # Shared Word document styling helpers
└── generators/
    ├── audit.py             # Business plan audit document
    ├── works_cited.py       # Works cited / references document
    ├── workbook.py          # Financial projections Excel workbook
    └── modules/
        ├── module_1.py      # Pre-Launch Timeline & Master Checklist
        ├── module_2.py      # Regulatory & Permit Compliance Guide
        ├── module_3.py      # Day-to-Day Operations Manual
        ├── module_4.py      # Brand Identity & Marketing Playbook
        └── module_5.py      # Year 1-2 Growth Roadmap & Scaling Plan
```

## Setup

```bash
pip install -r requirements.txt
```

## Usage

Generate all documents at once:

```bash
python main.py
```

Or generate individual documents:

```bash
python -m armageddon_treats.generators.audit
python -m armageddon_treats.generators.works_cited
python -m armageddon_treats.generators.workbook
python -m armageddon_treats.generators.modules.module_1
# ... etc.
```

Generated files are saved to the `output/` directory.

## Dependencies

- [python-docx](https://python-docx.readthedocs.io/) — Word document generation
- [openpyxl](https://openpyxl.readthedocs.io/) — Excel workbook generation
