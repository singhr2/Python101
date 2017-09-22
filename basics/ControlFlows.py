# ControlFlows.py

# To run from python interpreter
# > cd D:\dev\python\Python101\basics\
# > python
# > exec(open('ControlFlows.py').read())

## REFERENCE:
# http://www.openbookproject.net/books/bpp4awd/ch04.html

'''
* Parentheses are optional	: if (x < y)  ~ if x < y
* End-of-line ~ end of statement
* End of indentation ~  end of block
* Python detects block boundaries automatically, by line indentation
* Assignments create object references
* Names are created when first assigned. Python creates a variable name the first time you assign it a value (i.e., an object reference)
* no switch or case statement in Python
* Compound statements = header + “:” + indented statements. e.g., if-elif-else
* Python detects block boundaries automatically, by line indentation
'''


a = 1;
b = 2;
print(a + b)  # Three statements on one line

# you can make a single statement span across multiple lines. To make this work, you simply have to enclose
# part of your statement in a bracketed pair—parentheses (()), square brackets ([]), or curly braces ({}).
X = (a +
     b)
print('X is :', X)


#The if/else Ternary Expression
'''
if X:
	A = Y
else:
	A = Z
'''

# NameError: name 'X2' is not defined  <<-- If variable is unassigned
#X2 = ''  # retuns -> condition is false
X2 = 'A' # returns ->> condition is true
Y2 = 'condition is true'
Z2 = 'condition is false'
A2 = Y2 if X2 else Z2
print(A2)


# Block Indentation
print('\n block0')
x = 1
if x: # Any nonzero number or nonempty object is True
	print('block1')
	y = 2
	if y:
		print('block2')
	print('block1')
print('block0')


"""
import sys
sys.exit(0)
"""

# The if else statement
food = 'veg'
if food == 'spam':
    print('Ummmm, my favorite!')
else:
    print("No, I won't have it. I want spam!")

# Using not
print("\n[1]-------")
food = 'asian'
if not food == 'veg':
    print('Not veg')


print("\n[2]-------")
# ??? pass (Empty placeholder)
if True:  # This is always true
    pass  # so this is always executed, but it does nothing
else:
    pass

# e.g. 3
print("\n[3]-------")
x = int(input("Please enter an integer: "))
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

# Altertive to switch 
# A dictionary-based 'switch',Use has_key or get for default
print("\n[4]-------")
choice = input('Enter 1st character of your favourite color ?')
my_switch_dict = {'b': 'Blue', 'w':'White', 'y':'Yellow', 'g':'green'}
#This will return KeyError: 'x' (where x is the input entered) if invalid key is entered
#print(my_switch_dict[choice]) 

#option -1 : get function
# This will return 'None Sorry , No idea!' if invalid key is entered
print( my_switch_dict.get(choice), 'Sorry , No idea!') # 2nd parameter is the default value

#option -2  : in membership test in
if choice in my_switch_dict:
	print(my_switch_dict[choice])
else :
	print('Sorry , No idea!')
	
#option -3  : try-except
try:
	print(my_switch_dict[choice])
except:
	print('Sorry , No idea!')



# Nested conditionals
print('\n [5]number comparison')
num_1 = int(input("Please enter 1st number: "))
num_2 = int(input("Please enter 2nd number: "))
if num_1 < num_2:
    print(num_2, 'is greater than', num_1)
else:
    if num_2 < num_1:
        print(num_1, 'is greater than', num_2)
    else:
        print('Both numbers are same')

'''
every Python tool that scans an object from left to right uses the iteration protocol.

'''

# for LOOP_VARIABLE in SEQUENCE:
#    STATEMENTS

'''
for target in object: # Assign object items to target
	statements # Repeated loop body: use target
	if test: break # Exit loop now, skip else
	if test: continue # Go to top of loop now
else:
	statements # If we didn't hit a 'break'	
'''

for friend in ['Shreya', 'Anshi']:
    invitation = "Hi " + friend + ".  Please come to my party on Saturday!"
    print(invitation)

