#Python offers three different kinds of numbers with which you can work:
# integers, floating-point numbers (or floats), and imaginary numbers.

#There are three types of numbers in Python.
# Those are:
# integers, which are whole numbers (both negative and positive;
# floating-point numbers, which are any number with a decimal value; and
# imaginary number, which is the square-root of 1, and is used in the world of engineering and physics.

#Thee imaginary number behaves very much like a float, except that it cannot be mixed with a float.
# When you see an imaginary number, it will have the letter j trailing it e.g., 12j

#modulus operator (%) is used to return the remainder in a division

# if integers are mixed with a float, the result is a float,
# or if two integers are divided, they may also return a float, where appropriate (i.e.; 3/2).
#Dividing an integer by a floating-point decimal will always result in a floating-point number.

num1 =4023 - 22.4
print(num1)
print(type(num1))
print("%f" % (5/3))
print("%f" % (4023 - 22.4))

#To convert a number to a string, you can use the str function.
num2 =123
print(type(num2))
str1=str(num2)
print(str1)
print(type(str1))


#Number Formats
print("$%.02f" % 30.0) #$30.00
print("$%.03f" % 30.00123) #$30.001

#Use str() function to convert int to String
print("This is a string""" + str(4))

