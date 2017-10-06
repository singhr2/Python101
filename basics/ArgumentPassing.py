# ArgumentPassing.py

'''
references are implemented as pointers, all arguments are, in effect, passed by pointer.
Objects passed as arguments are never automatically copied.

Argument names in the function header become new, local names when the function
runs, in the scope of the function.

Changing a mutable object argument in a function may impact the caller.


<!> Immutable arguments (integers and strings) are effectively passed “by value.”
        It means we can pass large objects around our programs without making
        multiple copies along the way, and we can easily update these objects as we go.

<!> Mutable arguments(lists and dictionaries) are effectively passed “by pointer.”

• In a FUNCTION CALL, arguments must appear in this order: 
	any POSITIONAL arguments(value); 	<- Normal argument: matched by position 
		{
			> Positional parameters are the simplest, and default kind of parameter.
			> For positional arguments, the order of the arguments matters.
		}
	followed by a combination of any KEYWORD arguments (name=value) <- Keyword argument: matched by name
	the *ITERABLE form; <- Pass all objects in iterable as individual positional arguments
	followed by the **DICT form. <- Pass all key/value pairs in dict as individual keyword arguments

• In a FUNCTION HEADER, arguments must appear in this order: 
	any NORMAL (positional) arguments(name); 
	followed by any DEFAULT arguments (name=value); 
	followed by the *name (or * in 3.X) form; 
	followed by any name or name=value keyword-only arguments (in 3.X); 
	followed by the **name form.

* matching extensions, * and **, 
  are designed to support functions that take any number of arguments.
	one star means positionals, and 
	two applies to keywords.
	

	<!> '*' in Function Calls
	An argument will be unpacked and not packed. 
	In other words, the elements of the list or tuple are singularized
 
'''


# ----------------------------------------------
print('\n example-\'01\'')

# Argument names may share passed objects initially (they are essentially pointers to those objects),
# but only temporarily, when the function is first called.
# As soon as an argument name is reassigned, this relationship ends.

def changer(a, b, c): # Arguments assigned references to objects
    a = 2 # Changes local name's value only
    b[0] = 'changed' # Changes shared object in place
    c['name'] = 'ChangedKeyValue'

myStringVar = 'myStrValue'
myListVar = [101, 102]
myDict={'Name': 'Ranbir', 'phone': '1800-ranbir'}
changer(myStringVar, myListVar, myDict.copy()) # Pass immutable and mutable objects, dict is passed as copy (not the original one)
# myStringVar is unchanged, myListVar is different!; myDict is unchanged
# prints -> myStrValue ['changed', 102] {'Name': 'Ranbir', 'phone': '1800-ranbir'}
print(myStringVar, myListVar, myDict)


# ----------------------------------------------
print('\n example-\'02\' : return multiple values')

def multiple(x, y):  # FUNCTION HEADER
    x = 202 # Changes local names only
    y = [203, 204]
    return x, y # Return multiple new values in a tuple

X = 101
L = [102, 103]
print(type(multiple(X, L)))  # <class 'tuple'>
# <!><!><!> By default, arguments are matched by position, from left to right <!><!><!>
X, L = multiple(X, L)  # FUNCTION CALL
print(X, L) # 202 [203, 204]


# ----------------------------------------------
print('\n example-\'03\' : KEYWORD ARGUMENTS - allow us to match by name')

def someFunction(param1, param2, param3):
	print(param1, param2, param3)
someFunction('One', param3='Three', param2='Two') # prints -> One Two Three


# ----------------------------------------------
print('\n example-\'04\' : Defaults')

#SyntaxError: non-default argument follows default argument 
#def someFunction2(param1='One', param2, param3):

def someFunction2(param2, param3, param1='One'):
	print(param1, param2, param3)
someFunction2(param3='Three', param2='Two') # prints -> One Two Three

# ----------------------------------------------
print('\n example-\'05\' : positional, Defaults and Optionals')

# here, all three parameters are optional (as defined default values)
def someFunction2(param1='१', param2='२', param3='३'):
	print(param1, param2, param3)

#1st param matched by Position
#2nd param matched by default
#3rd param matched by keyword
someFunction2(1, param3='Three') # prints -> 1 २ Three

# use all defaults
someFunction2() # prints -> १ २ ३


# ----------------------------------------------
''' <IMP><IMP><IMP>
if you code a default to be a mutable object like list, dict (e.g., def f(a=[])), 
the SAME, SINGLE MUTABLE OBJECT IS REUSED EVERY TIME THE FUNCTION IS LATER CALLED 
— even if it is changed in place within the function. 

The net effect is that the argument’s default retains its value from the prior call, 
and is not reset to its original value coded in the def header. 

To reset anew on each call, move the assignment into the function body instead. 
MUTABLE DEFAULTS ALLOW STATE RETENTION, but this is often a surprise.
'''
print('\n example-\'06\' :Mutable Default Arguments e.g., List, Dict');

