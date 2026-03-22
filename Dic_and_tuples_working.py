# school_class = {}

# while True:
#     name = input("Enter the student's name: ")
#     if name == '':
#         break
    
#     score = int(input("Enter the student's score (0-10): "))
#     if score not in range(0, 11):
# 	    break
    
#     if name in school_class:
#         school_class[name] += (score,)
#     else:
#         school_class[name] = (score,)
        
# for name in sorted(school_class.keys()):
#     adding = 0
#     counter = 0
#     for score in school_class[name]:
#         adding += score
#         counter += 1
#     print(name, ":", adding / counter)


# 2/
# tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
# duplicates = tup.count(2)
# print(duplicates)    # outputs: 4

#3/
# d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
# d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
# d3 = {}

# for item in (d1, d2):
#     d3.update(item)
# print(d3)

# #4/
# my_list = ["car", "Ford", "flower", "Tulip"]

# t = tuple(my_list)
# print(type(t))

# 5/ Tuples to dictionary:
# colors = (("green", "#008000"), ("blue", "#0000FF"))

# colors_dictionary = dict(colors)

# print(colors_dictionary)













