class Operation:
    def __init__(self, filename, mode, content=None):
        self.filename = filename
        self.mode = mode
        self.content = content

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print(f"An exception occurred: {exc_value}")
        

        if hasattr(self, 'file'):
            self.file.close()
            print("File is closed.")


        return True  

with Operation("D:\Adv_Python\ContextManager\example.txt", "w") as file:
    file.write("This is a file written using a context manager.")


print("File operations are done.")
