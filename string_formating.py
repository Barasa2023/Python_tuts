#string formatting in python

#*************** .FORMAT METHOD **************************

name = "Kelvin"
age = 25
print("Hello {}, your age is {}".format(name, age))

#rearranging the inserted strings
print("The {1}, {0} {2}".format('brown', 'quick', 'fox'))

result = 100 / 777
print("The output is {r:1.3f}".format(r = result))

# ********************** F-STRING METHOD *****************
name = "James"
age  = 20
print(f"His name is {name} and he is {age} years old.")
