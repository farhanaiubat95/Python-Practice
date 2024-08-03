#Method works 3 typres
#1-static methods -when not touch any class or instance property
#2-Class methods (cls)
#3-Instance methods (self)

class Person:
    name="anonymous"

    #def changeName(obj, name):
    #    self.__class__.name = "Farhana"

    @classmethod #decorator
    def changeName(cls, name): #refering to the class
        cls.name=name

p1=Person()
p1.changeName("Efah islam")
print(p1.name)
print(Person.name)