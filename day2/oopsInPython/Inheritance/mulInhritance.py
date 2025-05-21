class Shape:
    def __init__(self, l):
        self.l = l ;
class Triangle(Shape):
    def __init__(self, l, height):
        super().__init__(l)
        self.height = height

class Child(Triangle):
    def __init__(self, l, height):
        super().__init__(l, height)

    def area(self):
        return 0.5 * self.l * self.height

c = Child(10, 5)
print(f"Area of Triangle: {c.area()}");
