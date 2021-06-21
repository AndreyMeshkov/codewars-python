# Find the Slope
#
# https://www.codewars.com/kata/55a75e2d0803fea18f00009d
#
# Given an array of 4 integers
# [a,b,c,d] representing two points (a, b) and (c, d), return a string representation of the slope of the line joining these two points.
#
# For an undefined slope (division by 0), return undefined . Note that the "undefined" is case-sensitive.
#
#    a:x1
#    b:y1
#    c:x2
#    d:y2
# Assume that [a,b,c,d] and the answer are all integers (no floating numbers!). Slope: https://en.wikipedia.org/wiki/Slope

def find_slope(points):
    if points[2] == points[0]:
        return "undefined"
    return str(int((points[3] - points[1]) / (points[2] - points[0])))

# Best practice:
#
# def find_slope(points):
#     try:
#         return str((points[3]-points[1])/(points[2]-points[0]))
#     except ZeroDivisionError:
#         return "undefined"

# Clever solution:
#
# def find_slope(points):
#     a,b,c,d = points
#     return 'undefined' if a == c else str((b - d) / (a - c))