def append_to(element, to=[]):
    to.append(element)
    return to

my_list = append_to(12)
print ('>> 1 :', my_list) # Prints -> >> 1 : [12]

my_other_list = append_to(42)
print ('>> 2 :', my_list) # Prints -> >> 2 : [12, 42]



# ----------------------------------------------
print('\n example-\'07\' : using * matching extension [in function header] ')
print('collects unmatched positional arguments into a tuple')

'''
'varargs' syntax (*name), 
	which specifies that any 'left over' arguments be passed into the varargs parameter as a tuple.
	One limitation on this is that currently, all of the regular argument slots must be filled before the vararg slot can be.
'''

def functionWithStar(param1, *args): 
	print('args: [', args, ']')

#TypeError: functionWithStar() missing 1 required positional argument: 'param1'
#functionWithStar()
functionWithStar(1)  			# args: [ () ]
functionWithStar(11,12) 		# args: [ (12,) ]
functionWithStar(111,112, 113) 	# args: [ (112, 113) ]


# ----------------------------------------------
print('\n example-\'08\' : using ** matching extension')
print('only works for keyword arguments')
print('the ** form allows you to convert from keywords to dictionaries')

def functionWithDoubleStar(param1, **args): 
	print('args: [', args, ']')
functionWithDoubleStar(1)  # args:  [ {} ]

# TypeError: functionWithDoubleStar() takes 1 positional argument but <x> were given
#functionWithDoubleStar(11,12)
#functionWithDoubleStar(111,112, 113)
functionWithDoubleStar(1, fName='Ranbir', lName='Singh') # args: [ {'fName': 'Ranbir', 'lName': 'Singh'} ]

# ----------------------------------------------
print('\nexample-\'09\' : using * and ** matching extensions')

def functionWithSingleAndDoubleStar(positionalParam, *args1, **args2): 
	print('\n')
	print('positionalParam:', positionalParam, '; args1:', args1, '; args2:', args2)

#TypeError: functionWithSingleAndDoubleStar() missing 1 required positional argument: 'keyWordParam'	
#functionWithSingleAndDoubleStar()

# positionalParam: 1 ; args1: ('PythonVersion:3.6.2',) ; args2: {}
functionWithSingleAndDoubleStar(1, 'PythonVersion:3.6.2') #  The 2nd param is string not dict

# positionalParam: 2 ; args1: ({'PythonVersion': '3.6.2'},) ; args2: {}
functionWithSingleAndDoubleStar(2, {'PythonVersion':'3.6.2'}) # The 2nd param is dict

# positionalParam: 3 ; args1: ('one', 'two') ; args2: {'fName': 'ranbir', 'lName': 'singh'}
functionWithSingleAndDoubleStar(3, *['one','two'], **{'fName':'ranbir','lName':'singh'})

# positionalParam: 4 ; args1: ('one', 'two') ; args2: {}
functionWithSingleAndDoubleStar(4, *['one','two'])

#positionalParam: 7 ; args1: ('1+', '2-', 'one', 'two') ; args2: {}
functionWithSingleAndDoubleStar(7, *['1+','2-'], *['one','two'])


# positionalParam: 5 ; args1: () ; args2: {'fName': 'ranbir', 'lName': 'singh'}
functionWithSingleAndDoubleStar(5, **{'fName':'ranbir','lName':'singh'})

# positionalParam: 6 ; args1: () ; args2: {'fName': 'ranbir', 'lName': 'singh', 'fName2': '2', 'lName2': '2'}
functionWithSingleAndDoubleStar(6, **{'fName':'ranbir','lName':'singh'}, **{'fName2':'2','lName2':'2'})


# ----------------------------------------------
print('\nexample-\'10\' : Again using * and ** matching extensions')

def func(af, b, c, d): # FUNCTION HEADER
    print(af, b, c, d)

#TypeError: func() missing 4 required positional arguments: 'a', 'b', 'c', and 'd'
#func()

#TypeError: func() missing 2 required positional arguments: 'c' and 'd'
#func(*(1, 2))

# TypeError: func() takes 4 positional arguments but 5 were given
#func(*(1, 2, 3, 4, 5))

#TypeError: func() got an unexpected keyword argument 'first'
# <!><!><!> reason for above error is 'Python will try to find parameter with name 'first' in FUNCTION HEADER  
#func(**{'first':1, 'second':2, 'third':3})

func(**{'af': 1, 'b': 2, 'c': 3, 'd': 4})


