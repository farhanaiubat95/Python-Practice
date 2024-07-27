#Dictionary methods
car={
    "Car Name":"BMW",
    "Size": 40,
    "color":"Blue"
}

#myDict.keys() - returns all keys
print()
print("Dict keys : ",car.keys())
print("Dict to list : ",list(car.keys()))
print("Length of dict : ",len(car))


#myDict.values() - returns all values 
print()
print("Dict values : ",car.values())
print("Dict to list : ",list(car.values()))

#myDict.items() - returns all (key,val)pairs as tuples 
print()
print("Dict items : ",car.items())
print("Dict to list : ",list(car.items()))

#myDict.get("key") - returns the key according to value
print()
print("Dict get : ",car.get("Size"))
print("Directly print : ",car["Size"])

#myDict.update() - inserts the specified items to the dictionaryprint()
print()
car.update({"Code":"1020"})
print("Dict update single details: ",car)

car_update= {"Code":"1020","Year":2020,"Car Name":"Tesla"}
car.update(car_update)
print("Dict update multiple details: ",car)