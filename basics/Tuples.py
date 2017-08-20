# Tuples.py

# To run from python interpreter
# > cd D:\dev\python\Python101\basics\
# > python
# > exec(open('Tuples.py').read())

'''
Tuples are roughly like a list that cannot be changed
—tuples are sequences, like lists, 
but they are immutable, like strings.

tuples are not generally used as often as lists in practice, but their immutability is the whole point. 
If you pass a collection of objects around your program as a list, it can be changed anywhere; 
if you use a tuple, it cannot.
'''

#List (uses [] )
# L = [1, 'apple', 1.23]

# Dictionary (uses {} )
# D = {'id': 1, 'name': 'apple', 'price': 1.23}

# Tuples (use () )
myEmptyTuple=()
print('myEmptyTuple:', myEmptyTuple)
print('total elements in myEmptyTuple:', len(myEmptyTuple))

myTuple1 = (1, 2, 3, 4)
print('myTuple1:', myTuple1)

print('total elements:', len(myTuple1))

print('2nd element:', myTuple1[1])

#Add some more
myTuple1 += (5, 6, 1, 1)
print('myTuple1 (after adding elements):', myTuple1)

print('myTuple1.index(1) :', myTuple1.index(1));

print('myTuple1.count(1) : ', myTuple1.count(1))

#Without explicit assiging to (+=) myTuple1, the contents will nto change
print('myTuple1 :::', myTuple1 +('temp1', 'temp2'))
print('myTuple1', myTuple1)

# Test for immutability of Tuples
# uncomment below line and running will return error -> TypeError: 'tuple' object does not support item assignment
#myTuple1[0] = 2

# Create new tuple
myTuple1 = (99,) + myTuple1[1:] # Make a new tuple for a new value
print('myTuple1:', myTuple1)


# Like lists and dictionaries, tuples support mixed types and nesting, 
#but they don’t grow and shrink because they are immutable

T = 'spam', 3.0, [11, 22, 33]
print('T[1] :', T[1])  #3.0
print('T[2][1] :', T[2][1]) # 22



