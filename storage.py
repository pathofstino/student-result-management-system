
import json
from pathlib import Path
from student import Student

DATA_FILE = Path(__file__).parent / "data" / "students.json"


def load_students() -> list[Student]:
    """Load saved student records from the JSON file."""
    try:
        if not DATA_FILE.exists():
            print("No existing student records found.")
            return []

        with DATA_FILE.open("r", encoding="utf-8") as file:
            records = json.load(file)

        return [Student.from_dict(record) for record in records]

    except (json.JSONDecodeError, OSError, KeyError, TypeError) as error:
        print(f"Warning: Unable to load student records: {error}")
        return []


def save_students(students: list[Student]) -> None:
    """Save student records to the JSON file."""
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(
            [student.to_dict() for student in students],
            file,
            indent=4,
            ensure_ascii=False
        )

    print("Student records saved successfully.")
