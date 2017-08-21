# Set.py

# To run from python interpreter
# > cd D:\dev\python\Python101\basics\
# > python
# > exec(open('Set.py').read())
#


# >>> List (uses [] )
# L = [1, 'apple', 1.23]

# >>> Dictionary (uses {} )
# D = {'id': 1, 'name': 'apple', 'price': 1.23}

# >>> Tuples (use () )
# myTuple1 = (1, 2, 3, 4)

#Set are neither mappings nor sequences;
#Sets are 'unordered' collections of 'unique' and 'immutable' objects

## Make a set out of a sequence
# Create set : Option-1 : by calling the built-in set function
X = set('spam')
print('type(X):', type(X));
print('X :', X) # Returns elements in different order in each run

## Make a set with set literals
# Create set : Option-2 : by using new set literals and expressions
Y = {'h', 'a', 'm'}
print('type(Y):', type(Y));
print('Y :', Y) 

Z=X, Y
print('type(Z):', type(Z)); # type(Z): <class 'tuple'>
print('Z :', Z)  #  ({'m', 'p', 'a', 's'}, {'m', 'a', 'h'})

andResult = X & Y # Intersection
print('X & Y :', andResult) # {'a', 'm'}

orResult = X | Y # Union
print('X | Y :', orResult) # {'m', 'h', 's', 'p', 'a'}


diffResult= X - Y # Difference
print(' X - Y :', diffResult) # {'p', 's'}

isXGreaterThanY = X > Y # Superset
print('X > Y :', isXGreaterThanY) # False

## Set comprehensions (3.X and 2.7)
{n ** 2 for n in [1, 2, 3, 4]} # Set comprehensions in 3.X and 2.7

#list(set([1, 2, 1, 3, 1])) # Filtering out duplicates (possibly reordered)
print('list(set([1, 2, 1, 3, 1])) :', list(set([1, 2, 1, 3, 1])))  # [1, 2, 3]

#set('spam') - set('ham') # Finding differences in collections
print('spam-ham :', set('spam') - set('ham'))  # {'p', 's'}

set('spam') == set('asmp') # Order-neutral equality tests (== is False)
print(' spam==asmp ?:', set('spam') == set('asmp'))  #True
