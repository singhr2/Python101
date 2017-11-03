# Modules101.py

'''
> Modules are packages of names i.e., 
    places to define names you want to make visible to the rest of a system. 

> Modules are just namespaces (places where names are created), 
  and the names that live in a module are called its 'attributes'.

> Modules provide an easy way to organize components into a system 
by serving as self-contained packages of variables known as namespaces.

> internally, module namespaces are stored as dictionary objects

A program is a system of modules. 
It has one top-level script file (launched to run the program), and 
multiple module files (imported libraries of tools). 
Scripts and modules are both text files containing Python statements, 
though the statements in modules usually just create objects to be used later.

* Python automatically comes with a large collection of utility modules known as the standard library.

* Some C programmers like to compare the Python module import operation to a C #include, 
  but they really shouldn’t—in Python, imports are not just textual insertions of one file into another. 
  They are really runtime operations that perform three distinct steps the first time a program imports a given file:
	1. FIND the module’s file.
	2. COMPILE source-to-byte-code  (if needed).
		! compilation happens when a file is being imported
		! only imported files leave behind .pyc files on your machine

		byte code files are segregated in a __pycache__ subdirectory (C:/Users/user1/AppData/Local/Programs/Python/Python36-32/Lib) 
		and named with their Python version to avoid contention and recompiles when multiple Pythons are installed


	3. RUN the module’s code to build the objects it defines.


> PYTHONPATH is simply a list of user-defined and platform-specific names of directories that contain Python code files.
! module search path is a list of directories that can be customized via the environment variable PYTHONPATH, and possibly via .pth files

!!! Python chooses the first file it can find on the search path that matches the imported name.

> source code file : *.py
> byte code file : *.pyc
> optimized byte code file : *.pyo

extension modules,
Python module writtenin an external language such as C, C++, and others (e.g., Java)

'''
# !! Copy out _all_ variables
# from module1 import *

# Modules are loaded and run on the first import or from, and only the first (just once per file, per process)
# You may use reload function to explicitly load it later
# Just like def, import and from are executable statements, not compile-time declarations
import sys
print('Module Search Path :', sys.path)

# modules expose most of their interesting properties as built-in attributes,

# from <moduleName> import <name1>[,<name2>...., <nameN>]
# from always imports the entire module into memory if it has not yet been imported, 
#regardless of how many names it copies out of the file.
# Here you don't have to type <moduleName>. prefix each time you refer to variable
from sys import path
print('\nModule Search Path{again} ::', path)


# using the as extension>
# from <moduleName> import <name1> as <extension>
from sys import path as moduleSearchPath
print('\nModule Search Path{yet again} :::', moduleSearchPath)

print('------------------')
print(sys.__dict__) # __dict__ attribute associated with module objects

print('==================')
print(dir(sys)) # The dir function is roughly equivalent to the sorted keys list of an object’s __dict__ attribute


# Refer to ModuleDummy.py

print('~~~~~~~~~~~~~~~~~~~~')
import ModuleDummy as dummy
print(list(dummy.__dict__.keys()))
print('__name__ for ModuleDummy is :', dummy.__dict__['__name__'])



from ModuleDummy import a, _b, c, _d
print(a)  
print(b)  # NameError: name 'b' is not defined



#Reloading Modules
'''
a module’s code is run only once per process by default. To force a module’s code to be reloaded and rerun, 
you need to ask Python to do so explicitly by calling the reload built-in function.

The 'reload function' forces an already loaded module’s code to be reloaded and rerun. 
Assignments in the file’s new code change the existing module object in place.
'''


# --------------------------------------
# exec built-in function to run commands
# --------------------------------------
