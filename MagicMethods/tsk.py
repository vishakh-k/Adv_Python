class Add:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self):
        return f"The Addition is: ({self.x} + {self.y}) = {self.x + self.y}"

    def __sub__(self):
        return f"The Subtraction is: ({self.x} - {self.y}) = {self.x - self.y}"

    def __mul__(self):
        return f"The Multiplication is: ({self.x} * {self.y}) = {self.x * self.y}"

    def __truediv__(self):
        if self.y == 0:
            return "Division by zero is not allowed."
        result = self.x / self.y
        return f"The Division is: ({self.x} / {self.y}) = {result:.2f}"


n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))


obj = Add(n1, n2)

# Call methods
print(obj.__add__())
print(obj.__sub__())
print(obj.__mul__())
print(obj.__truediv__())
