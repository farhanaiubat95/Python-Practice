#tuple - immutable 
tup=(1,2,3,4,5)
print("Tuple : ",tup)

#if tuple has a single value, thn write tup=(1,)
print()
tup=(1,)
print("Single tuple : ",tup)

#tuple slicing
print()
tup=(1,2,3,4,5,2)
print("tup[1]:tup[3] : ",tup[1:3])

#tuple method- tup.index(el)- returns index of first occurrence
print() 
print("Find 2 : ",tup.index(2))
print("Count 2 : ",tup.count(2))