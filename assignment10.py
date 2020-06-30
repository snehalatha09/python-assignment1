# to open a filein python using try and execpt
try:
    f=open("hello.txt")
except:
        print("file can't be opened")
        exit()
        for line in f:
            if line.startswith('welcome'):
                print(line)


#to split the data in a file
  
with open("hello.txt")as f:
        data=f.readlines()
        for line in data:
            word=line.split("\n")
            print(word)



#to read the content of the file using with statment
with open ("hello.txt")as f:
    data=f.read()
    print(data)



#programme to remove the file 
import os
os.remove("hello.txt")
#programme to remove directory
import os
os.rmdir("abc")
#programme to create a list and access the elements in the list
s=['cse','sneha','c',12]
for i in s:
    print(i[2])
          
