# Fake Binary
#
# https://www.codewars.com/kata/57eae65a4321032ce000002d
#
# Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

def fake_bin(x):
    result = ""
    for num in x:
        if num < "5":
            result += "0"
        else:
            result += "1"
    return result

# Best practice and clever solution:
#
# def fake_bin(x):
#     return ''.join('0' if c < '5' else '1' for c in x)
