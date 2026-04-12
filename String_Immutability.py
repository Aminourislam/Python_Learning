my_str_1 = 'Hello'
my_str_2 = "World"

#If you need a multi-line string:
my_str_3 = """Multiline string"""
my_str_4 = '''Another multiline string'''

#Use the opposite kind of quotes. That is, if your string contains single quotes, use double quotes to wrap the string, and vice versa:
#Example Code

msg = "It\'s a sunny day"
quote = 'She said, "Hello World!"'
msg = 'It\'s a sunny day'
quote = "She said, \"Hello!\""

# need to check if a string contains one or more characters.
my_str = 'Hello world'

print('Hello' in my_str)  # True
print('hey' in my_str)    # False
print('hi' in my_str)    # False
print('e' in my_str)  # True
print('f' in my_str)  # False

#str lenth check:

my_str = 'Hello world'
print(len(my_str))  # 11

#checking latter with indexing:

my_str = "Hello world"

print(my_str[0])  # H
print(my_str[6])  # w

#Negative indexing:

print(my_str[-1])  # d
print(my_str[-2]) # l

# strings are modifyable:

greeting = 'hi'
greeting = 'hello'
print(greeting) # hello

#But direct modification of a string isn't allowed:

greeting = 'hi'
greeting[0] = 'H' # TypeError: 'str' object does not support item assignment