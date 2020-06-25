#programme1
# Programme to add natural numbers
sum=0
n=int(input("enter the number"))
for i in range(1,100):
    if i==n:
        break
    
    sum=sum+i
print('sum of the natural numxbers is ',sum)


#programme2
#To count the number of even and odd numbers in the series
count1=0
count2=0
x=[1,2,3,4,5,6,7,8,9,10]
for i  in x:
    if i%2==0:
        count1=1+count1
    else:
        count2=1+count2
print("count of even numbers in the given range is ",count1)
print("count if odd numbers in the given range is",count2)


#programme3
#To print all the numbers from 0 to 6 execpt 3 and 6
for i in  range(0,6):
    if i==3:
        continue
    print(i)


#programme4
#To print squares of all numbers in the list
import math
x=[1,2,3,4,5,6,7,8,9,10]
for i in x:
    print("squre of the",i,'is',i*i)

#programme5    
# to calculate the sum and avarage of some integer numbers
n=int(input("enter the number"))
sum=0
average=1
for i in range(1,n):
    sum=sum+i
print('sum of the integer numbers is',sum)
average=sum/2
print('average of the numbers is',average)



#programm6
#To reverse a  given number
number=int(input("enter the number too reverse that numbers"))
rev=0
while(number>0):
    reminder=number%10
    rev=(rev*10)+reminder
    number=number//10
print('the reverse of the given number is',rev)



#programme7
#to print odd number whithin the range
num=int(input('enter the number9'))
for i in range(1,num):
    if i%2!=0:
        print('odd numbers in the given range is',i)


#programme8
#To check whether the number is palindrome or not
n=1234
temp=n
rev=0
while n>0:
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("the number is palindrome")
else:
    print("the number is not palindrome")



#programme9
#To print an identity matix
n=3
for i in range(0,n):
    for j in range(0,n):
        if(i==j):
            print('1')
        else:
            print('0')
    print()




#programme10
#To check the number is perfect or not
n=6
sum=0
for i in range (1,n):
    if(n%i==0):
        sum=sum+1
if (sum==n):
    print("the num is perfect")
else:
    print("the number is not perfect")
    


#programme11
#To count the number of digits in the given number
n= int(input("enter the number"))
count=0
while(n>0):
    count=count+1
    n=n//10
print("the number of digits in the given number is",count)
