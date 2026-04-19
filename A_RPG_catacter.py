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