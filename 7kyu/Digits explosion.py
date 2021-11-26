# Digits explosion
#
# https://www.codewars.com/kata/585b1fafe08bae9988000314
#
# Given a string made of digits [0-9], return a string where each digit is repeated a number of times equals to its value.
#
# Examples
# explode("312") # => "333122"
# explode("102269") # => "12222666666999999999"

def explode(s):
    return "".join([i * int(i) for i in s])

# Best practice and clever solution:
#
# def explode(s):
#     return ''.join(c * int(c) for c in s)
