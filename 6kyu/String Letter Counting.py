# String Letter Counting
#
# https://www.codewars.com/kata/59e19a747905df23cb000024
#
# Take an input string and return a string that is made up of the number of occurences of each english letter in the input followed by that letter, sorted alphabetically. The output string shouldn't contain chars missing from input (chars with 0 occurence); leave them out.
#
# An empty string, or one with no letters, should return an empty string.
#
# Notes:
#
# the input will always be valid;
# treat letters as case-insensitive
# Examples
# "This is a test sentence."  ==>  "1a1c4e1h2i2n4s4t"
# ""                          ==>  ""
# "555"                       ==>  ""

def string_letter_count(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    string = s.lower()
    result = ""
    for letter in alphabet:
        if letter in string:
            result += f"{string.count(letter)}{letter}"
    return result

# Best practice and clever solution:
#
# from collections import Counter
#
# def string_letter_count(s):
#     cnt = Counter(c for c in s.lower() if c.isalpha())
#     return ''.join(str(n)+c for c,n in sorted(cnt.items()))
