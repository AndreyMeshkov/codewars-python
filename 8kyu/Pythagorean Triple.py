# Pythagorean Triple
#
# https://www.codewars.com/kata/5951d30ce99cf2467e000013
#
# Given an array of 3 integers a, b and c, determine if they form a pythagorean triple.
#
# A pythagorean triple is formed when:
#
# c2 = a2 + b2
# where c is the largest value of a, b, c.
#
# For example: a = 3, b = 4, c = 5 forms a pythagorean triple, because 52 = 32 + 42
#
# Return Values
# 1 if a, b and c form a pythagorean triple
# 0 if a, b and c do not form a pythagorean triple
# For Python: return True or False

def pythagorean_triple(integers):
    integers = sorted(integers)
    return (integers[2] ** 2) == (integers[0] ** 2 + integers[1] ** 2)
#
# Best practice and clever solution:
#
# def pythagorean_triple(integers):
#     a, b, c = sorted(integers)
#     return a * a + b * b == c * c
