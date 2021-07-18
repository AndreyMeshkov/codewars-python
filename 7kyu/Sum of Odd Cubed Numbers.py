# Sum of Odd Cubed Numbers
#
# https://www.codewars.com/kata/580dda86c40fa6c45f00028a
#
# Find the sum of the odd numbers within an array, after cubing the initial integers. The function should return undefined/None/nil/NULL if any of the values aren't numbers.
#
# Note: Booleans should not be considered as numbers.

def cube_odd(arr):
    result = 0
    for num in arr:
        if type(num) != int:
            return None
        if num % 2 == 1:
            result += num ** 3
    return result

# Best practice and clever solution:
#
# def cube_odd(arr):
#     return sum( n**3 for n in arr if n % 2 ) if all(type(n) == int for n in arr) else None