#BooleanTest.py

# explicit Boolean data type called bool,
# with the values True and False available as preassigned built-in names which are instances of bool, which is in turn just a subclass
# (in the object-oriented sense) of the built-in integer type int.
# True and False behave exactly like the integers 1 and 0

'''
In Python,
 integer 0 represents false,
 integer 1 represents true.

Python recognizes any empty data structure as false
nonempty data structure as true.
the notions of true and false are intrinsic properties of every object in Python—each object is either true or false, as follows:
• Numbers are false if zero, and true otherwise.
• Other objects are false if empty, and true otherwise.
"spam"      True
""          False
[1, 2]      True
[]          False
{'a': 1}    True
{}          False
1           True
0.0         False
None        False
'''
print(type(True)) #<class 'bool'>

print(type('True')) #<class 'str'>

print('isinstance(True, int) ?', isinstance(True, int)) #True

# Same value
True == 1 #True

# But a different object
True is 1 #False

# Same as: 1 or 0
True or False #True

True + 4 #5

if True:
   print ("Answer")
   print ("True")
else:
   print ("Answer")
   print ("False")
