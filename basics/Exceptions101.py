#Exceptions101.py

#
# catch (except) exception
#
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

