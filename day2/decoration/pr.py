def decorator(func):
    def wrapper():
        print("Hello World");
        func();
        print("Namaste World");
    return wrapper;

@decorator
def greet():
    print("VK");
greet();