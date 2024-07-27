#list slicing
#list_name=[starting_idx:ending_idx]- here ending_idx is not included
marks=[10,20,30,40,50] #marks[0], marks[1]
print(marks)
print()
print("Marks index from 1 to 4 : ",marks[1:4])

#list[ :4] is same as list[0:4]
print()
print("marks[0]:marks[3] : ",marks[:3])

#list[1:] is same as list[0:len(str)]
print()
print("marks[1]:marks[~] : ",marks[1:])
print()
print("marks[3]:marks[~] : ",marks[3:])

#Negative index - start from -1 = -5, -4, -3, -2, -1
print()
print("marks[-5]:marks[-1] : ",marks[-5:-1])