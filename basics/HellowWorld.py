#HellowWorld.py
# to run, 
# cd  D:\dev\python\Python101\basics
# python HellowWorld.py

print('Hello World')

#When two or more arguments are passed, print  function displays each argument separated by space.
print("Hello", "World")

# THis is single-line comment
# print('Hello World')

#multiline comment
'''
This 
is
multi-line
comment
print('This will not be printed too')
'''

#Simultaneous Assignments
x=1
y=2
y,x=x,y
print('x=', x)
print('y=', y)

print('type(x) :', type(x))

# you can assign multiple variables within a single statement.
a, b, c = 1, 2, "Hey"

#assign the same value to multiple variables
a = b = c = "Hey"

# Mix
#a, b = 2  #TypeError: 'int' object is not iterable

#variable names (as with all identifiers) are case sensitive.
var1='all lowercase'
vAr1='A capital'
vaR1='R capital'
vAR1='AR caps'
print(var1, vAr1, vaR1, vAR1)

# Receiving input from Console
name = input("Enter your name: ")
print('name entered:', name)

num1=10
num2=20
print('10+20=', num1+num2)
print("10-20=", num1-num2)

var = 10 - 30
print('var is:', var)

print('2==3 :', 2==3)
print('2^3=', 2^3)
# Exponentiation Operator
print('2**3=',2**3)

#/ – Float Division
print('3/2=',3/2)

#// – Integer Division ( truncate the decimal part)
print('3//2=', 3//2)

#  remainder or modulus operator
print('35%4=', 35%4)


# you can treat True and False as though
# they are predefined variables set to integers 1 and 0.
True == 1


# False and True will have 1st char as Caps
x=False
y=True

print('x and y :', x and y)
print('x or y :', x or y)
print('not x :', not x)
#print(xor )