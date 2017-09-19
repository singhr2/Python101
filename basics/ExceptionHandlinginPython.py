# ExceptionHandlinginPython.py

'''
The code, which harbours the risk of an exception, is embedded in a try block. 
But whereas in Java exceptions are caught by catch clauses, we have statements introduced by an "except" keyword in Python. 
It's possible to create "custom-made" exceptions: With the raise statement it's possible to force a specified exception to occur.

Reference: https://www.python-course.eu/python3_exception_handling.php
'''

'''
Custom-made Exceptions

	It's possible to create Exceptions yourself:
		>>> raise SyntaxError("Sorry, my fault!")
		Traceback (most recent call last):
		  File "<stdin>", line 1, in <module>
		SyntaxError: Sorry, my fault!
		
	The best or the Pythonic way to do this, consists in defining an exception class which inherits from the Exception class. You will have to go through the chapter on "Object Oriented Programming" to fully understand the following example:
		class MyException(Exception):
			pass

		raise MyException("An exception doesn't always prove the rule!")
'''

# Following line will throw 'ValueError: invalid literal for int() with base 10: '<yourInputHere>' ' when 1.2 or a is
#  entered n = int(input("Please enter a number: "))

while True:
    try:
        n = int(input("Please enter a integer: "))  # to accept float use float(input(..))
        print('Entered value is:', n)
        break
    except ValueError:
        print('Invalid Input, retry')
    # except (IOError, ValueError):
    #	print("An I/O error or a ValueError occurred")
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise
print('Good Job !')
