# Beginner - Lost Without a Map
#
# https://www.codewars.com/kata/57f781872e3d8ca2a000007e
#
# Given an array of integers, return a new array with each value doubled.
#
# For example:
#
# [1, 2, 3] --> [2, 4, 6]

def maps(a):
    return [x * 2 for x in a]

# Best practice and clever solution:
#
# def maps(a):
#     return [2 * x for x in a]
