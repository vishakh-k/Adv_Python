def decorator(func):
    def wrapper(*args, **kwargs):
        print("Hello")
        func(*args, **kwargs)
        print("Welcome to this World")
    return wrapper

@decorator
def greet(name):
    print(f"Hello, {name}")

greet("Vishakh")
