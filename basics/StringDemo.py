# StringDemo.py

# http://thepythonguru.com/python-strings/

one_char = 'a'
print(type(one_char))

one_str = "this is a string"
print(type(one_str))

print("I said, \"Don't "
      "do "
      "it\"")

print(""" This
is 
it""")

print("Roses are red \n Violets are blue ")


# encode([encoding=”utf-8”][, errors=”strict”])
#   errors : 'strict, 'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace'
print('This is £ pound sign')  # This is £ pound sign
encoded_value = 'This is £ pound sign'.encode() # b'This is \xc2\xa3 pound sign'
print('encoded_value :', encoded_value)
encoded_as_latin1 = 'This is £ pound sign'.encode('iso-8859-1')
print('encoded_as_latin1 :', encoded_as_latin1)  # b'This is \xa3 pound sign'

# bytes.decode(encoding=”utf-8”, errors=”strict”)¶
print('decoded from UTF-8 :', encoded_value.decode())  # This is £ pound sign
print('decoded from latin1 :', encoded_as_latin1.decode('latin-1' ))  # This is £ pound sign

print(encoded_value.hex())      # 5468697320697320c2a320706f756e64207369676e
print(encoded_as_latin1.hex())  # 5468697320697320a320706f756e64207369676e

# String functions : https://docs.python.org/3/library/stdtypes.html
print('cApitalizE'.capitalize())  # Capitalize

# str.strip([chars])
# Return a copy of the string with the leading and trailing characters removed.
#   chars : If omitted or None, the chars argument defaults to removing whitespace.
print('[', '   spacious   '.strip(), ']')  #

# lstrip([chars])
print('[', '   spacious   '.lstrip(), ']')  # [ spacious    ]
print('[', 'www.example.com'.lstrip('cmowz.'), ']')  # [ example.com ]

# rstrip([chars])
#   chars : If omitted or None, the chars argument defaults to removing whitespace.
print('[', '   spacious   '.rstrip(), ']')  # [    spacious ]
print('[', 'mississippi'.rstrip('ipz'), ']')  # [ mississ ]

# zfill(width)
# Return a copy of the string left filled with ASCII '0' digits to make a string of length width.
# The original string is returned if width is less than or equal to len(s).
print("42".zfill(5))  # '00042'
print("-42".zfill(5))  # '-0042'

# in operator
# To check if sub is a substring or not, use the in operator
print('Py' in 'Python')  # True
print('py' in 'Python')  # False
print('Rx' in 'Python')  # False

# find()
# Return the lowest index i (starts from 0) or -1 if sub is not found.
# The find() method should be used only if you need to know the position of sub.
# str.find(sub[, start[, end]])
print('Ranbir Singh'.find('an'))  # 1
print('Ranbir Singh'.find('Rx'))  # -1

# index(sub[, start[, end]])
# Like find(), but raise ValueError when the substring is not found.

# replace()
print('Just Do It'.replace(' ', '!'))  # Just!Do!It

# count()
# str.count(sub[, start[, end]])
print('Ranbir'.count('an'))  # 1
print('Ranbir'.count('rx'))  # 0

# startswith(prefix[, start[, end]])
# Return True if string starts with the prefix, otherwise return False.
#   prefix can also be a tuple of prefixes to look for.
#   With optional start, test string beginning at that position.
#   With optional end, stop comparing string at that position.
print('Ranbir'.endswith('ir'))  #

# endswith()
print('Ranbir'.endswith('ir'))  # True
print('Ranbir'.endswith('iR'))  # False


# str.split(sep=None[, maxsplit=-1])
# str.split(str="", num = string.count(str))
#     str − This is any delimeter, by default it is space.
#     num − this is number of lines to be made
str = "this is string example....wow!!!"
print(str.split())  # ['this', 'is', 'string', 'example....wow!!!']
print(str.split('i', 1))  # ['th', 's is string example....wow!!!']
print(str.split('w'))  # ['this is string example....', 'o', '!!!']

# String Concatanation
# Using + to Combine Strings
print("John" + "Everyman")  #
# or just separate every string with a comma (,)
print("John" "Everyman")  #

# with space
print("John" + " " + "Everyman")  #
# is equivalent to
# Use comma to add space
print("John", "Everyman")  #

# Use %s (format specifier)
print("John %s%s" % ("Every", "Man"))

'''in your last format specifier, you added a 10, 
so it is expecting a string with ten characters. 
When it does not find ten (it only finds three ... M-a-n) it pads space in between with seven spaces.
'''
print("%s %s %10s" % ("John", "Every", "Man"))
print("%-5s %s %10s" % ("John", "Every", "Man"))
str1 = "Hello"
str2 = "Hello"
str3 = str1 + ""
str4 = "World"
str5 = str1
str6 = str1 + " "

print('str1 id:', id(str1))
print('str2 id:', id(str2))
print('str3 id:', id(str3))
print('str4 id:', id(str4))
print('str5 id:', id(str5))
print('str6 id:', id(str6))

print("str1==str2", str1 == str2)
print("str1==str5", str1 == str5)
print("str1==str3", str1 == str3)
print("str4==str3", str4 == str3)
