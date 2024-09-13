#OOP 
#Class is a blueprint for creating objects.
#creating class 
#creating object(instance of class)
class Student:
    name="-----Operation"
    num = 1

s1=Student()
print(s1.name)
s2=Student()
print(s2.num)


#---Constructor - (init function)
#All classes have a function called __init__(), which is always executed when the object is being initiated.
print()
class Car:
    
    #default constructors
    def __init__(self):
        # print(self)
        print("-----Constructor Self pass..")

s1=Car()
print(s1)

#multiple parameter
print()
class Animal:

    #Parameterized constructors
    def __init__(self,name,price): #you can write different name instead of self
        self.name=name
        self.price=price
        print("-----Multiple constructor.")

s1=Animal("Cat",100) # "cat" - This data is called -" Attributes "
print(s1.name,s1.price)