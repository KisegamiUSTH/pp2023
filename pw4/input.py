def get_student_input():
    student_id = input("Enter student id: ")
    student_name = input("Enter student name: ")
    student_dob = input("Enter student date of birth: ")
    return student_id, student_name, student_dob

def get_course_input():
    course_id = input("Enter course id: ")
    course_name = input("Enter course name: ")
    return course_id, course_name

def get_mark_input(student_name):
    mark = float(input(f"Enter mark for student {student_name}: "))
    return mark

def get_course_id_input():
    course_id = input("Enter course id: ")
    return course_id
