# MapReduceFilter.py

# map() function
#   => Mapping Functions over Iterables: map
# Syntax : r = map(func, seq)

# The map function applies a passed-in function to each item in an iterable object 
# and returns a list containing all the function call results.
#
# map applies a 'function' call to each item instead of an arbitrary 'expression', 
# it is a somewhat less general tool, and often requires extra helper functions or lambdas.

'''
map calls funcIncrementBy10 on each list item
and collects all the return values into a new list

map is an iterable in Python 3.X
'''

inputList = [1, 2, 3, 4]

def funcIncrementBy10(x): 
	return x + 10


# ----------------------------------------------------------------
#		MAP : Mapping Functions over Iterables
#  iterator = map(function,  listOrTupleSeqnc)
#
#  note; 
#  * (to verify) If function is None, the identity function is assumed;
#  * the iterable arguments may be a sequence or any iterable object; 
#  * the result is always a list
#
# ----------------------------------------------------------------

# Output : [11, 12, 13, 14]
print(list(map(funcIncrementBy10, inputList))) 


# (Option-2) using list comprehension
# Output :  [11, 12, 13, 14]
print(list(funcIncrementBy10(x) for x in inputList))

# Output : [11, 12, 13, 14]
print( [funcIncrementBy10(x) for x in inputList] )

# Output : {11, 12, 13, 14}
print( {funcIncrementBy10(x) for x in inputList} )

#
# (Option-3) Using Lambda instead of function
# Note : body of a lambda has to be a single expression (not a series of statements)
# Output : [11, 12, 13, 14]
print(list(map((lambda x: x + 10), inputList))) 


# ----------------------------------------------------------------
# FYI : lambda example 2
#
# The general syntax of a lambda function is quite simple: 
#     lambda argument_list: expression 
# ----------------------------------------------------------------
#e.g.,1
lower = (lambda x, y: x if x < y else y)
print(lower('a', 'b'))  # a
print(lower(10,1))  # 1

#e.g.#2
showall = lambda input1: [print(line, end='') for line in input1]
# Not clear why Output : 1234>> [None, None, None, None]
print('>>', showall(inputList)) 


# ----------------------------------------------------------------
# FILTER : Selecting Items in Iterables
#   filter(function, sequence) 
# > filter out all the elements of a sequence "sequence", for which the function function returns True
# > function is its first argument. function has to return a Boolean value, i.e. either True or False. 
#   !!! With filter function as None, the function defaults to Identity function, and each element in randomList is checked if it's true or not.
# > sequence : iterable which is to be filtered, could be sets, lists, tuples, or containers of any iterators
# > Only if function returns True will the element be produced by the iterator, which is the return value of filter(function, sequence). 
# ----------------------------------------------------------------

# list of alphabets
alphabets = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

# function that filters vowels
def filterVowels(alphabet):
    vowels = ['a', 'e', 'i', 'o', 'u']

    if(alphabet in vowels):
        return True
    else:
        return False

filteredVowels = filter(filterVowels, alphabets)

print('The filtered vowels are:')
for vowel in filteredVowels:
    print(vowel)


''' output: 
The filtered vowels are:
a
e
i
o
'''


# filter with None as function
# random list
randomList = [1, 'a', 0, False, True, '0']

filteredList = filter(None, randomList)

print('The filtered elements are:')
for element in filteredList:
    print(element)

''' Output : 
The filtered elements are:  
1                           
a                           
True                        
0                           
'''


# ----------------------------------------------------------------
# REDUCE: Combining Items in Iterables
# > Present in functools module, so we need to import as below:
#   from functools import reduce
#
# > reduces a list to a single value by combining elements via a supplied function. 
#
# Note: 
# At each step, reduce passes the current sum or product, along with the next item from the list, 
# to the passed-in lambda function. By default, the first item in the sequence
# initializes the starting value.
# ----------------------------------------------------------------

# option-1
from functools import reduce # Import in 3.X, not in 2.X

#option-2
#import functools
# functools.reduce(...)

print(reduce((lambda x, y: x + y), [1, 2, 3, 4])) #10

print(reduce((lambda x, y: x * y), [1, 2, 3, 4])) #24

# e.g.#2
print(reduce(lambda x,y: x+y, [47,11,42,13])) # 113
