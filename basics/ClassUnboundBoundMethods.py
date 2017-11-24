# ClassUnboundBoundMethods.py

'''
* A function is created by the def statement, or by lambda.

>>> Unbound (class) method objects: no 'self'
* An unbound method is a simple function that can be called without an object context. 

>>> Bound (instance) method objects: self + function pairs
* A bound method is an instance method, ie. it works on an object. 
* When calling a bound method object, Python provides an instance for you automatically



* When a function is accessed on a class instance, it is transformed into a bound method, 
  that automatically supplies the instance to the method as the first self parameter.

* Python 3 doesn't have unbound methods

'''
class A(object):  # class named 'A'

    def f1(self): 
        # Through the self parameter, instance methods can freely access attributes and other methods on the same object.
        print('<A> self.__class__ :', self.__class__) # prints -> <A> self.__class__ : <class '__main__.A'>
        print('inside instance function f1')
        pass

    def f2(): 
        print('inside function f2')
        pass

    #Because the class method only has access to this cls argument, it can’t modify object instance state. 
    #That would require access to self. 
    #However, class methods can still modify class state that applies across all instances of the class.
    @classmethod
    def classmethod(cls):
        print('class method called', cls)

    # The decorator tells the built-in default metaclass type (the class of a class) 
    # to not create bound methods for method_three.
    # 
    # This type of method takes neither a self nor a cls parameter (but of course it’s free to accept an arbitrary number of other parameters).
    # Therefore a static method can neither modify object state nor class state. 
    # Static methods are restricted in what data they can access – and they’re primarily a way to namespace your methods.
    @staticmethod
    def method_three():
        print("Called method_three")

obj1 = A()  # an instance

# using 'A()'' is equivaluent to using 'obj1'

#print(A.__dict__)
#print(A.__dict__.keys())

# TypeError: f1() missing 1 required positional argument: 'self'
# A.f1()

# When a function is accessed on a class instance, it is transformed into a bound method, 
# that automatically supplies the instance to the method as the first self parameter.
A().f1() # inside function f1
# -this is equivalent to -
A.f1(obj1) # inside function f1

A.f2() # inside function f2

# TypeError: f2() takes 0 positional arguments but 1 was given
#A.f2(obj1)

# TypeError: f2() takes 0 positional arguments but 1 was given
# A().f2()

# no impact ??
#A.method_three

x=A.method_three
x() # Called method_three


#instance method
y=A.f1
#TypeError: f1() missing 1 required positional argument: 'self'
#y() 
y(obj1) # inside function f1


A().method_three() # Called method_three
A.method_three() # Called method_three


# TESTING CLASS METHODS

m1= A.classmethod
print(m1) # <bound method A.classmethod of <class '__main__.A'>>
m1() # class method called <class '__main__.A'>

A().classmethod() # class method called <class '__main__.A'>

