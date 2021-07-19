# Adding ordinal indicator suffixes to numbers
#
# https://www.codewars.com/kata/52dca71390c32d8fb900002b
#
# Finish the function numberToOrdinal, which should take a number and return it as a string with the correct ordinal indicator suffix (in English). That is:
#
# numberToOrdinal(1) ==> '1st'
# numberToOrdinal(2) ==> '2nd'
# numberToOrdinal(3) ==> '3rd'
# numberToOrdinal(4) ==> '4th'
# ... and so on
# For the purposes of this kata, you may assume that the function will always be passed a non-negative integer. If the function is given 0 as an argument, it should return '0' (as a string).
#
# To help you get started, here is an excerpt from Wikipedia's page on Ordinal Indicators:
#
# st is used with numbers ending in 1 (e.g. 1st, pronounced first)
# nd is used with numbers ending in 2 (e.g. 92nd, pronounced ninety-second)
# rd is used with numbers ending in 3 (e.g. 33rd, pronounced thirty-third)
# As an exception to the above rules, all the "teen" numbers ending with 11, 12 or 13 use -th (e.g. 11th, pronounced eleventh, 112th, pronounced one hundred [and] twelfth)
# th is used for all other numbers (e.g. 9th, pronounced ninth).

def number_to_ordinal(n):
    string = str(n)
    if n == 0:
        return "0"
    if string[-1] == "1" and (n == 1 or string[-2] != "1"):
        return string + "st"
    if string[-1] == "2" and (n == 1 or string[-2] != "1"):
        return string + "nd"
    if string[-1] == "3" and (n == 1 or string[-2] != "1"):
        return string + "rd"
    return string + "th"

# Best practice:
#
# def numberToOrdinal(n):
#     if not (11 <= n % 100 <= 13):
#         if n % 10 == 1:
#             return f'{n}st'
#         elif n % 10 == 2:
#             return f'{n}nd'
#         elif n % 10 == 3:
#             return f'{n}rd'
#     return f'{n}th' if n else '0'
#
# Clever solution:
#
# def numberToOrdinal(n):
#     return '0' if n==0 else str(n) + ('th' if 10 <= n % 100 < 20 else {1:'st', 2:'nd', 3:'rd'}.get(n%10, 'th'))