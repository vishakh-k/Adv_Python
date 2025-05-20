def operation(a, b):
    def add():
        print(a + b);
    return add;
obj=operation(2,4);
obj();
