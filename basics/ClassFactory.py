#ClassFactory.py

#generator function
def factory(aClass, *pargs, **kargs): # Varargs tuple, dict
    return aClass(*pargs, **kargs) # Call aClass (or apply in 2.X only)

class Spam:
    def doit(self, message):
        print('>>> ', message)

class Person:
    def __init__(self, name, job=None):
        self.name = name
        self.job = job

    def doit(self, message):
        print('@@@ ', message)


def main():
    object1 = factory(Spam) # Make a Spam object
    print('Created Spam object')
    object1.doit('from Spam object')

    object2 = factory(Person, "Arthur", "King") # Make a Person object
    print('Created Person object')
    object2.doit('doit for Arthur object')

    object3 = factory(Person, name='Brian') # Ditto, with keywords and default
    print('Created Person object with default param')
    object2.doit('doit for Brian object')

if __name__ == '__main__':
    main()
