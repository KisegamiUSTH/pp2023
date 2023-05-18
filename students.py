import numpy as np

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

    def calculate_average_gpa(self):
        credits = np.array([course.credit for course in self.courses.values()])
        marks = np.array([self.marks[course_id] for course_id in self.marks.keys()])
        weighted_sum = np.sum(credits * marks)
        total_credits = np.sum(credits)
        if total_credits == 0:
            return 0.0
        average_gpa = weighted_sum / total_credits
        return average_gpa    