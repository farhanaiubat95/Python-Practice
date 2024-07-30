#File i/o - write
# "r" , "r+" , "w" , "w+" , "a" , "a+"
#r+ - read+ overwrite (pointer start) - No truncate
#w+ -  ||      ||                     - Truncate
#a+ -  ||    append   (pointer end)   - No truncate

f=open("sampleOfWrite.txt","a") #"w","a" - this two automatically create a file with given name
data=f.write("This is appened 2...")
print(data)
f.close()


#with - automatic close file
with open("sampleOfWrite.txt","r") as f:
    data=f.read()
    print(data)
