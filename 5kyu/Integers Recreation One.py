# Integers: Recreation One
#
# https://www.codewars.com/kata/55aa075506463dac6600010d
#
# 1, 246, 2, 123, 3, 82, 6, 41 are the divisors of number 246. Squaring these divisors we get: 1, 60516, 4, 15129, 9, 6724, 36, 1681. The sum of these squares is 84100 which is 290 * 290.
#
# Task
# Find all integers between m and n (m and n integers with 1 <= m <= n) such that the sum of their squared divisors is itself a square.
#
# We will return an array of subarrays or of tuples (in C an array of Pair) or a string. The subarrays (or tuples or Pairs) will have two elements: first the number the squared divisors of which is a square and then the sum of the squared divisors.
#
# Example:
# list_squared(1, 250) --> [[1, 1], [42, 2500], [246, 84100]]
# list_squared(42, 250) --> [[42, 2500], [246, 84100]]
# The form of the examples may change according to the language, see "Sample Tests".
#
# Note
# In Fortran - as in any other language - the returned string is not permitted to contain any redundant trailing whitespace: you can use dynamically allocated character strings.
import math


def list_squared(m, n):
    result = []
    for num in range(m, n + 1):
        divisors = set()
        for i in range(1, int(math.sqrt(num) + 1)):
            if num % i == 0:
                divisors.add(i ** 2)
                divisors.add(int(num / i) ** 2)
        sum_divisors = sum(divisors)
        if math.sqrt(sum_divisors) % 1 == 0:
            result.append([num, sum_divisors])
    return result

# Best practice:
#
# CACHE = {}
#
#
# def squared_cache(number):
#     if number not in CACHE:
#         divisors = [x for x in range(1, number + 1) if number % x == 0]
#         CACHE[number] = sum([x * x for x in divisors])
#         return CACHE[number]
#
#     return CACHE[number]
#
#
# def list_squared(m, n):
#     ret = []
#
#     for number in range(m, n + 1):
#         divisors_sum = squared_cache(number)
#         if (divisors_sum ** 0.5).is_integer():
#             ret.append([number, divisors_sum])
#
#     return ret

# Clever solution:
#
# WOAH = [1, 42, 246, 287, 728, 1434, 1673, 1880,
#         4264, 6237, 9799, 9855, 18330, 21352, 21385,
#         24856, 36531, 39990, 46655, 57270, 66815,
#         92664, 125255, 156570, 182665, 208182, 212949,
#         242879, 273265, 380511, 391345, 411558, 539560,
#         627215, 693160, 730145, 741096]
#
# list_squared = lambda HUH, YEAH: [[YES, DUH(YES)] for YES in WOAH if YES >= HUH and YES <= YEAH]
# DUH = lambda YEP: sum(WOW**2 for WOW in range(1, YEP + 1) if YEP % WOW == 0)
