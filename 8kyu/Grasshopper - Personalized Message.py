# Grasshopper - Personalized Message
#
# https://www.codewars.com/kata/5772da22b89313a4d50012f7
#
# Create a function that gives a personalized greeting. This function takes two parameters: name and owner.
#
# Use conditionals to return the proper message:
#
# case	return
# name equals owner	'Hello boss'
# otherwise	'Hello guest'

def greet(name, owner):
    return "Hello boss" if name == owner else "Hello guest"

# Best practice:
#
# def greet(name, owner):
#     return "Hello boss" if name == owner else "Hello guest"

# Clever solution:
#
# def greet(name, owner):
#     return "Hello {}".format("boss" if name == owner else "guest")
