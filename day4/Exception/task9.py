class Student(Exception):
    def __init__(self, msg):
        self.msg = msg
        super().__init__(self.msg)

try:
    mark = input("Enter marks: ")

    if not mark.isdigit():
        raise Student("Invalid input. Please enter a positive integer.")

    mark = int(mark)

    if mark < 0 or mark > 100:
        raise Student("Marks should be between 0 and 100.")

    if mark > 90:
        print("Grade is A")
    elif mark > 70:
        print("Grade is B")
    elif mark > 35:
        print("Grade is C")
    else:
        print("Student Failed")

except Student as e:
    print("Error:", e)
