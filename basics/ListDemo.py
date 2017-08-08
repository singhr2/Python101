# ListDemo.py

# To run from python interpreter
# > cd D:\dev\python\Python101\basics\StringDemo.py
# > python
# > exec(open('StringDemo.py').read())
#

# List have no fixed type constraint
# lists have no fixed size i.e. they can grow and shrink on demand, 
# in response to list-specific operations

# They are also mutable—unlike strings, lists can be modified in place by assignment to
#offsets as well as a variety of list method calls

myList = ['one', 'two', 'three']
print('myList :', myList)
print('total elements :', len(myList))

myListOfDifferentObjects = ['one', 2, False]
print('myListOfDifferentObjects :', myListOfDifferentObjects)
print('2nd element in list :', myListOfDifferentObjects[1])

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

# Append
print('\n -->>> append() example');
print('before :', languagesList);
languagesList.append('Python')
print('after :', languagesList);


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

# list comprehension expression
#Give me row[1] for each row in matrix M, in a new list.
# The result is a new list containing column 2 of the matrix.

M=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
col2 = [row[1] for row in M] # Collect the items in column 2
print('col2 :', col2)



# range—a built-in that generates successive integers
print('list(range(4)) :', list(range(4)))
# from −6 to +6 by 2 
print('list(range(-6, 7, 2)) :', list(range(-6, 7, 2)))
