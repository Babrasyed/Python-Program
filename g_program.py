# Write a Python program to create a menu-based calculator using a while loop.

# The program should display the following menu:
# 2. Subtraction
# 1. Addition
# 3. Multiplication
# 4. Division
# 5. Exit

# The user will enter a choice from the menu. According to the selected option, the program should take 
# two numbers as input and perform the required operation.

# The calculator should continue running until the user selects the Exit option.

# If the user enters an invalid choice, display an appropriate message.

choice = 6
while choice !=5:
    
    print("""            press 1 for addition:
            press 2 for substraction
            press 3 for multiplication
            press 4 for division
            press 5 for exit to stop""")
    choice= int(input("press the button:"))
    number1=int(input("enter your number1:"))
    number2=int(input("enter your number2:"))
    if choice ==1:
        result= number1+number2
        print(f"addition={number1}+{number2}")
        print(f"result= {result}")
    if choice == 2:
        result= number1-number2
        print(f"subraction={number1}-{number2}")
        print(f"result= {result}")
    if choice == 3:
        result= number1*number2
        print(f"multiplication={number1}*{number2}")
        print(f"result= {result}")
    if choice == 4:
        result= number1/number2
        print(f"division={number1}/{number2}")
        print(f"result= {result}")
    if choice == 5:
        result= exit
    

# password = ""
# count=0
# while password != "admin":
#     if count != 4:
#         password =input("enter password : ")
#     else:
#         print("4 attemps")
#         break
        
#     print("running......")
#     count+=1
    
# for i in range(1,10):
#     if i==5:
#         break
#     print(i)

                                                    #next

# list1=["aqib","babra","amna"]
# for i in list1:
#     print(i)
# item = []
# n=int(input("how much enteries : "))
# for i in range(1,n+1):
#     employee_name=input("Enter employee name : ")
#     item.append(employee_name)
# print(item)

item = []
n=int(input("how much enteries : "))
for i in range(1,n+1):
    employee_name=input("Enter employee name : ")
    item.append(employee_name)
print(item)