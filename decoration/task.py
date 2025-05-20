def decorator(func):
    def wrapper():
        print("Hello");
        func();
        print("Welcome to Python Programming");
    return wrapper;

@decorator
def greet(name):
    print(f"{name}");
greet();