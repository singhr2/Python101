# String2.py

'''
Case matters: SPAM is not the same as spam
'''

print("This is a basic string")

# no space added between strings
print("We learned to join two strings using" + "the plus operation")

# space added between strings
print("We learned to join two strings using", "the comma operation")

first_string = 245
print(type(first_string))

# Copying Data
pennies_saved = 1
pennies_earned = pennies_saved
print(pennies_earned)

'''
In Python, if you’d like a statement to continue to the next line, it is
possible to use the \ marker to indicate this:
'''
x = 1 + 2 + 3 + 4 + \
    5 + 6 + 7 + 8
print('x:', x)
print('type(x) :', type(x))

# Semicolon Can Optionally Terminate a Statement
# generally discouraged by most Python style guides,
str_2 = 'String 2'; str_3 = "3rd string"
print('str_2 :', str_2, ', str_3 :', str_3)

