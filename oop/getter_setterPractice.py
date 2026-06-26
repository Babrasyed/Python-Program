class Employee:
    def __init__(self,name):
        self.name=""
        
        if len(name) <= 5:
            self.name=name
        
        else:
            print('"stick to the limit"')

    def set_name(self,name):
        if len(name) <= 5:
            self.name=name
        else:
            print("stick to the limit")
emp=Employee("babra")

emp.set_name("kuttyyyyyyyyy")
# print(emp.name)
emp.name="kkkkkkkkkkkkkkkkkkk"
# print(emp.name)