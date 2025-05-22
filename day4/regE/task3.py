import re
text="welcome to SIT"
a=re.search(r"SIT",text)
print(a.start());
print(a.end());