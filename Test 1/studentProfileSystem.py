## Program 2 — Student Profile System (9 marks)

# **File name:** `student_profile.py`

# Write a program for **student profile** that:
# 1. Asks for **student full name**
# 2. Shows **how many characters** are in the name
# 3. Shows the **first** and **last** character of the name
# 4. Asks for **school name** and displays a welcome message by joining the texts:

# ```
# Welcome, Sara! You study at City School.

full_name= input("enter your full name:")
print(len(full_name))
print(f"first character: {full_name[0]}")
print(f"last character: {full_name[-1]}")
school=input("enter your school name:")
print(f"Welcome, {full_name}! you study at {school}")