def message():
    print("Enter a number: ", end="");

print("Start form here:");
message();
a = int(input());
message();
b = int(input());
message();
c = int(input());
add = a+b+c
print("addition:", add);
print("end");

#one parameter function
def message(number):
    print("Enter a number:", number)

number = 1234
message(1)
print(number)
#Two parameter function
def message(what, number):
    print("Enter", what, "number", number)
message(1,2);
message("telephone", 11)
message("price", 5)
message("enter", "number")
