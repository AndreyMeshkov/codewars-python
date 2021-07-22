# Remove Duplicates
#
# https://www.codewars.com/kata/53e30ec0116393fe1a00060b
#
# Remove Duplicates
# You are to write a function called unique that takes an array of integers and returns the array with duplicates removed. It must return the values in the same order as first seen in the given array. Thus no sorting should be done, if 52 appears before 10 in the given array then it should also be that 52 appears before 10 in the returned array.
#
# Assumptions
# All values given are integers (they can be positive or negative).
# You are given an array but it may be empty.
# They array may have duplicates or it may not.
# Example
# print unique([1, 5, 2, 0, 2, -3, 1, 10])
# [1, 5, 2, 0, -3, 10]
#
# print unique([])
# []
#
# print unique([5, 2, 1, 3])
# [5, 2, 1, 3]

def unique(integers):
    result = []
    for integer in integers:
        if integer not in result:
            result.append(integer)
    return result

# Best practice and clever solution:
#
# from collections import OrderedDict
# def unique(integers):
#     return list(OrderedDict.fromkeys(integers))
