def student_report(student):
    lines = [
        "=" * 48,
        "             STUDENT REPORT CARD",
        "=" * 48,
        f"Student ID: {student.student_id}",
        f"Full Name: {student.full_name}",
        f"Class/Form: {student.class_form}",
        f"Gender: {student.gender}",
        f"Date of Birth: {student.date_of_birth}",
        "-" * 48,
        "SUBJECT                         SCORE",
        "-" * 48,
    ]

    if student.scores:
        for subject, score in student.scores.items():
            lines.append(f"{subject:<30} {score:>6.1f}")
        lines.extend([
            "-" * 48,
            f"Total: {student.total():.1f}",
            f"Average: {student.average():.2f}",
            f"Grade: {student.grade()}",
            f"Date scores entered/updated: {student.result_date or 'Not recorded'}",
        ])
    else:
        lines.append("No scores have been entered yet.")

    lines.append("=" * 48)
    return "\n".join(lines)


def class_report(students):
    lines = ["NEW HORIZON SCHOOL - CLASS RESULTS", "=" * 65]
    lines.append(f"{'ID':<14}{'NAME':<25}{'TOTAL':>8}{'AVERAGE':>10}{'GRADE':>8}")
    lines.append("-" * 65)
    for student in sorted(students, key=lambda item: item.average(), reverse=True):
        if student.scores:
            lines.append(
                f"{student.student_id:<14}{student.full_name[:24]:<25}"
                f"{student.total():>8.1f}{student.average():>10.2f}{student.grade():>8}"
            )
        else:
            lines.append(f"{student.student_id:<14}{student.full_name[:24]:<25}{'No scores':>26}")
    return "\n".join(lines)


def class_statistics(students):
    scored = [student for student in students if student.scores]
    if not scored:
        return "No student scores are available for statistics."

    averages = [student.average() for student in scored]
    highest = max(scored, key=lambda item: item.average())
    lowest = min(scored, key=lambda item: item.average())

    return (
        f"Students with results: {len(scored)}\n"
        f"Highest average: {highest.average():.2f} ({highest.full_name})\n"
        f"Lowest average: {lowest.average():.2f} ({lowest.full_name})\n"
        f"Class average: {sum(averages) / len(averages):.2f}"
    )


def save_text_report(content):
    from pathlib import Path
    from datetime import datetime

    report_dir = Path(__file__).parent / "reports"
    report_dir.mkdir(exist_ok=True)
    filename = report_dir / f"class_report_{datetime.now():%Y%m%d_%H%M%S}.txt"
    filename.write_text(content, encoding="utf-8")
    return filename
