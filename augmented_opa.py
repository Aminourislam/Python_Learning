#   augmented assignment
### variable <operator>= value


my_var = 10
my_var += 5
print(my_var) # 15

count = 14
count -= 3
print(count) # 11

product = 65
product *=5
print(product) #325

div = 100
div /= 5
print(div)

#The floor division operator (//=) floor‑divides the left variable by the right and stores the result back in the left variable:
total_pages = 23
total_pages //= 5
print(total_pages) # 4

#The modulo assignment operator (%=) computes the remainder of the left variable divided by the right and stores it back in the left variable:
bits = 35
bits %= 2
print(bits) # 1

# The power opperator;
power = 2
power **= 3
print(power) # 8


#some augmented assignment operators with strings
greet = 'Hello'
greet += ' World'
print(greet) # Hello World
greet *=3
print(greet)

#greet -= 'World'
#print(greet) 
# TypeError: unsupported operand type(s) for -=: 'str' and 'str'
#greet /= 'World'
#print(greet) # TypeError: unsupported operand type(s) for /=: 'str' and 'str'


#x++, you can simply write x += 1, which makes it obvious that you're incrementing the value of x by 1.
#Writing ++x in Python just applies the unary plus twice, and does not increment anything:
my_var = 5

print(+my_var)   # 5
print(++my_var)  # 5
print(+++my_var) # 5

my_var += 1

print(my_var) # 6