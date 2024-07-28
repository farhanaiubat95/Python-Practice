#Loops are used for sequential traversal.
#For traversing list , string , tuples
List=[1,2,3]
Tupple=("One","Two","Three")
String="Farhana"
print("Print the list :")
for val in List:
    print(val)

print("Print the Tupple :")
for val in Tupple:
    print(val)

print("Print the String :")
for val in String:
    print(val)


#for loop  with else
print()
print("Print the list :")
for val in List:
    print(val)
else:
    print("END")


#Linear Search
print()
nums=[20,35,6,8,9,9]
x=6
idx=0
for val in nums:
    if(val==x):
        print(x," - found..")
        print("Number found at index : ",idx)
    idx+=1


#range() - give a sequence numbers, starting from 0 & increments by 1(by default) & stop before a specified number.
#range(start?,stop,step?)
print()
Seq=range(3)
for i in Seq:
    print("Range : ",i)

print()
for i in range(5):
    print("Range1 : ",i)

#wriitng style - 3 types 
print()
for i in range(5): #range(stop)
    print("Range(stop) : ",i)

print()
for i in range(2,5): #range(start, stop)
    print("Range1(start,stop) : ",i)

print()
for i in range(10,2,-3): #range(start, stop)
    print("Range1(start,stop,step) : ",i)


#Pass Statement- null statement that does nothing.
#It is used as a placeholder for future code
print()
for i in range(5):
    pass
print("skip loop..")