'''
Schema Validator Part 6

Daily Coding Challenge
June 6, 2026

Given an object (JavaScript) or dictionary (Python), determine if it matches the following schema:

Roles = "user" | "creator" | "moderator" | "staff" | "admin"

UserProfile = {
  username: string,
  posts: number,
  verified: boolean,
  role: Roles,
  supporter?: boolean,
  badges: string[]
}

{
  users: UserProfile[]
}

    The pipe (|) symbol means "or". role must be one of the listed Roles values.
    The question mark (?) after supporter means that the field is optional, but is the specified type if it exists.
    UserProfile[] denotes an array of UserProfile objects. An empty array is valid.
    Extra keys are allowed
'''

def is_valid_schema(obj):
    # Step 1: Check that 'users' exists and is a list
    if not isinstance(obj.get('users'), list):
        return False
    
    users_list = obj['users']
    
    # Step 2: Empty list is always valid
    if not users_list:
        return True
    
    Roles = {"user", "creator", "moderator", "staff", "admin"}
    
    # Step 3: Validate each user in the list
    for user in users_list:
        # Required keys
        if not all(key in user for key in ['username', 'posts', 'verified', 'role', 'badges']):
            return False
        
        # Type checks
        if not isinstance(user['username'], str):
            return False
        if not isinstance(user['posts'], int):
            return False
        if not isinstance(user['verified'], bool):
            return False
        if not isinstance(user['role'], str) or user['role'] not in Roles:
            return False
        if 'supporter' in user and not isinstance(user['supporter'], bool):
            return False
        if not isinstance(user['badges'], list):
            return False
        if not all(isinstance(badge, str) for badge in user['badges']):
            return False
    
    return True


'''
Tests:
'''
print(is_valid_schema({"users": [{"username": "ron", "posts": 14, "verified": True, "role": "creator", "badges": ["early-adopter"]}, {"username": "cher", "posts": 25, "verified": True, "role": "moderator", "supporter": True, "followers": 20, "badges": ["helper"]}]})) # True.
print(is_valid_schema({"users": []})) # True.
print(is_valid_schema({"users": {"username": "anne", "posts": 0, "verified": False, "role": "user", "supporter": False, "badges": []}})) # False.
print(is_valid_schema({"users": [{"username": "tony", "posts": 10, "verified": True, "role": "creator", "supporter": True, "badges": ["liked", 6]}]})) # False.
print(is_valid_schema({"users": [{"username": "ursula", "posts": 3, "verified": False, "role": "user", "supporter": "false", "badges": ["comeback"]}]})) # False.
print(is_valid_schema({"users": [{"username": "benny", "posts": 55, "verified": True, "role": "superstar", "supporter": True, "badges": ["veteran"]}]})) # False.
print(is_valid_schema({"users": [{"username": "chase", "posts": 1, "verified": "yes", "role": "staff", "supporter": False, "badges": ["superstar"]}]})) # False.
print(is_valid_schema({"users": [{"username": "carla", "posts": "10", "verified": False, "role": "user", "supporter": False, "badges": ["newbie"]}]})) # False.
print(is_valid_schema({"users": [{"posts": 4, "verified": False, "role": "admin", "supporter": False, "badges": ["superuser", "veteran"]}]})) # False.
print(is_valid_schema({"users": [{"username": "harold", "posts": 80, "verified": True, "role": "creator", "supporter": True, "badges": ["liked", "hero"]}, {"username": "kim", "posts": 11, "verified": False, "role": "admin", "supporter": True, "badges": ["first"]}, {}]})) # False.
