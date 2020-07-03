#program to print the largest and smalest number in the list
seq=[1,2,3,4,5,6,7,8,9,10]
print('max in the list',max(seq))
print('min in the list',min(seq))


#program to check list is empty or not
l=[]
if len(l)==0:
    print("the list is empty")
#program to sum the elements in the list

a=[12,34,87]
print(sum(a))

#programm to copy or clone  a list
list1=[4,5,6,7]
list2=list1.coopy()
print(list2)
#programme to print the numbers of a specified list after removing even numbers from it
list=[11,22,33,44,55]
for i in list:
    if(i%2==0):
        list.remove(i)
print(list)

