#BasicFunctions.py

'''
> Python functions are objects
	
> first-class object model
  Function objects may be assigned to other names, passed to other functions, embedded in data structures, returned from one function to another, 
  and more, as if they were simple numbers or strings.
'''

#
#After a def runs, the function name is simply a reference to an object
# — you can reassign that object to other names freely and call it through any reference
#
def echo(message): # Name echo assigned to function object
    print(message)

echo('Direct call') # Call object through original name

x = echo # Now x references the function too
x('Indirect call!') # Call object through name by adding ()


#
#Passing function as parameter
#
def indirect(func, arg):
    func(arg) # Call the passed-in object by adding ()

indirect(echo, 'Argument call!') # Pass the function to another function

