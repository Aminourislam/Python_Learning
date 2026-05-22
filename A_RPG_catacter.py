def dot_printing(number_of_filled_dot):
    dots = ""
    for i in range(7):
        if i < number_of_filled_dot:
            dot = "●"
        else:
            dot = "○"
        dots += dot
    return dots


def create_character(name, seat_1, seat_2, seat_3):
    if name == "":
        x = "The character should have a name"
        return x
    elif not isinstance(name, str):
        x = "The character name should be a string."
        return x
    elif len(name) > 10:
        x = "The character name is too long"
        return x
    elif " " in name:
        x = "The character name should not contain spaces."
        return x
    elif isinstance(( seat_1, seat_2, seat_3), int):
        x = "All stats should be integers"
        return x
    elif (seat_1 and seat_2 and seat_3) <  1:
        x = " All stats should be no less than 1"
        return x
    elif (seat_1 and seat_2 and seat_3) >  4:
        x = "All stats should be no more than 4"
        return x
    elif (seat_1 + seat_2 + seat_3) > 7:
        x = "The character should start with 7 points"
        return x
    seat_1_dots = dot_printing(seat_1)
    seat_2_dots = dot_printing(seat_2)
    seat_3_dots = dot_printing(seat_3)

    x = f"{name} \nSTR {seat_1_dots} \nINT {seat_2_dots} \nCHA {seat_3_dots}"
    return x
x = create_character('ren', 4, 2, 1)
print(x)
x = create_character('ren', 0, 2, 1)
print(x)
x = create_character('ruman', 8, 2, 1)
print(x)



# full_dot = '●'
# empty_dot = '○'

# def validate_name(name):
#     if not isinstance(name, str):
#         return 'The character name should be a string'
#     if len(name) > 10:
#         return 'The character name is too long'
#     if " " in name:
#         return 'The character name should not contain spaces'


# def validate_stats(strength, ntelligence, charisma):
#     for stat in (strength, ntelligence, charisma):
#         if not isinstance(stat, int):
#             return 'All stats should be integers'

#     for stat in (strength, ntelligence, charisma):
#         if stat < 1:
#             return 'All stats should be no less than 1'

#     for stat in ( strength, ntelligence, charisma):
#         if stat > 4:
#             return 'All stats should be no more than 4'
    
#     if strength + ntelligence + charisma != 7:
#         return 'The character should start with 7 points'

# def create_dots(stat):
#     return stat * full_dot + empty_dot * (10 - stat)


# def create_character(name, strength, ntelligence, charisma):
#     name_error = validate_name(name)
#     if name_error:
#         return name_error

#     stats_error = validate_stats(strength, ntelligence, charisma)
#     if stats_error:
#         return stats_error

#     return (
#         f'{name}\n'
#         f'STR {create_dots(strength)}\n'
#         f'INT {create_dots(ntelligence)}\n'
#         f'CHA {create_dots(charisma)}'
#     )
#     