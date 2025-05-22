import re

text = "Python is best for AI and ML. Python developers love it."
updated_text = re.sub(r"\bPython\b", "Java", text)

print("Updated Text:", updated_text)
