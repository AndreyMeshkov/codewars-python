# Making Copies
#
# https://www.codewars.com/kata/53d2697b7152a5e13d000b82
#
# Write a function that takes a list (in Python) or array (in other languages) of numbers, and makes a copy of it.
#
# Note that you may have troubles if you do not return an actual copy, item by item, just a pointer or an alias for an existing list or array.
#
# If not a list or array is given as a parameter in interpreted languages, the function should raise an error.
#
# Examples:
#
# t = [1, 2, 3, 4]
# t_copy = copy_list(t)
#
# t[1] += 5
# t = [1, 7, 3, 4]
# t_copy = [1, 2, 3, 4]

def copy_list(l):
    if type(l) == list and len(l) > 0:
        return l.copy()
    else:
        raise Exception("Error")

# Best practice and clever solution:
#
# def copy_list(l):
#   return list(l)