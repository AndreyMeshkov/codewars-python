# Which triangle is that?
#
# https://www.codewars.com/kata/564d398e2ecf66cec00000a9
#
# Build a function that will take the length of each side of a triangle and return if it's either an Equilateral, an Isosceles, a Scalene or an invalid triangle.
#
# It has to return a string with the type of triangle.
# For example:
#
# type_of_triangle(2, 2, 1) --> "Isosceles"

def type_of_triangle(a, b, c):
    print(a, b, c)
    count = 0
    if a == b:
        count += 1
    if a == c:
        count += 1
    if b == c:
        count += 1
    if type(a) == str or type(b) == str or type(
            c) == str or a + b <= c or a + c <= b or b + c <= a:
        return "Not a valid triangle"
    if count == 3:
        return "Equilateral"
    if count == 1:
        return "Isosceles"
    if count == 0:
        return "Scalene"

# Best practice and clever solution:
#
# def type_of_triangle(a, b, c):
#     if any(not isinstance(x, int) for x in (a, b, c)):
#         return "Not a valid triangle"
#     a, b, c = sorted((a, b, c))
#     if a + b <= c:
#         return "Not a valid triangle"
#     if a == b and b == c:
#         return "Equilateral"
#     if a == b or a == c or b == c:
#         return "Isosceles"
#     return "Scalene"
