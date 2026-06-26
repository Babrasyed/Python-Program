# ## Program 6 — Marks Management System (7 marks)

# **File name:** `marks_management.py`

# Write a program for **student marks** that:
# 1. Write a function named **calculate_total** that takes 3 subject marks and gives back their total
# 2. Asks the user for marks in **Math**, **English**, and **Python**
# 3. Uses **calculate_total** and displays:

def calculate_total(maths,english,python):
    
    total_marks= maths+english+python
    return total_marks
maths= int(input("enter maths mark:"))
english= int(input("enter english marks:"))
python= int(input("enter python marks:")) 

total_marks=calculate_total(maths,english,python)
print(f"Total Marks: {total_marks}")



