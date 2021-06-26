# They say that only the name is long enough to attract attention. They also said that only a simple Kata will have someone to solve it. This is a sadly story #1: Are they opposite?
#
# https://www.codewars.com/kata/574b1916a3ebd6e4fa0012e7
#
# Task
# Give you two strings: s1 and s2. If they are opposite, return true; otherwise, return false. Note: The result should be a boolean value, instead of a string.
#
# The opposite means: All letters of the two strings are the same, but the case is opposite. you can assume that the string only contains letters or it's a empty string. Also take note of the edge case - if both strings are empty then you should return false/False.
#
# Examples
# isOpposite("ab","AB") should return true;
# isOpposite("aB","Ab") should return true;
# isOpposite("aBcd","AbCD") should return true;
# isOpposite("AB","Ab") should return false;
# isOpposite("","") should return false;

def is_opposite(s1, s2):
    return s1 != "" and s1.swapcase() == s2

# Best practice and clever solution:
#
# def is_opposite(s1, s2):
#     return False if not(s1 or s2) else s1.swapcase() == s2
