# Example 1:
dictionary = {
              "cat": "chat",
              "dog": "chien",
              "horse": "cheval"
}
# Example 2:
#   Modifing
phone_numbers = {'boss': 5551234567,
              'Suzy': 22657854310
}

dictionary["cat"]= "minou"
print(dictionary)

#  sorted
#for key in sorted(dictionary.keys())
#print(dictionary)

##   same as key method we had a method values
for french in dictionary.values():
    print(french)

###   adding a new key and value:
phone_numbers["swan"] = 225478756
print(phone_numbers)
