#Print Command-------1
print("Hi, It's 26th July...")

#Variable Declare & Print-------2
name="Farhana"
Age= 25
price=20.25
print()
print("My Name is", name,". My age is ",Age,". My Books Price is ",price,"TK. ");

#Type Declare in output-------3
answer= True
print()
print(type(name))
print(type(Age))
print(type(price))
print(type(answer))

#Expression Execution-------4
A,B,C=10,2,20
D=A*C+B
Txt="#"
print()
print(A*Txt*B, A*B)
print(A+B*C) #Arithmetic Expression
print(D)

#another example 4.1 of -------4
A,B="10",2
Txt="@"
print()
print((A+Txt)*B) #Here used "+"---it's called Concatenation

#Division Operator
Div1=B/C
print()
print(Div1) #ans will be float

#Integer Division with float & int will give int displayed as float
A,B,C,D=1.5,4,5,-6
Div2=A//B
print()
print(Div2, A/B)

#Result of (B//C) is same as floor(B/C) , must give lesser or equal value.
#5.2-> 5 , -5.2-> -6 , 0.1->0
print(B//C)
print(D//C)
print(C//D)


"""For remainder is negative when denominator is negative
(+%+ = +), (-%- = +), (+%- = -), (-%+ = +)"""
print()
print(B%C)
print(D%C)
print(C%D)