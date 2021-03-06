# Remove exclamation marks
#
# https://www.codewars.com/kata/57a0885cbb9944e24c00008e
#
# Write function RemoveExclamationMarks which removes all exclamation marks from a given string.

def remove_exclamation_marks(s):
    return s.replace("!", "")

# Best practice and clever solution:
#
# def remove_exclamation_marks(s):
#     return s.replace('!', '')
