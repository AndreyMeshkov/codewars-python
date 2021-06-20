# Ensure question
#
# https://www.codewars.com/kata/5866fc43395d9138a7000006
#
# Given a string, write a function that returns the string with a question mark ("?") appends to the end, unless the original string ends with a question mark, in which case, returns the original string.
#
# ensure_question("Yes") == "Yes?"
# ensure_question("No?") == "No?"

def ensure_question(s):
    return s + '?' if '?' not in s else s

# Best practice and clever solution:
#
# def ensure_question(s):
#     return s.rstrip('?') + '?'
