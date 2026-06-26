## Program 3 — Student Record System (9 marks)

# **File name:** `student_record.py`

# Write a program for **student academic record** that:
# 1. Creates a dictionary `student` with:
#    - `"name"` → `"Ali"`
#    - `"roll_no"` → `102`
#    - `"subjects"` → a list of 3 subjects (e.g. `["Math", "English", "Python"]`)
# 2. Displays the **full student dictionary**
# 3. Displays only the **2nd subject** from the subjects list
# 4. Displays the **total number of subjects** in the list

student={"name": "ali",
         "roll_no": 102,
         "subjects":["maths", "english","python"]}
print(student)
print(student["subjects"][1])
print(len(student["subjects"]))
print(student ["name"])



    