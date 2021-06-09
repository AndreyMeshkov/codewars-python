# repeatIt
#
# https://www.codewars.com/kata/557af9418895e44de7000053
#
# Create a function that takes a string and an integer (n).
#
# The function should return a string that repeats the input string n number of times.
#
# If anything other than a string is passed in you should return "Not a string"
#
# Example
# "Hi", 2 --> "HiHi"
# 1234, 5 --> "Not a string"

def repeat_it(string, n):
    return "Not a string" if not isinstance(string, str) else string * n

# Best practice and clever solution:
#
# def repeat_it(string,n):
#     return string * n if isinstance(string,str) else 'Not a string'
