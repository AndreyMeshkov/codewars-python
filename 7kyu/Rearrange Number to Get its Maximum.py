# Rearrange Number to Get its Maximum
#
# https://www.codewars.com/kata/563700da1ac8be8f1e0000dc
#
# Create a function that takes one positive three digit integer and rearranges its digits to get the maximum possible number. Assume that the argument is an integer.
#
# Return -1 if the argument is not valid
# Return null (nil for Ruby, nothing for Julia) if the argument is not valid.
#
# maxRedigit(123); // returns 321

def max_redigit(num):
    if 99 < num < 1000:
        return int("".join(sorted(list(str(num)))[::-1]))
    else:
        return None

# Best practice and clever solution:
#
# def max_redigit(num):
#     if isinstance(num, int) and 99 < num < 1000:
#         return int("".join(sorted(str(num), reverse=True)))