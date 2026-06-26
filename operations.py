# #Calculated program first test
# print("press 1 for addition") 
# print("press 2 for subraction")
# print("press 3 for multiplication")
# print("press 4 for division")
# # choice=int(input("choose any operation:")) # choose variable
# number1=int(input("enter number 1: "))    #int for intigers
# number2=int(input("enter number 2: "))
# if choice == 1: 
#     result=number1+number2
#     print(f"result:{result}")
# if choice == 2:
#     result=number1-number2
#     print(f"result:{result}")
# if choice == 3:
#     result=number1*number2
#     print(f"result:{result}")
# if choice == 4:
#     result=number1/number2
#     print(f"result:{result}") #formated string
# else:
#     print("please enter correct value")

    #practice

print("""press 1 for multiplication
press 2 for subtraction
press 3 for division""")
choice= int(input("press the button:"))
number1=int(input("enter your number1:"))
number2=int(input("enter your number2:"))
number3=int(input("enter your number3:"))
number4=int(input("enter your number4:"))
if choice ==1:
    result= number1*number2*number3*number4
    print(f"multiplictaion={number1}*{number2}*{number3}*{number4}")
    print(f"result= {result}")
if choice == 2:
    result= number1-number2-number3-number4
    print(f"subraction={number1}-{number2}-{number3}-{number4}")
    print(f"result= {result}")
if choice == 3:
    result= number1/number2/number3/number4
    print(f"division={number1}/{number2}/{number3}/{number4}")
    print(f"result= {result}")






    # parent class
class Animal:
    
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        
    def displayInfo(self):
        print(self.name,self.age,self.gender)
    
    def eat(self):
        print("Animal is eating...")
        
# child class        
class Dog(Animal):
    
    def __init__(self,name,age,gender,breed):
        super().__init__(name,age,gender)
        self.breed=breed
   
    
    def bark(self):
        print("Dog is barking...")
        
    def eat(self):
        super().eat()
        print("Dog is eating...")
        
dog1=Dog("Tommy",24,"male","German Shepherd")
# print(dog1.name)
# print(dog1.breed)
# dog1=Dog("German Shepherd")
dog1.eat()
# dog1.displayInfo()
# animal1=Animal("Cat",23,'female')

# animal1.displayInfo()
# dog1=Dog()
# dog1.bark()
# dog1.eat()


print("---------------------------------------------------")