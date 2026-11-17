
import csv
import os

FILE_NAME = "students.csv"


# Create CSV file if it does not exist
def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Roll Number", "Name", "Marks"])


# Add a new student
def add_student():
    roll_no = input("Enter Roll Number: ")

    students = read_students()

    for student in students:
        if student["Roll Number"] == roll_no:
            print("Student with this roll number already exists!")
            return

    name = input("Enter Student Name: ")

    try:
        marks = float(input("Enter Marks: "))

        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100.")
            return

    except ValueError:
        print("Please enter valid marks.")
        return

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([roll_no, name, marks])

    print("Student added successfully!")


# Read all student records
def read_students():
    students = []

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            students.append(row)

    return students


# Display all students
def view_students():
    students = read_students()

    if len(students) == 0:
        print("No student records found.")
        return

    print("\n------ STUDENT DETAILS ------")

    for student in students:
        print("Roll Number:", student["Roll Number"])
        print("Name:", student["Name"])
        print("Marks:", student["Marks"])
        print("-----------------------------")


# Search for a student
def search_student():
    roll_no = input("Enter Roll Number to Search: ")

    students = read_students()

    for student in students:
        if student["Roll Number"] == roll_no:
            print("\nStudent Found!")
            print("Roll Number:", student["Roll Number"])
            print("Name:", student["Name"])
            print("Marks:", student["Marks"])
            return

    print("Student not found!")


# Delete a student
def delete_student():
    roll_no = input("Enter Roll Number to Delete: ")

    students = read_students()
    updated_students = []
    found = False

    for student in students:
        if student["Roll Number"] == roll_no:
            found = True
        else:
            updated_students.append(student)

    if found:
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Roll Number", "Name", "Marks"])

            for student in updated_students:
                writer.writerow([
                    student["Roll Number"],
                    student["Name"],
                    student["Marks"]
                ])

        print("Student deleted successfully!")
    else:
        print("Student not found!")


# Update student details
def update_student():
    roll_no = input("Enter Roll Number to Update: ")

    students = read_students()
    found = False

    for student in students:
        if student["Roll Number"] == roll_no:
            found = True

            print("Enter new details:")
            name = input("Enter New Name: ")

            try:
                marks = float(input("Enter New Marks: "))

                if marks < 0 or marks > 100:
                    print("Marks must be between 0 and 100.")
                    return

            except ValueError:
                print("Please enter valid marks.")
                return

            student["Name"] = name
            student["Marks"] = str(marks)
            break

    if found:
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Roll Number", "Name", "Marks"])

            for student in students:
                writer.writerow([
                    student["Roll Number"],
                    student["Name"],
                    student["Marks"]
                ])

        print("Student details updated successfully!")
    else:
        print("Student not found!")


# Main menu
def main():
    create_file()

    while True:
        print("\n================================")
        print("     STUDENT MANAGEMENT SYSTEM")
        print("================================")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Update Student")
        print("6. Exit")
        print("================================")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            delete_student()

        elif choice == "5":
            update_student()

        elif choice == "6":
            print("Thank you for using Student Management System!")
            break

        else:
            print("Invalid choice! Please select between 1 and 6.")


# Run the program
if __name__ == "__main__":
    main()
