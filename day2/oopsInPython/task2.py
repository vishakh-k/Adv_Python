class Sit:
    def display(self):
        pass

class MCA(Sit):
    def display(self):
        print("Welcome to MCA department");

class MBA(Sit):
    def display(self):
        print("Welcome to MBA department");

class CSE(Sit):
    def display(self):
        print("Welcome to CSE department");

class ECE(Sit):
    def display(self):
        print("Welcome to ECE department");

obj = [MCA(),MBA(),CSE(),ECE()];

for i in obj:
    i.display();