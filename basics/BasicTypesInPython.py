# BasicTypesInPython.py

# To run from python interpreter
# > cd D:\dev\python\Python101\basics\
# > python
# > exec(open('BasicTypesInPython.py').read())
#

# http://www.diveintopython3.net/native-datatypes.html

"""
> Booleans : are either True or False.
> Numbers : can be 
		> integers (1 and 2), 
		> floats (1.1 and 1.2), 
		> complex numbers.
		> [NEW] decimal numbers, which are fixed-precision floating-point numbers, and 
		> [NEW] fraction(1/2 and 2/3) numbers, which are rational numbers with both a numerator and a denominator. 
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

print('\n ~~~~~~~~~~~~~~~~')

print('1) Numeric types')
print(type(1)) #int
print(type(1.0)) #float
print(type(2/3)) #float

import fractions
x = fractions.Fraction(1, 3)
print('x ->', x) # 1/3
print(type(x))  #<class 'fractions.Fraction'>


# 
whatTypeIsIt = 3.141
print('type(whatTypeIsIt) :', type(whatTypeIsIt)) # <class 'float'>
print('whatTypeIsIt :', whatTypeIsIt)  # 3.141


# Decimals: fixed precision
import decimal 
d = decimal.Decimal('3.141')
print('type(d) :', type(d)) # <class 'decimal.Decimal'>
print('d :', d) # 3.141

print('d + 1 :', d + 1)  # 4.1 why ???

decimal.getcontext().prec = 5 

print('d + 1 :', d + 1)  # 4.141

decimal.Decimal('1.00') / decimal.Decimal('3.00') # Decimal('0.33')


# Fractions: numerator+denominator
from fractions import Fraction 
f = Fraction(2, 3)
f + 1
Fraction(5, 3)
f + Fraction(1, 2)
Fraction(7, 6)


#Adding an int to a float yields a float.
int_1=1
float_1=2.3
sum=int_1 + float_1;
print('sum :', sum) #sum : 3.3
print(type(sum)) #float


#explicitly coerce an int to a float by calling the float() function.
int_2=2
print('float(2)', float(int_2))

#isinstance(value, type)
print('isinstance(1, int) -> ', isinstance(1, int) ) #True

print('\n 2) String')
print(type('String Value')) #<class 'str'>
print(type('True')) #<class 'str'>


#Due to some legacy issues left over from Python 2, booleans can be treated as numbers. True is 1; False is 0.

print('\n 3) Booolean')
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