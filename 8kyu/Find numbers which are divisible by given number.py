# Find numbers which are divisible by given number
#
# https://www.codewars.com/kata/55edaba99da3a9c84000003b
#
# Complete the function which takes two arguments and returns all numbers which are divisible by the given divisor. First argument is an array of numbers and the second is the divisor.
#
# Example
# divisible_by([1, 2, 3, 4, 5, 6], 2) == [2, 4, 6]

def divisible_by(numbers, divisor):
    return [x for x in numbers if x % divisor == 0]

# Best  practice and clever solution:
#
# def divisible_by(numbers, divisor):
#     return [x for x in numbers if x%divisor == 0]
