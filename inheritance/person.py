# Parent class define ki - Person
class Person:
    def __init__(self, name, age): # Constructor jo name aur age set karega
        self.name = name
        self.age = age

    def get_details(self):  # Method jo name aur age return karega
        return self.name, self.age

# Child class Student jo Person class ko inherit kar rahi hai
class Student(Person):
    def __init__(self, name , age, student_id):
        super().__init__(name,age) # Parent class ka constructor call kiya (super() use karke)
        self.student_id = student_id # Student ka extra attribute
       
    def get_details(self):
        return self.name, self.age, self.student_id  # Method override kiya, par sirf student_id return kar raha hai

# Student class ka object banaya
s = Student("rahul",25,101) 

# Parent class ke attributes ko access kar rahe hain
print(s.name)
print(s.age)

# get_details method call kiya
print(s.get_details())  # Output: 101