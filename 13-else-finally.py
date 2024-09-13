# else-finally
# The try block does not raise any errors, so the else block is executed:
try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")


# The finally block gets executed no matter if the try block raises any errors or not:
print()
try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")


# The try block will raise an error when trying to write to a read-only file:
print()
try:
    f = open("sampleOfWrite.txt")
    try:
        f.write("Lorum Ipsum")
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close()
except:
    print("Something went wrong when opening the file")
