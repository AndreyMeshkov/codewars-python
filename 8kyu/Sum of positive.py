# Sum of positive
#
# https://www.codewars.com/kata/5715eaedb436cf5606000381
#
# You get an array of numbers, return the sum of all of the positives ones.
#
# Example [1,-4,7,12] => 1 + 7 + 12 = 20
#
# Note: if there is nothing to sum, the sum is default to 0.

def positive_sum(arr):
    result = 0
    for i in arr:
        if i > 0:
            result += i
    return result

# Best practice and clever solution:
#
# def positive_sum(arr):
#     return sum(x for x in arr if x > 0)
