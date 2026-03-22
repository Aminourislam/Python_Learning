def check_tringle(a,b,c):
    if a+b<=c:
        return 0;
    elif b+c<=a:
        return 0;
    elif c+a<=b:
        return 0;
    else:
        return 1
print("Enter three sides lenth to check we can make a tringle or not:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

value = check_tringle(a,b,c)
if value == a:
    ans = "Yes"
else:
    ans = "\'NO\'"
    
print("Is we can make tringle:" + ans)
    
