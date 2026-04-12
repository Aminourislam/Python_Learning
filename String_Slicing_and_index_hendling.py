my_str = "Hello world"

print(my_str[0])  # H
print(my_str[6])  # w
print(my_str[-1]) # d

#string[start:stop]
print(my_str[1:4]) # ell
print(my_str[2:8]) #llo wo
#the stop index is non-inclusive, so [1:4] just extracted the characters from index 1, and up to, but not including, the character at index 4.

#we can start without starting or ending inedex
print(my_str[:7])  # Hello w
print(my_str[8:])  # rld

#slicing a string does not modify the original string:
my_str = 'Hello world'
print(my_str[8:])  # rld
print(my_str)  # Hello world

#i can canomit both the start and stop indices, which will extract the whole string:
print(my_str[:])  # Hello world

# where to start: where will end: increment/decrement
#string[start:stop:step]
print(my_str[0:11:2])  # Hlowrd

#A trick for reverse a string by setting step to -1, and leaving start and stop blank:
print(my_str[::-1]) # dlrow olleH

