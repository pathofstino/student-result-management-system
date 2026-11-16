# New Horizon Student Result Management System

A menu-driven Student Result Management System built with Python for the Introduction to Python Programming practical project.

## Features

- Register, view, search, update and delete students.
- Record scores in five subjects: Mathematics, English, Biology, Chemistry and Physics.
- Calculate total, average and grade automatically.
- Update an individual subject score.
- Display individual report cards.
- Display class results and rank students by average.
- Calculate highest average, lowest average and class average.
- Save class reports as text files.
- Save and load student records using JSON so data remains available after the program closes.

## Requirements

- Python 3.8 or later.
- No third-party packages are required.

## How to run

1. Download or clone this repository.
2. Open a terminal or command prompt in the `student_result_system` folder.
3. Run:

   ```bash
   python main.py
   ```

   On some computers, use `python3 main.py`.

4. Select an option from the menu and follow the instructions.

## Project structure

```text
student_result_system/
├── main.py
├── student.py
├── results.py
├── storage.py
├── reports.py
├── data/
│   └── students.json
├── reports/
└── README.md
```

## Grading scale used in this example

| Average | Grade |
|---|---|
| 70–100 | A |
| 60–69.99 | B |
| 50–59.99 | C |
| 45–49.99 | D |
| Below 45 | F |

This is an example scale selected for the project because the assignment does not specify exact grade boundaries. Change the `grade()` method in `student.py` if your lecturer or school gives a different scale.

## Python concepts demonstrated

- Variables, strings, numbers and type conversion.
- `if`, `elif`, `else`, `for` and `while`.
- Lists and dictionaries.
- Functions with parameters and return values.
- Sorting with `sorted()`.
- Exception handling with `try` and `except`.
- JSON file reading and writing.
- Modules and imports across multiple Python files.
- Object-oriented programming with the `Student` class.
- Date and time using `datetime`.

## Notes

- Each student's record is stored in `data/students.json`.
- The program creates the data file when the first record is saved.
- Each score must be between 0 and 100.
- The five required subjects are listed in `results.py`.
- Class statistics are calculated from students who have scores entered.
