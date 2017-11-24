#ClassInheritance2.py

'''
Diamond problem

        A
       /  \
      B    C
       \  /
        D   

 <!> Multiple inheritance with old-style (those which don't inherit from object; python 2.x) classes is governed by two rules: 
 (a) For classic classes (the default in 2.X): DFLR
 depth-first and then left-to-right (DFLR search order).
	Python climbs all the way to the top, hugging the left side of the tree, 
	before it backs up and begins to look further to the right. 

(b) For new-style classes (optional in 2.X and automatic in 3.X): MRO
"Method Resolution Order" ( MRO)
  * it’s the path Python follows for inheritance in new-style classes
	* this search proceeds across by levels before moving up. 
	* This search order is called the new-style MRO for “method resolution order” 
	(and often just MRO for short when used in contrast with the DFLR order).

	the MRO essentially works like this:
		1. List all the classes that an instance inherits from using the classic class’s DFLR
			lookup rule, and include a class multiple times if it’s visited more than once.
		2. Scan the resulting list for duplicate classes, removing all but the last occurrence of
			duplicates in the list.
'''

class A:
    def meth(s): 
        print('A.meth')

class B(A):
    pass

class C(A):
    def meth(s):
        print('C.meth')

class D(B, C): 
    pass # Use default search order

x = D() 
print("> ")
x.meth() # C.meth

# ------------------------
class D(B, C): 
    meth = C.meth # <== Pick C's method: new-style (and 3.X)

x = D()
print(">> ")
x.meth() # C.meth

# ------------------------
class D(B, C):
    meth = B.meth # <== Pick B's method: classic

x=D()
print(">>> ")
x.meth() # A.meth

# AttributeError: 'D' object has no attribute '__bases__'
#print('x.__bases__ :', x.__bases__)

# Output: D.__bases__ : (<class '__main__.B'>, <class '__main__.C'>)
print('D.__bases__ :', D.__bases__)

#----------------------------------------------------
# Change the base class
#----------------------------------------------------
# output: D.__bases__(2) : (<class '__main__.A'>,)
D.__bases__ = (A,)
print('D.__bases__(2) :', D.__bases__)

# print mro
print('D.__mro__ :', D.__mro__)