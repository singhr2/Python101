# ClassDecorators.py

'''
<!> Functions and methods are called callable as they can be called.
In fact, any object which implements the special method __call__() is termed callable. 
So, in the most basic sense, a decorator is a callable that returns a callable.

The @ indicates the application of the decorator.

A decorator takes in a function, adds some functionality and returns it.
In the context of design patterns, decorators dynamically alter the functionality of a function, method or class 
without having to directly use subclasses.

Python decorators : 
* similar to the notion and syntax of annotations in Java 
* both addressed this specific need and provided a general tool for adding logic that manages both functions and classes, or later calls to them.

It comes in two flavors:
>>> Function decorators (Python 2.4) : augment 'function' definitions. 
 They specify special operation modes for both simple functions and classes’ methods 
 by wrapping them in an extra layer of logic implemented as another function, usually called a metafunction.
 
 Function decorators are simply wrappers to existing functions.

 For instance, they may be used to augment functions with code that logs calls made to them, 
 checks the types of passed arguments during debugging, and so on.
 
 built-in function decorators : marking static and class methods


 SYNTAX:
  @<metafunction>
  def <someFunction- a function that manages anotherfunction>:
 	logic


>>> Class decorators (added in Python 2.6 and 3.0) : augment 'class' definitions. 
  They do the same for classes, adding support for management of whole objects and their interfaces. 
  Though perhaps simpler, they often overlap in roles with metaclasses.
'''

#
# -------------------------------------------
# demo of using existing decorator
#--------------------------------------------
#

class Methods(): # object needed in 2.X for property setters
    def instanceMthd(self, x): # Normal instance method: passed a self
        print([self, x])

    @staticmethod
    def staticMthd(x): # Static: no instance passed
        print([x])

    @classmethod
    def classMthd(cls, x): # Class: gets class, not instance
        print([cls, x])

    @property # Property: computed on fetch
    def someProperty(self):
        return 'Ranbir ' + self.__class__.__name__


instance01 = Methods()

# TypeError: instanceMthd() missing 1 required positional argument: 'x'
# Methods.instanceMthd(101) 

# output: [<__main__.Methods object at 0x01F33690>, 201]
instance01.instanceMthd(201)  

Methods.staticMthd(102) # [102]
instance01.staticMthd(202) # [202]

Methods.classMthd(103) # [<class '__main__.Methods'>, 103]
instance01.classMthd(203) # [<class '__main__.Methods'>, 203]

# Output: <property object at 0x006A1E70>
print(Methods.someProperty)

# TypeError: 'str' object is not callable
#instance01.someProperty() 

# output: Ranbir Methods
print(instance01.someProperty)



#
# -----------------------------------------------------
# Custom decorator
# ref: http://python-3-patterns-idioms-test.readthedocs.io/en/latest/PythonDecorators.html
# ------------------------------------------------------
#

print('\n....Custom decorator demo...\n')

class my_decorator():

    def __init__(self, f):
        print("inside my_decorator.__init__()")
        print(type(f)) # <class 'function'>
        print('f.__name__ :', __name__) # f.__name__ : __main__
        f() # Prove that function definition has completed; calls aFunction()

    def __call__(self):
        print("inside my_decorator.__call__()")

@my_decorator
def aFunction():
    print("inside aFunction()")

print("Finished decorating aFunction()")

aFunction()

'''
Notice that the constructor for my_decorator is executed at the point of decoration of the function. 
Since we can call f() inside __init__(), it shows that the creation of f() is complete before the decorator is called. 

Output:
	inside my_decorator.__init__()
	inside aFunction()
	Finished decorating aFunction()
	inside my_decorator.__call__()
'''


#
# e.g., 2
#
#

class entry_exit(object):

    def __init__(self, f):
        print("inside entry_exit.__init__()")
        self.f = f

    def __call__(self):
        print("Entering", self.f.__name__)
        self.f()
        print("Exited", self.f.__name__)

@entry_exit
def func1():
    print("inside func1()")

@entry_exit
def func2():
    print("inside func2()")

func1()
func2()

'''
output: 
	inside entry_exit.__init__() # from @entry_exit for func1()
	inside entry_exit.__init__() # from @entry_exit for func2()

	# from func1()
	Entering func1 
	inside func1()
	Exited func1

	# from func2()
	Entering func2
	inside func2()
	Exited func2
'''