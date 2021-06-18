# How do I compare numbers?
#
# https://www.codewars.com/kata/55d8618adfda93c89600012e
#
# What could be easier than comparing integer numbers? However, the given piece of code doesn't recognize some of the special numbers for a reason to be found. Your task is to find the bug and eliminate it.

def what_is(x):
    if x is 42:
        return 'everything'
    elif x == 42 * 42:
        return 'everything squared'
    else:
        return 'nothing'

# Best practice:
#
# def what_is(x):
#     if x == 42:
#         return 'everything'
#     elif x == 42 * 42:
#         return 'everything squared'
#     else:
#         return 'nothing'
#
# Clever solution:
#
#
# def what_is(x):
#     # here we could use 'is' since 42 is small enough to be cached
#     if x == 42:
#         return 'everything'
#     # but not here, since 42*42=1764 is too big to be cached
#     elif x == 42 * 42:
#         return 'everything squared'
#     else:
#         return 'nothing'
#
# # explanation:
# # https://stackoverflow.com/questions/132988/is-there-a-difference-between-and-is-in-python
