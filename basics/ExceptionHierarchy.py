#ExceptionHierarchy.py

# Reference : https://airbrake.io/blog/python-exception-handling/class-hierarchy

'''
BaseException   <-- topmost root, printing and constructor defaults
	Exception   <-- Exception: root of user-defined exceptions
		ArithmeticError <-- root of numeric errors
			FloatingPointError
			OverflowError
			ZeroDivisionError
		AssertionError
		AttributeError
		BufferError
		EOFError
		ImportError
			ModuleNotFoundError
		LookupError <-- root of indexing errors
			IndexError
			KeyError
		MemoryError
		NameError
			UnboundLocalError
		OSError
			BlockingIOError
			ChildProcessError
			ConnectionError
				BrokenPipeError
				ConnectionAbortedError
				ConnectionRefusedError
				ConnectionResetError
			FileExistsError
			FileNotFoundError
			InterruptedError
			IsADirectoryError
			NotADirectoryError
			PermissionError
			ProcessLookupError
			TimeoutError
		ReferenceError
		RuntimeError
			NotImplementedError
			RecursionError
		StopIteration
		StopAsyncIteration
		SyntaxError
			IndentationError
				TabError
		SystemError
		TypeError
		ValueError
			UnicodeError
				UnicodeDecodeError
				UnicodeEncodeError
				UnicodeTranslateError
		Warning
			BytesWarning
			DeprecationWarning
			FutureWarning
			ImportWarning
			PendingDeprecationWarning
			ResourceWarning
			RuntimeWarning
			SyntaxWarning
			UnicodeWarning
			UserWarning
	GeneratorExit
	KeyboardInterrupt
	SystemExit


BaseException
The BaseException class is, as the name suggests, the base class for all built-in exceptions in Python. Typically, this exception is never raised on its own, and should instead be inherited by other, lesser exception classes that can be raised.

The BaseException class (and, thus, all subclass exceptions as well) allows a tuple of arguments to be passed when creating a new instance of the class. In most cases, a single argument will be passed to an exception, which is a string value indicating the specific error message.

This class also includes a with_traceback(tb) method, which explicitly sets the new traceback information to the tb argument that was passed to it.


Exception

Exception is the most commonly-inherited exception type (outside of the true base class of BaseException). In addition, all exception classes that are considered errors are subclasses of the Exception class. In general, any custom exception class you create in your own code should inherit from Exception.

The Exception class contains many direct child subclasses that handle most Python errors, so we’ll briefly go over each below:


<!> ArithmeticError – The base class for the variety of arithmetic errors, such as when attempting to divide by zero, or when an arithmetic result would be too large for Python to accurately represent.

<!> AssertionError – This error is raised when a call to the [assert] statement fails.

<!> AttributeError – Python’s syntax includes something called attribute references, which is just the Python way of describing what you might know of as dot notation. In essence, any primary token in Python (like an identifier, literal, and so forth) can be written and followed by a period (.), which is then followed by an identifier. That syntax (i.e. primary.identifier) is called an attribute reference, and anytime the executing script encounters an error in such syntax an AttributeError is raised.

<!> BufferError – Python allows applications to access low level memory streams in the form of a buffer. For example, the bytes class can be used to directly work with bytes of information via a memory buffer. When something goes wrong within such a buffer operation a BufferError is raised.

<!> EOFError – Similar to the Java EOFException article we did a few days ago, Python’s EOFError is raised when using the input() function and reaching the end of a file without any data.

<!> ImportError – Modules are usually loaded in memory for Python scripts to use via the import statement (e.g. import car from vehicles). However, if an import attempt fails an ImportError will often be raised.

<!> LookupError – Like ArithmeticError, the LookupError is generally considered a base class from which other subclasses should inherit. All LookupError subclasses deal with improper calls to a collection are made by using invalid key or index values.

<!> MemoryError – In the event that your Python application is about to run out of memory a MemoryError will be raised. Since Python is smart enough to detect this potential issue slightly before all memory is used up, a MemoryError can be rescued and allow you to recover from the situation by performing garbage collection of some kind.

<!> NameError – Raised when trying to use an identifier with an invalid or unknown name.

<!> OSError – This error is raised when a system-level problem occurs, such as failing to find a local file on disk or running out of disk space entirely. OSError is a parent class to many subclasses explicitly used for certain issues related to operating system failure, so we’ll explore those in future publications.

<!> ReferenceError – Python includes the weakref module, which allows Python code to create a specific type of reference known as a weak reference. A weak reference is a reference that is not “strong” enough to keep the referenced object alive. This means that the next cycle of garbage collection will identify the weakly referenced object as no longer strongly referenced by another object, causing the weakly referenced object to be destroyed to free up resources. If a weak reference proxy created via the weakref.proxy() function is used after the object that is referenced has already been destroyed via garbage collection, a ReferenceError will be raised.

<!> RuntimeError – A RuntimeError is typically used as a catchall for when an error occurs that doesn’t really fit into any other specific error classification.

<!> StopIteration – If no default value is passed to the next() function when iterating over a collection, and that collection has no more iterated value to retrieve, a StopIteration exception is raised. Note that this is not classified as an Error, since it doesn’t mean that an error has occurred.

<!> StopAsyncIteration – As of version 3.5, Python now includes coroutines for asynchronous transactions using the async and await syntax. As part of this feature, collections can be asynchronously iterated using the __anext__() method. The __anext__() method requires that a StopAsyncIteration instance be raised in order to halt async iteration.

<!> SyntaxError – Just like most programming languages, a SyntaxError in Python indicates that there is some improper syntax somewhere in your script file. A SyntaxError can be raised directly from an executing script, or produced via functions like eval() and exec().

<!> SystemError – A generic error that is raised when something goes wrong with the Python interpreter (not to be confused with the OSError, which handles operating system issues).

<!> TypeError – This error is raised when attempting to perform an operation on an incorrect object type.

<!> ValueError – Should be raised when a function or method receives an argument of the correct type, but with an actual value that is invalid for some reason.

<!> Warning – Another parent class to many subclasses, the Warning class is used to alert the user in non-dire situations. There are a number of subclass warnings that we’ll explore in future articles.

<!> GeneratorExit
A generator is a specific type of iterator in Python, which simplifies the process of creating iterators with constantly changing values. By using the yield statement within a generator code block, Python will return or “generate” a new value for each call to next(). When the explicit generator.close() method is called a GeneratorExit instance is raised.

<!> KeyboardInterrupt
This simple exception is raised when the user presses a key combination that causes an interrupt to the executing script. For example, many terminals accept Ctrl+C as an interrupt keystroke.

<!> SystemExit
Finally, the SystemExit exception is raised when calling the sys.exit() method, which explicitly closes down the executing script and exits Python. Since this is an exception, it can be rescued and programmatically responded to immediately before the script actually shuts down.	
'''
