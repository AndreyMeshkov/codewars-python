# Transpose two strings in an array
#
# https://www.codewars.com/kata/581f4ac139dc423f04000b99
#
# You will be given an array that contains two strings. Your job is to create a function that will take those two strings and transpose them, so that the strings go from top to bottom instead of left to right.
#
# e.g. transposeTwoStrings(['Hello','World']);
#
# should return
#
# H W
# e o
# l r
# l l
# o d
# A few things to note:
#
# There should be one space in between the two characters
# You don't have to modify the case (i.e. no need to change to upper or lower)
# If one string is longer than the other, there should be a space where the character would be

def transpose_two_strings(arr):
    result = ''
    n = max(len(arr[0]), len(arr[1]))
    for i in range(n):
        if i < len(arr[0]):
            result += arr[0][i] + ' '
        else:
            result += '  '
        if i < len(arr[1]):
            result += arr[1][i]
        else:
            result += ' '
        if i < n - 1: result += '\n'
    return result

# Best practice:
#
# from itertools import izip_longest
#
#
# def transpose_two_strings(arr):
#     output = '{} {}'.format
#     return '\n'.join(output(*a) for a in izip_longest(*arr, fillvalue=' '))

# Clever solution:
#
# import itertools
# def transpose_two_strings(arr):
#     return '\n'.join( ' '.join(elt) for elt in itertools.zip_longest(arr[0],arr[1],fillvalue=' ') )
