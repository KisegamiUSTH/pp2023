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
