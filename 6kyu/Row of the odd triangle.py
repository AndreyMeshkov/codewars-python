# Row of the odd triangle
#
# https://www.codewars.com/kata/5d5a7525207a674b71aa25b5
#
# Given a triangle of consecutive odd numbers:
#
#              1
#           3     5
#        7     9    11
#    13    15    17    19
# 21    23    25    27    29
# ...
# find the triangle's row knowing its index (the rows are 1-indexed), e.g.:
#
# odd_row(1)  ==  [1]
# odd_row(2)  ==  [3, 5]
# odd_row(3)  ==  [7, 9, 11]
# Note: your code should be optimized to handle big inputs.

def odd_row(n):
    first_num = n * n - (n - 1)
    return [i for i in range(first_num, first_num + n * 2, 2)]

# Best practice:
#
# odd_row = lambda n:list(range(n*(n-1)+1,n*(n+1),2))

# Clever solution:
#
# def odd_row(n):
#     m = (n - 1) * n + 1
#     return [*range(m, m + n * 2, 2)]
