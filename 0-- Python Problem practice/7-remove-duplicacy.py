# Write a Python program to remove duplicates from a list.
list = [4, 5, 6, 3, 2, 3, 1, 4, 5]
list1 = []

list.sort()

for x in range(0, len(list)-1):
    if list[x] != list[x+1]:
        list1.append(list[x])
print(list1)
