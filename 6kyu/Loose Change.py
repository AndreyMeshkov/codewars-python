# Loose Change
#
# https://www.codewars.com/kata/5571f712ddf00b54420000ee
#
# Welcome young Jedi! In this Kata you must create a function that takes an amount of US currency in cents, and returns a dictionary/hash which shows the least amount of coins used to make up that amount. The only coin denominations considered in this exercise are: Pennies (1¢), Nickels (5¢), Dimes (10¢) and Quarters (25¢). Therefor the dictionary returned should contain exactly 4 key/value pairs.
#
# Notes:
#
# If the function is passed either 0 or a negative number, the function should return the dictionary with all values equal to 0.
# If a float is passed into the function, its value should be be rounded down, and the resulting dictionary should never contain fractions of a coin.
# Examples
# loose_change(56)    ==>  {'Nickels': 1, 'Pennies': 1, 'Dimes': 0, 'Quarters': 2}
# loose_change(-435)  ==>  {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
# loose_change(4.935) ==>  {'Nickels': 0, 'Pennies': 4, 'Dimes': 0, 'Quarters': 0}

def loose_change(cents):
    coins = {
        'Nickels': 0,
        'Pennies': 0,
        'Dimes': 0,
        'Quarters': 0
    }
    coins_value = [25, 10, 5, 1]
    keys = ['Quarters', 'Dimes', 'Nickels', 'Pennies']
    if cents <= 0:
        return coins
    for i in range(len(coins_value)):
        number_of_coins = cents // coins_value[i]
        if number_of_coins > 0:
            coins[keys[i]] = number_of_coins
            cents -= number_of_coins * coins_value[i]
    return coins

# Best practice:

# import math


# def loose_change(cents):
#     if cents < 0:
#         cents = 0
#     cents = int(cents)
#
#     change = {}
#
#     change['Quarters'] = cents // 25
#     cents = cents % 25
#
#     change['Dimes'] = cents // 10
#     cents = cents % 10
#
#     change['Nickels'] = cents // 5
#     cents = cents % 5
#
#     change['Pennies'] = cents
#
#     return change

# Clever solutiom:
#
# def loose_change(cents):
#     c = max(int(cents), 0)
#     return {'Quarters': c/25, 'Dimes': c%25/10, 'Nickels': c%25%10/5, 'Pennies': c%5}
