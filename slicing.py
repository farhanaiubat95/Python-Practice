#slicing- from index - 
# str[starting_idx:ending_idx] - here ending_idx is not included
str="Farhana"
print("str[1]:str[4] : ",str[1:4])

#str[ :4] is same as str[0:4]
print()
print("str[0]:str[4] : ",str[:4])

#str[1:] is same as str[0:len(str)]
print()
print("str[1]:str[~] : ",str[1:])
print()
print("str[4]:str[~] : ",str[4:])

#Negative index - start from -1 = -5, -4, -3, -2, -1
print()
print("str[-5]:str[-1] : ",str[-5:-1])
