'''Schema Validator Part 4

Daily Coding Challenge
June 4, 2026

Given an object (JavaScript) or dictionary (Python), determine if it matches the following schema:

Roles = "user" | "creator" | "moderator" | "staff" | "admin"

{
  username: string,
  posts: number,
  verified: boolean,
  role: Roles,
  supporter?: boolean
}

The pipe (|) symbol means "or". role must be one of the listed Roles values.
The question mark (?) after supporter means that the field is optional, but is the specified type if it exists.
Extra keys are allowed
'''
def is_valid_schema(obj):
    Roles = ["user", "creator", "moderator", "staff", "admin"]
    required_keys = ['username', 'posts', 'verified', 'role']
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
    
    
    return True

print(is_valid_schema({"username": "vivian", "posts": 1, "verified": False, "role": "user", "supporter": True})) # True
print(is_valid_schema({"username": "rudolph", "posts": 15, "verified": True, "role": "creator"})) # True
print(is_valid_schema({"username": "hernandez", "posts": 35, "verified": True, "role": "moderator", "supporter": False, "followers": 55})) # True
print(is_valid_schema({"username": "julia", "posts": 50, "verified": True, "role": "admin", "supporter": "true"})) # False
print(is_valid_schema({"username": "bernard", "posts": 0, "verified": True, "role": "friend", "supporter": True})) # False
print(is_valid_schema({"username": "felix", "posts": 40, "verified": "yes", "role": "staff", "supporter": False})) # False
print(is_valid_schema({"username": "jimmy", "posts": True, "verified": False, "role": "creator", "supporter": True})) # False
print(is_valid_schema({"username": True, "posts": 30, "verified": True, "role": "moderator", "supporter": False})) # False