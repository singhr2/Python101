#Python offers three different kinds of numbers with which you can work:
# integers, floating-point numbers (or floats), and imaginary numbers.

#There are three types of numbers in Python.
# Those are:
# integers, which are whole numbers (both negative and positive;
# floating-point numbers, which are any number with a decimal value; and
# imaginary number, which is the square-root of 1, and is used in the world of engineering and physics.

#Thee imaginary number behaves very much like a float, except that it cannot be mixed with a float.
# When you see an imaginary number, it will have the letter j trailing it e.g., 12j

#modulus operator (%) is used to return the remainder in a division

# if integers are mixed with a float, the result is a float,
# or if two integers are divided, they may also return a float, where appropriate (i.e.; 3/2).
#Dividing an integer by a floating-point decimal will always result in a floating-point number.


'''
	In Python, data takes the form of objects—either built-in objects that Python provides, or objects we create using Python tools.
	Objects are the basis of every Python program you will ever write
	Python’s core Numeric object types.
		Literal 								Interpretation
		--------------------------------		-----------------------------------
		1234, −24, 0, 99999999999999 			Integers (unlimited size)
		1.23, 1., 3.14e-10, 4E210, 4.0e+210 	Floating-point numbers
		Decimal('1.0'), Fraction(1, 3) 			Decimal and fraction extension types
		3+4j, 3.0+4.0j, 3J 						Complex number literals (realpart{optional} +imaginarypart, where the imaginarypart is terminated with a j or J.)
		0o177, 0x9ff, 0b101010 					Octal, hex, and binary literals in 3.X
		set('spam'), {1, 2, 3, 4} 				Sets: 2.X and 3.X construction forms
		bool(X), True, False 					Boolean type and constants

	Integers may be coded in decimal (base 10), hexadecimal (base 16; leading 0x or 0X), octal (base 8; leading 0o or 0O), or binary (base 2; leading 0b or 0B).
	> Octal literals: base 8, digits 0-7
	> Hex literals: base 16, digits 0-9/A-F 
	> Binary literals: base 2, digits 0-1 
	>>> oct(64), hex(64), bin(64) # Numbers=>digit strings
	('0o100', '0x40', '0b1000000')
	
	[Operators]
	Operators 					Description
	------------------			----------------------------------
	x if y else z 				Ternary selection (x is evaluated only if y is true)
	x or y 						Logical OR (y is evaluated only if x is false)
	x and y 					Logical AND (y is evaluated only if x is true)
	not x 						Logical negation
	x | y 						Bitwise OR, set union
	x & y 						Bitwise AND, set intersection	
	~x 							Bitwise NOT (inversion)
	x ^ y 						Bitwise XOR, set symmetric difference
	x in y, 					x not in y Membership (iterables, sets)
	x is y, 					x is not y Object identity tests
	x == y,x != y	 			Value equality operators
	x ** y 						Power (exponentiation)
	x % y						Modulus (remainder), format; [5%3 = 2]
	X / Y						[ 5/3 = 1.6666666666666667 ]
	X // Y						Floor division - truncates fractional remainders down to their floor,[ 5//3 = 1 ]
	
	 

 
	(...) Tuple, expression, generator expression
	[...] List, list comprehension
	{...} Dictionary, set, set and dictionary comprehensions
	
'''

# Functions
# -----------
# hex(I), oct(I), and bin(I) convert an integer to its representation string in these three bases, 
# int(str, base) : converts a runtime string to an integer per a given base(10,16, 8, 2).
# complex(real, imag) : to create complex number

int(3.1415) # Truncates float to integer => 3
float(3) # Converts integer to float => 3.0

# Adding a string to an integer results in an error, unless you manually convert one or the other;


# --- bitwise operator -----
x = 1 # 1 decimal is 0001 in bits
x << 2 # Shift left 2 bits: 0100
#prints 4
x | 2 # Bitwise OR (either bit=1): 0011
#prints 3
x & 1 # Bitwise AND (both bits=1): 0001
#prints 1



#-- Floor versus truncation --
import math
math.floor(2.5) # Closest number below value
#prints 2
math.floor(-2.5)
#prints -3
math.trunc(2.5) # Truncate fractional part (toward zero)
#prints 2
math.trunc(-2.5)
#prints -2


num1 =4023 - 22.4
print(num1)
print(type(num1))
print("%f" % (5/3))
print("%f" % (4023 - 22.4))

#To convert a number to a string, you can use the str function.
num2 =123
print(type(num2))
str1=str(num2)
print(str1)
print(type(str1))


#Number Formats
print("$%.02f" % 30.0) #$30.00
print("$%.03f" % 30.00123) #$30.001

#Use str() function to convert int to String
print("This is a string""" + str(4))

