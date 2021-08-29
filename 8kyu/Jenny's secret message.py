# Jenny's secret message
#
# https://www.codewars.com/kata/55225023e1be1ec8bc000390
#
# Jenny has written a function that returns a greeting for a user. However, she's in love with Johnny, and would like to greet him slightly different. She added a special case to her function, but she made a mistake.
#
# Can you help her?

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return f"Hello, {name}!"

# Best practice:
#
# def greet(name):
#     if name == "Johnny":
#         return "Hello, my love!"
#     return "Hello, {name}!".format(name=name)

# Clever solution:
#
# def greet(name):
#     return "Hello, {name}!".format(name = ('my love' if name == 'Johnny' else name));