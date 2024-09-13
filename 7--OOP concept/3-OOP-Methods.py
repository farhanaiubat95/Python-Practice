#OOP - Methods
class Car:
    def __init__(self,name,tier):
        self.name=name
        self.Tier=tier
    def welcome(self):
        print("Car name :",self.name)
    def tier(self):
        print("Car has",self.Tier,"tier")

c1=Car("BMW",4)
c1.welcome()
c1.tier()

#==find average marks
print()
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("Hi",self.name,".Your average score is : ",sum/3)

s1=Student("Farhana",[100,90,80])
s1.get_avg()
s2=Student("Riya",[74,90,80])
s2.get_avg()
s2.name="Diya" #directly can be changed
s2.get_avg()


#======static methods
#methods that don't use the self parameter(work at class level)
print()
class Vegetables:
    @staticmethod #decorator
    def print_name():
        print("I love fresh vegetables..")

v1=Vegetables()
v1.print_name()





























