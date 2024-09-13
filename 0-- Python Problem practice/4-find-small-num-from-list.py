# Write a Python program to get the smallest number from a list.
items = [4, 5, 6, 3, 2, 1]

items.sort(reverse=True)  # descending

length = len(items)
print("Largest number is : ", items[length-1])
print("Largest element is:", min(items))
print("Largest number is : ", items[-1])
