# Is the string uppercase?
#
# https://www.codewars.com/kata/56cd44e1aa4ac7879200010b
#
# Is the string uppercase?
# Task
# Create a method is_uppercase() to see whether the string is ALL CAPS. For example:
#
# is_uppercase("c") == False
# is_uppercase("C") == True
# is_uppercase("hello I AM DONALD") == False
# is_uppercase("HELLO I AM DONALD") == True
# is_uppercase("ACSKLDFJSgSKLDFJSKLDFJ") == False
# is_uppercase("ACSKLDFJSGSKLDFJSKLDFJ") == True
# In this Kata, a string is said to be in ALL CAPS whenever it does not contain any lowercase letter so any string containing no letters at all is trivially considered to be in ALL CAPS.

import re


def is_uppercase(inp):
    return re.search("[a-z]", inp) is None

# Best practice and clever solution:
#
# def is_uppercase(inp):
#     return inp.upper()==inp
