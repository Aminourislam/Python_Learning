#Mixing positional and keyword arguments
def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)
print("a = ", end="")
a = int(input())
print("b = ", end="")
b = int(input())
print("c = ", end="")
c = int(input())
adding(a,b,c);
adding(c = 1, a = 2, b = 3)

# Mixxxxing
adding(3, c = 1, b = 2)
#### TypeError: adding() got multiple values for argument 'a'
#    adding(3, a = 1, b = 2)

###   more details for parametered function
def introduction(first_name, last_name="Smith"):
     print("Hello, my name is", first_name, last_name)
introduction("kalvin")
introduction("James", "Doe") # it show output poperly with out error;

def intro(first_name="John", last_name="Smith"):
    print("Hello, my name is", first_name, last_name)
intro()
intro("Amin", "Islam")

def subtra(a, b):
    print(a - b)
#It's important to remember that positional
#arguments mustn't follow keyword arguments.
#That's why if you try to run the following snippet:
subtra(5, b=2)    # outputs: 3
#subtra(a=5, 2)    # Syntax Error
