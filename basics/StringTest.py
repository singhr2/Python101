'''

In Python, a string type object is a sequence (left-to- right order) of characters.
Strings start and end with single or double quotes Python strings are immutable.
Single and double quoted strings are same and you can use a single quote within a string when it is surrounded by double quote and vice versa.
Declaring a string is simple, see the following statements.

http://www.w3resource.com/python/python-data-type.php
'''


#string1 ="PYTHON TUTORIAL"
#Character	P	Y	T	H	O	N	 	T	U	T	O	R	I	A	L
#Index (from left)	 0	1	2	 3	4	5	6 	7	8	9	10	11	 12	13	14
#Index (from right)	-15	-14	-13	-12	-11	-10	-9	-8	-7	-6	-5	-4	-3	-2	-1

string1 ="PYTHON TUTORIAL"

print('string1:', string1)
print('string1[0]:', string1[0])
print('string1[-1]:', string1[-1])


index1  = "012345678"
string1 = "The quick"

print('indexes ->[', index1, ']')
print('string1 ->[', string1, ']')
print('string1[0] ->', string1[0]) # The 1st item in S
print('string1[-1] ->', string1[-1]) # The last item in S


## Substring ##
# In a slice, the left bound defaults to zero, and
# the right bound defaults to the length of the sequence being sliced.
print('string1[4:7] ->', string1[4:7])  # Slice of S from offsets 4 through 6 (not 7)
print('string1[:] ->', string1[:]) #  = 0:len(string1)
print('string1[:-1] ->', string1[:-1]) #  = 0:len(string1)
print('string1[4:] ->',string1[4:]);
print('string1[:7] ->', string1[:7])

#include '
# either inside " or use \'
print("doesn\'t", 'doesn\'t')

#With special characters \t, \n
print('C:\text\new')
print(r'C:\text\new')

S2 = 'A\nB\tC' # \n is end-of-line, \t is tab
print('length of ', r'A\nB\tC', 'is ;', len(S2)) # Each stands for just one character


# Immutable
'''
Every string operation is defined to produce a new string as its result, 
because strings are immutable in Python—they cannot be changed in place after they are created. 
In other words, you can never overwrite the values of immutable objects.
'''

# TypeError: 'str' object does not support item assignment
# Uncomment below line to see error
#string1[0] = 'H' # Immutable objects cannot be changed

S='dummy'
S = 'z' + S[1:] # But we can run expressions to make new objects
print('s ->', S)

print('abc Is Alphabets :', 'abc'.isalpha())
print('abc4 Is Alphabets :', 'abc4'.isalpha())
print('Is Numeric :', 'abc4'.isnumeric())
print('Is digit :', 'abc4'.isdigit())
print('Is AlphaNumeric :', 'abc4'.isalnum())


#'in' operator in Strings
str2='Change'
print('Is \'c\' present in ', str2,  'c' in str2)
print('Is \'C\' present in ', str2,  'C' in str2)

## Find the offset of a substring in S
print("Change.find('ang') ->", str2.find('ang'))

## Replace
str2=str2.replace('ang', 'XYZ')
print('str2 ->', str2)

# String to List
line = 'aaa,bbb,ccccc,dd'
myList = line.split(',')
print('myList =', myList)
totalItemsInList = len(myList);
print('Total items in list:' , totalItemsInList)
print('Last item in list :', myList[totalItemsInList-1])


# dir: lists variables assigned in the caller’s scope
# Because methods are function attributes, they will show up in this list.
# names with double underscores in this list  relates to overloading in classes
# they represent the implementation
print(dir())
print(dir(myList))

## Help on topic
print(help(dir))
print(help(S.replace))

#
#The backslash (\) character is used to introduce a special character. See the following table.
#
#Escape sequence	Meaning
#\n	Newline
#\t	Horizontal Tab
#\\	Backslash
#\'	Single Quote
#\"	Double Quote




#Strings are arrays of characters and elements of an array can be accessed using indexing.
# Indices start with 0 from left side and -1 when starting from right side.

