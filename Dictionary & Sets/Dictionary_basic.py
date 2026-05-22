#Dictionary Basic

Dictionary = {
	'Name' : 'Amin',
	'Roll' : 106,
	'Class' : 7,
	'Section' : 'A'
}

# Adding new key and its value.
Dictionary['Address'] = 'India'
print(Dictionary)
# Updating value in a existing key
Dictionary.update({'Address' : 'Bangladesh'}) # dictionary.update({'key' : 'value'})
# Printing a value of a key.
print(Dictionary['Name']) # dictionary['key']
# print(Dictionary['Amin']) # Error

Dictionary2 = dict([('Name', 'Akash'), ('Roll', 2), ('Class', 7), ('Section', 'A')])
print(Dictionary)
print(Dictionary2)

########### Common Dictionary Methods

#     get() Methods			#
# dictionary.get(key, default)
print(Dictionary.get('Roll', 'default'))
print(Dictionary.get('Rol', 'Missing key'))

#		keys() Methods		#
# dictionary.keys()
print(Dictionary.keys()) # give all key of that dictionary

#		values() Methods		#
# dictionary.values()
print(Dictionary2.values())  #Give all Value of a dictionary had.

#		items() Methods		#
# dictionary.items()
print(Dictionary.items()) #It give Key-Value pairs 

#		clear() Methods		#
# dictionary.clear()
Dictionary2.clear() # Deleting all Key-value once.
print("Here printing Dictionary2 after exicuting clear() method. ",Dictionary2)

#		pop() Methods		#
# dictionary.pop('key')
dic3 = {'About':'You', "Address": "India"}
dic3.pop('Address') # Delete specified keys' value.
print(dic3)

#		popitem() Methods		#
# dictionary.popitem()
dic3['Address'] = 'Bangladesh'
print(dic3)
dic3.popitem() # NO argument need. it remove last inserted key-value
print(dic3)

# looping over a Dictionary
for key in Dictionary.keys(): # for keys
	print(key)
for value in Dictionary.values(): # for values
	print(value)
for key, values in Dictionary.items(): # for key-value both
	print(f"{key} : {values}")


# enumerate() Function
# It give Index of a element and that element
for index, key in  enumerate(Dictionary.keys(),1): # enumerate(argument, starting_index)
	print(f"{index}. {key}")
print('\n')
for index, value in enumerate(Dictionary.values()):
	print(f"{index}. {value}")
for index, key_value, in enumerate(Dictionary.items()):
	print(f"{index}. {x for x in key_value}")