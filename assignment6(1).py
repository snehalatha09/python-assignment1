#programme to display the fibonacci sequence
n=int(input("enter the value of n"))
n1,n2=0,1
count=0
if n<=0:
    print("enter te positive number")
elif n==1:
    print("fibonacci sequence upto",n)
    print(n1)
else:
    while count<n:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count +=1
#programme to print the multiplication table of a number
k=int(input("enter a number"))
i=1
while i<=10:
    print(k,'x',i,'=',k*i)
    i=i+1
