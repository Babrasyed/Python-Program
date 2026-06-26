# Question Statement: Employee Management System (Basic)

# Write a Python program to create a simple Employee Management System. The program should continuously
#  run and display a menu to the user.

# The system must perform the following tasks:

# Add an employee by taking only the employee name as input from the user.
# Store all employee names in a list.
# Display all stored employee names .
# Delete an employee by entering the employee name. If the name exists in the list, remove it; otherwise
#  show a message like "Employee not found."
# If no employee is added, display a message like "No employees found."
# Provide an option to exit the program.

# The program should show the following menu:

# 1. Add Employee
# 2. Show Employees
# 3. Delete Employee
# 4. Exit

# The program should keep running until the user selects the Exit (4) option.

# employee=[]
# n=int(input("enter no. of enteries to add:"))
# for i in range(1,n+1):
#     employee_name=input("enter employee name:")
#     employee.append(employee_name)
# print(employee)
# name_remove=input("enter name to be removed from the list:")
# if name_remove in employee:
#     employee.remove(name_remove)
#     print(employee)
# else:
#     print("employee not found")



# employees = []
# print("""press 1 for adding employee
#           press 2 to show employee list
#           press 3 to remove employee
#           press 4 to exit""")
# choice=0
# while choice != 4:
   
#     choice=int(input("press the button:"))
#     if choice == 1:
#         employee=input("enter employee name:")
#         employees.append(employee)
#         print("employee added to the list")
#     elif choice == 2:
#         # index=0
#         #  for i,v in enumerate(employees):
#         #         print(f"employee {i} is {v}")
#         for i in employees:
#             print(i)
#     elif choice ==3:
#         name_remove=input("enter employee name to remove:")
#         if name_remove in employees:
#             employees.remove(name_remove)
#             print(f"employee {name_remove} removed")
#         else:
#             print("employee name not found")
#     elif choice == 4:
#         print("Exit")
#         break    
#     else:
#         print("invalid choice")


# employee=[]
# epmloyee.append(employee_name)
        
# for i in employee:
#     employee_name=input("enter employee name:")
#     employee.append(employee_name)
# print(employee)
# name_remove=input("enter name to be removed from the list:")
# if name_remove in employee:
#     employee.remove(name_remove)
#     print(employee)
# else:
#     print("employee not found")

# list1=[23,45,34,45]
# temp=1
# for i in list1:
#     temp=temp*i
# print(temp)


# Write a Python program that uses a for loop to take multiple student marks from the user and store them 
# in a list.

# The program should first ask how many students' marks the user wants to enter. Then, using a for loop, 
# it should take marks of each student one by one.

# After collecting all the marks, display:
# - All marks in a list
# - Highest marks
# - Lowest marks
# - Total marks
marks=[]
# students=[]
n=int(input("how many marks you want to enter:"))
for i in range(1,n+1):
    # student_name=input("enter student name:")
    # students.append(student_name)
    mark=int(input("enter marks:"))
    marks.append(mark)
print(f"Marks:{marks}")
# mark=0
# for i in marks:
#     mark=mark+i
# print(f"Total Marks: {mark}")
# print(max(mark))
max=marks[0]
for i in marks:
    if i>max:
        max=i
print(f"Max:{max}")
min=marks[0]
for i in marks:
    if i<min:
        min=i
print(f"Min:{min}")
    

        




# print("Highest Marks:", max(marks))
# print("lowest Marks:", min(marks))
# print("Total Marks:", sum(marks))
# print(len(marks))





