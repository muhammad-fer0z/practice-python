class Student:
    # class constructor
    def __init__(self, student_id, student_name, student_marks):
        self.student_id = student_id
        self.student_name = student_name
        self.student_marks = student_marks

    # setter methods
    def set_student_id(self, student_id):
        self.student_id = student_id

    def set_student_name(self, student_name):
        self.student_name = student_name

    def set_student_marks(self, student_marks):
        self.student_marks = student_marks

    # getter methods
    def get_student_name(self):
        return self.student_name

    def get_student_id(self):
        return self.student_id

    def get_student_marks(self):
        return self.student_marks
