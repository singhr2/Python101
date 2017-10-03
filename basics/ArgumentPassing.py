# ArgumentPassing.py

'''
references are implemented as pointers, all arguments are, in effect, passed by pointer.
Objects passed as arguments are never automatically copied.

Argument names in the function header become new, local names when the function
runs, in the scope of the function.

Changing a mutable object argument in a function may impact the caller.


<!> Immutable arguments (integers and strings) are effectively passed “by value.”
        It means we can pass large objects around our programs without making
        multiple copies along the way, and we can easily update these objects as we go.

<!> Mutable arguments(lists and dictionaries) are effectively passed “by pointer.”
'''


# ----------------------------------------------
print('example-\'01\'')


# Argument names may share passed objects initially (they are essentially pointers to those objects),
# but only temporarily, when the function is first called.
# As soon as an argument name is reassigned, this relationship ends.

def changer(a, b, c): # Arguments assigned references to objects
    a = 2 # Changes local name's value only
    b[0] = 'changed' # Changes shared object in place
    c['name'] = 'ChangedKeyValue'

myStringVar = 'myStrValue'
myListVar = [101, 102]
myDict={'Name': 'Ranbir', 'phone': '1800-ranbir'}
changer(myStringVar, myListVar, myDict.copy()) # Pass immutable and mutable objects, dict is passed as copy (not the original one)
# myStringVar is unchanged, myListVar is different!; myDict is unchanged
# prints -> myStrValue ['changed', 102] {'Name': 'Ranbir', 'phone': '1800-ranbir'}
print(myStringVar, myListVar, myDict)


# ----------------------------------------------
print('example-\'02\' : return multiple values')

def multiple(x, y):
    x = 2 # Changes local names only
    y = [3, 4]
    return x, y # Return multiple new values in a tuple
X = 1
L = [1, 2]
print(type(multiple(X, L)))  # <class 'tuple'>
X, L = multiple(X, L) # Assign results to caller's names
print(X, L) # (2, [3, 4])