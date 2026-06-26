# ### 1. Division Calculator
# * Take two numbers from the user.
# * Divide the first number by the second number.
# * Handle ZeroDivisionError if the second number is zero.

# ### 2. Number Input Validation

# * Take a number from the user.
# * Handle ValueError if the user enters invalid input (like text instead of a number).
# * If the input is valid, print the square of the number.

# ### 3. List Index Access

# * Create a list of 5 items.
# * Ask the user to enter an index.
# * Handle IndexError if the index is out of range.
# * If valid, print the item at that index.

# num1=int(input("enter a number:"))
# num2=int(input("enter a number:"))
# try:
#     division=num1/num2
#     print(division)
#     print(type(division))

# except Exception as e:
#     print(e)

list1=[1,2,3,4,5]
try:
    index=int(input("enter index:"))
    print(list1[index])
except IndexError:
    print("list index out of range")


