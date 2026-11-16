
from pathlib import Path
from datetime import datetime


def student_report(student):
    """Generate a detailed report card for an individual student."""

    lines = [
        "=" * 50,
        "             NEW HORIZON SCHOOL",
        "                REPORT CARD",
        "=" * 50,
        f"Student ID:       {student.student_id}",
        f"Full Name:        {student.full_name}",
        f"Class/Form:       {student.class_form}",
        f"Gender:           {student.gender}",
        f"Date of Birth:    {student.date_of_birth}",
        "-" * 50,
        f"{'SUBJECT':<32}{'SCORE':>8}",
        "-" * 50,
    ]

    if student.scores:
        for subject, score in student.scores.items():
            lines.append(f"{subject:<32}{score:>8.1f}")

        lines.extend([
            "-" * 50,
            f"Total Score:      {student.total():.1f}",
            f"Average Score:    {student.average():.2f}",
            f"Grade:            {student.grade()}",
            f"Result Date:      {student.result_date or 'Not recorded'}",
        ])
    else:
        lines.append("No examination scores have been recorded.")

    lines.append("=" * 50)

    return "\n".join(lines)


def class_report(students):
    """Generate a summary of all students and their academic results."""

    lines = [
        "NEW HORIZON SCHOOL - CLASS RESULTS",
        "=" * 70,
        f"{'STUDENT ID':<15}{'NAME':<25}{'TOTAL':>8}{'AVERAGE':>12}{'GRADE':>10}",
        "-" * 70,
    ]

    ranked_students = sorted(
        students,
        key=lambda item: item.average(),
        reverse=True
    )

    for student in ranked_students:
        if student.scores:
            lines.append(
                f"{student.student_id:<15}"
                f"{student.full_name[:24]:<25}"
                f"{student.total():>8.1f}"
                f"{student.average():>12.2f}"
                f"{student.grade():>10}"
            )
        else:
            lines.append(
                f"{student.student_id:<15}"
                f"{student.full_name[:24]:<25}"
                f"{'No scores':>30}"
            )

    lines.append("=" * 70)

    return "\n".join(lines)


def class_statistics(students):
    """Calculate and display the overall class performance statistics."""

    scored_students = [
        student for student in students if student.scores
    ]

    if not scored_students:
        return "No student scores are available for statistics."

    averages = [student.average() for student in scored_students]

    highest = max(scored_students, key=lambda item: item.average())
    lowest = min(scored_students, key=lambda item: item.average())

    class_average = sum(averages) / len(averages)

    return (
        "\nCLASS PERFORMANCE STATISTICS\n"
        + "=" * 40 + "\n"
        f"Students with results: {len(scored_students)}\n"
        f"Highest average: {highest.average():.2f} ({highest.full_name})\n"
        f"Lowest average: {lowest.average():.2f} ({lowest.full_name})\n"
        f"Overall class average: {class_average:.2f}\n"
        + "=" * 40
    )


def save_text_report(content):
    """Save the generated class report as a text file."""

    report_dir = Path(__file__).parent / "reports"
    report_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = report_dir / f"class_report_{timestamp}.txt"

    filename.write_text(content, encoding="utf-8")

    print("Class report generated successfully!")

    return filename
