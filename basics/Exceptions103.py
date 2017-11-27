# Exceptions103.py

# 
# assert Statement
# syntactic shorthand for a common raise usage pattern, and 
# an assert can be thought of as a conditional raise statement.
# 
#


# The easiest way to think of an assertion is to liken it to a 
# raise-if statement (or to be more accurate, a raise-if-not statement). 
# An expression is tested, and if the result comes up false, an exception is raised.

def KelvinToFahrenheit(Temperature):
   # if the test evaluates to false, Python raises an AssertionError exception
   assert (Temperature >= 0),"Colder than absolute zero!"
   return ((Temperature-273)*1.8)+32

print (KelvinToFahrenheit(273)) # Output : 32.0

# AssertionError: Colder than absolute zero!
print (KelvinToFahrenheit(-5))



