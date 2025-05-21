class Add:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        print("Hello");
        return f"Sum: {self.x + self.y}"

    def __repr__(self):
        print("world")
        return f"Add({self.x}, {self.y})"
        
obj = Add(5, 7)
print(str(obj))    
print(repr(obj))    
