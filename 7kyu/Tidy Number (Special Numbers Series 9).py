# Tidy Number (Special Numbers Series #9)
#
# https://www.codewars.com/kata/5a87449ab1710171300000fd
#
# Definition
# A Tidy number is a number whose digits are in non-decreasing order.
#
# Task
# Given a number, Find if it is Tidy or not .
#
# Warm-up (Highly recommended)
# Playing With Numbers Series
# Notes
# Number passed is always Positive .
#
# Return the result as a Boolean
#
# Input >> Output Examples
# tidyNumber (12) ==> return (true)
# Explanation:
# The number's digits { 1 , 2 } are in non-Decreasing Order (i.e) 1 <= 2 .
#
# tidyNumber (32) ==> return (false)
# Explanation:
# The Number's Digits { 3, 2} are not in non-Decreasing Order (i.e) 3 > 2 .
#
# tidyNumber (1024) ==> return (false)
# Explanation:
# The Number's Digits {1 , 0, 2, 4} are not in non-Decreasing Order as 0 <= 1 .
#
# tidyNumber (13579) ==> return (true)
# Explanation:
# The number's digits {1 , 3, 5, 7, 9} are in non-Decreasing Order .
#
# tidyNumber (2335) ==> return (true)
# Explanation:
# The number's digits {2 , 3, 3, 5} are in non-Decreasing Order , Note 3 <= 3
#
# Playing with Numbers Series
# Playing With Lists/Arrays Series
# For More Enjoyable Katas
# ALL translations are welcomed
# Enjoy Learning !!
# Zizou

def tidyNumber(n):
    string = str(n)
    for i in range(len(string) - 1):
        if string[i] > string[i + 1]:
            return False
    return True

# Best practice and clever solution:
#
# def tidyNumber(n):
#     s = list(str(n))
#     return s == sorted(s)
