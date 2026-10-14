students = []


def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    return "F"


def add_student():
    name = input("Enter student name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    try:
        marks = [
            float(input("Enter marks for subject 1: ")),
            float(input("Enter marks for subject 2: ")),
            float(input("Enter marks for subject 3: "))
        ]

        if any(mark < 0 or mark > 100 for mark in marks):
            print("Marks must be between 0 and 100.")
            return

    except ValueError:
        print("Please enter valid numeric marks.")
        return

    average = sum(marks) / len(marks)

    student = {
        "name": name,
        "marks": marks,
        "average": round(average, 2),
        "grade": calculate_grade(average)
    }

    students.append(student)
    print(f"Student '{name}' added successfully.")


def view_students():
    if not students:
        print("No student records found.")
        return

    for student in students:
        print(f"\nName: {student['name']}")
        print(f"Marks: {student['marks']}")
        print(f"Average: {student['average']}")
        print(f"Grade: {student['grade']}")


def main():
    while True:
        print("\n--- Student Management System ---")
        print("1. Add student")
        print("2. View students")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
