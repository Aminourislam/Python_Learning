class Student: #class declaration
    name = "akash" 
    # class lavel variable which can access all obj
    
    def __init__(self, name, roll, grade): # initializar or spacial method method 1, there more like this __gt__() for >. and more are in internet
        self.name = name
        #attribute = variable 
        self.roll = roll
        self.grade = grade
s1 = Student("Ruman", 55, 12)
# changing attribute name
print(s1.name)
s1.name = "Khalek"
print(s1)


# s2 = Student() # Error for no arguments
# print(s2.name)
'''
**********object variable accessing with py build in fun

1. getattr(obj, attribute_name, defult_value)
2. setattr()
3. hasattr()
4. delattr()
'''
print(getattr(s1, "name", "No name found"))