# NumberFunctions.py

# To run from python interpreter
# > cd D:\dev\python\Python101\basics\
# [option-1]  
# > python
# > exec(open('NumberFunctions.py').read())
# OR
# [option-2]
# python NumberFunctions.py
# http://www.diveintopython3.net/native-datatypes.html

# Python also provides both built-in functions and
# standard library modules for numeric processing

num_1=35
print('num_1.bit_length() :', num_1.bit_length()) # ?

print('decimal number :' , num_1)  #35
print('Binary equivalent:', bin(num_1))  # 0b100011
print('Hexa equivalent:', hex(num_1))  # 0x23
print('Octa equivalent:', oct(num_1))  # 0o43

# Truncate (integer conversion)
print('int(2.567) :', int(2.567)) # 2
print('int(−2.567) :', int(-2.567)) # -2
print('int(\'01010101\'):', int('01010101')) #1010101
print('int(\'01010101\', 2):', int('01010101', 2)) #85 [arg2=base]
#print(' :', ) #

# Round (Python 3.X version)
print('round(2.567) :', round(2.567)) #3
print('round(2.467) :', round(2.467)) #2
print('round(2.567, 2) :', round(2.567, 2)) # 2.57


print('pow(2, 4) :', pow(2, 4)) #16
print('2 ** 4 :', 2 ** 4) # 16

print('abs(-42.0) :', abs(-42.0)) # 42.0
print('sum((1, 2, 3, 4)) :', sum((1, 2, 3, 4))) #10
print('min(3, 1, 2, 4) :', min(3, 1, 2, 4)) #1
print('max(3, 1, 2, 4) :', max(3, 1, 2, 4)) #4


# when you hear “module,” think “import.”
# importing built-in math module
import math # Ideally this should be moved to top

print('math.pi :', math.pi) #3.141592653589793
print('math.sqrt(144) :', math.sqrt(144)) # 12.0
print('math.sqrt(2) :', math.sqrt(2)) # 1.4142135623730951
## Floor (next-lower integer)
print('math.floor(2.567) :', math.floor(2.567)) # 2
print('math.floor(-2.567) :', math.floor(-2.567)) # -3
## Truncate (drop decimal digits)
print('math.trunc(2.567) :', math.trunc(2.567)) # 2
print('math.trunc(-2.567) :', math.trunc(-2.567)) # -2

print(' :', ) #

# ------ Random------
import random

#for <variable> in <sequence>:
# range(n) generates an iterator to progress the integer numbers starting with 0 and ending with (n -1)
# range(begin,end) # increment of range() has been 1
# range(begin,end, step) # step : increments, can be both negative and positive, but not zero
for x in range(2,5) : # print 3 random numbers e.g., 0.84462438338923, 0.47778402135365905, 0.557122347748778
	print('random[',x, '] =', random.random())

print('~~~~~~~~~~~')
for x in list(range(2,5)) :
	print('random[',x, '] =', random.random())
	
print('~~~~~~~~~~~')
for x in list(range(2,15, 4)) : # 2, 6, 10, 14
	print('random[',x, '] =', random.random())

print('~~~~~~~~~~~')	
for x in 'Ranbir' :
	print('randint[',x, '] =', random.randint(1, 10))

print('~~~~~~~~~~~')	
for y in range(1,9) :
	print(random.choice(['Ranbir', 'Shreya', 'Anshi']))

options=['one', 'two', 'threee']
print('options :', options) #  ['one', 'two', 'threee']
random.shuffle(options)
print('options :', options) # ['one', 'two', 'threee']
random.shuffle(options)
print('options :', options) #['threee', 'two', 'one']


