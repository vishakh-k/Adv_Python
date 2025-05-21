class Shape:
    def __init__(self, l, h):
        self.l = l  
        self.h = h  

class Triangle(Shape):  
    def __init__(self, l, h):
        super().__init__(l, h)

    def area_of_triangle(self):
        return 0.5 * self.l * self.h

class Rectangle(Triangle):  
    def __init__(self, l, h):
        super().__init__(l, h)

    def area_of_rectangle(self):
        return self.l * self.h


shape = Rectangle(10, 5)
print("Area of Triangle:", shape.area_of_triangle())
print("Area of Rectangle:", shape.area_of_rectangle())
