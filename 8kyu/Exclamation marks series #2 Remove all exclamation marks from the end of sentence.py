# Exclamation marks series #2: Remove all exclamation marks from the end of sentence
#
# https://www.codewars.com/kata/57faece99610ced690000165
#
# Description:
# Remove all exclamation marks from the end of sentence.
#
# Examples
# remove("Hi!") === "Hi"
# remove("Hi!!!") === "Hi"
# remove("!Hi") === "!Hi"
# remove("!Hi!") === "!Hi"
# remove("Hi! Hi!") === "Hi! Hi"
# remove("Hi") === "Hi"

def remove(s):
    while s[-1] == "!":
        s = s[0:-1]
    return s

# Best practice:
#
# def remove(s):
#     return s.rstrip("!")
#
# Clever solution:
#
# def remove(s):
#     while s and s[-1] == "!":
#         s = s[:-1]
#     return s
