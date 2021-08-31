# Least Common Multiple
#
# https://www.codewars.com/kata/5259acb16021e9d8a60010af
#
# Write a function that calculates the least common multiple of its arguments; each argument is assumed to be a non-negative integer. In the case that there are no arguments (or the provided array in compiled languages is empty), return 1.

from math import gcd


def lcm(*args):
    if 0 in args:
        return 0
    lcm = 1
    for i in args:
        lcm = lcm * i // gcd(lcm, i)
    return lcm

# Best practice and clever solution:
#
# from math import gcd
# from functools import reduce
# from operator import mul
#
# def lcm(*args):
#     return 1 if not args else reduce(lambda a, b: mul(a, b) // gcd(a, b), args)