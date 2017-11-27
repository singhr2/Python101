#Exceptions101.py

#
# try -> except -> else -> finally
# catch (except) exception
#

'''
try:
    statements # Run this main action first
except name1:
    statements # Run if name1 is raised during try block
except (name2, name3):
    statements # Run if any of these exceptions occur
except name4 as var:
    statements # Run if name4 is raised, assign instance raised to var
except:
    statements # generic; handles any exception.; Run for all other exceptions raised
else:
    statements # Run if no exception was raised during try block
finally: # The finally encloses all else
    Coding Termination Actions with finally

*** Note − 
  > You can provide 'except' clause(s), or a 'finally' clause, but not both. 
  > You cannot use 'else' clause as well along with a 'finally' clause.

  !!!!
  finally is executed regardless of whether the statements in the try block fail or succeed. 
  else is executed only if the statements in the try block don't raise an exception.
  You can almost emulate an else clause by moving its code into the try block:
  i.e.
    else: Run if no exceptions are raised in the try block.
    finally: Always perform this block on exit.
'''


print('-----------------------')
print('Run with 1 command-line argument (representing valid/invalid file_name) as needed in example (6)')
print('Sample syntax : python Exceptions101.py myFileName.ext')
print('-----------------------\n\n\n')

def f():
    x = int("f1")

try:
    f()
except ValueError as e:
    print("got it :-) ", e)

print("Let's get on")



print('\n(2)---------------------------------')
print('throw exception')
#
# throw exception
# 
try:
    try:
        f()
    except ValueError as e:
        print("## got it :-) ", e)
        print("## raising the exception again.....")
        
        # To raise the same exception
        # raise

        # To raise different exception
        raise SyntaxError("## Sorry, my fault!")
except SyntaxError as se:
        print('## got syntaxError')

print("## Let's get on")




print('\n(3)---------------------------------')
print('Custom exception + finally')
#
# Custom exception
#
class MyCustomException (Exception):
	pass

try:
    try:
        f()
    except ValueError as e:
        print("!! got it :-) ", e)
        print("!! raising the exception again.....")
        
        # To raise the same exception
        # raise

        # To raise different exception
        raise MyCustomException("!! caught MyCustomException !")
except MyCustomException as ce:
        print('!! got MyCustomException')
finally:
	   print('!! THIS MUST GET PRINTED ALWAYS')



print('\n(4)---------------------------------')
print('try with finally')

try:
    #x = float(input("Your number: "))
    x = float(1)
    inverse = 1.0 / x
finally: # finally is run on the way out regardless of whether an exception was raised,
    print("There may or may not have been an exception.")
print("The inverse: ", inverse)




print('\n(5)---------------------------------')
print('Combining try, except and finally')
try:
    x = float(input("Your number: "))
    inverse = 1.0 / x
except ValueError:
    print("You should have given either an int or a float")
except ZeroDivisionError:
    print("Infinity")
finally: 
    print("There may or may not have been an exception.")




print('\n(6)---------------------------------')
print('try... except... optional else clause...')
import sys
file_name = sys.argv[1] # <-- Read command-line arguement
print('file_name :', file_name)
text = []
try:
    fh = open(file_name, 'r')
except IOError:
    print('cannot open', file_name)
else:
    text = fh.readlines()
    fh.close()

if text:
    print(text[100])

