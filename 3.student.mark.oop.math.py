import curses
from students import Student
from courses import Course
import math

students = {}
courses = {}

def add_student(stdscr):
    stdscr.clear()
    stdscr.addstr("Enter student id: ")
    stdscr.refresh()
    student_id = stdscr.getstr().decode()
    stdscr.addstr("Enter student name: ")
    stdscr.refresh()
    student_name = stdscr.getstr().decode()
    stdscr.addstr("Enter student date of birth: ")
    stdscr.refresh()
    student_DOB = stdscr.getstr().decode()
    students[student_id] = Student(student_id, student_name, student_DOB)

def add_course(stdscr):
    stdscr.clear()
    stdscr.addstr("Enter course id: ")
    stdscr.refresh()
    course_id = stdscr.getstr().decode()
    stdscr.addstr("Enter course name: ")
    stdscr.refresh()
    course_name = stdscr.getstr().decode()
    courses[course_id] = Course(course_id, course_name)

def add_mark(stdscr):
    stdscr.clear()
    stdscr.addstr("Enter course id: ")
    stdscr.refresh()
    course_id = stdscr.getstr().decode()
    if course_id not in courses:
        stdscr.addstr("Course not found")
        stdscr.refresh()
        stdscr.getch()
        return
    for student_id in students:
        stdscr.addstr(f"Enter mark for student {students[student_id].name}: ")
        stdscr.refresh()
        mark = stdscr.getstr().decode()
        mark = math.floor(float(mark) * 10) / 10  # Round down to 1 decimal place
        students[student_id].add_course(course_id, courses[course_id].name)
        students[student_id].add_mark(course_id, mark)

def list_courses(stdscr):
    stdscr.clear()
    for course_id in courses:
        stdscr.addstr(f"{course_id}: {courses[course_id].name}\n")
    stdscr.refresh()
    stdscr.getch()

def list_students(stdscr):
    stdscr.clear()
    sort_students_by_gpa(stdscr)
    stdscr.refresh()
    stdscr.getch()

def list_marks(stdscr):
    stdscr.clear()
    stdscr.addstr("Enter course id: ")
    stdscr.refresh()
    course_id = stdscr.getstr().decode()
    if course_id not in courses:
        stdscr.addstr("Course not found")
        stdscr.refresh()
        stdscr.getch()
        return
    for student_id in students:
        if course_id in students[student_id].courses:
            stdscr.addstr(f"{students[student_id].name}: {students[student_id].marks[course_id]}\n")
    stdscr.refresh()
    stdscr.getch()

def sort_students_by_gpa(stdscr):
    stdscr.clear()
    sorted_students = sorted(students.values(), key=lambda student: student.calculate_average_gpa(), reverse=True)
    for student in sorted_students:
        stdscr.addstr(f"{student.name}: {student.calculate_average_gpa()}\n")
    stdscr.refresh()
    stdscr.getch()



def main(stdscr):
    curses.echo()  # Enable echoing of user input
    while True:
        stdscr.clear()
        stdscr.addstr("Select an option\n")
        stdscr.addstr("1. Add a student\n")
        stdscr.addstr("2. Add a course\n")
        stdscr.addstr("3. Add marks for a course\n")
        stdscr.addstr("4. List courses\n")
        stdscr.addstr("5. List students\n")
        stdscr.addstr("6. List marks for a course\n")
        stdscr.addstr("7. Quit\n")
        stdscr.addstr("Enter your choice: ")
        stdscr.refresh()

        choice = stdscr.getstr().decode()

        if choice == "1":
            add_student(stdscr)
        elif choice == "2":
            add_course(stdscr)
        elif choice == "3":
            add_mark(stdscr)
        elif choice == "4":
            list_courses(stdscr)
        elif choice == "5":
            list_students(stdscr)
        elif choice == "6":
            list_marks(stdscr)
        elif choice == "7":
            break
        else:
            stdscr.addstr("Invalid choice\n")
            stdscr.refresh()
            stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(main)
