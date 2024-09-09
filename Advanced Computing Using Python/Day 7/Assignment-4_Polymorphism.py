
class shape:

    shape_name =""
    def print_shape_area(self):
        print(f"Subclass is yet to be implemented")


class Circle(shape):

    def __init__(self, radius):
        self.radius = radius

    def print_shape_area(self,):
        print(f"Area of the circle is : {3.14*(self.radius **2)}")

class Rectangle(shape):

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def print_shape_area(self):
        print(f"Area of reactangle is : {self.length*self.breadth}")

def printarea(shape):
    shape.print_shape_area()

circle = Circle(5)
rectangle = Rectangle(10,5)
shape1 = shape()

rectangle2 = Rectangle(100,100)

printarea(circle)
printarea(rectangle)
printarea(shape1)
printarea(rectangle2)



