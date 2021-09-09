# Array Deep Count
#
# https://www.codewars.com/kata/596f72bbe7cd7296d1000029
#
# len(a) will give you the number of top-level elements in the list/array named a.
#
# Your task is to create a function deepCount that returns the number of ALL elements within an array, including any within inner-level arrays.
#
# For example:
#
# deepCount([1, 2, 3]);
# //>>>>> 3
# deepCount(["x", "y", ["z"]]);
# //>>>>> 4
# deepCount([1, 2, [3, 4, [5]]]);
# //>>>>> 7
# The input will always be an array.

def deep_count(a):
    count = 0
    for i in a:
        count += 1
        if isinstance(i, list):
            count += deep_count(i)
    return count

# Best practice:
#
# def deep_count(a):
#     result = 0
#     for i in range(len(a)):
#         if type(a[i]) is list:
#             result += deep_count(a[i])
#         result += 1
#     return result
#
# Clever solution:
#
# def deep_count(a):
#     return sum(1 + (deep_count(x) if isinstance(x, list) else 0) for x in a)
