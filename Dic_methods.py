# Dic = {"Ami":"me","oi":"Hey","tui":"You"}
# for key in Dic.keys():
#     print(key, "->",Dic[key])

# dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

# for item in dictionary.items():
#     print(item)
# for i in dictionary.values():
#     print(i)

# dictionary["Hand"]="Hat"
# print(dictionary)
# dictionary["Hand"]="Hand"
# print(dictionary)

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
print(dictionary)
dictionary.update({"duck": "canard"})
print(dictionary)

del dictionary["duck"]
print(dictionary)
# For deleting last item :
dictionary.popitem()
print(dictionary
)
