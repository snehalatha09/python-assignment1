#height common factor of given two numbers
n1=int(input("enter the first number"))
n2=int(input("enter the second number"))
while n1!=n2:
    if n1>n2:
        n1=n1-n2
    else:
        n2=n2-n1
print("HCF of two numbers is :",n1)
#binary to decimal
a=input("enter the input")
x=int(a,2)
print(x)

