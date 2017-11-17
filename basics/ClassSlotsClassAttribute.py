# ClassSlotsClassAttribute.py

'''
* Slots in subs are pointless when absent in supers
* Slots in supers are pointless when absent in subs
* 

'''

class SlotDemo():  # implictly extends object
	# we can use slots to prevent the dynamic creation of attributes
    __slots__ = ['name', 'job', 'attr3']

    def __init__(self, pName, pJob):
        self.name =pName
        self.job=pJob

obj1 = SlotDemo('Ranbir', 'java Dev')
print('Initial Job :', obj1.job) # 

obj1.job = 'updated'
print('New Job :', obj1.job) # 

# AttributeError: 'SlotDemo' object has no attribute 'xyz'
# to allow working, comment the __slots__ OR add xyz in the list.
#obj1.xyz='newValue'
#print('undeclared attribute - obj1.xyz :', obj1.xyz)

# AttributeError: attr3
# Reason: instance attribute names must still be assigned before they can be referenced
#print('??', obj1.attr3)

obj1.attr3 = '3rd attr value'
print('declared attribute - obj1.attr3 :', obj1.attr3)