# printing table
for x in range(13):  # Generate numbers 0 to 12
    print(x, '\t', 2 ** x)

# e.g.
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

for c in 'spam':
    print(c.upper())


##
# The list comprehension will often run faster than a for loop today on some types of code (perhaps even twice as fast)
# —a property that could matter in your programs for large data sets.


squares = []
for x in [1, 2, 3, 4, 5]:  # This is what a list comprehension does
    squares.append(x ** 2)  # Both run the iteration protocol internally
print('squares (approach-1) :', squares);

''' This is equivalent to below code '''
squares = []
squares = [x ** 2 for x in [1, 2, 3, 4, 5]]
print('squares (approach-2) :', squares);

## BREAK
for i in [12, 16, 17, 24, 29]:
    if i % 2 == 1:  # if the number is odd
        break  # immediately exit the loop
    print(i)
print("done")


# A tuple of values is assigned to a tuple of names on each iteration,
'''
 > ValueError: too many values to unpack (expected 3)
    When Values in list (inside Tuple) are more than variables in for loop
        T = [(1, 2, 3), ('a', 'b', 'c'), (True, False, None, True)]
        for(x,y,z) in T:

 > ValueError: not enough values to unpack (expected 3, got 2)
    When values in any list in tuple are less than variables in for loop 
        T = [(1, 2, 3), ('a', 'b', 'c'), (True, False)]
        for(x,y,z) in T:
'''
T = [(1, 2, 3), ('a', 'b', 'c'), (True, False, None)]
for (x, y, z) in T:
    print(x, y)

# extended sequence assignment
# *b indicates b will have everyhting left over after a and c
'''
1[2, 3] 4
5[6, 7] 8
'''
for (a, *b, c) in [(1, 2, 3, 4), (5, 6, 7, 8)]:
    print(a, b, c)

# sequence assignment 2
'''
Output:
a,b, C : 1 , 2 , 3
a,b, C : X , Y , 6
'''
print('\n sequence assignment example 2')
for ((a, b), c) in [([1, 2], 3), ['XY', 6]]:
    print('a,b, C :', a, ',',  b, ',', c)
	
	

# zip(*iterables) built-in function
'''
 > allows us to use for loops to visit multiple sequences in parallel—not overlapping in time, but during the same loop.
 > zip takes one or more sequences as arguments and returns a series of tuples that pair up parallel items taken from those sequences
 
 The zip() function returns an iterator of tuples based on the iterable object.
 > If no parameters are passed, zip() returns an empty iterator
 > If a single iterable is passed, zip() returns an iterator of 1-tuples. Meaning, the number of elements in each tuple is 1.
 > If multiple iterables are passed, ith tuple contains ith 
	Suppose, two iterables are passed; one iterable containing 3 and other containing 5 elements. 
	Then, the returned iterator has 3 tuples. It's because iterator stops when shortest iterable is exhaused. <---
'''
numbersList = [1, 2, 3]
strList = ['one', 'two']
numbersTuple = ('ONE', 'TWO', 'THREE', 'FOUR')

# Converting to set - Using 2 Iterables
result = zip(numbersList, numbersTuple)   
resultSet = set(result)
print('type of result :', type(result)) # <class 'zip'>
print('zip result :', result) #  <zip object at 0x00719EE0>
print('resultSet :', resultSet) #  {(1, 'ONE'), (2, 'TWO'), (3, 'THREE')}

# Convert to List
resultList = list(result) # []
print('resultList 1:', resultList)
resultList = list(zip(numbersList, numbersTuple)) #  [(1, 'ONE'), (2, 'TWO'), (3, 'THREE')]
print('resultList 2:', resultList)


