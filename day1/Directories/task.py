import os

print("Current Working Directory:", os.getcwd())

print("List of Files and Directories:", os.listdir())

dir_path = r"D:\Java"  
if not os.path.exists(dir_path):  
    os.mkdir(dir_path)
    print(f"Directory '{dir_path}' created.")
else:
    print(f"Directory '{dir_path}' already exists.")

os.chdir(dir_path)
print(f"Changed working directory to: {os.getcwd()}")

print("Current Working Directory:", os.getcwd())

#abc=os.remove(r"D:\Adv_Python\basics\star1.py");
#if not abc:
    #print("File removed");
#else:
    #print("File is not deleted");

abc=os.rmdir(r"D:\studentprofile");
if not abc:
    print("File removed");
else:
    print("File is not deleted");