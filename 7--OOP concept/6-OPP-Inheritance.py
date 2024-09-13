#Inheritance
class Car:
    def __init__(self,type):
        self.type=type
    
    @staticmethod
    def start():
        print("Car started...")

    @staticmethod
    def stop():
        print("Car stpped...")

class Toyota(Car):
    def __init__(self,name,type):
        super().__init__(type) # super is used for calling constructors
        self.name=name

car=Toyota("BMW","solid")
print("Car name : ",car.name)
print("Car type : ",car.type)
car.start()