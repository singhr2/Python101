#NamingConvention.py

'''
> Names that begin with a single underscore (_X) are not imported by a from module
import * statement
> Names that begin with two underscores and do not end with two more (__X) are
localized (“mangled”) to enclosing classes
> Names that have two leading and trailing underscores (__X__) are system-defined
names that have special meaning to the interpreter
> The name that is just a single underscore (_) retains the result of the last expression
when you are working interactively.
> names with two leading and trailing underscores (e.g., __name__) generally have special meaning
to the Python interpreter, you should avoid this pattern for your own names
'''

# Case matters: SPAM is not the same as spam

import math  # built-in module math
print('math.pi :', math.pi)

# The docstring is stored in the module's __doc__ global.
print(__doc__)