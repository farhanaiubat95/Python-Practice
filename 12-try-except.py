# Try-except
# without declare particular error
try:
    list = [10, 0, 50]
    answer = list[0]/list[1]
    print(answer)
except:
    print("something wrong")


# particular error handle - ZeroDivisionError
try:
    list = [10, 0, 50]
    answer = list[0]/list[1]
    print(answer)
except ZeroDivisionError:
    print("Dividing by zero is not possible..")


# particular error handle - ZeroDivisionError
try:
    list = [10, 0, 50]
    answer = list[0]/list[4]  # index 4 is not exist
    print(answer)
except IndexError:
    print("Giving index is out of bound.")


# multiple exception
# particular error handle -TypeError ,valueError
try:
    num = int(input("Enter number : "))
    answer = num / 0  # index 4 is not exist
    print(answer)
    print(x)
except TypeError:
    print("Type error.")
except ZeroDivisionError:
    print("Dividing by zero is not possible.")
except ValueError:
    print("Value Error occure.")
except NameError:
    print("Variable is not defined.")
except:
    print("Something went wrong...")
