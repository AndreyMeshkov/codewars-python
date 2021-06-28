# Last
#
# https://www.codewars.com/kata/541629460b198da04e000bb9
#
# Find the last element of the given argument(s).
#
# Examples
# last([1, 2, 3, 4]) ==>  4
# last("xyz")        ==> "z"
# last(1, 2, 3, 4)   ==>  4
# In javascript and CoffeeScript a list will be an array, a string or the list of arguments.

def last(*args):
    try:
        return args[-1][-1]
    except:
        return args[-1]

# Best practice:
#
# def last(*args):
#     return args[-1] if not hasattr(args[-1], "__getitem__") else args[-1][-1]
#
# Clever solution:
#
# def last(*args):
#     try:
#         return args[-1][-1]
#     except:
#         return args[-1]
