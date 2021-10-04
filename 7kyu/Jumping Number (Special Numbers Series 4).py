# Jumping Number (Special Numbers Series #4)
#
# https://www.codewars.com/kata/5a54e796b3bfa8932c0000ed
#
# Definition
# Jumping number is the number that All adjacent digits in it differ by 1.
#
# Task
# Given a number, Find if it is Jumping or not .
#
# Warm-up (Highly recommended)
# Playing With Numbers Series
# Notes
# Number passed is always Positive .
#
# Return the result as String .
#
# The difference between ‘9’ and ‘0’ is not considered as 1 .
#
# All single digit numbers are considered as Jumping numbers.
#
# Input >> Output Examples
# jumpingNumber(9) ==> return "Jumping!!"
# Explanation:
# It's single-digit number
# jumpingNumber(79) ==> return "Not!!"
# Explanation:
# Adjacent digits don't differ by 1
# jumpingNumber(23) ==> return "Jumping!!"
# Explanation:
# Adjacent digits differ by 1
# jumpingNumber(556847) ==> return "Not!!"
# Explanation:
# Adjacent digits don't differ by 1
# jumpingNumber(4343456) ==> return "Jumping!!"
# Explanation:
# Adjacent digits differ by 1
# jumpingNumber(89098) ==> return "Not!!"
# Explanation:
# Adjacent digits don't differ by 1
# jumpingNumber(32) ==> return "Jumping!!"
# Explanation:
# Adjacent digits differ by 1
# Playing with Numbers Series
# Playing With Lists/Arrays Series
# For More Enjoyable Katas
# ALL translations are welcomed
# Enjoy Learning !!
# Zizou

def jumping_number(number):
    string = str(number)
    for i in range(len(string) - 1):
        if abs(int(string[i]) - int(string[i + 1])) != 1:
            return "Not!!"
    return "Jumping!!"

# Best practice and clever solution:
#
# def jumping_number(number):
#     arr = list(map(int, str(number)))
#     return ('Not!!', 'Jumping!!')[all(map(lambda a, b: abs(a - b) == 1, arr, arr[1:]))]
