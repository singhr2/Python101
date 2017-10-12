#BasicOOPs.py

'''
Python blends support for multiple programming paradigms:
procedural (with its basic statements), 
object-oriented (with its classes), and
functional - Python includes a set of built-ins used for functional programming—tools that apply functions to sequences and other iterables. 
This set includes tools that call functions on an iterable’s items (map); filter out items based on a test function
'''


'''
a = 3
The above line results following steps: 
1. Create an object to represent the value 3.
2. Create the variable a, if it does not yet exist.
3. Link the variable a to the new object 3.
'''

# Shared References/shared object
'''
a = 3
b = a

the variables a and b wind up referencing the same object (3)
(that is, pointing to the same chunk of memory).
'''

# !!! Types Live with Objects, Not Variables

# Objects Are Garbage-Collected


# “Weak” References
'''
a weak reference, implemented by the weakref standard library module, is a
reference to an object that does not by itself prevent the referenced object from being
garbage-collected. If the last remaining references to an object are weak references, the
object is reclaimed and the weak references to it are automatically deleted (or otherwise
notified).
'''

#Copy objects
import copy
X = copy.copy(Y) # Make top-level "shallow" copy of any object Y
X = copy.deepcopy(Y) # Make deep copy of any object Y: copy all nested parts

