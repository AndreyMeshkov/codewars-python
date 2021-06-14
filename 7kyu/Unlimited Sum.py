# Unlimited Sum
#
# https://www.codewars.com/kata/536c738e49aa8b663b000301
#
# Write a function sum that accepts an unlimited number of integer arguments, and adds all of them together.
#
# The function should reject any arguments that are not integers, and sum the remaining integers.
#
# sum(1, 2, 3)    ==>  6
# sum(1, "2", 3)  ==>  4

def sum(*args):
    result = 0
    for num in args:
        if type(num) == int:
            result += num
    return result

# Best practice and clever solution:
#
# from __builtin__ import sum as builtin_sum
#
# def sum(*args):
#     return builtin_sum(arg for arg in args if isinstance(arg, int))
