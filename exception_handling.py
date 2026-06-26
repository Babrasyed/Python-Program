# num1=6
# num2=0
# result=num1/num2
# print(result)

try:
    num1=int(input("enter a num:"))
    num2= int(input("enter a num2:"))
    result=num1/num2
except Exception as e:
    print(e)
    
print("result")


#fILE hANDLING
with open("abc.txt","r") as file:
    print(file.readline())

    
with open("abc.txt","r") as file:
    for line in file:
        print(line)