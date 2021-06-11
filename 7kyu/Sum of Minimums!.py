# Sum of Minimums!
#
# https://www.codewars.com/kata/5d5ee4c35162d9001af7d699
#
# Given a 2D list of size m * n. Your task is to find the sum of minimum value in each row.
#
# For Example:
#
# [
#   [1, 2, 3, 4, 5],       # minimum value of row is 1
#   [5, 6, 7, 8, 9],       # minimum value of row is 5
#   [20, 21, 34, 56, 100]  # minimum value of row is 20
# ]

def sum_of_minimums(numbers):
    res = 0
    for i in numbers:
        res += min(i)
    return res

# Best practice and clever solution:
#
# def sum_of_minimums(numbers):
#     return sum(map(min, numbers))
