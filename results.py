from datetime import datetime

SUBJECTS = ["Mathematics", "English", "Biology", "Chemistry", "Physics"]


def enter_scores(student):
    """Collect five subject scores and record the date entered."""
    scores = {}
    print("\nEnter scores from 0 to 100.")
    for subject in SUBJECTS:
        while True:
            try:
                score = float(input(f"{subject}: "))
                if not 0 <= score <= 100:
                    print("Score must be between 0 and 100.")
                    continue
                scores[subject] = score
                break
            except ValueError:
                print("Please enter a valid number.")
    student.scores = scores
    student.result_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Scores saved successfully.")


def update_one_score(student):
    if not student.scores:
        print("This student has no scores yet. Enter scores first.")
        return

    print("Subjects:", ", ".join(student.scores.keys()))
    subject = input("Which subject do you want to update? ").strip().title()
    if subject not in student.scores:
        print("Subject not found.")
        return

    while True:
        try:
            score = float(input(f"New score for {subject}: "))
            if 0 <= score <= 100:
                student.scores[subject] = score
                student.result_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print("Score updated.")
                return
            print("Score must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")
