#dictionary -- Unordered , mutable , don't allow duplicate "dict keys"
#store data values in ( key:value ) pairs
#here, key is never be list , but rest of the types are acceptable

student={
    "Name":"Farhana",
    "Age" :25,
    "weight": 55.5,
    "Marks" : (10,20,23,56,70),
    "Hobby" : ["Coding","Dancing","Drawing"],
    "Love someone?" : True,
    12: "times run.."
    
}
print(student)
print(student["Name"])

#add new key value
#change any value
student["Fail"]="Last Time"
student["weight"]="60"
print()
print(student)

#nested dictionary
student={
    "Name":"Farhana",
    "sub":{
        "Biology":100,
        "chem":49,
        "Math":70
    }
}
print()
print("Dictionary : ",student)
print("Subject : ",student["sub"])
print("Chemistry mark : ",student["sub"]["chem"])