# String formatting
# F-string allows you to format selected parts of a string.
txt = f"The price is 49 dollars"
print(txt)


# Placeholders and Modifiers
# To format values in an f-string, add placeholders {},
# a placeholder can contain variables, operations, functions, and modifiers to format the value.
print()
price = 59
txt = f"The price is {price} dollars"
print(txt)


# A placeholder can also include a modifier to format the value.
# A modifier is included by adding a colon : followed by a legal formatting type,
# like .2f which means fixed point number with 2 decimals:
print()
price = 100
txt = f"The price is {price:.2f} dollars"
print(txt)

# direct display value without variable
txt = f"The price is {95:.2f} dollars"
print(txt)


# Perform Operations in F-Strings
print()
txt = f"The price is {20 * 20} dollars"
print(txt)

price = 100
tax = 40
txt = f"The price is {price + (price * tax)} dollars"
print(txt)


# if...else statements inside the placeholders
print()
price = 60
txt = f"It is very {'Expensive' if price > 50 else 'Cheap'}"
print(txt)


# Execute Functions in F-Strings
print()
Name = "farhana"
txt = f"I love {Name.upper()}"
print(txt)


# Own function
print()


def circle(r):
    return 3.1416*r**2


circle = f"The circle radius is {circle(10):.2f} meter ."
print(circle)


# string format()
print()
price = 50
txt = "The price is {:.2f} dollars"
print(txt.format(price))

# multiple values
print()
quantity = 5
itemno = 50
price = 100
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))


# Index Numbers
print()
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(10, 30, 80))


# another index way
print()
age = 25
name = "Farhana"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))


# Named Indexes
print()
Student = "my name is {name}, My roll is {roll}."
print(Student.format(name="Farhana", roll=10))
