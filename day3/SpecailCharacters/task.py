import re
text="Welcome to 4546546 python world";
p=r"[a-z A-Z 0-9]";
ans=re.findall(p,text);
print(ans)