#Arithmatic Operators ( +, -, *, /, %, **(power operator))
A=20
B=2
print("sum = ",A+B)
print("Sub = ",A-B)
print("Mul = ",A*B)
print("Div = ",A/B)
print("Mod = ",A%B)
print("Power A^B = ",A**B)

#relational operators ( == , != , > , >= , < , <=)
a=100
b=50
print()
print(a," equal ",b," = ",a==b)
print(a," not equal ",b," = ",a!=b)
print(a," greater than ",b," = ",a>b)
print(a," greater than equal ",b," = ",a>=b)
print(a," less than ",b," = ",a<b)
print(a," less than equal ",b," = ",a<=b)

#Assignment operators ( = , += , -= , *= , /= , %= , **=)
c=30
c+=3 #c= c+3
print()
print("+ equal to = ",c)
c=30
c-=3 #c= c-3
print("- equal to = ",c)
c=30
c*=3 #c= c*3
print("* equal to = ",c)
c=30
c/=3 #c= c/3
print("/ equal to = ",c)
c=30
c**=3 #c= c**3
print("++ equal to = ",c)

#Logical operators( not , and , or)
print()
print("not False = ",not False) #True
print("not True = ",not True) #False

a=50
b=5
print()
print("not ",a,">",b," = ",not(a>b)) #False
print("not ",a,"<",b," = ",not(a<b)) #True

print()
val1=True
val2=False
print("and operator between",val1," and ",val2," : ",val1 and val2)
print("or operator between",val1," or ",val2," : ",val1 or val2)
print("Consider expression between (not", val1," and ",val2," or ",val1,") : ",not val1 and val2 or val1)

print()
print("and operator between",a,"==",b," and ",a,">",b," : ",(a==b) and (a>b))
print("or operator between",a,"==",b," or ",a,">",b," : ",(a==b) or (a>b))

#Membership Operators(in, not in)

#Identity Operators(is, is not)

#Bitwise Operators(&(AND),|(OR), ^(XOR))