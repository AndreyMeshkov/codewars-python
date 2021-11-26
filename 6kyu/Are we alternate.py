# Are we alternate?
#
# https://www.codewars.com/kata/59325dc15dbb44b2440000af
#
# Create a function isAlt() that accepts a string as an argument and validates whether the vowels (a, e, i, o, u) and consonants are in alternate order.
#
# is_alt("amazon")
# // true
# is_alt("apple")
# // false
# is_alt("banana")
# // true
# Arguments consist of only lowercase letters.

def is_alt(s):
    vowels = ("a", "e", "i", "o", "u")
    if s[0] in vowels:
        if all([s[i] in vowels for i in range(len(s)) if i % 2 == 0]):
            if all([s[i] not in vowels for i in range(len(s)) if i % 2 == 1]):
                return True
    elif s[1] in vowels:
        if all([s[i] in vowels for i in range(len(s)) if i % 2 == 1]):
            if all([s[i] not in vowels for i in range(len(s)) if i % 2 == 0]):
                return True
    return False

# Best practice and clever solution:
#
# import re
#
# def is_alt(s):
#     return not re.search('[aeiou]{2}|[^aeiou]{2}',s)
