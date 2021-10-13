# Numbers in strings
#
# https://www.codewars.com/kata/59dd2c38f703c4ae5e000014
#
# In this Kata, you will be given a string that has lowercase letters and numbers. Your task is to compare the number groupings and return the largest number. Numbers will not have leading zeros.
#
# For example, solve("gh12cdy695m1") = 695, because this is the largest of all number groupings.
#
# Good luck!
#
# Please also try Simple remove duplicates

import re


def solve(s):
    lst = [int(i) for i in re.split("[^\d]", s) if i != ""]
    return max(lst)

# Best practice and clever solution:
#
# import re
#
#
# def solve(s):
#     return max(map(int,re.findall(r"(\d+)", s)))