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

type([]) # <class 'list'>
type({}) # <class 'dict'>
type(()) # <class 'tuple'>

l1=['1','2']
type(l1) # <class 'list'>
print(l1, ' has ', len(l1), 'elements') # ['1', '2']  has  2 elements
print('list.count(\'2\') :', l1.count('2')) # 1
print('list.count(\'-999\') :', l1.count('-999')) # 0
print('l1.index(\'2\') ?', l1.index('2')) # 1
#print('l1.index(\'-999\') ?', l1.index('-999')) # ValueError: '-999' is not in list

#Add element at end
l1.append('3rd') # ['1', '2', '3rd']
print(l1)

#add element at index
l1.insert(1, 'add at index 1') #['1', 'add at index 1', '2', '3rd']
print(l1)

l1.remove('add at index 1')
print(l1)

# ------------------------------------
t1=('1','2') 
type(t1) #<class 'tuple'>

# ------------------------------------
# SET
# sets are essentially like valueless dictionaries
#set’s items are unordered, unique, and immutable

s2={'1','2'}
type(s2) # <class 'set'>

set('spam') #{'m', 's', 'p', 'a'}

type([1, 2, 3, 4]) # <class 'list'>
# Create Set from List
set([1, 2, 3, 4]) # {1, 2, 3, 4}

type({1, 2, 3, 4}) #<class 'set'>


S1 = {1, 2, 3, 4}
print('S1 :', S1)

# Intersection
S1 & {1, 3} # {1, 3}

# Union
{1, 5, 3, 6} | S1 # {1, 2, 3, 4, 5, 6}

# Difference
S1 - {1, 3, 4} # {2}

# Superset
S1 > {1, 3}  #True

S1 - {1, 2, 3, 4} # set() , { Note: Empty sets print differently }

# add() method
S1.add('alot')
print('S1 (after adding alot :', S1) #{1, 2, 3, 4, 'alot'}

# ------------------------------------
d2={'1':'one', '2':'two'}
type(d2) #<class 'dict'>