# Converting to set - Using 3 Iterables 
result = zip(numbersList, strList, numbersTuple)
resultSet = set(result)
print('resultSet 3 iterators :', resultSet) # {(1, 'one', 'ONE'), (2, 'two', 'TWO')}
	
	
#---------------------------------------------------
# map() function : map(function, iterable(1..*), ...)
#
#  Normally, map takes a function and one or more sequence arguments and 
#  collects the results of calling the function with parallel items taken from the sequence(s).
# 	in short, The map() function applies a given to function to each item of an iterable and 
#   returns a list of the results.
#    function - map() passes each item of the iterable (list, tuple etc.) to this function.
#    iterable - iterable(list, tuple etc.) which is to be mapped
#---------------------------------------------------

# e.g., 1 : map using custom function
def calculateSquare(n):
  return n*n

numbers = (1, 2, 3, 4)
result = map(calculateSquare, numbers) # note the function name is not in quotes
print('\nresult from map :', result) # <map object at 0x01F43310>

# converting map object to set
numbersSquare = set(result)
print('map > numbersSquare :', numbersSquare) #  {16, 1, 4, 9}

# e.g., 2 : map using built-in function
input_string = ['Just Do It', '2nd', 'third']
resultMap2 = map(len, input_string)
print('map > list[resultMap2] :', list(resultMap2)) #  [10, 3, 5]
print('map > set[resultMap2] :', set(resultMap2)) #   set()

resultMap2 = map(len, input_string)
print('map > set[resultMap2] :', set(resultMap2)) #   {10, 3, 5}



# e.g.3
def fahrenheit(T):
    return ((float(9)/5)*T + 32)

def celsius(T):
    return (float(5)/9)*(T-32)

temperatures = (36.5, 37, 37.5, 38, 39)
F = map(fahrenheit, temperatures)
C = map(celsius, F)

temperatures_in_Fahrenheit = list(map(fahrenheit, temperatures))
temperatures_in_Celsius = list(map(celsius, temperatures_in_Fahrenheit))
print(temperatures_in_Fahrenheit) # [97.7, 98.60000000000001, 99.5, 100.4, 102.2]
print(temperatures_in_Celsius) # [36.5, 37.00000000000001, 37.5, 38.00000000000001, 39.0]



#
# Since map() expects a function to be passed in, lambda functions are commonly used while working with map() functions.
# A lambda function is a function without a name.
# 

# ---------------------------------------------------
# while loop
#
# break: Jumps out of the closest enclosing loop
# continue: Jumps to the top of the closest enclosing loop
# pass: Does nothing at all: it’s an empty statement placeholder
#		pass is roughly to statements as None is to objects—an explicit nothing.
# Loop else block : Runs if and only if the loop is exited normally
# ---------------------------------------------------

'''
while test:  # Loop test
	statements  # Loop body
	if test: break # Exit loop now, skip else if present
	if test: continue # Go to top of loop now, to test1
else:  # Optional else
	statements # Run if didn't exit loop with break
'''

## Another while loop example
x = 4
print('before while loop')
while x > 0:
    print('spam!' * x)
    x -= 1
print('after while loop')

while True:
    reply = input('Enter text, type q to exit:')
    if reply == 'q': break
    print(reply.upper())
print('Bye, i\'ll stop now as you typed stop')

# CONTINUE
for i in [12, 16, 17, 24, 29, 30]:
    if i % 2 == 1:  # if the number is odd
        continue  # don't process it
    print(i)
print("done")


# with/as : Context managers (3.X, 2.6+)
#The advantage of using a with statement is that it is guaranteed to close the file no matter how the nested block exits.
#This allows common try…except…finally usage patterns to be encapsulated for convenient reuse.
'''
with open('output.txt', 'w') as f:
    f.write('Hi there!')
'''

# AttributeError: __enter__
'''
with ['spam'] as iterator:
    print(iterator)
'''

# Comprehensions
M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print('M :', M)

col2 = [row[1] for row in M]
print('col2 :', col2)

print('after adding 1 to send element in each row :', [row[1] + 1 for row in M])

print('Filter out odd items :', [row[1] for row in M if row[1] % 2 == 0])
