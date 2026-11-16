from datetime import datetime
from student import Student
from storage import load_students, save_students
from results import SUBJECTS, enter_scores, update_one_score
from reports import student_report, class_report, class_statistics, save_text_report


def find_student(students, search_value):
    search_value = search_value.strip().lower()
    for student in students:
        if (student.student_id.lower() == search_value
                or search_value in student.full_name.lower()):
            return student
    return None


def ask_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty.")


def register_student(students):
    print("\n--- REGISTER NEW STUDENT ---")
    student_id = ask_non_empty("Student ID: ")
    if find_student(students, student_id):
        print("A student with that ID already exists.")
        return

    full_name = ask_non_empty("Full name: ")
    class_form = ask_non_empty("Class/Form: ")
    gender = ask_non_empty("Gender: ")

    while True:
        date_of_birth = ask_non_empty("Date of birth (YYYY-MM-DD): ")
        try:
            datetime.strptime(date_of_birth, "%Y-%m-%d")
            break
        except ValueError:
            print("Use the format YYYY-MM-DD, for example 2009-04-17.")

    students.append(Student(student_id, full_name, class_form, gender, date_of_birth))
    save_students(students)
    print("Student registered successfully.")


def view_students(students):
    if not students:
        print("No students have been registered.")
        return
    print("\n--- REGISTERED STUDENTS ---")
    for number, student in enumerate(students, start=1):
        print(f"{number}. {student.student_id} | {student.full_name} | "
              f"{student.class_form} | Average: "
              f"{student.average():.2f}" if student.scores else
              f"{number}. {student.student_id} | {student.full_name} | "
              f"{student.class_form} | No scores yet")


def search_student(students):
    query = input("Enter student ID or part of the student's name: ")
    student = find_student(students, query)
    if student:
        print(student_report(student))
    else:
        print("Student not found.")


def update_student(students):
    student = find_student(students, input("Enter student ID or name: "))
    if not student:
        print("Student not found.")
        return

    print("Press Enter to keep the current value.")
    new_name = input(f"Full name [{student.full_name}]: ").strip()
    new_class = input(f"Class/Form [{student.class_form}]: ").strip()
    new_gender = input(f"Gender [{student.gender}]: ").strip()
    new_dob = input(f"Date of birth [{student.date_of_birth}]: ").strip()

    if new_name:
        student.full_name = new_name
    if new_class:
        student.class_form = new_class
    if new_gender:
        student.gender = new_gender
    if new_dob:
        try:
            datetime.strptime(new_dob, "%Y-%m-%d")
            student.date_of_birth = new_dob
        except ValueError:
            print("Invalid date; keeping the old date of birth.")

    save_students(students)
    print("Student information updated.")


def delete_student(students):
    student = find_student(students, input("Enter student ID or name: "))
    if not student:
        print("Student not found.")
        return
    confirm = input(f"Delete {student.full_name}? Type YES to confirm: ")
    if confirm == "YES":
        students.remove(student)
        save_students(students)
        print("Student deleted.")
    else:
        print("Deletion cancelled.")


def choose_student(students):
    student = find_student(students, input("Enter student ID or name: "))
    if not student:
        print("Student not found.")
    return student


def show_menu():
    print("""
====================================================
                 NEW HORIZON SCHOOL
          STUDENT RESULT MANAGEMENT SYSTEM
====================================================
1.  Register new student
2.  View all students
3.  Search for a student
4.  Update student information
5.  Delete a student
6.  Enter student scores
7.  Update an existing score
8.  View individual report card
9.  View class results
10. Rank students by average
11. View class statistics
12. Generate and save class report
13. Exit
""")


def main():
    students = load_students()
    print(f"Loaded {len(students)} student record(s).")

    while True:
        show_menu()
        choice = input("Choose an option (1-13): ").strip()

        try:
            if choice == "1":
                register_student(students)
            elif choice == "2":
                view_students(students)
            elif choice == "3":
                search_student(students)
            elif choice == "4":
                update_student(students)
            elif choice == "5":
                delete_student(students)
            elif choice == "6":
                student = choose_student(students)
                if student:
                    enter_scores(student)
                    save_students(students)
            elif choice == "7":
                student = choose_student(students)
                if student:
                    update_one_score(student)
                    save_students(students)
            elif choice == "8":
                student = choose_student(students)
                if student:
                    print(student_report(student))
            elif choice == "9":
                print(class_report(students))
            elif choice == "10":
                ranked = sorted(students, key=lambda item: item.average(), reverse=True)
                print("\n--- STUDENT RANKING ---")
                for position, student in enumerate(ranked, start=1):
                    if student.scores:
                        print(f"{position}. {student.full_name} - "
                              f"{student.average():.2f} ({student.grade()})")
            elif choice == "11":
                print(class_statistics(students))
            elif choice == "12":
                content = class_report(students) + "\n\n" + class_statistics(students)
                path = save_text_report(content)
                print(f"Report saved to: {path}")
            elif choice == "13":
                save_students(students)
                print("Your records have been saved. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a number from 1 to 13.")
        except (OSError, ValueError) as error:
            print(f"An error occurred: {error}. Please try again.")


if __name__ == "__main__":
    main()
