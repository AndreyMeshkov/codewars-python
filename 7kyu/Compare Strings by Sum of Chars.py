# Compare Strings by Sum of Chars
#
# https://www.codewars.com/kata/576bb3c4b1abc497ec000065
#
# Compare two strings by comparing the sum of their values (ASCII character code).
#
# For comparing treat all letters as UpperCase
# null/NULL/Nil/None should be treated as empty strings
# If the string contains other characters than letters, treat the whole string as it would be empty
# Your method should return true, if the strings are equal and false if they are not equal.
#
# Examples:
# "AD", "BC"  -> equal
# "AD", "DD"  -> not equal
# "gf", "FG"  -> equal
# "zz1", ""   -> equal (both are considered empty)
# "ZzZz", "ffPFF" -> equal
# "kl", "lz"  -> not equal
# null, ""    -> equal

def compare(s1, s2):
    return calc_sum(s1) == calc_sum(s2)


def calc_sum(s):
    result = 0
    if s is not None:
        for ch in s.upper():
            if ch.isalpha():
                result += ord(ch)
            else:
                result = 0
                break
    return result

# Best practice and clever solution:
#
# def compare(s1,s2):
#     a,b =  (sum(ord(c) for c in s.upper()) for s in (s1, s2) if s.isalpha())
#     return a == b
