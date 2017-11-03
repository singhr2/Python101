#Generator.py

'''
Two language constructs delay result creation whenever possible in user-defined operations:
Generators can be better in terms of both memory use and performance in larger programs. 
They allow functions to avoid doing all the work up front, which is especially useful 
when the result lists are large or when it takes a lot of computation to produce each value. 
Generators distribute the time required to produce the series of values among loop iterations.

• Generator functions (available since 2.3) 
	> are coded as normal def statements, 
	> unlike functions, which return a whole array, a generator yields one value at a time. This requires less memory.

	when created, they are compiled specially into generators object that supports the "iteration protocol". 
	they return a result generator that can appear in any iteration context

	The state that generator functions retain when they are suspended includes both their code location,
	and their entire local scope. Hence, their local variables retain information between results, 
	and make it available when the functions are resumed.



• Generator expressions (available since 2.4) 
  	* Generator expression is similar to a list comprehension. 
  	* The difference is that a generator expression returns a generator, not a list.
	* A generator expression is created with round brackets.

'''
#An iterable object’s iterator is fetched initially with the iter built-in function

# Iterating using iterator
myList1 = [1,2,3,4]
itr1=iter(myList1)
[ print(x) for x in itr1]


#------------------------------
#Option-2
# Note: sys.exit() will stop processing any code there after in the file, hence commented.
#------------------------------
'''
import sys
itr1=iter(myList1)
while True:
   try:
      #print ('>>', next(itr1))
      print ('>>', itr1.__next__())
   except StopIteration:
      sys.exit() #you have to import sys module for this

'''


#------------------------------
# Using Generator function
#------------------------------
print('Using Generator function')
def gensquares(N):
    for i in range(N):
        yield i ** 2 # Resume here later

myGeneratorObj = gensquares(4)

print('## 1 :', next(myGeneratorObj))
print('## 2 :', next(myGeneratorObj))


# ------------------------------------------
# Generator Expressions: Iterables Meet Comprehensions
# memory-space optimization
# ------------------------------------------
'''
generator expressions are just like normal list comprehensions, and support all their syntax including if filters  and loop nesting
—but they are enclosed in parentheses instead of square brackets.

instead of building the result list in memory, they return a generator object—an automatically created iterable. 
This iterable object in turn supports the iteration protocol to yield one piece of the result list at a time in any iteration context.

'''
myList2 = [x ** 2 for x in range(4)] # List comprehension: build a list ; USES []
# above comprehension returns: [0, 1, 4, 9]
print(type(myList2)) # <class 'list'>
print(myList2) # [0, 1, 4, 9]

result2 = (x ** 2 for x in range(4)) # Generator expression: make an iterable; USES ()
# # above Generator Expression returns: <generator object <genexpr> at 0x00000000029A8288>
print(type(result2)) # <class 'generator'>
print(result2) # <generator object <genexpr> at 0x02451D80>


# e.g.,2
MyGenerator2 = (c * 4 for c in 'SPAM')
myIterator2 = iter(MyGenerator2)
print(">>> ", next(myIterator2)) # >>>  SSSS
print(">>> ", next(myIterator2)) # >>>  PPPP
print(">>> ", next(myIterator2)) # >>>  AAAA
print(">>> ", next(myIterator2)) # >>>  MMMM
print(">>> ", next(myIterator2)) #   StopIteration