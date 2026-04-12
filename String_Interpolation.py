#In Python, we can combine multiple strings together with the plus (+) operator. 
#This process is called string concatenation.
my_str_1 = 'Hello'
my_str_2 = "World"

str_plus_str = my_str_1 + ' ' + my_str_2
print(str_plus_str) # Hello World

# If we want to use different data ty
name = 'John Doe'
age = 26
#name_and_age = name + age
#print(name_and_age) # TypeError: can only concatenate str (not "int") to str

# str represtation:
name = 'John Doe'
age = 26

name_and_age = name + str(age)
print(name_and_age) # John Doe26


name_and_age = name  # Start with the name
name_and_age += str(age)  # Append the age as string

print(name_and_age)  # John Doe26

#The process of inserting variables and expressions into a string is called string interpolation.
#Python has a category of string called f-strings (short for formatted string literals), which allows us to handle interpolation with a compact and readable syntax.

name = 'John Doe'
age = 26
name_and_age = f'My name is {name} and I am {age} years old'
print(name_and_age) # My name is John Doe and I am 26 years old

num1 = 5
num2 = 10
print(f'The sum of {num1} and {num2} is {num1 + num2}') # The sum of 5 and 10 is 15

#Note how you don't need to convert non-string types with the str() function. In the example above, the value of the age, num1, and num2 variables is converted under the hood into a string during the interpolation process.

