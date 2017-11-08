#ClassInstance.py

# classes serve as a sort of object factory
class Person: # Base class
    # constructor
    # called automatically when an instance is made and has a special first argument self
    # self is the newly created instance object

    '''    
    def __init__(self, pname, pjob, ppay): # local variable are pname, pjob, ppay (in scope of __init__ method)
        self.name = pname # state information/Instance Attributes : name, job, pay
        self.job=pjob
        self.pay=ppay
    '''

    # Definitioan with defaults        
    def __init__(self, lname, ljob=None, lpay=111):
        self.name = lname
        self.job=ljob
        self.pay=lpay


    def lastName(self) :
    	return self.name.split()[-1]

    def giveHike(self, percentHike)	:
    	#self.pay *= percentHike
    	hike = int(self.pay * percentHike)
    	print('hike calculated :', hike)
    	self.pay = int (self.pay + hike)

if __name__ == '__main__':
 	print ('This program is being run by itself')
else:
   	print ('I am being imported from another module')

# Allow this file to be imported as well as run/tested 
if __name__ == '__main__':
    # person1 and person2 are both namespace objects—like all class instances
    person1 = Person('Steve Jobs', 'CEO', 9999)
    person2 = Person('Bill Gates')
    print('Salary of', person1.name, '  :', person1.pay) # Salary of Steve Jobs   : 9999
    print('Salary of', person2.name, '  :', person2.pay) # Salary of Bill Gates   : 111

    print('Last name of ', person2.name, ' is :', person2.lastName())

    print('Current salary of ', person1.name, ' is :', person1.pay)
    #person1.pay *= .1
    person1.giveHike(1) # 100 %
    print('New salary of ', person1.name, ' is :', person1.pay)

    print('Current salary of ', person2.name, ' is :', person2.pay)
    person2.giveHike(.1) # 10 %
    print('Current salary of ', person2.name, ' is :', person2.pay)

