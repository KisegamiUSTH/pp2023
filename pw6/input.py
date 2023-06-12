import os
import pickle

def write_student_info(students):
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)

def write_course_info(courses):
    with open("courses.pickle", "wb") as file:
        pickle.dump(courses, file)

def write_marks(students):
    with open("marks.pickle", "wb") as file:
        pickle.dump(students, file)

def compress_files():
    compression_method = input("Select a compression method (zip, tar): ")
    if compression_method == "zip":
        import zipfile
        with zipfile.ZipFile("students.dat", "w") as archive:
            archive.write("students.pickle")
            archive.write("courses.pickle")
            archive.write("marks.pickle")
    elif compression_method == "tar":
        import tarfile
        with tarfile.open("students.dat", "w") as archive:
            archive.add("students.pickle")
            archive.add("courses.pickle")
            archive.add("marks.pickle")
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
    file_list = ["students.pickle", "courses.pickle", "marks.pickle", "students.dat"]
    for file_name in file_list:
        if os.path.exists(file_name):
            os.remove(file_name)
