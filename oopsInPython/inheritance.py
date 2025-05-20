class Shape:
    def __init__(self, radius):
        self.radius = radius;

class Circle(Shape):
    def area(self):
        return 3.14 * self.radius ** 2;

c=Circle(5);

print(c.area());