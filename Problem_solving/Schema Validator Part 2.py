def is_valid_schema(obj):
    dic = obj
    list_keys = [key for key in dic.keys()]
    if ('username' in list_keys) and ('posts' in list_keys) and ('verified' in list_keys):
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
    else:
        return False

print(is_valid_schema({"username": "alice", "posts": 10, "verified": False}))
print(is_valid_schema({"username": "carol", "posts": 15, "verified": True, "followers": 25}))
print(is_valid_schema({"username": "frank", "posts": "21", "verified": True}))
print(is_valid_schema({"username": "sam", "posts": 17, "verified": "false"}))
print(is_valid_schema({"username": "bill", "verified": True}))
print(is_valid_schema({"username": "fred", "verified": True}))
print(is_valid_schema({"username": 5, "posts": 10, "verified": True}))