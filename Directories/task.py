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
