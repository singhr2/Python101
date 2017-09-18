#
# MiscExamples01.py
#
# cd <directory-where-this-file-exists>
# python MiscExamples01.py
#
# Ref : 
#  https://campus.datacamp.com/courses/intro-to-python-for-data-science/chapter-3-functions-and-packages?ex=10
#  
'''
str(), to convert a value into a string. 
str(savings), for example, will convert the float savings to a string.

Similar functions such as int(), float() and bool() will help you convert Python values into any type.

the == operator, tests whether the two referenced objects have the same values;
this is the method almost always used for equality checks in Python.
The second method, the is operator, instead tests for object identity—it returns True only if
both names point to the exact same object, so it is a much stronger form of equality testing and is rarely applied in most programs.

'''

a = b = 0
b = b + 1
print(a, b) #0 1


# OPERATORS
# Exponentiation
print(4 ** 2) #16

# Modulo (returns the remainder)
print(18 % 7) #4


# convert to other types
# str(), int(), float(), bool()


# List
# List is a compound data type; you can group values together:

#my_list[start:end]
#The start index will be included, while the end index is not.

x = ["a", "b", "c", "d"]
x[1] = "r"
x[2:] = ["s", "t"]
print('x :' , x) #['a', 'r', 's', 't']

x = ["a", "b", "c", "d"]
print('x[1] :', x[1]) #b
print('x[-3]:', x[-3]) # same result!

# Merge/add lists
x = ["a", "b", "c", "d"]
print('x[1] + x[3]:', x[1] + x[3]) #bd

#-----------------------------------------------
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
print('areas :', areas)

# index() - Print out the index of the element 20.0
print(areas.index(20.0)) # 2 (3rd itm)

# count() - Print out how often 14.5 appears in areas
print(areas.count(14.5)) # 0


#-----------------------------------------------
#slice means selecting multiple elements from your list
#Slicing and dicing (2)
x = ["a", "b", "c", "d"]
print('x[:2] :', x[:2]) #['a', 'b']
print('x[2:] :', x[2:] ) # ['c', 'd']
print('[:] :',  x[:] )  #['a', 'b', 'c', 'd']

#Subsetting lists of lists
x2 = [["11", "12", "13"],
     ["21", "22", "23"],
     ["31", "32", "33"]]
print('len(x2):', len(x2)) #  3
print('x2:', x2) #	[['11', '12', '13'], ['21', '22', '23'], ['31', '32', '33']]
print('x2[2][0]:', x2[2][0]) #31
print('x2[2][:2]:', x2[2][:2]) #['31', '32']

#extend a list
x3 = ["a", "b", "c", "d"]
y3 = x + ["e", "f"]
#print(' :', )
print('x3 :', x3) #['a', 'b', 'c', 'd']
print('y3 :', y3) #['a', 'b', 'c', 'd', 'e', 'f']

#Delete list elements
x4 = ["a", "b", "c", "d"]
del(x4[1]) 
print('x4 :', x4) # ['a', 'c', 'd']


# Add lists# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]
full = first + second

# Sort full in descending order: full_sorted
full_sorted = sorted(full, reverse = True)

# Print out full_sorted
print(full_sorted) #[20.0, 18.0, 11.25, 10.75, 9.5]

# Print out type of full_sorted
print(type(full_sorted))  #<class 'list'>

# Print out length of full_sorted
print(len(full_sorted)) #5

#
x5 = ["a", "b", "c", "d"]
print('x5[:2] =',x5[:2]) #['a', 'b']
print('x5[2:] =', x5[2:]) # ['c', 'd']
print('x5[:] =', x5[:]) # ['a', 'b', 'c', 'd']


# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]


#append(), that adds an element to the list it is called on,
# e.g.,Use append twice to add poolhouse and garage size
areas.append(24.5)
areas.append(15.45)

#remove(), that removes the first element of a list that matches the input, and
# Reverse the orders of the elements in areas
print(areas.reverse())


#reverse(), that reverses the order of the elements in the list it is called on.


# ------------ Functions -----------------------
# print() , type(), len(), help(), max()


# String functions
room = "poolhouse"

# Use upper() on room: room_up
room_up = room.upper()
print(room_up) #POOLHOUSE

# Print out the number of o's in room using count()
print(room.count('o')) #3