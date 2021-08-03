# Simple frequency sort
#
# https://www.codewars.com/kata/5a8d2bf60025e9163c0000bc
#
# In this Kata, you will sort elements in an array by decreasing frequency of elements. If two elements have the same frequency, sort them by increasing value.
#
# solve([2,3,5,3,7,9,5,3,7]) = [3,3,3,5,5,7,7,2,9]
# --we sort by highest frequency to lowest frequency. If two elements have same frequency, we sort by increasing value
# More examples in test cases.
#
# Good luck!
#
# Please also try Simple time difference

import collections


def solve(arr):
    counts = collections.Counter(arr)
    new_list = sorted(arr, key=lambda x: (-counts[x], x))
    return new_list

# Best practice and clever solution:
#
# from collections import Counter
#
# def solve(a):
#     c = Counter(a)
#     return sorted(a, key=lambda k: (-c[k], k))