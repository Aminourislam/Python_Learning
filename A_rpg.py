def dot_printing(number_of_filled_dot):
    dots = ""
    for i in range(10):
        if i < number_of_filled_dot:
            dot = "●"
        else:
            dot = "○"
        dots += dot
    return dots

def create_character(name, stat1, stat2, stat3):
    # Validate name
    if not isinstance(name, str):
        return "The character name should be a string."
    if name == "":
        return "The character should have a name."
    if len(name) > 10:
        return "The character name is too long."
    if " " in name:
        return "The character name should not contain spaces."
    
    # Validate stats are integers
    if not all(isinstance(stat, int) for stat in [stat1, stat2, stat3]):
        return "All stats should be integers."
    
    # Validate stats range
    if not all(1 <= stat <= 4 for stat in [stat1, stat2, stat3]):
        if any(stat < 1 for stat in [stat1, stat2, stat3]):
            return "All stats should be no less than 1."
        if any(stat > 4 for stat in [stat1, stat2, stat3]):
            return "All stats should be no more than 4."
    
    # Validate sum
    if sum([stat1, stat2, stat3]) != 7:
        return "The character should start with 7 points."
    
    # Prepare output
    stat_abbrs = ["STR", "INT", "CHA"]
    stats = [stat1, stat2, stat3]
    lines = [name]
    for abbr, stat in zip(stat_abbrs, stats):
        dots = dot_printing(stat)
        line = f"{abbr} {dots}"
        lines.append(line)
    return "\n".join(lines)

# Example usage
x = create_character('ren', 4, 2, 1)
print(x)