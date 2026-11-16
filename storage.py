import json
from pathlib import Path
from student import Student

DATA_FILE = Path(__file__).parent / "data" / "students.json"


def load_students():
    """Load students from JSON. Return an empty list if the file is not yet available."""
    try:
        if not DATA_FILE.exists():
            return []
        with DATA_FILE.open("r", encoding="utf-8") as file:
            records = json.load(file)
        return [Student.from_dict(record) for record in records]
    except (json.JSONDecodeError, OSError, KeyError, TypeError) as error:
        print(f"Warning: saved data could not be loaded: {error}")
        return []


def save_students(students):
    """Save all student records to JSON."""
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump([student.to_dict() for student in students], file, indent=4)
