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
        del self.x
        del self.y
        del self.range

    # Some method.
    def greet(self):
    	print('>>> hello from SuperClass')


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
instance2(111,222) # invokes __call__ method

# At the end following gets printed
# >>> CoolStuffSuper.__del__