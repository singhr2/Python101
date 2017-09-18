# SharedReference.py
'''
This scenario in Python—with multiple names referencing the same object—is usually called a
shared reference (and sometimes just a shared object).

there are objects and operations that perform in-place object changes—Python’s mutable types,
including lists, dictionaries, and sets.

The == operator, tests whether the two referenced objects have the same values;
this is the method almost always used for equality checks in Python.
The second method, the is operator, instead tests for object identity—it returns True only if
both names point to the exact same object, so it is a much stronger form of equality testing and
is rarely applied in most programs.
'''

a = 3
b = a
a = 'spam'
print(a, b)  # spam 3

a1 = 3
b1 = a1
a1 = a1 + 2
print('\n Check-1 :', a1, b1)  # 5 3

L1 = [2, 3, 4]  # A mutable object
L2 = L1  # Make a reference to the same object
L3 = L1[:]  # Make a copy of L1 (or list(L1), copy.copy(L1), etc.)

print('\n Check-2 :')
print(L1)  # [2, 3, 4]
print(L2)  # [2, 3, 4]
print(L3)  # [2, 3, 4]

print('\n Check-3 :')
L1[1] = 999  # An in-place change
print(type(L1), L1)  # <class 'list'> [2, 999, 4]
print(L2)  # [2, 999, 4]
print(L3)  # [2, 3, 4]

print('\n Check-4 :')
L2[2] = 'Hello'
print(L1)  # [2, 999, 'Hello']
print(type(L1), L2)  # <class 'list'> [2, 999, 'Hello']
print(L3)  # [2, 3, 4]

print('\n Check-5 :')
L1 = 'Hello! Python'
print(type(L1), L1)  #<class 'str'>  Hello! Python
print(L2)  # [2, 999, 'Hello']
print(L3)  # [2, 3, 4]
