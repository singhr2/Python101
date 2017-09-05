#BooleanTest.py

# explicit Boolean data type called bool, 
# with the values True and False available as preassigned built-in names which are instances of bool, which is in turn just a subclass 
# (in the object-oriented sense) of the built-in integer type int. 
# True and False behave exactly like the integers 1 and 0

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