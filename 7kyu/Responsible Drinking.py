# Responsible Drinking
#
# https://www.codewars.com/kata/5aee86c5783bb432cd000018
#
# Welcome to the Codewars Bar!
# Codewars Bar recommends you drink 1 glass of water per standard drink so you're not hungover tomorrow morning.
#
# Your fellow coders have bought you several drinks tonight in the form of a string. Return a string suggesting how many glasses of water you should drink to not be hungover.
#
# Examples
# "1 beer"  -->  "1 glass of water"
# because you drank one standard drink
#
# "1 shot, 5 beers, 2 shots, 1 glass of wine, 1 beer"  -->  "10 glasses of water"
# because you drank ten standard drinks
# Note:
#
# To keep the things simple, we'll consider that any "numbered thing" in the string is a drink. Even "1 bear" -> "1 glass of water"; or "1 chainsaw and 2 pools" -> "3 glasses of water"...

def hydrate(drink_string):
    words = drink_string.split(" ")
    numbers = [int(i) for i in words if i.isdigit()]
    result = sum(numbers)
    return f"{result} glass of water" if result == 1 else f"{result} glasses of water"

# Best practice:
#
# def hydrate(drink_string):
#     c=sum(int(c) for c in drink_string if c.isdigit())
#     return "{} {} of water".format(c,'glass') if c==1 else "{} {} of water".format(c,'glasses')

# Clever solution:
#
# import re
#
# def hydrate(s):
#     n = sum(map(int,re.findall(r'\d+',s)))
#     return f"{ n } glass{ 'es'*(n!=1) } of water"
