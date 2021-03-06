# Find within array
#
# https://www.codewars.com/kata/51f082ba7297b8f07f000001
#
# We'll create a function that takes in two parameters:
#
# a sequence (length and types of items are irrelevant)
# a function (value, index) that will be called on members of the sequence and their index. The function will return either true or false.
# Your function will iterate through the members of the sequence in order until the provided function returns true; at which point your function will return that item's index.
#
# If the function given returns false for all members of the sequence, your function should return -1.
#
# true_if_even = lambda value, index: value % 2 == 0
# find_in_array([1,3,5,6,7], true_if_even) # --> 3

def find_in_array(seq, predicate):
    try:
        return [predicate(val, ind) for ind, val in enumerate(seq)].index(True)
    except:
        return -1

# Best practice:
#
# def find_in_array(seq, predicate):
#     for index, value in enumerate(seq):
#         if predicate(value, index):
#             return index
#     return -1

# Clever solution:
#
# def find_in_array(seq, fn):
#     return next((i for i, j in enumerate(seq) if fn(j, i)), -1)
