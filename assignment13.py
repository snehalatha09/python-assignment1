#To check whether the string starts with specified charecter
a="Have a nice day"
a.lower().startswith("h")
a.startswith("have")
#To print the index of the charecter in the string
s='snehalatha'
b=s.find('l')
print(b)
#To iterate over dictionaries usin for loop
sam={'one':1,'two':25,'three':35,'four':4}
for x in sam:
    if sam[x]>20:
        print(sam[x])
        
#To remove the given key from the strig
#1
student={
    "name":"emma",
    "class":9,
    "marks":75
}
del student["name"]
student.popitem()
student.pop("class")
print(student)
