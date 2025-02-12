class Shape:
    def __init__(self, color):
        self.color = color

    def display(self):
        return self.color

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius   

    def display(self):
        return super.display()+"Circle with area : " + str(self.area()) + "."


class Rectangle(Shape):
    def __init__(self, color, length, width):
        super().__init__(color)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def display(self):
        return super().display()+"Rectangle with area : "+str(self.area()) +"."   

circle = Circle("red", 5)
rectangle = Rectangle("blue", 4, 6)

print(circle.display())
print(rectangle.display())