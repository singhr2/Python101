#Class102.py
# Class Inheritance

'''
Polymorphism
* In X.method, the meaning of method depends on the type (class) of subject object X.
* Polymorphism in Python is based on object interfaces, not types (ie overloading functions).
* write your code to expect only an object interface, not a specific data type.
'''

class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    
    def lastName(self):
        return self.name.split()[-1]
    
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))
    
    def __repr__(self): # Added method
        return '[Person: %s, %s]' % (self.name, self.pay) # String to print

    # __str__ for user-friendly displays 
    #__repr__ with extra details for developers to view.
    def __repr__(self):
        return '[Person: %s, %s]' %(self.name, self.job)

    def sayHello(self, name=None):
        if name is not None:
            print ('Hello ', name, '!') 
        else:
            print ('Hello !')



class Manager(Person): # Define Manager extends(is a subclass of) Person
	# customizing constructor

    '''
    # Overloading constructor is not working
    #
    def __init__(self, name1): 
        Person.__init__(self, name1, 'mgr', 111)
    '''

    def __init__(self, name1, pay1): # Redefine constructor
        Person.__init__(self, name1, 'mgr', pay1) # Run original with 'mgr'

    # customizing one behavior in a subclass
    def giveRaise(self, percent, bonus=.25):
        #self.pay = int(self.pay * (2 + percent))
        Person.giveRaise( self, int(percent+bonus) )
    
    # additional behavior for Manager
    def getSalesPercentage(self) :
    	return self.pay * .25

    def __repr__(self):
        return '[Manager: %s, %s]' %(self.name, self.job)


# Subclass now has exactly the same behavior as Superclass
class ManagerSubclass(Manager):
    pass

#  this runs only if we are running from within the module ?
if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    mgr1 = Manager('SomeName', 876.98)
    # mgr3 = Manager('SomeName')  # TypeError: __init__() missing 1 required positional argument: 'pay'

    print('--All three--')
    for obj in (bob, sue, mgr1): # Process objects generically
        obj.giveRaise(.10) # Run this object's giveRaise
        print(obj) # Run the common __repr__

    # AttributeError: 'Person' object has no attribute 'getSalesPercentage'
    #print(bob.getSalesPercentage())

    print('mgr1.getSalesPercentage :' , mgr1.getSalesPercentage())

    thirdLevelObj = ManagerSubclass('RS', 786)
    print('>>> ', thirdLevelObj.getSalesPercentage())  # >>>  196.5


# method overloading
mgr1.sayHello() # Hello !
mgr1.sayHello('Demo User') # Hello  Demo User !


print(mgr1.__class__) # <class '__main__.Manager'>
print(Manager.__class__) #<class 'type'>

print(mgr1.__dict__) # {'name': 'SomeName', 'job': 'mgr', 'pay': 876}
print(Manager.__dict__) # {'__module__': '__main__', '__doc__': "\n    # Overloading constructor is not working\n    #\n    def __init__(self, name1): \n

print(mgr1.__dict__.keys()) # dict_keys(['name', 'job', 'pay'])
print(Manager.__dict__.keys()) # dict_keys(['__module__', '__doc__', '__init__', 'giveRaise', 'getSalesPercentage', '__repr__'])


# AttributeError: 'Manager' object has no attribute '__bases__'
#print(mgr1.__bases__)

print(Manager.__bases__) # (<class '__main__.Person'>,)
print(ManagerSubclass.__bases__) # (<class '__main__.Manager'>,)

# !!!!!!!!!!!!!!!
'''
normal method call of this form:
    instance.method(args...)
is automatically translated by Python into this equivalent form:
    class.method(instance, args...)
where the class containing the method to be run is determined by the inheritance search rule applied to the method’s name.
'''
Manager.sayHello(mgr1, 'Called through class')  # Hello  Called through class !



# TODO : https://pythonspot.com/en/encapsulation/
