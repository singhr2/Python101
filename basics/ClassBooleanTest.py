#ClassBooleanTest.py

'''
* Boolean Tests: __bool__ and __len__ * 

When you code classes, you can define what this means for your objects by coding methods that give the True or False values of instances on request.

Python first tries __bool__ to obtain a direct Boolean value; 
if that method is missing, Python tries __len__ to infer a truth value from the object’s length.
If both methods are present Python prefers __bool__ over __len__, because it is more specific

'''

class class1 :
	# __bool__ method not defined, fallback to __len__ method.
    def __len__(self):
    	# ValueError: __len__() should return >= 0
    	#return -1
    	return 1

obj1 = class1();

# returns Flase as len returns 0; else it will return True (if value is >0)
if(obj1):
    print('True')
else :
	print('False')


# ~~~~~~~~~~~~~~~~~~~~~~~~
class class2 :
    def __bool__(self):
    	return False

obj2 = class2();

# returns Flase as len returns 0; else it will return True (if value is >0)
if(obj2):
    print('True')
else :
	print('False')





