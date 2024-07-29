#Function
#Block of statements that perform a specific task
# def - define
#def func(param1,param2): return val

def call_sum(a, b): #parameters 
    sum=a+b
    print(sum)
    return sum
call_sum(5,10) #function call; arguments
call_sum(10,20)
call_sum(20,30)

#null parameters
print()
def write():
    print("TCWF")

write()

#list
name=["Farhana","priya","Diya"]
roll=[10,20,30,40]

def print_len(list):
    print(len(list))

print_len(name)
print_len(roll)

#print list element in a single line
print()
print("List : ",end=" ")
def print_list(list):
    for item in list:
        print(item,", ",end=" ")
print_list(name)
