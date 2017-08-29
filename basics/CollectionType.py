# CollectionType.py

# To run from python interpreter
# > cd D:\dev\python\Python101\basics\
# [option-1]  
# > python
# > exec(open('CollectionType.py').read())
# OR
# [option-2]
# python CollectionType.py


# Set
# an unordered collection of unique and immutable objects
# sets are iterable, can grow and shrink on demand, and may contain a variety of object types.

l1=['1','2']
type(l1) # <class 'list'>

# ------------------------------------
t1=('1','2') 
type(t1) #<class 'tuple'>

# ------------------------------------
s2={'1','2'}
type(s2) # <class 'set'>

set('spam') #{'m', 's', 'p', 'a'}

set([1, 2, 3, 4]) # {1, 2, 3, 4}


S1 = {1, 2, 3, 4}

# Intersection
S1 & {1, 3} # {1, 3}

# Union
{1, 5, 3, 6} | S1 # {1, 2, 3, 4, 5, 6}

# Difference
S1 - {1, 3, 4} # {2}

# Superset
S1 > {1, 3}  #True

# ------------------------------------
d2={'1':'one', '2':'two'}
type(d2) #<class 'dict'>




