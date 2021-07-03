# Fuel Calculator
#
# https://www.codewars.com/kata/57b58827d2a31c57720012e8
#
# In this kata you will have to write a function that takes litres and price_per_litre as arguments. Purchases of 2 or more litres get a discount of 5 cents per litre, purchases of 4 or more litres get a discount of 10 cents per litre, and so on every two litres, up to a maximum discount of 25 cents per litre. But total discount per litre cannot be more than 25 cents. Return the toal cost rounded to 2 decimal places. Also you can guess that there will not be negative or non-numeric inputs.
#
# Good Luck!

def fuel_price(litres, price_per_litre):
    discount = int(litres / 2) * 0.05
    if discount > 0.25:
        discount = 0.25
    return round(litres * (price_per_litre - discount), 2)

# Best practice and clever solution:
#
# def fuel_price(litres, price_per_liter):
#     discount = int(min(litres, 10)/2) * 5 / 100
#     return round((price_per_liter - discount) * litres, 2)
