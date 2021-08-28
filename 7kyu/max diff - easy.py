# max diff - easy
#
# https://www.codewars.com/kata/588a3c3ef0fbc9c8e1000095
#
# You must implement a function that return the difference between the biggest and the smallest value in a list(lst) received as parameter.
#
# The list(lst) contains integers, that means it may contain some negative numbers.
#
# If the list is empty or contains a single element, return 0.
#
# The list(lst) is not sorted.
#
# max_diff([1, 2, 3, 4]) # return 3, because 4 - 1 == 3
# max_diff([1, 2, 3, -4]) # return 7, because 3 - (-4) == 7
# Have fun!

def max_diff(lst):
    return max(lst) - min(lst) if len(lst) > 0 else 0

# Best practice and clever solution:
#
# def max_diff(list):
#     return max(list) - min(list) if list else 0
