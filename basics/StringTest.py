# StringTest.py

'''
    Python strings are categorized as immutable sequences, meaning that the characters they contain have a
    left-to-right positional order and that they cannot be changed in place.

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

#indexing
#In Python, characters in a string are fetched by indexing
'''
• The first item is at offset 0.
• Negative indexes mean to count backward from the end or right.
• S[0] fetches the first item.
• S[−2] fetches the second item from the end (like S[len(S)−2]).
'''

print('indexes ->[', index1, ']')
print('string1 ->[', string1, ']')
print('string1[0] ->', string1[0]) # The 1st item in string1
# Technically, a negative offset is added to the length of a string to derive a positive offset.
# S[len(S)−indexPassed]).
print('string1[-1] ->', string1[-1]) # 9+(-1) =8 =>  k
print(string1, 'starts with ck ?', string1.startswith('ck')) #False
print(string1, 'starts with Th ?', string1.startswith('Th')) #True
print(string1, 'starts with th ?', string1.startswith('th')) #False
print(string1, 'ends with ck ?', string1.endswith('ck')) #True
print(string1, 'ends with Th ?', string1.endswith('Th')) # False


#escape characters
stringWithEscapeChars = 'a\nb\tc'
# length of string

print('len('+stringWithEscapeChars+') :' + str(len(stringWithEscapeChars)) )
#len(a
#b       c) :5

#escaping special character (r in front of string)
stringWithEscapeChars2 = r'a\nb\tc'
print('len('+stringWithEscapeChars2+') :' + str(len(stringWithEscapeChars2)) ) # len(a\nb\tc) :7


## Slicing: extract a section ##
#Slicing (S[i:j]) extracts contiguous sections of sequences
# In a slice, the left bound defaults to zero, and
# the right bound defaults to the length of the sequence being sliced.
'''
• The upper bound is noninclusive.
• Slice boundaries default to 0 and the sequence length, if omitted.
• S[1:3] fetches items at offsets 1 up to but not including 3.
• S[1:] fetches items at offset 1 through the end (the sequence length).
• S[:3] fetches items at offset 0 up to but not including 3.
• S[:−1] fetches items at offset 0 up to but not including the last item.
• S[:] fetches items at offsets 0 through the end—making a top-level copy of S
'''

print('string1[4:7] ->', string1[4:7])  # Slice of S from offsets 4 through 6 (not 7)
print('string1[:] ->', string1[:]) #  = 0:len(string1)
print('string1[:-1] ->', string1[:-1]) #  = 0:len(string1)
print('string1[4:] ->',string1[4:]);
print('string1[:7] ->', string1[:7])


# Extended slicing
'''
X[I:J:K], which means “extract all the items in X, from offset I through J−1, by K.”
The third limit, K, defaults to +1, which is why normally all items in a slice are extracted from left to right.
'''
extendedSlicingStr = '1234567890abcde'
print('extendedSlicingStr :', extendedSlicingStr) #1234567890abcde
print('extendedSlicingStr[1:10:2] :', extendedSlicingStr[1:10:2]) #24680 (note 2 has index 1)
print('extendedSlicingStr[::2] :',extendedSlicingStr[::2]) #13579ace
print('extendedSlicingStr[::-2] :',extendedSlicingStr[::-2]) #eca97531

# Repeating string
repeatMe= 'Hello'
print('repeatMe * 3 :', repeatMe * 3)  #HelloHelloHello

# joining strings
myStr2='World'
print(repeatMe+myStr2) #HelloWorld
print('myStr2[1]) :', myStr2[1]) #o

# remove whitespace
stringWithLeadingAndTrailingSpaces='  Hello  '
print('stringWithLeadingAndTrailingSpaces : [', stringWithLeadingAndTrailingSpaces, ']')
print('> with strip [', stringWithLeadingAndTrailingSpaces.strip(), ']') #[ Hello ]
print('> with lstrip [', stringWithLeadingAndTrailingSpaces.lstrip(), ']') # [ Hello   ]
print('> with rstrip [', stringWithLeadingAndTrailingSpaces.rstrip(), ']') # [   Hello ]

# replace
print('stringWithLeadingAndTrailingSpaces : [', stringWithLeadingAndTrailingSpaces.replace(' ', '*'), ']') # [ **Hello** ]

#
print('in lowercase :', stringWithLeadingAndTrailingSpaces.lower()) #hello
print('in uppercase :', stringWithLeadingAndTrailingSpaces.upper()) #HELLO
print('in capitalize :', stringWithLeadingAndTrailingSpaces.capitalize()) # ???

#find
S = 'xxxxSPAMxxxxSPAMxxxx'
where = S.find('SPAM')
print('where :', where) #4

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

## Help on topic (uncomment below to test)
#print(help(dir))
#print(help(S.replace))




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
