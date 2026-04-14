def apply_discount(price, discount):
    if not isinstance(price, (int, float)):
        returning = "The price should be a number"
        return returning
    if not isinstance(discount, (int, float)):
        returning = "The discount should be a number"
        return returning
    if price <= 0:
        returning = "The price should be greater than 0"
        return returning
    if discount < 0 or discount > 100:
        returning = "The discount should be between 0 and 100"
        return returning
    final_price = price - (price * (discount / 100))
    returning = f"Final price: {final_price}"
    return returning
    
print(apply_discount(100,20))
print(apply_discount(200,50))
print(apply_discount(50,0))
print(apply_discount(100,0))
print(apply_discount(74.5,20.0))