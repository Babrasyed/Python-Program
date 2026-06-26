# Employee management System
def add_employees():
    name=input("enter your name:")
    employee_id=input("enter your id:")
    salary=input("enter your salary:")
    with open ("employee.txt","a") as file:
        file.write(f"{name}, {employee_id}, {salary} \n")
def view_employees():
    with open ("employee.txt","r") as file:
        print(file.read())

view_employees()


print("""press 1 for adding employee
          press 2 to show employee list
          press 4 to exit""")
choice=0
while choice != 4:
   
    choice=int(input("press the button:"))
    if choice == 1:
        add_employees()
    elif choice == 2:
       view_employees()
    elif choice == 4:
        print("Exit")
        break    
    else:
        print("invalid choice")