# Class101.py

'''
classes are essentially factories for generating multiple instances

A class consists of two parts: the header and the body. 

Python’s class model is extremely dynamic. 
Classes and instances are just namespace objects, with attributes created on the fly by assignment.

The instances possess dictionaries __dict__, which they use to store their attributes and their corresponding values.

Python automatically calls a method named __init__ each time an instance is generated from a class
The new instance is passed in to the self argument of __init__ as usual
! The __init__ method is known as the constructor because of when it is run
If no __init__ is present, class calls return an empty instance, without initializing it.
'''

'''
class DerivedClassName(BaseClassName):
    pass
'''

def convertToUppercase(someObj):
	return someObj.name.upper()

class Person:

    def __init__(self, first, last): # class header
        self.firstname = first # members / attributes
        self.lastname = last

    def Name(self):
        return self.firstname + " " + self.lastname


# class Employee extends Person
class Employee(Person):


	# If no __init__ is present, class calls return an empty instance, without initializing it.
    def __init__(self, first, last, staffnum): # constructor
        Person.__init__(self,first, last) 
        # it can also be coded as -> 
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
print(z.staffnumber)



class MyEmptyClass: pass # Empty namespace object
# classes are objects in their own right, even without instances.
MyEmptyClass.name = 'Bob' # Just objects with attributes
print(MyEmptyClass.name) # Note: Acessing by class name w/o creating object
x = MyEmptyClass() # Instance-based records
y = MyEmptyClass()

# name is stored on the class only
print('before :', MyEmptyClass.name, x.name, y.name) # prints -> before : Bob Bob Bob
x.name = 'Ranbir'
print('after :', MyEmptyClass.name, x.name, y.name) # prints -> after : Bob Ranbir Bob



print(convertToUppercase(x))
