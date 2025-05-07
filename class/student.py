class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def show(self):
        print("name:", self.name, "marks:", self.marks)

s = student("aisha",70)
s.show()
