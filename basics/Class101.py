# Class101.py

'''
A class consists of two parts: the header and the body. 

 The instances possess dictionaries __dict__, which they use to store their attributes and their corresponding values.

 Python automatically calls a method named __init__ each time an instance is generated from a class
 The new instance is passed in to the self argument of __init__ as usual
 ! The __init__ method is known as the constructor because of when it is run
 If no __init__ is present, class calls return an empty instance, without initializing it.

'''

'''
class DerivedClassName(BaseClassName):
    pass
'''

class Person:

    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def Name(self):
        return self.firstname + " " + self.lastname

class Employee(Person):

    def __init__(self, first, last, staffnum):
        Person.__init__(self,first, last) 
        # can be -> 
        #super().__init__(first, last) 

        self.staffnumber = staffnum

    def GetEmployee(self):
        return self.Name() + ", " +  self.staffnumber

x = Person("Ranbir", "Singh")
y = Employee("James", "Bond", "1007")

print('-------------------')
print(x.Name())
print(y.GetEmployee())