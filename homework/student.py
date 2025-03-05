# write a python class named student with 2 attributes : student_id, student_name .
# add a new attribute: student_class. 
# create a function to display all attributes and their values in the student class.

class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

    def add_class(self, student_class):
        self.student_class = student_class

    def display_info(self):
        print(f"Student ID: {self.student_id}")
        print(f"Student Name: {self.student_name}")
        print(f"Student Class: {self.student_class}")

s1 = Student(101 , "Aishwarya")
s1.add_class("BCA-3rd year")
s1.display_info()

# Student ID: 101
# Student Name: Aishwarya
# Student Class: BCA-3rd year