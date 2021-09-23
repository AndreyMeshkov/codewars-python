# Character frequency
#
# https://www.codewars.com/kata/53e895e28f9e66a56900011a
#
# Write a function that takes a piece of text in the form of a string and returns the letter frequency count for the text. This count excludes numbers, spaces and all punctuation marks. Upper and lower case versions of a character are equivalent and the result should all be in lowercase.
#
# The function should return a list of tuples (in Python and Haskell) or arrays (in other languages) sorted by the most frequent letters first. The Rust implementation should return an ordered BTreeMap. Letters with the same frequency are ordered alphabetically. For example:
#
#   letter_frequency('aaAabb dddDD hhcc')
# will return
#
#   [('d',5), ('a',4), ('b',2), ('c',2), ('h',2)]
# Letter frequency analysis is often used to analyse simple substitution cipher texts like those created by the Caesar cipher.

def letter_frequency(text):
    obj = {}
    for ch in text:
        if ch.isalpha():
            letter = ch.lower()
            if letter in obj:
                obj[letter] += 1
            else:
                obj[letter] = 1
    return tuple(sorted(obj.items(), key=lambda x: (-x[1], x[0])))

# Best practice and clever solution:
#
# from collections import Counter
# from operator import itemgetter
#
# def letter_frequency(text):
#     items = Counter(c for c in text.lower() if c.isalpha()).items()
#     return sorted(
#         sorted(items, key=itemgetter(0)),
#         key=itemgetter(1),
#         reverse=True
#     )
