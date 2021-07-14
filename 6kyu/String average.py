# String average
#
# https://www.codewars.com/kata/5966847f4025872c7d00015b
#
# You are given a string of numbers between 0-9. Find the average of these numbers and return it as a floored whole number (ie: no decimal places) written out as a string. Eg:
#
# "zero nine five two" -> "four"
#
# If the string is empty or includes a number greater than 9, return "n/a"

def average_string(s):
    if len(s) == 0:
        return "n/a"
    list_num = s.split()
    numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven",
               "eight", "nine"]
    total = 0
    for num in list_num:
        if num in numbers:
            total += numbers.index(num)
        else:
            return "n/a"
    return numbers[int(total / len(list_num))]

# Best practice and clever solution:
#
# N = ['zero','one','two','three','four','five','six','seven','eight','nine']
#
# def average_string(s):
#     try:
#         return N[sum(N.index(w) for w in s.split()) // len(s.split())]
#     except (ZeroDivisionError, ValueError):
#         return 'n/a'
