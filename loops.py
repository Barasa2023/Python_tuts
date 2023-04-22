#loops
#for loops
names = ["Kelvin", "Barasa", "Charles", "Waliuba"]

#print out the names
for name in names:
    print(name)

#add all the elements of a list

marks = [50, 74, 68, 87, 66]
total = 0
for mark in marks:
    total += mark

print(total)

#for loops with strings

mystring = "Hello World"

for letter in mystring:
    print(letter)

#tuple unpacking

mylist = [(1, 2), (3,4), (5,6)]

for a,b in mylist:
    print(a)
    print(b)

#for loops in dictionaries

dic = {"name": "Kelvin", "age": 24, "address": "Mombasa", "phone": 744554}
for item in dic:
    print(item)

#print the key and value
for item in dic.items():
    print(item)

#print only values

for value in dic.values():
    print(value)
