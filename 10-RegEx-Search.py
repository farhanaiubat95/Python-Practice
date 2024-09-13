#RegEx
import re

#Check if the string starts with "The" and ends with "Spain":
txt = "Tech codism with farhana"
x = re.search("^Tech", txt) #First word "^word"
Y = re.search(".*farhana$", txt) #last word ".*word$"

if x:
  print("YES! First word match")
if Y:
  print("YES! Last word match")
else:
  print("No match")


#The findall() Function
#The findall() function returns a list containing all matches.
x = re.findall("a", txt)
print()
print(x)

#The search() Function
#The search() function searches the string for a match, and returns a Match object if there is a match.
#If there is more than one match, only the first occurrence of the match will be returned:
txt = "Tech codism with farhana"
x = re.search("\s", txt)
print()
print("The first white-space character is located in position:", x.start())


#The split() Function
#The split() function returns a list where the string has been split at each match:
x=re.split("\s",txt,1)
print()
print(x)


#The sub() Function
#The sub() function replaces the matches with the text of your choice:
txt="Tech codism with Farhana"
x=re.sub("\s","\t3",txt)
y=re.sub("\s","\t2",txt,2)
print()
print(x)
print(y)


#For search
#span()
print()
x = re.search("c\w+", txt)
print(x.span())

#string
print()
x = re.search(r"\bc\w+", txt)
print(x.string)

#group()
print()
x = re.search(r"\bF\w+", txt)
print(x.group())

