import numpy as np
from math import floor
from domains.course import Course
from domains.student import Student
from input import (
    get_student_input,
    get_course_input,
    get_mark_input,
    get_course_id_input,
    write_student_info,
    write_course_info,
    write_marks,
    compress_files,
    check_and_decompress_files,
    cleanup_files
)
from output import (
    print_course,
    print_student,
    print_student_mark,
    print_student_gpa,
    print_sorted_students
)

students = {}
courses = {}

def add_student():
    student_id, student_name, student_dob = get_student_input()
    students[student_id] = Student(student_id, student_name, student_dob)

def add_course():
    course_id, course_name = get_course_input()
    courses[course_id] = Course(course_id, course_name)

def add_mark():
    course_id = get_course_id_input()
    if course_id not in courses:
        print("Course not found")
        return
    for student_id in students:
        mark = get_mark_input(students[student_id].name)
        mark = floor(mark * 10) / 10  # Rounding down to 1 decimal place
        students[student_id].add_course(course_id, courses[course_id].name)
        students[student_id].add_mark(course_id, mark)

def list_courses():
    for course_id in courses:
        print_course(course_id, courses[course_id].name)

def list_students():
    for student_id in students:
        print_student(student_id, students[student_id].name, students[student_id].dob)

def list_marks():
    course_id = get_course_id_input()
    if course_id not in courses:
        print("Course not found")
        return
    for student_id in students:
        if course_id in students[student_id].courses:
            print_student_mark(students[student_id].name, students[student_id].marks[course_id])

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

def calculate_and_list_gpa():
    student_id = input("Enter student id: ")
    if student_id in students:
        gpa = calculate_gpa(students[student_id])
        print_student_gpa(students[student_id].name, gpa)
    else:
        print("Student not found")

def sort_students_by_gpa():
    sorted_students = sorted(students.values(), key=lambda student: calculate_gpa(student), reverse=True)
    print_sorted_students(sorted_students)

def run_program():
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
            calculate_and_list_gpa()
        elif choice == "8":
            sort_students_by_gpa()
        elif choice == "9":
            break
        else:
            print("Invalid choice")

    write_student_info(students)
    write_course_info(courses)
    write_marks(students)
    compress_files()
    cleanup_files()

check_and_decompress_files()
run_program()
