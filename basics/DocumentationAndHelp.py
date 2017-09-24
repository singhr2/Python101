# DocumentationAndHelp.py

'''
dir function
    Lists of attributes available in objects


[ Python documentation strings (or docstrings) , __doc__ ]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
provide a convenient way of associating documentation with
Python modules, functions, classes, and methods.
* Python supports documentation that is automatically attached to
objects and retained at runtime for inspection.
* Docstrings can be accessed by the __doc__ attribute on objects.
* >>> import sys
  >>> print(sys.__doc__)

[ PyDoc: The help Function ]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
two most prominent PyDoc interfaces are
    the built-in help function and
    the PyDoc GUI- and web-based HTML report interfaces
e.g.,
    help() : to get the interactive help utility.
    help(sys) : for help on the str class.
    help(sys.__doc__) : Help on __doc__ method of sys module
    help(''.replace) : replace(...) method of builtins.str instance

>>> PyDoc’s all-browser mode
python -m pydoc -b
    –m Python command-line argument
    for convenience to locate PyDoc’s module file on your module import search path.
'''