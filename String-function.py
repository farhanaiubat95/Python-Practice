#String Function
str= "tech Codism with Farhana"
#str.endswith("last part")- returns "true" if string ends with substr
print(str.endswith("Farhana"))

#str.capitalize()- Capitalizes 1st char
print()
print("Capitalizing 1st character : ",str.capitalize())
print(str)

#str.replace(old,new) - replaces all occurrences of old with new
print()
print("Replace Farhana to Bente : ",str.replace("Farhana","Bente"))
print("Replace a to o : ",str.replace("a","o"))

#str.find("word") - returns 1st index of 1st occurrence
print()
print("Find C : ",str.find("C"))
print("Find P : ",str.find("P")) #not valid - ans : -1

#str.count("") - counts the occurrences of substr in string
str= "tech Codism with Farhana with you."
print()
print(str)
print("Count a : ",str.count("a"))
print("Count with : ",str.count("with"))
