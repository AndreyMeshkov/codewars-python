# Largest Elements
#
# https://www.codewars.com/kata/53d32bea2f2a21f666000256
#
# Write a program that outputs the top n elements from a list.
#
# Example:
#
# largest(2, [7,6,5,4,3,2,1])
# # => [6,7]

def largest(n, xs):
    return sorted(xs)[-n:]

# Best practice and clever solurion:
#
#
# def largest(n, xs):
#     "Find the n highest elements in a list"
#
#     return sorted(xs)[-n:];
