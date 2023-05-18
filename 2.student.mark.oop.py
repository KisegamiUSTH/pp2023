from students import Student
from courses import Course

students = {}
courses = {}

def add_student():
    student_id = input("Enter student id: ")
    student_name = input("Enter student name: ")
    student_DOB = input("Enter student date of birth: ")
    students[student_id] = Student(student_id, student_name, student_DOB)

def add_course():
    course_id = input("Enter course id: ")
    course_name = input("Enter course name: ")
    courses[course_id] = Course(course_id, course_name)

def add_mark():
    course_id = input("Enter course id: ")
    if course_id not in courses:
        print("Course not found")
        return
    for student_id in students:
        mark = float(input(f"Enter mark for student {students[student_id].name}: "))
        students[student_id].add_course(course_id, courses[course_id].name)
        students[student_id].add_mark(course_id, mark)

def list_courses():
    for course_id in courses:
        print(f"{course_id}: {courses[course_id].name}")

def list_students():
    for student_id in students:
        print(f"{student_id}: {students[student_id].name} ({students[student_id].dob})")

def list_marks():
    course_id = input("Enter course id: ")
    if course_id not in courses:
        print("Course not found")
        return
    for student_id in students:
        if course_id in students[student_id].courses:
            print(f"{students[student_id].name}: {students[student_id].marks[course_id]}")

while True:
    print("Select an option")
    print("1. Add a student")
    print("2. Add a course")
    print("3. Add marks for a course")
    print("4. List courses")
    print("5. List students")
    print("6. List marks for a course")
    print("7. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        add_course()
    elif choice == "3":
        add_mark()
    elif choice == "4":
        list_courses()
    elif choice == "5":
        list_students()
    elif choice == "6":
        list_marks()
    elif choice == "7":
        break
    else:
        print("Invalid choice")
