# first class (Course class)
class Course:
    course_id_counter = 1

    def __init__(self, course_name, course_level):
        self.course_id = Course.course_id_counter
        Course.course_id_counter += 1
        self.course_name = course_name
        self.course_level = course_level


# second class (student class)
class Student:
    student_id_counter = 1

    def __init__(self, student_name, student_level):
        self.student_name = student_name
        self.student_id = Student.student_id_counter
        Student.student_id_counter += 1
        self.student_level = student_level
        self.student_courses = []

    # method to add new course to student course
    def add_course(self, course):
        if self.student_level == course.course_level:
            self.student_courses.append(course)
            print("Course added to student successfully!")
        else:
            print("Student and course levels don't match.")

    # method to display student details
    def display_student_details(self):
        print("Student Id:", self.student_id)
        print("Student Name:", self.student_name)
        print("Student Level:", self.student_level)
        print("Courses Enrolled:")
        print("-" * 10)
        for course in self.student_courses:
            print("- Course Name:", course.course_name, "Course Level:", course.course_level)

        print("-_-" * 10)


def main():
    students = []
    courses = []

    # options that will appear
    while True:
        print("\nSelect Choices Please.")
        print("1. Add New Student")
        print("2. Remove Student")
        print("3. Edit Student")
        print("4. Display All Students")
        print("5. Create New Course")
        print("6. Add Course to Student")
        print("0. Exit")

        choice = input("Enter your choice: ")

        # Add New Student
        if choice == "1":
            student_name = input("Enter student name: ")
            student_level = input("Enter student level (A-B-C): ").upper()
            while student_level not in ["A", "B", "C"]:
                student_level = input("Invalid input. Enter student level (A-B-C): ").upper()
            new_student = Student(student_name, student_level)
            students.append(new_student)
            print("Student saved successfully!")

        # Remove Student
        elif choice == "2":
            student_id = int(input("Enter student ID to remove: "))
            found_student = None
            for student in students:
                if student.student_id == student_id:
                    found_student = student
                    break
            if found_student:
                students.remove(found_student)
                print("Student removed successfully!")
            else:
                print("Student not found.")

        # Edit Student
        elif choice == "3":
            student_id = int(input("Enter student ID to edit: "))
            found_student = None
            for student in students:
                if student.student_id == student_id:
                    found_student = student
                    break
            if found_student:
                new_name = input("Enter new student name: ")
                new_level = input("Enter new student level (A-B-C): ").upper()
                while new_level not in ["A", "B", "C"]:
                    new_level = input("Invalid input. Enter student level (A-B-C): ").upper()
                found_student.student_name = new_name
                found_student.student_level = new_level
                print("Student edited successfully!")
            else:
                print("Student not found.")

        # Display All Students
        elif choice == "4":
            print("\nAll Students:")
            for student in students:
                student.display_student_details()

        # Create New Course
        elif choice == "5":
            course_name = input("Enter course name: ")
            course_level = input("Enter course level (A-B-C): ").upper()
            while course_level not in ["A", "B", "C"]:
                course_level = input("Invalid input. Enter course level (A-B-C): ").upper()
            new_course = Course(course_name, course_level)
            courses.append(new_course)
            print("Course created successfully!")

        # Add Course to Student
        elif choice == "6":
            student_id = int(input("Enter student ID: "))
            course_id = int(input("Enter course ID: "))
            found_student = None
            found_course = None

            for student in students:
                if student.student_id == student_id:
                    found_student = student
                    break
            for course in courses:
                if course.course_id == course_id:
                    found_course = course
                    break

            if found_student and found_course:
                found_student.add_course(found_course)
            else:
                print("Student or course not found.")

        # Exit
        elif choice == "0":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
