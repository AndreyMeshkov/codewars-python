# Average Scores
#
# https://www.codewars.com/kata/57b68bc7b69bfc8209000307
#
# Create a function that returns the average of an array of numbers ("scores"), rounded to the nearest whole number. You are not allowed to use any loops (including for, for/in, while, and do/while loops).

def average(array):
    return round(sum(array) / len(array))

# Best practice and clever solution:
#
# def average(array):
#     return round(sum(array) / len(array))