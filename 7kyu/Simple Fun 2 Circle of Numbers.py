# Simple Fun #2: Circle of Numbers
#
# https://www.codewars.com/kata/58841cb52a077503c4000015/train/python
#
# Task
# Consider integer numbers from 0 to n - 1 written down along the circle in such a way that the distance between any two neighbouring numbers is equal (note that 0 and n - 1 are neighbouring, too).
#
# Given n and firstNumber/first_number/first-number, find the number which is written in the radially opposite position to firstNumber.
#
# Example
# For n = 10 and firstNumber = 2, the output should be 7
#
#
#
# Input/Output
# [input] integer n
#
# A positive even integer.
#
# Constraints: 4 ≤ n ≤ 1000.
#
# [input] integer firstNumber/first_number/first-number
#
# Constraints: 0 ≤ firstNumber ≤ n - 1
#
# [output] an integer

def circle_of_numbers(n, fst):
    return (fst + n / 2) % n

# Best practice and clever solution:
#
# def circle_of_numbers(n, fst):
#     return (fst + (n/2)) % n
