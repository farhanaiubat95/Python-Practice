#Loop - 2 types = "While" , "For"
count=1 # called Iterator
while count<=5: 
    print("Number",count) #process called Iteration
    count+=1

#traverse
print()
nums= [1,2,3,"list","print"]
i=0
while i<len(nums):
    print(nums[i])
    i+=1

#search
#break
print()
nums= [1,2,3,50,30,399]
print(nums)
i=0
# x=int(input("Search : "))
x=3
while i<len(nums):
    if(nums[i]==x):
        print("Found ",x," in index",i)
        break
    else:
        print("$")
    i+=1

#continue
print()
i=0
while i<=10:
    if(i%2==0):
        i+=1
        continue #skip
    print("Odd : ",i)
    i+=1