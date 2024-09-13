#File I/O - Python can be used to perform operations on a file(read & write data)
#types of all files:
# 1. Text Files : .txt, .docx, .log etc
# 2. Binary Files : .mp4, .mov, .png, .jpeg etc

#Open,read & Close Fole
# f= open("file_name (.txt, .docx)","mode(read, write)")
# data=f.read()
# data=f.readline()
# f.close()

f= open("4-input.py","r")
data=f.read()
print(data)

f= open("4-input.py","r")
print()
data=f.read(5) #read word limit
print("Print first 5 characters : ",data)

f= open("4-input.py","r")
print()
data=f.readline() #read entire line
print("Print 1 line  : ",data)
data1=f.readline() #read entire line
print("Print 2 line  : ",data1)
f.close()
