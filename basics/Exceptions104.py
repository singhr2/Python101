# Exceptions104.py


#
# Context Management Protocol
# example : with/as statement
#
# SYNTAX: 
#     with expression [as variable]:
#          with-block
#
# the with/as statement is designed to be an alternative to a common try/finally usage idiom; 
# like that statement, with is in large part intended for specifying
# termination-time or “cleanup” activities that


'''
where is the code that is actually being called when the variable goes out of scope? 
The short answer is, "wherever the context manager is defined." 
You see, there are a number of ways to create a context manager. 
The simplest is to define a class that contains two special methods: __enter__() and __exit__(). 

__enter__() returns the resource to be managed (like a file object in the case of open()). 
__exit__() does any cleanup work and returns nothing.


Context managers allow you to allocate and release resources precisely when you want to. 
The most widely used example of context managers is the with statement. 

A common use case of context managers is locking and unlocking resources and closing opened files

'''

with open('SampleTextFile.txt', 'w') as opened_file:
    opened_file.write('Hi there!\n')
    opened_file.write('Bye Bye!!\n')


#The above code opens the file, writes some data to it and then closes it. 
# If an error occurs while writing the data to the file, it tries to close it. 
# The above code is equivalent to:

'''
file = open('some_file', 'w')
try:
    file.write('Hola!')
finally:
    file.close()
'''


#
#
#Implementing Context Manager as a Class
# Ref: http://book.pythontips.com/en/latest/context_managers.html
#
#

'''
At the very least a context manager has an __enter__ and __exit__ methods defined. 
'''

# object known as a context manager that must have __enter__ and __exit__ methods
class MyFile(object):
    def __init__(self, file_name, method):
        print('inside __init__')
        self.file_obj = open(file_name, method)
    def __enter__(self):
        print('inside __enter__')
        return self.file_obj
    def __exit__(self, type, value, traceback):
        print('inside __exit__')
        self.file_obj.close()

with MyFile('SampleTextFile.txt', 'r') as opened_file:
    lines = opened_file.readlines()

# print using list comprehension
[print('>>', x) for x in lines]


'''
Output ->
	inside __init__
	inside __enter__
	inside __exit__
	Hi there!	<-- File contents

	Bye Bye!!
'''


#
# with statement may also specify multiple (sometimes referred to as “nested”) context managers with new comma syntax.
#
'''
with A() as a, B() as b:
    ...statements...

is equivalent to the following, which also works in 3.0 and 2.6:
with A() as a:
    with B() as b:
        ...statements...
'''

