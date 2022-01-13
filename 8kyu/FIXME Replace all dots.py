# FIXME: Replace all dots
#
# https://www.codewars.com/kata/596c6eb85b0f515834000049
#
# The code provided is supposed replace all the dots . in the specified String str with dashes -
#
# But it's not working properly.
#
# Task
# Fix the bug so we can all go home early.
#
# Notes
# String str will never be null.

import re
def replace_dots(str):
    return re.sub(r"\.", "-", str)

# Best practice:
#
# def replace_dots(string):
#     return string.replace('.', '-')

# Clever solution:
#
# import re
# def replace_dots(str):
#     return re.sub(r"\.", "-", str)