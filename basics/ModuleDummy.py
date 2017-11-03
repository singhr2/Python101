#ModuleDummy.py

# This is referenced in Modules101.py

# !!!!  the _<variableName> convention and __all__ list has meaning only to the from * statement form
# __all__ identifies names to be copied, while 
# _<variableName> identifies names not to be copied.
# __all__ has precedence over _X
# if __all__ is not defined, from * copies all names without a single leading underscore
# e.g.,
#__all__ = ['a', '_d'] 

a, _b, c, _d = 1, 2, 3, 4

myVar1 = 'Hello Python'

import sys 

x = sys.version

print(x)