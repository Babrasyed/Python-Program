#object oriented programming
# to organize the programe
# real world entity is object
# e.g employee is an object  what funtions can be performed with it.it's functionalities.
# Class is properties and funtion of object. it is a blueprint of object 
class Employee:
    name=""
    age=""
    department=""
    
    def add_employee(self):
        print("employee added")
    
emp1=Employee()
emp1.add_employee()



 class Employee:
#     def __init__(self,name,salary,department):
#         self.name=name
#         self.salary=salary
#         self.department=department

# emp1=Employee()

# emp1=Employee("babra",55000,"HR")
# emp2=Employee("sdfas",55000,"HR")
# emp3=Employee("sdfsad",55000,"HR")
# emp4=Employee("sdfsa",55000,"HR")
# emp5=Employee("sadfsd",55000,"HR")


# print(emp1.name,emp1.salary,emp1.department)
    
class Employee:
    
    def __init__(self,name,salary,age):
        self.name=name
        self.salary=salary
        self.age=age
      
    def view_detail(self):
        print(self.name,self.salary,self.age)
        
emp1=Employee("lumri",55000,24)


emp2=Employee("bandri",55000,24)
emp3=Employee("churail",55000,24)
# print(emp1.name,emp1.salary,emp1.age)
# print(emp2.name,emp2.salary,emp2.age)
# print(emp3.name,emp3.salary,emp3.age)
emp1.view_detail()
emp2.view_detail()
emp3.view_detail()