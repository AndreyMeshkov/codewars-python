# Merging sorted integer arrays (without duplicates)
#
# https://www.codewars.com/kata/573f5c61e7752709df0005d2
#
# Write a function that merges two sorted arrays into a single one. The arrays only contain integers. Also, the final outcome must be sorted and not have any duplicate.

def merge_arrays(first, second):
    return sorted(list(set(first + second)))

# Best practice and clever solution:
#
# def merge_arrays(a, b):
#     return sorted(set(a + b))
