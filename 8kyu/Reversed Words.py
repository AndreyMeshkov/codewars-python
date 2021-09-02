# Reversed Words
#
# https://www.codewars.com/kata/51c8991dee245d7ddf00000e
#
# Complete the solution so that it reverses all of the words within the string passed in.
#
# Example:
#
# "The greatest victory is that which requires no battle" --> "battle no requires which that is victory greatest The"

def reverse_words(s):
    return " ".join(s.split()[::-1])

# Best practice and clever solution:
#
# def reverseWords(str):
#     return " ".join(str.split(" ")[::-1])