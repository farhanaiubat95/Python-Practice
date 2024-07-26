#Coditional statements (if-elif-else)
age=35

if(age<=12):
    print("Child")
elif(age<=20):
    print("teneger")
elif(age<=30):
    print("Young")
else:
    print("older day by day")


#Single Line if/Ternary Operator
#<var>=<val1> if <condition> else <val2>
print()
car="BMW"
code="1020 code" if car=="BMW" else "no data present"
print("Car has",code)

food= "Burger"
print(food ,"is Spicy.") if food =="Burger" or food=="Pizza" else print(food,"is not spicy")

#Clever if/Ternary Operator
#<var> = (false_val,true_val) [<condition>]
print()
Age=int(input("Age : "))
vote=("yes","no") [Age<18]
print(vote)

print()
salary=float(input("Salary : "))
tax=salary*(0.1,0.2) [salary>20000]
print(tax)