# Count of positives / sum of negatives
#
# https://www.codewars.com/kata/576bb71bbbcf0951d5000044
#
# Given an array of integers.
#
# Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers.
#
# If the input array is empty or null, return an empty array.
#
# Example
# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].

def count_positives_sum_negatives(arr):
    if len(arr) == 0:
        return []
    positive_num = 0
    sum_negative = 0
    for num in arr:
        if num > 0:
            positive_num += 1
        else:
            sum_negative += num
    return [positive_num, sum_negative]

# Best practice:
#
# def count_positives_sum_negatives(arr):
#     if not arr: return []
#     pos = 0
#     neg = 0
#     for x in arr:
#       if x > 0:
#           pos += 1
#       if x < 0:
#           neg += x
#     return [pos, neg]
#
# Clever solution:
#
# def count_positives_sum_negatives(arr):
#     return [len([x for x in arr if x > 0])] + [sum(y for y in arr if y < 0)] if arr else []
