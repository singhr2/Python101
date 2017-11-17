#ClassInheritance.py


'''
methods work in exactly the same way as simple functions, 
with one crucial exception: a method’s first argument always receives the instance object that is the implied subject of the method call.

Python automatically maps instance method calls to a class’s method functions as follows. 

** In Python 3.X, all classes are automatically what were formerly called “new style,”
whether they explicitly inherit from object or not. Coding the object superclass is optional and implied.

****
Method calls made through an instance, like this:
	instance.method(args...)
are automatically translated to class method function calls of this form:
	class.method(instance, args...)

In a class’s method, the first argument is usually called self by convention 
(technically, only its position is significant, not its name).
'''



class Super1 :
	def __init__(self, pName) :
		self.name=pName

	def printMe(self):
		print('Super1 :', self.name)

class Super2 :
	def __init__(self, pJob) :
		self.job=pJob

	def printMe(self):
		print('Super2 :', self.job)

class Subclass1 (Super1, Super2) :
	def __init__(self, pName1, pJob1, pEmpID) :
		self.employeeId = pEmpID
		Super1.__init__(self, pName1)
		Super2.__init__(self, pJob1)

	def printMe(self):
		print('Subclass1 :', self.name)

		#OK
		#print('Subclass1 :', self.job)
		#print('Subclass1 :', self.employeeId)

		Super1.printMe(self)
		Super2.printMe(self)

#TypeError: __init__() missing 3 required positional arguments: 'pName1', 'pJob1', and 'pEmpID'
#obj1 = Subclass1()

obj1 = Subclass1('Ranbir', 'Architect', 101)

# OK
#print(obj1.name) # Ranbir
#print(obj1.job) # Architect
#print(obj1.employeeId) # 101

obj1.printMe()


print('\n--------')
obj2 = Super1('YourName')
obj2.printMe()

# print subclasses 
print('Subclasses of Super1 :', Super1.__subclasses__())

# -----------------------------------------
# Class Interface Techniques
# ----------------------------------------

#Super: Defines a method function and a delegate that expects an action in a subclass.
class Super:
    def method(self):
        print('in Super.method') # Default behavior

    def delegate(self): # makes this class abstract superclass
        self.action() # Expected to be defined by subclasses


#Inheritor : Doesn’t provide any new names, so it gets everything defined in Super.		
class Inheritor(Super): # Inherit method verbatim
    pass


#Replacer: Overrides Super’s method with a version of its own.
class Replacer(Super): # Replace method completely
    def method(self):
        print('in Replacer.method')


#Extender : Customizes Super’s method by overriding and calling back to run the default.
class Extender(Super): # Extend method behavior
    def method(self):
        print('starting Extender.method')
        Super.method(self)
        print('ending Extender.method')


# Provider: Implements the action method expected by Super’s delegate method.
class Provider(Super): # Fill in a required method
    def action(self):
        print('in Provider.action')


if __name__ == '__main__':
    for klass in (Inheritor, Replacer, Extender):
        print('\n' + klass.__name__ + '...')
        klass().method()
    print('\nProvider...')
    x = Provider()
    x.delegate()

''' 
Output :
	                               
	Inheritor...                   
	in Super.method                
	                               
	Replacer...                    
	in Replacer.method             
	                               
	Extender...                    
	starting Extender.method       
	in Super.method                
	ending Extender.method         
	                               
	Provider...                    
	in Provider.action             
                               
'''


# Negative tests

#AttributeError: 'Super' object has no attribute 'action'
#X = Super()
#X.delegate()

# AttributeError: 'Inheritor' object has no attribute 'action'
#X2 = Inheritor()
#X2.delegate()

class Sub(Super):
	def action(self): 
		print('spam')

X3 = Sub()
X3.delegate() # spam
