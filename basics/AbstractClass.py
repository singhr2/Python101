#AbstractClass.py


# example-01
#
# This is not an abstract class because:
#  > we can instantiate an instance from
#  > we are not required to implement do_something in the class defintition of B 

class AbstractClass:
    def do_something(self):
        pass
    
    
class B(AbstractClass):
    pass

a = AbstractClass()
b = B()


'''
Python comes with a module which provides the infrastructure for defining Abstract Base Classes (ABCs). 
This module is called - for obvious reasons - abc.
This feature may also be used to define an expected interface, automatically verified in client classes.
'''
# example-02

from abc import ABC, abstractmethod

class AbstractClassExample(ABC):
    def __init__(self, value):
        self.value = value
        super().__init__() # ??? super needs not be 1st line (as in case of Java) - to confirm.??
    
    @abstractmethod
    def do_something(self):
        pass

# TypeError: Can't instantiate abstract class AbstractClassExample with abstract methods do_something
#a1 = AbstractClassExample()


class DoAdd42(AbstractClassExample):
    def do_something(self):
        return self.value + 42
    
class DoMul42(AbstractClassExample):
   
    def do_something(self):
        return self.value * 42
    
x = DoAdd42(10)
y = DoMul42(10)
print(x.do_something()) # 52
print(y.do_something()) # 420