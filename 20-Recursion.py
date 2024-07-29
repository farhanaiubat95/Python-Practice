#Recursion - When a function calls itself repeatedly
def Show(n):
    if(n==0): #Base Case - must give like loop condition
        return #control return
    print(n)
    Show(n-1)
    print("END") # print END when n== 1, 2, 3 repeated , after n==0 return and stop
Show(3)

#factorial
print()
print("Numbers : ",end=" ")
def Fact(n):
    if(n==1 or n==0):
        return 1
    print(n,end=" ")
    return Fact(n-1) * n
  
print("\nFactorial value is : ",Fact(4))


#Print sum of natural numbers
print()
print("Numbers : ",end=" ")
def Sum(n):
    if(n==0):
        return 0
    print(n,end=" ")
    return Sum(n-1)+n
    

print("\nTotal Sum : ",Sum(5))