#BasicLambda.py

'''
Python has two tools for building functions: def and lambda.Here’s an example. 
You can build a function in the normal way, using def, like this:
	def square_root(x): return math.sqrt(x)
or you can use lambda a.k.a. anonymous (i.e. unnamed) functions.
	square_root = lambda x: math.sqrt(x)


Python supports the creation of anonymous functions (i.e. functions that are not bound to a name) at runtime, 
using a construct called "lambda"

It is a very powerful concept that's well integrated into Python and 
is often used in conjunction with typical functional concepts like filter(), map() and reduce().

Syntax: 
	lambda arg1, arg2,... argN : expression-using-received-arguments


'''

# lambda is an expression, not a statement
#  <!> an expression returns (or evaluates to) a value, whereas a statement does not. 
#  <!> Function calls are expressions.

# Ideally, Lambda is a tool for building callback handlers.

# Because of this, a lambda can appear in places a def is not allowed by Python’s syntax
#   — inside a list literal or a function call’s arguments etc.

# Lambda functions can have any number of arguments but only one expression (not a series of statements). 
#The expression is evaluated and returned. 

# lambda’s body is a single expression, not a block of statements
# lambda definition does not include a "return" statement -- it always contains an expression which is returned.

# lambda is designed for coding simple functions,and def handles larger tasks

print(' function usin func keyword')
def func(x, y, z): 
	return x + y + z

# Here, f is assigned the function object the lambda expression creates;
print(' Achieving the same using lambda expression')
f = lambda x,y,z : x + y + z

print('Output from functional call :', func(1,2,3))  # Output from functional call : 6
print('Output from Lambda :', f(1,2,3))  # Output from Lambda : 6


# ----------------------------------------
someVar = lambda x: x * 2
print(someVar(5))  # Output: 10

# This is equivalent to 

def double(x):
   return x * 2

print('b. ', double(5))  # Output: b.  10


# ----------------------------------
# Defaults work on lambda arguments
#

x = (lambda a="Fee", b="Fie", c="Foe": a + b + c)
print(x("wee"))  # weeFieFoe

# -----------------------------------------------------------------


lower = (lambda x, y: x if x < y else y)
print(lower('aa', 'bb')) # 'aa'


# 
squares_list = list(map((lambda x: x ** 2), range(10)))
print(squares_list) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]