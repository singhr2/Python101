# Class101.py

'''
classes are essentially factories for generating multiple instances
classes are mostly just namespaces—that is, tools for defining names (i.e., attributes) that export data and logic to clients.

A class consists of two parts: the header and the body. 

Like everything else, class names always live within a module
more than one class can be coded in a single module file

common convention in Python dictates that class names should begin with an uppercase letter, to help make them more distinct from module names

Python’s class model is extremely dynamic. 
Classes and instances are just namespace objects, with attributes created on the fly by assignment.

The instances possess dictionaries __dict__, which they use to store their attributes and their corresponding values.

Python automatically calls a method named __init__ each time an instance is generated from a class
The new instance is passed in to the self argument of __init__ as usual
! The __init__ method is known as the constructor because of when it is run
If no __init__ is present, class calls return an empty instance, without initializing it.
'''

####
# class vs module
###
'''
• Modules
— Implement data/logic packages
— Are created with Python files or other-language extensions
— Are used by being imported
— Form the top-level in Python program structure

• Classes
— Implement new full-featured objects
— Are created with class statements
— Are used by being called
— Always live within a module
'''


'''
# a class that does nothing and have no attribute

class DerivedClassName(BaseClassName):
    pass
'''

'''
statement’s general form:

    class name(superclass,...): # Assign to name
        attr = value            # Shared class data
        def method(self,...):   # Methods
            self.attr = value   # Per-instance data
'''

def convertToUppercase(someObj):
	return someObj.name.upper()


class Person:
    def __init__(self, first, last): # class header
        self.firstname = first # members / attributes
        self.lastname = last

    def Name(self): # self is the new object of class
        return self.firstname + " " + self.lastname


# class Employee extends Person
class Employee(Person):
	# If no __init__ is present, class calls return an empty instance, without initializing it.
    def __init__(self, first, last, staffnum): # constructor
        
        # Calling Superclass Constructors

        # option-1
        Person.__init__(self,first, last) 
        
        # option-2
        #super().__init__(first, last) 


        self.staffnumber = staffnum

    def GetEmployee(self):
        return self.Name() + ", " +  self.staffnumber

#Each instance object inherits class attributes and gets its own namespace.
x = Person("Ranbir", "Singh")
y = Employee("James", "Bond", "1007")

print('-------------------')
print(x.Name())
print(y.GetEmployee())


z = Employee("Arnold", "LName", 123.45) #

#polymorphism 
#means that the meaning of an operation depends on the object being operated on. 
# here, staffnumber is assigned float value while for y it was assigned string
print(z.staffnumber)


# ------------------------
#  Special attributes: 
# ------------------------
#__dict__ is the dictionary containing the class’s namespace; i.e. is the attribute dictionary;
print(z.__dict__) # {'name': 'Ranbir'}
print(z.__dict__.keys()) # dict_keys(['name'])

#
#__str__ and __repr__ in Python
#
# __repr__ is a built-in function used to compute the "official" string reputation of an object, while 
# __str__ is a built-in function that computes the "informal" string representations of an object.
# __repr__ is more for developers while __str__ is for end users.
# Implement __repr__ for every class you implement. There should be no excuse.
# Implement __str__ for classes which you think readability is more important of non-ambiguity.

print()
print()

#
# __name__ is the class name { works with class name NOT with instance}
#
# Not working , returns error -> AttributeError: 'Employee' object has no attribute '__name__'
#print(z.__name__)
#This works
print('Employee.__name__ :', Employee.__name__) # Employee.__name__ : Employee


# __class__ is the instance’s class.
print('each instance has a link to its class that Python creates for us—it’s called __class__')
print(z.__class__) # <class '__main__.MyEmptyClass'>


# __module__ is the module name in which the class was defined;
print('z.__module__ :', z.__module__) # Employee.__module__ : __main__

# __bases__ is a tuple containing the base classes, in the order of their occurrence in the base class list; 
# Not working , returns error ->  AttributeError: 'Employee' object has no attribute '__bases__'
#print(z.__bases__)

print('Employee.__bases__ :', Employee.__bases__) # Employee.__bases__ : (<class '__main__.Person'>,)

# __doc__ is the class’s documentation string, or None if undefined; 
print('z.__doc__ :', z.__doc__) # z.__doc__ : None


# ------------------------------------------------------------------------
class MyEmptyClass: pass # Empty namespace object
# classes are objects in their own right, even without instances.
MyEmptyClass.name = 'Bob' # Just objects with attributes
print(MyEmptyClass.name) # Note: Acessing by class name w/o creating object
x2 = MyEmptyClass() # Instance-based records
y2 = MyEmptyClass()

# __dict__ literally is an instance’s attribute namespace.
# the below will print -> ??? {'__module__': '__main__', '__dict__': <attribute '__dict__' of 'MyEmptyClass' objects>, ...
print('???', MyEmptyClass.__dict__)


# name is stored on the class only
print('before :', MyEmptyClass.name, x2.name, y2.name) # prints -> before : Bob Bob Bob
x2.name = 'Ranbir'
print('after :', MyEmptyClass.name, x2.name, y2.name) # prints -> after : Bob Ranbir Bob

print(convertToUppercase(x2))


# -------------------
class rec: pass
rec.name = 'Bob'
rec.age = 40
print(rec.name)
x = rec() # Instances inherit class names
print(x.age) # 40

# Indexing dict does not do inheritance, returns error -> KeyError: 'age'
# print(x.__dict__['age']) 
print(x.__class__) # <class '__main__.rec'>
print(rec.__bases__) # (<class 'object'>,)