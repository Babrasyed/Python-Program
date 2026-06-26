# # parent class
#Single inheritence
# class Animal:
    
#     def __init__(self,name,age,gender):
#         self.name=name
#         self.age=age
#         self.gender=gender
        
#     def displayInfo(self):
#         print(self.name,self.age,self.gender)
    
#     def eat(self):
#         print("Animal is eating...")
        
# # child class        
# class Dog(Animal):
    
#     def __init__(self,name,age,gender,breed):
#         super().__init__(name,age,gender)
#         self.breed=breed
   
    
#     def bark(self):
#         print("Dog is barking...")
        
#     def eat(self):
#         super().eat()
#         print("Dog is eating...")
        
# dog1=Dog("Tommy",24,"male","German Shepherd")
# # print(dog1.name)
# # print(dog1.breed)
# # dog1=Dog("German Shepherd")
# dog1.eat()
# # dog1.displayInfo()
# # animal1=Animal("Cat",23,'female')

# # animal1.displayInfo()
# # dog1=Dog()
# # dog1.bark()
# # dog1.eat()



#Hierarical inhereitence

# class Employee:
#     def __init__(self, name, salary):
#         self.name=name
#         self.salary=salary
#     def view_info(self):
#         print(self.name, self.salary)
# class Manager(Employee):
#     def __init__(self, name, salary, department):
#         super().__init__(name, salary)
#         self.department=department
#     #methodoverridding
#     def view_info(self):
#         super().view_info()
#         print(self.department)

# class Developer(Employee):
#     def __init__(self, name, salary,language):
#         super().__init__(name, salary)
#         self.language=language
        
#     #methodoverridding
#     def view_info(self):
#         super().view_info()
#         print(self.language)


    
# dev1=Developer("malik aqib keera",40,"python")
# dev1.view_info()

# multiple inheritence
class Employee:
    def __init__(self, name, salary):
        self.name=name
        self.salary=salary
    def view_info(self):
        print(self.name, self.salary)

class Benefits:
    def __init__(self, medical_allowance):
        self.medical_allowance=medical_allowance
    def view_info(self):
        print(self.medical_allowance)

class Manager(Benefits,Employee):
    def __init__(self, name, salary, department,medical_allowance):
        Employee.__init__(self,name, salary)
        Benefits.__init__(self,medical_allowance)

        self.department=department
    #methodoverridding
    # def view_info(self):
    #     view_info()
    

        # print(self.department)

# class Developer(Employee):
#     def __init__(self, name, salary,language):
#         super().__init__(name, salary)
#         self.language=language
        
    #methodoverridding
    # def view_info(self):
    #     super().view_info()
    #     print(self.language)

men1=Manager("malik aqib keera",40,"python","OPD")
Employee.view_info(men1)
Benefits.view_info(men1)

# Multi Inheritance
class Grandparent:
    def legacy(self): return "Old Gold"

class Parent(Grandparent):
    def business(self): return "Factory"

class Child(Parent):