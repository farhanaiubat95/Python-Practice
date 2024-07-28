#set methods
#set - mutable
#element is unique and immutable(hashable)
#unhashable - dict , list , set
Set=set()

#add an element
Set.add(1) # passing element
Set.add(2)
Set.add(2)
Set.add(("tuple","use"))
Set.add(3)
print("Add : ",Set)
print("Set Length : ",len(Set))

#removes the element
print()
Set.remove(1) # passing element
print("Remove : ",Set)
print("Set Length : ",len(Set))


#empties the set
print()
Set.clear()
print("Clear : ",Set)
print("Set Length : ",len(Set))

#removes a random value
print()
Set={"Me",6,"I",2,3}
print("Set : ",Set)
Set.pop()
print("Pop : ",Set)
print("Set Length : ",len(Set))

#Union - combines both set values & returns a new set
Set1={1,2,3}
Set2={2,3,4}
print()
print("Set1 : ",Set1)
print("Set2 : ",Set2)
print("After union new set : ",Set1.union(Set2)) #give us new set
print("Check set1 : ",Set1)


#intersection - combines common values & returns a new set
print()
print("After intersection new set : ",Set1.intersection(Set2))