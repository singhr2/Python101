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

# Output : [11, 12, 13, 14]
print(list(map(funcIncrementBy10, inputList))) 


# (Option-2) using list comprehension
print(list(funcIncrementBy10(x) for x in inputList))

print( [funcIncrementBy10(x) for x in inputList] )
print( {funcIncrementBy10(x) for x in inputList} )

#
# (Option-3) Using Lambda instead of function
# Output : [4, 5, 6, 7]
print(list(map((lambda x: x + 3), inputList))) 