def apply_discount(price, discount):
    if not isinstance(price, (int, float)):
        return "The price should be a number."
    if not isinstance(discount, (int, float)):
        return "The discount should be a number."
    if price <= 0:
        return "The price should be greater than 0."
    if discount < 0 or discount > 100:
        return "The discount should be between 0 and 100."
    final_price = price - (price * (discount / 100))
    return final_price

while True:
    try:
        price_input = input("Enter product price: ")
        price = float(price_input)
        discount_input = input("Enter how much discount want to give: ")
        discount = float(discount_input)
    except ValueError:
        print("Please enter valid numbers.")
        continue

    result = apply_discount(price, discount)
    print("Result:", result)
    if isinstance(result, (int, float)):
        break