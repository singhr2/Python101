# ClassSpecialAttributes.py

class CoolStuffSuper(object):

    #  Class Constructor
    def __init__(self, x, y, range): 
        #super(Stuff, self).__init__()
        print('>>> CoolStuffSuper.__init__')
        self.x = x
        self.y = y
        self.range = range

    # makes instance callable as a function; called when your instance is called.
	# -- in other words, those instances now behave like functions.
    def __call__(self, x, y): 
        print('>>> CoolStuffSuper.__call__')
        self.x = x
        self.y = y
        print ('>>> __call__ with (%d,%d)' % (self.x, self.y))

    #  Class Destructor
    # run automatically when an instance’s space is being reclaimed (i.e., at “garbage collection” time)
    def __del__(self):  
        print('>>> CoolStuffSuper.__del__')

        # What is del for ?
        #del self.x
        #del self.y
        #del self.range

    # Some method.
    def greet(self):
        print('>>> hello from SuperClass')

    # __getattr__ 
    # invoked only when the attribute can not be found in object dictionary.
    #  Implementing __getattr__ causes the hasattr built-in function to always return True, unless an exception is raised from within __getattr__.
    def __getattr__(self, name):
        print('__getattr__ invoked as attribute [', name, '] not found in dictionary')
        return 123456
    
    # __setattr__
    # __setattr__ allows you to override Python's default mechanism for member assignment.
    # all attribute assignments go through __setattr__, 
    # even for variables that are present in the __dict__ magic variable. For this reason, we don't recommend implementing __setattr__.
    def __setattr__(self, name, value):
        print('__setattr__ invoked for [', name, '] with value [', value, ']')
        # print ('set %s to %s' % (name, repr(value)))

    #    if name in ('a', 'b'):
    #        object.__setattr__(self, name, value)


class CoolStuffSub(CoolStuffSuper):

    def __init__(self):
        #super(Stuff, self).__init__()
        print('### CoolStuffSub.__init__')
        CoolStuffSuper.__init__(self, 101,201,301)

    def __call__(self):
        print('### CoolStuffSub.__call__')

    def __del__(self):
        print('### CoolStuffSub.__del__')

    def greet(self):
        print('### hello from SubClass, x=', self.x) # 101


# if __name__ == '__main__':
#instance1 = CoolStuffSub()
#instance1.greet()

print('\n-----------------')
instance2 = CoolStuffSuper(1,2,3)
instance2.greet()

# Python runs a __call__ method for function call expressions applied to your instances, 
# HERE, INSTANCE instance2 IS BEHAVING LIKE A FUNCTION.
instance2(111,222) # invokes __call__ method


# ranbir attribute doesnot exist in this class, it will invoke __getattr__
# Output: 
#    __getattr__ invoked as attribute [ ranbir ] not found in dictionary
#    123456
print(instance2.ranbir)


# At the end following gets printed
# >>> CoolStuffSuper.__del__