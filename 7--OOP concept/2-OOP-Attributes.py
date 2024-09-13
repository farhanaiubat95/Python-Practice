#Class & Instance Attributes
class Student:
    college_name="Farhana College." #class attributes & save it one time inside memory
    name="ABC" #class Attribute
    def __init__(self,name):
        self.name=name #object/instance attribute - different for all object
        print("This is ",self.name,"'s college..")

s1=Student("Efah")
print(s1.college_name) # two way cab be called
print(Student.college_name)
print(s1.name)


#if same "name" -for class & object attributes , then
# Obj > class attributes
