# PythonNamespaceAndScope.py

# Reference
# 1) https://www.python-course.eu/python3_global_vs_local_variables.php
# 2) http://python-textbok.readthedocs.io/en/1.0/Variables_and_Scope.html


# Everything in Python is an object. Name is a way to access the underlying object.
# For example, when we do the assignment a = 2, here 2 is an object stored in memory and
# a is the name we associate it with.
# We can get the address (in RAM) of some object through the built-in function, id().

# namespace
# namespace is a collection of names.
# Each module creates its own global namespace.
#       Modules refer to a file containing Python statements and definitions.

# Python creates, changes, or looks up the name in what is known as a namespace —
#         a place where names live.

# [global variable]
# A variable which is defined in the main body of a file is called a global variable.
# It will be visible throughout the file, and also inside any file which imports that file.

# [local variable]
# A variable which is defined inside a function is local to that function.
# It is accessible from the point at which it is defined until the end of the function, and
# exists for as long as the function is executing.

# The parameter names in the function definition behave like local variables,
# but they contain the values that we pass into the function when we call it.

'''
* Functions define a local scope and modules define a global scope
* Also note that any type of assignment within a function classifies a name as local
• If a variable is assigned inside a def, it is local to that function.
• If a variable is assigned in an enclosing def, it is nonlocal to nested functions.
• If a variable is assigned outside all defs, it is global to the entire file.
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
