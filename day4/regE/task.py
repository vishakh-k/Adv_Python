import re

text1 = "vishakhkt2003@gmail.com"
p1 = r"^[a-zA-Z0-9._%+-]+@gmail\.com$"

text2 = "+91 123-267-9876"
p2 = r"^\+91\s\d{3}-\d{3}-\d{4}$"

if re.findall(p1, text1):
    print("Valid Gmail")
else:
    print("Invalid Gmail")

if re.findall(p2, text2):
    print("Valid PhoneNumber")
else:
    print("Invalid PhoneNumber")

