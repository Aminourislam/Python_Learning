def liters_100km_to_miles_gallon(liters):
    ans =((100*3.785411784)/(1.609344*liters))
    return ans
def miles_gallon_to_liters_100km(miles):
    ans =((100*3.785411784)/(1.609344*miles))
    return ans

a = "mile/gal"
b = "liter/100km"
print(liters_100km_to_miles_gallon(3.9),a)
print(liters_100km_to_miles_gallon(7.5),a)
print(liters_100km_to_miles_gallon(10.),a)

print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
