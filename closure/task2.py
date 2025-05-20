def apply_operation(a, b):
    def add():
        print(a + b);
    return add;
obj=apply_operation(2,4);
obj();
