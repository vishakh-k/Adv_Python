class Operation:
    def __init__(self,a,b):
        self.a=a;
        self.b=b;
    #addition
    def add(self):
        return self.a+self.b;
    #substraction
    def sub(self):
        return self.a-self.b;
    #multiplication
    def mul(self):
        return self.a*self.b;
    #devision
    def div(self):
        return self.a/self.b;

obj1=Operation(8,4);
print(obj1.add());
print(obj1.sub());
print(obj1.mul());
print(obj1.div());