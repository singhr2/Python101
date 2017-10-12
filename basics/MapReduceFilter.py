#MapReduceFilter.py

# map() function
#   => Mapping Functions over Iterables: map
# Syntax : r = map(func, seq)

# The map function applies a passed-in function to each item in an iterable object 
# and returns a list containing all the function call results.

'''
map calls funcIncrementBy10 on each list item
and collects all the return values into a new list

map is an iterable in Python 3.X
'''

inputList = [1, 2, 3, 4]

def funcIncrementBy10(x): 
	return x + 10

print(list(map(funcIncrementBy10, inputList))) # [11, 12, 13, 14]


#--
# Function expression
# Output : [4, 5, 6, 7]
print(list(map((lambda x: x + 3), inputList))) 