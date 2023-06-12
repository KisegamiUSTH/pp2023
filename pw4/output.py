def print_course(course_id, course_name):
    print(f"{course_id}: {course_name}")

def print_student(student_id, student_name, student_dob):
    print(f"{student_id}: {student_name} ({student_dob})")

def print_student_mark(student_name, mark):
    print(f"{student_name}: {mark}")

def print_student_gpa(student_name, gpa):
    print(f"Student {student_name} has GPA {gpa}")

def print_sorted_students(sorted_students):
    for student in sorted_students:
        print(f"{student.name}: GPA {student.gpa}")
