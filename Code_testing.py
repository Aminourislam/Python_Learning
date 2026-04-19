
full_dot = '●'
empty_dot = '○'

def validate_name(name):
    if not isinstance(name, str):
        return 'The character name should be a string'
    if len(name) > 10:
        return 'The character name is too long'
    if " " in name:
        return 'The character name should not contain spaces'


def validate_stats(strength, ntelligence, charisma):
    for stat in (strength, ntelligence, charisma):
        if not isinstance(stat, int):
            return 'All stats should be integers'

    for stat in (strength, ntelligence, charisma):
        if stat < 1:
            return 'All stats should be no less than 1'

    for stat in ( strength, ntelligence, charisma):
        if stat > 4:
            return 'All stats should be no more than 4'
    
    if strength + ntelligence + charisma != 7:
        return 'The character should start with 7 points'

def create_dots(stat):
    return stat * full_dot + empty_dot * (10 - stat)


def create_character(name, strength, ntelligence, charisma):
    name_error = validate_name(name)
    if name_error:
        return name_error

    stats_error = validate_stats(strength, ntelligence, charisma)
    if stats_error:
        return stats_error

    return (
        f'{name}\n'
        f'STR {create_dots(strength)}\n'
        f'INT {create_dots(ntelligence)}\n'
        f'CHA {create_dots(charisma)}'
    )

print(create_character('ren', 4, 2, 1))


def dot_printing(number_of_filled_dot):
    dots = ""
    for i in range(7):
        if i < number_of_filled_dot:
            dot = "●"
        else:
            dot = "○"
        dots += dot
    return dots
def create_character(name, stat_1, stat_2, stat_3):
    if not isinstance(name, str):
        return "The character name should be a string"
    if name == "":
        return "The character should have a name"
    if len(name) > 10:
        return "The character name is too long"
    if " " in name:
        return "The character name should not contain spaces"
    if not all(isinstance(stat, int) for stat in [stat_1, stat_2, stat_3]):
        return "All stats should be integers"
    if (stat_1 < 1) or (stat_2 < 1) or (stat_3 < 1):
        return "All stats should be no less than 1"
    if (stat_1 > 4) or (stat_2 > 4) or (stat_3 > 4):
        return "All stats should be no more than 4"
    if sum([stat_1,stat_2,stat_3]) != 7:
        return "The character should start with 7 points"
    stat_1_dots = dot_printing(stat_1)
    stat_2_dots = dot_printing(stat_2)
    stat_3_dots = dot_printing(stat_3)

    return  (
        f"{name}\n"
        f"STR {stat_1_dots}\n"
        f"INT {stat_2_dots}"
        f"\nCHA {stat_3_dots}"
        )

print(create_character('ren', 4, 2, 1))