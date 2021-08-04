# Return Two Highest Values in List
#
# https://www.codewars.com/kata/57ab3c09bb994429df000a4a
#
# In this kata, your job is to return the two distinct highest values in a list. If there're less than 2 unique values, return as many of them, as possible.
#
# The result should also be ordered from highest to lowest.
#
# Examples:
#
# [4, 10, 10, 9]  =>  [10, 9]
# [1, 1, 1]  =>  [1]
# []  =>  []

def two_highest(arg1):
    sorted_set = sorted(set(arg1))
    if len(sorted_set) > 1:
        return [sorted_set[-1], sorted_set[-2]]
    elif len(sorted_set) > 0:
        return [sorted_set[-1]]
    else:
        return []

# Best practice:
#
# def two_highest(ls):
#     result = sorted(list(set(ls)), reverse=True)[:2]
#     return result if isinstance(ls, (list)) else False
#
# Clever solution:
#
# import heapq
# def two_highest(list_):
#     return heapq.nlargest(2, set(list_)) if type(list_) == list else False
