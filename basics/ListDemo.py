# ListDemo.py

# To run from python interpreter
# > cd D:\dev\python\Python101\basics\StringDemo.py
# > python
# > exec(open('ListDemo.py').read())
#OR
# > python ListDemo.py

# List have no fixed type constraint
# lists have no fixed size i.e. they can grow and shrink on demand, in response to list-specific operations
# list is an ordered collection object type
# they are mutable objects

# They are also mutable—unlike strings, lists can be modified in place by assignment to
#offsets as well as a variety of list method calls

###
# Also, check examples in CollectionType.py
###

#L = [] An empty list
myEmptyList = []
print('size of empty list :', len(myEmptyList))

myListUsingString=list("abcde")
print('myListUsingString :', myListUsingString) # ['a', 'b', 'c', 'd', 'e']

myListUsingRange=list(range(-6, 6, 2))
print('myListUsingRange :', myListUsingRange) # [-6, -4, -2, 0, 2, 4]

myList = ['one', 'two', 'three']
print('myList :', myList)
print('total elements :', len(myList))

myListOfDifferentObjects = ['one', 2, False, {}]
print('myListOfDifferentObjects :', myListOfDifferentObjects)
print('2nd element in list :', myListOfDifferentObjects[1])
print('type(4th element in list) :', type(myListOfDifferentObjects[3])) #<class 'dict'>


# add more elements
myList += myListOfDifferentObjects
print('concated list :', myList)

# Duplicate the values
myList = myList * 2
print('concated list(twice) :', myList)


###   Type-Specific Operations ####

#SORTING
print('\n -->>> Sorting example');
languagesList =['Java', 'Pl/SQL', 'JavaScript', 'HTML']
print('languagesList :', languagesList);
print('Sorted :', languagesList.sort()) # Prints  None , why ?
print('languagesList :', languagesList); # prints sorted values


#reverse()
print('\n -->>> reverse() example');
print('languagesList :', languagesList);
languagesList.reverse()
print('languagesList :', languagesList);

# Append - To add a single item to the end of a list,
# we can concatenate or call append
print('\n -->>> append() example');
print('before :', languagesList);
languagesList.append('Python')
print('after :', languagesList);

List3 = [1, 2]
List3 = List3 + [3] # Concatenate: slower
print(List3) # [1, 2, 3]
List3.append(4) # Faster, but in place
print(List3) # [1, 2, 3, 4]


'''
[ Adding more than one items:  { + (concatenate)  vs extend() method }
-------------------------------------------------------
To add a set of items to the end, we can either concatenate (+) or 
call the list extend() method

Concatenation operations must create a new object, copy in the list on the left, and then
copy in the list on the right.

By contrast, in-place method calls simply add items at the end of a memory block
(it can be a bit more complicated than that internally, but this description suffices).
'''
List4 = [1, 2]
List4 = List4 + [5, 6]  # Concatenate: slower
print(List4)  # [1, 2, 3, 4, 5, 6]
List4.extend([7, 8])  # Faster, but in place
print(List4)  # [1, 2, 3, 4, 5, 6, 7, 8]


# POP
print('\n -->>> pop() example');
print('before :', languagesList);
languagesList.pop(1)
print('after :', languagesList);

# IndexError: list index out of range
#UNCOMMENT BELOW LINE TO TEST
#print (languagesList[999])


# LIST within LIST (multi-dimensional list)
MultiDimensionalList = [
     [1, 2, 3],       # A 3 × 3 matrix, as nested lists
     ['a', 'b', 'c'], # Code can span lines if bracketed
     ['False', 'True']
	]
print('MultiDimensionalList :', MultiDimensionalList);

# Get 3rd element from 2nd list
print('3rd element from 2nd list :', MultiDimensionalList[1][2])

#Get all 3rd list elements
print('3rd list elements :', MultiDimensionalList[2])



# #### list comprehension expression ####
M=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Suppose, for instance, that we need to extract the second column of our sample matrix.
# It’s easy to grab rows by simple indexing because the matrix is stored by rows,
# but it’s almost as easy to get a column with a list comprehension

# List comprehensions (coded in square brackets) derive from set notation;
# they are a way to build a new list by running an expression on each item in a sequence,
# one at a time, from left to right.

# List comprehensions are composed of an expression and a looping construct that share a variable name (row, here).
# The preceding list comprehension means basically what it says: "Give me row[1] for each row in matrix M, in a new list."
# The result is a new list containing column 2 of the matrix.

# Give me row[1] for each row in matrix M, in a new list.
# The result is a new list containing column 2 of the matrix.
col2 = [row[1] for row in M] # Collect the items in column 2
print('col2 :', col2) #  [2, 5, 8]

# range: a built-in that generates successive integers
print('list(range(4)) :', list(range(4)))  #  [0, 1, 2, 3]

# from −6 to +6 by 2
print('list(range(-6, 7, 2)) :', list(range(-6, 7, 2)))  #  [-6, -4, -2, 0, 2, 4, 6]

# Filter out odd items
print('[row[1] for row in M if row[1] % 2 == 0] ::', [row[1] for row in M if row[1] % 2 == 0] )  # [2, 8]

# Add 1 to each item in column 2
print('[row[1] + 1 for row in M] ::', [row[1] + 1 for row in M] )  #[3, 6, 9]

# Create a set of row sums
print('M :', M)
print('{sum(row) for row in M}', {sum(row) for row in M}) # Result not in same order as the list

G = (sum(row) for row in M)
print('type(G) :', type(G))
print('G :', G)
