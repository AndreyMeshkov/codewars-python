# Array Deep Count
#
# https://www.codewars.com/kata/596f72bbe7cd7296d1000029
#
# len(a) will give you the number of top-level elements in the list/array named a.
#
# Your task is to create a function deepCount that returns the number of ALL elements within an array, including any within inner-level arrays.
#
# For example:
#
# deepCount([1, 2, 3]);
# //>>>>> 3
# deepCount(["x", "y", ["z"]]);
# //>>>>> 4
# deepCount([1, 2, [3, 4, [5]]]);
# //>>>>> 7
# The input will always be an array.

def deep_count(a):
    count = 0
    for i in a:
        count += 1
        if isinstance(i, list):
            return count + deep_count(i)
    return count
# TODO-1 - fix