#File i/o - write
# "r" , "r+" , "w" , "w+" , "a" , "a+"
#r+ - read+ overwrite (pointer start) - No truncate
#w+ -  ||      ||                     - Truncate
#a+ -  ||    append   (pointer end)   - No truncate

# f=open("sampleOfWrite.txt","a") #"w","a" - this two automatically create a file with given name
# data=f.write("This is appended 3...")
# print(data)
# f.close()


#with - automatic close file
with open("sampleOfWrite.txt","r") as f:
    data=f.read()

#replace file 
new_data=data.replace("line","row")
print(new_data)

with open("sampleOfWrite.txt","w") as f: #overwrite on that file
    f.write(new_data)
    # f.write("\nThis is 2nd line")

#use function

# def check_for_word():
#     word="Fake"
#     with open("sampleOfWrite.txt","r") as f:
#         data = f.read()
#         if(data.find(word)!= -1):
#             print("Found")
#         else:
#             print("Not Found")

# check_for_word()


#Line check
def check_for_line():
    word="Fake"
    data=True
    line_no=1
    with open("sampleOfWrite.txt","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no+=1
    return -1

print(check_for_line())

