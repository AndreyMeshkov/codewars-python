# Count letters in string
#
# https://www.codewars.com/kata/5808ff71c7cfa1c6aa00006d
#
# In this kata, you've to count lowercase letters in a given string and return the letter count in a hash with 'letter' as key and count as 'value'. The key must be 'symbol' instead of string in Ruby and 'char' instead of string in Crystal.
#
# Example:
#
# letter_count('arithmetics') #=> {"a": 1, "c": 1, "e": 1, "h": 1, "i": 2, "m": 1, "r": 1, "s": 1, "t": 2}

def letter_count(s):
    result = {}
    for ch in s:
        if ch in result:
            result[ch] += 1
        else:
            result[ch] = 1
    return result

# Best practice:
#
# from collections import Counter
# def letter_count(s):
#     return Counter(s)
#
# Clever solution:
#
# from collections import Counter as letter_count
