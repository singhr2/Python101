#ObjPersistence.py

'''
object persistence — making objects live on after the program that creates them exits

Object persistence is implemented by three standard library modules, available in every Python:
a) pickle : Serializes arbitrary Python objects to and from a string of byte stream
	* convert object to a string of bytes
	* By storing an object’s pickle string on a file, you effectively make it permanent and persistent: 
			simply load and unpickle it later to re-create the original object.

b) dbm : Implements an access-by-key filesystem for storing strings

c) shelve : Uses the other two modules to store Python objects on a file by key
	* to store 'pickled' objects by key
	* shelve translates an object to its pickled string with pickle and stores that string under a key in a dbm file; 
	  when later loading, shelve fetches the pickled string by key and re-creates the original object in memory with pickle.


'''

#For the simplest code, use the dump() and load() functions.

import pickle

# An arbitrary collection of objects supported by pickle.
data = {
    'a': [1, 2.0, 3, 4+6j],
    'b': ("character string", b"byte string"),
    'c': {None, True, False}
}
print("original data :", data)

with open('data.pickle', 'wb') as f:  # wb = write Binary 
    # Pickle the 'data' dictionary using the highest protocol available.
    pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)
print("data pickled ")


#The following example reads the resulting pickled data.
with open('data.pickle', 'rb') as f: # rb = read Binary 
    # The protocol version used is detected automatically, so we do not
    # have to specify it.
    data = pickle.load(f)

print("unpickled data :", data)


#
# -------------------------------------------------------------------------
# Shelve
# * The shelve module implements persistent storage for arbitrary Python objects which can be pickled, using a dictionary-like API.
# -------------------------------------------------------------------------
#
'''
shelve module provides an extra layer of structure that allows you to store pickled objects by key. 
shelve translates an object to its pickled string with pickle and stores that string under a key in a dbm file; 
when later loading, shelve fetches the pickled string by key and re-creates the original object in memory with pickle.

The shelf is accessed by keys, just as with a dictionary. The values are pickled and written to a database created and managed by anydbm.
'''

import shelve

#Creating a new Shelf
s = shelve.open('test_shelf.db')
try:
    s['key1'] = { 'int': 10, 'float':9.5, 'string':'Sample data' }
finally:
    s.close()



#To access the data again, open the shelf and use it like a dictionary:
# s = shelve.open('test_shelf.db')
# print (s['key1'])
# -or-
#  to open the database 'read-only', pass the flag 
#s = shelve.open('test_shelf.db', flag='r')




# Note:
# Changes done to existing object will not get auto-reflected in shelve.
# we need to manually update the shelf explicitly by storing the item again

#To automatically catch changes to volatile objects stored in the shelf, 
#open the shelf with writeback enabled. The writeback flag causes the shelf to remember 
#all of the objects retrieved from the database using an in-memory cache. 
#Each cache object is also written back to the database when the shelf is closed.
s = shelve.open('test_shelf.db', writeback=True)
try:
    print ('>> 1 :', s['key1'])
    s['key1']['new_value'] = 'this was not here before'
    print ('>> 2 :', s['key1'])
finally:
    s.close()

s = shelve.open('test_shelf.db', writeback=True)
try:
    print ('>> 3 :', s['key1'])
finally:
    s.close()