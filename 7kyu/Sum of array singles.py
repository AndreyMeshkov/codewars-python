# Sum of array singles
#
# https://www.codewars.com/kata/59f11118a5e129e591000134
#
# In this Kata, you will be given an array of numbers in which two numbers occur once and the rest occur only twice. Your task will be to return the sum of the numbers that occur only once.
#
# For example, repeats([4,5,7,5,4,8]) = 15 because only the numbers 7 and 8 occur once, and their sum is 15. Every other number occurs twice.
#
# More examples in the test cases.
#
# Good luck!

def repeats(arr):
    result = 0
    for num in arr:
        if arr.count(num) == 1:
            result += num
    return result

# Best practice:
#
# def repeats(arr):
#     return sum([x for x in arr if arr.count(x) == 1])
#
# Clever solution:
#
# repeats=lambda a:2*sum(set(a))-sum(a)
