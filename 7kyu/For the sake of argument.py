# For the sake of argument
#
# https://www.codewars.com/kata/5258b272e6925db09900386a
#
# Write a function named numbers.
#
# function should return True if all the parameters it is passed are of the integer type or float type. Otherwise, the function should return False.
#
# The function should accept any number of parameters.
#
# Example usage:
#
# numbers(1, 4, 3, 2, 5); # True
# numbers(1, "a", 3); # False
# numbers(1, 3, None); # False
# numbers(1.23, 5.6, 3.2) # True

def numbers(*args):
    return list(args) == [i for i in args if
      not isinstance(i, bool) and (isinstance(i, int) or isinstance(i, float))]

# Best practice and clever solution:
#
# def numbers(*args):
#     return all(type(a) in (int, float) for a in args)