class Student:
    school= "PAEC Model College"
    @staticmethod
    def welcome_student():
        print(f"Welcome to {Student.school}")
    def __init__(self,name, age,marks):
        self.name= name
        self.age= age
        self.marks= marks
    def grade(self):
        if self.marks >= 90:
            print("Grade A")
        elif self.marks >= 80:
            print("Grade B")
        elif self.marks >= 70:
            print("Grade C")
        else:
            print("FAIL")
stud1=Student("Babra",23,99)
print(stud1.name)
print(stud1.age)
print(stud1.marks)
stud1.grade()
print(stud1.school)
stud1.welcome_student()
