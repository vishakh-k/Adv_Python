import re
text = "Python is best for AI and MLis Python"
p = r"\Bis"
abc = re.findall(p, text);
if abc:
    print("Found")
else:
    print("Not found")