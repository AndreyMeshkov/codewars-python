# Remove String Spaces
#
# https://www.codewars.com/kata/57eae20f5500ad98e50002c5
#
# Simple, remove the spaces from the string, then return the resultant string.

def no_space(x):
    return x.replace(" ", "")

# Best practice and clever solution:
#
# def no_space(x):
#     return x.replace(' ' ,'')