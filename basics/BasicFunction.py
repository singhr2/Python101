# BasicFunction.py

'''
> def : new statement, is an executable code
  * def creates an function object and assigns it to a function's name.
  * def is much like an = statement (i.e. assigns a name at runtime.)

  [syntax]:
  def name(arg1, arg2,... argN):  # def header line - function name ( zero or more parameters)
      statements # Function body
      ..
      # return can show up anywhere in a function body

      [return [value/None]]

  * def func(): ... # Create function object
  * func() # Call object
  * func.attr = value # Attach attributes

> return sends a result object back to the caller
> yield sends a result object back to the caller, but remembers where it left off.
> Arguments are passed by assignment (object reference).
  Arguments, return values, and variables are not declared.

> function calls can also pass arguments by name with name=value keyword syntax, and
unpack arbitrarily many arguments to send with *pargs and **kargs starred-argument notation

> variables in functions :
local : (By default) all names assigned in a function are local to that function and
        exist only while the function runs
global : global declares module-level variables that are to be assigned
'''


def times(num1, num2):
    multiplication_result = num1 * num2
    print(num1, '*', num2, '=', multiplication_result)
    return multiplication_result

times(12, 10)

# polymorphism
times('Ni', 4) # Functions are "typeless"

returnedValue = times(3.14, 4) # Save the result object
print('returnedValue :', returnedValue)


def intersect(seq1, seq2):
    local_variable1 = [] # Start empty
    for x in seq1: # Scan seq1
        if x in seq2: # Common item?
            local_variable1.append(x) # Add to end
    return local_variable1

s1 = "SINGAPORE"
s2 = "AMERICA"
answer1 = intersect(s1, s2) # ['S', 'A', 'M']
print('type(answer1) :', type(answer1))
print('intersect returned :', answer1 )

# polymorphism test (passing list instead of String)
answer2 = intersect([1, 2, 3], (1, 4))
print('intersect returned answer2 :', answer2 )


# option-2 : the function could be replaced with a single list comprehension expression
print([x for x in s1 if x in s2])


