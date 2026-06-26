# ## Program 1 — Student Registration System (9 marks)

# **File name:** `student_registration.py`

# Write a program for **new student registration** that:
# 1. Asks for **student name**
# 2. Asks for **roll number** (store as a whole number)
# 3. Asks for **age** (store as a whole number)
# 4. Asks for **class** (e.g. `"10-A"`)
# 5. Displays a registration card like:

# ```
# --- Student Registered ---
# Name: Sara
# Roll No: 101
# Age: 16
# Class: 10-A

# student= 
# student_name:input("enter name:")
# roll_no:int(input("enter roll number:"))
# age:int(input("enter your age in numbers:"))
# class_name:input("enter your class:")

student={}
student["name"]=input("enter name:")
student["roll_no"]=int(input("enter roll number:"))
student["age"]=int(input("enter your age in numbers:"))
student["class_name"]=input("enter your class:")
# print("name :",student["name"])
# print(student["roll_no"])
# print(student["age"])
# print(student["class_name"])

for key,val in student.items():
    print(f"{key} : {val}")


