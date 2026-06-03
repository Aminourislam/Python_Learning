# Schema Validator Part 3
# Roles = "user", "creator", "moderator", "staff", "admin"

# {
#   username: string,
#   posts: number,
#   verified: boolean,
#   role: Roles
# }

#     The pipe (|) symbol means "or". role must be one of the listed Roles values.
#     Extra keys are allowed

def each_input_validation(dic):
        if isinstance(dic['username'], str):
            a = True
        else:
            a = False
        if isinstance(dic['posts'], int):
            b = True
        else:
            b = False
        if isinstance(dic['verified'], bool):
            c = True
        else:
            c = False
        if all([a, b, c]):
            return True
        else:
            return False
def is_valid_schema(obj):
    dic = obj
    list_keys = [key for key in dic.keys()]
    if ('username' in list_keys) and ('posts' in list_keys) and ('verified' in list_keys) and ('role' in list_keys):
        Roles = ("user", "creator", "moderator", "staff", "admin")
        if dic['role'] in Roles:
            return each_input_validation(dic)
        else:
            return False
    else:
        return False


print(is_valid_schema({"username": "henry", "posts": 0, "verified": True, "role": "staff"})) # True.
print(is_valid_schema({"username": "sara", "posts": 45, "verified": False, "role": "creator", "followers": 70})) # True.
print(is_valid_schema({"username": "penelope", "posts": 20, "verified": True, "role": "admin"})) # True.
print(is_valid_schema({"username": "kevin", "posts": 0, "verified": False, "role": "user"})) # True.
print(is_valid_schema({"username": "george", "posts": 15, "verified": True, "role": "moderator"})) # True.
print(is_valid_schema({"username": "david", "posts": 0, "verified": False, "role": "guest"})) # False.
print(is_valid_schema({"username": "wendy", "posts": 10, "verified": True})) # False.
print(is_valid_schema({"username": "fabian", "posts": 1, "verified": True, "role": True})) # False.
print(is_valid_schema({"username": 8, "posts": 1, "verified": True, "role": "user"})) # False.
print(is_valid_schema({"username": "penny", "posts": "10", "verified": True, "role": "staff"})) # False.
print(is_valid_schema({"username": "john", "posts": "1", "verified": "true", "role": "admin"})) # False.