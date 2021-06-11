# What century is it?
#
# https://www.codewars.com/kata/52fb87703c1351ebd200081f
#
# Return the century of the input year. The input will always be a 4 digit string, so there is no need for validation.
#
# Examples
# "1999" --> "20th"
# "2011" --> "21st"
# "2154" --> "22nd"
# "2259" --> "23rd"
# "1124" --> "12th"
# "2000" --> "20th"
import math


def what_century(year):
    century = str(math.ceil(int(year) / 100))
    str_ = ''
    if century[-1] == '1' and int(century) > 20:
        str_ = 'st'
    elif century[-1] == '2' and int(century) > 20:
        str_ = 'nd'
    elif century[-1] == '3' and int(century) > 20:
        str_ = 'rd'
    else:
        str_ = 'th'
    return century + str_

# Best practice and clever solution:
#
# def what_century(year):
#     n = (int(year) - 1) // 100 + 1
#     return str(n) + ("th" if n < 20 else {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th"))