# ----------------------------------------------
print('\nexample-\'11\' : Again using * and ** matching extensions')
def f(a,b,x,y):
    print(a,b,x,y)

d = {'a':'append', 'b':'block','x':'extract','y':'yes'}
f(**d) # ('append', 'block', 'extract', 'yes')


# **(Arbitrary Keyword Parameters) in combination with *:
t = (47,11)
d = {'x':'extract','y':'yes'}
f(*t, **d) # (47, 11, 'extract', 'yes')


# ----------------------------------------------
# keyword-only arguments : arguments that must be passed by keyword only and will never be filled in by a positional argument
# keyword-only arguments are coded as named arguments that may appear after *args in the arguments list.
print('\nexample-\'12\' : keyword-only arguments')

def positional_function(foo, bar):
    print('foo :',foo,', bar: ', bar)

positional_function(3, 4)
positional_function(3, bar=4)
positional_function(foo=3, bar=4)

# For positional arguments, the order of the arguments matters. Below is an error to explain this
#TypeError: positional_function() got multiple values for argument 'foo'
#positional_function(4, foo=3)

# ----------------------------------------------
print('\nexample-\'13\' : keyword-only arguments -2')

def keyWordOnly(a, *b, c):
    print(a, b, c)
keyWordOnly(1, 2, c=3)
keyWordOnly(a=1, c=3)

# TypeError: keyWordOnly() missing 1 required keyword-only argument: 'c'
#keyWordOnly(1, 2, 3)


# ----------------------------------------------
print('\nexample-\'14\' : keyword-only arguments -2')
'''
	We can also use a * character by itself in the arguments list to indicate that a function does not accept a variable-length argument list 
	but still expects all arguments following the * to be passed as keywords. 
	In the below function, paramA may be passed by position or name again, but keyWordOnlyParam1 and keyWordOnlyParam2 must be keywords, 
	and NO EXTRA POSITIONALS are allowed
	
	keyword-only arguments with defaults are OPTIONAL, 
	but those without defaults effectively become REQUIRED keywords for the function:
'''
def keyword_only_function(paramA, *, keyWordOnlyParam1=False, keyWordOnlyParam2='*'):
	print(paramA, keyWordOnlyParam1, keyWordOnlyParam2)

keyword_only_function('1st param', keyWordOnlyParam1=True, keyWordOnlyParam2='aaa')

#TypeError: keyword_only_function() takes 1 positional argument but 3 were given
#keyword_only_function('1st param', True, 'aaa')

#TypeError: keyword_only_function() missing 1 required positional argument: 'paramA'
#keyword_only_function(keyWordOnlyParam1='someValue')

keyword_only_function(paramA='1st param2')

keyword_only_function(paramA='1st param2', keyWordOnlyParam2='someValue')

keyword_only_function(paramA='1st param3', keyWordOnlyParam1='someValue')

keyword_only_function(paramA='1st param3', keyWordOnlyParam2='--', keyWordOnlyParam1='**')



'''
	keyword-only arguments must be specified after a single star *, not two stars **
	— named arguments CANNOT APPEAR AFTER the **args arbitrary keywords form, and 
	a** can’t appear by itself in the arguments list.
'''
#SyntaxError: invalid syntax
#def kwonly(a, **pargs, b, c):
#def kwonly(a, **, b, c):


# ----------------------------------------------
print('\nexample-\'15\' : keyword-only arguments with * and **')

def f1(a, *b, c=6, **d): 
    print(a, b, c, d)

# 1 (2, 3, 4) 6 {}
f1(1, 2, 3, 4)

#1 (2, 3, 4, 5, 6) 6 {}
f1(1, 2, 3, 4, 5, 6)

#SyntaxError: positional argument follows keyword argument
#f1(1, 2, c='Hello', {'fName':'Ranbir', 'lname':'singh'})

#1 (2,) Hello {'fName': 'Ranbir', 'lname': 'singh'}
f1(1, 2, c='Hello', **{'fName':'Ranbir', 'lname':'singh'})

def f2(a, *b, c, **d): 
    print(a, b, c, d)

#TypeError: f2() missing 1 required keyword-only argument: 'c'
#f2(1, 2, 3, 4)

#TypeError: f2() missing 1 required keyword-only argument: 'c'
#f2(1, 2, 3, 4, 5, 6)

#1 (2,) Hello {'fName': 'Ranbir', 'lname': 'singh'}
f2(1, 2, c='Hello', **{'fName':'Ranbir', 'lname':'singh'})

#1 (2, 3) 7 {'x': 4, 'y': 5}
f2(1, *(2, 3), c=7, **dict(x=4, y=5))