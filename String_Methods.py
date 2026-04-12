my_str ="Hi, How are you"

# Uppercase my string.
uppercase_my_str = my_str.upper()
print(uppercase_my_str) #HI, HOW ARE YOU

# Lowercase my string.
lowercase_my_str = my_str.lower()
print(lowercase_my_str) #hi, how are you

#leading and trailing characters removing,
#If no argument is passed it removes leading and trailing whitespace
my_str_1 = "     Hi,    How are you          .            "
trimmed_my_str = my_str.strip()
print(trimmed_my_str)

# Replacing 
replaced_my_str = my_str.replace('Hi' , 'Hello')
print(replaced_my_str)

# Splits a string on a specified separator into a list of strings.
# string ---> List of word
split_words = my_str.split()
print(split_words)

# Joining string from List:
my_list = ['Hi,', 'How', 'are', 'you.']
join_my_str = ' '.join(my_list)
print(join_my_str)

# startswith(prefix): Returns a boolean indicating if a string starts with the specified prefix
print(my_str.startswith("Hi"))
print(my_str.startswith("Hello"))

#endswith(suffix): Returns a boolean indicating if a string ends with the specified suffix.
print(my_str.endswith('you'))
print(my_str.endswith('world'))


# find(substring): Returns the index of the first occurrence of substring, or -1 if it doesn't find one.
word_index_find = my_str.find('are')
print(word_index_find)
word_index_find = my_str.find('hello')
print(word_index_find)# -1 because not found

# count(substring): Returns the number of times a substring appears in a string.
# Hi, How are you.
counting_a_letter = my_str.count('o')
print(counting_a_letter)
counting_a_letter = my_str.count('h')
print(counting_a_letter)

# capitalize(): Returns a new string with the first character capitalized and the other characters lowercased.
my_str_2 = 'hi, how are you!'
capitalize_str = my_str_2.capitalize()
print(capitalize_str)

# isupper(): Returns True if all letters in the string are uppercase and False if not.
is_all_upper = my_str.isupper()
print(is_all_upper)

# islower()
is_all_lower = my_str_2.islower()
print(is_all_lower)

#title(): Returns a new string with the first letter of each word capitalized.
title_for_str = my_str_2.title()
print(title_for_str)
