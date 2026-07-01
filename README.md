# Word to GIFT Converter

A Python application that converts multiple-choice questions stored in Microsoft Word (.docx) documents into the GIFT format used by Learning Management Systems (LMS) such as Moodle.

## Features

- Reads questions from a Microsoft Word (.docx) file
- Validates question format before conversion
- Detects common formatting errors:
  - Missing correct answer
  - Multiple correct answers
  - Missing answer markers
  - Invalid answer markers
  - Empty question text
  - Empty answer text
  - Less than two answer options
- Converts valid questions to GIFT format
- Prompts the user to enter the document name
- Handles missing files and asks the user to try again


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
Enter the name of the document in console -> Enter

The generated GIFT file will be saved in the project folder.

If the file cannot be found, the program will display an error message and ask you to enter the file name again.


If you wish to terminate the program, as name type "exit".

## Technologies

- Python
- python-docx

