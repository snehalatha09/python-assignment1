#proramm to sum all items in the dictionary
sam={1:32,2:34,3:12}
sum=0
for i in sam.values():
    sum+=i
print(sum)
    
#to demostrate accessing an element from the dictionaty
sam={1:32,2:34,3:12}
for x in sam:
    print(x,sam[x])
#programme to concate two dictionary
x={'a':1,'b':2}
y={'c':3,'d':4}
y['e']=5
y['f']=6
print(x,y)
#programme to add keys/values in a dictionary(update dictionary)
y={'c':3,'d':4}
y['e']=5
y['f']=6
print(y)
#To find the length of the dictionary
sam={1:32,2:34,3:12}
print(len(sam))

#To remove items from the dictionary

sam={1:32,2:34,3:12}
sam.pop(1)
print(sam)
