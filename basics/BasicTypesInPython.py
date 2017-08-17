
# http://www.diveintopython3.net/native-datatypes.html

"""
> Booleans : are either True or False.
> Numbers : can be integers (1 and 2), floats (1.1 and 1.2), fractions (1/2 and 2/3), or even complex numbers.
> Strings : are sequences of Unicode characters, e.g. an html document.
> Bytes and byte arrays, : e.g. a jpeg image file.
> Lists : are ordered sequences of values.
> Tuples : are ordered, 'immutable(unchangeable)' sequences of values.
> Sets : are unordered bags of values.
> Dictionaries : are unordered bags of key-value pairs.
"""

'''
In Python, by contrast, variables are best
thought of not as containers but as pointers. So in Python, when you
write
x = 4
you are essentially defining a pointer named x that points to some
other bucket containing the value 4.
'''

print('1) integer type')
print(type(1)) #int
print(type(1.0)) #float
print(type(2/3)) #float

import fractions
x = fractions.Fraction(1, 3)
print('x ->', x)
print(type(x))  #<class 'fractions.Fraction'>


#Adding an int to a float yields a float.
int_1=1
float_1=2.3
sum=int_1 + float_1;
print('sum :', sum)
print(type(sum)) #float

#xplicitly coerce an int to a float by calling the float() function.
int_2=2
print('float(2)', float(int_2))

#isinstance(value, type)
print('isinstance(1, int) -> ', isinstance(1, int) )

print('2) String')
print(type('String Value')) #str
print(type('True'))


#Due to some legacy issues left over from Python 2, booleans can be treated as numbers. True is 1; False is 0.

print('3) Booolean')
print(type(True))  #bool
print(type(False)) #bool
#print(type(false)) #Error

# LIST
S = 'shrubbery'
L = list(S)
print(type(L))  #list
print('List is ->', L)

L[1] = 'c'
print('Now List is ->', L)
print(S.join(L))
print('S is ->', S)

#
# Map in Java
example_dict = {'RS': 'Ranbir Singh', 'SS': 'Seena Singh'}
print(example_dict['RS'])
print(type(example_dict))
print(example_dict.get('SS'))

# To check what is dict()
another_dict=dict()
print(another_dict.items())
print(another_dict.values())