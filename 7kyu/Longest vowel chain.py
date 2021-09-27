# Longest vowel chain
#
# https://www.codewars.com/kata/59c5f4e9d751df43cf000035
#
# The vowel substrings in the word codewarriors are o,e,a,io. The longest of these has a length of 2. Given a lowercase string that has alphabetic characters only (both vowels and consonants) and no spaces, return the length of the longest vowel substring. Vowels are any of aeiou.
#
# Good luck!
#
# If you like substring Katas, please try:
#
# Non-even substrings
#
# Vowel-consonant lexicon

import re


def solve(s):
    lst = re.split('[^oeaiu]', s)
    print(lst)
    return max([len(x) for x in lst])

# Best practice and clever solution:
#
# def solve(s):
#     return max(map(len, ''.join(c if c in 'aeiou' else ' ' for c in s).split()))
