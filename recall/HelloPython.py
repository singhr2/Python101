# Run online at https://repl.it/repls/DisloyalKindheartedEvents
# Covers : print some text, get the type of some variable, custom function- define and invoke, get user input

#show current date (as well as only year part)
import datetime
today = datetime.date.today()
print (today)
print(today.year) # print only year

# This is a comment
print("Hello, Python!")
print(type(4)); # <class 'int'>
print(type('4')); # <class 'str'>

def performExchange(inr_to_exchange):
  gbp_to_inr_rate = 95.67;
  return inr_to_exchange * gbp_to_inr_rate;

#get input from user
amount = input('How many Pounds to be exchanged :')
# convert str to float
result = performExchange(float(amount))
print(type(result))  # <class 'float'>
print('result :' , result)

