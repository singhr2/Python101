#BasicFunctions.py

'''
> Python functions are objects
	
> first-class object model
  Function objects may be assigned to other names, passed to other functions, embedded in data structures, returned from one function to another, 
  and more, as if they were simple numbers or strings.
'''

#
#After a def runs, the function name is simply a reference to an object
# — you can reassign that object to other names freely and call it through any reference
#
def echo(message): # Name echo assigned to function object
    print(message)

echo('Direct call') # Call object through original name

x = echo # Now x references the function too
x('Indirect call!') # Call object through name by adding ()


#
#Passing function as parameter
#
def indirect(func, arg):
    func(arg) # Call the passed-in object by adding ()

indirect(echo, 'Argument call!') # Pass the function to another function



#
# add function objects into data structures
#
print('\n passing function as object ')

schedule = [ (echo, 'Ranbir!'), (echo, 'Singh!') ]

print(type(schedule))  # <class 'list'>
print(schedule[0])  # (<function echo at 0x004DD618>, 'Ranbir!')
print(type(schedule[0]))  # <class 'tuple'>
print(type(schedule[0][0]))  # <class 'function'>

for (func, arg) in schedule:
    func(arg)


#
# functions can also be created and returned for use elsewhere—
# the closure created in this mode also retains state from the enclosing scope:
#
# All function internals’ names have leading and trailing double underscores (“__X__”);
#


#
# Python 3 Function Annotations
#   => lets you add arbitrary metadata to function arguments and return value. 
# * coded in def header lines  
# * The annotations have no impact whatsoever on the execution of the function.  
# * Default arguments are specified after the annotation:
#   => the annotation (and its : character) appear before the default (and its = character).
# 

def func(a: 'spam', b: (1, 10), c: float) -> int:
    return a + b + c

print(func(101, 202, 303))  # 606

'''
when annotations are present, Python collects them in a 'dictionary' (key/value pair) 
and attaches it to the function object itself. 
Argument names become keys, the return value annotation is stored under key “return” if coded
'''
# {'a': 'spam', 'b': (1, 10), 'c': <class 'float'>, 'return': <class 'int'>}
print(func.__annotations__)

'''
a => spam
b => (1, 10)
c => <class 'float'>
return => <class 'int'>
'''
for arg in func.__annotations__:
    print(arg, '=>', func.__annotations__[arg])


# annotation with default
def func(a: 'spam' = 4, b: (1, 10) = 5, c: float = 6) -> int:
	return a + b + c

print(func(1, 2, 3))  # 6
print(func())  # 4 + 5 + 6 (all defaults) # 15

