#Property decorator
class Student:
    def __init__(self, phy, chem, math):
        self.phy=phy
        self.chem=chem
        self.math=math
    
    #def calcPercentage(self):
    #    self.percentage=str((self.phy+self.chem+self.math)/3)+"%"

    @property
    def percentage(self):
        return str((self.phy+self.chem+self.math)/3)+"%"

s1=Student(100,97,56)
print(s1.percentage)
s1.math=100
print(s1.percentage)
