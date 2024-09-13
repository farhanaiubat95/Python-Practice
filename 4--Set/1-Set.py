#set - unordered(no indx) , unique & immutable
#Never store " list & dictionary"
Set={1,2,4,5,"Hi"}
print("Set : ",Set)

#ignore duplicate items
print()
Set={1,2,2,4,5,"Hi","hi","love","love"} #not maintain any order
print("Set : ",Set)

#length
print()
print("Set Length : ",len(Set))

#empty set
print()
Set=set()
print("Empty set - set() : ",type(Set))

print()
Set={} # this is Dictionary not set
print("Empty Dict : ",type(Set))
