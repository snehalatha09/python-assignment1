#python programme to calculate the length of the string
g='kallu snehalatha'
n=len(g)
print('the length of the string',n)


#to print the number of charecters in the string
count=0
i='kallu snehalatha'
for x in i:
    count=count+1
print(count)



#To count the no of times letter 'o'appear in string 'hello world'
count=0
i='hello world'
for x in i:
    if x=='o':
        count=count+1
print('the letter o appear in the string is ',count,'times')



#Programme to compare two strings
a=input("enter one string")
b=input("enter another string")
print(a>b)
print(a>=b)
print(a!=b)
print(a<b)
print(a<=b)




#To check the substring in the given string
s='kallu snehalatha'
if'sneha' in s:
    print(" the substring is in the given string true")




#To find the length of the string without using len
count=0
i='refrigerator'
for x in i:
    count=count+1
print('length of the string is ',count)




#Programme to print the every charecter in the string using loop
s=input("enter the string")
for i in s:
    print(i)
    




#PYTHON SCRIPT THAT TAKES INPUT FROM THE USER AND DISPLAYS THAT BACK IN UPPER AND LOWER CASES
user_input=input("What is your favourite colour")
print('My fav colour is',user_input.upper())
print('My fav colour is',user_input.lower())






#counting the accurrences of the string using string.count() in python
str="I LOVE MY FAMILY"
print(str.count("FAMILY"))







#python programme to removing ith charecter from a string
s='kallusnehalatha'
print("the original string is:",s)
n=s[:2]
print(" the new string is ",n)
