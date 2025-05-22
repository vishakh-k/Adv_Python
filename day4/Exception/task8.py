class Division(Exception):
    def __init__(self, msg):
        self.msg = msg
        super().__init__(self.msg)

try:
    num = int(input("Enter the number: "))  
    if num<0:
        raise Division("Number is negative. Please enter a positive number.")
except Division as e:
    print(e);
