#ClassNamespace2.py

# this file is to be referred in conjugation with ClassNamespace.py

import ClassNamespace

X = 66
print(X) # 66: the global variable from this file

print(ClassNamespace.X) # 11: globals become attributes after imports

ClassNamespace.f() # 11: ClassNamespace's X, not the one here!
ClassNamespace.g() # 22: local in other file's function
print(ClassNamespace.C.X) # 33: attribute of class in other module

I = ClassNamespace.C()
print(I.X) # 33: still from class here
I.m()
print(I.X) # 55: now from instance!


