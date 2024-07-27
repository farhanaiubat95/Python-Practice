#list method
list=[1,2,44,7,6,8,89]
print(list)

#list.append() - adds one element at the end
print()
list.append(90)
print("append 90 : ",list)

#sorting - list.sort() -Ascending
print()
list.sort()
print("Ascending Sort : ",list) 

# descending
print()
list.sort(reverse=True)
print("Descending Sort : ",list) 

# sort - works  also in characters
letter=['a', 's','t',"farhana","bannana"]
letter.sort()
print()
print("Sorting : ",letter)

#reverse
print()
letter.reverse()
print("Reverse : ",letter)

#list.insert(idx,el)
print()
letter.insert(2,'w')
print("Insert w in indx[2] : ",letter)

#list.remove(el) - removes first occurrences of element
print()
letter.remove('w')
print("Remove indx[1] : ",letter)

#list.pop(idx) - removes element at idx
print()
letter.pop(2)
print("Pop indx[2] : ",letter)

