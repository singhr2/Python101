#Class102.py
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





class Manager(Person): # Define Manager as subclass of Person
	# customizing constructor
    def __init__(self, name, pay): # Redefine constructor
        Person.__init__(self, name, 'mgr', pay) # Run original with 'mgr'

    # customizing one behavior in a subclass
    def giveRaise(self, percent, bonus=.25):
        #self.pay = int(self.pay * (2 + percent))
        Person.giveRaise( self, int(percent+bonus) )
    
    def getSalesPercentage(self) :
    	return self.pay * .25

    def __repr__(self):
        return '[Manager: %s, %s]' %(self.name, self.job)




if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    mgr1 = Manager('SomeName', 876.98)
    # mgr3 = Manager('SomeName')  # TypeError: __init__() missing 1 required positional argument: 'pay'

    print('--All three--')
    for obj in (bob, sue, mgr1): # Process objects generically
        obj.giveRaise(.10) # Run this object's giveRaise
        print(obj) # Run the common __repr__

    print(mgr1.getSalesPercentage())

'''
print(bob)
print(sue)
print(bob.lastName(), sue.lastName())
sue.giveRaise(.10)
print(sue)

print(mgr1)
'''

# method overloading
mgr1.sayHello() # Hello !
mgr1.sayHello('Demo User') # Hello  Demo User !



# TODO : https://pythonspot.com/en/encapsulation/
