def addMul(a):
    def multiply(n):
        res = a*n;
        print(res);
    return multiply;
obj=addMul(10);
print(obj(5));