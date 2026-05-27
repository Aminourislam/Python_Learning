import math

def get_pizzas_to_order(hours_worked):
    slice_counts = []
    for hrs in hours_worked:
        slices = math.ceil(hrs / 3)
        if slices < 2:
            slices = 2
        slice_counts.append(slices)
    
    total_slices = sum(slice_counts)
    pizzas = math.ceil(total_slices / 8)
    print(pizzas)
    return pizzas

    
get_pizzas_to_order([8,8,8,8]) #2
get_pizzas_to_order([10, 9, 8, 2, 2, 6, 10]) #3
get_pizzas_to_order([1, 2, 3, 4, 5]) #2
get_pizzas_to_order([8, 8, 8, 8, 8, 8, 8, 8]) #3
get_pizzas_to_order([9, 9, 6]) #1
get_pizzas_to_order([10, 12, 16, 9, 8, 11, 15, 8, 0]) #5