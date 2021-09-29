# Split and then add both sides of an array together.
#
# https://www.codewars.com/kata/5946a0a64a2c5b596500019a
#
# Inspired by the Fold an Array kata. This one is sort of similar but a little different.
#
# Task
# You will receive an array as parameter that contains 1 or more integers and a number n.
#
# Here is a little visualization of the process:
#
# Step 1: Split the array in two:
#
# [1, 2, 5, 7, 2, 3, 5, 7, 8]
#       /            \
# [1, 2, 5, 7]    [2, 3, 5, 7, 8]
# Step 2: Put the arrays on top of each other:
#
#    [1, 2, 5, 7]
# [2, 3, 5, 7, 8]
# Step 3: Add them together:
#
# [2, 4, 7, 12, 15]
# Repeat the above steps n times or until there is only one number left, and then return the array.
#
# Example
# Input: arr=[4, 2, 5, 3, 2, 5, 7], n=2
#
#
# Round 1
# -------
# step 1: [4, 2, 5]  [3, 2, 5, 7]
#
# step 2:    [4, 2, 5]
#         [3, 2, 5, 7]
#
# step 3: [3, 6, 7, 12]
#
#
# Round 2
# -------
# step 1: [3, 6]  [7, 12]
#
# step 2:  [3,  6]
#          [7, 12]
#
# step 3: [10, 18]
#
#
# Result: [10, 18]

def split_and_add(numbers, n):
    while n > 0 and len(numbers) > 1:
        n -= 1
        left_lst = numbers[0:len(numbers) // 2]
        right_lst = numbers[len(numbers) // 2:]
        if len(left_lst) == len(right_lst):
            for i in range(len(left_lst)):
                numbers[i] = left_lst[i] + right_lst[i]
        else:
            numbers[0] = right_lst[0]
            for i in range(1, len(right_lst)):
                numbers[i] = left_lst[i - 1] + right_lst[i]
        numbers = numbers[0: len(right_lst)]
    return numbers

# Best practice and clever solution:
#
# def split_and_add(numbers, n):
#     for _ in range(n):
#         middle = len(numbers) // 2
#         left = numbers[:middle]
#         right = numbers[middle:]
#         numbers = [a + b for a, b in zip((len(right) - len(left)) * [0] + left, right)]
#         if len(numbers) == 1:
#             return numbers
#     return numbers