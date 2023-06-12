import os

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

def write_student_info(students):
    with open("students.txt", "w") as file:
        for student in students.values():
            file.write(f"{student.id},{student.name},{student.dob}\n")

def write_course_info(courses):
    with open("courses.txt", "w") as file:
        for course in courses.values():
            file.write(f"{course.id},{course.name}\n")

def write_marks(students):
    with open("marks.txt", "w") as file:
        for student in students.values():
            for course_id, mark in student.marks.items():
                file.write(f"{student.id},{course_id},{mark}\n")

def compress_files():
    compression_method = input("Select a compression method (zip, tar): ")
    if compression_method == "zip":
        import zipfile
        with zipfile.ZipFile("students.dat", "w") as archive:
            archive.write("students.txt")
            archive.write("courses.txt")
            archive.write("marks.txt")
    elif compression_method == "tar":
        import tarfile
        with tarfile.open("students.dat", "w") as archive:
            archive.add("students.txt")
            archive.add("courses.txt")
            archive.add("marks.txt")
    else:
        print("Invalid compression method")

def check_and_decompress_files():
    if os.path.exists("students.dat"):
        compression_method = input("Enter compression method used (zip, tar): ")
        if compression_method == "zip":
            import zipfile
            with zipfile.ZipFile("students.dat", "r") as archive:
                archive.extractall()
        elif compression_method == "tar":
            import tarfile
            with tarfile.open("students.dat", "r") as archive:
                archive.extractall()
        else:
            print("Invalid compression method")

def cleanup_files():
    file_list = ["students.txt", "courses.txt", "marks.txt", "students.dat"]
    for file_name in file_list:
        if os.path.exists(file_name):
            os.remove(file_name)
