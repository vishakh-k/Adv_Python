def decorator(func):
    def wrapper(*args, **kwargs):  
        print("Addition and Multiplication");
        func(*args, **kwargs);  
        print("Programme executed");
    return wrapper;

@decorator
def greet(a,b):
    res1 = a+b;  #Addition
    res2 = a*b;  #Multiplication
    print(res1);
    print(res2);
greet(4,5); 
