# Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

list = ['abc', 'xyz', 'aba', '1221']

c = 0
for x in list:
    if len(x) >= 2:
        if x[0] == x[len(x)-1]:
            c = c+1

print(c)
