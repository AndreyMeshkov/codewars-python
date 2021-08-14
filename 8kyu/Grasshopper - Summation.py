# Grasshopper - Summation
#
# https://www.codewars.com/kata/55d24f55d7dd296eb9000030
#
# Summation
# Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.
#
# For example:
#
# summation(2) -> 3
# 1 + 2
#
# summation(8) -> 36
# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8

def summation(num):
    return sum(x for x in range(num + 1))

# Best practice:
#
# def summation(num):
#     return sum(xrange(num + 1))
#
# Clever solution:
#
# def summation(num):
#     return (1+num) * num / 2