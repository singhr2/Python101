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

# -----------------------------------
#  List functions
# -----------------------------------
myList1=['1','2']
type(myList1) # <class 'list'>
print(myList1, ' has ', len(myList1), 'elements') # ['1', '2']  has  2 elements

print('list.count(\'2\') :', myList1.count('2')) # 1
print('list.count(\'-999\') :', myList1.count('-999')) # 0

# index() : Raises a ValueError if there is no such item.
print('myList1.index(\'2\') ?', myList1.index('2')) # 1
#print('myList1.index(\'-999\') ?', myList1.index('-999')) # ValueError: '-999' is not in list

#Add element at end
myList1.append('3rd') # ['1', '2', '3rd']
print(myList1)

#add element at index
desired_index= 1;
myList1.insert(desired_index, 'add at index 1') #['1', 'add at index 1', '2', '3rd']
print(myList1)

# Removes the first item from the list that has a value of x. 
#don't return it.
myList1.remove('add at index 1')
print(myList1)

# Removes the item at the given position in the list, and returns it. 
#If no index is specified, pop() removes and returns the last item in the list.
index_to_remove = 2;
myList1.pop(index_to_remove)
print('List after removing element at index (',index_to_remove,') :', myList1)

# remove all elements from list
myList1.clear()
print('List after removing all elements :', myList1)

# Iterate through list
myList1.append('temp1')
myList1.append('temp2')
myList1.append('temp3')

print(myList1)

for i in myList1 :
	print(i)

# extend list
list1 = ['physics', 'chemistry', 'maths']
list2=list(range(5)) #creates list of numbers between 0-4
list1.extend(list2)
print ('list1 :', list1)  # ['physics', 'chemistry', 'maths', 0, 1, 2, 3, 4]
print ('list2 :', list2)  # [0, 1, 2, 3, 4]

# reverse list
list1.reverse()
print ('list1 (after reverse) :', list1)

# SORTING LIST
# sort(key=None(default), reverse=False(default))

#Sorts objects of list, use compare func if given
a = ["bee", "wasp", "moth", "ant"]
a.sort()
print(a) #['ant', 'bee', 'moth', 'wasp']

a = ["bee", "butterfly", "wasp", 'a']
a.sort(key=len)
print(a) #['a', 'bee', 'wasp', 'butterfly']

a = ["bee", "butterfly", "wasp", 'a']
a.sort(key=len, reverse=True)
print(a) #['butterfly', 'wasp', 'bee', 'a']


#
S = {c * 4 for c in 'spam'}
print(S) # {'pppp', 'ssss', 'aaaa', 'mmmm'}


# ------------------------------------
t1=('1','2') 
type(t1) #<class 'tuple'>




# ------------------------------------
# SET
# sets are essentially like valueless dictionaries
# set’s items are unordered, unique, and immutable
# 
#largely because of their implementation, sets can only contain immutable (a.k.a. “hashable”) object types. 
# Hence, lists and dictionaries cannot be embedded in sets, but tuples can if you need to store compound values.

s2={'1','2'}
type(s2) # <class 'set'>

set('spam') #{'m', 's', 'p', 'a'}

type([1, 2, 3, 4]) # <class 'list'>
# Create Set from List
L = [1, 2, 1, 3, 2, 4, 5]
s1=set(L)
print('set from list:', s1) # {1, 2, 3, 4, 5}

{1, 2, 3, 4, 5}

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


# Comparison
L1, L2 = [1, 3, 5, 2, 4], [2, 5, 3, 4, 1]
L1 == L2 # False, Order matters in sequences

set(L1) == set(L2) # True, Order-neutral equality

sorted(L1) == sorted(L2) # True, Similar but results ordered

'spam' == 'asmp', set('spam') == set('asmp'), sorted('spam') == sorted('asmp')
#(False, True, True)


engineers = {'bob', 'sue', 'ann', 'vic'}
managers = {'tom', 'sue'}
'bob' in engineers # Is bob an engineer?
# True

engineers & managers # Who is both engineer and manager?
#{'sue'}

engineers | managers # All people in either category
#{'bob', 'tom', 'sue', 'vic', 'ann'}

engineers - managers # Engineers who are not managers
#{'vic', 'ann', 'bob'}
managers - engineers # Managers who are not engineers
#{'tom'}

engineers > managers # Are all managers engineers? (superset)
#False



# ------------------------------------
d2={'1':'one', '2':'two'}
type(d2) #<class 'dict'>




