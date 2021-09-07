# Calculate average
#
# https://www.codewars.com/kata/57a2013acf1fa5bfc4000921
#
# Write a function which calculates the average of the numbers in a given list.
#
# Note: Empty arrays should return 0.

def find_average(numbers):
    return 0 if len(numbers) == 0 else sum(numbers) / len(numbers)

# Best practice and clever solution:
#
# def find_average(array):
#     return sum(array) / len(array) if array else 0
