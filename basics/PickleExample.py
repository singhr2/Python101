#PickleExample.py
'''
pickle module implements a fundamental, but powerful algorithm for serializing and de-serializing a Python object structure.
“Pickling” is the process whereby a Python object hierarchy is converted into a byte stream, and
“unpickling” is the inverse operation, whereby a byte stream is converted back into an object hierarchy.
Pickling (and unpickling) is alternatively known as “serialization”, “marshalling,” or “flattening”,
however, to avoid confusion, the terms used here are “pickling” and “unpickling”..

Python has a more primitive serialization module called marshal,
but in general pickle should always be the preferred way to serialize Python objects.
'''
import pickle

# Save a dictionary into a pickle file.
dict_color = { "lion": "yellow", "kitty": "red" }
pickle.dump( dict_color, open( "save.pkl", "wb" ) )

# Load the dictionary back from the pickle file.
dict_color_loaded = pickle.load( open( "save.pkl", "rb" ) )
    # => favorite_color is now { "lion": "yellow", "kitty": "red" }
print('dict_color_loaded :', dict_color_loaded)
