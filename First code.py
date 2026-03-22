def adding(num1, num2):
    sum = num1 + num2
    return sum
print("Enter two number for sum: ")
a = float(input("a = "))
b = float(input("b = "))
summition = adding(a,b)
print("sum of", a,"and", b, "is:", round(summition,2))
