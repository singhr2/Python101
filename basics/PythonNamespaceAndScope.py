# PythonNamespaceAndScope.py

# Reference
# 1) https://www.python-course.eu/python3_global_vs_local_variables.php
# 2) http://python-textbok.readthedocs.io/en/1.0/Variables_and_Scope.html


# Everything in Python is an object. Name is a way to access the underlying object.
# For example, when we do the assignment a = 2, here
# 		2 is an object stored in memory and 
#		a is the name we associate it with.
# We can get the address (in RAM) of some object through the built-in function, id().

# namespace = collection of names; a place where names live.
# 	Each module creates its own global namespace.


# [global variable]
# A variable which is defined in the main body of a file is called a global variable.
# It will be visible throughout the file, and also inside any file which imports that file.

# <!> <!> <!> Avoid the temptation to use globals whenever you can—they tend to make programs difficult to understand and reuse, 
# and won’t work for cases where one copy of saved data is not enough.
# Try to communicate by calling functions, passing in arguments and getting back return values.

# [local variable]
# A variable which is defined inside a function is local to that function.
# It is accessible from the point at which it is defined until the end of the function, and exists for as long as the function is executing.

# The parameter names in the function definition behave like local variables, 
# but they contain the values that we pass into the function when we call it.

'''
* Functions define a local scope and modules define a global scope
* variable scopes are determined entirely by the locations of the variables in the source code of your program files, not by function calls.
* Also note that any type of assignment within a function classifies a name as local
• If a variable is assigned inside a def, it is 'local' to that function.
• If a variable is assigned in an enclosing def, it is 'nonlocal' to nested functions.
• If a variable is assigned outside all defs, it is 'global' to the entire file.
	=> When you hear “global” in Python, think “module.”
	
<!> Name references search at most four scopes: local, then enclosing functions (if any), then global{enclosing module}, then built-in.
	
<!> If you need to assign a name that lives at the top level of the module enclosing the function, 
		you can do so by declaring it in a 'global' statement inside the function. 
		
<!> If you need to assign a name that lives in an enclosing def, 
		as of Python 3.X you can do so by declaring it in a 'nonlocal' statement.	

<!> code typed at the interactive command prompt lives in a module, too, and follows the normal scope rules: 
		they are global variables, accessible to the entire interactive session
'''

'''
	Python’s name-resolution scheme is sometimes called the LEGB rule
	When you use an unqualified name inside a function, Python searches up to four scopes
	— the local (L) scope i.e. function , then 
	- the local scopes of any enclosing (E) defs and lambdas, then 
	- the global (G) scope i.e. Module, and then 
	- the built-in (B) scope — and stops at the first place the name is found. 
		* the built-in scope is just a built-in module called builtins
		* The built-in scope is implemented as a standard library module named builtins in 3.X
	
	
	Note: 
	* global statement tells Python that a function plans to change one or more global names
	* Modules refer to a file containing Python statements and definitions.
	* If the name is not found during this search, Python reports an error.
'''

# ---------------------
# ---- example 1 -----
# ---------------------
print('\n ----- executing example 1')

X = 'Global'  # Global (module) scope


def func():
    # shadows name 'X' from outer scope
    X = 'Local'  # Local (function) scope
    print('Local X:', X)  # prints -> Local X: Local


print(' Global X :', X)  # prints -> Global X : Global

func()


# ---------------------
# ---- example 2 -----
# ---------------------
print('\n ----- executing example 2')


def f1():
    # below statement (if uncommented) will return -> UnboundLocalError: local variable 's' referenced before assignment
    # print(s)
    s = "local !!!"  # local scope
    print('f1().a :', s)  # prints -> f1().a : local !!!


s = "Global !!!"  # Global scope

f1()

print('2.b :', s)  # prints -> 2.b : Global !!!


#---------------------
# ---- example 3 ------
# ---------------------
print('\n ----- executing example 3')


def f2():
    '''
    In this case (i.e. global s), all references to x are interpreted as references to the s from the module namespace.
    Note that the global declarations must be placed at the beginning of the function, and
    that it affects all uses of the variable inside the function.
    '''
    global s
    print('f2().a :',  s)  # prints -> f2().a : !!! Global !!!

    s = "!!! local !!!"  # local scope
    print('f2().b :', s)  # prints -> f2().b : !!! local !!!


s = "!!! Global !!!"  #

f2()

# Why local is printed ???
print('3.c :', s)  # prints -> 3.c : !!! local !!!



#---------------------
# ---- example 4 ------
# ---------------------
print('\n ----- executing example 4')
def hider():
    open = 'spam' # Local variable, hides built-in here
	
	# The below line will no longer opens a file in this scope!
	# TypeError: 'str' object is not callable
    # open('data.txt') 

hider()

#---------------------
# ---- example 5 ------
# ---------------------


