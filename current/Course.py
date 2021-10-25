'''
Course class


'''

class Course:
    def __init__(self, number, name, instructor, max_number_of_students):
        self.number = number
        self.name = name
        self.instructor = instructor
        self.max_students = max_number_of_students

    def __str__(self): return self.name

