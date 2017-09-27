# ScopeRulesLEGB.py
'''
LEGB lookup rule

A reference (X) looks for the name X 
	> first in the current [L]ocal scope (function); then
	> in the local scopes of any lexically [E]nclosing functions in your source code, from inner to outer;
		(also referred as statically nested scopes), then 
	> in the current [G]lobal scope (the module file); and finally 
	> in the [B]uilt-in scope (the module builtins). 
	
	Global declarations make the search begin in the global (module file) scope instead.

	* (X = value) creates or changes the name X in the current local scope, by default. 
	
	* If X is declared 'global' within the function, 
			the assignment creates or changes the name X in the enclosing module’s scope instead. 
			
	* If, on the other hand, X is declared 'nonlocal' within the function in 3.X (only), 
			the assignment changes the name X in the closest enclosing function’s local scope.

'''

X1 = 99 # Global scope name: not used
def fa():
    X1 = 88 # Enclosing def local
    def fb():
        print(X1) # Reference made in nested def
    fb()
fa() # Prints 88: enclosing def local

def f1():
    X2 = 88
	
    def f2():
        print(X2)  # Remembers X2 in enclosing def scope
	
    return f2  # Return f2 but don't call it
	
action = f1() # Make, return function
action() # Call it now: prints 88

