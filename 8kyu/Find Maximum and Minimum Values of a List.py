# Find Maximum and Minimum Values of a List
#
# https://www.codewars.com/kata/577a98a6ae28071780000989
#
# Your task is to make two functions, max and min (maximum and minimum in PHP and Python, maxi and mini in Julia) that take a(n) array/vector of integers list as input and outputs, respectively, the largest and lowest number in that array/vector.
#
# #Examples
#
# maximun([4,6,2,1,9,63,-134,566]) returns 566
# minimun([-52, 56, 30, 29, -54, 0, -110]) returns -110
# maximun([5]) returns 5
# minimun([42, 54, 65, 87, 0]) returns 0
# #Notes
#
# You may consider that there will not be any empty arrays/vectors.

def minimum(arr):
    return min(arr)


def maximum(arr):
    return max(arr)

# Best practice:
#
# def min(arr):
#     low = arr[0]
#     for i in arr[1:]:
#         if i < low:
#             low = i
#     return low
#
# def max(arr):
#     high = arr[0]
#     for i in arr[1:]:
#         if i > high:
#             high = i
#     return high

# Clever solution:
# def min(arr):
#     return sorted(arr)[0]
#
# def max(arr):
#     return sorted(arr)[-1]