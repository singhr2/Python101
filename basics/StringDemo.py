# StringDemo.py

#http://thepythonguru.com/python-strings/

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


#String functions : https://docs.python.org/3/library/stdtypes.html
print('cApitalizE'.capitalize())  # Capitalize




# String Concatanation
#Using + to Combine Strings
print("John" + "Everyman")
# or just separate every string with a comma (,)
print("John" "Everyman")

# with space
print("John" + " " + "Everyman")
# is equivalent to
# Use comma to add space
print("John" , "Everyman")

# Use %s (format specifier)
print("John %s%s" % ("Every" , "Man"))

'''in your last format specifier, you added a 10, 
so it is expecting a string with ten characters. 
When it does not find ten (it only finds three ... M-a-n) it pads space in between with seven spaces.
'''
print("%s %s %10s" % ("John" , "Every", "Man"))
print("%-5s %s %10s" % ("John" , "Every", "Man"))
str1="Hello"
str2="Hello"
str3=str1+""
str4="World"
str5=str1;
str6=str1+" "

print('str1 id:' , id(str1));
print('str2 id:' , id(str2));
print('str3 id:' , id(str3));
print('str4 id:' , id(str4));
print('str5 id:' , id(str5));
print('str6 id:' , id(str6));

print("str1==str2", str1==str2)
print("str1==str5", str1==str5)
print("str1==str3", str1==str3)
print("str4==str3", str4==str3)

