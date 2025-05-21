class Shape:
    def display(self):
        pass

class Triangle(Shape):
    def display(self, l, b):
        return 0.5 * l * b

# Create object
obj = [Triangle()]

# Call display method with values
for i in obj:
    print(i.display(4, 4))  # Output: 8.0
