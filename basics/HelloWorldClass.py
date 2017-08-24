#HelloWorldClass.py

# To run from python interpreter

# > cd D:\dev\python\Python101\basics\
# > python
# > exec(open('HelloWorldClass.py').read())

# -OR-

# cd D:\dev\python\Python101\basics
# python HelloWorldClass.py
#


class HelloWorld:
	def __init__(self):
		self.firstName = 'default'
		self.lastName = 'default'
		self.salary = None
	def __init__(self, p_firstName, p_lastName, p_salary):
		self.firstName = p_firstName
		self.lastName = p_lastName
		self.salary = p_salary
	def greet(self):
		print('Hello ', self.firstName, ' ', self.lastName)
	def getFirstName(self) :
		print('First Name is:', self.firstName)
	def getLastName(self) :
		print('Last Name is:', self.lastName)
	def getSalary(self) :
		print('Salary is:', self.salary)		
	def printAttributes(self):
		print('First Name is:', self.firstName)
		print('Last Name is:', self.lastName)
		print('Salary is:', self.salary)		

		
instance1 = HelloWorld('Ranbir', 'Singh', 999999.99)
print('instance1 :', instance1)
instance1.greet()
instance1.getFirstName()
instance1.getLastName()
instance1.getSalary()
instance1.printAttributes()


# get input from user
f_name = input('Enter your first Name :')
l_name = input('Enter your last Name :')
t_salary = float(input('Enter your salary :'))
newInstance = HelloWorld(f_name, l_name, t_salary)
newInstance.printAttributes()
