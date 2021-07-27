# Minimize Sum Of Array (Array Series #1)
#
# https://www.codewars.com/kata/5a523566b3bfa84c2e00010b
#
# Introduction and Warm-up (Highly recommended)
# Playing With Lists/Arrays Series
# Task
# Given an array of integers , Find the minimum sum which is obtained from summing each Two integers product .
#
# Notes
# Array/list will contain positives only .
# Array/list will always has even size
# Input >> Output Examples
# minSum({5,4,2,3}) ==> return (22)
# Explanation:
# The minimum sum obtained from summing each two integers product , 5*2 + 3*4 = 22
# minSum({12,6,10,26,3,24}) ==> return (342)
# Explanation:
# The minimum sum obtained from summing each two integers product , 26*3 + 24*6 + 12*10 = 342
# minSum({9,2,8,7,5,4,0,6}) ==> return (74)
# Explanation:
# The minimum sum obtained from summing each two integers product , 9*0 + 8*2 +7*4 +6*5 = 74

def min_sum(arr):
    sorted_list = sorted(arr)
    result = 0
    for i in range(0, int(len(arr) / 2)):
        result += sorted_list[i] * sorted_list[-1 - i]
    return result

# Best practice and clever solution:
#
# def min_sum(arr):
#     arr = sorted(arr)
#     return sum(arr[i]*arr[-i-1] for i in range(len(arr)//2))
