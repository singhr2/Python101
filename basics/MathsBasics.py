

print('exponentiation: 2**3 :', 2**3)

myInteger=123
print(type(myInteger))

myFloatingPoint= 123.45
print(type(myFloatingPoint))


# Complex numbers have a real and imaginary part.
# Python supports complex numbers either by specifying the number in (real + imagJ) or (real + imagj) form
# or using a built-in method complex(x, y).
myComplexNum = 2+3j
print(type(myComplexNum))

print(len(str(2 ** 5)))

### modules are just packages of additional tools that we import to use:
import math
print('math.pi=', math.pi)
print('sqrt 4=', math.sqrt(4))

# Random
import random
print('random.random():', random.random())

randonNumber = random.choice([1, 2, 3, 4])
print('randomNumber:', randonNumber)