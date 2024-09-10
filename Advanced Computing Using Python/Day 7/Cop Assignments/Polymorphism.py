class Shape:
    def area(self):
        print("Shape Covers Area")

class Rectangle(Shape):
    def __init__(self, length, breadth):
        super()
        self._length = length
        self._breadth = breadth

    def area(self):
        print(f"Area of rectangle is {self._length * self._breadth}")

class Circle(Shape):
    def __init__(self, radius):
        super()
        self._radius = radius

    def area(self):
        print(f"Area of circle is {self._radius ** 2 * 3.1416}")

if __name__ == '__main__':
    rect  = Rectangle(length= 5, breadth=10)
    circ = Circle(radius= 5)
    rect.area()
    circ.area()