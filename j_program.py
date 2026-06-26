Students={}
n=int(input("hown many students:"))
for i in range(1,n+1):
    student=input("enter student name:")
    mark=input("enter marks:")
    Students[student]=mark
print(Students)