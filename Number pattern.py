def number_pattern(n):
    if not isinstance(n, int):
        return "Argument must be an integer value."
    if n < 1:
        return "Argument must be an integer greater than 0."
    my_str = ""
    for i in range(1, n + 1):
        my_str += f"{i} "
    return my_str.strip()
print(number_pattern(4))
print(number_pattern(12))
