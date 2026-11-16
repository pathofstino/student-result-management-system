class Student:
    """Represents one student and their academic records."""

    def __init__(self, student_id, full_name, class_form, gender, date_of_birth,
                 scores=None, result_date=None):
        self.student_id = student_id
        self.full_name = full_name
        self.class_form = class_form
        self.gender = gender
        self.date_of_birth = date_of_birth
        self.scores = scores or {}
        self.result_date = result_date

    def total(self):
        return sum(self.scores.values())

    def average(self):
        if not self.scores:
            return 0.0
        return self.total() / len(self.scores)

    def grade(self):
        """Example grading scale; change the boundaries if your school uses another scale."""
        average = self.average()
        if average >= 70:
            return "A"
        elif average >= 60:
            return "B"
        elif average >= 50:
            return "C"
        elif average >= 45:
            return "D"
        return "F"

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "full_name": self.full_name,
            "class_form": self.class_form,
            "gender": self.gender,
            "date_of_birth": self.date_of_birth,
            "scores": self.scores,
            "result_date": self.result_date,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["student_id"],
            data["full_name"],
            data["class_form"],
            data["gender"],
            data["date_of_birth"],
            data.get("scores", {}),
            data.get("result_date"),
        )
