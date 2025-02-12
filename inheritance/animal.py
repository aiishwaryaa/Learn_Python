#parent class
class Animal:
    def __init__(self,name): #constructor
        self.name = name

    def make_sound(self):
        print("some sound") 

#child class
class Dog(Animal):
    def make_sound(self):# Overriding method
        print("Woof woof")

dog = Dog("cooper")
print(dog.name)
dog.make_sound()
