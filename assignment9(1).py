#to read an entire text file
f1=open("hello.txt","w")
f1.write("welcome to python programming")
f1.close()
f1=open("hello.txt","r")
print(f1.read())

#to append text to the file and read the text
f1=open("hello.txt","a")
f1.write("\nhello")
f1.close()
f1=open("hello.txt","r")
print(f1.read())
f1.close()


# to remove leading and trailing spaces from the string
str="kallu sneha latha"
str1=str.rstrip('l')
str2=str.lstrip('l')
print(str1)
print(str2)

#to read the content of the file using for loop
f1=open("hello.txt")
for each in f1:
  print(each)
  
  
  
  
  
