file = open("D:\Adv_Python\ContextManager\example.txt","w")

file.write("hello")
file.writelines("hello"
"sjdksajdk\n"
"saldalskmdklasd\n"
"dwjkjsndn")


file = open("D:\Adv_Python\ContextManager\example.txt","r")

print(file.seek(10));
print(file.tell());
print(file.read());

file.close();