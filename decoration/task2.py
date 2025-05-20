def decorator(func):
    def wrapper(r):  
        print("Area of circle");
        func(r);  
        print("Programme executed");
    return wrapper;

@decorator
def greet(r):
    res = 3.14 * r**2;  
    print(res);

greet(4) ; 
