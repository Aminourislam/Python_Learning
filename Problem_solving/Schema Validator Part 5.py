'''Schema Validator Part 5

Given an object (JavaScript) or dictionary (Python), determine if it matches the following schema:

Roles = "user" | "creator" | "moderator" | "staff" | "admin"

{
  username: string,
  posts: number,
  verified: boolean,
  role: Roles,
  supporter?: boolean,
  badges: string[]
}

    The pipe (|) symbol means "or". role must be one of the listed Roles values.
    The question mark (?) after supporter means that the field is optional, but is the specified type if it exists.
    The brackets [] after string means that badges should be an array of strings (or empty).
    Extra keys are allowed

'''

def is_valid_schema(obj):
    Roles = ["user", "creator", "moderator", "staff", "admin"]
    required_keys = ['username', 'posts', 'verified', 'role', 'badges']
    for key in required_keys:
        if key not in obj:
            return False
    
    if not isinstance(obj['username'], str):
        return False 
    # if not isinstance(obj['posts'], int):
    if type(obj['posts']) is not int:
        return False
    if not isinstance(obj['verified'], bool):
        return False
    if not isinstance(obj['role'], str) or obj['role'] not in Roles:
        return False
    if 'supporter' in obj:
        if not isinstance(obj['supporter'], bool):
            return False
    if not isinstance(obj['badges'], list):
        return False
    if not all([isinstance(badge, str) for badge in obj['badges']]):
        return False
    
    
    return True

#Tests:
print(is_valid_schema({"username": "gill", "posts": 12, "verified": False, "role": "creator", "supporter": False, "badges": ["early-adopter", "popular"]})) # True.
print(is_valid_schema({"username": "tonya", "posts": 299, "verified": True, "role": "moderator", "supporter": True, "badges": ["streak-master", "veteran"], "followers": 1233})) # True.
print(is_valid_schema({"username": "zara", "posts": 0, "verified": False, "role": "user", "supporter": False, "badges": []})) # True.
print(is_valid_schema({"username": "nicole", "posts": 65, "verified": True, "role": "admin", "supporter": False, "badges": ["first-post", 18]})) # False.
print(is_valid_schema({"username": "tim", "posts": 25, "verified": True, "role": "staff", "supporter": False})) # False.
print(is_valid_schema({"username": "charlie", "posts": 0, "verified": False, "role": "user", "supporter": "no", "badges": ["first-post", "anniversary"]})) # False.
print(is_valid_schema({"username": "wanda", "posts": 15, "verified": True, "role": "friend", "supporter": True, "badges": ["popular"]})) # False.
print(is_valid_schema({"username": "guy", "posts": 5, "verified": "false", "role": "staff", "supporter": True, "badges": ["helper"]})) # False.
print(is_valid_schema({"username": "carrie", "verified": True, "role": "moderator", "supporter": True, "badges": ["helper", "sharer"]})) # False.
print(is_valid_schema({"username": True, "posts": 75, "verified": True, "role": "creator", "supporter": True, "badges": ["veteran"]})) # False.
