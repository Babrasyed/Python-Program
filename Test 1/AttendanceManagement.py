# ## Program 4 — Attendance Management System (9 marks)

# **File name:** `attendance_system.py`

# Write a program for **daily attendance** that:
# 1. Asks how many students are present today (e.g. `6`)
# 2. Takes **roll number** of each present student (one by one) and stores in a **list**
# 3. Remove duplicate roll numbers if entered twice (keep only unique ones)
# 4. Displays:
#    - `Attendance list:` followed by the list
#    - `Unique students present:` followed by the unique roll numbers
#    - `Total unique present:` followed by how many unique students

# ---
present_student=[]
n=int(input("how many students are present:"))
for i in range(1,n+1):
    roll_no=int(input("enter roll number:"))
    present_student.append(roll_no)

set1=set(present_student)

print(f"attendnce list: {present_student}")
print(f"unique students present: {set1}")
print(f"total unique students present:{len(set1)}")





