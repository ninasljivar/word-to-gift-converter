# Word to GIFT Converter

A Python application that converts multiple-choice questions stored in Microsoft Word (.docx) documents into the GIFT format used by Learning Management Systems (LMS) such as Moodle.

## Features

- Reads questions directly from a Word document
- Supports multiple-choice questions ([MC])
- Validates question format before conversion
- Detects common formatting errors:
  - Missing correct answer
  - Multiple correct answers
  - Missing answer markers
  - Invalid answer markers
  - Empty question text
  - Empty answer text
  - Less than two answer options
- Generates a valid GIFT output file


## Installation

Clone the repository:

```bash
git clone https://github.com/ninasljivar/word-to-gift-converter.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Place your Word document in the project directory.

Run:

```bash
python main.py
```
Type the name of the document in console -> Enter

The generated GIFT file will be saved in the project folder.

## Technologies

- Python
- python-docx

