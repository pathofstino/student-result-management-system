
from datetime import datetime

SUBJECTS = ["Mathematics", "English", "Biology", "Chemistry", "Physics"]


def get_valid_score(prompt):
    """Request and validate a score between 0 and 100."""
    while True:
        try:
            score = float(input(prompt))

            if 0 <= score <= 100:
                return score

            print("Invalid score! Enter a value between 0 and 100.")

        except ValueError:
            print("Invalid input! Please enter a number.")


def enter_scores(student):
    """Collect five subject scores and record the entry date."""
    scores = {}

    print("\nEnter student scores (0-100).")

    for subject in SUBJECTS:
        scores[subject] = get_valid_score(f"{subject}: ")

    student.scores = scores
    student.result_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print("\nAll scores have been recorded successfully!")


def update_one_score(student):
    """Update an existing subject score for a student."""
    if not student.scores:
        print("No scores available. Please enter scores first.")
        return

    print("\nAvailable subjects:", ", ".join(student.scores.keys()))

    subject_input = input("Enter the subject to update: ").strip()

    subject = next(
        (name for name in student.scores
         if name.casefold() == subject_input.casefold()),
        None
    )

    if subject is None:
        print("Subject not found. Please check the subject name.")
        return

    new_score = get_valid_score(f"Enter new score for {subject}: ")

    student.scores[subject] = new_score
    student.result_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"{subject} score updated successfully!")
