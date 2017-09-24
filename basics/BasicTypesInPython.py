# BasicTypesInPython.py

# To run from python interpreter
# > cd D:\dev\python\Python101\basics\
# > python
# > exec(open('BasicTypesInPython.py').read())
#

# http://www.diveintopython3.net/native-datatypes.html

'''
In Python, types are determined automatically at runtime, not in response to declarations in your code. 
This means that you never declare variables ahead of time.

Numbers, strings, lists, dictionaries, tuples, files, and sets are generally considered to be the core object (data) types. 
Types, None, and Booleans are sometimes classified this way as well. 
There are multiple number types (integer, floating point, complex, fraction, and decimal) and 
multiple string types (simple strings and Unicode strings in Python 2.X, and text strings and byte strings in Python 3.X).

They are known as “core” types because they are part of the Python language itself and are always available;

A “sequence” is a positionally ordered collection of objects. Strings, lists, and tuples are all sequences in Python. 
They share common sequence operations, such as indexing, concatenation, and slicing, but also have type-specific method calls. 

The term “mapping” denotes an object that maps keys to associated values.
Python’s dictionary is the only mapping type in the core type set. 
Mappings do not maintain any left-to-right positional ordering; they support access to data stored by key, plus type-specific method calls.

*** everything in a Python system is an object type

Built-in type		Example
--------------		------------------------------------------
None				(None object)
					None 
						A special object serves as an empty placeholder (much like a NULL pointer in C). 
						it is returned from functions that don’t explicitly return anything.
					* is always considered to be false.
					* None does not mean “undefined.” That is, None is something, not nothing (despite its name!)
					   —it is a real object and a real piece of memory that is created and given a built-in name by Python itself
					   
Booleans			True,False
						True and false are intrinsic properties of every object in Python, each object is either ture of false, as follows:
						* words True and False are equivalent to 1 and 0,
						Numbers are false if zero, and true otherwise
						Other objects are false if empty, and true otherwise
						False:	None, ‘’, [], {}, 0, 0.0, (), set([])
						True:	“something”, [1, 2], {‘eggs’: ‘spam’}, 1, 0.1, (3, 4), {5, 6}
						
Numbers				123,3.14,3+4j,0xef,Decimal,Fraction
						Integer and float-point
						Complex number
						Decimal: fixed-precision
						Fraction: rational number
					
Strings				‘spam’,”Bob’s”,b’ax01c’,u’spxc4m’

Lists				[1,[2,’Three’],4.5], list(range(10)), list(‘spam’)
						Ordered collections of arbitrary objects
						Accessed by offset
						Variable-length, heterogeneous, and arbitrarily nestable
						Of the category “mutable sequence”
						Arrays of object references
						
Tuples				(1,’spam’,4,’U’),tuple(‘spam’),namedtuple
						Ordered collections of arbitrary objects
						Accessed by offset
						Of the category “immutable sequence”
						Fixed-length, heterogeneous, and arbitrarily nestable
						Arrays of object references
						
Dicts				 {}, {‘food’:’spam’,’taste’:’yum’},dict(hours=10)
						Accessed by key, not offset position
						Unordered collections of arbitrary objects
						Variable-length, heterogeneous, and arbitrarily nestable
						Of the category “mutable mapping”
						Tables of object references (hash tables)
						
Sets				{1,’a’,’bc’},set(‘abc’)
						Unordered collections of arbitrary objects
						Accessed by iteration, membership test, not offset position
						Variable-length, heterogeneous, and arbitrarily nestable
						Of the category “mutable mapping”
						Collections of object references
						
Files				open(‘eggs.txt’)
functions			def,lambda
modules				import,`__module__`
classes				object,types,metaclasses

Ref: http://learning-python.readthedocs.io/en/latest/chapter03/README.html
'''

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
A complete inventory of Python’s numeric toolbox includes:
	• Integer and floating-point objects
	• Complex number objects
	• Decimal: fixed-precision objects (decimals are like floating-point numbers, but they have a fixed number of decimal points. )
	• Fraction: rational number objects
	• Sets: collections with numeric operations
	• Booleans: true and false
	• Built-in functions and modules: round, math, random, etc.
	• Expressions; unlimited integer precision; bitwise operations; hex, octal, and binary formats
	• Third-party extensions: vectors, libraries, visualization, plotting, etc.
	
Literal 								Interpretation
1234, −24, 0, 99999999999999 			Integers (unlimited size)
1.23, 1., 3.14e-10, 4E210, 4.0e+210 	Floating-point numbers
0o177, 0x9ff, 0b101010 					Octal, hex, and binary literals in 3.X
0177, 0o177, 0x9ff, 0b101010 			Octal, octal, hex, and binary literals in 2.X
3+4j, 3.0+4.0j, 3J 						Complex number literals
set('spam'), {1, 2, 3, 4} 				Sets: 2.X and 3.X construction forms
Decimal('1.0'), Fraction(1, 3) 			Decimal and fraction extension types
bool(X), True, False 					Boolean type and constants	
'''


'''
In Python, by contrast, variables are best
thought of not as containers but as pointers. So in Python, when you write
x = 4
you are essentially defining a pointer named x that points to some other bucket 
containing the value 4.

