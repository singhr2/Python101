#Generator.py

'''
Two language constructs delay result creation whenever possible in user-defined operations:

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

#Option-2
import sys
itr1=iter(myList1)
while True:
   try:
      #print ('>>', next(itr1))
      print ('>>', itr1.__next__())
   except StopIteration:
      sys.exit() #you have to import sys module for this


# Generator function
def gensquares(N):
    for i in range(N):
        yield i ** 2 # Resume here later

myGeneratorObj = gensquares(4)

print('## ', next(myGeneratorObj))
