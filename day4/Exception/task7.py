class Division(Exception):
    def __init__(self, msg):
        self.msg=msg;
        super().__init__(self.msg)
try:
    passw=input("enter the password:");
    if len(passw)<6:
        raise Division("Password is lesser then 6 characters");
except Division as e:
    print(e);