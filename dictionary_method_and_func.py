# Example 1:
dictionary = {
              "cat": "chat",
              "dog": "chien",
              "horse": "cheval"
}
# Example 2:
phone_numbers = {'boss': 5551234567,
              'Suzy': 22657854310
}
# keys() method example:
for key in dictionary.keys():
    print(key, "->", dictionary[key])


# item() method example:
for english, french in dictionary.items():
    print(english, "->", french)
