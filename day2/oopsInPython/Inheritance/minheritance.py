class Area:
    def __init__(self, r):
        self.r = r

    def area(self):
        a = 3.14 * self.r ** 2
        return a

class Square:
    def square(self, a):
        return a ** 2

class Child(Area, Square):
    def __init__(self, r):
        super().__init__(r)

    def display(self):
        print(f"Area of Circle: {self.area():.2f}")
        print(f"Square of Radius: {self.square(self.r)}")

# Usage
c = Child(5)
c.display()
