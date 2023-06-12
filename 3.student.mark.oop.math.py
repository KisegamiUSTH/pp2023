import numpy as np
from math import floor

class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
        self.courses = {}
        self.marks = {}

    def add_course(self, course_id, course_name):
        self.courses[course_id] = course_name

    def add_mark(self, course_id, mark):
        self.marks[course_id] = mark

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
        mark = floor(mark * 10) / 10  # Rounding down to 1 decimal place
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

def calculate_gpa(student):
    credits = []
    marks = []
    for course_id, mark in student.marks.items():
        course_credits = credits[course_id]
        credits.append(course_credits)
        marks.append(mark)
    total_credits = sum(credits)
    weighted_marks = np.array(marks) * np.array(credits)
    gpa = np.sum(weighted_marks) / total_credits
    return round(gpa, 2)

def sort_students_by_gpa():
    sorted_students = sorted(students.values(), key=lambda student: calculate_gpa(student), reverse=True)
    for student in sorted_students:
        print(f"{student.name}: GPA {calculate_gpa(student)}")

students = {}
courses = {}

while True:
    print("Select an option")
    print("1. Add a student")
    print("2. Add a course")
    print("3. Add marks for a course")
    print("4. List courses")
    print("5. List students")
    print("6. List marks for a course")
    print("7. Calculate and list GPA")
    print("8. Sort students by GPA")
    print("9. Quit")

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
        student_id = input("Enter student id: ")
        if student_id in students:
            gpa = calculate_gpa(students[student_id])
            print(f"Student {students[student_id].name} has GPA {gpa}")
        else:
            print("Student not found")
    elif choice == "8":
        sort_students_by_gpa()
    elif choice == "9":
        break
    else:
        print("Invalid choice")
