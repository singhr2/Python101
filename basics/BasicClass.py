#MyBasicUserDefinedClass.py

# To run from python interpreter
# > cd D:\dev\python\Python101\basics\
# > python
# > exec(open('BasicClass.py').read())
#

# Ref: 
# http://www.openbookproject.net/books/bpp4awd/index.html
# https://en.wikibooks.org/wiki/A_Beginner%27s_Python_Tutorial/Classes
# Learning Python 5E

'''
In abstract terms, classes define new types of objects that extend the core set.
Classes are an optional feature of Python, and simpler built-in types such as lists and dictionaries are often better tools than user-coded classes.
'''

# The function called __init__ is run when we create an instance of class
# self is the first parameter in any function defined inside a class.
# class’s methods automatically receive the instance being processed by a given method call (in the self argument)

# e.g., 1
'''
class Shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.description = "This shape has not been described yet"
        self.author = "Nobody has claimed to make this shape yet"
    def area(self):
        return self.x * self.y
    def perimeter(self):
        return 2 * self.x + 2 * self.y
    def describe(self,text):
        self.description = text
    def authorName(self,text):
        self.author = text
    def scaleSize(self,scale):
        self.x = self.x * scale
        self.y = self.y * scale
'''

class Worker:
	def __init__(self, name, pay): # Initialize when created
		self.name = name 		   # self is the new object
		self.pay = pay
	def firstName(self):
		return self.name.split()[0] # Split string on blanks		
	def lastName(self):
		return self.name.split()[-1] # Split string on blanks
	def giveRaise(self, percent):
		self.pay *= (1.0 + percent) # Update pay in place

emp1 = Worker('Ranbir Singh', 12345) # Make two instances
print('emp1.firstName() :', emp1.firstName()) # Call method: Ranbir is self

emp2 = Worker('Seena Singh', 67890)    # Each has name and pay attrs
print('emp2.lastName():', emp2.lastName()) # Seena is the self subject

emp2.giveRaise(.10) # Updates Seena's pay
print('emp2.pay(after hike):', emp2.pay)
