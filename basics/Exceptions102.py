# Exceptions102.py


# raise Statement
# To trigger exceptions explicitly, you can code raise statements.
#
# syntax: 
#  > raise instance # Raise instance of class
#   e.g., raise IndexError() # Instance (created in statement)
#
#  > raise class    # Make and raise instance of class: makes an instance
#   e.g., raise IndexError # Class (instance created)
#
#  > raise          # Reraise the most recent exception



# raise newexception from otherexception
'''
When the from is used in an explicit raise request, 
the expression following from specifies another exception class or instance 
to attach to the __cause__ attribute of the new exception being raised.
'''

try:
    print(1 / 0)
except Exception as exc:
    raise RuntimeError("Something bad happened")   # without  from clause

'''
Output: 
	Traceback (most recent call last):
	  File "Exceptions102.py", line 39, in <module>
	    print(1 / 0)
	ZeroDivisionError: division by zero

	During handling of the above exception, another exception occurred:  <-------

	Traceback (most recent call last):
	  File "Exceptions102.py", line 41, in <module>
	    raise RuntimeError("Something bad happened")
	RuntimeError: Something bad happened
'''

try:
    print(1 / 0)
except Exception as exc:
    raise RuntimeError("Something bad happened") from exc

'''
OUTPUT: 
	Traceback (most recent call last):                                          
	  File "Exceptions102.py", line 39, in <module>                             
	    print(1 / 0)                                                            
	ZeroDivisionError: division by zero                                         
	                                                                            
	The above exception was the direct cause of the following exception:  <-------
	                                                                            
	Traceback (most recent call last):                                          
	  File "Exceptions102.py", line 41, in <module>                             
	    raise RuntimeError("Something bad happened") from exc                   
	RuntimeError: Something bad happened                                        
'''
