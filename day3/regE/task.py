import re
text = "Hy python developer"
p = "dev"
abc = re.search(p, text)
if abc:
    print("Found")
else:
    print("Not found")

