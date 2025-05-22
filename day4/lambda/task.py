# In Python, lambda is used to create anonymous functions, which are functions without a name. These are typically used for short, simple functions that are passed as arguments to higher-order functions like map(), filter(), or sorted().

def function(a,b):
    print(a+b);

function(10,20)

num=lambda a,b:a+b
print(num(10,20));