<!> When you use a name in a program, 
    Python creates, changes, or looks up the name in what is known as a namespace —
        a place where names live.
'''


# Two ways to import type
# Option 1 => Refer as fractions.Fraction
import fractions

# Option 2 => Refer as Fraction
# from <module-name> import <TypeName>
from fractions import Fraction 
from decimal import  Decimal


#In Python, we code to object interfaces(operations supported), not to types. 
#That is, we care what an object does, not what it is.
#Not caring about specific types means that code is automatically applicable to many of them—any object with a compatible interface will work, 
#regardless of its specific type.
#polymorphism is probably the key idea behind using Python well.

#
# !!! type is a built-in function which returns type object  !!!!
#
print('type(123.45) :', type(123.45)) # <class 'float'>

## 3.X: types are classes, and vice versa
print('type(type(123.45)) :', type(type(123.45))) # <class 'type'>

#print('self :', self)

## type testing
if type(L) == type([]):
	print('type(L) :', type(L)) #<class 'list'>
	print('type([]) :', type([])) # <class 'list'> 
	print('type(L) == type([]) ? ') #True

equalsResult = type(L) == type([])
print('equalsResult :', equalsResult) #True
print('type(equalsResult) :', type(equalsResult)) # <class 'bool'>
	
if type(L) == list: # Using the type name
	print('yes')
	
if isinstance(L, list): # Object-oriented tests
	print('yes')
	

print('\n ~~~~~~~~~~~~~~~~')
print('1) Numeric types')
print(type(1)) #<class 'int'>
print(type(1.0)) #<class 'float'>
print(type(2/3)) #<class 'float'>

#fraction numbers : rational numbers with both a numerator and a denominator
x = fractions.Fraction(1, 3) # if not imported as 'from <module> import <type>
print('x ->', x) # 1/3
print(type(x))  #<class 'fractions.Fraction'>

# Fractions: numerator+denominator
fraction1 = Fraction(2, 3)  # when imported as 'from <module> import <type>
print('fraction1 :', fraction1)# 2/3
print('fraction1+ 1 :', fraction1+ 1) # 5/3
print('fraction1 :', fraction1) # 2/3

fraction2 = Fraction(5, 3)
print('fraction2 + Fraction(1, 2) :', fraction2 + Fraction(1, 2)) #13/6


# Fraction objects can also be created from floating-point number strings
f1 = Fraction('.25') # Fraction(1, 4)
f2 = Fraction('1.25') # Fraction(5, 4)
f_sum=Fraction('.25') + Fraction('1.25') # Fraction(3, 2)

#
Fraction.from_float(1.75) #Fraction(7, 4)

# 
whatTypeIsIt = 3.141
print('type(whatTypeIsIt) :', type(whatTypeIsIt)) # <class 'float'>
print('whatTypeIsIt :', whatTypeIsIt)  # 3.141


# Decimals: fixed precision floating-point numbers
print('decimal.getcontext() :', decimal.getcontext())
print('decimal.getcontext().prec :', decimal.getcontext().prec)

#d = decimal.Decimal('3.141')
d = Decimal('3.141')
print('type(d) :', type(d)) # <class 'decimal.Decimal'>
print('d :', d) # 3.141

print('d + 1 :', d + 1)  #  4.141

# Set precision
decimal.getcontext().prec = 5 
print('d + 1 :', d + 1)  # 4.141

print('decimal division: 1.00/3.00 :', decimal.Decimal('1.00') / decimal.Decimal('3.00')) # Decimal('0.33')


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


# Booleans (with predefined True and False objects that are essentially just the integers 1 and 0 with custom display logic)
# Due to some legacy issues left over from Python 2, booleans can be treated as numbers. True is 1; False is 0.

print('\n 3) Booolean')
print(type(True))  #bool
print(type(False)) #bool
#print(type(false)) #Error
print('1 > 2 :', 1 > 2) #False
print('bool(\'spam\'):', bool('spam')) # True


#a special placeholder object called None commonly used to initialize names and objects
someVariable = None
print('someVariable :', someVariable) #None
print('type(someVariable) :', type(someVariable)) #<class 'NoneType'>

# LIST
print('\n 4) List')
S = 'shrubbery'
L = list(S)
print(type(L))  # <class 'list'>
print('List is ->', L)

L[1] = 'c'
print('Now List is ->', L)
print(S.join(L))
print('S is ->', S)

# List of None
ListOfNone = [None] * 5
print('ListOfNone :', ListOfNone)

# Map in Java
example_dict = {'RS': 'Ranbir Singh', 'SS': 'Seena Singh'}
print(example_dict['RS'])
print(type(example_dict))
print(example_dict.get('SS'))

# To check what is dict()
another_dict=dict()
print(another_dict.items())
print(another_dict.values())