# Round by 0.5 steps
#
# https://www.codewars.com/kata/51f1342c76b586046800002a
#
# Collect|
# Round any given number to the closest 0.5 step
#
# I.E.
#
# solution(4.2) = 4
# solution(4.3) = 4.5
# solution(4.6) = 4.5
# solution(4.8) = 5
# Round up if number is as close to previous and next 0.5 steps.
#
# solution(4.75) == 5

def solution(n):
    return 0.5 - (n % 0.5) + n if n % 0.5 >= 0.25 else n - (n % 0.5)

# Best practice and clever solution:
#
# def solution(n):
#     return round(2 * n) / 2
