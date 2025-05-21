# Base class
class Shape:
    def get_values(self):
        # Placeholder: overridden in each child
        pass

    def display(self):
        # Placeholder: overridden in each child
        pass

# Child class 1
class Triangle(Shape):
    def get_values(self):
        self.base = float(input("Enter base of Triangle: "))
        self.height = float(input("Enter height of Triangle: "))

    def display(self):
        area = 0.5 * self.base * self.height
        print(f"Triangle Area = {area}")

# Child class 2
class Rectangle(Shape):
    def get_values(self):
        self.length = float(input("Enter length of Rectangle: "))
        self.breadth = float(input("Enter breadth of Rectangle: "))

    def display(self):
        area = self.length * self.breadth
        print(f"Rectangle Area = {area}")

# Child class 3
class Circle(Shape):
    def get_values(self):
        self.radius = float(input("Enter radius of Circle: "))

    def display(self):
        area = 3.1416 * self.radius * self.radius
        print(f"Circle Area = {area}")

# Polymorphism in action
def process_shape(shape: Shape):
    shape.get_values()
    shape.display()

# You can call this like:
print("--- Triangle ---")
process_shape(Triangle())

print("\n--- Rectangle ---")
process_shape(Rectangle())

print("\n--- Circle ---")
process_shape(Circle())
