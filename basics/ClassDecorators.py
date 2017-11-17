# ClassDecorators.py

'''
Python decorators—similar to the notion and syntax of annotations in Java— 
both addressed this specific need and provided a general tool for adding logic that manages both functions and classes, or later calls to them.

This is called a “decoration,” but in more concrete terms is really just a way to run extra processing steps at function and 
class definition time with explicit syntax. It comes in two flavors:
• Function decorators—the initial entry in this set, added in Python 2.4—augment
function definitions. They specify special operation modes for both simple functions
and classes’ methods by wrapping them in an extra layer of logic implemented
as another function, usually called a metafunction.

• Class decorators—a later extension, added in Python 2.6 and 3.0—augment class
definitions. They do the same for classes, adding support for management of whole
objects and their interfaces. Though perhaps simpler, they often overlap in roles
with metaclasses.
'''

