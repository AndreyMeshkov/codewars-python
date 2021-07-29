# Sum of integers in string
#
# https://www.codewars.com/kata/598f76a44f613e0e0b000026
#
# Your task in this kata is to implement a function that calculates the sum of the integers inside a string. For example, in the string "The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog", the sum of the integers is 3635.
#
# Note: only positive integers will be tested.
import re


def sum_of_integers_in_string(s):
    numbers = re.split("[^0-9]", s)
    result = 0
    for i in numbers:
        if len(i) > 0:
            result += int(i)
    return result

# Best practice:
#
# import re
#
# def sum_of_integers_in_string(s):
#     return sum(int(x) for x in re.findall(r"(\d+)", s))

# Clever solution:
#
# def sum_of_integers_in_string(s):
#     return sum(map(int, ''.join(c if c.isdigit() else ' ' for c in s).split()))
