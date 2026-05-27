'''Vowel Balance

Given a string, determine whether the number of vowels in the first half of the string is equal
to the number of vowels in the second half.

    The string can contain any characters.
    The letters a, e, i, o, and u, in either uppercase or lowercase, are considered vowels.
    If there's an odd number of characters in the string, ignore the center character.

Waiting: 1. is_balanced("racecar") should return True.
Waiting: 2. is_balanced("Lorem Ipsum") should return True.
Waiting: 3. is_balanced("Kitty Ipsum") should return False.
Waiting: 4. is_balanced("string") should return False.
Waiting: 5. is_balanced(" ") should return True.
Waiting: 6. is_balanced("abcdefghijklmnopqrstuvwxyz") should return False.
Waiting: 7. is_balanced("123A#b!E&*456-o.U") should return True.
'''
def check_logic(num_v_front, num_v_back):
    if (num_v_front == 0) and (num_v_back == 0):
        return False
    if num_v_front == num_v_back:
        return True
    else:
        return False

def is_balanced(str):
    str_len = len(str)
    mid_len = str_len // 2
    mi = - mid_len
    vowels = "aeiou"
    num_v_front = 0
    num_v_back = 0
    str_list = list(str.lower())
    for i in range(mid_len):
        if str_list[i] in vowels:
            num_v_front += 1
    for i in range(mi,0):
        if str_list[i] in vowels:
            num_v_back += 1
    print(num_v_front)
    print(num_v_back)
    return check_logic(num_v_front,num_v_back)

print(is_balanced("racecar")) #True
print(is_balanced("Lorem Ipsum"))
print(is_balanced("Kitty Ipsum"))
