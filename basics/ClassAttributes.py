#ClassAttributes.py

'''
Every time we use an expression of the form 'object.attr' (where object is an instance or class object),
Python searches the namespace tree from bottom to top, 
beginning with object, looking for the first attr it can find. 
This includes references to self attributes in your methods.
'''

class ClassA:
	attrib1 = '>> Default Value for Class Attribute'

obj1 = ClassA()
obj2 = ClassA()

print('ClassA.attrib1 :', ClassA.attrib1)
print('obj1.attrib1 :', obj1.attrib1)
print('obj2.attrib1 :', obj2.attrib1)
print('----------\n ')

ClassA.attrib1 = '<<< Updated Default Value for Class Attribute'
print('ClassA.attrib1 :', ClassA.attrib1)
print('obj1.attrib1 :', obj1.attrib1)
print('obj2.attrib1 :', obj2.attrib1)
print('----------\n ')

# This creates a new instance attribute attrib1 for obj1
obj1.attrib1 = '!!! Updated Value for instance variable Obj1'
print('ClassA.attrib1 :', ClassA.attrib1)
print('obj1.attrib1 :', obj1.attrib1)
print('obj2.attrib1 :', obj2.attrib1)


## -------------------------------------------
class MixedNames: # Define class
    data = 'spam' # Assign class attr
    def __init__(self, value): # Assign method name
        self.data = value # Assign instance attr

    def display(self):
        print(self.data, MixedNames.data) # Instance attr, class attr

x = MixedNames(1) # Make two instance objects
y = MixedNames(2) # Each has its own data

# self.data differs, MixedNames.data is the same
x.display() # 1 spam
y.display() # 2 spam