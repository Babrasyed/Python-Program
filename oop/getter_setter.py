#GEtter SETTER:

class Student:
    def __init__(self,name,marks):
        self.__name=name
        self.__marks=marks
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name=name
        
    #getter
    def get_marks(self):
        return self.__marks
    
    
    #setter 
    def set_marks(self,value):
        if value>0 and value < 100:
            self.__marks=value
        else:
            print("invalid value")
            

student=Student("babra",90)
student.name="aqib"
print(student.name)

student.mark=-12
print(student.marks)


# student.set_marks(0)
# marks=student.get_marks()
# print(marks)

